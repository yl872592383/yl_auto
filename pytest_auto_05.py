#   特殊方法函数形式
import pytest


class TestDemo(object):

    def setup(self):
        print("开始")

    def teardown(self):
        print("结束")

    def test_func1(self):
        print('我是函数1')

    def test_func2(self):
        print('我是函数2')


if __name__ == '__main__':
    pytest.main(['-s', 'pytest_auto_05.py'])
