from userModel import User
import mysql.connector

class UserDao:
    def __init__(self):
        self.con = mysql.connector.connect(host='localhost', database='pythonmysql', user='root', password='cradfor')
        self.cursor = self.con.cursor()

    def findAll(self):
        findAll = "select * from user"
        self.cursor.execute(findAll)
        lines = self.cursor.fetchall()
        for line in lines:
            print(f"Id: {line[0]}")
            print(f"Name: {line[1]}")
            print(f"Password: {line[2]}")
            print(f"Email: {line[3]}\n")

    def findById(self, id):
        findById = f"select * from user where id = {id}"
        self.cursor.execute(findById)
        line = self.cursor.fetchall()
        for i in line:
            print(f"Id: {i[0]}")
            print(f"Name: {i[1]}")
            print(f"Password: {i[2]}")
            print(f"Email: {i[3]}\n")

    def insert(self, obj):
        insert = f"insert into user values (default, '{obj.login}', md5('{obj.senha}'), '{obj.email}')"
        self.cursor.execute(insert)
        self.con.commit()
        print(f'User with login: {obj.login} was added')

    def deleteById(self, id):
        deleteById = f"delete from user where id = {id}"
        self.cursor.execute(deleteById)
        self.con.commit()
        print(f'Deleted user with id: {id}')

    def updateById(self, obj):
        updateById = f"""update user set 
            login = '{obj.login}', 
            senha = md5('{obj.senha}'), 
            email = '{obj.email}' 
            where id = {obj.id}"""
        self.cursor.execute(updateById)
        self.con.commit()
        print(f'Updated user with id: {obj.id}')

    def closeConection(self):
        if self.con.is_connected():
            self.con.close()
            self.cursor.close()

