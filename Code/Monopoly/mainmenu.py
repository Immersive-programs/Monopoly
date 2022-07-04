class mainmenu:
    def run(lcd, invert, select):
        tcolor = 1
        bcolor = 0
        if invert:
             tcolor = 0
             bcolor = 1
        lcd.fill(bcolor)
        lcd.text('РЕЖИМ:', 0, 0, tcolor)
        lcd.fill_rect(10,10,84,7,bcolor)
        lcd.text('МОНОПОЛИЯ', 0, 10, tcolor)
        lcd.fill_rect(40,40,84,7,bcolor)
        lcd.text('НАСТРОЙКИ', 0, 40, tcolor)
        if select == 0:
            lcd.text('<', 76, 10, tcolor)
        elif select == 1:
            lcd.text('<', 76, 40, tcolor)
        lcd.show()
