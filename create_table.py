import psycopg2

def main():
    connection = psycopg2.connect(
        host="localhost",
        database="mydatabase",
        user="postgres",
        password="secret",
        port="5432"
    )

    cursor = connection.cursor()

    create_table_query = """
    CREATE TABLE IF NOT EXISTS chunks (
        chunk_id INTEGER PRIMARY KEY,
        text TEXT NOT NULL,
        page_range INT[2] NOT NULL,
        line_range INT[2] NOT NULL,
        filename TEXT NOT NULL,
        embedding VECTOR NOT NULL,
    );
    """
    cursor.execute(create_table_query)
    connection.commit()
    cursor.close()
    connection.close()

if __name__ == "__main__":
    main()
