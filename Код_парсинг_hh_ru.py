import requests
import json
import os
import time

# Директория для хранения файлов с вакансиями
vacancies_dir = 'C:/vacancy'
os.makedirs(vacancies_dir, exist_ok=True)

vacancies_file = os.path.join(vacancies_dir, 'all_vacancies.json')


# Функция для добавления вакансии в подходящий файл
def add_vacancy_to_file(vacancy):
    with open(vacancies_file, 'a', encoding='utf-8') as file:
        json.dump(vacancy, file, ensure_ascii=False)
        file.write('\n')

    # Остальная часть кода (функция fetch_vacancies и точка входа main) остается без изменений


def fetch_vacancies(keywords=['Программист'], max_vacancies=50000000):
    all_vacancies = []

    for keyword in keywords:
        page = 0

        while len(all_vacancies) < max_vacancies:

            params = {'text': keyword, 'page': page, 'per_page': 100}
            try:
                response = requests.get('https://api.hh.ru/vacancies', params=params)
                response.raise_for_status()
                vacancies = response.json()

                if 'items' in vacancies:
                    for vacancy in vacancies['items']:
                        if vacancy not in all_vacancies:  # Избегаем дублирования
                            all_vacancies.append(vacancy)
                            add_vacancy_to_file(vacancy)  # Добавляем вакансию в файл
                            print(f'Текущее количество найденных вакансий: {len(all_vacancies)}')  # Вывод прогресса

                        if len(all_vacancies) >= max_vacancies:
                            break
                else:
                    break

                if 'pages' in vacancies and page >= vacancies['pages']:
                    break
                time.sleep(1)
                page += 1


            except requests.exceptions.HTTPError as e:
                print(f"HTTP error occurred: {e}")
                break


            except requests.exceptions.ConnectionError as e:
                print(f"Connection error occurred: {e}")
                time.sleep(1)  # Ждем перед повторной попыткой


    return all_vacancies

