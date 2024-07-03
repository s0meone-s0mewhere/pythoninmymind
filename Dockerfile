# syntax=docker/dockerfile:1


FROM python


ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Задать рабочий каталог
WORKDIR /pythoninmymind

# Установить зависимости
#RUN pip install --upgrade pip
RUN --mount=type=cache,target=/root/.cache/pip \
    --mount=type=bind,source=requirements.txt,target=requirements.txt \
    python -m pip install -r requirements.txt

COPY . /pythoninmymind/

EXPOSE 8000
CMD ["./wait-for-it.sh", "db:5432", "--", "uwsgi", "--ini", "./config/uwsgi/uwsgi.ini"]




