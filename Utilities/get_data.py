import json
import logging
from Utilities.helper_psql import insert_member

def get_selfDev_members(psql_conn):
    # Reads data from data/data.json and adds it to PostgreSQL database 
    with open('data/data.json') as json_file:
        data = json.load(json_file)
        for member in data:
            logging.info(f"Processing member: {member.get('name', 'Unknown')}")  # Safe retrieval of name
            insert_member(psql_conn, {
                'discord_id': member.get('discord_id', ''),
                'name': member.get('name', ''),
                'age': member.get('age', ''),
                'pro_language': member.get('programming_language', ''),  # Change the key name to match your data
                'comment': member.get('comment', '')
            })
