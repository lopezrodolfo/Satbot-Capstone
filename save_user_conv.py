import pymysql
from getpass import getpass
from datetime import datetime

connection = pymysql.connect(host = "satbot.ceylumpmaw0a.us-west-1.rds.amazonaws.com",
                             user = "admin",
                             password = "satbot123",
                             db = "sb_users") 

username = input("Please enter your username: ")
password = getpass("Please enter your password: ")
class_name = input("Please enter the name of the class here: ")

"""
TODO:
1) Connect to the user DB and retrieve user ID

2) Connect to class DB and retrieve class ID from class_name
"""


def insert_conversation_records(text):
    try:
        with connection.cursor() as cursor:
            sql = f"SELECT IFNULL(MAX(chat_id), 0) from {username+'_log'};"
            cursor.execute(sql)
            result = cursor.fetchone()
            chat_id, *rest = result
            chat_id += 1
            sql = f"INSERT INTO {username+'_log'} (`chat_id`, `text`, `sender`, `class_code`, `timestamp`) \
                                           VALUES (%s, %s, %s, %s, %s);"
            cursor.execute(sql, (chat_id, text, username, class_name, datetime.now()))

        # Connection is not autocommit by default, so we must commit to save changes
        connection.commit()
        print(f'Successfully inserted records')
        
    except Exception as e:
        print(f'Error in insertion to MySQL database: {e}')

if __name__ == '__main__':
    while True:
        inp = input('Would you like to talk to the chatbot? (y/n): ')
        if inp == 'y':
            text = input('Input text: ')
            insert_conversation_records(text)
        elif inp == 'n':
            break
        else:
            pass