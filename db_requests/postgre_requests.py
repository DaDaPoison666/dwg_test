import psycopg2


class Db:
    def __enter__(self):
        self.connection = psycopg2.connect(
            host="localhost",
            database="bwg",
            user="postgres",
            password="qasergyuj",
            port="5432")
        self.cursor = self.connection.cursor()
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.cursor.close()
        self.connection.close()

    def select_name_query(self):
        select_query = "SELECT first_name, last_name FROM celebrities"
        self.cursor.execute(select_query)
        query = self.cursor.fetchall()
        return query

    def update_table(self, first_name, last_name, link='null', state='false'):
        update_query = (
            f"UPDATE celebrities SET updated_at = CURRENT_DATE, in_wiki = {state}, wiki_link = '{link}'"
            f"WHERE first_name = '{first_name}'AND last_name = '{last_name} '"
        )
        self.cursor.execute(update_query)
        self.connection.commit()
