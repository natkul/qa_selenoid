**QA_SELENOID.py README**

**Требования**
1. Настройте логирование внутри PageObject'ов. (черед модуль logging).
2. Добавьте аннотации для шагов и тестов для трансляции в отчёт Allure.
3. Настройте Selenoid, добавьте несколько браузеров и запустите на них тесты.
4. Предусмотрите возможность запуска тестов как на удаленных сервисах так и локально.
5. Предусмотрите снятие скриншота и добавление его в отчёт при падении тестов.

**Запуск и результат**

Установка:
$ git clone git@github.com:natkul/qa_selenoid.git

OpenCart (linux):
Поднять OpenCart: sudo OPENCART_PORT=8081 PHPADMIN_PORT=8888 LOCAL_IP=$(hostname -I | grep -o "^[0-9.]*") docker-compose up -d
Запустить Selenoid: sudo ./cm selenoid start

Запуск:
$ python3 -m pip install -r requirements.txt
$ pytest --browser_version <browser_version> --browser <browser>
example : pytest  --browser_version 101.0 --browser chrome)

Реализованы автотесты с использованием паттерна PageObject. Добавлены аннотации для шагов и тестов для трансляции в отчёт Allure.
В browsers.json добавлен MicrosoftEdge, "versions": {104.0, 88.0}. Есть возможность запуска тестов как удалённо, так и локально.
При падении теста предусмотрено снятие скриншота и добавление в Allure
