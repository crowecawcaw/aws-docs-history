# Monitoring Amazon Aurora log files

Every RDS database engine generates logs that you can access for auditing and troubleshooting. The type of logs depends on your database
engine.

You can access database logs for DB instances using the AWS Management Console, the AWS Command Line Interface (AWS CLI), or the Amazon RDS API. You can't view, watch, or download transaction
logs.

###### Note

In some cases, logs contain hidden data. Therefore, the AWS Management Console might show content in a log file, but
the log file might be empty when you download it.

###### Topics

- [Viewing and listing database log files](USER_LogAccess.Procedural.md "USER_LogAccess.Procedural.md")
- [Downloading a database log file](USER_LogAccess.Procedural.md "USER_LogAccess.Procedural.md")
- [Watching a database log file](USER_LogAccess.Procedural.md "USER_LogAccess.Procedural.md")
- [Publishing database logs to Amazon CloudWatch Logs](USER_LogAccess.Procedural.md "USER_LogAccess.Procedural.md")
- [Reading log file contents using REST](DownloadCompleteDBLogFile.md "DownloadCompleteDBLogFile.md")
- [Aurora MySQL database log files](USER_LogAccess.Concepts.md "USER_LogAccess.Concepts.md")
- [Aurora PostgreSQL database log files](USER_LogAccess.Concepts.md "USER_LogAccess.Concepts.md")
