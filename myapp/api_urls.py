from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .api_views import (
    TicketViewSet, CommentViewSet,
    CategoryViewSet, TicketAttachmentViewSet
)

router = DefaultRouter()
router.register(r'tickets', TicketViewSet, basename='ticket')
router.register(r'comments', CommentViewSet, basename='comment')
router.register(r'categories', CategoryViewSet, basename='category')
router.register(r'attachments', TicketAttachmentViewSet, basename='attachment')

urlpatterns = [
    path('', include(router.urls)),
]
