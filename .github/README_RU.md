<div align="center">
  <h1>PyRule34</h1>
  
  **Это легкая асинхронная библиотека для API <a href="https://rule34.xxx">rule34</a>**
  
  <p><strong>
      <a href="/README.md">English</a>
      ·
      Русский
    </strong></p>
    
  <!--https://img.shields.io/badge/License-GPL_3.0-<COLOR>.svg?style=for-the-badge-->
  <a>[![GitHub - Лицензия](https://img.shields.io/github/license/Hypick122/pyrule34.svg?style=for-the-badge&color=light-green)](https://github.com/Hypick122/pyrule34/blob/master/LICENSE)</a>
  <br>
  <a>[![PyPI - Версия](https://img.shields.io/pypi/v/pyrule34?color=blue&style=for-the-badge&logo=pypi&logoColor=white)](https://pypi.org/project/pyrule34)</a>
  <a>[![PyPI - Установки](https://img.shields.io/pypi/dm/pyrule34?style=for-the-badge&color=blue)](https://pepy.tech/project/pyrule34)</a>
  <br>
  <a>[![Python - Версия](https://img.shields.io/badge/PYTHON-3.5+-red?style=for-the-badge&logo=python&logoColor=white)](https://pepy.tech/project/pyrule34)</a>
  <!--[![PyPI status](https://img.shields.io/pypi/status/pyrule34.svg?style=for-the-badge)](https://pypi.python.org/pypi/pyrule34)-->
  <!--https://img.shields.io/pypi/pyversions/pyrule34.svg?style=for-the-badge-->
</div>

## Оглавление

- [Начиная](#начиная)
  - [Установить с помощью PyPI](#установить-с-помощью-pypi)
  - [Клонировать репозиторий](#клонировать-репозиторий)
- [Использование](#использование)
  - [Search](#поиск)
  - [Получить пост](#получить-пост)
  - [Комментарии к посту](#комментарии-к-посту)
  - [Рандомный пост](#рандомный-пост)
  - [Пул](#пул)
  - [Избранное пользователя](#избранное-пользователя)
  - [Топ 100 персонажей и тегов](#топ-100-персонажей-и-тегов)
  - [Топ пользователей](#топ-пользователей)

## Начиная

##### Установить с помощью PyPI

```
pip install -U pyrule34
```

или

##### Клонировать репозиторий

```
git clone https://github.com/Hypick122/pyrule34.git
```

2. Установите необходимые пакеты Python:

```
pip install -U aiohttp, beautifulsoup4, lxml
```

3. Создайте .py файл и импортируете необходимые библиотеки:

```python
import asyncio
from pyrule34 import AsyncRule34
```

## Использование


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

### Получить пост

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
