# 类形式
import pytest


class TestDemo(object):
    def test_func1(self):
        print('我是函数1')

    def test_func2(self):
        print('我是函数2')


if __name__ == '__main__':
    pytest.main(['-s', 'pytest_auto_04.py'])
