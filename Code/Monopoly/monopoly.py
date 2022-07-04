class monopoly:
    def run(lcd, invert, select, players):
        tcolor = 1
        bcolor = 0

        if invert:
             tcolor = 0
             bcolor = 1

        lcd.fill(bcolor)
        if len(players[0]) > 0:
            if len(players[0]) == 1:
                lcd.text('ОТ', -1, 40, tcolor)
                lcd.text('2',17, 40, tcolor)
                lcd.text('ИГРОКОВ', 27, 40, tcolor)
            for i in range(len(players[0])):
                h = i*10

                if select == i:
                    if invert:
                        tcolor = 1
                        lcd.fill_rect(0,h,84,7,0)
                    else:
                        tcolor = 0
                        lcd.fill_rect(0,h,84,7,1)
                else:
                    tcolor = 1
                    bcolor = 0

                    if invert:
                        tcolor = 0
                        bcolor = 1

                lcd.text(str(i+1), -1, h, tcolor)
                lcd.text('И', 6, h, tcolor)
                lcd.text('Г', 14, h, tcolor)
                lcd.text('Р', 20, h, tcolor)
                lcd.text('О', 27, h, tcolor)
                lcd.text('К', 34, h, tcolor)

                lcd.pixel(41,h+2,tcolor)
                lcd.pixel(41,h+4,tcolor)

                tm = len(str(players[1][i]))
                w = 77 - tm * 7
                for b in range(tm):
                    nw = w + b*7
                    lcd.text(str(players[1][i])[b], nw, h, tcolor)
                lcd.text('$', 77, h, tcolor)
        else:
            lcd.text('ПОДНЕСИТЕ', 0, 0, tcolor)
            lcd.text('КАРТУ', 0, 10, tcolor)
            lcd.text('ДЛЯ', 0, 20, tcolor)
            lcd.text('ДОБАВЛЕНИЯ', 0, 30, tcolor)
            lcd.text('ИГРОКА', 0, 40, tcolor)
        lcd.show()
