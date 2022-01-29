import dbcreds
import mariadb as db


class BlogActions:

    def view_blog():
        conn = db.connect(user=dbcreds.user,
                          password=dbcreds.password,
                          host=dbcreds.host,
                          port=dbcreds.port,
                          database=dbcreds.database)
        cursor = conn.cursor()

        cursor.execute(
            f"select content from blog_post bp")
        blog_posts = cursor.fetchall()

        cursor.close()
        conn.close()

        for blog_post in blog_posts:
            print(blog_post[0])

    def submit_blog(username):
        conn = db.connect(user=dbcreds.user,
                          password=dbcreds.password,
                          host=dbcreds.host,
                          port=dbcreds.port,
                          database=dbcreds.database)
        cursor = conn.cursor()

        blog_post = input('write your post: ')

        cursor.execute(f'insert into blog_post(username, content) values("{username}","{blog_post}")')
        conn.commit()

        cursor.close()
        conn.close()