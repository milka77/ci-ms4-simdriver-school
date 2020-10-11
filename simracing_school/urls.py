"""simracing_school URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from .views import Facebook, Twitter, Instagram, iRacing, CrewChief, TradingPaints

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('', include('home.urls')),
    path('facebook/', Facebook.as_view(), name='facebook'),
    path('twitter/', Twitter.as_view(), name='twitter'),
    path('instagram/', Instagram.as_view(), name='instagram'),
    path('crewchief/', CrewChief.as_view(), name='crewchief'),
    path('iracing/', iRacing.as_view(), name='iracing'),
    path('tradepaints/', TradingPaints.as_view(), name='tradingpaints'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
