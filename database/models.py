from django.db import models

class User(models.Model):
    userID = models.UUIDField(primary_key=True) # editable=False ?
    name = models.CharField(max_length=20)
    password = models.CharField(max_length=255)
    email = models.EmailField(max_length=254)
    displayName = models.CharField(max_length=20, blank=True)
    profilePicture = models.CharField(max_length=255, blank=True)
    bio = models.CharField(max_length=255, blank=True)
    backgroundColor = models.CharField(max_length=7, blank=True) # hex color
    backgroundImage = models.CharField(max_length=255, blank=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    
class Friend(models.Model):
    friendShipID = models.AutoField(primary_key=True)
    user1 = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user1')
    user2 = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user2')
    friendDate = models.DateTimeField(auto_now_add=True)

#    def __str__(self):
#        return self.friendShipID
    
class FriendRequest(models.Model):
    requestID = models.AutoField(primary_key=True)
    user1 = models.ForeignKey(User, on_delete=models.CASCADE, related_name='requester')
    user2 = models.ForeignKey(User, on_delete=models.CASCADE, related_name='requestee')
    requestDate = models.DateTimeField(auto_now_add=True)

    # def __str__(self):
    #     return self.requestID
    
class Post(models.Model):
    postID = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    community = models.ForeignKey('Community', on_delete=models.CASCADE, null=True, blank=True)
    postDate = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255, null=True, blank=True)
    postDate = models.DateTimeField(auto_now_add=True)
    hasEdit = models.BooleanField(default=False, blank=True)
    editDate = models.DateTimeField(null=True, blank=True)

    # def __str__(self):
    #     return self.postID
    
class Media(models.Model):
    mediaID = models.AutoField(primary_key=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    mediaType = models.IntegerField() # 0 = image, 1 = video?
    mediaURL = models.CharField(max_length=255)

    # def __str__(self):
    #     return self.mediaID
    
class PostVote(models.Model):
    voteID = models.AutoField(primary_key=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    vote = models.BooleanField() # True = upvote, False = downvote

    # def __str__(self):
    #     return self.voteID
    
class Comment(models.Model):
    commentID = models.AutoField(primary_key=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    commentDate = models.DateTimeField(auto_now_add=True)
    commentContent = models.CharField(max_length=255)
    replyTo = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True) #now foreign key?
    hasEdit = models.BooleanField(default=False)
    editDate = models.DateTimeField(null=True, blank=True)

    # def __str__(self):
    #     return self.commentID
    
class CommentVote(models.Model):
    voteID = models.AutoField(primary_key=True)
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    vote = models.BooleanField() # True = upvote, False = downvote

    # def __str__(self):
    #     return self.voteID
    
class Community(models.Model):
    communityID = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20)
    description = models.CharField(max_length=255, blank=True)
    iconURL = models.CharField(max_length=255, blank=True)
    created = models.DateTimeField(auto_now_add=True)

    # def __str__(self):
    #     return self.communityID
    
class CommunityMembership(models.Model):
    membershipID = models.AutoField(primary_key=True) #composite key?
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    community = models.ForeignKey(Community, on_delete=models.CASCADE)
    joinDate = models.DateTimeField(auto_now_add=True)
    role = models.IntegerField() # 0 = member, 1 = moderator, 2 = admin, 3 = owner

    # def __str__(self):
    #     return self.membershipID
    
class Convo(models.Model):
    convoID = models.AutoField(primary_key=True)
    convoName = models.CharField(max_length=20, blank=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
         return "convo"
    
class ConvoParticipant(models.Model):
    participantID = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    convo = models.ForeignKey(Convo, on_delete=models.CASCADE)

    def __str__(self):
        return "participant"
    
class Message(models.Model): #add editing?
    messageID = models.AutoField(primary_key=True)
    convo = models.ForeignKey(Convo, on_delete=models.CASCADE)
    sender = models.ForeignKey(User, on_delete=models.CASCADE)
    messageDate = models.DateTimeField(auto_now_add=True)
    message = models.CharField(max_length=255)

    def __str__(self):
        return self.messageID
    
class ConvoSetting(models.Model):
    settingID = models.AutoField(primary_key=True)
    convo = models.ForeignKey(Convo, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    isMuted = models.BooleanField(default=False)
    isPinned = models.BooleanField(default=False)

    def __str__(self):
         return "setting"