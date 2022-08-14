from ir_rx.nec import NEC_8
from machine import Pin, Timer, PWM
from time import sleep
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
    idtr = '';
    rlp = 0
    glp = 0
    blp = 0
    
    def mainmenu():
        from mainmenu import mainmenu
        mainmenu.run(menu.LCD, invert=menu.invert, select=menu.mainselect)
        del mainmenu        
    def monopolymenu(i = -1):
        from monopoly import monopoly
        monopoly.run(menu.LCD, invert=menu.invert, select=i, players=menu.players)
        del monopoly
        if i >=0:
            menu.blp = PWM(Pin(12), freq=1000,duty_u16=42768)
            menu.rlp = PWM(Pin(27), freq=1000,duty_u16=0)
            menu.glp = PWM(Pin(14), freq=1000,duty_u16=0)
        else:
            menu.blp = PWM(Pin(12), freq=1000,duty_u16=12768)
            menu.rlp = PWM(Pin(27), freq=1000,duty_u16=0)
            menu.glp = PWM(Pin(14), freq=1000,duty_u16=0)
        menu.ir = NEC_8(Pin(15, Pin.IN), menu.IR)
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
                if menu.mainselect < 3:
                    menu.mainselect += 1
                    menu.mainmenu()
            elif newdata == '43':
                if menu.mainselect == 0:
                    menu.startgame()
                elif menu.mainselect == 1:
                    menu.loadgame()
                    menu.startgame()
                elif menu.mainselect == 2:
                    menu.menu = 1
                    menu.settingsmenu()
                    gc.collect()
                elif menu.mainselect == 3:
                    menu.menu = 99
                    tcolor = 1
                    bcolor = 0
                    if menu.invert:
                        tcolor = 0
                        bcolor = 1
                    menu.LCD.fill(menu.invert)
                    menu.LCD.text('!СОЗДАТЕЛИ!', -1, 0, tcolor)
                    menu.LCD.text('КОМАНДА', 18, 10, tcolor)
                    menu.LCD.text('I', -2, 20, tcolor)
                    menu.LCD.text('m', 4, 20, tcolor)
                    menu.LCD.text('m', 12, 20, tcolor)
                    menu.LCD.text('e', 20, 20, tcolor)
                    menu.LCD.text('r', 27, 20, tcolor)
                    menu.LCD.text('s', 34, 20, tcolor)
                    menu.LCD.text('i', 39, 20, tcolor)
                    menu.LCD.text('v', 44, 20, tcolor)
                    menu.LCD.text('e', 51, 20, tcolor)
                    menu.LCD.text('C', 58, 20, tcolor)
                    menu.LCD.text('i', 63, 20, tcolor)
                    menu.LCD.text('t', 69, 20, tcolor)
                    menu.LCD.text('y', 76, 20, tcolor)
                    menu.LCD.text('НИКИТА И', 10, 30, tcolor)
                    menu.LCD.text('ДЕНИС', 24, 40, tcolor)
                    menu.LCD.show()
        elif menu.menu == 99:
            menu.menu = 0
            menu.mainmenu()
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
                menu.blp = PWM(Pin(12), freq=1000,duty_u16=22768)
                menu.rlp = PWM(Pin(27), freq=1000,duty_u16=22768)
                menu.glp = PWM(Pin(14), freq=1000,duty_u16=22768)
            elif newdata == '15' and len(menu.players[0]) > 1:
                menu.menu = 5
                menu.mode = True
                menu.paymenu()
                menu.IR(0,0,0)
                menu.blp = PWM(Pin(12), freq=1000,duty_u16=22768)
                menu.rlp = PWM(Pin(27), freq=1000,duty_u16=22768)
                menu.glp = PWM(Pin(14), freq=1000,duty_u16=22768)
            elif newdata == '43' and len(menu.players[0]) > 1:#>||
                menu.menu = 6
                menu.transfermenu()
                menu.IR(0,0,0)
                menu.blp = PWM(Pin(12), freq=1000,duty_u16=22768)
                menu.rlp = PWM(Pin(27), freq=1000,duty_u16=22768)
                menu.glp = PWM(Pin(14), freq=1000,duty_u16=0)
            elif newdata == '09':
                menu.menu = 4
                bcolor = 0
                tcolor = 1
                if menu.invert:
                    tcolor = 1
                    bcolor = 0
                menu.LCD.fill(bcolor)
                menu.LCD.text('BЫЙTИ?', 0, 1, tcolor)
                menu.LCD.text('>| ВЫХОД', 0, 11, tcolor)
                menu.LCD.text('EQ НАЗАД', 0, 21, tcolor)
                menu.LCD.line(8,18,8,11,tcolor)
                menu.LCD.line(7,18,7,11,tcolor)
                menu.card = False
                menu.LCD.show()
        elif menu.menu == 4:
            if newdata == '09':
                menu.menu = 3
                menu.monopolymenu()
                menu.blp = PWM(Pin(12), freq=1000,duty_u16=12768)
                menu.rlp = PWM(Pin(27), freq=1000,duty_u16=0)
                menu.glp = PWM(Pin(14), freq=1000,duty_u16=0)
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
                        menu.blp = PWM(Pin(12), freq=1000,duty_u16=0)
                        menu.rlp = PWM(Pin(27), freq=1000,duty_u16=22768)
                        menu.glp = PWM(Pin(14), freq=1000,duty_u16=0)
                    else:
                        menu.LCD.text('ПОПОЛНЕНИЕ:', 0, 0, tcolor)
                        menu.blp = PWM(Pin(12), freq=1000,duty_u16=0)
                        menu.rlp = PWM(Pin(27), freq=1000,duty_u16=0)
                        menu.glp = PWM(Pin(14), freq=1000,duty_u16=22768)
                    menu.LCD.text(str(res)+'$', 0, 10, tcolor)
                    menu.LCD.text('ПОДНЕСИТЕ', 0, 30, tcolor)
                    menu.LCD.text('КАРТУ', 0, 40, tcolor)
                        
                    if menu.sound:
                        menu.beep(freq = 1000)
                        sleep(0.2)
                        menu.beep(freq = 2000)
                elif menu.menu == 6:
                    menu.menu = 8
                    menu.LCD.fill(bcolor)
                    menu.LCD.text('ПЕРЕВОД:', 0, 0, tcolor)
                    menu.LCD.text(str(menu.bfmoney)+'$', 0, 10, tcolor)
                    menu.LCD.text('ПОДНЕСИТЕ', 0, 20, tcolor)
                    menu.LCD.text('КАРТУ ДЛЯ', 0, 30, tcolor)
                    menu.LCD.text('ОПЛАТЫ', 0, 40, tcolor)
                    menu.blp = PWM(Pin(12), freq=1000,duty_u16=0)
                    menu.rlp = PWM(Pin(27), freq=1000,duty_u16=22768)
                    menu.glp = PWM(Pin(14), freq=1000,duty_u16=0)
                    if menu.sound:
                        menu.beep(freq = 2000)
                        sleep(0.2)
                        menu.beep(freq = 1000)
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
                    if menu.sound: menu.beep()
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
                                if menu.sound:
                                    menu.beep(freq = 650)
                                sleep(2)
                                menu.monopolymenu()
                                menu.savegame()
                    elif menu.menu == 8:
                        for i in range(len(menu.players[0])):
                            if menu.players[0][i] == uuid:
                                menu.players[1][i] -= menu.bfmoney
                                menu.menu = 9
                                menu.idtr = uuid;
                                menu.LCD.fill(bcolor)
                                menu.LCD.text('ПЕРЕВОД:', 0, 0, tcolor)
                                menu.LCD.text(str(menu.bfmoney)+'$', 0, 10, tcolor)
                                menu.LCD.text('ПОДНЕСИТЕ', 0, 20, tcolor)
                                menu.LCD.text('КАРТУ ДЛЯ', 0, 30, tcolor)
                                menu.LCD.text('ПОПОЛНЕНИЯ', 0, 40, tcolor)
                                menu.LCD.show()
                                menu.blp = PWM(Pin(12), freq=1000,duty_u16=0)
                                menu.rlp = PWM(Pin(27), freq=1000,duty_u16=0)
                                menu.glp = PWM(Pin(14), freq=1000,duty_u16=22768)
                                if menu.sound:
                                    menu.beep(freq = 1000)
                                    sleep(0.2)
                                    menu.beep(freq = 2000)
                    elif menu.menu == 9:
                        for i in range(len(menu.players[0])):
                            if menu.players[0][i] == uuid and menu.idtr != uuid:
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
                                if menu.sound:
                                    menu.beep(freq = 650)
                                sleep(2)
                                menu.monopolymenu()
                                menu.savegame()
                else:
                    return False
        elif menu.menu == 3:
            menu.monopolymenu()
