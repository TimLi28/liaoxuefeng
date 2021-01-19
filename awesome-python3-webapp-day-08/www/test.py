#!/usr/bin/env python     
# -*- coding:utf-8 -*-
# @Time    : 2020/3/19 21:41
# @Author  : Winnie
# @Email   : licy8@wasu.com
# @File    : test.py
# @Software: PyCharm
import orm
import sys
import asyncio
from models import User, Blog, Comment

async def test(loop):
	await orm.create_pool(loop=loop, user='root', password='hzcnc_enable', db='awesome')

	u = User(name='licy', email='123', passwd='1234567890', image='about:blank')

	await u.save()

if __name__ == '__main__':

    loop = asyncio.get_event_loop()
    loop.run_until_complete( asyncio.wait([test( loop )]) )
    loop.close()
    if loop.is_closed():
        sys.exit(0)