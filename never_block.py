"""
docker run \
    -e HEADS=7 \
    -e TORS=3 \
    -p 8800:8800 \
    -p 1080:1080 \
    -p 2090:2090 \
    -p 8888:8888 -p 8889:8889 -p 8890:8890 -p 8891:8891 -p 8892:8892 -p 8893:8893 -p 8894:8894 \
    datawookie/medusa-proxy
"""

from itertools import cycle
import logging
from time import time, sleep

logging.basicConfig(
    level="WARN", 
    filename=NAME + ".log",
    format='%(asctime)s,%(msecs)d %(levelname)-8s [%(filename)s:%(lineno)d] %(message)s',
    datefmt='%Y-%m-%d:%H:%M:%S',
)

list_proxy = [
    "http://127.0.0.1:8888",
    "http://127.0.0.1:8889",
    "http://127.0.0.1:8890",
    "http://127.0.0.1:8891",
    "http://127.0.0.1:8892",
    "http://127.0.0.1:8893",
    "http://127.0.0.1:8894",
]

proxy_cycle = cycle(list_proxy)

def main(keyword):
    try:
        proxy = next(proxy_cycle)
        proxies = {
            "http": proxy,
            "https":proxy
        }
        headers = {'User-agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36 Edge/12.246"}
        response = requests.get(
            f"http://suggestqueries.google.com/complete/search?client=firefox&hl=vi&q={keyword}",
            timeout=(60, 60),
            headers=headers,
            proxies=proxies
        )
        if response.status_code == 200:
            result = json.loads(response.content.decode('utf-8'))
            print("Result: " + result[1])
        else:
            print("Status: " + response.status_code)
    except requests.exceptions.ReadTimeout as ex_timeout:
            sleep(1)
            pass
    except Exception as ex:
        logging.exception(ex)

if __name__ == "__main__":
    main("quần áo")