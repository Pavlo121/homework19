from django.db import connection

def get_user(email):
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM user WHERE email = %s", [email])
        return cursor.fetchone()

