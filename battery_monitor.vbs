Set WshShell = CreateObject("WScript.Shell")


WshShell.CurrentDirectory = "C:\imubashir0\Battery_Monitor"


WshShell.Run "pythonw battery_monitor.pyw", 0, False


Set WshShell = Nothing