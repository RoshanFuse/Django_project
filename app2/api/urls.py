from django.urls import path,include
from app2.api import views
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register('curd',views.DataViewsSet,basename='user')


urlpatterns = [
    path('',include(router.urls))
               ]
