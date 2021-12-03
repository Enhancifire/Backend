import mysql.connector as c
import re

regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'



def check(email):

    if(re.search(regex, email)):
        return True
    else:
        return False


con = c.connect(host="localhost", user="root", port="3306",
                password="fs144", database="BLOG")

cur = con.cursor()


def SignUp(email, username, password):
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
        cur.execute(mystring,(str(email), username, str(password)))
        con.commit()
    
        
    else:
        if(me == 0):
            return "email already exists"
        else:
            return "username already exists"


def Login(email, passw):

    x = check(email)
    if(x):
        cur.execute("select email from users")
        usernames = cur.fetchall()
        for email in usernames:
            em = 1
        else:
            em = 0
    else:
        cur.execute("select username from users")
        usernames = cur.fetchall()
        for email in usernames:
            em = 1
        else:
            em = 0
    if(em == 1):
        cur.execute("select password from users where username=?", email)
        passwords = cur.fetchall()
        if(passw in passwords):
            y = 1
            return "login successful", 200
        else:
            y = 0
            return "login unsuccessful", 400

    else:
        return "Username/Email Doesn't exist", 404

def PostList():
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
        cur.execute("insert into posts (username, postTitle, postbody) values (?,?,?)",username, postTitle, postBody)
        return 201

def ReturnPost(postId):
        cur.execute(f"select * from posts where postId={postId}")
        s_post_data = cur.fetchall()
        for i in s_post_data:
            return {
                "postTitle": i[0],
                "postId": i[1],
                "postBody":  i[2],
                "dateCreated": i[3]
            }


def DeletePost(postId):
        cur.execute("delete from posts where postId=?", postId)
        return 201

def ModifyPost(postId, postBody, postTitle):
        cur.execute("update posts set postBody = ?, postTitle = ? where postId=?",
                    postBody, postTitle, postId)
        return 200
