# python-pytest
Python pytest repository

# 1. Install python

  
  1. For Window User please go to reference link
  2. For Linux - Ubuntu 18.04 + : python3.6 comes  installed by default (factory default)
  3. For MacOS -  Open terminal and hit command brew install python3
  
  Reference - https://realpython.com/installing-python/


# 2. Install pip

 
  For Window User - Please check “Install Pip” option while installing python
  For Linux / MacOS User - Open command line and hit following command
    `sudo apt install python3-pip`


# 3. Create Virtual Environment and Install Dependencies

  Step 3 is optional if you are not using a virtual environment
  
  1. Install Virtual Environment  -   `pip3 install virtualenv`
  2. Create Virtual Environment - `virtualenv -p /usr/bin/python3.6 <path_of_venv>`
     Syntax - `virtualenv -p <python_path> <path_of_venv>`
  3. Activate Virtual Environment - `source <path_of_venv>/bin/activate`
  4. Run Command - `pip install -r <project_dir>/requirements.txt`
  
# 4. Run automation from command line

  1. Run on "regression" test cases on chrome browser
  `pytest -m regression --browser=chrome test_suites/ --html=report.html`
  
  2. Run on "sanity" test cases on headless chrome browser
  `pytest -m sanity --browser=headlesschrome test_suites/ --html=report.html`
  
  3. Run on "sanity" test cases on firefox browser with different sut url
  `pytest -m sanity --browser=firefox test_suites/ --sut "https://www.testurl.com --html=report.html`
  
  4. Run on "regression" test cases on headless firefox browser with different sut url
  `pytest -m sanity --browser=headlessfirefox test_suites/ --sut "https://www.testurl.com --html=report.html`


