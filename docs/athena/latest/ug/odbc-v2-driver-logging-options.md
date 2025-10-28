# Logging options

Administrator rights are required to modify the settings described here. To make the
changes, you can use the ODBC Data Source Administrator **Logging Options**
dialog box or modify the Windows registry directly.

## Log level

This option enables ODBC driver logs. In Windows, you can use the registry or a dialog
box to enable or disable logging. The option is located in the following registry
path:

```
Computer\HKEY_LOCAL_MACHINE\SOFTWARE\Amazon Athena\ODBC\Driver
```

| **Connection string name** | **Parameter type** | **Default value** | **Connection string example**                           |
| -------------------------- | ------------------ | ----------------- | ------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| LogLevel                   | Optional           | `0`               | `LogLevel=1;`                                           | ## Log path Specifies path to the file where the ODBC driver logs are stored. You can use the registry or a dialog box to set this value. The option is located in the following registry path: `Computer\HKEY_LOCAL_MACHINE\SOFTWARE\Amazon Athena\ODBC\Driver` |
| **Connection string name** | **Parameter type** | **Default value** | **Connection string example**                           |
| ---                        | ---                | ---               | ---                                                     |
| LogPath                    | Optional           | `none`            | `LogPath=C:\Users\`username`\projects\internal\trunk\;` | ## Use AWS Logger Specifies if AWS SDK logging is enabled. Specify 1 to enable, 0 to disable.                                                                                                                                                                    |
| **Connection string name** | **Parameter type** | **Default value** | **Connection string example**                           |
| ---                        | ---                | ---               | ---                                                     |
| UseAwsLogger               | Optional           | `0`               | `UseAwsLogger=1;`                                       |
