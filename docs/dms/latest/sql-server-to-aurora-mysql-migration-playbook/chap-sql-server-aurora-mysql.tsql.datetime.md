

# Date and time functions for T-SQL
<a name="chap-sql-server-aurora-mysql.tsql.datetime"></a>

This topic provides reference information about date and time functions in Microsoft SQL Server and Amazon Aurora MySQL, which is valuable for database administrators and developers migrating from SQL Server to Aurora MySQL. You can understand the similarities and differences in how these two database systems handle temporal operations, including system date and time values, time zone considerations, and specific function equivalents.


| Feature compatibility |  AWS SCT / AWS DMS automation level |  AWS SCT action code index | Key differences | 
| --- | --- | --- | --- | 
|  ![Three star feature compatibility](http://docs.aws.amazon.com/dms/latest/sql-server-to-aurora-mysql-migration-playbook/images/pb-compatibility-3.png)  |  ![Four star automation level](http://docs.aws.amazon.com/dms/latest/sql-server-to-aurora-mysql-migration-playbook/images/pb-automation-4.png)  |  [Date and Time Functions](chap-sql-server-aurora-mysql.tools.actioncode.md#chap-sql-server-aurora-mysql.tools.actioncode.datetime)  | Time zone handling. Syntax differences. | 

## SQL Server Usage
<a name="chap-sql-server-aurora-mysql.tsql.datetime.sqlserver"></a>

Date and time functions are scalar functions that perform operations on temporal or numeric input and return temporal or numeric values.

System date and time values are derived from the operating system of the server where SQL Server is running.

**Note**  
This section doesn’t address time zone considerations and time zone aware functions. For more information, see [Data Types](chap-sql-server-aurora-mysql.sql.datatypes.md).

### Syntax and Examples
<a name="chap-sql-server-aurora-mysql.tsql.datetime.sqlserver.examples"></a>

The following table lists the most commonly used date and time functions.


| Function | Purpose | Example | Result | Comments | 
| --- | --- | --- | --- | --- | 
|  `GETDATE` and `GETUTCDATE`  | Return a datetime value that contains the current local or UTC date and time. |  `SELECT GETDATE()`  | 2018-04-05 15:53:01.380 |  | 
|  `DATEPART`, `DAY`, `MONTH`, and `YEAR`  | Return an integer value representing the specified date part of a specified date. |  `SELECT MONTH(GETDATE()), YEAR(GETDATE())`  | 4, 2018 |  | 
|  `DATEDIFF`  | Returns an integer value of date part boundaries that are crossed between two dates. |  `SELECT DATEDIFF(DAY, GETDATE(), EOMONTH(GETDATE()))`  | 25 | How many days are left until the end of the month. | 
|  `DATEADD`  | Returns a datetime value that is calculated with an offset interval to the specified date part of a date. |  `SELECT DATEADD(DAY, 25, GETDATE())`  | 2018-04-30 15:55:52.147 |  | 
|  `CAST` and `CONVERT`  | Converts datetime values to and from string literals and to and from other datetime formats. |  `SELECT CAST(GETDATE() AS DATE)` <br /> `SELECT CONVERT(VARCHAR(20), GETDATE(), 112)`  | 2018-04-05 20180405 | Default date format. Style 112 (ISO) with no separators. | 

For more information, see [Date and Time functions](https://docs.microsoft.com/en-us/sql/t-sql/functions/date-and-time-data-types-and-functions-transact-sql?view=sql-server-ver15#DateandTimeFunctions) in the *SQL Server documentation*.

## MySQL Usage
<a name="chap-sql-server-aurora-mysql.tsql.datetime.mysql"></a>

 Amazon Aurora MySQL-Compatible Edition (Aurora MySQL) provides a very rich set of scalar date and time functions; more than SQL Server.

**Note**  
While some of the functions such as DATEDIFF seem to be similar to those in SQL Server, the functionality can be significantly different. Take extra care when migrating temporal logic to Aurora MySQL paradigms.

### Syntax and Examples
<a name="chap-sql-server-aurora-mysql.tsql.datetime.mysql.examples"></a>


| Function | Purpose | Example | Result | Comments | 
| --- | --- | --- | --- | --- | 
|  `NOW`, `LOCALTIME`, `CURRENT_TIMESTAMP`, and `SYSDATE`  | Returns a datetime value that contains the current local date and time. |  `SELECT NOW()`  | 2018-04-06 18:57:54 |  `SYSDATE` returns the time at which it runs, compared to `NOW`, which returns a constant time when the statement started running. Also, `SET TIMESTAMP` doesn’t affect `SYSDATE`. | 
|  `UTC_TIMESTAMP`  | Returns a datetime value that contains the current UTC date and time. |  `SELECT UTC_TIMESTAMP()`  | 2018-04-07 04:57:54 |  | 
|  `SECOND`, `MINUTE`, `HOUR`, `DAY`, `WEEK`, `MONTH`, and `YEAR`  | Returns an integer value representing the specified date part of a specified date function. |  `SELECT MONTH(NOW()), YEAR(NOW())`  | 4, 2018 |  | 
|  `DATEDIFF`  | Returns an integer value of the difference in days between two dates. |  `SELECT DATEDIFF(NOW(),'2018-05-01')`  | -25 |  `DATEDIFF` in Aurora MySQL is only for calculating difference in days. Use `TIMESTAMPDIFF` instead. | 
|  `TIMESTAMPDIFF`  | Returns an integer value of the difference in date part between two dates. |  `SELECT TIMESTAMPDIFF(DAY, NOW(),'2018-05-01')`  | 24 |  | 
|  `DATE_ADD`, `DATE_SUB`  | Returns a datetime value that is calculated with an offset interval to the specified date part of a date. |  `SELECT DATE_ADD(NOW(),INTERVAL 1 DAY);`  | 2018-04-07 19:35:32 |  | 
|  `CAST` and `CONVERT`  | Converts datetime values to and from string literals and to and from other datetime formats. |  `SELECT CAST(GETDATE() AS DATE)` <br /> `SELECT CONVERT(VARCHAR(20), GETDATE(), 112)`  | 2018-04-05<br />20180405 | Default date format. Style 112 (ISO) with no separators. | 

### Migration Considerations
<a name="chap-sql-server-aurora-mysql.tsql.datetime.mysql.considerations"></a>

The date and time handling paradigm in Aurora MySQL differs from SQL Server.

Be aware of the differences in data types, time zone awareness, and locale handling. For more information, see [Data Types](chap-sql-server-aurora-mysql.sql.datatypes.md).

## Summary
<a name="chap-sql-server-aurora-mysql.tsql.datetime.summary"></a>

The following table identifies similarities, differences, and key migration considerations.


| SQL Server function |  Aurora MySQL function | Comments | 
| --- | --- | --- | 
|  `GETDATE`, `CURRENT_TIMESTAMP`  |  `NOW`, `LOCALTIME`, `CURRENT_TIMESTAMP`, and `SYSDATE`  |  `CURRENT_TIMESTAMP` is the ANSI standard and it is compatible. `SYSDATE` returns the time at which it runs, unlike `NOW` which returns a constant time when the statement started running. Also, SET `TIMESTAMP` doesn’t affect `SYSDATE`. | 
|  `GETUTCDATE`  |  `UTC_TIMESTAMP`  |  | 
|  `DAY`, `MONTH`, and `YEAR`  |  `DAY`, `MONTH`, `YEAR`  | Compatible syntax. | 
|  `DATEPART`  |  `EXTRACT`, or one of: `MICROSECOND`, `SECOND`, `MINUTE`, `HOUR`, `DAY`, `DAYNAME`, `DAYOFWEEK`, `DAYOFYEAR`, `WEEK`, `MONTH`, `MONTHNAME`, `QUARTER`, `YEAR`  |  Aurora MySQL supports `EXTRACT` as a generic `DATEPART` function. For example, `EXTRACT (YEAR FROM NOW())`. It also supports individual functions for each day part. | 
|  `DATEDIFF`  |  `TIMESTAMPDIFF`  |  `DATEDIFF` in Aurora MySQL only calculates differences in days. | 
|  `DATEADD`  |  `DATE_ADD`, `DATE_SUB`, `TIMESTAMPADD`  |  `DATEADD` in Aurora MySQL only adds full days to a datetime value. Aurora MySQL also supports `DATE_SUB` for subtracting date parts from a date time expression. The argument order and syntax is also different and requires a rewrite. | 
|  `CAST` and `CONVERT`  |  `DATE_FORMAT`, `TIME_FORMAT`  | Although Aurora MySQL supports both `CAST` and `CONVERT`, they aren’t used for style conversion as in SQL Server. Use `DATE_FORMAT` and `TIME_FORMAT`. | 

For more information, see [Date and Time Functions](https://dev.mysql.com/doc/refman/5.7/en/date-and-time-functions.html) in the *MySQL documentation*.