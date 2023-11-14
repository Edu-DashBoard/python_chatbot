from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from main import views

urlpatterns = [
    path('', views.index),
    path('loading_answer/',views.loading_answer,name='loading_answer'),
    path('save_user_input/', views.save_user_input, name='save_user_input'),
    
    path('save_user_output/', views.save_user_output, name='save_user_output'),
    

]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

