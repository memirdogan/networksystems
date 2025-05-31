import threading

def coder(number, number2):
    print(f'Coder ID: {number}, {number2}')

threads = []
for k in range(5):
    for l in range(5):
        t = threading.Thread(target=coder, args=(k,l))
        threads.append(t)
        t.start()