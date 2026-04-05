FROM python:3.10-slim

WORKDIR /mainapp

COPY requirement1.txt .

RUN pip install --no-cache-dir -r requirement1.txt

COPY . .

RUN mkdir -p uploads

EXPOSE 8000

CMD ["uvicorn", "mainapp:app", "--host", "0.0.0.0", "8000"]

