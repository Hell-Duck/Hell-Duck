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

Задача 7:

![image](https://github.com/user-attachments/assets/c5654626-61b1-491d-81bf-137de31a2ac9)

Листинг: 

```C++
#include <iostream>
#include <filesystem>
#include <unordered_map>
#include <vector>
#include <fstream>
using namespace std;
namespace fs = filesystem;

string compute_hash(const fs::path& filePath) {
    ifstream file(filePath, ios::binary);
    string hash(istreambuf_iterator<char>(file), {});
    return hash;
}

int main(int argc, char* argv[]) {
    if (argc != 2) {
        cerr << "Использование: " << argv[0] << " <путь>" << endl;
        return 1;
    }

    fs::path dirPath(argv[1]);
    if (!fs::exists(dirPath) || !fs::is_directory(dirPath)) {
        cerr << "Указанный путь не является директорией." << endl;
        return 1;
    }
    unordered_map<string, vector<fs::path>> fileHashes;
    for (const auto& entry : fs::recursive_directory_iterator(dirPath)) {
        if (fs::is_regular_file(entry)) {
            string fileHash = compute_hash(entry);
            fileHashes[fileHash].push_back(entry);
        }
    }
    for (const auto& [hash, paths] : fileHashes) {
        if (paths.size() > 1) {
            cout << "Найдены дубликаты файлов с хэшем: " << hash << endl;
            for (const auto& path : paths) {
                cout << "    " << path << endl;
            }
            cout << endl;
        }
    }

    return 0;
}

```

Вывод:

//В файлах in и out перед запуском программы содержимое сделали одинаковым

![image](https://github.com/user-attachments/assets/10f375f9-13e5-47be-aaf2-925dd91a42ed)

Задача 8:

![image](https://github.com/user-attachments/assets/7cf37cfb-789b-47e1-b20a-c8f26da358d0)
Листинг:
```bash
#!/bin/bash

files=( $(find . -type f -name "*.$1") )

tar -cvf "archive.tar" "${files[@]}"

echo "Архив создан"
```
Пример ввода и вывода:

![image](https://github.com/user-attachments/assets/1e7438cd-3ef7-40d1-b44c-96e1a90e73cc)

Пример архива:

![image](https://github.com/user-attachments/assets/29605dea-1f80-4d72-b6f1-60ab5300af1b)


Задача 9:

![image](https://github.com/user-attachments/assets/62953766-d56a-40cc-97d9-b68e0160dd0e)

Листинг:

```C++
#include <fstream>
#include <iostream>
using namespace std;
int main() {
    ifstream in("in.txt");
    ofstream out("out.txt");
    string line;
    string line2;
    while (getline(in, line))
    {
        int count = 0;
        line2 = "";
        for (int i = 0; i < size(line); i++) {
            if (count == 4) {
                line2 += '\t';
                count = 0;
            }
            if (line[i] == ' ') {
                count++;
            }
            else {
                if (count == 0)
                    line2 += line[i];
                else
                {
                    for (int j = 0; j < count; j++)
                        line2 += ' ';
                }
                count = 0;
            }
        }
        out << line2 << "\n";
    }
}
```
Запуск:

![image](https://github.com/user-attachments/assets/1c320be7-e6b9-4a62-8559-ee3fff0f1630)

in.txt:

![image](https://github.com/user-attachments/assets/f6e878f1-0f69-458e-a801-6fad0a780c31)

out.txt:

![image](https://github.com/user-attachments/assets/f5c46d8e-c32b-411c-b610-e7c2ff565207)


Задача 10: 

![image](https://github.com/user-attachments/assets/5d50fa05-0d4b-4731-b925-7c52b6208612)
Листинг:
```bash
#!/bin/bash

for file in "$1"/*; do
    if [[ -f "$file" && ! -s "$file" ]]; then
        echo "Пустой файл: $file"
    fi
done
```
Ввод и вывод:
![image](https://github.com/user-attachments/assets/f29c52ac-81dc-46bb-bf10-9209815bdf07)
