
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path, include
from home import urls as home_urls
from disciplinas import urls as disciplinas_urls
from usuarios import urls as usuarios_urls
from django.conf import settings
from django.conf.urls.static import static

from django.http import HttpResponseRedirect

from django.conf.urls import url
from django.views.generic import TemplateView


urlpatterns = [
    path('', include(home_urls)),
    path('disciplinas/', include(disciplinas_urls)),
    path('usuarios/', include(usuarios_urls)),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('admin/', admin.site.urls)
]  + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
