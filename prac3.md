![image](https://github.com/user-attachments/assets/d4f537d9-9c28-40a2-b00f-2ed72bd5fa91)


```jsonnet
local student(name, age, group) = {
  age: age,
  group: group,
  name: name,
};

local groups = [
  "ИКБО-" + i + "-20" for i in std.range(1, 24)
];

local students = [
  student("Иванов И.И.", 19, "ИКБО-4-20"),
  student("Петров П.П.", 18, "ИКБО-5-20"),
  student("Сидоров С.С.", 18, "ИКБО-5-20"),
  student("Юдин А.А.", 20, "ИКБО-52-23"), 
];

{
  groups: groups,
  students: students,
  subject: "Конфигурационное управление",
}
```

![image](https://github.com/user-attachments/assets/2aaf3b9c-a56e-4a86-9de2-13a86be0c9d6)

```dash
let Student = { age : Natural, group : Text, name : Text }

let Group = Text

let groupPrefix = "ИКБО-"

let groupYear = "-20"

let makeGroup =
      λ(n : Natural) →
        groupPrefix ++ Natural/show n ++ groupYear

let groups =
      [ makeGroup 1, makeGroup 2, makeGroup 3, makeGroup 4, makeGroup 5
      , makeGroup 6, makeGroup 7, makeGroup 8, makeGroup 9, makeGroup 10
      , makeGroup 11, makeGroup 12, makeGroup 13, makeGroup 14, makeGroup 15
      , makeGroup 16, makeGroup 17, makeGroup 18, makeGroup 19, makeGroup 20
      , makeGroup 21, makeGroup 22, makeGroup 23, makeGroup 24
      ]

let students =
      [ { age = 19, group = makeGroup 4, name = "Иванов И.И." }
      , { age = 18, group = makeGroup 5, name = "Петров П.П." }
      , { age = 18, group = makeGroup 5, name = "Сидоров С.С." }
      , { age = 20, group = makeGroup 6, name = "Юдин А.А." }
      ]

let subject = "Конфигурационное управление"

in  { groups = groups, students = students, subject = subject }
```

Вывод:
groups:
  - "ИКБО-1-20"
  - "ИКБО-2-20"
  - "ИКБО-3-20"
  - "ИКБО-4-20"
  - "ИКБО-5-20"
  - "ИКБО-6-20"
  - "ИКБО-7-20"
  - "ИКБО-8-20"
  - "ИКБО-9-20"
  - "ИКБО-10-20"
  - "ИКБО-11-20"
  - "ИКБО-12-20"
  - "ИКБО-13-20"
  - "ИКБО-14-20"
  - "ИКБО-15-20"
  - "ИКБО-16-20"
  - "ИКБО-17-20"
  - "ИКБО-18-20"
  - "ИКБО-19-20"
  - "ИКБО-20-20"
  - "ИКБО-21-20"
  - "ИКБО-22-20"
  - "ИКБО-23-20"
  - "ИКБО-24-20"

students:
  - age: 19
    group: "ИКБО-4-20"
    name: "Иванов И.И."
  - age: 18
    group: "ИКБО-5-20"
    name: "Петров П.П."
  - age: 18
    group: "ИКБО-5-20"
    name: "Сидоров С.С."
  - age: 20
    group: "ИКБО-6-20"
    name: "Юдин А.А."

subject: "Конфигурационное управление"


![image](https://github.com/user-attachments/assets/cc6623f1-dff7-4698-a218-56df6f96d5cc)

```python
import random


def parse_bnf(text):
    '''
    Преобразовать текстовую запись БНФ в словарь.
    '''
    grammar = {}
    rules = [line.split('=') for line in text.strip().split('\n')]
    for name, body in rules:
        grammar[name.strip()] = [alt.split() for alt in body.split('|')]
    return grammar


def generate_phrase(grammar, start):
    '''
    Сгенерировать случайную фразу, исключая пустые строки.
    '''
    if start in grammar:
        seq = random.choice(grammar[start])
        return ''.join([generate_phrase(grammar, name) for name in seq])
    return str(start)


BNF = '''
S = 0 S | 1 S | 0 | 1
'''

# Генерация фраз
for i in range(10):
    print(generate_phrase(parse_bnf(BNF), 'S'))

```

Вывод:

![image](https://github.com/user-attachments/assets/6263ad4a-6fc8-4c51-b7a1-c2cff9824afc)


![image](https://github.com/user-attachments/assets/beaca0f1-91b6-48e8-9c72-08728f2ae279)

```python
import random


def parse_bnf(text):
    '''
    Преобразовать текстовую запись БНФ в словарь.
    '''
    grammar = {}
    rules = [line.split('=') for line in text.strip().split('\n')]
    for name, body in rules:
        grammar[name.strip()] = [alt.split() for alt in body.split('|')]
    return grammar


def generate_phrase(grammar, start):
    '''
    Сгенерировать случайную фразу, исключая пустые строки.
    '''
    if start in grammar:
        seq = random.choice(grammar[start])
        return ''.join([generate_phrase(grammar, name) for name in seq])
    return str(start)


BNF = '''
S = ( S ) | { S } | ( S ) S | { S } S | ( ) | { }
'''

# Генерация фраз
for i in range(10):
    print(generate_phrase(parse_bnf(BNF), 'S'))
```

Вывод:

![image](https://github.com/user-attachments/assets/b861ccf1-db14-453a-923c-dc60513e1700)


![image](https://github.com/user-attachments/assets/e6f276df-4a3b-4f0b-9250-d3cae610e23f)

```python
import random

def parse_bnf(text):
    '''
    Преобразовать текстовую запись БНФ в словарь.
    '''
    grammar = {}
    rules = [line.split('=') for line in text.strip().split('\n')]
    for name, body in rules:
        grammar[name.strip()] = [alt.split() for alt in body.split('|')]
    return grammar

def generate_expression(grammar, start):
    '''
    Сгенерировать случайное логическое выражение.
    '''
    if start in grammar:
        seq = random.choice(grammar[start])
        return ''.join([generate_expression(grammar, name) for name in seq])
    return str(start)

BNF = '''
E = E & E | E | E | ~E | ( E ) | y | x
'''

# Генерация логических выражений
for i in range(10):
    print(generate_expression(parse_bnf(BNF), 'E'))

```
Вывод:


![image](https://github.com/user-attachments/assets/763b3192-22f8-4e97-b675-0b649c85fcdf)

