## Environment Setup
- Python 3.12
- Setup Chrome browser (Download link - "https://www.google.com/chrome")
- Setup Firefox browser (Download link - "https://www.mozilla.org/en-US/firefox/new/")


## Usage
1. `pip3 install -r requirements.txt`:  Install all dependencies. (Link - https://www.jetbrains.com/help/pycharm/managing-dependencies.html#configure-requirements)
2. Set `browser = chrome` for run test in chrome driver or `browser = firefox` for run test in firefox browser.
3. `pytest -s -v -n 2 --reruns 1 --reruns-delay 5 --html=reports/validation_report.html --self-contained-html` Run all tests with report
4. `nowina\reports` folder with generated report.
5. `nowina\screenshots` folder with screenshots which appeared during test fail.

