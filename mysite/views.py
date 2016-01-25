from django.db import connection
from django.shortcuts import render

def check_status(request):
    if connection.is_usable():
        database_status = 'working'
    else:
        database_status = 'down'
    return render(request, 'status.html', {'database_status': database_status})