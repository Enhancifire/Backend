from flask import Flask, request
from flask_restful import Api, Resource, reqparse, abort
import sql_connector as sqlCon

app = Flask(__name__)
api = Api(app)

# User Class
class UserModel():
    def __init__(self, userId, username,  email):
        self.userId = userId
        self.username = username
        self.email = email

    def returnUsername(self):
        return self.username

    def returnEmail(self):
        return self.email

    def returnUserId(self):
        return self.userId

class PostModel():
    def __init__(self,userId, postID, postTitle, postBody, dateCreated):
        self.userId = userId
        self.postId = postID
        self.postTitle = postTitle
        self.postBody = postBody
        self.dateCreated = dateCreated

users = [
UserModel(0, "Faiz", "fs144rules@gmail.com")
        ]

posts = [
PostModel(123, users[0].returnUserId(), "Test Title", "Lorem ipsum dolor sit amet", "30/11/2021"),
PostModel(123, users[0].returnUserId(), "Test Title", "Lorem ipsum dolor sit amet", "30/11/2021"),
PostModel(123, users[0].returnUserId(), "Test Title", "Lorem ipsum dolor sit amet", "30/11/2021"),
PostModel(123, users[0].returnUserId(), "Test Title", "Lorem ipsum dolor sit amet", "30/11/2021")
        ]
# Sign in
login_args = reqparse.RequestParser()
login_args.add_argument('email', type=str, required=True)
login_args.add_argument('password', type=str, required=True)

class Login (Resource):
    def get(self):
        args = login_args.parse_args()
        return "", 200

# Sign up
signup_args = reqparse.RequestParser()
signup_args.add_argument('email', type=str, required=True)
signup_args.add_argument('password', type=str, required=True)
signup_args.add_argument('username', type=str, required=True)

class Signup (Resource):
    def get(self):
        return {"username": users[0].username, "email": users[0].email}, 200

    def put(self):
        args = signup_args.parse_args()
        users.append(UserModel(len(users)+1, args.username,args.email))

        return "Successfull", 201

# Post

post_args = reqparse.RequestParser()
post_args.add_argument('postTitle', type=str, required=True)
post_args.add_argument('postBody', type=str, required=True)
post_args.add_argument('postTitle', type=str, required=True)

class Post(Resource):
    def get(self):
        postlist = sqlCon.PostList()
        return postlist, 200

    def put(self):
        return ""

class IndividualPost(Resource):
    def get(self, postId):
        return sqlCon.ReturnPost(postId=postId)


api.add_resource(Login, "/login")
api.add_resource(Signup, "/signup")
api.add_resource(Post, "/post")
api.add_resource(IndividualPost, "/post/<int:postId>")
if __name__ == "__main__":
    app.run(debug=True)

