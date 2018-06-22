from test_case.htmlreport import save_file
from test_case.loginsuite import all_suite

if __name__ == '__main__':
    runner = save_file()
    all_suite = all_suite()
    runner.run(all_suite)