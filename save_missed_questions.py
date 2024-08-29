#Create a function that adds incorrect/missed questions to the database

import pymysql

connection = pymysql.connect(host = "satbot.ceylumpmaw0a.us-west-1.rds.amazonaws.com",
                             user = "admin",
                             password = "satbot123",
                             db = "sb_intents") 

print("Chat Section\n")

chat_text = input("What may I assist you with?\n")
estimated_intent = "NULL"


def insert_missed_questions():
    try:
        with connection.cursor() as cursor:
            sql = f"SELECT IFNULL(MAX(question_id),0) from incomplete_questions;"
            cursor.execute(sql)
            result = cursor.fetchone()
            question_id, *rest = result
            question_id += 1
            sql = f"INSERT INTO incomplete_questions (`question_id`, `estimated_intent`,`chat_text`) VALUES (%s, %s, %s);"
            cursor.execute(sql, (question_id, estimated_intent, chat_text))

        # Connection is not autocommit by default, so we must commit to save changes
        connection.commit()
        print(f'Successfully inserted records')
        
    except Exception as e:
        print(f'Error in insertion to MySQL database: {e}')

if __name__ == '__main__':
    insert_missed_questions()