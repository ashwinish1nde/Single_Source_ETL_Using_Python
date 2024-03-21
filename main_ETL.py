
from Utilities.helper_psql import init_logger, sql_connection, create_table
from Utilities.get_data import get_selfDev_members
import logging

if __name__ == '__main__':
    # Initialize logger
    init_logger()
    
    # Establish database connection and get cursor
    conn, cur = sql_connection()
    
    # Check if connection and cursor are valid
    if conn is not None and cur is not None:
        try:
            # Create table if it doesn't exist
            create_table(conn)
            
            # Call function to get and insert data
            get_selfDev_members(conn)
           
        finally:
            # Close cursor and connection
            cur.close()
            conn.close()
            logging.info("Connection and cursor closed.")
    else:
        logging.error("Failed to establish database connection.")
