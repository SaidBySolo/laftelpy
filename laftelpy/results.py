from typing import Any, Optional


class Results:
    def __init__(self, **data: Any) -> None:
        self.data = data
        self.__id = data.pop("id", None)
        self.__name = data.pop("name", None)
        self.__img = data.pop("img", None)
        self.__cropped_img = data.pop("cropped_img", None)
        self.__home_img = data.pop("home_img", None)
        self.__home_cropped_img = data.pop("home_cropped_img", None)
        self.__is_adult = data.pop("is_adult", None)
        self.__genres = data.pop("genres", [])
        self.__medium = data.pop("medium", None)
        self.__distributed_air_time = data.pop("distributed_air_time", None)
        self.__is_laftel_only = data.pop("is_laftel_only", False)
        self.__is_uncensored = data.pop("is_uncensored", False)
        self.__is_dubbed = data.pop("is_dubbed", False)
        self.__is_avod = data.pop("is_avod", False)
        self.__is_viewing = data.pop("is_viewing", False)
        self.__latest_episode_created = data.pop("latest_episode_created", None)

    def to_dict(self) -> dict[str, Any]:
        return {
            "id": self.id,
            "name": self.name,
            "img": self.cropped_img,
            "cropped_img": self.cropped_img,
            "home_img": self.home_img,
            "home_cropped_img": self.home_cropped_img,
            "is_adult": self.is_adult,
            "genres": self.genres,
            "medium": self.medium,
            "distributed_air_time": self.distributed_air_time,
            "is_laftel_only": self.is_laftel_only,
            "is_uncensored": self.is_uncensored,
            "is_dubbed": self.is_dubbed,
            "is_avod": self.is_avod,
            "is_viewing": self.is_viewing,
            "latest_episode_created": self.latest_episode_created,
        }

    @property
    def id(self) -> Optional[str]:
        """
        Return laftel id
        """
        return self.__id

    @property
    def name(self) -> Optional[str]:
        """
        Return anime name
        """
        return self.__name

    @property
    def img(self) -> Optional[str]:
        return self.__img

    @property
    def cropped_img(self) -> Optional[str]:
        return self.__cropped_img

    @property
    def home_img(self) -> Optional[str]:
        return self.__home_img

    @property
    def home_cropped_img(self) -> Optional[str]:
        return self.__home_cropped_img

    @property
    def is_adult(self) -> Optional[bool]:
        return self.__is_adult

    @property
    def genres(self) -> list[str]:
        return self.__genres

    @property
    def medium(self) -> Optional[str]:
        return self.__medium

    @property
    def distributed_air_time(self) -> Optional[str]:
        return self.__distributed_air_time

    @property
    def is_laftel_only(self) -> Optional[bool]:
        return self.__is_laftel_only

    @property
    def is_uncensored(self) -> Optional[bool]:
        return self.__is_uncensored

    @property
    def is_dubbed(self) -> Optional[bool]:
        return self.__is_dubbed

    @property
    def is_avod(self) -> Optional[bool]:
        return self.__is_avod

    @property
    def is_viewing(self) -> Optional[bool]:
        return self.__is_viewing

    @property
    def latest_episode_created(self) -> Optional[str]:
        return self.__latest_episode_created
