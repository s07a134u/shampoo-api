import os
from google.cloud import storage


# 設定
BUCKET_NAME = "shampoo_api"          # アップロード先のバケット名
LOCAL_FILE = "shampoo.csv"             # アップロードするファイル名
DESTINATION_BLOB = "shampoo.csv"  # GCS上で保存するファイル名



def upload(bucket_name, source_file, destination_blob):

    
#引数チェック
    if bucket_name is None:
        raise ValueError("bucket_name が None です。")
    if source_file is None:
        raise ValueError("source_file が None です。")
    if destination_blob is None:
        raise ValueError("destination_blob が None です。")

#アップロード処理

    #GCSにアクセスする窓口を作成
    client = storage.Client()

    #GCSの中のバケットを指定してアクセスする
    bucket = client.bucket(bucket_name)

    #バケットの中に作るファイル（Blob＝オブジェクト）を指定
    blob = bucket.blob(destination_blob)   

    #ローカルのファイルをバケットにアップロード
    blob.upload_from_filename(source_file)

    #正しくアップロードされた場合コンソールに出力
    print(f"Uploaded {source_file} to gs://{bucket_name}/{destination_blob}")
