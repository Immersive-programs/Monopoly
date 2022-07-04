from ir_rx.nec import NEC_8
from machine import Pin, Timer
from utime import sleep
import gc
import mfrc522
class menu:

    mainselect = 0
    LCD = None
    tim = None
    menu = 0
    invert = False
    sselect = 0
    money = 1500
    sound = True
    players = [[],[]]
    mode = False;
    bfmoney = 0
    bfresult = 0

    def mainmenu():
        from mainmenu import mainmenu
        mainmenu.run(menu.LCD, invert=menu.invert, select=menu.mainselect)
        del mainmenu

    def monopolymenu(i = -1):
        from monopoly import monopoly
        monopoly.run(menu.LCD, invert=menu.invert, select=i, players=menu.players)
        del monopoly

    def settingsmenu():
        from settings import settings
        settings.run(menu.LCD, invert=menu.invert, select=menu.sselect, money = menu.money, sound = menu.sound)
        del settings

    def paymenu():
        from paymenu import paymenu
        paymenu.run(menu.LCD, invert=menu.invert, select=menu.mainselect, mode = menu.mode)
        del paymenu

    def transfermenu():
        from transfer import transfer
        transfer.run(menu.LCD, invert=menu.invert, select=menu.mainselect)
        del transfer

    def IR(data, addr, ctrl):
        newdata = '{:02x}'.format(data)
        if menu.menu == 0:
            if newdata == '44':
                if menu.mainselect > 0:
                    menu.mainselect -= 1
                    menu.mainmenu()
            elif newdata == '40':
                if menu.mainselect < 1:
                    menu.mainselect += 1
                    menu.mainmenu()
            elif newdata == '43':
                if menu.mainselect == 0:
                    menu.menu = 3
                    tcolor = 1
                    bcolor = 0
                    if menu.invert:
                        tcolor = 0
                        bcolor = 1
                    menu.LCD.fill(menu.invert)
                    menu.LCD.text('УПРАВЛЕНИЕ:', 0, 0, tcolor)
                    menu.LCD.text('EQ', 0, 10, tcolor)
                    menu.LCD.text('CH:ВЫХОД', 17, 10, tcolor)
                    menu.LCD.text('+/-: БAHK', 0, 20, tcolor)
                    menu.LCD.text('> :ПЕРЕВОД', 0, 30, tcolor)
                    menu.LCD.text('0-9: ВВОД', 0, 40, tcolor)
                    menu.LCD.show()
                    sleep(5)
                    menu.cardsearch()
                    menu.monopolymenu()
                    menu.tim.init(period=1000, mode=Timer.PERIODIC, callback=lambda t:menu.cardsearch())
                    gc.collect()
                elif menu.mainselect == 1:
                    menu.menu = 1
                    menu.settingsmenu()
                    gc.collect()
        elif menu.menu == 1:
            if newdata == '09':
                menu.menu = 0
                menu.mainmenu()
                gc.collect()
            elif newdata == '44':
                if menu.sselect > 0:
                    menu.sselect -= 1
                    menu.settingsmenu()
            elif newdata == '40':
                if menu.sselect < 2:
                    menu.sselect += 1
                    menu.settingsmenu()
            elif newdata == '43':
                if menu.sselect == 0:
                    if menu.invert:
                        menu.invert = False
                    else:
                        menu.invert = True
                    menu.savesettings()
                    menu.settingsmenu()
                if menu.sselect == 1:
                    if menu.sound:
                        menu.sound = False
                    else:
                        menu.sound = True
                    menu.savesettings()
                    menu.settingsmenu()
                if menu.sselect == 2:
                    menu.menu = 2
                    gc.collect()
        elif menu.menu == 2:
            bcolor = 0
            tcolor = 1
            if newdata == '09':
                if len(str(menu.money)) == 1:
                    menu.money = 0
                else:
                    menu.money = int(str(menu.money)[:-1])
            elif newdata == '0c':#1
                if len(str(menu.money)) < 4:
                    if menu.money == 0:
                        menu.money = 1
                    else:
                        menu.money = int(str(menu.money)+'1')
            elif newdata == '18':#2
                if len(str(menu.money)) < 4:
                    if menu.money == 0:
                        menu.money = 2
                    else:
                        menu.money = int(str(menu.money)+'2')
            elif newdata == '5e':#3
                if len(str(menu.money)) < 4:
                    if menu.money == 0:
                        menu.money = 3
                    else:
                        menu.money = int(str(menu.money)+'3')
            elif newdata == '08':#4
                if len(str(menu.money)) < 4:
                    if menu.money == 0:
                        menu.money = 4
                    else:
                        menu.money = int(str(menu.money)+'4')
            elif newdata == '1c':#5
                if len(str(menu.money)) < 4:
                    if menu.money == 0:
                        menu.money = 5
                    else:
                        menu.money = int(str(menu.money)+'5')
            elif newdata == '5a':#6
                if len(str(menu.money)) < 4:
                    if menu.money == 0:
                        menu.money = 6
                    else:
                        menu.money = int(str(menu.money)+'6')
            elif newdata == '42':#7
                if len(str(menu.money)) < 4:
                    if menu.money == 0:
                        menu.money = 7
                    else:
                        menu.money = int(str(menu.money)+'7')
            elif newdata == '52':#8
                if len(str(menu.money)) < 4:
                    if menu.money == 0:
                        menu.money = 8
                    else:
                        menu.money = int(str(menu.money)+'8')
            elif newdata == '4a':#9
                if len(str(menu.money)) < 4:
                    if menu.money == 0:
                        menu.money = 9
                    else:
                        menu.money = int(str(menu.money)+'9')
            elif newdata == '16':#0
                if len(str(menu.money)) < 4:
                    if menu.money == 0:
                        menu.money = 0
                    else:
                        menu.money = int(str(menu.money)+'0')
            elif newdata == '19':#+100
                if len(str(menu.money)) < 3:
                    if menu.money == 0:
                        menu.money = 100
                    else:
                        menu.money = int(str(menu.money)+'100')
            elif newdata == '0d':#+200
                if len(str(menu.money)) < 3:
                    if menu.money == 0:
                        menu.money = 200
                    else:
                        menu.money = int(str(menu.money)+'200')
            if menu.invert:
                tcolor = 1
                bcolor = 0
            else:
                tcolor = 0
                bcolor = 1
            menu.LCD.fill_rect(0,40,76,7,bcolor)
            menu.LCD.text('new:'+str(menu.money), 0, 40, tcolor)
            menu.LCD.show()
            if newdata == '43':
                menu.menu = 1
                menu.settingsmenu()
                menu.savesettings()
                gc.collect()
        elif menu.menu == 3:
            if newdata == '07' and len(menu.players[0]) > 1:
                menu.menu = 5
                menu.mode = False
                menu.paymenu()
                menu.IR(0,0,0)
            elif newdata == '15' and len(menu.players[0]) > 1:
                menu.menu = 5
                menu.mode = True
                menu.paymenu()
                menu.IR(0,0,0)
            elif newdata == '43' and len(menu.players[0]) > 1:#>||
                menu.menu = 6
                menu.transfermenu()
                menu.IR(0,0,0)
            elif newdata == '09':
                menu.menu = 4
                bcolor = 0
                tcolor = 1
                if menu.invert:
                    tcolor = 1
                    bcolor = 0
                menu.LCD.fill(bcolor)
                menu.LCD.text('BЫЙTИ?', 0, 0, tcolor)
                menu.LCD.text('>|| ВЫХОД', 0, 10, tcolor)
                menu.LCD.text('EQ  НАЗАД', 0, 20, tcolor)
                menu.card = False
                menu.LCD.show()
        elif menu.menu == 4:
            if newdata == '09':
                menu.menu = 3
                menu.monopolymenu()
            elif newdata == '43':
                menu.menu = 0
                menu.mainmenu()
                menu.players = [[],[]]
                menu.tim.deinit()
        elif menu.menu == 5 or menu.menu == 6:
            if newdata == '46':
                menu.menu = 3
                menu.bfmoney = 0
                menu.bfresult = 0
                menu.monopolymenu()
            elif newdata == '09':
                if len(str(menu.bfmoney)) == 1:
                    menu.bfmoney = 0
                else:
                    menu.bfmoney = int(str(menu.bfmoney)[:-1])
            elif newdata == '0c':#1
                if len(str(menu.bfmoney)) < 4:
                    if menu.bfmoney == 0:
                        menu.bfmoney = 1
                    else:
                        menu.bfmoney = int(str(menu.bfmoney)+'1')
            elif newdata == '18':#2
                if len(str(menu.bfmoney)) < 4:
                    if menu.bfmoney == 0:
                        menu.bfmoney = 2
                    else:
                        menu.bfmoney = int(str(menu.bfmoney)+'2')
            elif newdata == '5e':#3
                if len(str(menu.bfmoney)) < 4:
                    if menu.bfmoney == 0:
                        menu.bfmoney = 3
                    else:
                        menu.bfmoney = int(str(menu.bfmoney)+'3')
            elif newdata == '08':#4
                if len(str(menu.bfmoney)) < 4:
                    if menu.bfmoney == 0:
                        menu.bfmoney = 4
                    else:
                        menu.bfmoney = int(str(menu.bfmoney)+'4')
            elif newdata == '1c':#5
                if len(str(menu.bfmoney)) < 4:
                    if menu.bfmoney == 0:
                        menu.bfmoney = 5
                    else:
                        menu.bfmoney = int(str(menu.bfmoney)+'5')
            elif newdata == '5a':#6
                if len(str(menu.bfmoney)) < 4:
                    if menu.bfmoney == 0:
                        menu.bfmoney = 6
                    else:
                        menu.bfmoney = int(str(menu.bfmoney)+'6')
            elif newdata == '42':#7
                if len(str(menu.bfmoney)) < 4:
                    if menu.bfmoney == 0:
                        menu.bfmoney = 7
                    else:
                        menu.bfmoney = int(str(menu.bfmoney)+'7')
            elif newdata == '52':#8
                if len(str(menu.bfmoney)) < 4:
                    if menu.bfmoney == 0:
                        menu.bfmoney = 8
                    else:
                        menu.bfmoney = int(str(menu.bfmoney)+'8')
            elif newdata == '4a':#9
                if len(str(menu.bfmoney)) < 4:
                    if menu.bfmoney == 0:
                        menu.bfmoney = 9
                    else:
                        menu.bfmoney = int(str(menu.bfmoney)+'9')
            elif newdata == '16':#0
                if len(str(menu.bfmoney)) < 4:
                    if menu.bfmoney == 0:
                        menu.bfmoney = 0
                    else:
                        menu.bfmoney = int(str(menu.bfmoney)+'0')
            elif newdata == '19':#+100
                if len(str(menu.bfmoney)) < 3:
                    if menu.bfmoney == 0:
                        menu.bfmoney = 100
                    else:
                        menu.bfmoney = int(str(menu.bfmoney)+'100')
            elif newdata == '0d':#+200
                if len(str(menu.bfmoney)) < 3:
                    if menu.bfmoney == 0:
                        menu.bfmoney = 200
                    else:
                        menu.bfmoney = int(str(menu.bfmoney)+'200')
            elif newdata == '43' :#>||
                bcolor = 0
                tcolor = 1
                if menu.invert:
                    tcolor = 1
                    bcolor = 0
                if menu.menu == 5:
                    menu.menu = 7
                    menu.LCD.fill(bcolor)
                    res = menu.bfresult + (menu.bfmoney*-1)
                    if menu.mode:
                        res = menu.bfresult + menu.bfmoney
                    if res < 0:
                        menu.LCD.text('К ВЫЧЕТУ:', 0, 0, tcolor)
                    else:
                        menu.LCD.text('ПОПОЛНЕНИЕ:', 0, 0, tcolor)
                    menu.LCD.text(str(res)+'$', 0, 10, tcolor)
                    menu.LCD.text('ПОДНЕСИТЕ', 0, 30, tcolor)
                    menu.LCD.text('КАРТУ', 0, 40, tcolor)
                elif menu.menu == 6:
                    menu.menu = 8
                    menu.LCD.fill(bcolor)
                    menu.LCD.text('ПЕРЕВОД:', 0, 0, tcolor)
                    menu.LCD.text(str(menu.bfmoney)+'$', 0, 10, tcolor)
                    menu.LCD.text('ПОДНЕСИТЕ', 0, 20, tcolor)
                    menu.LCD.text('КАРТУ ДЛЯ', 0, 30, tcolor)
                    menu.LCD.text('ОПЛАТЫ', 0, 40, tcolor)
                menu.LCD.show()
            elif newdata == '07' and menu.menu == 5:#-
                res = menu.bfresult + (menu.bfmoney*-1)
                if menu.mode:
                    res = menu.bfresult + menu.bfmoney
                menu.bfresult = res
                menu.mode = False
                menu.bfmoney = 0
            elif newdata == '15' and menu.menu == 5:#+
                res = menu.bfresult + (menu.bfmoney*-1)
                if menu.mode:
                    res = menu.bfresult + menu.bfmoney
                menu.bfresult = res
                menu.mode = True
                menu.bfmoney = 0
            if  newdata != '43':
                tcolor = 1
                if menu.invert:
                    tcolor = 0
                if menu.menu == 5:
                    menu.paymenu()
                else:
                    menu.transfermenu()
                menu.LCD.text(str(menu.bfmoney)+'$', 7, 20, tcolor)
                if menu.menu == 5:
                    res = menu.bfresult + (menu.bfmoney*-1)
                    if menu.mode:
                        res = menu.bfresult + menu.bfmoney
                    if res < 0:
                        menu.LCD.text('-', 0, 40, tcolor)
                        res = res * -1
                    else:
                        menu.LCD.text('+', 0, 40, tcolor)
                    menu.LCD.text(str(res)+'$', 7, 40, tcolor)
                menu.LCD.show()
        elif newdata == '46' and (menu.menu == 7 or menu.menu == 8):
            menu.menu = 3
            menu.bfmoney = 0
            menu.bfresult = 0
            menu.monopolymenu()

    def cardsearch():
        (stat, tag_type) = menu.rdr.request(menu.rdr.REQIDL)
        if stat == menu.rdr.OK:
            (stat, raw_uid) = menu.rdr.anticoll()
            if stat == menu.rdr.OK:
                if menu.menu == 3:
                    uuid = "0x%02x%02x%02x%02x" % (raw_uid[0], raw_uid[1], raw_uid[2], raw_uid[3])
                    for i in range(len(menu.players[0])):
                        if menu.players[0][i] == uuid:
                            menu.monopolymenu(i)
                            return False
                    menu.players[0].append(uuid)
                    menu.players[1].append(menu.money)
                    menu.monopolymenu()
                elif menu.menu == 7 or menu.menu == 8 or menu.menu == 9:
                    uuid = "0x%02x%02x%02x%02x" % (raw_uid[0], raw_uid[1], raw_uid[2], raw_uid[3])
                    tcolor = 1
                    bcolor = 0
                    if menu.invert:
                         tcolor = 0
                         bcolor = 1
                    if menu.menu == 7:
                        for i in range(len(menu.players[0])):
                            if menu.players[0][i] == uuid:
                                res = menu.bfresult + (menu.bfmoney*-1)
                                if menu.mode:
                                    res = menu.bfresult + menu.bfmoney
                                menu.players[1][i] += res
                                menu.bfresult = 0
                                menu.bfmoney = 0
                                menu.menu = 3
                                menu.LCD.fill(bcolor)
                                menu.LCD.circle(22,40,22,tcolor,1.183)
                                menu.LCD.circle(21,40,22,tcolor,1.183)
                                menu.LCD.line(25,10,38,36,tcolor)
                                menu.LCD.line(55,10,38,36,tcolor)
                                menu.LCD.line(25,11,38,37,tcolor)
                                menu.LCD.line(55,11,38,37,tcolor)
                                menu.LCD.show()
                                sleep(3.5)
                                menu.monopolymenu()
                    elif menu.menu == 8:
                        for i in range(len(menu.players[0])):
                            if menu.players[0][i] == uuid:
                                menu.players[1][i] -= menu.bfmoney
                                menu.menu = 9
                                menu.LCD.fill(bcolor)
                                menu.LCD.text('ПЕРЕВОД:', 0, 0, tcolor)
                                menu.LCD.text(str(menu.bfmoney)+'$', 0, 10, tcolor)
                                menu.LCD.text('ПОДНЕСИТЕ', 0, 20, tcolor)
                                menu.LCD.text('КАРТУ ДЛЯ', 0, 30, tcolor)
                                menu.LCD.text('ПОПОЛНЕНИЯ', 0, 40, tcolor)
                                menu.LCD.show()
                    elif menu.menu == 9:
                        for i in range(len(menu.players[0])):
                            if menu.players[0][i] == uuid:
                                menu.players[1][i] += menu.bfmoney
                                menu.bfresult = 0
                                menu.bfmoney = 0
                                menu.menu = 3
                                menu.LCD.fill(bcolor)
                                menu.LCD.circle(22,40,22,tcolor,1.183)
                                menu.LCD.circle(21,40,22,tcolor,1.183)
                                menu.LCD.line(25,10,38,36,tcolor)
                                menu.LCD.line(55,10,38,36,tcolor)
                                menu.LCD.line(25,11,38,37,tcolor)
                                menu.LCD.line(55,11,38,37,tcolor)
                                menu.LCD.show()
                                sleep(3.5)
                                menu.monopolymenu()
                else:
                    return False
        elif menu.menu == 3:
            menu.monopolymenu()

    def savesettings():
        f = open('settings.set', 'w')
        f.write(str(menu.invert)+'\n')
        f.write(str(menu.sound)+'\n')
        f.write(str(menu.money)+'\n')
        f.close()

    def run(lcd):
        lcd.includechars()
        lcd.setmethod(1)
#         menu.do_read()
        try:
            f = open('settings.set')
            read = f.read().split('\n')
            if read[0] == 'True':
                menu.invert = True
            else:
                menu.invert = False
            if read[1] == 'True':
                menu.sound = True
            else:
                menu.sound = False
            menu.money = int(read[2])
            f.close()
        except Exception:
            menu.savesettings()
        menu.LCD = lcd
        ir = NEC_8(Pin(19, Pin.IN), menu.IR)
        menu.tim = Timer(0)
        menu.rdr = mfrc522.MFRC522(32, 33, 25, 14, 12)
        menu.mainmenu()
        #menu.tim.init(period=1000, mode=Timer.PERIODIC, callback=lambda t:menu.cardsearch())
        print('menu')

