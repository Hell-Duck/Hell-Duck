![image](https://github.com/user-attachments/assets/6c158b97-4e3c-4d2c-95ec-cce019e96037)

Служебная информация о пакете matplotlib:

![image](https://github.com/user-attachments/assets/27c588c9-7667-4c9b-90d6-5b7cb1b36560)

Основные элементы содержимого файла со служебной информацией из пакета:

Name: Название пакета.

Version: Текущая версия пакета.

Summary: Краткое описание пакета.

Home-page: Ссылка на домашнюю страницу пакета.

Author: Авторы пакета.

Author-email: Электронная почта авторов.

License: Лицензия пакета.

Location: Расположение установленного пакета.

Requires: Список зависимых пакетов, необходимых для работы.

Required-by: Список пакетов, которые зависят от matplotlib.

Чтобы получить пакет без менеджера пакетов, прямо из репозитория нужно перейти по ссылке: https://matplotlib.org




![image](https://github.com/user-attachments/assets/b1061b22-8d0c-428c-8bb1-d1fdf2b4bb1a)

![image](https://github.com/user-attachments/assets/055cea4b-127d-4e35-a900-5ffc04a2ee96)
Чтобы получить пакет без менеджера пакетов, прямо из репозитория нужно перейти по ссылке: http://expressjs.com/


![image](https://github.com/user-attachments/assets/775ce48d-2319-4157-aadb-a7695dfe8cc4)
matplotlib:
![image](https://github.com/user-attachments/assets/dff1d6ee-af31-4c7a-ac5d-f341b1cfa275)
express:
![image](https://github.com/user-attachments/assets/5d069fae-e8d6-4b65-91fd-15d415d46529)




![image](https://github.com/user-attachments/assets/711c54e7-302a-460f-9cff-81584ba07e76)

```MiniZinc
include "globals.mzn";

var 0..9: d1;  
var 0..9: d2; 
var 0..9: d3;  
var 0..9: d4; 
var 0..9: d5;  
var 0..9: d6; 

constraint all_different([d1, d2, d3, d4, d5, d6]);

constraint d1 + d2 + d3 = d4 + d5 + d6;  

solve minimize d1 * 100000 + d2 * 10000 + d3 * 1000 + d4 * 100 + d5 * 10 + d6;
```
Вывод:

d1 = 4;
d2 = 3;
d3 = 2;
d4 = 8;
d5 = 1;
d6 = 0;
----------
d1 = 3;
d2 = 4;
d3 = 2;
d4 = 8;
d5 = 1;
d6 = 0;
----------
d1 = 2;
d2 = 4;
d3 = 3;
d4 = 8;
d5 = 1;
d6 = 0;
----------
d1 = 2;
d2 = 3;
d3 = 4;
d4 = 8;
d5 = 1;
d6 = 0;
----------
d1 = 1;
d2 = 4;
d3 = 3;
d4 = 6;
d5 = 2;
d6 = 0;
----------
d1 = 1;
d2 = 3;
d3 = 4;
d4 = 6;
d5 = 2;
d6 = 0;
----------
d1 = 1;
d2 = 2;
d3 = 6;
d4 = 5;
d5 = 4;
d6 = 0;
----------
d1 = 1;
d2 = 2;
d3 = 6;
d4 = 4;
d5 = 5;
d6 = 0;
----------
d1 = 0;
d2 = 5;
d3 = 4;
d4 = 6;
d5 = 2;
d6 = 1;
----------
d1 = 0;
d2 = 4;
d3 = 5;
d4 = 6;
d5 = 2;
d6 = 1;
----------
d1 = 0;
d2 = 2;
d3 = 6;
d4 = 4;
d5 = 3;
d6 = 1;
----------
d1 = 0;
d2 = 2;
d3 = 6;
d4 = 3;
d5 = 4;
d6 = 1;
----------
d1 = 0;
d2 = 1;
d3 = 8;
d4 = 4;
d5 = 3;
d6 = 2;
----------
d1 = 0;
d2 = 1;
d3 = 8;
d4 = 3;
d5 = 4;
d6 = 2;
----------
d1 = 0;
d2 = 1;
d3 = 8;
d4 = 2;
d5 = 4;
d6 = 3;
----------
d1 = 0;
d2 = 1;
d3 = 8;
d4 = 2;
d5 = 3;
d6 = 4;
----------


![image](https://github.com/user-attachments/assets/705ffa7e-89cb-485e-89be-3dcf5e3b2891)

```MiniZinc
set of int: MenuVersion = {100, 110, 120, 130, 150};
set of int: DropdownVersion = {230, 220, 210, 200, 180};
set of int: IconsVersion = {100, 200};

var MenuVersion: menu;
var DropdownVersion: dropdown;
var IconsVersion: icons;

constraint if menu >= 110 then dropdown >= 200 else dropdown = 180 endif;

constraint if dropdown <= 200 /\ dropdown > 180 then icons = 200 else icons = 100 endif;

solve satisfy;
```

Вывод:

menu = 100;
dropdown = 180;
icons = 100;




