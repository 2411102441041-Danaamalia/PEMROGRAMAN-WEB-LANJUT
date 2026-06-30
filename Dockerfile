FROM python:3.12-alpine

ENV PYTHONTDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

RUN apk update && apk add --no-cache gcc musl-dev linux-headers

RUN echo "django==5.2" > requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

COPY . /app/

EXPOSE 8000

CMD ["sh", "-c", "pip install gunicorn && gunicorn mysite.wsgi:application --bind 0.0.0.0:8000 --workers 2"]