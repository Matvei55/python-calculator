from math import*
List = ['+','-','*','/','#']
def is_int(s):
    try:
        int(s)
        return True
    except ValueError:
        print('ошибка,введи ЧИСЛО')
        return False
res=0
while True:
    if res!=0:
        chislo1=res
    else:
        chislo1= input('введи число под номером 1')
    if is_int(chislo1):
        chislo1 = int(chislo1)
        znak = input('введи знак')
    if znak not in List:
        print('ошибка')
    else:
        chislo2=input('введи число под номером 2')
    if is_int(chislo2):
        chislo2 = int(chislo2)
    if znak=='+':   
        res = chislo1 + chislo2
        print(res)
    elif znak=='-':   
        res = chislo1 - chislo2
        print(res)
    elif znak=='/':   
        res = chislo1 / chislo2
        print(res)
    elif znak=='*':   
        res = chislo1 * chislo2
        print(res)
    elif znak=='#':
        res = sqrt(chislo1)
        print(res)
    else:
        print('ошибка')
