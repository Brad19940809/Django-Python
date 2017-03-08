from django.conf.urls import include, url
from django.conf.urls import url
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^auth/', include('slock_account.urls')),
    # url()
]
