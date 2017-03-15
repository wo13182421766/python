def consumer():
    r = ''
    while True: #step3 无限执行
        n = yield r #step4 执行到最后 r = '200 OK' 再回到这一行，将 r 返回给 produce 的 'r = c.send(n)' 中的 r 并继续执行 produce 中的代码
        if not n:
            return
        print('[CONSUMER] Consuming %s...' % n)
        r = '200 OK'

def produce(c):
    c.send(None) #step1 执行 consumer 到 yield r
    n = 0
    while n < 5:
        n = n + 1
        print('[PRODUCER] Producing %s...' % n)
        r = c.send(n) #step2 将 n == 1 传给 'n = yield r' 中的 n 并继续执行 consumer 中代码
        print('[PRODUCER] Consumer return: %s' % r)
    c.close()

c = consumer()
produce(c)