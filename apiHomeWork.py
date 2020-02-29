import requests, json

print ('숙제1. 인스타에서 글퍼오기.')
'''
insta API주소중 oembed 부분까지 긁어옴.
(https://www.instagram.com/developer/embedding/#oembed)
'''

INSTA_API = 'https://api.instagram.com/oembed' #물음표 앞에 있는것 까지 긁어와서 API변수 이름에 넣어줌
params = {
    'url' : 'https://www.instagram.com/p/B8OBL7BDEpL/?utm_source=ig_web_copy_link' #멋사 공식계정 퍼가기에서 링크복사 해옴.
}

req = requests.get(INSTA_API, params = params) #request의 get함수를 써서 INSTA_API 주소와 parameter집어넣어서 결과값을 변수에 저장.
res = req.json()['title'] #안에 보니까 글부분은 'title'로 지정되어 있음. 1단이라 바로 긁어올 수 있음.
print(req.url) #바로가기 url 생성
print(res) #글 퍼오기


print ('숙제2. 구글 맵 연결하기.')
'''
구글 Direction API긁어옴.
(https://www.google.com/maps/dir/?api=1)
'''

GOOGLE_MAP_API = 'https://www.google.com/maps/dir/'
params = {
    'api' : '1', #왜 인지 모르겠으나 api 가이드에 이건 1이라고 적혀있었음.
    'origin' : 'Novaland golf park, quan 9, thanh pho ho chi minh', #출발지 지정
    'destination' : '38A nguyen thi dieu, quan 3 thanh pho ho chi minh', #도착지 지정
    'travelmode' : 'driving' #차로 가는걸로 설정, 걸어가는건 walking method
}

req = requests.get(GOOGLE_MAP_API, params = params) #request의 get함수를 써서 INSTA_API 주소와 parameter집어넣어서 결과값을 변수에 저장.
print(req.url) #바로가기 url 생성