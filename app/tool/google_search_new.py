import asyncio
import itertools
from typing import List

from googlesearch import search

from app.tool.base import BaseTool


class GoogleSearch(BaseTool):
    name: str = "google_search"
    description: str = """Perform a Google search and return a list of relevant links.
Use this tool when you need to find information on the web, get up-to-date data, or research specific topics.
The tool returns a list of URLs that match the search query.
"""
    parameters: dict = {
        "type": "object",
        "properties": {
            "query": {
                "type": "string",
                "description": "(required) The search query to submit to Google.",
            },
            "num_results": {
                "type": "integer",
                "description": "(optional) The number of search results to return. Default is 10.",
                "default": 10,
            },
        },
        "required": ["query"],
    }

    async def execute(self, query: str, num_results: int = 10) -> List[str]:
        try:
            num_results = int(num_results)
        except Exception:
            num_results = 10

        loop = asyncio.get_event_loop()
        links = await loop.run_in_executor(
            None, lambda: list(itertools.islice(search(query), num_results))
        )
        return links
