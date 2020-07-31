from django.urls import path
from . import views,urls
from django.conf import settings

urlpatterns = [
    path('', views.index,name="index"),
    path('login', views.login, name="login"),
    path('logout', views.logout, name="logout"),
    path('signup', views.signup, name="signup"),
    path('resetPasswordQuestions', views.resetPasswordQuestions, name="resetPasswordQuestions"),
    path('resetPassword', views.resetPassword, name="resetPassword"),
    path('subject', views.subject, name="subject"),
]


if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns +=static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns +=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)