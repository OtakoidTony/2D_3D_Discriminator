import requests
import json
from tqdm import tqdm
import urllib.request

opener=urllib.request.build_opener()

opener.addheaders=[('User-Agent','Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1941.0 Safari/537.36')]

urllib.request.install_opener(opener)

def get_dict(page=1, is3d=False):
    req = requests.get("https://gelbooru.com/index.php?page=dapi&s=post&q=index&json=1&tags=loli%20" +
                       ("3d" if is3d else "-3d")+"&limit=100&pid="+str(page))
    return json.loads(req.text)


for page in tqdm(range(1, 100)):
    data = get_dict(page, True)
    for e in data:
        url = e["file_url"]
        if url[-1] == "g":  # 확장명이 g로 끝나는 경우, gif나 mp4 파일들은 걸러짐.
            urllib.request.urlretrieve(url, "dataset/3d/"+e["image"])

for page in tqdm(range(1, 100)):
    data = get_dict(page, False)
    for e in data:
        url = e["file_url"]
        if url[-1] == "g":
            urllib.request.urlretrieve(url, "dataset/2d/"+e["image"])