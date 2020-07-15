How to use this automation scripts.
===================================

This script use Python as the programming language, with BDD framework (Gherkins), use python library called "Behave" and also Selenium.
Then we should have to prepare several things to run this code properly.

--------------------------------------------------------------------------------------------------------------------------------------------
Question: What to test?
Answer: I use Tiket.com desktop website (https://tiket.com/) for this automation test.

Q: What OS that I use?
A: I use Windows 10 Pro for the Operating System.

Q: What Browser that I use?
A: I use Chrome browser Version 83.0.4103.116 (Official Build) (64-bit)

Q: What text editor that I use?
A: I use pycharm community edition for this testing.

Q: Testing Scope / Scenario :
A: I choose the Product Train & Product Flight Scenario for this testing.

Assumption :
a. Assume that we have fair internet connection.
b. We have testing date before 18 July 2020, so there wiil be no date issue on the transaction test.
c. We have a registered email to tiket.com account. Also with verified mobilephone number for OTP code when login.

=======================================================================================================================

PREPARATION STEPS.
==================

1. Install Python. We use python 3.8.3

https://www.python.org/downloads/

2. Install python library / module :

a. Selenium
- Open windows command prompt / CMD. then type this command below and press enter button to install selenium.

pip install selenium

b. Behave
- Still in windows command prompt, type this command below and press enter to install.

pip install behave

c. Install Selenium webdriver / Chromedriver.

https://sites.google.com/a/chromium.org/chromedriver/

- Choose windows installation file, then download it.

- Unzip the file. Find "chromedriver.exe" and add the folder to the Windows PATH.

- You can follow the step to add the file to the windows PATH on this link below :

https://helpdeskgeek.com/windows-10/add-windows-path-environment-variable/


3. Install pycharm community edition. Setting the environtment and select python as the project intepreter. Make sure the libraries that we have installed before (Selenium & Behave) are available on the environtment.

https://www.jetbrains.com/pycharm/


4. Install pycharm plugins called "Gherkins" to read ".feature" extension. 

5. On the pycharm side, please find File > Open > Search the folder that you have download the attached file and unzip called "Feature".

6. Inside Feature directory / folder, you will find one folder named "steps" which contains two python file called "producttrain.py" & "productflight.py", and also the file with extension .feature named "tiketcom.feature" .

7. Open edit productflight.py . Find function / def  called "loginemail", on the line which contains username & password. Change the string value with your registered email & password. Then save it. 

------------------------------------------------------------------------------------------------------------------------------------------------

RUN THE TEST.
=============

A. Open Terminal on the bottom side of the pycharm project. Type this command below and press enter.

behave feature\tiketcom.feature

B. The test should be run properly. 

Note : Make sure you input the OTP code manually when the Scenario reach Login steps.

