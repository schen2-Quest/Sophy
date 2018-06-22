import HTMLTestRunner


def save_file():
    file_path = "pyResult.html"
    print("--------------------------->")
    fp = open(file_path, 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title='PythonWebUiTestReport', description= 'test result as below')
    return runner