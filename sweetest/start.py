from sweetest.autotest import Autotest
import sys


# 项目名称，和测试用例、页面元素表文件名称中的项目名称必须一致
project_name = 'Baidu'

# 单 sheet 页面模式
sheet_name = 'baidu'

# sheet 页面匹配模式，仅支持结尾带*
#sheet_name = 'TestCase*'

# #sheet 页面列表模式
#sheet_name = ['TestCase', 'test']

# 环境配置信息
# Chrome
desired_caps = {'platformName': 'Desktop', 'browserName': 'Chrome'}
server_url = ''


# 执行
test = Autotest(project_name, sheet_name, desired_caps, server_url)

test.plan()

#测试报告详细数据，可以自行处理后写入其他测试报告系统
#print(test.report_data)

# 如果是集成到 CI/CD，可以给出退出码
#sys.exit(test.code)
