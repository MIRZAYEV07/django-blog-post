import json
from collections import OrderedDict
from django.db import connection


def dictfetchall(cursor):
    desc = cursor.description
    return [
        dict(zip([col[0] for col in desc], row))
        for row in cursor.fetchall()
    ]


def dictfetchone(cursor):
    desc = cursor.description
    return dict(zip([col[0] for col in desc], cursor.fetchone()))


def get_blog(slug):
    with connection.cursor() as cursor:
        cursor.execute(f"""

                SELECT * ,post.slug FROM blogs_post as post
                INNER JOIN blogs_postlanguage as pl
                ON post.id = pl.post_id
                INNER JOIN blogs_language as l
                ON pl.language_id = l.id
                INNER JOIN blogs_category as ctg
                ON ctg.id = post.categories_id
                INNER JOIN auth_user as auth
                ON post.user_id = auth.id
                WHERE post.slug = '{slug}' 



        """)
        data = dictfetchone(cursor)

    return data


def get_my_blog(user_name):
    with connection.cursor() as cursor:
        cursor.execute(f"""

                SELECT * ,post.slug FROM blogs_post as post
                INNER JOIN blogs_postlanguage as pl
                ON post.id = pl.post_id
                INNER JOIN blogs_language as l
                ON pl.language_id = l.id
                INNER JOIN blogs_category as ctg
                ON ctg.id = post.categories_id
                INNER JOIN auth_user as auth
                ON post.user_id = auth.id
                WHERE auth.username = '{user_name}' 



        """)
        data = dictfetchall(cursor)

    return data


def get_blogs_all(key_word=None, keyword2=None):
    if key_word:
        search = f"WHERE post.title like '%{key_word}%' or post.title like '%{key_word}%' "
    else:
        search = ''
    with connection.cursor() as cursor:
        cursor.execute(f"""

                SELECT * ,post.slug  FROM blogs_post as post
                INNER JOIN blogs_postlanguage as pl
                ON post.id = pl.post_id
                INNER JOIN blogs_language as l
                ON pl.language_id = l.id
                INNER JOIN blogs_category as ctg
                ON ctg.id = post.categories_id
                INNER JOIN auth_user as auth
                ON post.user_id = auth.id
                {search}





        """)
        data = dictfetchall(cursor)

    return data