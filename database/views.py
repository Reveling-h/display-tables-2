from django.shortcuts import render, redirect
from django.http import HttpResponse

from .models import *

# Create your views here.


def index(request):
    userData = User.objects.all()
    friendData = Friend.objects.all()
    friendRequestData = FriendRequest.objects.all()
    postData = Post.objects.all()
    postVoteData = PostVote.objects.all()
    commentData = Comment.objects.all()
    commentVoteData = CommentVote.objects.all()
    communityData = Community.objects.all()
    communityMembershipData = CommunityMembership.objects.all()
    convoData = Convo.objects.all()
    ConvoParticipantData = ConvoParticipant.objects.all()
    messageData = Message.objects.all()
    ConvoSettingData = ConvoSetting.objects.all()
    

    context = {'userData':userData,'friendData':friendData,'friendRequestData':friendRequestData,'postData':postData,'postVoteData':postVoteData, 'commentData':commentData, 'commentVoteData':commentVoteData, 'communityData':communityData, 'communityMembershipData':communityMembershipData, 'convoData':convoData, 'ConvoParticipantData':ConvoParticipantData, 'messageData':messageData, 'ConvoSettingData':ConvoSettingData}
    return render(request, 'data/button.html',context)


# def viewDatabase(request):
#     data = User.objects.all()

#     if request.method=='POST':
#         return redirect('/')

#     context = {'data':data}
#     return render(request, 'data/database.html',context)