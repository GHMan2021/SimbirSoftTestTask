## Установка и запуск проекта

Проект выполнения тестового задания от SimbirSoft на кейс "Заполнение формы регистрации на сайте https://demoqa.com/automation-practice-form" 

1. Склонировать репозиторий
```
git clone https://github.com/GHMan2021/SimbirSoftTestTask.git
```
2. Перейти в директорию проекта
3. Создать вируальное окружение
```
python -m venv venv
```
4. Активировать окружение
```
venv\Scripts\activate
```
5. Установка зависимостей
```
pip install -r requirements.txt
```
6. Запуск тестов
```
pytest --alluredir=tests/allure-results
```
7. Запуск отчета allure по тестам
```
allure serve tests/allure-results
```