#         elif menu.menu == 5 or menu.menu == 6:
#             pass

    def startgame():
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
        menu.LCD.text('>|:ПЕРЕВОД', 0, 30, tcolor)
        menu.LCD.text('0-9: ВВОД', 0, 40, tcolor)
        menu.LCD.line(8,37,8,30,tcolor)
        menu.LCD.line(7,37,7,30,tcolor)
        menu.LCD.show()
        if menu.sound:
            menu.beep(time=0.2);
            sleep(0.2)
            menu.beep(time=0.2);
            sleep(0.2)
            menu.beep(time=0.2);
        sleep(4)
        menu.cardsearch()
        menu.monopolymenu()
        menu.tim.init(period=1000, mode=Timer.PERIODIC, callback=lambda t:menu.cardsearch())
        gc.collect()

    def beep(time = 0.15,freq=1200,duty_u16=32768):
        bep = PWM(Pin(2), freq=freq,duty_u16=duty_u16)
        sleep(time) 
        Pin(2,Pin.OUT).value(0)
        bep.deinit()
      
    def savesettings():
        f = open('settings.set', 'w')
        f.write(str(menu.invert)+'\n')
        f.write(str(menu.sound)+'\n')
        f.write(str(menu.money)+'\n')
        f.close()
        
    def savegame():
        f = open('game.set', 'w')
        for i in range(len(menu.players[0])):
            f.write(menu.players[0][i]+'|'+str(menu.players[1][i])+'\n')
        f.close()
        
    def loadgame():
        f = open('game.set')
        try:
            read = f.read().split('\n')
            for i in range(len(read)-1):
                sp = read[i].split('|')
                menu.players[0].append(sp[0])
                menu.players[1].append(int(sp[1]))
        except Exception:
            print('cant open game.set')
        f.close()
            
    def run(lcd):
        lcd.includechars()
        lcd.setmethod(1)
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
        menu.ir = NEC_8(Pin(15, Pin.IN), menu.IR)
        menu.tim = Timer(0)
        menu.rdr = mfrc522.MFRC522(21, 19, 18, 16, 22)
        menu.mainmenu()
        
        menu.blp = PWM(Pin(12), freq=1000,duty_u16=12768)
        menu.rlp = PWM(Pin(27), freq=1000,duty_u16=0)
        menu.glp = PWM(Pin(14), freq=1000,duty_u16=0)
        gc.collect()
        
        if menu.sound: menu.beep();
        
        print('menu')
