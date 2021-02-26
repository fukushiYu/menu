#!/usr/bin/python3
import menu_i
#---------------------------------------------------------------
menu=r''' Menu
    1) 檢查service
    x) quit
    select :'''
r = "\x1b[2J\x1b[H"
menu=r+menu
k = input(menu)
while k!='x':
    if(k in ['1']):
        print(r)
        if(k=='1'):
            menu_i.check_services()
        input('Press Enter to continue...')
    k = input(menu)
print('End...')
#---------------------------------------------------------------

