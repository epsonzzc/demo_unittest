import unittest
from parameterized import parameterized

def add(x,y):
    return x+y

class TestAdd(unittest.TestCase):


    def test_add_01(self):
        res1 = add(1,2)
        self.assertEqual(res1,3)

    def test_add_02(self):
        res2 = add(1,0)
        self.assertEqual(res2, 1)

    def test_add_03(self):
        res3 = add(-1, 2)
        self.assertEqual(res3, 1)

    # def test_add(self):
    #     test_data = [(1,2,3),(1,0,1),(-1,2,1)]
    #     for x,y,expect in test_data:
    #         res = add(x,y)
    #         self.assertEqual(res,expect)

    @parameterized.expand([(1, 2, 3), (1, 0, 1), (-1, 2, 1)])
    def test_add(self,a,b,expect):
        res = add(a,b)
        self.assertEqual(res,expect)





if __name__ == '__main__':
    # global test_data = [(1, 2, 3), (1, 0, 1), (-1, 2, 1)]
    unittest.main()
