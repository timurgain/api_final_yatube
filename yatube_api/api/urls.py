from django.urls import include, path

from rest_framework import routers

from .views import CommentViewSet, FollowViewSet, GroupViewSet, PostViewSet

app_name = 'api'

router_v1 = routers.DefaultRouter()
router_v1.register(
    prefix=r'(?P<version>v1)/posts',
    viewset=PostViewSet,
)
router_v1.register(
    prefix=r'(?P<version>v1)/groups',
    viewset=GroupViewSet,
)
router_v1.register(
    prefix=r'(?P<version>v1)/posts/(?P<post_id>\d+)/comments',
    viewset=CommentViewSet,
    basename='comments',
)
router_v1.register(
    prefix=r'(?P<version>v1)/follow',
    viewset=FollowViewSet,
    basename='follow',
)

urlpatterns = [
    path('', include(router_v1.urls)),
]

urlpatterns += [
    path('v1/', include('djoser.urls.jwt')),
]
