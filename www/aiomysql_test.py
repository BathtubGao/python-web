import asyncio
import aiomysql

loop = asyncio.get_event_loop()

async def go():
    pool = await aiomysql.create_pool(host='192.168.0.145', port=3306,
                                           user='admin', password='admin123',
                                           db='gaoyu_test', loop=loop)

    with (await pool) as conn:
        cur = await conn.cursor()
        await cur.execute('insert into `users` (`email`,`created_at`,`admin`,`image`,`name`,`passwd`,`id`) values (%s,%s,%s,%s,%s,%s,%s)',['test@example.com', 1477035744.0416503, False, 'about:blank', 'Test', '123456', '00147703574404139eba149c6a6431ab9b249c8f2d622f4000'])
        # print(cur.description)
        affected = cur.rowcount
        await conn.commit()
        cur.close()
        conn.close()
    pool.close()
    await pool.wait_closed()

loop.run_until_complete(go())