"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include


from rest_framework.routers import DefaultRouter

from polls.views import QuestionViewSet, ChoiceViewSet

router = DefaultRouter()
router.register('question', QuestionViewSet)
router.register('choice', ChoiceViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    # path('polls/', include("polls.urls")),
    path('o/', include('oauth2_provider.urls', namespace='oauth2_provider')),
    path('oauth/', include('social_django.urls', namespace='social')),
    path('authentication/', include('polls.urls')),
    path('v1/', include(router.urls)),
    path('', include('django.contrib.auth.urls')),
]
