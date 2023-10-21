import aiohttp
from typing import Iterable, ClassVar
from bs4 import BeautifulSoup
import urllib.parse as urlparse
from urllib.parse import parse_qs

from .objects import *


class Users:
    def __init__(self, session, base_url, api_url):
        self.session = session
        self.url = base_url
        self.api_url = api_url

    async def user_favorite(
            self,
            user_id: Optional[int]
    ) -> None:
        url = self.url + f"?page=favorites&s=view&id={user_id}"
        raise RuntimeError("The function is not ready yet.")

    async def user_page(
            self,
            user_id: Optional[int]
    ) -> None:
        url = self.url + f"?page=account&s=profile&id={user_id}"
        raise RuntimeError("The function is not ready yet.")


class Stats:
    def __init__(self, session, base_url, api_url):
        self.session = session
        self.url = base_url
        self.api_url = api_url

    async def _get_stats(self, name: Optional[str] = None) -> List[R34Stats]:  # "Generator[R34Stats]"
        """
        Get the top users

        :param name: Top 10 taggers | Top 10 commenters | Top 10 forum posters | Top 10 image posters | Top 10 note editors | Top 10 favoriters
        :return: A list of top users
        """
        records = []
        async with self.session.get(self.url + "?page=stats") as response:
            tables = BeautifulSoup(await response.content.read(), features="html.parser").select(".toptencont > table")
            for table in tables:
                if table.select("thead > tr")[0].get_text(strip=True) == name:
                    for tr in table.find("tbody").find_all("tr"):
                        tds = tr.find_all("td")
                        records.append(R34Stats(tds[0].get_text(strip=True), tds[1].get_text(strip=True), tds[2].get_text(strip=True)))

        return records

    def taggers(self):
        return self._get_stats("Top 10 taggers")

    def commenters(self):
        return self._get_stats("Top 10 commenters")

    def forum_posters(self):
        return self._get_stats("Top 10 forum posters")

    def image_posters(self):
        return self._get_stats("Top 10 image posters")

    def note_editors(self):
        return self._get_stats("Top 10 note editors")

    def favorites(self):
        return self._get_stats("Top 10 favoriters")


class AsyncRule34:
    BASE_URL: ClassVar[str] = f"https://rule34.xxx/index.php"
    BASE_API_URL: ClassVar[str] = "https://api.rule34.xxx/index.php?page=dapi&q=index&json=1"

    def __init__(self):
        self.session = aiohttp.ClientSession()
        self.url = AsyncRule34.BASE_URL
        self.api_url = AsyncRule34.BASE_API_URL

        self.stats = Stats(self.session, self.url, self.api_url)
        self.users = Users(self.session, self.url, self.api_url)

    async def search(
            self,
            tags: Iterable[str],
            exclude_tags: Iterable[str] = None,
            limit: Optional[int] = 100,
            page_id: Optional[int] = 0,
    ) -> List[R34Post]:
        """
        Search for posts using specified inclusion and exclusion tags.

        :param tags: The include tags
        :param exclude_tags: The exclude tags
        :param limit: The (maximum) limit to get posts. Maximum 1000 per one request
        :param page_id: The page number
        :return: A list of posts
        """
        # if 0 > limit > 1000:
        url = self.api_url + '&tags=' + self._format_tags(tags, exclude_tags) + f'&limit={limit}&s=post'

        if page_id:
            url += f"&pid={page_id}"

        async with self.session.get(url) as response:
            json = (await response.json())

        if json is None:
            return []

        return list([R34Post.from_json(post) for post in json])

    async def get_post(
            self,
            posts_id: Optional[Union[list, int]],
            md5: Optional[str] = None
    ) -> List[R34Post]:
        """
        Get a post by ID or MD5 hash.

        :param posts_id: The list of IDs posts or post ID
        :param md5: The MD5 hash of the post
        :return: A list of post(s)
        """
        if isinstance(posts_id, int):
            posts_id = [posts_id]

        if (posts_id and md5) or (not posts_id and not md5):
            raise ValueError("You must specify the post(s) ID or md5, but not both.")

        posts = []

        for post_id in posts_id:
            url = (self.api_url + '&s=post' + (f'&tags=md5:{md5}' if md5 else f'&id={post_id}'))
            async with self.session.get(url) as response:
                for post in await response.json():
                    res = R34Post.from_json(post)
                    posts.extend([f"md5 post (post_id: {post_id}) != md5"] if md5 and res.md5 != md5 else list([res]))

        return posts

    async def get_pool(self) -> None:
        url = self.url + "?page=pool&s=show&id={page_id}"
        raise RuntimeError("The function is not ready yet.")

    async def get_post_comments(
            self,
            post_id: Optional[int],
            # md5: Optional[str] = None
    ) -> list[R34PostComment]:
        """
        Get a comments by post ID.

        :param post_id: The ID of the post
        :return: A list of comments
        """
        url = self.api_url + f"&s=comment&post_id={post_id}"  # returns: XML

        async with self.session.get(url) as response:
            bfs_raw = BeautifulSoup(await response.content.read(), features="xml")
            res_xml = bfs_raw.comments.findAll('comment')

            return [R34PostComment(**dict(comment.attrs)) for comment in res_xml]

    async def get_random_post(self) -> List[R34Post]:
        """
        Get a random post

        :return: A dict of random post
        """
        url = self.url + "?page=post&s=random"

        async with self.session.get(url) as response:
            parsed = urlparse.urlparse(str(response.url))

            return await self.get_post(int(parse_qs(parsed.query)['id'][0]))

    # search_tags, get_tag

    async def top_characters(self) -> List[R34TopCharacters]:
        """
        Get a list of top 100 characters

        :return: A list of characters
        """
        url = self.url + "?page=icame"

        async with self.session.get(url) as response:
            bfs_raw = BeautifulSoup(await response.content.read(), features="html.parser")
            rows = bfs_raw.find("table", border=1).find("tbody").find_all("tr")

            return [R34TopCharacters(row.select('td > a', href=True)[0].get_text(strip=True), row.select('td')[1].get_text(strip=True)) for row in rows if row]

    async def top_tags(self) -> List[R34TopTag]:
        """
        Get a list of top 100 tags

        :return: A list of tags
        """
        url = self.url + "?page=toptags"

        async with self.session.get(url) as response:
            bfs_raw = BeautifulSoup(await response.content.read(), features="html.parser")
            rows = bfs_raw.find("table", class_="server-assigns").find_all("tr")[2:]

            return [R34TopTag(rank=tag[0].string[1:], name=tag[1].string, percentage=tag[2].string[:-1]) for tag in (row.find_all("td") for row in rows)]

    @staticmethod
    def _format_tags(include_tags: Iterable[str], exclude_tags: Iterable[str] = None) -> str:
        format_tag = lambda tag, sign: sign + tag.strip().lower().replace(" ", "")

        include = "+".join(format_tag(tag, "") for tag in include_tags)
        exclude = "+".join(format_tag(tag, "-") for tag in exclude_tags) if exclude_tags else ""

        return include + "+" + exclude

    async def __aenter__(self):
        return self

    async def __aexit__(self, exc_type, val, tb):
        await self.session.close()

    async def close(self):
        await self.session.close()
