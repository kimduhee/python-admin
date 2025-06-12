from rest_framework.decorators import api_view
from django.db.models import Q
from django.http import JsonResponse
from django.core import serializers
from django.shortcuts import HttpResponse, render
from django.core.paginator import Paginator
from .models import AdminUser
from pyServer.common.responseUtil import commHttpResponse
import json

#관리자 관리 서브메인
@api_view(['GET'])
def adminuserSubmain(request):
    return render(request, "manage/adminuser/adminuser_submain.html")

#관리자 목록 조회
@api_view(['POST'])
def adminuserList(request):
    
    try:
        requestData = json.loads(request.body)

        #페이지 번호
        pageNo = requestData.get('pageNo')
        searchText = requestData.get('searchText')
        if not pageNo:
            pageNo = 1

        print("request parameter pageNo: %s" % str(pageNo))
        print("request parameter searchText: %s" % searchText)

        """
        result = None
        if not searchText:
            result = AdminUser.objects.all()
        else:
            result = AdminUser.objects.filter(admin_id = searchText)
        """
        #result = AdminUser.objects.raw("SELECT * FROM ADMIN_USER")
        
        obj = Q()
        if searchText:
            obj.add(Q(admin_id = searchText), obj.AND)

        result = AdminUser.objects.filter(obj)

        print("query: %s" % result.query)

        pages = Paginator(result, 10)
        page = pages.get_page(pageNo)

        resultList = serializers.serialize('json', page)
        resultJson = json.loads(resultList)

        result = {
            "adminList": resultJson,
            #"has_next": page.has_next(),
            #"has_previous": page.has_previous(),
            #"next_page_number": page.next_page_number() if page.has_next() else None,
            #"previous_page_nymber": page.previous_page_number() if page.has_previous() else None,
            "totalPage": pages.num_pages
        }

        return commHttpResponse(200, result)
    except:
        return commHttpResponse(500)
