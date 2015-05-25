#!/bin/bash

info_file=$(dirname $0)"/info.txt"
if [ ! -f $info_file ]; then
    echo "$info_file 가 없습니다!!"
    exit
fi

hak_num=$(cat $info_file | grep ^hak_num | cut -d'=' -f2 | tr -d ' ')
name=$(cat $info_file | grep ^name | cut -d'=' -f2 | tr -d ' ')

if [ "$#" -eq "0" ];then
    echo "[Error!] 실습 번호를 매개변수로 넣어주세요!!"
else
	zip_name=[실습$1]"$hak_num"_"$name".zip
	if [ -f "$zip_name" ]; then
		rm $zip_name
	fi
    zip_cmd="zip -r $zip_name cp"$1"_"$hak_num_p"*.c"
    echo "[Progress]"$zip_cmd
    eval $zip_cmd
fi
