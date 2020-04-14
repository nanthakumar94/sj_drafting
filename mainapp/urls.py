from django.urls import path

from . import views
urlpatterns = [
    path('', views.index, name='index'),
    # path('services/build_constrction_services/', views.build_services, name='build_services'),
    # path('services/family-modeling-services/', views.family_services, name='family_services'),
    # path('services/autocad-drafting-services/', views.autocad_services, name='autocad_services'),
    # path('services/solidworks-modeling-services/', views.solidworks, name='solidworks'),
    path('revit-building-construction-and-family-modeling-services/', views.bim_services, name='bim_services'),
    path('contact_us/', views.contact_us, name='contact_us'),
    path('autocad-drafting-services/', views.autocad_services, name='autocad_services'),
    path('solidworks-modeling-services/', views.solidworks, name='solidworks'),
    path('build_constrction_services/', views.build_services, name='build_services'),
    path('about_us/', views.about_us, name='about_us'),
    path('microstation_service/', views.microstation, name='microstation'),
    path('creo_modeling_services/', views.creo, name='creo'),
    path('inventor_modeling_services/', views.inventor, name='inventor'),
    path('tekla_services/', views.tekla, name='tekla'),
    path('contact', views.emailView, name='contact'),
    path('request_for_quote', views.request_for_quote, name='request_for_quote'),
]