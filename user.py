from mysqlconnection import connectToMySQL

class User:
    def __init__( self, data ):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name= data['last_name']
        self.email = data['email']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM users;"
        results = connectToMySQL("users_schema").query_db( query )
        users_all = []
        for row in results:
            users_all.append( cls(row) )
        return users_all

    @classmethod
    def create_user(cls, data):
        query = "INSERT INTO users ( first_name, last_name, email ) VALUES ( %(first_name)s, %(last_name)s, %(email)s );"
        new_user = connectToMySQL("users_schema").query_db( query, data )
        return new_user

    @classmethod
    def get_ind(cls, id):
        query = "SELECT * FROM users WHERE ID = %(id)s ;"
        ind_users = connectToMySQL("users_schema").query_db( query, id )
        user_ind = []
        for row in ind_users:
            user_ind.append( cls(row) )
        return user_ind

    @classmethod
    def edit_user(cls, data):
        query = "UPDATE users SET first_name = %(first_name)s, last_name = %(last_name)s, email = %(email)s WHERE id = %(id)s ;"
        edited_user = connectToMySQL("users_schema").query_db( query, data )
        return edited_user

    @classmethod
    def delete_user(cls, id):
        query = "DELETE FROM users WHERE id = %(id)s ;"
        deleted_user = connectToMySQL("users_schema").query_db( query, id )
        return deleted_user