# Приложение на Django 4.0

## Описание проекта

Приложение представляет собой сайт, посвященный национальным паркам Ваттового моря.

Он содержит два крупных раздела:
- регионы Ваттового моря;
- обитатели Ваттового моря.

Раздел "Обитатели" включает в себя 3 подраздела:
- животные;
- птицы;
- рыбы.


## Запуск приложения на локальном компьютере

1. Для работы приложения требуется Python не ниже версии 3.8.
Это требование отражено в документации Django [Поддерживаемые версии Python для Django](https://docs.djangoproject.com/en/4.0/faq/install/#what-python-version-can-i-use-with-django)

2. Клонируйте репозиторий на свой компьютер:
```bash
gh repo clone jkandrashina/petproject-ws
```

3. Откройте командную строку и перейдите в папку petproject-ws:
```bash
cd petproject-ws
```

4. Создайте в ней виртуальное окружение:

Linux
```bash
python3 -m venv venv
```
Windows
```bash
python -m venv venv
```

5. Активируйте виртуальное окружение, выполнив команду:

Linux
```bash
source venv/bin/activate
```
Windows
```bash
venv\scripts\activate
```

6. Установите необходимые библиотеки, прочитав их список из файла:

Linux
```bash
(venv) ~$ pip install -r requirements.txt
```
Windows
```bash
(venv)..> python -m pip install -r requirements.txt
```

7. Запустите виртуальный сервер:

Linux / Windows
```bash
python manage.py runserver
```

8. Откройте приложение в браузере, набрав в адресной строке:
```bash
http://127.0.0.1:8000
```