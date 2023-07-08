from django.urls import path, include

from .import views

from rest_framework import routers

router = routers.DefaultRouter()
router.register('api', views.MagarViewSet)

urlpatterns = [
   path('',views.index, name='index'),
   path('contact', views.contact, name='contact'),  
   path('magar_details/<slug>', views.magar_details, name='magar_details'),   
   path('indra/<slug>', views.indra_magar, name='indra'),     
   path('magar', views.magar, name='magar'),
   path('category/<slug>', views.category, name='category'),
   path('copyright/<slug>', views.copyright, name='copyright'),
   path('api/', include(router.urls)),
   path('magar_api', views.magar_api, name='magar_api')
   ]