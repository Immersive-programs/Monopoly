class transfer:
    def run(lcd, invert, select):
        tcolor = 1
        bcolor = 0
        if invert:
             tcolor = 0
             bcolor = 1
        lcd.fill(bcolor)
        lcd.text('БАНКОВСКИЙ', -1, 1, tcolor)
        lcd.text('ПЕРЕВОД:', 0, 11, tcolor)
        lcd.text('>', -1, 21, tcolor)
        lcd.show()
