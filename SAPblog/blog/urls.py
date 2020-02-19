from django.conf.urls import url
from SAPblog.blog import views

urlpatterns = [  
    url(r'^$', views.PostListView.as_view(), name = 'post_list'),
    url(r'^about/$', views.AboutView.as_view(), name = 'about'),
    url(r'^post/(?P<pk>\d+)$', views.PostDetailView.as_view(),name='post_detail'),
    url(r'^post/new/$',views.CreatePostView.as_view(), name = 'post_view'),
    url(r'^post/(?P<pk>\d+)/edit/$', views.PostUpdateView.as_view(), name = 'post_edit'),
    url(r'^post/(?P<pk>\d+)/remove/$',views.PostDeleteView.as_view(), name = 'post_remove'),
    url(r'^drafts/$', views.DraftListview.as_view(), name = 'post_draft_list'),
    url(r'^post/(?P<pk>\d+)/comment/$)',views.add_comment_to_post.as_view(), name = 'add_comment_post'), 
    url(r'^comment/(?P<pk>\d+)/approve/$', views.comment_approve, name='comment_approve'),
    url(r'^comment/(?P<pk>\d+)/remove/$', views.comment_remove, name = 'comment_remove'),
    url(r'^post/(?P<pk>\d+)/publish/$', views.post_published, name = 'post_publish'),
]