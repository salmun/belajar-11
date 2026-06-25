from django.shortcuts import render

# Create your views here.
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from loguru import logger

logger.add(
   "logs/app.log",
   rotation="10 MB",
   retention="30 days"
)

logger.info("Application started")


mahasiswa = [
    {
        "id": 1,
        "nama": "Salmun",
        "jurusan": "Teknik Informatika"
    }
]

karyawan = [
    {
        "id": 1,
        "nama": "Monticello",
        "jabatan": "Staff Management"
    }
]




@csrf_exempt
def mahasiswa_api(request):

    if request.method == "GET":

        return JsonResponse({
            "method": "GET",
            "data": mahasiswa
        })

    elif request.method == "POST":

        body = json.loads(request.body)

        mahasiswa.append(body)

        return JsonResponse({
            "method": "POST",
            "message": "Data berhasil ditambahkan",
            "data": body
        })

    elif request.method == "PUT":

        body = json.loads(request.body)

        mahasiswa[0] = body

        return JsonResponse({
            "method": "PUT",
            "message": "Data berhasil diganti",
            "data": body
        })

    elif request.method == "PATCH":

        body = json.loads(request.body)

        mahasiswa[0].update(body)

        return JsonResponse({
            "method": "PATCH",
            "message": "Data berhasil diubah sebagian",
            "data": mahasiswa[0]
        })

    elif request.method == "DELETE":

        mahasiswa.clear()

        return JsonResponse({
            "method": "DELETE",
            "message": "Data berhasil dihapus"
        })

def karyawan_api(request):
    if request.method == "GET":

        return JsonResponse({
            "method": "GET",
            "data": karyawan
        })

    elif request.method == "POST":

        body = json.loads(request.body)

        karyawan.append(body)

        return JsonResponse({
            "method": "POST",
            "message": "Data berhasil ditambahkan",
            "data": body
        })

    elif request.method == "PUT":

        body = json.loads(request.body)

        karyawan[0] = body

        return JsonResponse({
            "method": "PUT",
            "message": "Data berhasil diganti",
            "data": body
        })

    elif request.method == "PATCH":

        body = json.loads(request.body)

        karyawan[0].update(body)

        return JsonResponse({
            "method": "PATCH",
            "message": "Data berhasil diubah sebagian",
            "data": karyawan[0]
        })

    elif request.method == "DELETE":

        karyawan.clear()

        return JsonResponse({
            "method": "DELETE",
            "message": "Data berhasil dihapus"
        })
    
    