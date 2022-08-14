class mainmenu:
    def run(lcd, invert, select):
        tcolor = 1
        bcolor = 0
        if invert:
             tcolor = 0
             bcolor = 1
        lcd.fill(bcolor)
        lcd.text('МОНОПОЛИЯ:', -1, 0, tcolor)
        lcd.fill_rect(10,10,84,7,bcolor)
        lcd.text('НОВАЯ', -1, 10, tcolor)
        lcd.text('ИГРА', 40, 10, tcolor)
        
        lcd.text('В ', -1, 20, tcolor)
        lcd.text('О ', 6, 20, tcolor)
        lcd.text('С ', 13, 20, tcolor)
        lcd.text('Т ', 20, 20, tcolor)
        lcd.text('А ', 27, 20, tcolor)
        lcd.text('Н ', 34, 20, tcolor)
        lcd.text('О ', 41, 20, tcolor)
        lcd.text('В ', 48, 20, tcolor)
        lcd.text('И ', 55, 20, tcolor)
        lcd.text('Т ', 62, 20, tcolor)
        lcd.text('Ь ', 69, 20, tcolor)
        
        lcd.text('НАСТРОЙКИ', -1, 30, tcolor)
        lcd.text('О НАС', -1, 40, tcolor)
        
        lcd.text('НАСТРОЙКИ', -1, 30, tcolor)
        if select == 0:
            lcd.text('<', 76, 10, tcolor)
        elif select == 1:
            lcd.text('<', 76, 20, tcolor)
        elif select == 2:
            lcd.text('<', 76, 30, tcolor)
        elif select == 3:
            lcd.text('<', 76, 40, tcolor)
            
        lcd.show()
