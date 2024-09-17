Задача 1: 

![image](https://github.com/user-attachments/assets/9451b1b7-2bfd-4808-98a3-8273de54cd07)

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
![image](https://github.com/user-attachments/assets/2799ee1d-e190-44f7-9f6a-6babcd627b0e)

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



Задача 4:

![image](https://github.com/user-attachments/assets/22c36b1d-c97d-4cc3-ac08-d1d4d35c8b9c)

Листинг:

```bash
#!/bin/bash

file="$1"

id=$(grep -o -E '\b[a-zA-Z]*\b' "$file" | sort -u)
```

Вывод:

![image](https://github.com/user-attachments/assets/83a24137-4030-4a22-851b-8e5194029e1a)
![image](https://github.com/user-attachments/assets/57a15e65-c348-4e76-808b-e051b5e1d74b)



Задача 5:

![image](https://github.com/user-attachments/assets/24302247-9bab-4d15-9465-ee9818a2f5c5)

Листинг:

```bash
#!/bin/bash

file=$1

chmod 755 "./$file"

sudo cp "$file" /usr/local/bin/
```

Запуск:

![image](https://github.com/user-attachments/assets/ff797af3-4e22-4b79-b471-b07d5a08818d)

Результат:

![image](https://github.com/user-attachments/assets/d35deeb3-1055-4040-8672-aafcc5c195f4)



Задача 6:

![image](https://github.com/user-attachments/assets/4bc0c51f-e742-4284-825c-f380397dae63)

Листинг:
```C++
#include <fstream>
using namespace std;
int main() {
    ifstream in("banner.c");
    string line;
    getline(in, line);
    if (line[0] == '/') {
        if (line[1] == '/' || line[1] == '*')
            printf("Success\n");
        else {
            printf("Not success\n");
        }
    }
    else {
        printf("Not success\n");
    }
}
```
Вывод:

![image](https://github.com/user-attachments/assets/e760ddfb-064b-4023-9e30-4a7457733250)

