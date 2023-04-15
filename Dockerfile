FROM tiangolo/uvicorn-gunicorn-fastapi:python3.10-2022-11-25



COPY requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD [ "uvicorn", "app.main:app" , "--host",  "0.0.0.0" , "--port", "8000"] 