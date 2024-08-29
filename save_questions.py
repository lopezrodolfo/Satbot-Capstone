import pymysql

connection = pymysql.connect(host= "satbot.ceylumpmaw0a.us-west-1.rds.amazonaws.com",
                            user="admin",
                            password= "satbot123",
                            db= "sb_intents")




def add_q_a_pair(question, answer, class_code):
    try:
        with connection.cursor() as cursor:
            sql = f"SELECT IFNULL(MAX(intent_id), 0) from intents;"
            cursor.execute(sql)
            result = cursor.fetchone()
            intent_id, *rest = result
            intent_id += 1

            sql = "INSERT INTO intents (`intent_id`,`class_id`,`intent`,`response`,`access_count`) VALUES (%s, %s, %s, %s, %s);"
            cursor.execute(sql, (intent_id, class_code, question, answer, 0))
            connection.commit()
            print("Q&A pair added successfully!")

    except Exception as e:
        print(f"Error adding Q&A pair: {e}")

if __name__ == '__main__':
    class_id = input('Please enter your class code: ')
    while True:
        inp = input('Would you like to insert a new question/answer pair? (y/n): ')
        if inp == 'y':
            question = input('Write your question here: ')
            answer = input('Write your answer here: ')
            add_q_a_pair(question, answer, int(class_id))
        elif inp == 'n':
            break
        else:
            pass
