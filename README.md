# Telegram Programming Quiz Bot

Телеграм-бот для проведения викторин по программированию (Python, Terminal, Git, HTML/CSS). Использует нативные опросы Telegram в режиме викторины.

## Структура веток
- **`main`**: Чистый код бота. Подходит для локального запуска или большинства хостингов (Heroku, Render, VPS). **Без прокси.**
- **`pythonanywhere`**: Версия, оптимизированная для бесплатного тарифа PythonAnywhere. Включает настройки прокси и расширенную логику повторов при ошибках сети.

## Установка

1. Склонируйте репозиторий:
   ```bash
   git clone https://github.com/Yarmukhamedov/telegram-quiz-bot.git
   cd telegram-quiz-bot
   ```

2. Создайте файл `.env` и добавьте ваш токен:
   ```env
   TELEGRAM_TOKEN=ваш_токен_здесь
   ```

3. Установите зависимости:
   ```bash
   pip install -r requirements.txt
   ```

4. Запустите бота:
   ```bash
   python3 bot.py
   ```

## Деплой на PythonAnywhere

Если вы используете бесплатный тариф PythonAnywhere, переключитесь на специальную ветку:

```bash
git fetch origin
git checkout pythonanywhere
python3 bot.py
```

## Особенности
- **Quiz Mode**: Используются нативные опросы с объяснениями ответов.
- **Randomization**: Вопросы перемешиваются при каждом старте викторины.
- **Persistence**: Бот отслеживает прогресс пользователя в рамках сессии.
