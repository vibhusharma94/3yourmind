from django.conf.urls import url
from apps.company import views as company_views

urlpatterns = [
    url(r'^$', company_views.HomeView.as_view(), name='home'),
    url(r'^upload/?$', company_views.UploadApi.as_view(), name="upload"),
]
