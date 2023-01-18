from django.urls import path
from django.views.decorators.csrf import csrf_exempt

from . import views


urlpatterns = [
    path('register/',
         csrf_exempt(views.register.as_view()), name='audition_registration'),
    path('check-email/',
         csrf_exempt(views.register_check_email.as_view()), name='audition_check_email'),
    path('export/',
         csrf_exempt(views.export_registrations), name='export'),
    path('export-all/',
         csrf_exempt(views.export_registrations_all), name='export_all'),
]
