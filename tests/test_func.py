from pyrule34 import AsyncRule34
import asyncio


async def main():
    async with AsyncRule34() as r34:
        search = await r34.search(["neko"], page_id=2, limit=1)
        get_post = await r34.get_post(4931536)
        # get_pool = await r34.get_pool()
        get_post_comments = await r34.get_post_comments(4153825)
        get_random_post = await r34.get_random_post()
        top_character = await r34.top_characters()
        top_tags = await r34.top_tags()

        print("search: ", search)
        print("get_post: ", get_post[0].raw)
        # print("get_pool: ", get_pool)
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

        # tasks = [s async for s in r34.stats.taggers()]


loop = asyncio.get_event_loop()
loop.run_until_complete(main())
