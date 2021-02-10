from laftelpy.utils import check_arg, compare, convert_params, join_params
from laftelpy.typing import BRANDS, GENRES, MEDIUM, PRODUCTION, SORT, TAGS, YEARS
from typing import Optional
from aiohttp.typedefs import LooseHeaders
from laftelpy.search import Search
from laftelpy.http import LaftelRequester


class Client(LaftelRequester):
    def __init__(self, headers: LooseHeaders = {"laftel": "TeJava"}) -> None:
        super().__init__(headers=headers)

    async def search(self, keyword: str):
        return Search(**await self.get_search({"keyword": keyword}))

    async def discover(
        self,
        sort: SORT = "rank",
        viewable: Optional[bool] = None,
        svod: Optional[bool] = None,
        genres: Optional[list[GENRES]] = None,
        exclude_genres: Optional[list[GENRES]] = None,
        tags: Optional[list[TAGS]] = None,
        exclude_tags: Optional[list[TAGS]] = None,
        years: Optional[list[YEARS]] = None,
        ending: Optional[bool] = None,
        production: Optional[list[PRODUCTION]] = None,
        medium: Optional[list[MEDIUM]] = None,
        brands: Optional[list[BRANDS]] = None,
        size: int = 20,
        offset: int = 20,
    ):
        if genres and exclude_genres:
            compare(genres, exclude_genres)

        if tags and exclude_tags:
            compare(tags, exclude_tags)

        check_arg(self.discover, locals())

        params = {
            "sort": sort,
            "viewable": convert_params(viewable),
            "svod": convert_params(svod),
            "genres": genres,
            "exlude_genres": exclude_genres,
            "tags": tags,
            "exclude_tags": exclude_tags,
            "years": years,
            "ending": convert_params(ending),
            "production": production,
            "medium": medium,
            "brands": brands,
            "size": size,
            "offset": offset,
        }

        return Search(**await self.get_discover(join_params(params)))
