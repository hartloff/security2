import json
import sys
import sqlite3
import html


def setupDatabase():
    #connection = sqlite3.connect('/var/CSE113/hartloff/commentDatabase.db')
    connection = sqlite3.connect('commentDatabase.db')
    database = connection.cursor()
    database.execute("CREATE TABLE IF NOT EXISTS comments (id INTEGER, comment VARCHAR(25))")
    connection.commit()
    return connection


# Returns the next available ID to be used while inserting new songs
def getNewID(database):
    database.execute("SELECT MAX(id) FROM comments")
    maxID = database.fetchone()[0]
    newID = 0
    try:
        newID = maxID + 1
    except:
        pass
    return newID


def addComment(request, database):
    comment = request['comment']

    if comment == "None":
        # At least one of the fields was left empty. Do not add to the database
        return

    # Find a new ID for this song
    id = getNewID(database)

    # escape html for security
    #comment = html.escape(comment)

    #database.execute("INSERT INTO comments VALUES (?, ?)", (id, comment))
    database.execute("INSERT INTO comments VALUES (\"" + str(id) + "\", \"" + str(comment) + "\")")



def getAllComments(database):
    comments = ""
    database.execute("SELECT * FROM comments")
    for row in database:
        comments = comments + str(row[1]) + "<br/><hr/>"
    #return json.dumps(comments)
    return comments



def handleRequest(request):
    try:
        database = setupDatabase()

        if request["requestType"] == "addComment":
            addComment(request, database.cursor())
            response = "Comment Submitted: " + str(request) + "fds ksdaskdglsdfkladfsklsdfakfsdkl;kl;fsdflks;d"
        elif request["requestType"] == "getAllComments":
            response = getAllComments(database.cursor())
        else:
            response = "Invalid Request Type" + str(request)

        database.commit()
        database.close()
        return response
    except AttributeError as err:
        print(err)
    except:
        return sys.exc_info()[0]


# print(handleRequest({"requestType":"getAllSongs"}))
