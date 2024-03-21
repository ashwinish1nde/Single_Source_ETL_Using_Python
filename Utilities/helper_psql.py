import logging
import psycopg2

def init_logger():
    try:
        logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
        logging.info("Program and Logger Start.")
    except Exception as e:
        print(f"An error occurred while initializing the logger: {e}")

def sql_connection():
    conn = None
    cur = None
    try:
        # Connect to PostgreSQL Database 
        logging.info("Connecting to PostgreSQL...") 
        conn = psycopg2.connect(host='localhost', database='DevCommunity', user='postgres', password='ENTER YOUR PASSWORD')
        logging.info("Connection successfull!")

        # Create Cursor 
        cur = conn.cursor()

        logging.info("PostgreSQL Database Version: ")
        cur.execute('SELECT version()')

        # Display the PostgreSQL database server version 
        db_version = cur.fetchone()
        logging.info(db_version)

        return conn, cur  # Return the connection and cursor objects separately

    except (Exception, psycopg2.DatabaseError) as error:
        logging.error(error)
        # Close the cursor if it was created
        if cur is not None:
            cur.close()
        # Close the connection if it was established
        if conn is not None:
            conn.close()
        return None, None  # Return None for both connection and cursor
   

def create_table(psql_conn):
    # Create a table in PostgreSQL database 
    q_create_table = """
        CREATE TABLE IF NOT EXISTS members (
        discord_id VARCHAR(500) PRIMARY KEY,
        name VARCHAR(255) NOT NULL,
        age INT8 NOT NULL,
        programming_language VARCHAR(255) NOT NULL,
        comment VARCHAR(500) NOT NULL
        );
    """
    try:
        cur = psql_conn.cursor()
        cur.execute(q_create_table)
        logging.info(f"Executed query: {q_create_table}")
        cur.close()
        psql_conn.commit()

    except (Exception, psycopg2.DatabaseError) as error:
        logging.error(error)

def insert_member(psql_conn, member):
    q_insert_member = """
        INSERT INTO members (discord_id, name, age, programming_language, comment)
        VALUES (%s, %s, %s, %s, %s);
    """
    try:
        cur = psql_conn.cursor()
        cur.execute(q_insert_member, (member['discord_id'], member['name'], member['age'], member['pro_language'], member['comment']))
        logging.info(f"Executed query: {q_insert_member}")
        cur.close()
        psql_conn.commit()

    except (Exception, psycopg2.DatabaseError) as error:
        logging.error(error)
