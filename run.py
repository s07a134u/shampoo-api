from shampoo_get_API import RakutenAPI
from upload import upload

# 設定
BUCKET_NAME = "shampoo_api"          # アップロード先のバケット名
LOCAL_FILE = "shampoo.csv"             # アップロードするファイル名
DESTINATION_BLOB = "shampoo.csv"  # GCS上で保存するファイル名


def run():
    OUTPUT_CSV = RakutenAPI()
    print(f"{OUTPUT_CSV}を出力しました")

    #関数を呼び出す
    upload(BUCKET_NAME, LOCAL_FILE, DESTINATION_BLOB)

if __name__ == "__main__":
    run()

