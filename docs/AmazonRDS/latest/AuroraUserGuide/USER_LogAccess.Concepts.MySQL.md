# AuroraMySQL database log files

You can monitor the Aurora MySQL logs directly through the Amazon RDS console, Amazon RDS
API, AWS CLI, or AWS SDKs. You can also access MySQL logs by directing the logs to a database table in the main
database and querying that table. You can use the mysqlbinlog utility to download a binary log.

For more information about viewing, downloading, and watching file-based database logs,
see [Monitoring Amazon Aurora log files](USER_LogAccess.md "USER_LogAccess.md").

###### Topics

- [Overview of Aurora MySQL database logs](USER_LogAccess.MySQL.LogFileSize.md "USER_LogAccess.MySQL.LogFileSize.md")
- [Sending AuroraMySQL log output to tables](Appendix.MySQL.CommonDBATasks.Logs.md "Appendix.MySQL.CommonDBATasks.Logs.md")
- [Configuring Aurora MySQL binary logging for Single-AZ databases](USER_LogAccess.MySQL.BinaryFormat.md "USER_LogAccess.MySQL.BinaryFormat.md")
- [Accessing MySQL binary logs](USER_LogAccess.MySQL.Binarylog.md "USER_LogAccess.MySQL.Binarylog.md")
