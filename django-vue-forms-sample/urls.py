from django.conf.urls import url
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


from vue_formset import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),

    url(r'^$', views.index),
    url(r'^api/get_persons/?$', views.get_persons),
    url(r'^api/update_persons/?$', views.update_persons),
]
urlpatterns += staticfiles_urlpatterns()
