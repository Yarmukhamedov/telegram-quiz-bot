QUIZ_DATA = [
    {
        "question": "Что такое IDE?",
        "options": [
            "Интегрированная среда разработки",
            "Тип операционной системы",
            "Команда в терминале",
            "Язык программирования"
        ],
        "correct_index": 0,
        "explanation": "IDE (Integrated Development Environment) — это программа (например, VS Code), которая объединяет в себе текстовый редактор, отладчик и инструменты автоматизации."
    },
    {
        "question": "В чем разница между Терминалом и Оболочкой (Shell)?",
        "options": [
            "Это одно и то же",
            "Терминал — это окно, Shell — программа внутри, которая понимает команды",
            "Shell — это окно, Терминал — программа внутри",
            "Терминал только для Windows, Shell для Mac"
        ],
        "correct_index": 1,
        "explanation": "Терминал — это графическая оболочка (окно), а Shell (например, zsh или bash) — это интерпретатор, который выполняет ваши команды."
    },
    {
        "question": "Какая команда показывает путь к текущей папке?",
        "options": ["ls", "cd", "pwd", "mkdir"],
        "correct_index": 2,
        "explanation": "pwd (print working directory) выводит полный путь к папке, в которой вы сейчас находитесь."
    },
    {
        "question": "Как увидеть список всех файлов, включая скрытые?",
        "options": ["ls", "ls -a", "ls -l", "show all"],
        "correct_index": 1,
        "explanation": "Флаг -a (all) позволяет увидеть скрытые файлы (те, что начинаются с точки, например .git)."
    },
    {
        "question": "Как создать новую папку с названием 'projects'?",
        "options": ["touch projects", "cd projects", "mkdir projects", "new folder projects"],
        "correct_index": 2,
        "explanation": "mkdir (make directory) используется для создания новых папок."
    },
    {
        "question": "Какая клавиша используется для автодополнения команд в терминале?",
        "options": ["Enter", "Shift", "Tab", "Space"],
        "correct_index": 2,
        "explanation": "Tab — ваш лучший друг в терминале. Он дописывает названия файлов и папок за вас."
    },
    {
        "question": "Как открыть текущую папку в редакторе VS Code через терминал?",
        "options": ["vscode open", "code .", "open vscode", "start ."],
        "correct_index": 1,
        "explanation": "Команда 'code' вызывает VS Code, а точка '.' указывает на текущую директорию."
    },
    {
        "question": "Что делает команда 'touch index.html'?",
        "options": [
            "Открывает файл",
            "Удаляет файл",
            "Создает пустой файл index.html",
            "Запускает сайт"
        ],
        "correct_index": 2,
        "explanation": "touch используется для создания новых (обычно пустых) файлов."
    },
    {
        "question": "Какая команда используется для установки библиотек в Python?",
        "options": ["python get", "install-python", "pip install", "get-lib"],
        "correct_index": 2,
        "explanation": "pip — это менеджер пакетов для Python, используемый для установки сторонних библиотек."
    },
    {
        "question": "Как вернуться на одну папку назад (вверх)?",
        "options": ["cd ..", "cd back", "go back", "cd /"],
        "correct_index": 0,
        "explanation": "Две точки '..' в терминале всегда означают родительскую директорию."
    }
]
