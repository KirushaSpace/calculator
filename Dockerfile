FROM python:3.10

ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1

WORKDIR /code

# Install dependencies
COPY ./req.txt .
RUN pip install --no-cache-dir --upgrade -r req.txt

COPY . .

ENV PYTHONPATH=/code
EXPOSE 8000