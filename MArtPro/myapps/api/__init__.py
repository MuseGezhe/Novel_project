from rest_framework import routers

from api.art import ArtViewSet
from api.category import CategoryViewSet

# 创建API的路由对象
api_router = routers.DefaultRouter()

# 将分类显示视图注册到API路由中
api_router.register(u'cates',CategoryViewSet)
api_router.register(u'arts',ArtViewSet)