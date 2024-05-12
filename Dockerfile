FROM python:latest

# RUN apk update && \
#     apk add --no-cache python3 && \
#     # pip install --upgrade pip && \
#     # pip install flask

RUN pip install flask


WORKDIR /app

COPY web_server.py /app/web_server.py

EXPOSE 5000

CMD ["python", "web_server.py"]

# CMD ["sleep", "10000"]