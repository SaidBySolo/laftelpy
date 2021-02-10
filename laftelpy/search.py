from typing import Any, Optional

from laftelpy.results import Results


class Search:
    def __init__(self, **data) -> None:
        self.data = data
        self.__count = data.pop("count", None)
        self.__results = data.pop("results", [])
        self.__next = data.pop("next", None)

    def to_dict(self) -> dict[str, Any]:
        return {
            "count": self.count,
            "results": [result.to_dict() for result in self.results],
            "next": self.next,
        }

    @property
    def count(self) -> Optional[int]:
        """
        Return total
        """
        return self.__count

    @property
    def results(self) -> list[Results]:
        """
        Return results list
        """
        return [Results(**result) for result in self.__results]

    @property
    def next(self) -> Optional[str]:
        """
        Return next search url
        """
        return self.__next
