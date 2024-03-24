from psycopg2.extras import execute_values
import pandas as pd
import psycopg2
from psycopg2.extras import execute_values
import os
from dotenv import load_dotenv
# from dataclasses import dataclass

load_dotenv()

user_postegress = os.getenv("POSTGRES_USER")
pass_postegress = os.getenv("POSTGRES_PASSWORD")
host_postegress = os.getenv("PGHOST")
db_postegress = os.getenv("POSTGRES_DB")
port = 5432

class PostgresDb:

  def __init__(self, host, database, user,  password, port):
    self.host = host
    self.database = database
    self.user = user  
    self.password = password
    self.port = port

  def connect(self):
    self.conn = psycopg2.connect(
        host=self.host,
        database=self.database, 
        user=self.user,
        password=self.password,
        port = self.port
    )

  def create_update_table(self, df, table_name):
    
    columns = {
        "artist_id": "VARCHAR(255)",
        "name_artist": "VARCHAR(255)",
        "top10_rank": "INTEGER",
        "song_name": "VARCHAR(255)", 
        "song_id": "VARCHAR(255)",
        "album_name": "VARCHAR(255)",
        "album_id": "VARCHAR(255)",
        "release_date": "DATE"
    }

    try:
      cursor = self.conn.cursor()

      # Create table
      cols_str_sql = ','.join([f'"{col}" {data_type}' for col, data_type in columns.items()])
      create_table_sql = f"CREATE TABLE IF NOT EXISTS {table_name} ({cols_str_sql})"
      cursor.execute(create_table_sql)

      # INSERT/UPDATE INTO TABLE
      for _, row in df.iterrows():

        select_sql = f"SELECT song_id FROM {table_name} WHERE song_id = '{row['song_id']}'"

        cursor.execute(select_sql)
        result = cursor.fetchone()

        if result:
          update_table = f"""
            UPDATE {table_name} SET
                name_artist = '{row['name_artist']}',
                top10_rank = {row['top10_rank']},
                song_name = '{row['song_name']}', 
                album_name = '{row['album_name']}',
                album_id = '{row['album_id']}', 
                release_date = '{row['release_date']}'
            WHERE song_id = '{row['song_id']}'
        """
          
          cursor.execute(update_table)

        else:
           # Formating values
            values = [tuple(row[col] for col in columns)]
            value_rows = [str(tuple(x)) for x in values]

            # Query INSERT
            insert_sql = f"INSERT INTO {table_name} ({', '.join(columns)}) VALUES {', '.join(value_rows)}"
            cursor.execute(insert_sql)

     
      self.conn.commit()
      cursor.close()
      self.conn.close()

    except:
      self.conn.rollback()
      cursor.close()
      self.conn.close()
      raise Exception("Error into create or insert data into PostgreSQL.")
    
    
  def run_query(self, query):
    cursor = self.conn.cursor() 
    cursor.execute(query)
    records = cursor.fetchall()
    cols = [desc[0] for desc in cursor.description]
    cursor.close()

    return records, cols


