"""
This module contains all database interfacing methods for the MFlix
application. You will be working on this file for the majority of M220P.

Each method has a short description, and the methods you must implement have
docstrings with a short explanation of the task.

Look out for TODO markers for additional help. Good luck!
"""


from flask import current_app, g
from werkzeug.local import LocalProxy

from pymongo import MongoClient, DESCENDING, ASCENDING
from pymongo.write_concern import WriteConcern
from pymongo.errors import DuplicateKeyError, OperationFailure
from bson.objectid import ObjectId
from bson.errors import InvalidId
from pymongo.read_concern import ReadConcern


def get_db():
    """
    Configuration method to return db instance
    """
    db = getattr(g, "_database", None)
    MFLIX_DB_URI = current_app.config["MFLIX_DB_URI"]
    MFLIX_DB_NAME = current_app.config["MFLIX_NS"]
    if db is None:

        """
        Ticket: Connection Pooling

        Please change the configuration of the MongoClient object by setting the
        maximum connection pool size to 50 active connections.
        """

        """
        Ticket: Timeouts

        Please prevent the program from waiting indefinitely by setting the
        write concern timeout limit to 2500 milliseconds.
        """

        db = g._database = MongoClient(
        MFLIX_DB_URI,
        # TODO: Connection Pooling
        # Set the maximum connection pool size to 50 active connections.
        # TODO: Timeouts
        # Set the write timeout limit to 2500 milliseconds.
        )[MFLIX_DB_NAME]
    return db


# Use LocalProxy to read the global db instance with just `db`
db = LocalProxy(get_db)



"""
Ticket: User Management

For this ticket, you will need to implement the following six methods:

- get_user
- add_user
- login_user
- logout_user
- get_user_session
- delete_user

You can find these methods below this docstring. Make sure to read the comments
to better understand the task.
"""


def get_user(email):
    """
    Given an email, returns a document from the `users` collection.
    """
    # TODO: User Management
    # Retrieve the user document corresponding with the user's email.
    return db.users.find_one({ "some_field": "some_value" })


def add_user(name, email, hashedpw):
    """
    Given a name, email and password, inserts a document with those credentials
    to the `users` collection.
    """

    """
    Ticket: Durable Writes

    Please increase the durability of this method by using a non-default write
    concern with ``insert_one``.
    """

    try:
        # TODO: User Management
        # Insert a user with the "name", "email", and "password" fields.
        # TODO: Durable Writes
        # Use a more durable Write Concern for this operation.
        db.users.insert_one({
            "name": "mongo",
            "email": "mongo@mongodb.com",
            "password": "flibbertypazzle"
        })
        return {"success": True}
    except DuplicateKeyError:
        return {"error": "A user with the given email already exists."}


def login_user(email, jwt):
    """
    Given an email and JWT, logs in a user by updating the JWT corresponding
    with that user's email in the `sessions` collection.

    In `sessions`, each user's email is stored in a field called "user_id".
    """
    try:
        # TODO: User Management
        # Use an UPSERT statement to update the "jwt" field in the document,
        # matching the "user_id" field with the email passed to this function.
        db.sessions.update_one(
            { "some_field": "some_value" },
            { "$set": { "some_other_field": "some_other_value" } }
        )
        return {"success": True}
    except Exception as e:
        return {"error": e}


def logout_user(email):
    """
    Given a user's email, logs out that user by deleting their corresponding
    entry in the `sessions` collection.

    In `sessions`, each user's email is stored in a field called "user_id".
    """
    try:
        # TODO: User Management
        # Delete the document in the `sessions` collection matching the email.
        db.sessions.delete_one({ "some_field": "some_value" })
        return {"success": True}
    except Exception as e:
        return {"error": e}


def get_user_session(email):
    """
    Given a user's email, finds that user's session in `sessions`.

    In `sessions`, each user's email is stored in a field called "user_id".
    """
    try:
        # TODO: User Management
        # Retrieve the session document corresponding with the user's email.
        return db.sessions.find_one({ "some_field": "some_value" })
    except Exception as e:
        return {"error": e}


def delete_user(email):
    """
    Given a user's email, deletes a user from the `users` collection and deletes
    that user's session from the `sessions` collection.
    """
    try:
        # TODO: User Management
        # Delete the corresponding documents from `users` and `sessions`.
        db.sessions.delete_one({ "some_field": "some_value" })
        db.users.delete_one({ "some_field": "some_value" })
        if get_user(email) is None:
            return {"success": True}
        else:
            raise ValueError("Deletion unsuccessful")
    except Exception as e:
        return {"error": e}


def get_configuration():
    """
    Returns the following information configured for this client:

    - max connection pool size
    - write concern
    - database user role
    """

    try:
        role_info = db.command({'connectionStatus': 1}).get('authInfo').get(
            'authenticatedUserRoles')[0]
        return (db.client.max_pool_size, db.client.write_concern, role_info)
    except IndexError:
        return (db.client.max_pool_size, db.client.write_concern, {})
