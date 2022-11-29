#!/usr/bin/python2
#-*- coding: utf-8 -*-
#marshal py2

'''
PyMarshal - Compile Python Script
This project was created by DEVIL with Dark Army Spamming Gang BD
Copyright 12 - 07 - 2k19 @DEVIL
'''

try:
        import os,sys,time,marshal
except Exception as F:
        exit("[ModuleErr] %s"%(F))
        
if sys.version[0] in '2':
        exit("[sorry] use python version 3")

# Color
a='\033[1;30m'
r='\033[1;31m'
g='\033[32;1m' 
y='\033[1;33m'
c='\033[1;36m' 
w='\033[1;37m' 
n='\033[0;00m' 
br='\033[91;7m' 

bannerpy3 = """
{}╔══════════════════════════════════╗╔══════════════════════╗ 
{}║NOTE : THIS TOOLS IS FREE         ║║        ___T_         ║   
{}║══════════════════════════════════║║       | o o |        ║    
{}║AUTHOR    : DEVIL NAJMUL          ║║       |__-__|        ║    
{}║══════════════════════════════════║║       /| []|'        ║    
{}║WHATSAPP  : +8801977073308        ║║     ()/|___|\()      ║    
{}║══════════════════════════════════║║        |_|_|         ║    
{}║GITHUB    : N41M01                ║║       |_| |_|        ║    
{}║══════════════════════════════════║║                      ║    
{}║SERVER    : DATA -  WORKING       ║╚══════════════════════╝    
{}║══════════════════════════════════════════════════════════╗   
{}║FACEBOOK LINK : https://www.facebook.com/N41M01           ║    
{}║══════════════════════════════════════════════════════════║    
{}║FB PAGE LINK  : https://www.facebook.com/DEVIL.NAJMUL     ║    
{}╚══════════════════════════════════════════════════════════╝ 
""".format(r,y,br,n,y,w,r,w,y,br,n,y,w,r,w,y,br,n,y,w,r,w,y,r,a)

'''
Coded  : @DEVIL
Author : DEVIL NAJMUL
Team   : Dark Army Spamming Gang BD
Phone  : +8801977073308
Email  : devil.boy.najmul@gmail.com
Thanks : ZoneExploiter & CytoXploit
'''

os.system('clear')
try:
    print(bannerpy3)
    print (y+' ['+w+'#'+y+'] '+w+'\033[0;93m➣Example '+y+':'+w+'\033[0;94m /sdcard/DEVIL.py\n')
    file = input(y+' ['+w+'?'+y+'] '+w+'\033[0;92mInput your file location'+y+' :'+w+' ')
    o = file.replace('.py', '')
except KeyboardInterrupt:
    sys.exit()
else:
    try:
        strng = open(file, 'r').read()
    except IOError:
        print (r+'\n ['+w+'!'+r+'] '+r+'[ '+w+'Error '+r+'] '+w+'No such file or directory '+r+': '+w+'"'+deft+'"\n')
        sys.exit()
    try:
        code = compile(strng,'','exec')
        data = marshal.dumps(code)
    except TypeError:
        print (R + '   ['+W+'!'+R+'] '+R+'[ '+W+'File already to compiled\n') 
        sys.exit()

fileout = open(o + '_DEVIL_enc.py', 'w')
fileout.write('#Compiled By DEVIL\n')
fileout.write('#https://github.com/N41M01\n')
fileout.write('#https://www.facebook.com/DEVIL.NAJMUL\n')
fileout.write('import marshal\n')
fileout.write('exec(marshal.loads(' + repr(data) + '))')
fileout.close()
time.sleep(3) 
print (y+'\n ['+w+'+'+y+'] '+w+'File succes to compile   '+y+': ' + w + o + '_DEVIL_enc.py\n')
 
