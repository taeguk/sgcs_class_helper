서강대 c프로그래밍 수업에 유용하게 쓸 수 있는 툴 모음.
	-> 실습 파일 자동 제출 auto submit
	-> free Checker

ver 1.11

설치방법:
    tar -xvzf class_helper_ver_1_1.tar.bz2 를 쳐서 압축을 풉니다.
    cd class_helper_ver_1_1
    ./install.py
사용방법:
    mkdir명령어를 이용해 폴더를 하나 만듭니다.
    그 폴더안에서 실습문제 소스를 짭니다.
    소스 파일 이름은 p1.c p2.c p3.c ~~~ 이런식으로 합니다.
	(그 외의 .c 파일이 폴더 내에 없도록 주의해 주시기 바랍니다!)
    다 짜고 제출을 하고싶으면 auto_submit.py 를 치고 엔터를 누릅니다.
    끝~~

---ver 1.0---
첫 릴리즈 (auto submit 기능)

---ver 1.1---
1. send_email.py 수정
	-> 조교님께 이메일을 보냄과 동시에 자기자신에게도 이메일을 보내도록 수정. (이메일을 보냈다는 것을 기록으로 남기기 위해)
	-> 네이버 로그인 후 review 화면이 뜨도록 수정. (기존에는 review를 띄운 후 로그인을 했었음)

2. zip_compress.sh 수정
	-> zip프로그램 특성상 이미 압축파일이 있을 경우 예상했던 것과 다른 결과가 일어날 수 있어서 이미 압축파일이 있을 경우 삭제후 압축하도록 코드 수정.

3. freeChecker.sh 추가 (새 기능)
	c로 짠 프로그램의 동적할당 메모리 해제를 체크할 수 있는 freeChecker.sh 를 class helper 추가

---ver 1.11---
1. freeChecker.sh 수정
	64비트/32비트 호환.

