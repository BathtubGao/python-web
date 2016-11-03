import orm,asyncio,sys
from models import User,Blog,Comment

# 测试连接与save方法
@asyncio.coroutine
def test():
    yield from orm.create_pool(loop,user='admin',password='admin123',db='gaoyu_test')
    u = User(name='Jack',email='jack@sina.com.cn',passwd='123456',image='about:blank')
    yield from u.save()
    yield from orm.destory_pool()

loop = asyncio.get_event_loop()
loop.run_until_complete(test())
loop.close()
