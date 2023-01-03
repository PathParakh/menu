from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('/index', views.index),
    path('', views.index),
    path('/', views.index),
    path('index/', views.index),
    path('index', views.index, name="index"),
    path('check', views.check, name="check"),
    path('category', views.category, name="category"),
    path('delete/<int:id>', views.delete, name='delete'),
    path('update/<int:id>', views.update, name='update'),
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)