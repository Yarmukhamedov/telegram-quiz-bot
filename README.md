# 🤖 Telegram Quiz Bot

Этот бот создан для тестирования твоих знаний в области программирования (Терминал, IDE, Python).

## 🚀 Быстрый старт (Локально)

1.  **Установи Python**, если он еще не установлен.
2.  **Создай виртуальное окружение** (рекомендуется):
    ```bash
    python3 -m venv venv
    source venv/bin/activate  # Для Mac/Linux
    ```
3.  **Установи зависимости**:
    ```bash
    pip install -r requirements.txt
    ```
4.  **Получи токен бота**:
    - Напиши [@BotFather](https://t.me/BotFather) в Telegram.
    - Создай нового бота (`/newbot`) и скопируй API Token.
5.  **Настрой переменные окружения**:
    - Создай файл `.env` (или переименуй `.env.example`).
    - Вставь свой токен: `TELEGRAM_TOKEN=твой_токен`.
6.  **Запусти бота**:
    ```bash
    python bot.py
    ```

---

## 🌍 Инструкция по выгрузке на хостинг (Render.com)

Render — один из самых простых способов запустить бота бесплатно или за минимальную плату.

### Шаг 1: Подготовка
1. Создай аккаунт на [GitHub](https://github.com) (если нет).
2. Создай новый репозиторий (например, `my-quiz-bot`).
3. Загрузи файлы проекта (`bot.py`, `questions.py`, `requirements.txt`) в этот репозиторий. **НЕ ЗАГРУЖАЙ `.env`!**

### Шаг 2: Настройка на Render
1. Зайди на [Render.com](https://render.com) и создай аккаунт.
2. Нажми **New +** -> **Background Worker**.
3. Подключи свой GitHub и выбери репозиторий с ботом.
4. Настрой параметры:
   - **Name**: `quiz-bot`
   - **Runtime**: `Python 3`
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `python bot.py`
5. Нажми на кнопку **Advanced** -> **Add Environment Variable**:
   - Key: `TELEGRAM_TOKEN`
   - Value: `твой_токен_из_BotFather`
6. Нажми **Create Background Worker**.

Бот запустится автоматически и будет работать 24/7!

---

## 🐍 Вариант 2: PythonAnywhere (Если нужен только Python)

1. Создай аккаунт на [PythonAnywhere](https://www.pythonanywhere.com/).
2. Зайди в раздел **Consoles** -> **Bash**.
3. Клонируй свой репозиторий: `git clone https://github.com/твой_логин/репозиторий`.
4. Установи зависимости: `pip3 install --user -r requirements.txt`.
5. Создай файл `.env` прямо там через файловый менеджер.
6. Запусти бота: `python3 bot.py`.
   - *Примечание: В бесплатном тарифе PythonAnywhere нужно раз в сутки нажимать кнопку продления.*

---

## 📚 Как добавлять вопросы?

Просто редактируй файл `questions.py`. Каждый вопрос — это словарь в списке `QUIZ_DATA`. Не забудь перезапустить бота после изменений!
