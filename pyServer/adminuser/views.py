from django.http import JsonResponse
from django.core import serializers
from django.shortcuts import HttpResponse, render
from django.core.paginator import Paginator
from .models import AdminUser
import json

#관리자 관리 서브메인
def adminuserSubmain(request):
    return render(request, "manage/adminuser/adminuser_submain.html")

#관리자 목록 조회
def adminuserList(request):
    if request.method == 'POST':

        requestData = json.loads(request.body)

        #페이지 번호
        pageNo = requestData.get('pageNo')
        if not pageNo:
            pageNo = 1

        print("pageNo: " + str(pageNo))

        result = AdminUser.objects.all()
        pages = Paginator(result, 10)
        page = pages.get_page(pageNo)

        resultList = serializers.serialize('json', page)
        resultJson = json.loads(resultList)

        context = {
            "data": resultJson,
            "has_next": page.has_next(),
            "has_previous": page.has_previous(),
            "next_page_number": page.next_page_number() if page.has_next() else None,
            "previous_page_nymber": page.previous_page_number() if page.has_previous() else None,
            "num_pages": pages.num_pages
        }

        return JsonResponse(context, status=200, safe=False)
