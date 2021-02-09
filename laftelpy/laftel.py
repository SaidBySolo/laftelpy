from typing import Optional
from aiohttp.typedefs import LooseHeaders
from laftelpy.search import Search
from laftelpy.http import LaftelRequester


class Client(LaftelRequester):
    def __init__(self, headers: Optional[LooseHeaders] = {"laftel": "TeJava"}) -> None:
        super().__init__(headers=headers)

    async def search(self, keyword: str):
        return Search(**(await self.get_search(keyword)))

    # TODO: Typing
    async def discover(
        self,
        sort: str = "rank",
        viewable: bool = True,
        svod: bool = False,
        genres: str = None,
        exclude_genres: str = None,
        tags: str = None,
        years: str = None,
        ending: bool = None,
        production: str = None,
        medium: str = None,
        brands: str = None,
        size: int = 20,
        offset: int = 20,
    ):
        return Search(
            **(
                await self.get_discover(
                    sort,
                    viewable,
                    svod,
                    genres,
                    exclude_genres,
                    tags,
                    years,
                    ending,
                    production,
                    medium,
                    brands,
                    size,
                    offset,
                )
            )
        )
