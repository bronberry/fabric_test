from rest_framework.routers import DefaultRouter

from spammer.viewset import DistributionViewSet, ClientListViewSet, MessageListViewSet

router = DefaultRouter()

router.register(r"distribution", DistributionViewSet, "distribution")
router.register(r"client", ClientListViewSet, "client")
router.register(r"message", MessageListViewSet, "message")
