PyRule34 ![GitHub](https://img.shields.io/github/license/Hypick122/pyrule34)
=============================
### <strong>Русский | <a href="https://github.com/Hypick122/pyrule34/blob/master/README.md"> English </a></strong>
Это легкая асинхронная библиотека для API [rule34](rule34.xxx)

Установить [![Downloads](https://pepy.tech/badge/pyrule34)](https://pepy.tech/project/pyrule34)
-------------
Для библиотеки нужен Python 3.5 или выше
- Последняя версия на PyPI: [`1.1.0`](https://pypi.org/project/pyrule34/1.1.0/)
```sh
pip install -U pyrule34
```

Использование
-------------
Импортируем нужные библиотеки
```python
import asyncio
from pyrule34 import AsyncRule34
```
AsyncRule34 можно использовать в виде контекстого менеджера:
```python
#пример
async def main():
    async with AsyncRule34() as r34:
        get_posts = await r34.get_posts(4931536)
        
        print(get_posts[0].tags)
        
loop = asyncio.get_event_loop()
loop.run_until_complete(main())
```

### Поиск
Поиск постов по указанным тегам включения и исключения.

Возвращает список.

Параметры:
- `tags` - Включаемые теги
- `exclude_tags` - Теги исключения (по умолчанию: None)
- `limit` - (Максимальный) лимит на получение сообщений. Максимум 1000 за один запрос (по умолчанию: 100)
- `page_id` - Номер страницы (по умолчанию: 0)
```python
search = await r34.search(tags=["neko"], exclude_tags=["rating:general"], page_id=2, limit=1)
```
### Пост
Получить пост(ы) по ID или хэшу MD5.

Возвращает список.

Параметры:
- `posts_id`: Список ID постов или ID поста
- `md5`: Хэш MD5 поста (по умолчанию: None)
```python
get_posts = await r34.get_posts(4931536)
```
### Комментарии к посту
Получить комментарии по ID поста.

Возвращает список.

Параметры:
- `post_id`: ID поста
```python
get_post_comments = await r34.get_post_comments(4153825)
```
### Рандомный пост
Получить случайный пост.

Возвращает словарь.
```python
get_random_post = await r34.get_random_post()
```
### Пул
Получить пул по ID.

Возвращает список.

Параметры:
- `cid`: ID пула
- `offset`: смещение (по умолчанию: 0) | 1 страница - 45
```python
get_pool = await r34.get_pool(29619)
```
### Избранное пользователя
Получить избранное пользователя по ID

Возвращает список.

Параметры:
- `user_id`: ID пользователя
- `offset`: смещение (по умолчанию: 0) | 1 страница - 50
```python
favorite = await r34.users.favorites(2993217)
```
### Топ 100 персонажей и тегов
Получить 100 лучших персонажей или тегов.

Возвращает список.
```python
top_character = await r34.top_characters()
top_tags = await r34.top_tags()
```
### Топ пользователей
Получить топ 10 лучших пользователей по тегам, комментариям и т.п.

Возвращает список.
```python
taggers = await r34.stats.taggers()
favorites = await r34.stats.favorites()
commenters = await r34.stats.commenters()
forum_posters = await r34.stats.forum_posters()
image_posters = await r34.stats.image_posters()
note_editors = await r34.stats.note_editors()
```
