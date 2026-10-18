

# Using the Log Files
<a name="troubleshooting-logs"></a>

Use the Amazon DCV client log files to identify and troubleshoot problems with your Amazon DCV client. Logs are enabled by default on Windows (since 2024.0), Linux and macOS clients. When using older Windows clients a log file must be provided (see [Enabling debug in log files](#debugging-log-files)).

The log file location depends on the client used.

------
#### [ Windows ]

Log files are located at:

```
%localappdata%\Amazon\DCV\logs\client.log
```

------
#### [ macOS ]

Log files are located at:

```
~/Library/Logs/com.nicesoftware.dcvviewer/viewer.log
```

**Tip**  
You can also view macOS client logs in real time using Console.app or the `log` command-line tool:  

```
$ log stream --process dcvviewer
```
To query past logs:  

```
$ log show --process dcvviewer --last 1h
```

------
#### [ Linux ]

Log files are located at:

```
~/.local/share/NICE/dcvviewer/log/viewer.log
```

------

## Enabling debug in log files
<a name="debugging-log-files"></a>

In order to troubleshoot issues, the Amazon DCV debug logs must be explicitly enabled. The steps depend on the client used.

------
#### [ Windows ]

1. Navigate to the folder where the `dcvviewer.exe` file is located. By default, this is `C:\Program Files (x86)\NICE\DCV\Client\bin\`.

1. Do one of the following:
   + Open a command prompt and enter the following:

     ```
     dcvviewer --log-level debug --log-file-name C:/ProgramData/client.log
     ```
   + Add the following configuration to the connection file and double click on it to connect:

     ```
     [debug]
     logfilename=C:/ProgramData/client.log
     loglevel=debug
     ```

**Note**  
To enable logging on Windows without changing the default log level, set the value to `info` instead of `debug`. Logs are stored in the specified local file on your machine.

------
#### [ macOS ]

Do one of the following:
+ Open a terminal, navigate to the folder where the `dcvviewer` file is located (by default, `"/Applications/DCV Viewer.app/Contents/MacOS/"`), and enter the following:

  ```
  dcvviewer --log-level debug
  ```

  When the client launches, the log files appear in the terminal.
+ Add the following configuration to the connection file and double click on it to connect:

  ```
  [debug]
  loglevel=debug
  ```

------
#### [ Linux ]

1. Open a terminal.

1. Enter the following to launch the Amazon DCV client:

   ```
   dcvviewer --log-level debug
   ```

When the client launches, the log files appear in the terminal.

------