if __name__ == '__main__':
# Теперь принимаем список ключевых слов, разделенных запятой

    keywords = [
    'Программист', 'Разработчик', 'Developer', 'Тимлид', 'Teamlead', 'Team lead', 'Тестировщик', 'Аналитик',
    'Консультант','Project manager', 'IT Planning', 'ИТ директор', 'Директор по ИТ', 'IT Director', 'IT-директор',
    'Технический директор','CTO', 'Chief Technical Officer', 'Engineer', 'Инженер', 'Architect', 'Usability', 'Директор IT департамента',
    'Data mining', 'System Analyst', 'Programmer', 'Интерфейс', 'Инновации', 'Testing', 'QA',
    'Аналитика данных','Data Analyst', 'Data Scientist', 'Big Data', 'Machine Learning', 'Python', 'SQL','NoSQL', 'Tableau', 'Power BI',
    'Исследование данных', 'BI Analyst', 'Анализ данных', 'C++', 'C#', 'Java', 'Frontend разработчик',
    'Backend разработчик','Fullstack разработчик', 'DevOps инженер', 'Системный администратор', 'Тестировщик ПО', 'Продуктовый менеджер',
    'UI/UX дизайнер', 'Инженер по кибербезопасности', 'Игровой разработчик', 'Мобильный разработчик',
    'Разработчик блокчейн','Cloud инженер', 'Специалист по искусственному интеллекту', 'Специалист по Big Data', 'Менеджер проектов в IT',
    'Специалист по внедрению ERP систем', 'Интернет-маркетолог', 'Контент-менеджер',
    'Специалист по работе с клиентами в IT','SEO-специалист', 'Специалист по электронной коммерции', 'Веб-разработчик', 'Специалист по 3D моделированию',
    'Архитектор ПО', 'Специалист по машинному обучению', 'Системный интегратор', 'Сетевой инженер',
    'Специалист по IT-безопасности','Технический писатель', 'Облачные вычисления', 'Машинное обучение', 'Глубокое обучение',
    'Искусственный интеллект','Блокчейн', 'Криптовалюта', 'Большие данные', 'Интернет вещей', 'Кибербезопасность', 'Автоматизация', 'API',
    'DevOps','Контейнеризация','Сетевые протоколы', 'Software Development Life Cycle', 'SDLC',
    'DevOps Practices','Cloud Service Management', 'Data Visualization', 'Blockchain Technology', 'Cybersecurity Practices',
    'Internet of Things', 'IoT','Augmented Reality', 'AR', 'Virtual Reality', 'VR', 'Quantum Computing', 'Ethical Hacking',
    'Network Architecture','Digital Marketing Technologies', 'Content Management Systems', 'CMS', 'E-commerce Systems',
    'Project Management Methodologies','Agile', 'Scrum', 'анализ данных','работа с данными','seo','data','product manager',
    'IT', 'internet technology','AI','artificial intelligence','ML', 'Cloud', 'Architecture', 'Cybersecurity',
    'ИИ', 'языки программирования', 'Программирование','Администрирование серверов','cервер','Сетевые технологии',
    'Обеспечение безопасности сетей','Мониторинг и диагностика систем','Криптография','Защита данных','Проверка на проникновение',
    'Аудит безопасности','HTML','CSS','JavaScript','Фреймворки','React', 'Angular','Веб-серверы','Адаптивная верстка',
    'Визуализация данных','Статистический анализ','Инженер по автоматизации тестирования', 'Тестирование ПО','Selenium',
    'Автоматизация тестирования','Интеграционное тестирование','Continuous Integration','Continuous Deployment', 'CI','CD',
    'Docker', 'Kubernetes','Оркестрация ПО','Конфигурационное управление','Мониторинг инфраструктуры','Облачные сервисы для обработки данных', 'Data pipeline',
    'Нейронные сети', 'Глубокое обучение', 'Deep Learning',
    'Natural Language Processing', 'NLP', 'Computer Vision', 'Reinforcement Learning','Business Intelligence',
    'Защита информации','Системы обнаружения вторжений','IDS','Quality Assurance Engineer','Тест-дизайн',
    'Архитектура информационных систем','Cloud Engineer','Высокодоступные системы','Безопасность облачных сервисов',
    'Database Administrator','Database','СУБД','Network Engineer','PHP','Node.js', 'Appium','UI/UX',
    'искусственный интелект', 'Computer', 'Fullstack', 'ПО', 'Backend', 'Systems', 'игры', 'framework',
    'ERP','Веб','дизайн','Laravel','WordPress','MySQL','Oracle','Jira','бэкенд','фронтенд','виртуальная реальность',
    'Hibernate','технологии','Spring','проект','Junior','junior','джун','джуниор','Middle','middle','миддл','Senior','senior',
    'сеньор','Tech-продукт','Webflow','Carta','Alto','growth-директор','iOS','Android',
    'хранилищи информации', 'information technologies', 'конструирование компьютерных сетей', 'IT-отдел',
    'SEO-стратегия', 'СЕО-копирайтер', 'ATS', 'CV', 'Curriculum vitae', 'Go-to-market', 'поисковая система',
    'цифровой маркетинг', 'контент', 'цифровая среда',
    'ИТ-консалтинг', 'программные решения', 'аутсорсинг программного обеспечения', 'SERM', 'boolean',
    '1C', 'Ruby', 'написание кода',
    'Linux', 'Windows', 'MacOS', 'SQL Server', 'опыт работы с системами защиты информации',
    'Умение настраивать сетевые устройства',
    'Умение управлять сетевыми устройствами', 'маршрутизаторы', 'коммутаторы', 'сетевые точки доступа',
    'Знание основных протоколов сетевой связи',
    'HTTP', 'TCP', 'IP', 'FTP', 'Навыки работы с системами управления проектами', 'JIRA', 'Trello', 'Asana',
    'КриптоПро CSP', 'Git', 'plugin', 'плагины', 'Delphi', 'Visual Basic',
    'PhotoShop', 'CorelDraw', 'FrontPage', 'Waterfall',
    'Computer Science', 'Computer science', 'computer science', 'Analytical Skills', 'Analytical skills',
    'analytical skills',
    'Corel DRAW', 'Math CAD', 'Auto CAD', 'MatLab',
    'Acrobat Reader', 'STATISTIKA', 'Sjlaris', 'DB/2', 'Novell Netware', 'Unix', 'Apache', 'IIS', 'MS Project',
    'Rational Rose',
    'UML', 'MS Visio', 'Web Load', 'MS ACT', 'Application Center Test', 'Silk Test', 'Silk Performer', 'NUnit',
    'JUnit',
    'MS Outlook', 'MS Exchange Server', 'Visual C++', 'MFC', 'Win32 API', 'OLE', 'STL', 'ATL', 'DCOM', 'COM',
    'COM+', 'MTS',
    'ActiveX', 'ODBC', 'ADO', 'OLE DB', 'VSS', 'Visual Basic', 'VBA', 'XML', 'XSL', 'UML', 'ASP', 'CORB', 'Pascal',
    'OpenGL', 'DirectX', 'Proxy', 'FireWall', 'антивирус',
    'создание ботов', 'бот', 'парсинг', 'parsing', 'Azure', 'AWS', 'Google Cloud', 'Amazon Web',
    'Kamatera','Shopify', 'WooCommerce', 'BigCommerce', 'Magento', 'OpenCart', 'облачная безопасность',
    'анализ вредоносных программ',
    'обнаружение вторжений', 'CEH', 'OSCP', 'CISA', 'GCIH', 'разработка безопасного кода',
    'шифрование данных и файлов',
    'OLAP', 'запросы данных', 'технология кубов данных', 'обработка и интеграция необработанных данных',
    'структуры данных и алгоритмы', 'обработка естественного языка', 'интеграция и применение ИИ',
    'Software Development Kit', 'разработка Xcode', 'Github', 'React.js', 'Angular', 'служба поддержки ИТ',
    'GitHub', 'Bugzilla', 'Jenkins', 'Ansible', 'Terraform', 'Девопс', 'техписатель', 'Ява', 'Рубин', 'ИКТ',
    'Новые технологии', 'Файловые системы', 'Мобильные приложения', 'Визуальный FoxPro', 'FoxPro',
    'Пользовательский интерфейс',
    'ТензорФлоу', 'Программная инженерия', 'Потоки взаимодействия', 'сетевые структуры', 'Управление конфигурацией',
    'ЭВМ', 'Swift', 'CISM', 'CISSP', 'SEM', 'Meta skills', 'meta skills', 'хакатон', 'PostgreSQL',
    'ActionScript', 'Perl', 'стек', 'модульное тестирование', 'паттерны проектирования', 'IDE', 'bugs', 'bug',
    'баг','баги', 'userstory']
    all_vacancies = fetch_vacancies(keywords=keywords)
    print(f'Найдено вакансий: {len(all_vacancies)}')