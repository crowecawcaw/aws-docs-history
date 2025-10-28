# Enable updates for license included applications on image builder with

Powershell

To enable updates for license included applications on image builder with
Powershell, follow these steps.

- Run the following command with PowerShell as an administrator:

`Set-ItemProperty -Path
 "HKLM:\SOFTWARE\Microsoft\Office\ClickToRun\Configuration" -Name UpdatesEnabled
 -Value True`
