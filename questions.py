QUIZ_DATA = [
    # --- PREVIOUS QUESTIONS (1-81) ---
    {
        "question": "Что такое IDE?",
        "options": ["Интегрированная среда разработки", "Тип ОС", "Команда терминала", "Язык программирования"],
        "correct_index": 0,
        "explanation": "IDE (например, VS Code) объединяет редактор, отладчик и инструменты в одном месте.",
        "category": "general",
        "difficulty": "easy"
    },
    {
        "question": "В чем разница между Терминалом и Оболочкой (Shell)?",
        "options": ["Это одно и то же", "Терминал — окно, Shell — программа внутри", "Shell — окно, Терминал — программа", "Терминал только для Windows"],
        "correct_index": 1,
        "explanation": "Терминал — это окно, а Shell (zsh, bash) — интерпретатор команд.",
        "category": "terminal",
        "difficulty": "easy"
    },
    {
        "question": "Какая команда показывает путь к текущей папке?",
        "options": ["ls", "cd", "pwd", "mkdir"],
        "correct_index": 2,
        "explanation": "pwd (print working directory) выводит путь к текущей директории.",
        "category": "terminal",
        "difficulty": "easy"
    },
    {
        "question": "Как увидеть скрытые файлы?",
        "options": ["ls", "ls -a", "ls -l", "show all"],
        "correct_index": 1,
        "explanation": "Флаг -a (all) показывает файлы, начинающиеся с точки.",
        "category": "terminal",
        "difficulty": "easy"
    },
    {
        "question": "Как создать папку с названием 'projects'?",
        "options": ["touch projects", "cd projects", "mkdir projects", "new folder"],
        "correct_index": 2,
        "explanation": "mkdir используется для создания директорий.",
        "category": "terminal",
        "difficulty": "easy"
    },
    {
        "question": "Клавиша для автодополнения команд?",
        "options": ["Enter", "Shift", "Tab", "Space"],
        "correct_index": 2,
        "explanation": "Tab дописывает названия файлов и команд за вас.",
        "category": "terminal",
        "difficulty": "easy"
    },
    {
        "question": "Как открыть текущую папку в VS Code через терминал?",
        "options": ["vscode open", "code .", "open vscode", "start ."],
        "correct_index": 1,
        "explanation": "Команда 'code .' открывает текущую директорию в VS Code.",
        "category": "terminal",
        "difficulty": "easy"
    },
    {
        "question": "Что делает 'touch index.html'?",
        "options": ["Открывает файл", "Удаляет файл", "Создает пустой файл", "Запускает сайт"],
        "correct_index": 2,
        "explanation": "touch создает новые пустые файлы.",
        "category": "terminal",
        "difficulty": "easy"
    },
    {
        "question": "Как устанавливать библиотеки в Python?",
        "options": ["python get", "install-python", "pip install", "get-lib"],
        "correct_index": 2,
        "explanation": "pip — стандартный менеджер пакетов для Python.",
        "category": "python",
        "difficulty": "easy"
    },
    {
        "question": "Как вернуться на одну папку назад?",
        "options": ["cd ..", "cd back", "go back", "cd /"],
        "correct_index": 0,
        "explanation": "Две точки '..' означают переход в родительскую папку.",
        "category": "terminal",
        "difficulty": "easy"
    },
    {
        "question": "Что делает команда 'ls -l'?",
        "options": ["Список файлов в одну строку", "Подробный список (права, размер, дата)", "Удаляет файлы", "Скрывает файлы"],
        "correct_index": 1,
        "explanation": "Флаг -l (long) выводит подробную информацию о файлах.",
        "category": "terminal",
        "difficulty": "easy"
    },
    {
        "question": "Как очистить окно терминала?",
        "options": ["delete", "clean", "clear", "cls"],
        "correct_index": 2,
        "explanation": "Команда clear полностью очищает видимую область терминала.",
        "category": "terminal",
        "difficulty": "easy"
    },
    {
        "question": "Для чего нужен Git?",
        "options": ["Для написания кода", "Для хранения паролей", "Для контроля версий и совместной работы", "Для запуска сайтов"],
        "correct_index": 2,
        "explanation": "Git позволяет сохранять историю изменений и работать над кодом в команде.",
        "category": "git",
        "difficulty": "easy"
    },
    {
        "question": "Что делает команда 'git push'?",
        "options": ["Скачивает изменения", "Отправляет локальные коммиты в облако", "Удаляет проект", "Создает новый файл"],
        "correct_index": 1,
        "explanation": "Push 'выталкивает' ваши сохраненные изменения на сервер (например, GitHub).",
        "category": "git",
        "difficulty": "medium"
    },
    {
        "question": "Как проверить версию Python в терминале?",
        "options": ["python --version", "check python", "ver py", "python3 start"],
        "correct_index": 0,
        "explanation": "Команда --version показывает установленную версию интерпретатора.",
        "category": "python",
        "difficulty": "easy"
    },
    {
        "question": "Какой тег в HTML создает ссылку?",
        "options": ["<link>", "<a>", "<href>", "<url>"],
        "correct_index": 1,
        "explanation": "Тег <a> (anchor) используется для создания гиперссылок.",
        "category": "html_css",
        "difficulty": "easy"
    },
    {
        "question": "Какой атрибут тега <img> указывает путь к картинке?",
        "options": ["link", "path", "src", "href"],
        "correct_index": 2,
        "explanation": "src (source) указывает на источник изображения.",
        "category": "html_css",
        "difficulty": "easy"
    },
    {
        "question": "Как в CSS изменить цвет текста?",
        "options": ["text-color", "color", "font-color", "background"],
        "correct_index": 1,
        "explanation": "Свойство color отвечает за цвет текста в CSS.",
        "category": "html_css",
        "difficulty": "easy"
    },
    {
        "question": "Что делает команда 'rm -rf'?",
        "options": ["Создает папку", "Рекурсивно удаляет папку без подтверждения", "Переименовывает файл", "Копирует проект"],
        "correct_index": 1,
        "explanation": "Осторожно! rm -rf удаляет всё в указанной папке навсегда.",
        "category": "terminal",
        "difficulty": "medium"
    },
    {
        "question": "Что такое 'front-end' разработка?",
        "options": ["Создание серверной части", "Работа с базами данных", "Создание интерфейса, который видит пользователь", "Настройка серверов"],
        "correct_index": 2,
        "explanation": "Front-end — это всё, с чем взаимодействует пользователь в браузере.",
        "category": "general",
        "difficulty": "easy"
    },
    {
        "question": "Что такое SSH?",
        "options": ["Протокол для безопасного удаленного доступа", "Тип жесткого диска", "Язык программирования", "Команда для удаления файлов"],
        "correct_index": 0,
        "explanation": "SSH (Secure Shell) позволяет безопасно управлять сервером через интернет.",
        "category": "ssh",
        "difficulty": "medium"
    },
    {
        "question": "Для чего нужна переменная окружения PATH?",
        "options": ["Для хранения паролей", "Чтобы система знала, где искать исполняемые файлы команд", "Для ускорения интернета", "Для изменения цвета терминала"],
        "correct_index": 1,
        "explanation": "PATH содержит список папок, в которых система ищет программы, когда вы вводите их названия.",
        "category": "os",
        "difficulty": "medium"
    },
    {
        "question": "Какой символ используется как разделитель путей в Windows?",
        "options": ["/", "\\", "|", ":"],
        "correct_index": 1,
        "explanation": "В Windows используется обратный слэш (\\), а в macOS и Linux — прямой (/).",
        "category": "os",
        "difficulty": "easy"
    },
    {
        "question": "Как в macOS открыть текущую папку в Finder через терминал?",
        "options": ["finder .", "show .", "open .", "start ."],
        "correct_index": 2,
        "explanation": "Команда 'open .' в macOS открывает текущую директорию в графическом интерфейсе.",
        "category": "os",
        "difficulty": "medium"
    },
    {
        "question": "Что такое Homebrew (brew) в macOS?",
        "options": ["Редактор текста", "Менеджер пакетов для установки программ", "Тип шрифта", "Обновление системы"],
        "correct_index": 1,
        "explanation": "Homebrew — это самый популярный менеджер пакетов для macOS.",
        "category": "os",
        "difficulty": "medium"
    },
    {
        "question": "Как расшифровывается SSH?",
        "options": ["Simple System Helper", "Secure Shell", "Super Speed Host", "Server State Handler"],
        "correct_index": 1,
        "explanation": "Secure Shell — защищенная оболочка.",
        "category": "ssh",
        "difficulty": "easy"
    },
    {
        "question": "Где обычно хранятся SSH ключи пользователя?",
        "options": ["В папке Documents", "В папке ~/.ssh", "На рабочем столе", "В системном реестре"],
        "correct_index": 1,
        "explanation": "Стандартный путь для ключей — скрытая папка .ssh в домашней директории.",
        "category": "ssh",
        "difficulty": "medium"
    },
    {
        "question": "Какая команда в Linux/macOS показывает запущенные процессы в реальном времени?",
        "options": ["ps", "list", "top", "show"],
        "correct_index": 2,
        "explanation": "Команда top (или htop) показывает загрузку процессора и активные программы.",
        "category": "terminal",
        "difficulty": "medium"
    },
    {
        "question": "Что делает команда 'sudo'?",
        "options": ["Удаляет файл", "Запускает команду от имени суперпользователя (администратора)", "Выключает компьютер", "Ничего не делает"],
        "correct_index": 1,
        "explanation": "sudo (substitute user do) дает права администратора для выполнения команды.",
        "category": "os",
        "difficulty": "medium"
    },
    {
        "question": "Как в терминале найти слово 'error' в файле log.txt?",
        "options": ["find error log.txt", "grep 'error' log.txt", "search error", "scan log.txt"],
        "correct_index": 1,
        "explanation": "grep — это мощный инструмент для поиска текста в файлах.",
        "category": "terminal",
        "difficulty": "medium"
    },
    {
        "question": "Какая команда в Windows CMD является аналогом 'ls'?",
        "options": ["list", "show", "dir", "get"],
        "correct_index": 2,
        "explanation": "В классической консоли Windows для вывода списка файлов используется dir.",
        "category": "os",
        "difficulty": "easy"
    },
    {
        "question": "Какое расширение обычно имеют файлы скриптов терминала в Windows?",
        "options": [".sh", ".exe", ".bat", ".py"],
        "correct_index": 2,
        "explanation": ".bat или .cmd — расширения для пакетных файлов (скриптов) Windows.",
        "category": "os",
        "difficulty": "medium"
    },
    {
        "question": "Как остановить зависший процесс в терминале по его ID (PID)?",
        "options": ["stop [PID]", "end [PID]", "kill [PID]", "exit [PID]"],
        "correct_index": 2,
        "explanation": "Команда kill отправляет сигнал завершения процессу.",
        "category": "terminal",
        "difficulty": "medium"
    },
    {
        "question": "Что такое 'публичный ключ' (id_rsa.pub) в SSH?",
        "options": ["Пароль от компьютера", "Ключ, который вы копируете на сервер для доступа", "Ключ, который нельзя никому показывать", "Файл с настройками интернета"],
        "correct_index": 1,
        "explanation": "Публичный ключ можно безопасно передавать другим, а приватный должен храниться в секрете.",
        "category": "ssh",
        "difficulty": "hard"
    },
    {
        "question": "Какая команда выводит справку (руководство) по любой команде в Linux/macOS?",
        "options": ["help", "info", "man", "guide"],
        "correct_index": 2,
        "explanation": "Команда man (manual) открывает встроенную документацию.",
        "category": "terminal",
        "difficulty": "easy"
    },
    {
        "question": "Как создать новую ветку в Git?",
        "options": ["git branch-new", "git checkout -b", "git add-branch", "git commit -b"],
        "correct_index": 1,
        "explanation": "Команда git checkout -b [имя] создает новую ветку и сразу переключается на неё.",
        "category": "git",
        "difficulty": "medium"
    },
    {
        "question": "Что делает команда 'git stash'?",
        "options": ["Удаляет все файлы", "Временно прячет незавершенные изменения", "Отправляет код на сервер", "Создает коммит"],
        "correct_index": 1,
        "explanation": "Stash позволяет сохранить изменения в 'кармане', чтобы вернуться к ним позже.",
        "category": "git",
        "difficulty": "hard"
    },
    {
        "question": "Как объединить ветку 'feature' с текущей?",
        "options": ["git combine feature", "git join feature", "git merge feature", "git pull feature"],
        "correct_index": 2,
        "explanation": "git merge используется для слияния веток.",
        "category": "git",
        "difficulty": "medium"
    },
    {
        "question": "Какой тип данных в Python является неизменяемым?",
        "options": ["List", "Dictionary", "Tuple", "Set"],
        "correct_index": 2,
        "explanation": "Tuple (кортеж) нельзя изменить после создания, в отличие от списков.",
        "category": "python",
        "difficulty": "medium"
    },
    {
        "question": "Как в Python добавить элемент в конец списка?",
        "options": ["list.add()", "list.push()", "list.append()", "list.insert()"],
        "correct_index": 2,
        "explanation": "Метод append() добавляет один элемент в конец существующего списка.",
        "category": "python",
        "difficulty": "easy"
    },
    {
        "question": "Что выведет print(type([]))?",
        "options": ["<class 'tuple'>", "<class 'dict'>", "<class 'list'>", "<class 'set'>"],
        "correct_index": 2,
        "explanation": "Квадратные скобки [] создают объект класса list.",
        "category": "python",
        "difficulty": "easy"
    },
    {
        "question": "Для чего используется 'pip freeze > requirements.txt'?",
        "options": ["Для запуска программы", "Для сохранения списка всех установленных библиотек", "Для удаления Python", "Для очистки кеша"],
        "correct_index": 1,
        "explanation": "Это стандартный способ сохранить зависимости проекта для других разработчиков.",
        "category": "python",
        "difficulty": "medium"
    },
    {
        "question": "Что такое 'лямбда-функция' в Python?",
        "options": ["Сложная математическая функция", "Анонимная функция в одну строку", "Функция для работы с файлами", "Системная ошибка"],
        "correct_index": 1,
        "explanation": "Lambda — это короткий способ написать небольшую функцию без имени.",
        "category": "python",
        "difficulty": "hard"
    },
    {
        "question": "Как изменить права файла на 'чтение и запись для всех'?",
        "options": ["chmod 777", "chmod 444", "chmod 000", "chmod 111"],
        "correct_index": 0,
        "explanation": "777 дает полные права (rwx) владельцу, группе и остальным.",
        "category": "terminal",
        "difficulty": "hard"
    },
    {
        "question": "Что делает символ '|' (pipe) в терминале?",
        "options": ["Останавливает команду", "Передает вывод одной команды на вход другой", "Разделяет файлы", "Удаляет пробелы"],
        "correct_index": 1,
        "explanation": "Конвейер позволяет связывать команды в цепочки (например, ls | grep 'txt').",
        "category": "terminal",
        "difficulty": "medium"
    },
    {
        "question": "Что делает команда 'echo $HOME'?",
        "options": ["Выводит текст '$HOME'", "Выводит путь к домашней директории пользователя", "Очищает домашнюю папку", "Создает папку HOME"],
        "correct_index": 1,
        "explanation": "$ указывает на переменную окружения. $HOME хранит путь к профилю пользователя.",
        "category": "terminal",
        "difficulty": "medium"
    },
    {
        "question": "Как в CSS сделать Flex-контейнер?",
        "options": ["display: block", "display: flex", "type: flex", "position: flex"],
        "correct_index": 1,
        "explanation": "Свойство display со значением flex превращает элемент в гибкий контейнер.",
        "category": "html_css",
        "difficulty": "easy"
    },
    {
        "question": "Какое свойство Flexbox выравнивает элементы по главной оси?",
        "options": ["align-items", "justify-content", "align-content", "flex-direction"],
        "correct_index": 1,
        "explanation": "justify-content отвечает за горизонтальное выравнивание (по умолчанию).",
        "category": "html_css",
        "difficulty": "medium"
    },
    {
        "question": "Что такое семантический тег в HTML?",
        "options": ["Тег, который меняет цвет", "Тег, описывающий смысл контента (<header>, <article>)", "Скрытый тег для SEO", "Тег для вставки кода"],
        "correct_index": 1,
        "explanation": "Семантика помогает поисковикам и скринридерам понимать структуру сайта.",
        "category": "html_css",
        "difficulty": "medium"
    },
    {
        "question": "Как сделать текст жирным в CSS?",
        "options": ["font-style: bold", "text-weight: bold", "font-weight: bold", "font-bold: true"],
        "correct_index": 2,
        "explanation": "font-weight регулирует толщину шрифта.",
        "category": "html_css",
        "difficulty": "easy"
    },
    {
        "question": "Какая команда создаст SSH-ключ?",
        "options": ["ssh-add", "ssh-keygen", "ssh-create", "ssh-new"],
        "correct_index": 1,
        "explanation": "ssh-keygen генерирует пару из публичного и приватного ключей.",
        "category": "ssh",
        "difficulty": "medium"
    },
    {
        "question": "Что такое файл '~/.ssh/config'?",
        "options": ["Вирус", "Файл для настройки быстрых подключений к серверам", "Справочник команд SSH", "Список всех паролей"],
        "correct_index": 1,
        "explanation": "В этом файле можно прописать алиасы для серверов, чтобы подключаться просто через 'ssh myserver'.",
        "category": "ssh",
        "difficulty": "hard"
    },
    {
        "question": "Как подключиться к серверу по SSH, если он работает на порту 2222?",
        "options": ["ssh -p 2222 user@host", "ssh user@host:2222", "ssh -port 2222 user@host", "ssh --p 2222 user@host"],
        "correct_index": 0,
        "explanation": "Флаг -p (маленькая p) используется для указания порта в SSH.",
        "category": "ssh",
        "difficulty": "hard"
    },
    {
        "question": "Что такое 'swap' в операционных системах?",
        "options": ["Быстрый процессор", "Файл или раздел подкачки на диске при нехватке RAM", "Замена видеокарты", "Команда для перезагрузки"],
        "correct_index": 1,
        "explanation": "Swap используется системой, когда оперативная память (RAM) полностью заполнена.",
        "category": "os",
        "difficulty": "hard"
    },
    {
        "question": "Какая комбинация клавиш обычно закрывает процесс в терминале?",
        "options": ["Ctrl + C", "Ctrl + Z", "Ctrl + X", "Ctrl + V"],
        "correct_index": 0,
        "explanation": "Ctrl + C посылает сигнал прерывания (SIGINT) активному процессу.",
        "category": "terminal",
        "difficulty": "easy"
    },
    {
        "question": "Что означает 'localhost'?",
        "options": ["Чужой сервер", "Ваш собственный компьютер (IP 127.0.0.1)", "Локальная сеть провайдера", "Сайт в интернете"],
        "correct_index": 1,
        "explanation": "Localhost — это стандартное имя для обращения к самому себе в сети.",
        "category": "os",
        "difficulty": "easy"
    },
    {
        "question": "Как в Python проверить, есть ли ключ в словаре?",
        "options": ["if key in dict:", "if dict.has(key):", "if key exists in dict:", "if key is in dict:"],
        "correct_index": 0,
        "explanation": "Оператор 'in' — самый быстрый и правильный способ проверки ключа.",
        "category": "python",
        "difficulty": "medium"
    },
    {
        "question": "Что делает 'git fetch'?",
        "options": ["Скачивает изменения и объединяет их", "Просто скачивает информацию о новых коммитах без слияния", "Удаляет ветку", "Создает копию проекта"],
        "correct_index": 1,
        "explanation": "Fetch обновляет данные о сервере, но не меняет ваш локальный код (в отличие от pull).",
        "category": "git",
        "difficulty": "hard"
    },
    {
        "question": "Как в CSS задать расстояние между границей элемента и его содержимым?",
        "options": ["margin", "padding", "border-spacing", "gap"],
        "correct_index": 1,
        "explanation": "Padding — это внутренний отступ, margin — внешний.",
        "category": "html_css",
        "difficulty": "easy"
    },
    {
        "question": "Что делает команда 'df -h' в терминале?",
        "options": ["Показывает свободное место на дисках в удобном виде", "Удаляет историю команд", "Форматирует диск", "Выводит список папок"],
        "correct_index": 0,
        "explanation": "df (disk free) с флагом -h (human-readable) показывает объем дисков в Гб/Мб.",
        "category": "terminal",
        "difficulty": "medium"
    },
    {
        "question": "Что такое 'f-строки' в Python?",
        "options": ["Файловые строки", "Форматированные строки с префиксом f", "Строки с ошибками", "Функциональные строки"],
        "correct_index": 1,
        "explanation": "f-строки (например, f'Hello {name}') позволяют удобно вставлять переменные в текст.",
        "category": "python",
        "difficulty": "easy"
    },
    {
        "question": "Как в Git отменить последний коммит, сохранив изменения в файлах?",
        "options": ["git reset --hard HEAD~1", "git reset --soft HEAD~1", "git delete commit", "git undo"],
        "correct_index": 1,
        "explanation": "--soft HEAD~1 удаляет запись о коммите, но оставляет ваш код нетронутым.",
        "category": "git",
        "difficulty": "hard"
    },
    {
        "question": "Что делает команда 'cat file.txt'?",
        "options": ["Удаляет файл", "Выводит содержимое файла в терминал", "Создает копию файла", "Редактирует файл"],
        "correct_index": 1,
        "explanation": "cat (concatenate) используется для быстрого просмотра содержимого файлов.",
        "category": "terminal",
        "difficulty": "easy"
    },
    {
        "question": "Как в HTML сделать нумерованный список?",
        "options": ["<ul>", "<list>", "<ol>", "<nl>"],
        "correct_index": 2,
        "explanation": "<ol> (ordered list) создает список с цифрами, <ul> — с точками.",
        "category": "html_css",
        "difficulty": "easy"
    },
    {
        "question": "Что такое 'z-index' в CSS?",
        "options": ["Размер шрифта", "Порядок наслоения элементов (кто выше, кто ниже)", "Скорость анимации", "Тип прозрачности"],
        "correct_index": 1,
        "explanation": "Z-index определяет, какой элемент будет перекрывать другой по оси Z.",
        "category": "html_css",
        "difficulty": "medium"
    },
    {
        "question": "Какая команда в терминале позволяет искать файлы по имени?",
        "options": ["search", "find", "lookup", "locate"],
        "correct_index": 1,
        "explanation": "Команда find — стандартный инструмент поиска файлов и папок.",
        "category": "terminal",
        "difficulty": "medium"
    },
    {
        "question": "Что делает команда 'history'?",
        "options": ["Показывает дату", "Выводит список последних введенных команд", "Очищает компьютер", "Удаляет куки"],
        "correct_index": 1,
        "explanation": "History позволяет быстро найти и повторить команду, которую вы вводили ранее.",
        "category": "terminal",
        "difficulty": "easy"
    },
    {
        "question": "Что такое 'virtualenv' (или venv) в Python?",
        "options": ["Виртуальный компьютер", "Изолированная среда для библиотек проекта", "Облачное хранилище", "Антивирус для кода"],
        "correct_index": 1,
        "explanation": "Venv позволяет разным проектам иметь разные версии библиотек и не конфликтовать.",
        "category": "python",
        "difficulty": "medium"
    },
    {
        "question": "Как в Git посмотреть историю всех коммитов?",
        "options": ["git history", "git show", "git log", "git list"],
        "correct_index": 2,
        "explanation": "git log выводит список всех сделанных изменений с авторами и датами.",
        "category": "git",
        "difficulty": "easy"
    },
    {
        "question": "Что делает команда 'cp -r folder1 folder2'?",
        "options": ["Удаляет папку", "Рекурсивно копирует папку со всем содержимым", "Переименовывает папку", "Перемещает папку"],
        "correct_index": 1,
        "explanation": "Флаг -r (recursive) обязателен для копирования папок.",
        "category": "terminal",
        "difficulty": "medium"
    },
    {
        "question": "Что выведет print(10 // 3) в Python?",
        "options": ["3.333", "3", "4", "1"],
        "correct_index": 1,
        "explanation": "// — это оператор целочисленного деления.",
        "category": "python",
        "difficulty": "medium"
    },
    {
        "question": "Какая команда в терминале показывает, кто залогинен в системе?",
        "options": ["who", "users", "whoami", "me"],
        "correct_index": 2,
        "explanation": "whoami выводит имя текущего пользователя.",
        "category": "terminal",
        "difficulty": "easy"
    },
    {
        "question": "Что такое 'id_rsa' (без расширения .pub)?",
        "options": ["Ваш публичный ключ", "Ваш секретный (приватный) ключ SSH", "Название папки", "Файл с логами"],
        "correct_index": 1,
        "explanation": "Это приватный ключ. Его НЕЛЬЗЯ передавать никому, иначе доступ к вашим серверам будет открыт.",
        "category": "ssh",
        "difficulty": "medium"
    },
    {
        "question": "Как в CSS прижать элемент к правому краю экрана (старый способ)?",
        "options": ["align: right", "float: right", "move: right", "margin-right: 0"],
        "correct_index": 1,
        "explanation": "Float когда-то был основным способом позиционирования, сейчас чаще используют Flexbox.",
        "category": "html_css",
        "difficulty": "medium"
    },
    {
        "question": "Что такое 'коммит' (commit) в Git?",
        "options": ["Копия проекта", "Сохраненный снимок изменений с описанием", "Удаление файлов", "Ошибка в коде"],
        "correct_index": 1,
        "explanation": "Коммит фиксирует текущее состояние проекта в истории версий.",
        "category": "git",
        "difficulty": "easy"
    },
    {
        "question": "Как запустить Python-скрипт в фоновом режиме в Linux?",
        "options": ["python bot.py --background", "python bot.py &", "start python bot.py", "run bot.py"],
        "correct_index": 1,
        "explanation": "Символ & в конце команды запускает её в фоновом режиме терминала.",
        "category": "terminal",
        "difficulty": "hard"
    },
    # --- NEW QUESTIONS (82-132) ---
    {
        "question": "Что такое 'рекурсия' в программировании?",
        "options": ["Цикл for", "Функция, вызывающая саму себя", "Ошибка компиляции", "Тип данных"],
        "correct_index": 1,
        "explanation": "Рекурсия — это когда функция вызывает себя для решения более мелкой подзадачи.",
        "category": "general",
        "difficulty": "hard"
    },
    {
        "question": "Как в Python создать генератор списка (list comprehension) из чисел от 0 до 9?",
        "options": ["[x for x in range(10)]", "{x for x in range(10)}", "(x for x in range(10))", "[range(10)]"],
        "correct_index": 0,
        "explanation": "[x for x in range(10)] — это компактный способ создания списка.",
        "category": "python",
        "difficulty": "medium"
    },
    {
        "question": "Что делает блок 'finally' в конструкции try-except?",
        "options": ["Выполняется только при ошибке", "Выполняется всегда, независимо от наличия ошибки", "Останавливает программу", "Пропускает ошибку"],
        "correct_index": 1,
        "explanation": "Finally полезен для закрытия файлов или соединений, которые должны быть закрыты в любом случае.",
        "category": "python",
        "difficulty": "medium"
    },
    {
        "question": "Для чего нужен оператор 'yield' в Python?",
        "options": ["Для выхода из цикла", "Для создания функции-генератора", "Для удаления переменной", "Для импорта модуля"],
        "correct_index": 1,
        "explanation": "Yield возвращает значение и 'замораживает' состояние функции до следующего вызова.",
        "category": "python",
        "difficulty": "hard"
    },
    {
        "question": "Как в Python скопировать список 'a' в список 'b' так, чтобы они были независимы?",
        "options": ["b = a", "b = a.copy()", "b = set(a)", "b = move(a)"],
        "correct_index": 1,
        "explanation": "Метод copy() или срез a[:] создают новый объект в памяти.",
        "category": "python",
        "difficulty": "medium"
    },
    {
        "question": "Что такое 'git cherry-pick'?",
        "options": ["Удаление ветки", "Применение конкретного коммита из одной ветки в другую", "Сборка проекта", "Очистка репозитория"],
        "correct_index": 1,
        "explanation": "Cherry-pick позволяет перенести только один нужный коммит, не сливая ветки целиком.",
        "category": "git",
        "difficulty": "hard"
    },
    {
        "question": "Как в Git отменить коммит, создав новый 'обратный' коммит?",
        "options": ["git reset", "git revert", "git remove", "git undo"],
        "correct_index": 1,
        "explanation": "Revert — безопасный способ отмены, так как он не меняет историю, а добавляет новую запись.",
        "category": "git",
        "difficulty": "medium"
    },
    {
        "question": "Что делает команда 'git remote -v'?",
        "options": ["Удаляет сервер", "Показывает список адресов удаленных репозиториев", "Меняет версию Git", "Создает новую ветку"],
        "correct_index": 1,
        "explanation": "Флаг -v (verbose) выводит URL для fetch и push.",
        "category": "git",
        "difficulty": "medium"
    },
    {
        "question": "Как в Git посмотреть разницу между рабочим каталогом и последним коммитом?",
        "options": ["git diff", "git show", "git status", "git check"],
        "correct_index": 0,
        "explanation": "git diff показывает все незакоммиченные изменения в коде.",
        "category": "git",
        "difficulty": "easy"
    },
    {
        "question": "Для чего нужна команда 'git clone --depth 1'?",
        "options": ["Для полного копирования", "Для быстрого копирования только последнего коммита (без всей истории)", "Для клонирования скрытых веток", "Для удаления проекта"],
        "correct_index": 1,
        "explanation": "Shallow clone экономит время и место, если вам не нужна вся история изменений.",
        "category": "git",
        "difficulty": "hard"
    },
    {
        "question": "Как в терминале изменить владельца файла?",
        "options": ["chmod", "chown", "chgrp", "access"],
        "correct_index": 1,
        "explanation": "chown (change owner) позволяет сменить пользователя-владельца и группу файла.",
        "category": "terminal",
        "difficulty": "medium"
    },
    {
        "question": "Что делает команда 'alias g=\"git status\"'?",
        "options": ["Удаляет Git", "Создает короткий псевдоним 'g' для длинной команды", "Переименовывает Git", "Создает папку 'g'"],
        "correct_index": 1,
        "explanation": "Алиасы ускоряют работу, позволяя не печатать длинные команды целиком.",
        "category": "terminal",
        "difficulty": "easy"
    },
    {
        "question": "Как в терминале дописать текст в конец файла, не стирая его содержимое?",
        "options": ["echo 'text' > file.txt", "echo 'text' >> file.txt", "echo 'text' | file.txt", "append 'text' file.txt"],
        "correct_index": 1,
        "explanation": "'>' перезаписывает файл, а '>>' добавляет в конец.",
        "category": "terminal",
        "difficulty": "medium"
    },
    {
        "question": "Что делает флаг '-i' в команде grep?",
        "options": ["Игнорирует регистр (A и a — одно и то же)", "Показывает номера строк", "Ищет только в папках", "Инвертирует поиск"],
        "correct_index": 0,
        "explanation": "Флаг -i (ignore-case) делает поиск нечувствительным к регистру.",
        "category": "terminal",
        "difficulty": "medium"
    },
    {
        "question": "Как в терминале Linux посмотреть объем оперативной памяти?",
        "options": ["mem", "ram", "free -h", "show ram"],
        "correct_index": 2,
        "explanation": "Команда free показывает использование RAM и Swap.",
        "category": "os",
        "difficulty": "easy"
    },
    {
        "question": "Что такое 'root' в Linux?",
        "options": ["Обычный пользователь", "Суперпользователь с неограниченными правами", "Название папки с программами", "Командная строка"],
        "correct_index": 1,
        "explanation": "Root может изменять любые файлы в системе, поэтому работать под ним постоянно опасно.",
        "category": "os",
        "difficulty": "easy"
    },
    {
        "question": "Для чего используется команда 'scp'?",
        "options": ["Для удаления файлов", "Для безопасного копирования файлов между компьютерами по сети", "Для просмотра картинок", "Для сканирования портов"],
        "correct_index": 1,
        "explanation": "SCP (Secure Copy) работает через протокол SSH.",
        "category": "ssh",
        "difficulty": "medium"
    },
    {
        "question": "Что такое 'ssh-agent'?",
        "options": ["Вирус в системе", "Программа для хранения закрытых ключей в памяти", "Сервер для SSH", "Тип шифрования"],
        "correct_index": 1,
        "explanation": "SSH-agent позволяет не вводить пароль от ключа каждый раз при подключении.",
        "category": "ssh",
        "difficulty": "hard"
    },
    {
        "question": "Как в CSS создать переменную?",
        "options": ["$var: 10px;", "--my-var: 10px;", "var-my: 10px;", "@var: 10px;"],
        "correct_index": 1,
        "explanation": "Кастомные свойства в CSS начинаются с двойного дефиса.",
        "category": "html_css",
        "difficulty": "medium"
    },
    {
        "question": "Что такое 'CSS Specificity' (специфичность)?",
        "options": ["Скорость загрузки CSS", "Правила приоритета стилей (какой стиль победит)", "Адаптивность сайта", "Валидность кода"],
        "correct_index": 1,
        "explanation": "Стили по ID важнее стилей по классу, а те важнее стилей по тегу.",
        "category": "html_css",
        "difficulty": "hard"
    },
    {
        "question": "Как в CSS применить анимацию 'my-anim', которая длится 2 секунды?",
        "options": ["animation: my-anim 2s;", "animate: my-anim 2s;", "transition: my-anim 2s;", "keyframe: my-anim 2s;"],
        "correct_index": 0,
        "explanation": "Свойство animation связывает элемент с правилом @keyframes.",
        "category": "html_css",
        "difficulty": "medium"
    },
    {
        "question": "Что делает свойство 'box-sizing: border-box'?",
        "options": ["Скругляет углы", "Включает padding и border в общую ширину элемента", "Добавляет тень", "Делает элемент невидимым"],
        "correct_index": 1,
        "explanation": "Это упрощает верстку, так как размеры элемента не 'раздуваются' от отступов.",
        "category": "html_css",
        "difficulty": "hard"
    },
    {
        "question": "Какая файловая система является стандартной для современных Linux?",
        "options": ["NTFS", "FAT32", "ext4", "APFS"],
        "correct_index": 2,
        "explanation": "ext4 — четвертая версия расширенной файловой системы Linux.",
        "category": "os",
        "difficulty": "medium"
    },
    {
        "question": "Что такое 'UID' в Linux?",
        "options": ["Уникальный ID устройства", "Уникальный ID пользователя в системе", "Версия ядра", "Тип процессора"],
        "correct_index": 1,
        "explanation": "По UID система понимает, какой пользователь владеет файлом (у root UID всегда 0).",
        "category": "os",
        "difficulty": "hard"
    },
    {
        "question": "Какая команда в терминале позволяет переименовать файл 'a.txt' в 'b.txt'?",
        "options": ["rename a.txt b.txt", "mv a.txt b.txt", "cp a.txt b.txt", "edit a.txt b.txt"],
        "correct_index": 1,
        "explanation": "mv (move) используется и для перемещения, и для переименования.",
        "category": "terminal",
        "difficulty": "easy"
    },
    {
        "question": "Как в Python получить последний элемент списка 'L'?",
        "options": ["L[last]", "L[-1]", "L[end]", "L.last()"],
        "correct_index": 1,
        "explanation": "Отрицательные индексы в Python считают элементы с конца.",
        "category": "python",
        "difficulty": "easy"
    },
    {
        "question": "Что делает метод 'string.strip()' в Python?",
        "options": ["Переводит в верхний регистр", "Удаляет пробелы в начале и в конце строки", "Разбивает строку на части", "Заменяет символы"],
        "correct_index": 1,
        "explanation": "Strip убирает лишние невидимые символы (пробелы, переносы строк).",
        "category": "python",
        "difficulty": "medium"
    },
    {
        "question": "Для чего используется тег <meta charset='UTF-8'>?",
        "options": ["Для вставки стилей", "Для указания кодировки символов на странице", "Для подключения скриптов", "Для заголовка сайта"],
        "correct_index": 1,
        "explanation": "Это гарантирует, что браузер правильно отобразит кириллицу и спецсимволы.",
        "category": "html_css",
        "difficulty": "easy"
    },
    {
        "question": "Что такое 'Media Queries' в CSS?",
        "options": ["Запросы к базе данных", "Стили для адаптации под разные размеры экранов", "Проигрыватель видео", "Список шрифтов"],
        "correct_index": 1,
        "explanation": "С помощью @media можно менять дизайн сайта для телефонов и планшетов.",
        "category": "html_css",
        "difficulty": "medium"
    },
    {
        "question": "Какая команда в Git удаляет файл из репозитория, но оставляет его на диске?",
        "options": ["git rm file.txt", "git rm --cached file.txt", "git delete file.txt", "git ignore file.txt"],
        "correct_index": 1,
        "explanation": "--cached удаляет файл только из индекса (коммита).",
        "category": "git",
        "difficulty": "hard"
    }
]
