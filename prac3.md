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
let Prelude =
      https://prelude.dhall-lang.org/v19.0.0/package.dhall sha256:eb693342eb769f782174157eba9b5924cf8ac6793897fc36a31ccbd6f56dafe2
let Student = { age : Natural, group : Text, name : Text }

let mkStudent : Text -> Natural -> Text -> Student =
λ(name : Text) → λ(age : Natural) → λ(group : Text) →
{ age = age, group = group, name = name }

let groups : List Text =
let groupPrefix = "ИКБО-"
let groupSuffix = "-20"
let groupNumbers = List.range 1 25 
in List.map (λ(i : Natural) → groupPrefix ++ Text.show i ++ groupSuffix) groupNumbers

let students : List Student =
[ mkStudent "Иванов И.И." 19 "ИКБО-4-20"
, mkStudent "Петров П.П." 18 "ИКБО-5-20"
, mkStudent "Сидоров С.С." 18 "ИКБО-5-20"
, mkStudent "Юдин А.А." 20 "ИКБО-6-20" 
]

in { groups = generateGroups, students = students, subject = "Конфигурационное управление" }
```

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

