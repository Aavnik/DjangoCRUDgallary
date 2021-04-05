
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
  path('',views.gallary, name='gallary'),
  path('photov/<str:pk>/',views.photov, name='photov'),
  path('deletev/<str:pk>/',views.deletev, name='deletev'),
  path('addphotos',views.addphotos, name='addphotos')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)