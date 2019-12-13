# Copyright© 2019 By FajarTheGGman
# Wordlist Genertor for Google Code-in 2019©

class Wordlist:
    def banner():
        print("[---- Wordlist Generator By FajarTheGGman ----]\n")

    def main():
        f = str(input("[/] Wordlist File Name > "))
        fullname = str(input("[!] User FullName ? "))
        first = str(input("[!] First Name ? "))
        last = str(input("[!] Last Name ? "))
        nick = str(input("[!] Nickname ? "))
        pet = str(input("[!] Pet Name ? "))
        idol = str(input("[!] Idol Name ? "))
        birth = str(input("[!] Birth Date ? "))
        x = str(input("[!] Girlfriend/Boyfriend Name ? "))

        number = ['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20','1990','1991','1992','1993','1994','1995','1996','1997','1998','1999','2000','2001','2002','2003','2004','2005','2006','2007','2008','2009','2010','2011','2012','2013','2014','2015','2016','2017','2018','2019','2020','2021']

        file = open(f, "w")
        for k in number:
            file.write(fullname + k + "\n")
            file.write(first + k + "\n")
            file.write(first + last + "\n")
            file.write(nick + k + "\n")
            file.write(pet + k + "\n")
            file.write(fullname + pet + k + "\n")
            file.write(first + pet + k + '\n')
            file.write(last + idol + "\n")
            file.write(idol + k + "\n")
            file.write(first + idol + '\n')
            file.write(first + idol + k + '\n')
            file.write(idol + last + '\n')
            file.write(idol + last + k + '\n')
            file.write(birth + "\n")
            file.write(x + "\n")
            file.write(x + k + "\n")
        print("[+] Wordlist Successfully created !")

x = Wordlist
x.banner()
x.main()
