from typing import Optional, List, Union
from dataclasses import dataclass


@dataclass(init=True, frozen=True)
class R34Post:
    raw: Optional[dict]  # Iterable
    preview_url: Optional[str]
    sample_url: Optional[str]
    file_url: Optional[str]
    file_type: Optional[str]
    directory: Optional[int]
    hash: Optional[str]
    width: Optional[int]
    height: Optional[int]
    id: Optional[int]
    image: Optional[str]
    change: Optional[int]
    owner: Optional[str]
    parent_id: Union[str, int]
    rating: Optional[str]
    sample: Optional[bool]
    sample_height: Optional[int]
    sample_width: Optional[int]
    score: Optional[int]
    tags: List[str]
    source: Optional[str]
    status: Optional[str]
    has_notes: Optional[bool]
    comment_count: Optional[int]

    @staticmethod
    def from_json(json):
        pFileUrl = json["file_url"]
        file_type = "video" if pFileUrl.endswith(".mp4") else "gif" if pFileUrl.endswith(".gif") else "image"

        return R34Post(
            json,
            json["preview_url"],
            json["sample_url"],
            json["file_url"],
            file_type,
            json["directory"],
            json["hash"],
            json["width"],
            json["height"],
            json["id"],
            json["image"],
            json["change"],
            json["owner"],
            json["parent_id"],
            json["rating"],
            json["sample"],
            json["sample_height"],
            json["sample_width"],
            json["score"],
            json["tags"].split(" "),
            json["source"],
            json["status"],
            json["has_notes"],
            json["comment_count"],
        )


@dataclass(init=True, frozen=True)
class R34PostComment:
    created_at: Optional[str]
    post_id: Optional[int]
    body: Optional[str]
    creator: Optional[str]
    id: Optional[int]
    creator_id: Optional[int]


@dataclass(init=True, frozen=True)
class R34Stats:
    place: Optional[str]
    amount: Optional[int]
    username: Optional[str]


@dataclass(init=True, frozen=True)
class R34TopCharacters:
    name: Optional[str]
    # url = Optional[str]
    count: Optional[int]

    @property
    def url(self) -> Optional[str]:
        return "https://rule34.xxx/index.php?page=post&s=list&tags={0}".format(self.name.replace(" ", "_"))


@dataclass(init=True, frozen=True)
class R34TopTag:
    rank: Optional[int]
    name: Optional[str]
    percentage: Optional[int]

    @staticmethod
    def from_dict(dct: Optional[dict]):
        return R34TopTag(
            dct["rank"],
            dct["tagname"],
            dct["percentage"] * 100
        )
