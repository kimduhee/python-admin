from rest_framework.decorators import api_view
from django.http import JsonResponse
import json

#공통 응답
def commHttpResponse(statusCode, data=None):

    print("status: " + str(statusCode))

    #결과코드드
    statusCd = ""
    #결과메세지
    statusMag = ""

    if statusCode == 200:
        statusCd = "success"
        statusMsg = ""
    else:
        statusCd = "fail"
        statusMag = "일시적인 오류가 발생했습니다."

    result = {
        "status": statusCd,
        "msg": statusMag,
        "data": data
    }

    return JsonResponse(result, status=statusCode, safe=False)

    