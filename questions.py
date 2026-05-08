QUIZ_DATA = [
    {
        "question": "Что такое IDE?",
        "options": ["Интегрированная среда разработки", "Тип ОС", "Команда терминала", "Язык программирования"],
        "correct_index": 0,
        "explanation": "IDE (например, VS Code) объединяет редактор, отладчик и инструменты в одном месте."
    },
    {
        "question": "В чем разница между Терминалом и Оболочкой (Shell)?",
        "options": ["Это одно и то же", "Терминал — окно, Shell — программа внутри", "Shell — окно, Терминал — программа", "Терминал только для Windows"],
        "correct_index": 1,
        "explanation": "Терминал — это окно, а Shell (zsh, bash) — интерпретатор команд."
    },
    {
        "question": "Какая команда показывает путь к текущей папке?",
        "options": ["ls", "cd", "pwd", "mkdir"],
        "correct_index": 2,
        "explanation": "pwd (print working directory) выводит путь к текущей директории."
    },
    {
        "question": "Как увидеть скрытые файлы?",
        "options": ["ls", "ls -a", "ls -l", "show all"],
        "correct_index": 1,
        "explanation": "Флаг -a (all) показывает файлы, начинающиеся с точки."
    },
    {
        "question": "Как создать папку с названием 'projects'?",
        "options": ["touch projects", "cd projects", "mkdir projects", "new folder"],
        "correct_index": 2,
        "explanation": "mkdir используется для создания директорий."
    },
    {
        "question": "Клавиша для автодополнения команд?",
        "options": ["Enter", "Shift", "Tab", "Space"],
        "correct_index": 2,
        "explanation": "Tab дописывает названия файлов и команд за вас."
    },
    {
        "question": "Как открыть текущую папку в VS Code через терминал?",
        "options": ["vscode open", "code .", "open vscode", "start ."],
        "correct_index": 1,
        "explanation": "Команда 'code .' открывает текущую директорию в VS Code."
    },
    {
        "question": "Что делает 'touch index.html'?",
        "options": ["Открывает файл", "Удаляет файл", "Создает пустой файл", "Запускает сайт"],
        "correct_index": 2,
        "explanation": "touch создает новые пустые файлы."
    },
    {
        "question": "Как устанавливать библиотеки в Python?",
        "options": ["python get", "install-python", "pip install", "get-lib"],
        "correct_index": 2,
        "explanation": "pip — стандартный менеджер пакетов для Python."
    },
    {
        "question": "Как вернуться на одну папку назад?",
        "options": ["cd ..", "cd back", "go back", "cd /"],
        "correct_index": 0,
        "explanation": "Две точки '..' означают переход в родительскую папку."
    },
    {
        "question": "Что делает команда 'ls -l'?",
        "options": ["Список файлов в одну строку", "Подробный список (права, размер, дата)", "Удаляет файлы", "Скрывает файлы"],
        "correct_index": 1,
        "explanation": "Флаг -l (long) выводит подробную информацию о файлах."
    },
    {
        "question": "Как очистить окно терминала?",
        "options": ["delete", "clean", "clear", "cls"],
        "correct_index": 2,
        "explanation": "Команда clear полностью очищает видимую область терминала."
    },
    {
        "question": "Для чего нужен Git?",
        "options": ["Для написания кода", "Для хранения паролей", "Для контроля версий и совместной работы", "Для запуска сайтов"],
        "correct_index": 2,
        "explanation": "Git позволяет сохранять историю изменений и работать над кодом в команде."
    },
    {
        "question": "Что делает команда 'git push'?",
        "options": ["Скачивает изменения", "Отправляет локальные коммиты в облако", "Удаляет проект", "Создает новый файл"],
        "correct_index": 1,
        "explanation": "Push 'выталкивает' ваши сохраненные изменения на сервер (например, GitHub)."
    },
    {
        "question": "Как проверить версию Python в терминале?",
        "options": ["python --version", "check python", "ver py", "python3 start"],
        "correct_index": 0,
        "explanation": "Команда --version показывает установленную версию интерпретатора."
    },
    {
        "question": "Какой тег в HTML создает ссылку?",
        "options": ["<link>", "<a>", "<href>", "<url>"],
        "correct_index": 1,
        "explanation": "Тег <a> (anchor) используется для создания гиперссылок."
    },
    {
        "question": "Какой атрибут тега <img> указывает путь к картинке?",
        "options": ["link", "path", "src", "href"],
        "correct_index": 2,
        "explanation": "src (source) указывает на источник изображения."
    },
    {
        "question": "Как в CSS изменить цвет текста?",
        "options": ["text-color", "color", "font-color", "background"],
        "correct_index": 1,
        "explanation": "Свойство color отвечает за цвет текста в CSS."
    },
    {
        "question": "Что делает команда 'rm -rf'?",
        "options": ["Создает папку", "Рекурсивно удаляет папку без подтверждения", "Переименовывает файл", "Копирует проект"],
        "correct_index": 1,
        "explanation": "Осторожно! rm -rf удаляет всё в указанной папке навсегда."
    },
    {
        "question": "Что такое 'front-end' разработка?",
        "options": ["Создание серверной части", "Работа с базами данных", "Создание интерфейса, который видит пользователь", "Настройка серверов"],
        "correct_index": 2,
        "explanation": "Front-end — это всё, с чем взаимодействует пользователь в браузере."
    },
    {
        "question": "Что такое SSH?",
        "options": ["Протокол для безопасного удаленного доступа", "Тип жесткого диска", "Язык программирования", "Команда для удаления файлов"],
        "correct_index": 0,
        "explanation": "SSH (Secure Shell) позволяет безопасно управлять сервером через интернет."
    },
    {
        "question": "Для чего нужна переменная окружения PATH?",
        "options": ["Для хранения паролей", "Чтобы система знала, где искать исполняемые файлы команд", "Для ускорения интернета", "Для изменения цвета терминала"],
        "correct_index": 1,
        "explanation": "PATH содержит список папок, в которых система ищет программы, когда вы вводите их названия."
    },
    {
        "question": "Какой символ используется как разделитель путей в Windows?",
        "options": ["/", "\\", "|", ":"],
        "correct_index": 1,
        "explanation": "В Windows используется обратный слэш (\\), а в macOS и Linux — прямой (/)."
    },
    {
        "question": "Как в macOS открыть текущую папку в Finder через терминал?",
        "options": ["finder .", "show .", "open .", "start ."],
        "correct_index": 2,
        "explanation": "Команда 'open .' в macOS открывает текущую директорию в графическом интерфейсе."
    },
    {
        "question": "Что такое Homebrew (brew) в macOS?",
        "options": ["Редактор текста", "Менеджер пакетов для установки программ", "Тип шрифта", "Обновление системы"],
        "correct_index": 1,
        "explanation": "Homebrew — это самый популярный менеджер пакетов для macOS."
    },
    {
        "question": "Как расшифровывается SSH?",
        "options": ["Simple System Helper", "Secure Shell", "Super Speed Host", "Server State Handler"],
        "correct_index": 1,
        "explanation": "Secure Shell — защищенная оболочка."
    },
    {
        "question": "Где обычно хранятся SSH ключи пользователя?",
        "options": ["В папке Documents", "В папке ~/.ssh", "На рабочем столе", "В системном реестре"],
        "correct_index": 1,
        "explanation": "Стандартный путь для ключей — скрытая папка .ssh в домашней директории."
    },
    {
        "question": "Какая команда в Linux/macOS показывает запущенные процессы в реальном времени?",
        "options": ["ps", "list", "top", "show"],
        "correct_index": 2,
        "explanation": "Команда top (или htop) показывает загрузку процессора и активные программы."
    },
    {
        "question": "Что делает команда 'sudo'?",
        "options": ["Удаляет файл", "Запускает команду от имени суперпользователя (администратора)", "Выключает компьютер", "Ничего не делает"],
        "correct_index": 1,
        "explanation": "sudo (substitute user do) дает права администратора для выполнения команды."
    },
    {
        "question": "Как в терминале найти слово 'error' в файле log.txt?",
        "options": ["find error log.txt", "grep 'error' log.txt", "search error", "scan log.txt"],
        "correct_index": 1,
        "explanation": "grep — это мощный инструмент для поиска текста в файлах."
    },
    {
        "question": "Какая команда в Windows CMD является аналогом 'ls'?",
        "options": ["list", "show", "dir", "get"],
        "correct_index": 2,
        "explanation": "В классической консоли Windows для вывода списка файлов используется dir."
    },
    {
        "question": "Какое расширение обычно имеют файлы скриптов терминала в Windows?",
        "options": [".sh", ".exe", ".bat", ".py"],
        "correct_index": 2,
        "explanation": ".bat или .cmd — расширения для пакетных файлов (скриптов) Windows."
    },
    {
        "question": "Как остановить зависший процесс в терминале по его ID (PID)?",
        "options": ["stop [PID]", "end [PID]", "kill [PID]", "exit [PID]"],
        "correct_index": 2,
        "explanation": "Команда kill отправляет сигнал завершения процессу."
    },
    {
        "question": "Что такое 'публичный ключ' (id_rsa.pub) в SSH?",
        "options": ["Пароль от компьютера", "Ключ, который вы копируете на сервер для доступа", "Ключ, который нельзя никому показывать", "Файл с настройками интернета"],
        "correct_index": 1,
        "explanation": "Публичный ключ можно безопасно передавать другим, а приватный должен храниться в секрете."
    },
    {
        "question": "Какая команда выводит справку (руководство) по любой команде в Linux/macOS?",
        "options": ["help", "info", "man", "guide"],
        "correct_index": 2,
        "explanation": "Команда man (manual) открывает встроенную документацию."
    }
]
