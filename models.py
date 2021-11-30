class UserModel():
    def __init__(self, userId, username, email):
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
    def __init__(self, userId, postId, postTitle, postBody, dateCreated):
        self.userId = userId
        self.postId = postId
        self.postTitle = postTitle
        self.postBody = postBody
        self.dateCreated = dateCreated
