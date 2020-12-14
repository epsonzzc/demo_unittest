import unittest
from HTMLTestRunner import HTMLTestRunner

suite = unittest.TestLoader().discover('.',pattern='test*.py')
# runner = unittest.TextTestRunner()
# runner.run(suite)

# 使用HTMLTestRunner
test_report = 'test_report.html'
with open(test_report,'wb') as f:
    runner = HTMLTestRunner(f,title='测试报告',description='当前版本1.0')
    runner.run(suite)
