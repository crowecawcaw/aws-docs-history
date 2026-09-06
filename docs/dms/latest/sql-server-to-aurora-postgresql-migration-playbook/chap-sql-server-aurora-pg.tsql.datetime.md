

# Date and time functions for T-SQL
<a name="chap-sql-server-aurora-pg.tsql.datetime"></a>

This topic provides reference information about date and time functions in PostgreSQL compared to Microsoft SQL Server, which is valuable for database administrators and developers migrating from SQL Server to Amazon Aurora PostgreSQL. You can understand the differences in function names, syntax, and behavior between the two database systems when working with temporal data. The topic highlights key date and time functions, their equivalents across platforms, and offers guidance on handling potential compatibility issues.


| Feature compatibility |  AWS SCT / AWS DMS automation level |  AWS SCT action code index | Key differences | 
| --- | --- | --- | --- | 
|  ![Four star feature compatibility](http://docs.aws.amazon.com/dms/latest/sql-server-to-aurora-postgresql-migration-playbook/images/pb-compatibility-4.png)  |  ![Four star automation level](http://docs.aws.amazon.com/dms/latest/sql-server-to-aurora-postgresql-migration-playbook/images/pb-automation-4.png)  |  [Data Types](chap-sql-server-aurora-pg.tools.actioncode.md#chap-sql-server-aurora-pg.tools.actioncode.types)  | PostgreSQL is using different function names. | 

## SQL Server Usage
<a name="chap-sql-server-aurora-pg.tsql.datetime.sqlserver"></a>

Date and Time Functions are scalar functions that perform operations on temporal or numeric input and return temporal or numeric values.

System date and time values are derived from the operating system of the server on which SQL Server is running.

This section doesn’t address time zone considerations and time zone aware functions. For more information about time zone handling, see [Data Types](chap-sql-server-aurora-pg.sql.datatypes.md).

### Syntax and Examples
<a name="chap-sql-server-aurora-pg.tsql.datetime.sqlserver.examples"></a>

The following table includes the most commonly used date and time functions.


| Function | Purpose | Example | Result | Comments | 
| --- | --- | --- | --- | --- | 
|  `GETDATE` and `GETUTCDATE`  | Return a datetime value that contains the current local or UTC date and time. |  `SELECT GETDATE()`  | 2018-04-05 15:53:01.380 |  | 
|  `DATEPART`, `DAY`, `MONTH`, and `YEAR`  | Return an integer value representing the specified `DATEPART` of a specified date. |  `SELECT MONTH(GETDATE()), YEAR(GETDATE())`  | 4, 2018 |  | 
|  `DATEDIFF`  | Returns an integer value of `DATEPART` boundaries that are crossed between two dates. |  `SELECT DATEDIFF(DAY, GETDATE(), EOMONTH(GETDATE()))`  | 25 | How many days left until end of the month. | 
|  `DATEADD`  | Returns a datetime value that is calculated with an offset interval to the specified `DATEPART` of a date. |  `SELECT DATEADD(DAY, 25, GETDATE())`  | 2018-04-30 15:55:52.147 |  | 
|  `CAST` and `CONVERT`  | Converts datetime values to and from string literals and to and from other datetime formats. |  `SELECT CAST (GETDATE() AS DATE)` `SELECT CONVERT (VARCHAR(20), GETDATE(), 112)`  | 2018-04-05 20180405 | Default date format. Style 112 (ISO) with no separtors. | 

For more information, see [Date and Time functions](https://docs.microsoft.com/en-us/sql/t-sql/functions/date-and-time-data-types-and-functions-transact-sql?view=sql-server-ver15#DateandTimeFunctions) in the *SQL Server documentation*.

## PostgreSQL Usage
<a name="chap-sql-server-aurora-pg.tsql.datetime.pg"></a>

 Amazon Aurora PostgreSQL-Compatible Edition (Aurora PostgreSQL) provides a very rich set of scalar date and time functions; more than SQL Server.

While some of the functions appear to be similar to those in SQL Server, the functionality is significantly different. Take extra care when migrating temporal logic to Aurora PostgreSQL paradigms.

### Functions and Definition
<a name="chap-sql-server-aurora-pg.tsql.datetime.pg.functions"></a>


| PostgreSQL function | Function definition | 
| --- | --- | 
|  `AGE`  | Subtract from `current_date`. | 
|  `CLOCK_TIMESTAMP`  | Current date and time. | 
|  `CURRENT_DATE`  | Current date. | 
|  `CURRENT_TIME`  | Current time of day. | 
|  `CURRENT_TIMESTAMP`  | Current date and time (start of current transaction). | 
|  `DATE_PART`  | Get subfield (equivalent to extract). | 
|  `DATE_TRUNC`  | Truncate to specified precision. | 
|  `EXTRACT`  | Get subfield. | 
|  `ISFINITE`  | Test for finite interval. | 
|  `JUSTIFY_DAYS`  | Adjust interval so 30-day time periods are represented as months. | 
|  `JUSTIFY_HOURS`  | Adjust interval so 24-hour time periods are represented as days. | 
|  `JUSTIFY_INTERVAL`  | Adjust interval using `justify_days` and `justify_hours`, with additional sign adjustments. | 
|  `LOCALTIME`  | Current time of day. | 
|  `MAKE_DATE`  | Create date from year, month and day fields. | 
|  `MAKE_INTERVAL`  | Create interval from years, months, weeks, days, hours, minutes and seconds fields. | 
|  `MAKE_TIME`  | Create time from hour, minute and seconds fields. | 
|  `MAKE_TIMESTAMP`  | Create timestamp from year, month, day, hour, minute, and seconds fields. | 
|  `MAKE_TIMESTAMPTZ`  | Create timestamp with time zone from year, month, day, hour, minute, and seconds fields. If the time zone isn’t specified, the current time zone is used. | 
| NOW | Current date and time. | 
|  `STATEMENT_TIMESTAMP`  | Current date and time. | 
|  `TIMEOFDAY`  | Current date and time (like clock\_timestamp, but as a text string). | 
|  `TRANSACTION_TIMESTAMP`  | Current date and time. | 
|  `TO_TIMESTAMP`  | Convert Unix epoch (seconds since 1970-01-01 00:00:00\+00) to timestamp. | 

## Summary
<a name="chap-sql-server-aurora-pg.tsql.datetime.summary"></a>


| SQL Server function |  Aurora PostgreSQL function | 
| --- | --- | 
|  `GETDATE`, `CURRENT_TIMESTAMP`  |  `NOW`, `CURRENT_DATE`, `CURRENT_TIME`, `CURRENT_TIMESTAMP`  | 
|  `GETUTCDATE`  |  `current_timestamp at time zone 'utc'`  | 
|  `DAY`, `MONTH`, and `YEAR`  |  `EXTRACT(DAY/MONTH/YEAR FROM TIMESTAMP timestamp_value)`  | 
|  `DATEPART`  |  `EXTRACT`, `DATE_PART`  | 
|  `DATEDIFF`  |  `DATE_PART`  | 
|  `DATEADD`  |  `+ INTERVAL 'X days/months/years'`  | 
|  `CAST` and `CONVERT`  |  `CAST`  | 

For more information, see [Date/Time Functions and Operators](https://www.postgresql.org/docs/13/functions-datetime.html) in the *PostgreSQL documentation*.