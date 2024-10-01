# flake8: noqa F405
from customer.views import *
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
# flake8: noqa F405
from product.views import *
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r"users", CustomerViewset)
router.register(r"category", CategoryViewSet)
router.register(r"product", ProductViewSet)
router.register(r"purchase", PurchaseViewSet)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include(router.urls)),
    path("api/login/", LoginView.as_view(), name="login"),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
