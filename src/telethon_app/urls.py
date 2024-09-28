from rest_framework.routers import DefaultRouter

from .views import TelegramAccountViewSet, SubscribeChannelsViewSet, SendMessageViewSet

router = DefaultRouter()
router.register('telegram-accounts', TelegramAccountViewSet)
router.register('subscribe-channels', SubscribeChannelsViewSet, basename='subscribe-channels')
router.register('send-message', SendMessageViewSet, basename='send-message')
urlpatterns = router.urls
