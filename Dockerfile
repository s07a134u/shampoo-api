FROM python

WORKDIR /workspace

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

#アプリ一式
COPY shampoo_get_API.py upload.py run.py /workspace/

# 実行（引数がある場合はrun時に渡せます）
CMD ["python", "/workspace/run.py"]
