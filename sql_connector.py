import mysql.connector as c
con = c.connect(host="localhost", user="root", port="3306",
                password="root@123", database="BLOG")
print(con)


def SignUp(email, password, username):
    # if user exists, return error

    if 1 == 1:
        return "user exists"


def LoginWithEmail(email, password):
    return "UserID"


def LoginWithUsername(username, password):
    return "UserID"


def PostList():
    return [{
            "postTitle": "postTitle",
            "postId": "postId",
            "userId": "userId",
            "dateCreated": "dateCreated"
            }]


def AddPost(postTitle, userId, postBody):
    return "Created Successfully"


def ReturnPost(postId):
    return {
        "postTitle": "postTitle",
        "postId": "postId",
        "postBody": "postBody",
        "dateCreated": "dateCreated"
    }


def DeletePost(postId):
    return "Deleted Successfully"


def ModifyPost(postId, postBody, postTitle):
    return "Post Modified Successfully"
