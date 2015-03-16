#!/bin/bash

info_file=$(dirname $0)"/info.txt"
if [ ! -f $info_file ]; then
    echo "$info_file 가 없습니다!!"
    exit
fi

hak_num=$(cat $info_file | grep ^hak_num | cut -d'=' -f2 | tr -d ' ')

if [ "$#" -eq "0" ]; then
    echo "[Error!] 실습 번호를 매개변수로 넣어 주세요!!"
elif [ $1 == "0" ]; then
    recovery_cmd="rename 's/cp.*_"$hak_num"_//' *.c" 
    echo "$recovery_cmd"
    eval $recovery_cmd
else
    rename_cmd="rename 's/^p/cp"$1"_"$hak_num"_p/' p*.c"
    echo "$rename_cmd"
    eval $rename_cmd
fi
