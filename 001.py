import unittest
class TestLogin(unittest.TestCase):

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