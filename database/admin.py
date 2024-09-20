from django.contrib import admin

from .models import  *

admin.site.register(User)
admin.site.register(Friend)
admin.site.register(FriendRequest)
admin.site.register(Post)
admin.site.register(Media)
admin.site.register(PostVote)
admin.site.register(Comment)
admin.site.register(CommentVote)
admin.site.register(Community)
admin.site.register(CommunityMembership)
admin.site.register(Convo)
admin.site.register(ConvoParticipant)
admin.site.register(Message)
admin.site.register(ConvoSetting)