from django.urls import path
from . import views,urls
from django.conf import settings

urlpatterns = [
    path('', views.index,name="index"),
    path('login', views.loguser, name="login"),
    path('logout', views.logoutUser, name="logout"),
    path('signup', views.signup, name="signup"),
    path('resetPassword', views.resetPassword, name="resetPassword"),
]


if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns +=static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns +=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)