#!/usr/bin/python
#-*- coding: utf-8 -*-
import os, sys
import commands

home_directory = os.getenv("HOME")
file_directory = os.path.abspath( os.path.dirname(sys.argv[0]) )

#is_installed_file = file_directory + "/is_installed.txt"
res = commands.getoutput("cat ~/.profile | grep ^#class_helper_installed")

if res!="":
    print "이미 설치되어 있습니다."
    exit()

print "-------- Auto Submit Tool -------"
print "For C-Class --------- By taeguk -"
print
print "*** This is a progress for install ***"
print

print "[*] Install zip package"
os.system("mkdir "+file_directory+"/tmproot")
os.system("dpkg-deb -x "+file_directory+"/zip_3.0-8_amd64.deb "+file_directory+"/tmproot/")
print "[*] Install unzip package"
os.system("dpkg-deb -x "+file_directory+"/unzip_6.0-9ubuntu1_amd64.deb "+file_directory+"/tmproot/")

print "[*] Setting your information"
print

info_file = file_directory + "/info.txt"

if os.path.isfile(info_file):
	print "이미 있는 info.txt 파일을 사용하겠습니다!!"
	info_file = os.path.abspath( os.path.dirname(sys.argv[0]) ) + "/info.txt"
	hak_num = commands.getoutput("cat "+info_file+" | grep ^hak_num | cut -d'=' -f2 | tr -d ' '")
	name = commands.getoutput("cat "+info_file+" | grep ^name | cut -d'=' -f2 | tr -d ' '")
else:
    while True:
        hak_num = raw_input("학번을 입력해 주십시요.(ex. 20141500) 입력>> ")

        name = raw_input("이름을 입력해 주십시요.(ex. 권태국) 입력>> ")

        naver_id = raw_input("당신의 네이버아이디를 입력해 주십시요.(ex. xornrbboy) 입력>> ")

        target_addr = raw_input("조교님의 메일주소를 입력해 주십시요.(ex. 2014cprogramming03@gmail.com) 입력>> ") 

        email_text = raw_input("메일 보낼때의 text를 입력해 주십시오. (ex. c프로그래밍 실습 제출입니다~~) 입력>> ");

        print
        print "---------- INFO ---------"
        print "     학   번     : " + hak_num
        print "     이   름     : " + name
        print "  네이버 아이디  : " + naver_id
        print " 조교님 메일주소 : " + target_addr
        print "  이메일 텍스트  : " + email_text
        print
        sel = raw_input("정보가 올바르게 입력되었습니까? (Y/N)>> ")
        if sel=='Y' or sel=='y':
            break
        print
        print "정보를 다시 한번 입력해 주십시요..."
        print
    
    f = open(info_file,"a")
    f.write("hak_num="+hak_num+"\n")
    f.write("name="+name+"\n")
    f.write("naver_id="+naver_id+"\n")
    f.write("target_addr="+target_addr+"\n")
    f.write("email_text="+email_text+"\n")
    f.close()

print "[*] Information setting complete!"
print
print "[*] environment setting (add to .profile)"
cmd4echo = "export PATH=\"" + file_directory + "/tmproot/usr/bin:" + file_directory +":$PATH\""
os.system("cp -rf ~/.profile ~/.profile_original")
profile_file = home_directory + "/.profile"
f = open(profile_file,"a")
f.write(cmd4echo+"\n")
f.write("#class_helper_installed\n")
f.close()

#os.system("echo "+hak_num+name+" >> /sogang/under/cs20141500/tools/class_helper_user_list.txt");

print
print "INSTALL이 완료되었습니다.  계정에 다시 접속해주세요."
print
print "*메일 전송 기능을 사용하시려면 네이버메일 환경설정이 필요합니다"
print "*http://blog.naver.com/zw1012/220104479903 를 보고 네이버메일 smtp를 허용해주세요!"
print
print "vi readme.txt 를 통해 readme.txt를 확인해주세요."
print
