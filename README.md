
# 개발환경
+ Python(3.13.4)
+ IDE VSCode

<br/><br/>

# 명령어
### 서버 실행
> python manage.py runserver

### app(폴더)생성
> python manage.py startapp [app명]

### 마이그레이션을 생성
> python manage.py makemigrations [app명]

### 마이그레이션을 적용(DB 적용)
> python manage.py migrate

### 데이터베이스 테이블을 Django 모델 코드로 변환
> python manage.py inspectdb

### 라이브러리 설치
> pip install pymysql<br>
> pip install Django django-rest-framework<br>
> pip install mysqlclient

### 프로젝트 내 새 앱 생성
> python manage.py startapp admin

<br/><br/>

# Python 문법
### if
<pre><code>num = 10
if num < 0:
    print('0 보다 작다')
elif num > 0:
    print('0 보다 크다')
elif num == 0:
    print('0 과 같다')
else:
    print('그밖에')
=> 0 보다 크다

if not num :
    print('num 값이 null이거나 비어있음')
=> num 값이 null이거나 비어있음
</code></pre>

### for
<pre><code>txtList = ['A', 'B', 'C']
for t in txtList:
    print('값:' +  t)
    if(t == 'B'):
        break
=>
값:A
값:B
</code></pre>

### match
<pre><code>txt = "C"
match txt:
    case('A'):
        print('A값')
    case('B'):
        print('B값')
    case('C'):
        print('C값')
=> C값
</code></pre>

### 문자열 처리
문자열 합치기
<pre><code>txt = '문자'
no = 10

print(txt + no)
=> 오류

print(str(txt) + no)
=> 정상
</code></pre>

포맷팅
<pre><code>txt = 'test'
print('Test %s' % txt)
=> Test test
</code></pre>

