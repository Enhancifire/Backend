import mysql.connector as c
import re

regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'


def check(email):

    if(re.search(regex, email)):
        return True
    else:
        return False


con = c.connect(host="localhost", user="root", port="3306",
                password="root@123", database="BLOG")

cur = con.cursor()


def SignUp(email, username, password):             #
    print(username)
    me = 0
    mee = 0
    x = check(email)
    if(x):
        cur.execute("select email from users")
        usernames = cur.fetchall()
        for email in usernames:
            me = 0
    else:
        me = 1

    if(x == False):
        cur.execute("select username from users")
        usernames = cur.fetchall()
        for email in usernames:
            mee = 0
    else:
        mee = 1

    if (me == 0 & mee == 0):
        mystring = """insert into users (email, username, password) values (%s,%s,%s)"""
        cur.execute(mystring, (str(email), username, str(password)))
        con.commit()

    else:
        if(me == 0):
            return "email already exists"
        else:
            return "username already exists"


def Login(email, passw):                                #
    x = check(email)
    # checking email
    if(x == True):
        cur.execute("select email from users")
        emails = cur.fetchall()
        for i in range(0, len(emails)):
            if (email == emails[i][0]):
                em = 1
                break
        else:
            em = 0
    else:
        # checking username
        cur.execute("select username from users")
        usernames = cur.fetchall()

        for i in range(0, len(usernames)):
            if (email == usernames[i][0]):
                em = 1
                break
        else:
            em = 0
    if(em == 1):
        passww = "select password from users where email=%s"
        cur.execute(passww, (email,))
        passwords = cur.fetchall()
        print(passwords, passw)

        if(passw == passwords[0][0]):
            y = 1
            return "login successful", 200
        else:
            y = 0
            return "login unsuccessful", 400

    else:
        return "Username/Email Doesn't exist", 404


def PostList():                                      #
    cur.execute("select * from posts")
    post_data = cur.fetchall()
    postList = []
    for i in post_data:
        postList.append({
            "postId": i[0],
            "username": i[1],
            "postTitle": i[2],
            "postBody": i[3],
            "dateCreated": i[4]
        })
    return postList


def AddPost(username, postTitle, postBody):
    str = "insert into posts (username, postTitle, postbody) values (%s,%s,%s)"
    cur.execute(str, (username, postTitle, postBody))
    con.commit()
    return 201


def ReturnPost(postId):
    #
    cur.execute("select * from posts")
    cur.execute(f"select * from posts where postId={postId}")
    s_post_data = cur.fetchall()
    for i in s_post_data:
        return {
            "postTitle": i[0],
            "postId": i[1],
            "postBody":  i[2],
            "dateCreated": i[3]
        }


def DeletePost(postId):                            #
    deleteque = "delete from posts where postId=%s"
    cur.execute(deleteque, (postId,))
    con.commit()
    return 201


def ModifyPost(postId, postBody, postTitle):
    cur.execute("update posts set postBody = %s, postTitle = %s where postId=%s",
                (postBody, postTitle, postId,))
    con.commit()
    return 200
