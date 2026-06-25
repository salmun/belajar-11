from django.urls import path
from .views import mahasiswa_api
from .views import karyawan_api

urlpatterns = [
    path('mahasiswa/', mahasiswa_api),
    path('karyawan/', karyawan_api)
]
