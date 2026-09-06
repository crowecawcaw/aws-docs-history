

# Logging options
<a name="odbc-v2-driver-logging-options"></a>

**Warning**  
**Security:** When logging is enabled at verbose levels (DEBUG or TRACE), the AWS SDK used by the driver may log sensitive information such as authentication tokens and credentials in plaintext. Use verbose logging only for troubleshooting, and ensure log files are stored securely and deleted after use. Do not enable verbose logging in production environments.

Administrator rights are required to modify the settings described here. To make the changes, you can use the ODBC Data Source Administrator **Logging Options** dialog box or modify the Windows registry directly.

## Log level
<a name="odbc-v2-driver-logging-options-log-level"></a>

This option enables ODBC driver logs with different levels of detail. In Windows, you can use the registry or a dialog box to configure logging. The option is located in the following registry path:

```
Computer\HKEY_LOCAL_MACHINE\SOFTWARE\Amazon Athena\ODBC\Driver
```

The following log levels are available:
+ `OFF` - Logging is disabled
+ `ERROR` - Only error messages are logged
+ `WARN` - Warning messages and errors are logged
+ `INFO` - Informational messages, warnings, and errors are logged
+ `DEBUG` - Detailed debug information plus all lower level messages are logged
+ `TRACE` - Most detailed level of logging, includes all messages

**Note**  
Each log level includes all messages from the levels below it. Higher log levels may impact performance and generate larger log files.



| **Connection string name** | **Parameter type** | **Default value** | **Connection string example** | 
| --- | --- | --- | --- | 
| LogLevel | Optional | OFF | LogLevel=INFO; | 

## Log path
<a name="odbc-v2-driver-logging-options-log-path"></a>

Specifies path to the file where the ODBC driver logs are stored. You can use the registry or a dialog box to set this value. The option is located in the following registry path:

```
Computer\HKEY_LOCAL_MACHINE\SOFTWARE\Amazon Athena\ODBC\Driver
```



| **Connection string name** | **Parameter type** | **Default value** | **Connection string example** | 
| --- | --- | --- | --- | 
| LogPath | Optional | none | LogPath=C:\\Users\\{{username}}\\projects\\internal\\trunk\\; | 

## Use AWS Logger
<a name="odbc-v2-driver-logging-options-use-aws-logger"></a>

Specifies if AWS SDK logging is enabled. Specify 1 to enable, 0 to disable.



| **Connection string name** | **Parameter type** | **Default value** | **Connection string example** | 
| --- | --- | --- | --- | 
| UseAwsLogger | Optional | 0 | UseAwsLogger=0; | 

**Note**  
Logs may log sensitive information when `UseAwsLogger` is enabled and `LogLevel` is set to `DEBUG` or `TRACE`. `UseAwsLogger` is recommended only for troubleshooting purposes.