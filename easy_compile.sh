#/bin/bash
if [ "$#" -eq 0 ];then
    echo "[Error!] 만들 프로그램 이름을 매개변수로 넣어주세요!!"
else
    echo [progress] gcc -o $1 $1.c
    echo [progress] ./$1
    gcc -o $1 $1.c
    echo --------execute result--------
    ./$1
fi
