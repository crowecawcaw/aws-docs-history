# Using the Log Files

Use the Amazon DCV client log files to identify and troubleshoot problems with your Amazon DCV client.
Logs are enabled by default on Windows (since 2024.0), Linux and macOS clients. When
using older Windows clients a log file must be provided (see [Enabling debug in log files](#debugging-log-files "#debugging-log-files")).

- Windows client

```
%localappdata%\Amazon\DCV\logs\client.log
```

- Linux or macOS client

```
~/.local/share/NICE/dcvviewer/log/viewer.log
```

## Enabling debug in log files

In order to troubleshoot issues, the Amazon DCV debug logs must be explicitly enabled.

###### For Windows clients

1. Navigate to the folder where the `dcvviewer.exe` file is located. By default, this is `C:\Program Files (x86)\NICE\DCV\Client\bin\`.
2. Do one of the following:
   - Open a command prompt and enter the following:

   ```
   dcvviewer --log-level debug --log-file-name C:/ProgramData/client.log
   ```

   - Add the following configuration to the connection file and double click on it to connect:

   ```
   [debug]
   logfilename=C:/ProgramData/client.log
   loglevel=debug
   ```

###### Note

To enable logging on Windows without changing the default log level, set the value to `info` instead of `debug`.
Logs are stored in the specified local file on your machine.

###### For macOS clients

1. Open a terminal.
2. Navigate to the folder where the `dcvviewer` file is located. Usually it is located here: `/Applications/DCV\ Viewer.app/Contents/MacOS/dcvviewer`.
3. Enter the following to launch the Amazon DCV client:

```
dcvviewer --log-level debug
```

When the client launches, the log files appear in the terminal.

###### For Linux clients

1. Open a terminal.
2. Enter the following to launch the Amazon DCV client:

```
dcvviewer --log-level debug
```

When the client launches, the log files appear in the terminal.
