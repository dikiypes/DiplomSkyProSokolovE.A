FROM python:3.11

# Копирование requirements.txt и установка зависимостей
COPY requirements.txt .


RUN pip install --no-cache-dir -r requirements.txt

# Копирование остальных файлов проекта
COPY . .

# Запуск сервера Django
CMD ["sh", "-c", "python manage.py migrate && python manage.py runserver 0.0.0.0:3055"]
