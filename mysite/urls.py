from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from main import views
from main import admin
 
urlpatterns = [
    path('', views.index),
    path('admin/', admin.site.urls),
    path('main/', include('main.urls')),
    path('main2/', include())
]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

path('save_user_input/', views.save_user_input, name='save_user_input')