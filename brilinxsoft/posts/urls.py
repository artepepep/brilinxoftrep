from django.urls import path
from .views import GetCreatePosts, GetLastTenPosts, GetFixAmountPostsAPI

urlpatterns = [
    path('get-create-posts/', GetCreatePosts.as_view() ,name='get-create-posts'),
    path('get-last-10-posts/', GetLastTenPosts.as_view(), name='10-posts'),
    path('get-fix-amount-posts/', GetFixAmountPostsAPI.as_view(), name='fixed-amount-posts')
]