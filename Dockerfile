FROM python:3.9.4 as backend

ARG DJANGO_ENV=local

ENV LANG=C.UTF-8 LC_ALL=C.UTF-8 \
  DJANGO_ENV=${DJANGO_ENV} \  
  PYTHONFAULTHANDLER=1 \
  PYTHONUNBUFFERED=1 \
  PYTHONHASHSEED=random \  
  PIP_NO_CACHE_DIR=off \
  PIP_DISABLE_PIP_VERSION_CHECK=on \
  PIP_DEFAULT_TIMEOUT=100 \  
  POETRY_VERSION=1.1.6 \
  POETRY_VIRTUALENVS_CREATE=false

RUN apt update && apt install -y \
  curl \
  libffi-dev \
  openssl \
  musl-dev \
  cron \
  && rm -rf /var/lib/apt/lists/* \
  && pip install "poetry==$POETRY_VERSION"

WORKDIR /pysetup
COPY ./pyproject.toml ./poetry.lock*  /pysetup/
RUN echo $DJANGO_ENV
RUN poetry install $(test "$DJANGO_ENV" = production && echo "--no-dev") --no-interaction --no-ansi

WORKDIR /app
COPY . /app

ENV SENTRY_RELEASE YYZ
RUN chmod +x /app/entrypoint/entrypoint.sh
RUN mv .env.template .env
RUN python /app/manage.py collectstatic --no-input
ENTRYPOINT ["/app/entrypoint/entrypoint.sh"]


FROM nginx:1.17.6 as server
RUN mkdir -p /static/admin
COPY --from=backend /static/* /static/admin/
COPY entrypoint/nginx.conf /etc/nginx/nginx.conf
