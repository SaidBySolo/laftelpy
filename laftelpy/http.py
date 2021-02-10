from laftelpy.error import HTTPException
from typing import Any
import aiohttp
from aiohttp.typedefs import LooseHeaders


class LaftelRequester:
    def __init__(self, headers: LooseHeaders = {"laftel": "TeJava"}) -> None:
        self.headers = headers

    async def request(self, path: str, **kwargs) -> dict[str, Any]:
        async with aiohttp.ClientSession(headers=self.headers) as cs:
            async with cs.get("https://laftel.net/api" + path, **kwargs) as r:
                if not r.status == 200:
                    raise HTTPException(f"Code: {r.status}, Message: {r.reason}")
                return await r.json()

    async def get_search(self, params: dict[str, Any]):
        return await self.request(
            "/search/v1/keyword/", params=params, headers=self.headers
        )

    async def get_discover(self, params: dict[str, Any]):
        return await self.request(
            "/search/v1/discover/",
            headers=self.headers,
            params=dict(filter(lambda item: item[1] is not None, params.items())),
        )
