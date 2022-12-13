from os import path
import sys
import requests

YA_TOKEN = ""


class YaUploader:
    def __init__(self, token: str):
        self.token = token

    def upload(self, file_path: str):
        """Метод загружает файл file_path на яндекс диск"""
        url = "https://cloud-api.yandex.net/"
        headers = {"Content-Type": "application/json", "Accept": "application/json",
                   "Authorization": f"OAuth {self.token}"}

        # create test folder on disk
        request = "v1/disk/resources"
        params = {"path": "/test_upload"}
        req = requests.put(url=url + request, params=params, headers=headers)
        if req.status_code != 200 and req.status_code != 201 and req.status_code != 409:
            return req.status_code

        # upload file
        request = "v1/disk/resources/upload"
        params = {"path": f"test_upload/{path.split(file_path)[1]}", "overwrite": "True"}
        req = requests.get(url=url+request, params=params, headers=headers)
        if req.status_code == 200:
            href = req.json()['href']
            with open(file_path, 'rb') as f:
                req = requests.put(href, files={'file': f})
                return req.status_code
        else:
            return req.status_code


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('File path needed')
        sys.exit(1)

    FILE_PATH = sys.argv[1]

    if not path.exists(FILE_PATH):
        print('File does not exists')
        sys.exit(1)

    uploader = YaUploader(YA_TOKEN)
    result = uploader.upload(FILE_PATH)
    print(result)
