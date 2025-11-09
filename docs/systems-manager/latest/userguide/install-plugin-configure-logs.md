AWS Systems Manager Change Manager is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see
[AWS Systems Manager Change Manager availability change](change-manager-availability-change.md "change-manager-availability-change.md").

# (Optional) Turn on Session Manager plugin

logging

The Session Manager plugin includes an option to allow logging for sessions that you run. By
default, logging is turned off.

If you allow logging, the Session Manager plugin creates log files for both application
activity (`session-manager-plugin.log`) and errors
(`errors.log`) on your local machine.

###### Topics

- [Turn on logging for the Session Manager plugin
  (Windows)](#configure-logs-windows "#configure-logs-windows")
- [Enable logging for the Session Manager plugin
  (Linux and macOS)](#configure-logs-linux "#configure-logs-linux")

## Turn on logging for the Session Manager plugin

(Windows)

1. Locate the `seelog.xml.template` file for the
   plugin.

The default location is
`C:\Program Files\Amazon\SessionManagerPlugin\seelog.xml.template`. 2. Change the name of the file to
`seelog.xml`. 3. Open the file and change `minlevel="off"` to
`minlevel="info"` or
`minlevel="debug"`.

###### Note

By default, log entries about opening a data channel and
reconnecting sessions are recorded at the
**INFO** level. Data flow (packets and
acknowledgement) entries are recorded at the
**DEBUG** level. 4. Change other configuration options you want to modify. Options you
can change include:

    * **Debug level**: You can
     change the debug level from `formatid="fmtinfo"`
     to `formatid="fmtdebug"`.
    * **Log file options**: You can
     make changes to the log file options, including where the
     logs are stored, with the exception of the log file names.


    ###### Important

    Don't change the file names or logging won't work
     correctly.



    ```
    <rollingfile type="size" filename="C:\Program Files\Amazon\SessionManagerPlugin\Logs\session-manager-plugin.log" maxsize="30000000" maxrolls="5"/>
    <filter levels="error,critical" formatid="fmterror">
    <rollingfile type="size" filename="C:\Program Files\Amazon\SessionManagerPlugin\Logs\errors.log" maxsize="10000000" maxrolls="5"/>
    ```

5. Save the file.

## Enable logging for the Session Manager plugin

(Linux and macOS)

1. Locate the `seelog.xml.template` file for the
   plugin.

The default location is
`/usr/local/sessionmanagerplugin/seelog.xml.template`. 2. Change the name of the file to
`seelog.xml`. 3. Open the file and change `minlevel="off"` to
`minlevel="info"` or
`minlevel="debug"`.

###### Note

By default, log entries about opening data channels and
reconnecting sessions are recorded at the
**INFO** level. Data flow (packets and
acknowledgement) entries are recorded at the
**DEBUG** level. 4. Change other configuration options you want to modify. Options you
can change include:

    * **Debug level**: You can
     change the debug level from `formatid="fmtinfo"`
     to `outputs formatid="fmtdebug"`
    * **Log file options**: You can
     make changes to the log file options, including where the
     logs are stored, with the exception of the log file names.


    ###### Important

    Don't change the file names or logging won't work
     correctly.



    ```
    <rollingfile type="size" filename="/usr/local/sessionmanagerplugin/logs/session-manager-plugin.log" maxsize="30000000" maxrolls="5"/>
    <filter levels="error,critical" formatid="fmterror">
    <rollingfile type="size" filename="/usr/local/sessionmanagerplugin/logs/errors.log" maxsize="10000000" maxrolls="5"/>
    ```

    ###### Important

    If you use the specified default directory for storing
     logs, you must either run session commands using
     **sudo** or give the directory where
     the plugin is installed full read and write permissions.
     To bypass these restrictions, change the location where
     logs are stored.

5. Save the file.
