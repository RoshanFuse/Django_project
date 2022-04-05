from django.urls import path
from app2 import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('home/',views.home,name='home'),
    path('delete/<int:id>',views.delete,name='delete'),
    path('update/<int:id>',views.update,name='update')
    ]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)