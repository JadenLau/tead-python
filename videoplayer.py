import os
import time
ht = "#"

video = {
    'name': 'untitled',
    'res': [5,8],
    'px': 4096,
    'fps': 30,
    'data': [
        [[ht,91]]*40,
        [[ht,92]]*40,
        [[ht,93]]*40,
        [[ht,94]]*40,
        [[ht,95]]*40,
        [[ht,96]]*40,
        [[ht,97]]*40
    ]
}
echo_tmp = ""
def echo_run():
    os.system('clear')
    os.system(f'echo -e "{echo_tmp}"')

def echo_store(data):
    global echo_tmp
    print(f'data: {data}')
    # for a in data:
    a = data
    echo_tmp += f'\033[{a[1]}m{a[0]}'
    

for a in range(len(video['data'])):
    for b in video['data'][a]:
        echo_store(b)
        # for c in b:
        #     tmp += str(c)
        #     print(str(c))
        # echo_store(b)
    echo_run()
    time.sleep(1/video['fps'])