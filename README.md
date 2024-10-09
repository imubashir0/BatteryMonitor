# How to Implement and Run the Battery Monitor Script

## Overview

This guide details how to implement and run a Python-based battery monitor script that:
1.	**Monitors your laptop's battery status** to detect when the charger is connected or disconnected and when the battery is fully charged.
2.	**Displays pop-up notifications** for these events.
3.	**Runs the script manually via Command Prompt**.
4.	**Logs** changes in battery status.

## Step 1: Install Python on Your System

If Python is not already installed on your computer, follow these steps:

1.1 Download Python
  1.	Visit the official Python website.
  2.	Download the latest version of Python.

1.2 Install Python
  1.	Run the Python installer that you downloaded.
  2.	**Important:** On the first installation screen, check the box that says, "**Add Python to PATH**". This is crucial for running Python from the Command Prompt.
  3.	Click "**Install Now**" and wait for the installation to complete.

1.3 Verify Python Installation
  1.	Open Command Prompt:
     
        o	Press **Win** + **R**, type **cmd**, and press Enter.
  2.	Check Python Version:

    python --version
      
  This should return something like Python 3.11.x.
  3.	Check pip Installation:
  
    pip --version      
  This verifies that pip, Python’s package installer, is installed.

## Step 2: Install Required Libraries

To run the battery monitor script, you need two external libraries: **psutil** and **win10toast**.

2.1 Open Command Prompt
 
  •	Press **Win** + **R**, type **cmd**, and press Enter.

2.2 Install the Libraries
  1.	Install psutil for monitoring battery and system power information:

      pip install psutil
  2.	Install win10toast for displaying Windows notifications:

     pip install win10toast

## Step 3: Create the *battery_monitor.pyw* Script and *battery_monitor.log*
3.1 Choose a Directory for Your Script
 
  1.	Open File Explorer:
  
        o Navigate to your **Documents** folder (e.g. *C:\Users\YourUsername\Documents*).
  2.	Create a New Folder:
 
        o Right-click in the **Documents** folder and select New > Folder. Name it **BatteryMonitor**.
  3.	**Create a text file called battery_monitor.log**. 
  
        o	Remember to include the **.log** extension or the script will not work.
  4.	Save the **battery_monitor.pyw** file here.

## Step 4: Run the Script Manually in Command Prompt

Now that you've created the script, you can run it from Command Prompt.

4.1 Open Command Prompt
  
  1.	Press **Win** + **R**, type **cmd**, and press Enter.

4.2 Navigate to the Script Directory
  
  1.	In the Command Prompt window, use the cd command to navigate to the folder where you saved the script:

    	     cd C:\Users\YourUsername\Documents\BatteryMonitor

4.3 Run the Script
  
  1.	Once you’re in the correct directory, run the script with:

    pythonw battery_monitor.pyw
4.4 Verify Notifications
  
  1.	**Charger Connection:**

    	  o	Plug in and unplug your laptop’s charger to test notifications.

    	  o	You should see pop-up notifications indicating whether the charger is connected or disconnected.
  
  3.	**Battery Full:**

    	  o	Once the battery reaches 100%, a notification should appear indicating that the battery is fully charged.
 
  5.	**Low Battery:**

    	  o	If the battery level drops below 20%, you should receive a low battery notification.

4.5 Check Log File

The script logs events in a file called **battery_monitor.log**. To verify that the script is running as expected:
  1.	Navigate to *C:\Users\YourUsername\Documents\BatteryMonitor*.
  2.	Open the **battery_monitor.log** file using a text editor (e.g., Notepad).
  3.	Check the log for messages indicating that the script started and notifications were sent.

## Step 5: Troubleshooting

If the script doesn’t behave as expected, here are some common issues and how to resolve them:
  1.	No Notifications:
        o	Ensure that Windows Focus Assist is turned off or                   configured to allow notifications.
        o	Check the log file (battery_monitor.log) for any errors.
  2.	Script Not Running:
        o	Double-check the path you used to run the script. Make              sure pythonw is installed and you are pointing to the               correct Python executable.
        o	Run the script with python (instead of pythonw) to see              any errors printed in the Command Prompt.
  3.	Log File Not Being Created:
        o	Ensure that the script has permission to write to the               Documents\BatteryMonitor folder.

## Conclusion

By following this guide, you have implemented the battery_monitor.pyw program, which monitors your laptop's battery status and provides notifications when the charger is connected, disconnected, or when the battery is full. You have also learned how to run the script manually through **Command Prompt**.
For regular use, you can run the script whenever you need to monitor your battery status.


