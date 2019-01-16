from unittest import mock
import unittest
from module import Count

class TestCount(unittest.TestCase):

    def test_add(self):
        count = Count()
        #通过Mock类模拟被调用的方法add()方法，return_value 定义add()方法的返回值
        count.add = mock.Mock(return_value=13, side_effect=count.add)
        result = count.add(8, 8)
        print(result)
        count.add.assert_called_with(8, 8)
        self.assertEqual(result, 16)

if __name__ == '__main__':
    unittest.main()
