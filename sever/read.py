import pickle
def write_log(logInfo):
    with open('runlog.txt', 'r') as runlog:
        runlog.write(logInfo)
def read_txt():
    with open('p.txt', 'r') as f:
        list_p = []
        while 1:
            text = f.readline()
            if text == '' or text == '\n':
                break
            text = text.strip()
            list_p.append(text)
        return list_p

def get_pid(list_p):
    return int(list_p.split(" ")[0])


def read_apl():
    kf = open('key.apl', 'rb')
    keylog = pickle.load(kf)
    kf.close()
    return keylog








if __name__ == '__main__':
    a = read_apl()
    print(a)
