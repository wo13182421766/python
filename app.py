
import logging; logging.basicConfig(level=logging.INFO)

import asyncio, os, json, time
from datetime import datetime

from aiohttp import web

def index(request):
    return 
    return web.Response(body=b'<h1>Awesome</h1>', content_type='text/html')

# @ 只能修饰函数，且必须要在 def 上一行，asyncio.coroutine 作为一个函数 init 就是传入的参数
#把一个 generator 标记为 coroutine(协程) 类型，然后，我们就把这个 coroutine 扔到 EventLoop 中执行
@asyncio.coroutine
def init(loop):
    app = web.Application(loop=loop)
    app.router.add_route('GET', '/', index)
    srv = yield from loop.create_server(app.make_handler(), '127.0.0.1', 9000)
    logging.info('server started at http://127.0.0.1:9000...')
    return srv

loop = asyncio.get_event_loop()
loop.run_until_complete(init(loop))
loop.run_forever()