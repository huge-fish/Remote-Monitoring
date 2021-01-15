import psutil
import os
def get_all_info():
    with open('p.txt', 'w+', encoding='utf-8') as f:
        f.seek(0)
        f.truncate()
        pids = psutil.pids()
        for pid in pids:
            try:
                p = psutil.Process(pid)
            except Exception as e:
                continue
            name = p.name()
            memInfo = p.memory_info().rss
            info = str(pid) +' ' +"proccess name:"+name +' memory:'+str(int(memInfo / 1024 / 1024))
            f.write(info)
            f.write('\n')

def kill_p(pid):
    cmd = 'taskkill /F /IM '
    try:
        p = psutil.Process(pid)
    except Exception as e:
        return
    name = p.name()
    cmd = cmd + name
    os.system(cmd)




