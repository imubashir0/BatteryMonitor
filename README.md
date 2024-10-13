# How to Implement and Automate the Battery Monitor

## Overview

This guide details how to implement Battery Monitor, a program that:
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

## Step 3: Create the *battery_monitor.log* file
3.1 Choose a Directory for Your Script
 
  1.	Open File Explorer:
  
        o Navigate to your **Documents** folder (e.g. *C:\Users\YourUsername\Documents*).
  2.	Create a New Folder:
 
        o Right-click in the **Documents** folder and select New > Folder. Name it **BatteryMonitor**.
  3.	**Create a text file called battery_monitor.log**. 
  
        o	Remember to include the **.log** extension or the script will not work.
  4.	Save the **battery_monitor.pyw** and **battery_monitor.vbs** files here if you wish.

## Step 4: Edit the battery_monitor.vbs File

Right-click on the **battery_monitor.vbs** file.

Select *Edit* from the context menu. This will open the file in Notepad.

Find the following line in the script:

**WshShell.CurrentDirectory = "C:\path\to\your\BatteryMonitor"**

Replace **"C:\path\to\your\BatteryMonitor"** with the actual path where your Battery Monitor (**battery_monitor.pyw**) is located.

Save the File:

## Step 5: Test the battery_monitor.vbs File

Double-click the **battery_monitor.vbs** file to run it.

Confirm that the Battery Monitor starts by connecting your charger. A toaster notification should pop up on the bottom right of your screen.

If the Battery Monitor doesn't start, double-check that the file path you entered in Step 1 is correct.

## Step 6: Move/Copy the VBS File to the Startup Folder

To ensure that the Battery Monitor runs automatically every time you log in to your PC, you need to place the **battery_monitor.vbs** file in the Startup folder.

To open the Startup Folder, press **Win** + **R**, type **shell:startup**, and press Enter.

This will open the Startup folder, where you can place programs or scripts that you want to run automatically at login.

Move/Copy the **battery_monitor.vbs** file here

## Step 7: Verify Automatic Startup

Restart Your Computer.

After logging in, the Battery Monitor should start without any manual intervention and without showing a Command Prompt window.

## Step 8: Verify Notifications
  
  1.	**Charger Connection:**

    	  o	Plug in and unplug your laptop’s charger to test notifications.

    	  o	You should see pop-up notifications indicating whether the charger is connected or disconnected.
  
  3.	**Battery Full:**

    	  o	Once the battery reaches 100%, a notification should appear indicating that the battery is fully charged.
 
  5.	**Low Battery:**

    	  o	If the battery level drops below 20%, you should receive a low battery notification.

## Step 9: Check Log File

The script logs events in the **battery_monitor.log** file. To verify that the script is running as expected.

Navigate to it and open it using a text editor (e.g., Notepad).

Check the log for messages indicating that the script started and notifications were sent.

## Step 10: Troubleshooting

If the script doesn’t behave as expected, here are some common issues and how to resolve them:

  1.	No Notifications:

    	  o	Ensure that Windows Focus Assist is turned off or configured to allow notifications.
    	
        o	Check the log file (**battery_monitor.log**) for any errors.
    	
  2.	Script Not Running:
     
        o	Double-check the path you used to run the script. Make sure pythonw is installed and you are pointing to the correct Python executable.
    	
        o	Run the script with python (instead of pythonw) by editing the **battery_monitor.vbs** file to see any errors printed in the Command Prompt.
    	
  4.	Log File Not Being Created:
     
        o	Ensure that the script has permission to write to the Documents\BatteryMonitor folder.


