

# Using Windows PowerShell Files
<a name="using-powershell-files-with-session-scripts"></a>

To use Windows PowerShell files, specify the full path to the PowerShell file in the **filename** parameter:

```
"filename": 
"C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe",
```

Then specify your session script in the **arguments** parameter:

```
"arguments": "-File \"C:\\path\\to\\session\\script.ps1\"",
```

Finally, verify that the PowerShell Execution Policy allows your PowerShell file to run.