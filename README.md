# SkyStore Pro: E-commerce & Content Management System

![Python](https://img.shields.io/badge/python-3.11+-blue.svg)
![Django](https://img.shields.io/badge/django-5.2-green.svg)
![Redis](https://img.shields.io/badge/redis-caching-red.svg)

**SkyStore Pro** — веб-приложение на Django: каталог товаров и блог с публикацией материалов, регистрацией пользователей и кэшированием через Redis.

## Основной функционал

* **Каталог товаров:** категории, товары с изображениями и ценой, признак публикации, привязка владельца, кастомное право на снятие с публикации.
* **Блог:** записи с превью, динамические URL, счётчик просмотров, признак публикации.
* **Пользователи:** кастомная модель пользователя, регистрация, вход и выход (через встроенные `LoginView` / `LogoutView`).
* **Кэширование:** Redis (`django.core.cache.backends.redis.RedisCache`) — страницы каталога и выборка списка товаров.
* **Формы:** создание и редактирование товаров и записей блога через Django Forms из интерфейса сайта.

## Технологический стек

* **Framework:** Django 5.2 (MTV).
* **База данных:** PostgreSQL (`psycopg2-binary` в зависимостях Poetry).
* **Кэш:** Redis (пакет `redis` + `CACHE_LOCATION` в `.env`).
* **Frontend:** Django Templates, Bootstrap 5.
* **Окружение:** Poetry, переменные из `.env` (`python-dotenv`).

## Структура приложений

* `catalog/` — товары, категории, главная, контакты.
* `blog/` — статьи блога.
* `users/` — регистрация и аутентификация.
* `Django/` — настройки проекта и корневые URL.

## Требования перед запуском

1. Установлены **Python 3.11+** и [Poetry](https://python-poetry.org/docs/#installation).
2. Запущены **PostgreSQL** и **Redis** (адрес кэша задаётся в `CACHE_LOCATION`).
3. Создана пустая база в PostgreSQL под значения из `.env`.

## Установка и запуск

1. Клонируйте репозиторий:

   ```bash
   git clone https://github.com/AJLbN0H/skystore-pro-engine.git
   cd skystore-pro-engine
   ```

2. Установите зависимости:

   ```bash
   poetry install
   ```

3. Скопируйте пример переменных окружения и заполните значения:

   ```bash
   cp .env.sample .env
   ```

   В репозитории используется файл **`.env.sample`** (пример для `SECRET_KEY`, PostgreSQL, Redis и почты Yandex SMTP). Поля `EMAIL_*` нужны, если вы будете отправлять письма через настройки из `Django/settings.py`.

4. Примените миграции и запустите сервер разработки:

   ```bash
   poetry run python manage.py migrate
   poetry run python manage.py runserver
   ```

   Либо активируйте виртуальное окружение Poetry и вызывайте `python manage.py ...` без префикса `poetry run`.

5. **Опционально:** суперпользователь и демо-данные каталога:

   ```bash
   poetry run python manage.py csu
   poetry run python manage.py add_test_data
   ```

   Для загрузки фикстур (если используете): `loaddata` с файлами `catalog_fixture.json`, `product_moderators_fixture.json` в корне проекта.

## Замечания по конфигурации

* В `ALLOWED_HOSTS` по умолчанию пустой список — для продакшена его нужно заполнить.
* Без работающего Redis запросы к кэшу могут завершаться ошибкой подключения.
* Сброс пароля по e-mail в URL-паттернах не подключён; в `settings.py` уже задан SMTP Yandex для возможной доработки.

## Roadmap

* Корзина и оплата.
* Асинхронная загрузка изображений.
* Unit-тесты для ключевых представлений (сейчас в проекте тесты не зарегистрированы).
