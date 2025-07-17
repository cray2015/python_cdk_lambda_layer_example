import psycopg2
import os

def lambda_handler(event, context):
    conn = psycopg2.connect(
        host=os.environ["DB_HOST"],
        dbname=os.environ["DB_NAME"],
        user=os.environ["DB_USER"],
        password=os.environ["DB_PASSWORD"],
        port=5432
    )
    cur = conn.cursor()
    cur.execute("SELECT version();")
    version = cur.fetchone()
    cur.close()
    conn.close()

    return {
        "statusCode": 200,
        "body": f"PostgreSQL version: {version}"
    }
