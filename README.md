# OLD Monopoly

## Проект электронного терминала для игры Monopoly.

### Особенности:
- RFID карты (безконтакная оплата);
- Нет клавиатуры (Безконтактный ввод);
- Звуковая индикация;
- световая индикация.

### Компанентная база:
- Контроллер ESP32;
- Pcd8544 LCD дисплей;
- IR(nec) Приёмник сигнала;
- Mfrc522 Модуль для работы с RFID;
- Трёх цветный светодиод;
- Макетная плата под ESP.
- IR пульт "Car MP3 TZT"
- Зуммер 3.3V
- Понижаюший модуль 3.3V

### Зачем?:
- Терминал используется для замены бумажных денег на электронные карты, что значительно оптимизирует и ускоряет игровой процес. 

### Как играть?:
1. "Новая игра"
2. Поднести по очереди как минимум две карты с RFID
- Терминал будет отображать баланс каждого игрока(чтобы узнать какая карта привязана к счёту необходимо повторно поднести карту)
3. С помощью клавиш пульта ">||","+"/"-" выбрать необходимою операцию с балансом игроков  
4. "Подтвердить операцию картой"

### Дополнительные возможности:
- Востановить предыдущею игру (сохранение происходит после каждой банковской операции)
- Настройка:
  - Инвертировать пиксели экрана;
  - Отключение/Включение звуковой индикации; 
  - Выставление начаного счёта у игроков.
  
### Подключение компанентов: 
- Display:
  Название контакта дисплея | IO порт
  --- | ---
  BL | 13
  RST | 17
  CE | 32
  DC | 33
  DIR | 25
  CLK | 26

- RFID:
  Контакт | IO порт
  --- | ---
  SDA | 22
  SCK | 21
  MOSI | 19
  MI | 18
  SQI | 5
  RST | 16
  
- LEDS:
  Cветодтод | IO порт
  --- | ---
  R | 27
  G | 14
  B | 12
  
- Buzzer:
  Питание | IO порт
  --- | ---
  Power | 2

- IR:
  Выход с ИК приёмника | IO порт
  --- | ---
  DATA OUT | 15

### Если есть 3D принтер:
- В разделе "3D Models For Print" есть необходимые файлы для печати корпуса (Разработаны при помощи программы FreeCAD)
  - печать всех деталей проводилась с ширеной линий 0.2 mm и заполнением 100%
  - из-за не соверженства 3D модели "Monopoly-Крыша верх" пластик может немного потечь

### Реализация програмной части создовалась на MicroPython.

### Используемые библеотеки:
- micropython_ir -> https://github.com/peterhinch/micropython_ir
- micropython-mfrc522 -> https://github.com/cefn/micropython-mfrc522
- micropython-pcd8544 -> https://github.com/mcauser/micropython-pcd8544

### Деменстрация: 
- Фото:
  - ![IMG_20220904_155715](https://user-images.githubusercontent.com/80697141/188309613-837af193-8d40-41a5-9a95-b12475f34ae7.jpg)
- Видео:
  -  todo

