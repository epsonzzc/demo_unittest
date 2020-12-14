import login


def test_login_username():
    # 预期结果：自己登录的账号
    expect_username = 'test01'
    # 实际结果：显示在页面的账号
    actual_username = login.get_username()
    assert expect_username == actual_username

def test_login_password():
    # 预期结果：自己登录的密码
    expect_password = 'password01'
    # 实际结果：显示在页面的密码
    actual_password = login.get_password()
    assert expect_password == actual_password


test_login_password()
test_login_username()