from pyrule34 import AsyncRule34
import asyncio


async def main():
    async with AsyncRule34() as r34:
        search = await r34.search(["neko"], page_id=0, limit=-10)
        get_posts = await r34.get_posts(4931536, md5="7970c13cfd503ff23c82ee2d208c795c")
        get_pool = await r34.get_pool(29619)
        get_post_comments = await r34.get_post_comments(4153825)
        get_random_post = await r34.get_random_post()
        top_character = await r34.top_characters()
        top_tags = await r34.top_tags()

        print("search: ", search[0].hash)
        print("get_post: ", get_posts[0].hash)
        print("get_pool: ", get_pool[0].id)
        print("get_post_comments: ", get_post_comments)
        print("get_random_post: ", get_random_post)
        print("top_character: ", top_character)
        print("top_tags: ", top_tags, end="\n")

        taggers = await r34.stats.taggers()
        favorites = await r34.stats.favorites()
        commenters = await r34.stats.commenters()
        forum_posters = await r34.stats.forum_posters()
        image_posters = await r34.stats.image_posters()
        note_editors = await r34.stats.note_editors()

        print("taggers: ", taggers)
        print("favorites: ", favorites)
        print("commenters: ", commenters)
        print("forum_posters: ", forum_posters)
        print("image_posters: ", image_posters)
        print("note_editors: ", note_editors)

        favorite = await r34.users.favorites(2993217, offset=0)
        print("favorite: ", favorite)
        # profile = await r34.users.info(2993217)
        # print(profile)

        # tasks = [s async for s in r34.stats.taggers()]


loop = asyncio.get_event_loop()
loop.run_until_complete(main())
