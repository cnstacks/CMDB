from django.shortcuts import render
from django.shortcuts import HttpResponse


# Create your views here.


def report(request):
    # if request.method == "POST":
    #     asset_data = request.POST.get('asset_data')
    #     print(asset_data)
    #     return HttpResponse("成功收到数据！")
    return HttpResponse("成功收到数据！")
