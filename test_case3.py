import unittest
from login import get_password,get_username

version = 2.0

class TestLogin(unittest.TestCase):


    # 类方法
    @classmethod
    def setUpClass(cls) -> None:
        print('执行类之前执行')
    @classmethod
    def tearDownClass(cls) -> None:
        print('执行类之后执行')
    # 初始化用例
    def setUp(self) -> None:
        print('每次执行用例前执行')
    # 清空方法
    def tearDown(self) -> None:
        print('每次执行用例后执行')

    def test_login_username(self):
        print('获取用户名33333')
        # 预期结果：自己登录的账号
        expect_username = 'test01'
        # 实际结果：显示在页面的账号
        actual_username = get_username()
        self.assertEqual(expect_username,actual_username)
        # assert expect_username == actual_username

    # @unittest.skip('跳过获取密码')
    @unittest.skipIf(version>1,'跳过获取密码')
    def test_login_password(self):
        print('获取密码33333')
        # 预期结果：自己登录的密码
        expect_password = 'password01'
        # 实际结果：显示在页面的密码
        actual_password = get_password()
        self.assertEqual(expect_password,actual_password)
        # assert expect_password == actual_password

# if __name__ == '__main__':
    # test_login_username()
    # test_login_password()
    # unittest.main()


# 创建一个测试套件，相当于一组用例
# suite = unittest.TestSuite()
# suite.addTest(TestLogin('test_login_username'))
# suite.addTest(TestLogin('test_login_password'))
#
# runner = unittest.TextTestRunner()
# runner.run(suite)


# 使用TestLoader
suite = unittest.TestLoader().discover('.',pattern='test*.py')
runner = unittest.TextTestRunner()
runner.run(suite)
