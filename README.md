# VAT Selenium


Configuration
----------------

1) Install all requirements:

    ```bash
    pip install -r requirements.txt
    ```

2) Check your Chrome browser version: chrome://version
3) Download Selenium Chromedriver accordingly to your version:  https://chromedriver.chromium.org/downloads
4) Configure Selenium Chromedriver to Windows environment variables: https://www.browserstack.com/guide/run-selenium-tests-using-selenium-chromedriver


How to run tests
----------------
1) ***Run all tests in parallel:***

   ```bash
   pytest --env=dev -v -n auto --dist=loadfile --junitxml=reports/TEST-results.xml
   ```
   ***Note:***
   1) -n auto: pytest-xdist will use as many processes as your computer has CPU cores.
   2) --dist loadfile: Tests are grouped by their containing file. Groups are distributed to available workers as whole units. This guarantees that all tests in a file run in the same worker.
   3) --junitxml=reports/TEST-results.xml - creating xlm reports

2) Run all tests:

   ```bash
   pytest --junitxml=reports/TEST-results.xml -s -v tests
   ```

3) Run tests by "smoke" marker:

   ```bash
   pytest --env=dev --junitxml=reports/TEST-results.xml -s -v -m smoke 
   ```


How to create local HTML report
----------------
1) Create HTML report from junit report:
   ```bash
   python -m junit2htmlreport reports/TEST-results.xml reports/TEST-results.html
   ```
2) Open HTML report in browser:
   ```bash
   reports/TEST-results.html
   ```
