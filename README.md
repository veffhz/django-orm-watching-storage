# Пульт охраны банка
Пульт охраны — это сайт с визитами и карточками пропуска сотрудников банка.

Это внутренний репозиторий для сотрудников банка «Сияние». Если вы попали в этот репозиторий случайно, то вы не сможете его запустить, т.к. у вас нет доступа к БД, но можете свободно использовать код вёрстки или посмотреть как реализованы запросы к БД.


## Как установить
Для переменных окружения создайте файл `.env` и положите его в корень сайта. Затем запросите доступ к БД
у менеджера вашего банка. Для доступа вам понадобятся:

* `DB_HOST` = адрес сервера
* `DB_PORT` = порт сервера
* `DB_NAME` = имя БД
* `DB_USER` = имя пользователя БД
* `DB_PASSWORD` = пароль для БД
* `DEBUG` = включение режима отладки

## Как запустить

* Скачайте код
* Для работы сайта необходим установленный интерпретатор Python3.6. Затем загрузите зависимости с помощью "pip"
(либо "pip3", в случае конфликтов с Python2):
```
pip install -r requirements.txt
```

* Запустите веб-сервер
```bash
$ python manage.py runserver
```
* Откройте сайт в браузере по адресу [127.0.0.0:8000](http://127.0.0.0:8000)

## Цель проекта
Код написан в образовательных целях на онлайн-курсе для веб-разработчиков [dvmn.org](https://dvmn.org/).
