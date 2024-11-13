# 类形式
import pytest

aa = 2

class TestDemo(object):
    @pytest.mark.run(order=2)
    def test_func1(self):
        print('我是函数1')

    @pytest.mark.run(order=1)
    def test_func2(self):
        print('我是函数2')

    @pytest.mark.skipif(aa >= 2, reason='33333')
    def test_func3(self):
        print('我是函数3')

    def test_func4(self):
        print('我是函数4')
