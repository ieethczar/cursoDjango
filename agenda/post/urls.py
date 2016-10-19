from django.conf.urls import url
from . import views

urlpatterns=[
	url(r'^$',views.Home2.as_view(),name="inicio"),
	url(r'^lista/$',views.Listado.as_view(),name="lista"),
	url(r'^nuevo/$',views.Nuevo.as_view(),name="nuevo")
]