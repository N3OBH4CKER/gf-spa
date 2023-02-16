import sys, time, os, random

def psb(z):
    for e in z + '\n':
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(0.01)

def rm(n):
    up = '\x1b[1A'
    erase = '\x1b[2K'
    print n
    time.sleep(0.1)                                                        
    sys.stdout.write(up)
    sys.stdout.write(erase)

                                                                       
def logo1():
    logo2 = ' -----------------------------\xe2\x80\xa2\xe2\x97\x88\xe2\x80\xa2\n(  __)\\  ____--------------_------------\xe2\x80\xa2\xe2\x97\x88\xe2\x80\xa2\n|__(~)    \xe2\x80\xa2||\xe2\x80\xa2 KI VAI SINGLE NAKI----\xe2\x80\xa2\xe2\x97\x88\xe2\x80\xa2\n|__\\~~) \xe2\x80\xa2||\xe2\x80\xa2BD KOCHI MAL --------------\xe2\x80\xa2\xe2\x97\x88\xe2\x80\xa2\n|__(-----\\  \xe2\x80\xa2\xe2\x97\x88\xe2\x80\xa2------IS HERE BRO-------\xe2\x80\xa2\xe2\x97\x88\xe2\x80\xa2\n|__~~~\\ \xe2\x80\xa2\xe2\x97\x88\xe2\x80\xa2-----\xe2\x96\x88-------\xe2\x91\xa6-------\xe2\x96\x88------\xe2\x80\xa2\xe2\x97\x88\xe2\x80\xa2\n|__~~~\\ \xe2\x80\xa2\xe2\x97\x88\xe2\x80\xa2-----\xe2\x96\x88-------\xe2\x91\xa7-------\xe2\x96\x88------\xe2\x80\xa2\xe2\x97\x88\xe2\x80\xa2\n|__~~~\\ \xe2\x80\xa2\xe2\x97\x88\xe2\x80\xa2-----\xe2\x96\x88-------\xe2\x91\xa5-------\xe2\x96\x88------\xe2\x80\xa2\xe2\x97\x88\xe2\x80\xa2\n\x1b[1;91m=======================================\n\x1b[1;96mAuthor  \x1b[1;93m: \x1b[1;92mN3OB H4CKER \n\x1b[1;96mDeveloper \x1b[1;93m: \x1b[1;  N3OB X WASIF\n\x1b[1;96mFacebook  \x1b[1;93m: \x1b[1;  www.facebook.com/100074591152479\n\n\x1b[1;96mHack \x1b[1;93m: \x1b[1;92mGF_RANDOM\n\x1b[1;91m======================================='
    print logo2
    
    


def logo():
    os.system('figlet -f big GF_H4CKER')
    bannerr = '\x1b[1;91m=======================================\n\x1b[1;96mAuthor  \x1b[1;93m: \x1b[1;92mN3OB-H4CKER\n\x1b[1;96mDeveloper \x1b[1;93m: \x1b[1;  N3OB X WASIF\n\x1b[1;96mFacebook  \x1b[1;93m: \x1b[1;  www.facebook.com/100074591152479\n\x1b[1;96mHack \x1b[1;93m: \x1b[1;93m: \x1b[1;92mGF_RANDOM\n\x1b[1;91m======================================='
    print bannerr

def logger():
    os.system('clear')
    logo()
    CorrectUsername = 'N3OB'
    CorrectPassword = 'H4CKER'
    loop = 'true'
    while loop == 'true':
        username = raw_input('\n\x1b[1;95mUSERNAME:\x1b[1;93m ')
        if username == CorrectUsername:
            password = raw_input('\n\x1b[1;95mPASSWORD:\x1b[1;93m ')
            if password == CorrectPassword:
                print '\nAPPROVED!'
                #os.system('xdg-open https://www.facebook.com/100074591152479')
                time.sleep(1)
                loop = 'false'
            else:
                print 'wrong password'
                os.system('xdg-open https://youtu.be/Y1PT0WMpXv8')
                os.system('clear')
                logo()
        else:
            print 'wrong username'
            os.system('xdg-open https://youtu.be/MfchhZ0mmFk')
            os.system('clear')
            logo()

    os.system('clear')
    
def main():
    logger()
    logo1()
    os.system('xdg-open https://is.gd/vwCzKq')
    print '\x1b[1;96m[\xe2\x98\x86] \x1b[1;93mSearch your GF \x1b[1;96m[\xe2\x98\x86]\n'
    idd = raw_input('\x1b[1;96m[+] \x1b[1;93mYour gf name \x1b[1;91m: \x1b[1;92m')
    gof = '\n\x1b[1;91m   \xf0\x9f\x94\xb0\x1b[1;95m---------------\x1b[1;92mFinding ' + idd + ' \x1b[1;95m---------------\x1b[1;91m\xf0\x9f\x94\xb0\n'
    psb(gof)
    psb('\x1b[1;91m[\x1b[1;37;40m+\x1b[1;91m]\x1b[1;92m Please Wait........')
    for persent in range(101):
        per = str(persent)
        hulu = '\x1b[1;91m[\x1b[1;37;40m+\x1b[1;91m]\x1b[1;92m Finding Gf....\x1b[1;96m' + per + '%'
        rm(hulu)

    print hulu
    psb('\x1b[1;91m[\x1b[1;37;40m+\x1b[1;91m]\x1b[1;92m Grabbing your Gf.......')
    time.sleep(2)
    psb('\x1b[1;91m[\x1b[1;37;40m+\x1b[1;91m]\x1b[1;92m Fetching Info.......')
    gf = ('')      
    v = random.choice(gf)
    bof = '\x1b[1;91m[\x1b[1;37;40m+\x1b[1;91m]\x1b[1;92m We Cant Found ' + idd + '\n\tBut we Found Kochi Mal ' + v
    psb(bof)
    p = 'xdg-open ' + v
    os.system(p)
    time.sleep(2)
    psb('\x1b[1;91m[\x1b[1;37;40m+\x1b[1;91m]\x1b[1;91m  !!!!!!!!!!!!!.....please wait.......!!!!!!!!!!!')
    time.sleep(5)
    psb('\x1b[1;91m[\x1b[1;37;40m+\x1b[1;91m]\x1b[1;92m This girl has been found as your girlfriend...')
    psb('\x1b[1;91m[\x1b[1;37;40m+\x1b[1;91m]\x1b[1;92m Send a friend request this kochi Mal and enjoy......')
    psb('\x1b[1;91m[\x1b[1;37;40m+\x1b[1;91m]\x1b[1;92m Do not take it seriously bcz its just make for fun.......')
    

main()