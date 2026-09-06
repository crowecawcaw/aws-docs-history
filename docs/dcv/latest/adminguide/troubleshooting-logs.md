

# Using the Log Files
<a name="troubleshooting-logs"></a>

The Amazon DCV log files can be used to identify and troubleshoot problems with your Amazon DCV server. The Amazon DCV log files can be found in the following location on your Amazon DCV server:
+ Windows server

  ```
  C:\ProgramData\NICE\dcv\log\
  ```
**Note**  
The `ProgramData` folder might be hidden by default. If you do not see the `ProgramData` folder, set your file browser to show hidden items. Alternatively, enter `%programdata%` in the address bar and press **Enter**.
+ Linux and macOS server

  ```
  /var/log/dcv/
  ```

Multiple files with a similar name may be present. The numeric suffix identifies the age of a file. The numbers get higher as the file gets older. 

As you troubleshoot connection issues, the `server.log` file is the most relevant. When submitting a support request, attaching the whole folder is preferred, but older files can be excluded to limit the attachment size.

The Amazon DCV server enables you to configure the verbosity level of the log files. The following verbosity levels are available:
+ `error` — Provides the least detail. Includes errors only.
+ `warn` — Includes errors and warnings.
+ `info` — The default verbosity level. Includes errors, warnings, and information messages.
+ `debug` — Provides the most detail. Provides detailed information that is useful for debugging issues.

**Topics**
+ [Changing Log File Verbosity](#change-verbosity)

## Changing Log File Verbosity
<a name="change-verbosity"></a>

Changing verbosity enables you to adjust the level of detail in your logs, helping you diagnose and resolve issues more effectively. Increasing log verbosity captures more granular information about system. Decreasing log verbosity optimizes storage and enhances performance.

### For Windows
<a name="change-verbosity-windows"></a>

For Amazon DCV versions after the 2023.0 release, it is preferred to configure the log file verbosity via the command line. For older versions, you must configure the `level` parameter using the Windows Registry Editor.

**Release 2023.0 and newer**

1. Open a Command Prompt and Run as administrator.

1. Go to the installation directory:

   ```
   C:\Program Files\NICE\DCV\Server\bin
   ```

1. Enter the following command to set the level:

   ```
   dcv set-config --section log --key level "'LEVEL'"
   ```

1. Enter the following command to enable debugging:

   ```
   dcv set-config --section log --key level "'debug'"
   ```

**Note**  
Make sure you are using both double and single quotation marks.

**Release 2022.2 and older**

1. Open the Windows Registry Editor.

1. Navigate to the **HKEY\_USERS\\S-1-5-18\\Software\\GSettings\\com\\nicesoftware\\dcv\\log\\** key.

1. Open the **level** parameter by double-clicking. For **Value data**, type either `error`, `warn`, `info`, or `debug`, depending on the required verbosity level.

1. Choose **OK** and close the Windows Registry Editor.

### For Linux
<a name="change-verbosity-linux"></a>

For Amazon DCV versions after the 2023.0 release, it is preferred to configure the log file verbosity via the command line. For older versions, you must configure the `level` parameter in the `dcv.conf` file.

**Release 2023.0 and newer**

1. Open a terminal.

1. Enter the following command to set the level:

   ```
   sudo dcv set-config --section log --key level "'LEVEL'"
   ```

1. Enter the following command to enable debugging:

   ```
   sudo dcv set-config --section log --key level "'debug'"
   ```

**Note**  
Make sure you are using both double and single quotation marks.

**Release 2022.2 and older**

1. Navigate to `/etc/dcv/` and open the `dcv.conf` with your preferred text editor.

1. Locate the `level` parameter in the `[log]` section, and replace the existing verbosity level with either `error`, `warn`, `info`, or `debug`.

   ```
   [log]
   level="{{verbosity_level}}"
   ```

1. Save and close the file.

### For macOS
<a name="change-verbosity-macos"></a>

1. Open a terminal.

1. Enter the following command to set the level:

   ```
   sudo dcv set-config --section log --key level "'LEVEL'"
   ```

1. Enter the following command to enable debugging:

   ```
   sudo dcv set-config --section log --key level "'debug'"
   ```

**Note**  
Make sure you are using both double and single quotation marks.