from .entities.User import User


class ModelUser():
    @classmethod
    def login(self, db, user):
        try:
            cursor = db.connection.cursor()
            sql = "INSERT INTO user(username,password,fecha_creacion)VALUES(%s,%s,sysdate());"
            val = (user.username, user.password)
            cursor.execute(sql,val)
            db.connection.commit()
        except Exception as ex:
            raise Exception(ex)

'''    @classmethod
    def get_by_name(self, db, user,username):
        try:
            cursor = db.connection.cursor()
            sql = "SELECT id, username, password FROM user WHERE id = {}".format(username)
            cursor.execute(sql)
            row = cursor.fetchone()
            if row != None:
                return User(row[0], row[1], None, row[2])
            else:
                return None
        except Exception as ex:
            raise Exception(ex) '''