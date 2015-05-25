#!/bin/bash

info_file=$(dirname $0)"/info.txt"
if [ ! -f $info_file ]; then
    echo "$info_file 가 없습니다!!"
    exit
fi

hak_num=$(cat $info_file | grep ^hak_num | cut -d'=' -f2 | tr -d ' ')
name=$(cat $info_file | grep ^name | cut -d'=' -f2 | tr -d ' ')

echo
echo "=========Auto Submit Tool========"
echo "===For SGU_CS_C_CLASS===By taeguk"
echo
echo "실습 번호를 입력해 주세요.."
read week
echo

echo "-----[ 1st - name_change.sh ]-----"
name_change.sh $week
res=$(ls -al | grep 'cp'$week'_'$hak_num'_p.*.c')
if [ "$res" == "" ];then
    echo -e "\n    Failed to change name!!!    \n"
    exit
fi
echo

echo "-----[ 2st - zip_compress.sh ]-----"
zip_compress.sh $week
res=$(ls -al | grep $week']'$hak_num'_'$name'.zip')
if [ "$res" == "" ];then
    echo -e "\n    Failed to zip compression!!!    \n"
    exit
fi
echo

echo "-----[ 3st - send_email.py ]-----"
send_email.py $week

#echo
#echo "All progress was finished!!"
#echo "    @please check result!!" 
#echo
#echo "             Thank you :)        "
#echo
