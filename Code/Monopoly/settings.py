class settings:
    def run(lcd, invert, select,money,sound):
        tcolor = 1
        bcolor = 0

        if invert:
             tcolor = 0
             bcolor = 1

        lcd.fill(bcolor)
        lcd.text('EQ is exit!', 0, 0, tcolor)

        if select == 0:
            if invert:
                tcolor = 1
                bcolor = 0
            else:
                tcolor = 0
                bcolor = 1
        else:
            if invert:
                tcolor = 0
                bcolor = 1
            else:
                tcolor = 1
                bcolor = 0
        lcd.fill_rect(0,10,84,7,bcolor)
        lcd.text('Color:', 0, 10, tcolor)
        if invert:
            lcd.text('1', 47, 10, tcolor)
        else:
            lcd.text('0', 47, 10, tcolor)

        if select == 1:
            if invert:
                tcolor = 1
                bcolor = 0
            else:
                tcolor = 0
                bcolor = 1
        else:
            if invert:
                tcolor = 0
                bcolor = 1
            else:
                tcolor = 1
                bcolor = 0
        lcd.fill_rect(0,20,84,7,bcolor)
        lcd.text('Sound:', 0, 20, tcolor)
        lcd.text(str(sound), 47, 20, tcolor)

        if select == 2:
            if invert:
                tcolor = 1
                bcolor = 0
            else:
                tcolor = 0
                bcolor = 1
        else:
            if invert:
                tcolor = 0
                bcolor = 1
            else:
                tcolor = 1
                bcolor = 0
        lcd.fill_rect(0,30,84,18,bcolor)
        lcd.text('Money:', 0, 30, tcolor)
        lcd.text(str(money), 0, 40, tcolor)
        lcd.text('$', 77, 40, tcolor)
        lcd.show()
