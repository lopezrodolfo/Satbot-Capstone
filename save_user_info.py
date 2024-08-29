import pymysql
from getpass import getpass


connection = pymysql.connect(host = "satbot.ceylumpmaw0a.us-west-1.rds.amazonaws.com",
                             user = "admin",
                             password = "satbot123",
                             db = "sb_users") 


print("Personal Information Section\n")
firstName = input("Please enter your first name: ")
lastName = input("Please enter your last name: ")
email = input("Please enter your USD email address: ")
classCode = input("Please enter your class code: ")

print("Account Creation Seciton\n")
username = input("Please enter your username: ")

match = False
password = getpass("Please enter your password: ")
verify = getpass("Re Enter your password to verify: ")
while not match:
    if verify == password:
        match = True
    else:
        print("Passwords did not match")
        password = getpass("Please enter your password: ")
        verify = getpass("Re Enter your password to verify: ")


def insert_conversation_records():
    try:
        with connection.cursor() as cursor:
            sql = f"SELECT MAX(user_id) from user_master;"
            cursor.execute(sql)
            result = cursor.fetchone()
            user_id, *rest = result
            user_id += 1
            sql = f"INSERT INTO user_master (`user_id`, `username`, `password`, `first_name`, `last_name`, `email`, `classes`, `conversation_log`) \
                                           VALUES (%s, %s, %s, %s, %s, %s, %s, %s);"
            cursor.execute(sql, (user_id, username, password, firstName, lastName, email, classCode, username + '_log'))

            sql = f"CREATE TABLE {username+'_log'} (chat_id int, text longtext, sender varchar(255), class_code varchar(255), timestamp datetime);"
            cursor.execute(sql)

        # Connection is not autocommit by default, so we must commit to save changes
        connection.commit()
        print(f'Successfully inserted records')
        
    except Exception as e:
        print(f'Error in insertion to MySQL database: {e}')

if __name__ == '__main__':
    insert_conversation_records()