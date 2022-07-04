class paymenu:
    def run(lcd, invert, select, mode):
        tcolor = 1
        bcolor = 0
        if invert:
             tcolor = 0
             bcolor = 1
        lcd.fill(bcolor)
        lcd.text('БАНКОВСКАЯ', -1, 0, tcolor)
        lcd.text('ОПЕРАЦИЯ:', -1, 10, tcolor)
        if mode:
            lcd.text('+', -1, 20, tcolor)
        else:
            lcd.text('-', -1, 20, tcolor)
        lcd.text('ИТОГО:', -1, 30, tcolor)
        lcd.text('', -1, 0, tcolor)
        lcd.show()

