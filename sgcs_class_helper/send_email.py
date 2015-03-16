#!/usr/bin/python
#-*- coding: utf-8 -*-
import smtplib
import sys, os
import getpass
import commands

from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email import Encoders

if len(sys.argv) < 2:
    print "[Error!] [Execute Format] ./send_email <실습 주>"
    sys.exit()

####각종 상수들 모음####
info_file = os.path.abspath( os.path.dirname(sys.argv[0]) ) + "/info.txt"
hak_num = commands.getoutput("cat "+info_file+" | grep ^hak_num | cut -d'=' -f2 | tr -d ' '")
name = commands.getoutput("cat "+info_file+" | grep ^name | cut -d'=' -f2 | tr -d ' '")
naver_id = commands.getoutput("cat "+info_file+" | grep ^naver_id | cut -d'=' -f2 | tr -d ' '")
target_addr = commands.getoutput("cat "+info_file+" | grep ^target_addr | cut -d'=' -f2 | tr -d ' '")
email_text = commands.getoutput("cat "+info_file+" | grep ^email_text | cut -d'=' -f2 | tr -d ' '")

smtp_id = naver_id
text = email_text
subject = "[실습" + sys.argv[1] + "]"+hak_num+"_"+name
me = naver_id+"@naver.com"
you = target_addr
zip_name = subject + ".zip"
check_zip_cmd = "unzip -l " + zip_name + " | awk '(3<FNR)&&($4!=\"\"){print \"       -> \"$4}'"
########################

msg=MIMEMultipart()

msg['Subject'] = subject
msg['From'] = me
msg['To'] = you
msg.attach(MIMEText(text, 'plain', 'utf-8'))

part=MIMEBase('application','octet-stream')
part.set_payload(open(zip_name, 'rb').read())
Encoders.encode_base64(part)
part.add_header('Content-Disposition','attachment; filename="%s"' % os.path.basename(zip_name))
msg.attach(part)

msg2=MIMEMultipart()

msg2['Subject'] = subject + "#For_CHECK"
msg2['From'] = me
msg2['To'] = you
msg2.attach(MIMEText(text, 'plain', 'utf-8'))

part=MIMEBase('application','octet-stream')
part.set_payload(open(zip_name, 'rb').read())
Encoders.encode_base64(part)
part.add_header('Content-Disposition','attachment; filename="%s"' % os.path.basename(zip_name))
msg2.attach(part)

print smtp_id + "@smtp.naver.com login..."
password = getpass.getpass()
s = smtplib.SMTP_SSL('smtp.naver.com',465)
s.login(smtp_id, password)
s.quit()

print 
print "-----------Review----------"
print "Subject : " + subject
print "From : " + me
print "To : " + you
print "Text : " + text
print "File : " + zip_name
print "Inside " + zip_name + "..."
os.system(check_zip_cmd)
print "---------------------------"
print
sel = raw_input("위 정보가 정확합니까? 입력(Y/N)>> ")
if not (sel=="Y" or sel=='y'):
    sys.exit()

s = smtplib.SMTP_SSL('smtp.naver.com',465)
s.login(smtp_id, password)
s.sendmail(me, you, msg.as_string())
s.sendmail(me, me, msg2.as_string())
s.quit()

print
print "Send mail Okay!"
print 
print "All progress was finished!!"
print
print "             Thank you :)"
print
