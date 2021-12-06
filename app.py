from flask import Flask, jsonify
from flask_restful import Api, Resource, reqparse, abort
import sql_connector as sqlCon
from flask_cors import CORS

app = Flask(__name__)
CORS = Api(app)

# Sign in
login_args = reqparse.RequestParser()
login_args.add_argument('email', type=str)
login_args.add_argument('password', type=str)

class Login (Resource):
    def get(self):
        loginargs = login_args.parse_args()
        return sqlCon.Login(loginargs.email, loginargs.password)

# Sign up
signup_args = reqparse.RequestParser()
signup_args.add_argument('email', type=str, required=True)
signup_args.add_argument('password', type=str, required=True)
signup_args.add_argument('username', type=str, required=True)

class Signup (Resource):
    
    def post(self):
        signupargs = signup_args.parse_args()
        userId = sqlCon.SignUp(email=signupargs.email, 
                                password=signupargs.password, 
                                username=signupargs.username)
        data = {'userId': userId}
        

        return data, 201

# Post

post_args = reqparse.RequestParser()
post_args.add_argument('postTitle', type=str, required=True)
post_args.add_argument('postBody', type=str, required=True)
post_args.add_argument('username', type=str, required=True)

class Post(Resource):
    def get(self):
        postlist = sqlCon.PostList()
        return postlist, 200


class AddPost(Resource):
    def put(self):
        postargs = post_args.parse_args()
        
        return sqlCon.AddPost(postTitle=postargs.postTitle, username=postargs.username, postBody=postargs.postBody)

individualpost_args = reqparse.RequestParser()
individualpost_args.add_argument('postTitle', type =str, required=True)
individualpost_args.add_argument('postBody', type =str, required=True)


class IndividualPost(Resource):
    def get(self, postId):
        data = sqlCon.ReturnPost(postId=postId)
        response = jsonify(data)
        response.headers.add('Access-Control-Allow-Origin', "*")
        return response

    def delete(self, postId):
        sqlCon.DeletePost(postId=postId)
        return sqlCon.DeletePost(postId)

    def post(self, postId):
        updateArgs = individualpost_args.parse_args()
        return sqlCon.ModifyPost(postId=postId, postTitle=updateArgs.postTitle, postBody=updateArgs.postBody)



CORS.add_resource(Login, "/login")
CORS.add_resource(Signup, "/signup")
CORS.add_resource(Post, "/post")
CORS.add_resource(IndividualPost, "/post/<int:postId>")
CORS.add_resource(AddPost, "/post/add")
if __name__ == "__main__":
    app.run(debug=True)

