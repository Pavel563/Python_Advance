import sqlite3

con = sqlite3.connect("./users.db")
cur = con.cursor()
sql = """
SELECT * FROM users
"""
cur.execute(sql)
users_list = cur.fetchall()
con.close()


class User:
    def __init__(self, params):
        self.id = params[0]
        self.first_name = params[1]
        self.age = params[2]


for index, user in enumerate(users_list.copy()):
    # users_list[index] = {
    #     'id': user[0],
    #     'first_name': user[1],
    #     'age': user[2],
    # }
    users_list[index] = User(params)
# print(users_list)
for user in users_list:
    # print(user['age'])
    print(user.age)

breakpoint()