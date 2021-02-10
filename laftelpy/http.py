from typing import Any

import aiohttp
from aiohttp.typedefs import LooseHeaders

from laftelpy.error import HTTPException


class LaftelRequester:
    def __init__(self, headers: LooseHeaders = {"laftel": "TeJava"}) -> None:
        self.headers = headers

    async def request(self, path: str, **kwargs):
        async with aiohttp.ClientSession(headers=self.headers) as cs:
            async with cs.get("https://laftel.net/api" + path, **kwargs) as r:
                if not r.status == 200:
                    raise HTTPException(f"Code: {r.status}, Message: {r.reason}")
                return await r.json()

    async def get_search(self, params: dict[str, Any]):
        return await self.request("/search/v1/keyword/", params=params)

    async def get_discover(self, params: dict[str, Any]):
        return await self.request(
            "/search/v1/discover/",
            params=dict(filter(lambda item: item[1] is not None, params.items())),
        )

    async def get_daily(self):
        return await self.request("/search/v2/daily/")
