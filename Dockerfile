FROM python:3
WORKDIR /app
ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0
COPY requirement.txt /app/requirement.txt
RUN pip install --upgrade pip
RUN pip install -r /app/requirement.txt
EXPOSE 5000
COPY . .
CMD ["flask", "run"]