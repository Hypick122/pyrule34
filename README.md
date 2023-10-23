PyRule34 ![GitHub](https://img.shields.io/github/license/Hypick122/pyrule34)
=============================
### <strong><a href="https://github.com/Hypick122/pyrule34/blob/master/.github/README_RU.md"> Русский </a> | English </strong>
This is a lightweight asynchronous library for the [rule34](rule34.xxx) API

Install [![Downloads](https://pepy.tech/badge/pyrule34)](https://pepy.tech/project/pyrule34)
-------------
The library requires Python 3.5 or higher
- Latest version on PyPI: [`1.1.0`](https://pypi.org/project/pyrule34/1.1.0/)
```sh
pip install -U pyrule34
```

Usage
-------------
Importing required libraries
```python
import asyncio
from pyrule34 import AsyncRule34
```
AsyncRule34 can be used as a context manager:
```python
#example
async def main():
    async with AsyncRule34() as r34:
        get_posts = await r34.get_posts(4931536)
        
        print(get_posts[0].tags)
        
loop = asyncio.get_event_loop()
loop.run_until_complete(main())
```

### Search
Search for posts using specified inclusion and exclusion tags.

Returns a list.

Parameters:
- `tags` - The include tags
- `exclude_tags` - The exclude tags (default: None)
- `limit` - The (maximum) limit to get posts. Maximum 1000 per one request (default: 100)
- `page_id` - The page number (default: 0)
```python
search = await r34.search(tags=["neko"], exclude_tags=["rating:general"], page_id=2, limit=1)
```
### Post
Retrieve post(s) by ID or MD5 hash.

Returns a list.

Parameters:
- `posts_id`: The list of IDs posts or post ID
- `md5`: The MD5 hash of the post (default: None)
```python
get_posts = await r34.get_posts(4931536)
```
### Comments on the post
Get comments by post ID.

Returns a list.

Parameters:
- `post_id`: The ID of the post
```python
get_post_comments = await r34.get_post_comments(4153825)
```
### Random post
Get a random post.

Returns a dict.
```python
get_random_post = await r34.get_random_post()
```
### Pool
Get Pool by ID.

Returns a list.

Parameters:
- `cid`: Pool ID
- `offset`: offset (default: 0) | 1 page - 45
```python
get_pool = await r34.get_pool(29619)
```
### User Favorites
Get user's favorites by ID.

Returns a list.

Parameters:
- `user_id`: user ID
- `offset`: offset (default: 0) | 1 page - 50
```python
favorite = await r34.users.favorites(2993217)
```
### Top 100 characters and tags
Get the top 100 characters or tags.

Returns a list.
```python
top_character = await r34.top_characters()
top_tags = await r34.top_tags()
```
### Top users
Get the top 10 best users by tags, comments, etc.

Returns a list.
```python
taggers = await r34.stats.taggers()
favorites = await r34.stats.favorites()
commenters = await r34.stats.commenters()
forum_posters = await r34.stats.forum_posters()
image_posters = await r34.stats.image_posters()
note_editors = await r34.stats.note_editors()
```
