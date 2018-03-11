
def summa(x, y):
        return x + y

def vahennys(x, y):
        return x - y
def kerto(x, y):
        return x * y
def jako(x, y):
        return x / y

kierros = 0
while kierros == 0:
        print "valitse laskutoimitus."
        print "1.Summa"
        print "2.Vahennys"
        print "3.kerto"
        print "4.jako"
        while True:
                try:
                        valinta = int(raw_input("valitse toiminto(1,2,3,4):"))
                        break
                except ValueError:
                        print "Syota vain lukuja!"
        valinta2 = valinta
        while valinta2 >= 5:
                if valinta2 not in range(0,5):
                        print "valinta ei mahdollinen, yrita uudestaan"
                        valinta2 = int(raw_input("valitse toiminto(1,2,3,4):"))
                else:
                        valinta = valinta2          
        while True:
                try:
                        num1 = int(raw_input("Anna eka numero:"))
                        num2 = int(raw_input("Anna toka numero:"))
                        break
                except ValueError:
                        print "syota vain lukuja!"

        if valinta == 1:
                        try:
                                print num1, "+", num2,"=", summa(num1,num2)
                        except ValueError:
                                print "syota vain lukuja!"
        elif valinta == 2:
                try:
                        print num1, "-", num2,"=", vahennys(num1,num2)
                except ValueError:
                        print "Syota vain lukuja!"
        elif valinta == 3:
                try:
                        print num1, "*", num2,"=", kerto(num1,num2)
                except ValueError:
                        print "syota vain lukuja!"
        elif valinta == 4:
                try:
                        print num1, "/", num2,"=", jako(float(num1),float(num2))
                except (ZeroDivisionError):
                        print "Nollalla ei voi jakaa!"
                except ValueError:
                        print "syota numeroita, ei lukuja!"
        
        print "jatketaanko?"
        while True:
                try:
                        num3 = int(raw_input("1.Kylla \n2.Ei"))
                        break
                except ValueError:
                        print "syota vain lukuja!"
        if num3 == 1:
                kierros = 0
                print "\n"*3
        else :
                print "Suljetaan laskin!"
                kierros+=1
