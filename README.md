Задача 1: 

cut -d: -f1 passwd.txt | sort

cut - это утилита, которая используется для извлечения определенных полей

-d - это параметр, показывающий разделитель

-f1 - это параметр, показывающий, какой столбец будет считан

| - это оператор, указывающий на то, куда будут переданы данные из cut 
 
sort - утилита, сортирующая данные

Пример вывода:

![image](https://github.com/user-attachments/assets/fab17614-56bc-45fc-8e16-017e7878b2d5)

Файл:

![image](https://github.com/user-attachments/assets/17e200f6-50a1-42aa-a8d1-099f386daf8a)


Задача 2:

cat /etc/protocols | tail +8| sort | head -5
 
head - утилита, считывающая первые 10 строк в базавой настройке

tail - утилита обратная по смыслу head

tail +8 нужно чтобы исключить строки с объяснениями

![image](https://github.com/user-attachments/assets/8823e2c5-19f4-4bee-a6cf-46679726a74e)

Файл:

![image](https://github.com/user-attachments/assets/08e32145-c279-45af-8b97-93b5ffa90b53)


Задача 3:

![image](https://github.com/user-attachments/assets/5d6b736f-8052-44a7-8fa0-6dd24fa68183)

Листинг:
```C
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <readline/readline.h>

int main()
{
	char *a = readline("Введите текст: ");
	for (int i = 0; i < strlen(a) + 2; i++)
	{
		if (i == 0 || i == strlen(a) + 1)
			printf("+");
		else
			printf("-");
	}
	printf("\n");
	printf("|%s|\n", a);
	for (int i = 0; i < strlen(a) + 2; i++)
	{
		if (i == 0 || i == strlen(a) + 1)
			printf("+");
		else
			printf("-");
	}
	printf("\n");
	free(a);
	return 0;
}
```

Вывод:

![image](https://github.com/user-attachments/assets/64564be7-c45b-4fff-8196-b09f3ad30d16)
