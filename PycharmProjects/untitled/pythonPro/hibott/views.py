from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import json
import datetime
import json
import requests

section = '0'
CITY = '0'
COUNTY = '0'
VILLAGE = '0'

params = {"version": "2", "city":CITY, "county":COUNTY,"village":VILLAGE} #딕셔너리 형식 - 사용하기 편리하다.
headers = {"appKey": "fb15a052-28f1-437b-88b7-eccf830c4fa1"}
r = requests.get("https://api2.sktelecom.com/weather/current/minutely", params=params, headers=headers)

def keyboard(request):

    return JsonResponse({
        "type": "buttons",
        "buttons": ['지역 선택']
    })

@csrf_exempt
def answer(request):

    json_str = ((request.body).decode('utf-8'))
    received_json_data = json.loads(json_str)
    Local_name = received_json_data['content']
    Date_now = datetime.date.now().strftime("%m월 %d일")

    global params
    global headers
    global CITY
    global COUNTY
    global VILLAGE
    global section
    
    if Local_name == "지역 선택":

        return JsonResponse({
            'message': {
                'text': "지역을 선택해주세요"
            },
            'keyboard': {
                'type': 'buttons',
                'buttons': ['인천']
            }
        })

    if Local_name == "인천":
        CITY = Local_name

        return JsonResponse({
            'message' : {
                'text' : "구/군을 선택해주세요"
            },
            'keyboard' : {
                'type' : 'buttons',
                'buttons' : ['중구', '동구', '미추홀구', '연수구', '남동구', '부평구', '계양구', '서구', '강화군', '옹진군']
            }
        })

    if Local_name == "중구":
        COUNTY = Local_name
        section = "Final"

        return JsonResponse({
            'message' : {
                'text' : "동을 선택해주세요"
            },
            'keyboard' : {
                'type' : 'buttons',
                'buttons' : ['중앙동1가', '중앙동2가', '중앙동3가', '중앙동4가', '해안동1가', '해안동2가', '해안동3가', '해안동4가', '관동1가', '관동2가',
                             '관동3가', '항동1가', '항동2가', '항동3가', '항동4가', '항동5가', '항동6가', '항동7가',
                             '송학동1가', '송학동2가', '송학동3가', '사동', '신생동', '신포동', '답동', '신흥동1가',
                             '신흥동2가', '신흥동3가', '선화동', '유동', '율목동', '도원동', '내동', '경동', '용동', '인현동', '전동', '북성동1가', '북성동2가',
                             '북성동3가', '선린동', '송월동1가', '송월동2가', '송월동3가', '중산동', '운남동', '운서동', '운복동', '을왕동', '남북동', '덕교동',
                             '무의동', '연안동', '신흥동', '동인천동', '북성동', '송월동', '영종동', '영종1동', '용유동']
            }
        })

    if Local_name == '동구':
        COUNTY = Local_name
        section = "Final"

        return JsonResponse({
            'message' : {
                'text' : "동을 선택해주세요"
            },
            'keyboard' : 'buttons',
            'buttons' : ['만석동', '화수동', '송현동', '화평동', '창영동', '금곡동', '송림동', '화평동', '화수2동', '송현1.2동', '송현3동', '송림1동', '송림2동',
                         '송림3.5동', '송림4동', '송림6동', '금창동']
        })

    if Local_name == '미추홀구':
        COUNTY = Local_name
        section = "Final"

        return JsonResponse({
            'message' : {
                'text' : "동을 선택해주세요"
            },
            'keyboard' : 'buttons',
            'buttons' : ['숭의동', '용현동', '학익동', '도화동', '주안동', '관교동', '문학동', '숭의2동', '숭의1.3동',
                         '숭의4동', '용현1.4동', '용현2동', '용현3동', '용현5동', '학익1동', '학익2동', '도화1동', '도화2.3동',
                         '주안1동', '주안2동', '주안3동', '주안4동', '주안5동', '주안6동', '주안7동', '주안8동']
        })

    if Local_name == '연수구':
        COUNTY = Local_name
        section = "Final"

        return JsonResponse({
            'message' : {
                'text' : "동을 선택해주세요"
            },
            'keyboard' : 'buttons',
            'buttons' : ['옥련동', '선학동', '연수동', '청학동', '동춘동', '송도동', '옥련1동', '옥련2동', '연수1동', '연수2동',
                         '연수3동', '동춘1동', '동춘2동', '동춘3동', '송도1동', '송도2동', '송도3동']
        })

    if Local_name == '남동구':
        COUNTY = Local_name
        section = "Final"

        return JsonResponse({
            'message' : {
                'text' : "동을 선택해주세요"
            },
            'keyboard' : 'buttons',
            'buttons' : ['구월동', '간석동', '만수동', '장수동', '서창동', '운연동', '남촌동', '수산동', '도림동', '논현동', '고잔동',
                         '구월1동', '구월2동', '구월3동', '구월4동', '간석1동', '간석2동', '간석3동', '간석4동', '만수1동', '만수2동',
                         '만수3동', '만수4동', '만수5동', '만수6동', '장수서창동', '남촌도림동', '논현1동', '논현2동', '논현고잔동']
        })

    if Local_name == '부평구':
        COUNTY = Local_name
        section = "Final"

        return JsonResponse({
            'message' : {
                'text' : "동을 선택해주세요"
            },
            'keyboard' : 'buttons',
            'buttons' : ['부평동', '십정동', '산곡동', '청천동', '삼산동', '갈산동', '부개동', '일신동', '구산동', '부평1동', '부평2동', '부평3동',
                         '부평4동', '부평5동', '부평6동', '산곡1동', '산곡2동', '산곡3동', '산곡4동', '청천1동', '청천2동', '갈산1동', '갈산2동',
                         '삼산1동', '삼산2동', '부개1동', '부개2동', '부개3동', '십정1동', '십정2동']
        })

    if Local_name == '계양구':
        COUNTY = Local_name
        section = "Final"

        return JsonResponse({
            'message' : {
                'text' : "동을 선택해주세요"
            },
            'keyboard' : 'buttons',
            'buttons' : ['효성동', '계산동', '작전동', '서운동', '임학동', '용종동', '병방동', '방축동', '박촌동', '동양동', '귤현동', '상야동', '하야동',
                         '평동', '노오지동', '선주지동', '이화동', '오류동', '갈현동', '둑실동', '목상동', '다남동', '장기동', '효성1동', '효성2동', '계산1동',
                         '계산2동', '계산3동', '계산4동', '작전1동', '작전2동', '작전서운동', '계양1동', '계양2동', '계양3동']
        })

    if Local_name == '서구':
        COUNTY = Local_name
        section = "Final"

        return JsonResponse({
            'message' : {
                'text' : "동을 선택해주세요"
            },
            'keyboard' : 'buttons',
            'buttons' : ['백석동', '시천동', '검암동', '경서동', '공촌동', '연희동', '심곡동', '가정동', '신현동', '석남동', '원창동', '가좌동', '마전동', '당하동',
                         '원당동', '대곡동', '금곡동', '오류동', '왕길동', '불로동', '청라동', '검암경서동', '청라1동', '청라2동', '청라3동', '가정1동', '가정2동',
                         '가정3동', '석남1동', '석남2동', '석남3동', '신현원창동', '가좌1동', '가좌2동', '가좌3동', '가좌4동', '검단동', '불로대곡동', '오류왕길동']
        })

    if Local_name == '강화군':
        COUNTY = Local_name
        section = "Final"

        return JsonResponse({
            'message' : {
                'text' : "읍/면을 선택해주세요"
            },
            'keyboard' : 'buttons',
            'buttons' : ['강화읍', '선원면', '불은면', '길상면', '화도면', '양도면', '내가면', '하점면', '양사면', '송해면', '교동면', '삼산면', '서도면']
        })

    if Local_name == '옹진군':
        COUNTY = Local_name
        section = "Final"

        return JsonResponse({
            'message' : {
                'text' : "면을 선택해주세요"
            },
            'keyboard' : 'buttons',
            'buttons' : ['북도면', '백령면', '대청면', '덕적면', '영흥면', '자월면', '연평면']
        })

    if section == "Final":
        data = json.loads(r.text)
        weather = data["weather"]["minutely"]
        cTime = weather[0]["temperature"]["tc"]
        VILLAGE = Local_name

        return JsonResponse({
            'message' : {
                'text' : CITY + COUNTY + VILLAGE + "의 기온은" + cTime + "입니다.\n다른 지역을 확인하고 싶으시면 버튼을 눌러주세요!"
            },
            'type' : 'buttons',
            'buttons' : ['인천']
        })
