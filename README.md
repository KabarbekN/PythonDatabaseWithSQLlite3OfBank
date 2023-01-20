# PythonDatabaseWithSQLlite3OfBank

Бұл Python 3 және SQlite3 көмегімен банк жүйесінің дерекқорын жасау үшін қолданылады

Бастамас бұрын біз пайдаланушылар, депозит, несие атаулары бар 3 дерекқорды жасаймыз
Бұл кодтың БАРЛЫҚ ЕГЕР БАР БОЛМАСА арнайы пәрменін пайдалану себебінен қалдыруға болады

Әрбір дерекқорда нақты деректер болады
Пайдаланушылар
id БҮТІН БАСТАУЫШ КҮЙЕУ
кіру TEXT
құпия сөз TEXT
қолма-қол ақша BIGINT

несие
name_id INTEGER
month_sol INT
несиелер_сомасы INT
FROEIGN КІЛТІ (аты_идентификатор) СІЛТЕМЕЛЕР пайдаланушылар (rowid)

депозит
name_id INTEGER,
     month_sol INT,
     депозит_сомасы,
     ШЕТЕЛДІК КІЛТ(аты_идентификатор) СІЛТЕМЕЛЕР пайдаланушылар(идентификатор)

Мұнда біз банк жүйесінің әртүрлі сәттерімен жұмыс істей аламыз, мысалы:
-Тіркелу
-Кіру
- TakeCash
- Қолма-қол ақшаны қосыңыз
-UpdateClientInformation
- Клиентті жою
- Клиенттерге ақпаратты көрсету

Бұл функциялардың барлығы функцияны шақыру үшін арнайы сандарды пайдалану арқылы консоль тақтасынан іске қосылады
1, 2, 3 ... және т.б
Мұнда 6 функция олардың барлығы бағдарламаны іске қосқаннан кейін пәрмендер тақтасында көрсетіледі

Әрбір командалық бағдарламаны пайдалану үшін кейбір нұсқаулар көрсетіледі және бұл функциялар арасында шарлау оңай

Бұл кодпен жұмысты бастау үшін сізге ештеңе жүктеп алу немесе импорттау қажет емес, өйткені қазіргі уақытта sqlite3 python-мен бірге жүреді.

Сондықтан, егер сізде python орнатылған болса, ештеңе істеудің қажеті жоқ, бірақ егер сізде python болмаса, jetbrains.com сайтына өтіп, IDE pycharm орнатуға болады.
Немесе python python.com ресми веб-сайтынан python бағдарламасының соңғы нұсқасын орнатуға болады

Деректер базасы осы кодтың басынан бастап жасалады, сондықтан сізге бұл туралы қамқорлық қажет емес

Мұнда біз CREATE, SELECT, UPDATE, SET, WHERE сияқты SQl пәрмендерін қолдандық, сонымен қатар деректер базасымен жұмыс істеу үшін .db қолдандық.

Бұл пәрмендердің барлығы осы құжаттаманың басында жазылған арнайы функцияларда қолданылады


This is used to create a database of bank system with Python 3 and SQlite3 

Before we start we are creating 3 databases with names users, deposit, credit 
ALL of this code can be leaved because of using special command IF NOT EXISTS 

Every database have specific data
Users 
id INTEGER PRIMARY KEY
login TEXT
password TEXT
cash BIGINT

credit 
name_id INTEGER
month_left INT
amount_of_credits INT
FROEIGN KEY (name_id) REFERENCES users(rowid)

deposit
name_id INTEGER,
    month_left INT, 
    amount_of_deposit,
    FOREIGN KEY(name_id) REFERENCES users(id)

Here we can work with different moments of banking system such as:
-Register  Works by INSERT INTO function
-Login  Works by SELECT 
-TakeCash  WORKS BY Select 
-AddCash
-UpdateClientInformation
-Delete Client
-Show Clients Infromation
-Take credit 
-open Deposit 
-credited clients
-AScending ordering
-Descending Ordering
-Search specific user
-filter function

All of this functions runs from console panel just by using cpecial numbers to call a function
Like 1, 2, 3 ... and etc
There 6 functoion all of them will be showed on command panel after starting a programme

To use every command programme will show some instructions and it is easy to navigate between this functions

To start work with this code you do not need to download or importing anything because sqlite3 nowadays go with python 

So you do not need to do anythig if you have already installed python, but if you do not have python you can go to jetbrains.com and install IDE pycharm
Or just from offical website of python python.com you can install last version of python

Database will be created from the beggining of this code so you dont need to care about this

Here We used SQl commands like CREATE, SELECT, UPDATE, SET, WHERE, also using .db to work with our data base

All of this commands used in specific functions that was already written in the beginning of this documentation
