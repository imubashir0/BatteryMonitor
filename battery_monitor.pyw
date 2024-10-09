import time
import psutil
import sys
import threading
import logging
from win10toast import ToastNotifier
import os

# Configure logging
logging.basicConfig(
    filename=os.path.join(os.path.expanduser("~"), "Documents", "BatteryMonitor", "battery_monitor.log"),
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

# Initialize the notifier once
toaster = ToastNotifier()

def send_notification(title, message):
    try:
        toaster.show_toast(title, message, duration=5, threaded=True)
        logging.info(f"Notification sent: {title} - {message}")
    except Exception as e:
        logging.error(f"Failed to send notification: {e}")

def is_another_instance_running():
    current_pid = os.getpid()
    for proc in psutil.process_iter(['pid', 'name']):
        if proc.info['name'] == 'pythonw.exe' and proc.info['pid'] != current_pid:
            return True
    return False

def check_battery_status():
    if is_another_instance_running():
        send_notification("Battery Monitor", "Another instance is already running.")
        logging.info("Another instance detected. Exiting.")
        sys.exit()

    try:
        battery = psutil.sensors_battery()
        if battery is None:
            send_notification("Battery Monitor", "Cannot access battery information.")
            logging.error("Cannot access battery information.")
            return  # Exit if battery information is unavailable

        charger_connected = battery.power_plugged
        battery_percent = battery.percent
        battery_full = battery_percent >= 100 and charger_connected

        # Initialize previous states if None
        if check_battery_status.charger_connected_prev is None:
            check_battery_status.charger_connected_prev = charger_connected
            logging.info(f"Initial charger status: {'Connected' if charger_connected else 'Disconnected'}")

        if check_battery_status.battery_full_prev is None:
            check_battery_status.battery_full_prev = battery_full
            if battery_full:
                logging.info("Battery is initially full.")

        # Notify if battery is below 20%
        if battery_percent <= 20 and not getattr(check_battery_status, 'low_battery_notified_prev', False):
            send_notification("Low Battery", f"Battery level is at {battery_percent}%. Please charge soon.")
            check_battery_status.low_battery_notified_prev = True
        elif battery_percent > 20:
            check_battery_status.low_battery_notified_prev = False

        # Check charger connection status
        if charger_connected and not check_battery_status.charger_connected_prev:
            send_notification("Charger Connected", "Your laptop is now charging.")
        elif not charger_connected and check_battery_status.charger_connected_prev:
            send_notification("Charger Disconnected", "Your laptop is running on battery.")

        # Check if battery is full
        if battery_full and not check_battery_status.battery_full_prev:
            send_notification("Battery Full", "Your battery is fully charged.")

        # Update previous states
        check_battery_status.charger_connected_prev = charger_connected
        check_battery_status.battery_full_prev = battery_full

    except Exception as e:
        send_notification("Battery Monitor Error", str(e))
        logging.error(f"Exception in check_battery_status: {e}")

    # Schedule the next check
    threading.Timer(3, check_battery_status).start()

# Initialize previous states
check_battery_status.charger_connected_prev = None
check_battery_status.battery_full_prev = None
check_battery_status.low_battery_notified_prev = False

def main():
    logging.info("Battery Monitor started.")
    # Start the first check
    check_battery_status()

    # Keep the script running
    while True:
        time.sleep(1)

if __name__ == "__main__":
    main()
