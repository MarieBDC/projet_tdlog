from django.conf.urls import include, url, patterns
from django.contrib import admin
from page_accueil import views

urlpatterns = [
    # Examples:
    # url(r'^$', 'tdlog.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', views.accueil)
]
