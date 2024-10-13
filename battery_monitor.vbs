Set WshShell = CreateObject("WScript.Shell")


WshShell.CurrentDirectory = "C:\path\to\your\BatteryMonitor"


WshShell.Run "pythonw battery_monitor.pyw", 0, False


Set WshShell = Nothing
