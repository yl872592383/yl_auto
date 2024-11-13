# 函数形式
import pytest


def test_func():
    print('我是函数')


if __name__ == '__main__':
    pytest.main(['-s', 'pytest_auto_01.py'])
