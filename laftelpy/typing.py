from typing import Literal, Optional, TypedDict, Union


class ResultsDict(TypedDict):
    id: str
    name: str
    img: str
    cropped_img: str
    home_img: str
    home_cropped_img: str
    is_adult: bool
    genres: list[str]
    medium: str
    distributed_air_time: str
    is_laftel_only: bool
    is_uncensored: bool
    is_dubbed: bool
    is_avod: bool
    is_viewing: bool
    latest_episode_created: bool


class SearchDict(TypedDict):
    count: int
    results: list[ResultsDict]
    next: str


SORT = Literal["rank", "name", "recent", "cnt_eval", "avg_rating"]

GENRES = Literal[
    "판타지",
    "로맨스",
    "액션",
    "순정",
    "하렘",
    "BL",
    "개그",
    "일상",
    "SF",
    "스포츠",
    "스릴러",
    "모험",
    "백합",
    "치유",
    "음악",
    "아이돌",
    "음식",
    "마법소녀",
    "추리",
    "범죄",
    "시대물",
    "재난",
    "메카닉",
    "공포",
    "무협",
    "성인",
    "아동",
]

TAGS = Literal[
    "먼치킨",
    "이세계",
    "역하렘",
    "학교",
    "게임",
    "동양풍",
    "얀데레",
    "츤데레",
    "두뇌유희",
    "슬픔",
    "멘붕",
    "뱀파이어",
    "요괴 및 괴물",
    "시공이동",
    "디스토피아",
    "가족",
    "육아",
    "회사",
    "야구",
    "농구",
    "축구",
    "따뜻",
    "대학교",
    "열혈",
    "도박",
    "자전거",
    "잔인",
    "범죄",
    "정치",
    "왕권다툼",
    "철학적",
    "패션",
    "사랑과 우정 사이",
    "감염 및 좀비",
    "4차원 개그",
    "성장",
    "우주",
    "소꿉친구",
    "삼각관계",
    "남장여자",
    "복수",
    "연예인",
    "퇴마",
    "막장",
    "신분차이",
    "주체적 여성",
    "남매",
    "밀리터리",
    "역사",
    "건담 비우주세기",
    "여장남자",
    "오타쿠",
    "성전환",
    "서양풍",
    "추리",
    "풀 3D",
    "외모지상주의",
    "왕궁 및 성",
    "동물",
    "선생님",
    "나이차 큼",
    "건담 우주세기",
    "배틀",
    "미스테리",
    "현실적",
    "비판적",
    "무거움",
    "춤",
    "치유",
]


YEARS = Literal[
    "2021년 1분기",
    "2020년 4분기",
    "2020년 3분기",
    "2020년 2분기",
    "2020년 1분기",
    "2019년 4분기",
    "2019년 3분기",
    "2019년 2분기",
    "2019년 1분기",
    "2018년 4분기",
    "2018년 3분기",
    "2018년 2분기",
    "2018년 1분기",
    "2017년 4분기",
    "2017년 3분기",
    "2010년대",
    "2000년대",
    "1990년대",
    "1990년대 이전",
]

PRODUCTION = Literal[
    "본즈",
    "쿄토애니메이션",
    "매드하우스",
    "A-1Pictures",
    "유포테이블",
    "WitStudio",
    "프로덕션 I.G",
    "P.A.Works",
    "J.C.Staff",
    "샤프트",
    "동화공방",
    "스튜디오 딘",
    "실버 링크",
    "스튜디오 피에로",
    "MAPPA",
    "화이트폭스",
    "라르케",
    "트리거",
    "폴리곤 픽쳐스",
    "사테라이트",
]

MEDIUM = Literal["TVA", "극장판", "OVA"]

BRANDS = Literal["애니맥스 플러스", "애니플러스", "KTH", "대원", "카툰 네트워크", "기타"]

CompareList = Union[list[GENRES], list[TAGS]]

SearchParameters = dict[
    str,
    Optional[
        Union[
            str,
            list[GENRES],
            list[TAGS],
            list[YEARS],
            list[PRODUCTION],
            list[MEDIUM],
            list[BRANDS],
        ]
    ],
]
