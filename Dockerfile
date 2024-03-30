# syntax=docker/dockerfile:1

# Comments are provided throughout this file to help you get started.
# If you need more help, visit the Dockerfile reference guide at
# https://docs.docker.com/go/dockerfile-reference/

# Want to help us make this template better? Share your feedback here: https://forms.gle/ybq9Krt8jtBL3iCk7


FROM python

# Задать переменные среды
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Задать рабочий каталог
WORKDIR /pythoninmymind

# Установить зависимости
RUN pip install --upgrade pip
RUN --mount=type=cache,target=/root/.cache/pip \
    --mount=type=bind,source=requirements.txt,target=requirements.txt \
    python -m pip install -r requirements.txt

COPY . /pythoninmymind/

EXPOSE 8000
CMD ["./wait-for-it.sh", "db:5432", "--", "uwsgi", "--ini", "./config/uwsgi/uwsgi.ini"]




