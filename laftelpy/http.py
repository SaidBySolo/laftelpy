from typing import Any, Optional
import aiohttp
from aiohttp.typedefs import LooseHeaders


class LaftelRequester:
    def __init__(self, headers: Optional[LooseHeaders] = {"laftel": "TeJava"}) -> None:
        self.headers = headers

    async def request(self, path: str, **kwargs) -> dict[str, Any]:
        async with aiohttp.ClientSession(headers=self.headers) as cs:
            async with cs.get("https://laftel.net/api" + path, **kwargs) as r:
                print(r.url)
                return await r.json()

    @staticmethod
    def convert_params(param_value: Optional[bool]):
        if param_value is None:
            return
        else:
            return str(param_value).lower()

    async def get_search(self, keyword: str):
        data = await self.request(
            "/search/v1/keyword/", params={"keyword": keyword}, headers=self.headers
        )
        return data

    async def get_discover(
        self,
        sort: str = "rank",
        viewable: bool = True,
        svod: bool = None,
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
        params = {
            "sort": sort,
            "viewable": self.convert_params(viewable),
            "svod": self.convert_params(svod),
            "genres": genres,
            "exlude_genres": exclude_genres,
            "tags": tags,
            "years": years,
            "ending": self.convert_params(ending),
            "production": production,
            "medium": medium,
            "brands": brands,
            "size": size,
            "offset": offset,
        }

        data = await self.request(
            "/search/v1/discover/",
            headers=self.headers,
            params=dict(filter(lambda item: item[1] is not None, params.items())),
        )
        return data
