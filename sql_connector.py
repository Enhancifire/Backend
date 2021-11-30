def SignUp(self, email, password, username):
    # if user exists, return error
    if 1 == 1:
      return "user exists"

def LoginWithEmail(self, email, password):
    return "UserID"

def LoginWithUsername(self, username, password):
    return "UserID"

def PostList(self):
    return [{
            "postTitle": "postTitle",
            "postId": "postId",
            "userId": "userId",
            "dateCreated": "dateCreated"
            }]

def AddPost(self, postTitle, userId, postBody):
    return "Created Successfully"

def ReturnPost(self, postId):
    return {
            "postTitle": "postTitle",
            "postId": "postId",
            "postBody": "postBody",
            "dateCreated": "dateCreated"
            }

def DeletePost(self, postId):
    return "Deleted Successfully"

def ModifyPost(self, postId, postBody, postTitle):
    return "Post Modified Successfully"
