from urllib import request
import json
import time
import threading

code = input('帖子编码')
url = "https://api.codemao.cn/web/forums/posts/"+code+"/details?offset=1&limit=10"
user_agent = "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHML, like Gecko) Chrome/27.0.1453.94 Safari/537.36"

head = {}
head["User-Agent"] = user_agent


def blaster(thread_i):
    for i in range(0, 150):
        req = request.Request(url, headers=head)

        response = request.urlopen(req)
        data = response.read().decode('utf-8')

        j = json.loads(data)

        print("\033[36m[ThreadId: {}]\033[30m ".format(
            threading.currentThread().ident) + str(j['n_views']))
        time.sleep(0.1)


t = [None for x in range(2)]
for i in range(1, 1000):
    t[i] = threading.Thread(target=blaster, args=[str(i)])
    t[i].start()

if __name__ == '__main__':
    try:
        while 1:
            pass
    except KeyboardInterrupt:
        pass