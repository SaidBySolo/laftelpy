from laftelpy.utils import check_arg, compare, convert_params, join_params
from laftelpy.typing import BRANDS, GENRES, MEDIUM, PRODUCTION, SORT, TAGS, YEARS
from typing import Optional
from aiohttp.typedefs import LooseHeaders
from laftelpy.search import Search
from laftelpy.http import LaftelRequester


class Client(LaftelRequester):
    def __init__(self, headers: Optional[LooseHeaders] = {"laftel": "TeJava"}) -> None:
        super().__init__(headers=headers)

    async def search(self, keyword: str):
        return Search(**await self.get_search({"keyword": keyword}))

    async def discover(
        self,
        sort: SORT = "rank",
        viewable: bool = True,
        svod: bool = False,
        genres: list[GENRES] = None,
        exclude_genres: list[GENRES] = None,
        tags: list[TAGS] = None,
        exclude_tags: list[TAGS] = None,
        years: list[YEARS] = None,
        ending: bool = None,
        production: list[PRODUCTION] = None,
        medium: list[MEDIUM] = None,
        brands: list[BRANDS] = None,
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
