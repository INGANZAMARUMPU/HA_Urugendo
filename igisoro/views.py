from django.shortcuts import render, HttpResponse

def kugwiza(request, igiharuro):
    igiharuro = int(igiharuro)
    umwimbu = ""
    for a in range(1, 13):
        umurongo = f"{a} x {igiharuro} = {a*igiharuro}<br>"
        print(umurongo)
        umwimbu += umurongo
    return HttpResponse(umwimbu)