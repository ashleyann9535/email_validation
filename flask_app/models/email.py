import re
from flask import flash
from flask_app.config.mysqlconnection import connectToMySQL


# make class, class methods with SQL, and logic
class Email:
    db = 'email_validation_schema'

    def __init__(self, data):
        self.id = data['id']
        self.email = data['email']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

#Create 
    @classmethod
    def create_email(cls, data):
        query = """
        INSERT INTO emails (email, created_at, updated_at)
        VALUES (%(email)s, NOW(), NOW())
        ;"""

        return connectToMySQL(cls.db).query_db(query, data)

#Read 
    @classmethod
    def read_all_emails(cls):
        query = """
        SELECT * FROM emails
        ;"""

        result = connectToMySQL(cls.db).query_db(query)
        emails = []
        for email in result:
            emails.append(cls(email))
        return emails

    @classmethod
    def get_by_email(cls, email):
        data = {'email': email}
        query = """
        SELECT * FROM emails WHERE %(email)s
        ;"""
        result = connectToMySQL(Email.db).query_db(query, data)
        if result:
            result = cls(result[0])
        return result

#Update 


#Delete 
    @classmethod
    def delete_user(cls, id):
        data = {'id': id}
        query = """
        DELETE FROM emails WHERE id = %(id)s
        ;"""

        return connectToMySQL(cls.db).query_db(query, data)

#Validate 
    @staticmethod
    def validate_email(email):
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        is_valid = True
        if Email.get_by_email(email['email'].lower()):
            flash('Email already in use.')
            is_valid = False
        if not EMAIL_REGEX.match(email['email']):
            flash('Invalid email address!')
            is_valid = False
        else:
            flash('Email is valid')
            is_valid = True
        return is_valid