

# Oracle TIMEZONE data type and functions and MySQL CONVERT\_TZ function
<a name="chap-oracle-aurora-mysql.sql.timezone"></a>

With AWS DMS, you can convert date and time values between different time zones when migrating databases. The Oracle `TIMEZONE` data type and functions, along with the MySQL `CONVERT_TZ` function, facilitate working with timestamps across time zones. The following sections provide details on leveraging Oracle `TIMEZONE` and MySQL `CONVERT_TZ` during database migrations using AWS DMS.


| Feature compatibility |  AWS SCT / AWS DMS automation level |  AWS SCT action code index | Key differences | 
| --- | --- | --- | --- | 
|  ![Two star feature compatibility](http://docs.aws.amazon.com/dms/latest/oracle-to-aurora-mysql-migration-playbook/images/pb-compatibility-2.png)  |  ![No automation](http://docs.aws.amazon.com/dms/latest/oracle-to-aurora-mysql-migration-playbook/images/pb-automation-0.png)  |  [Date and Time Functions](chap-oracle-aurora-mysql.tools.actioncode.md#chap-oracle-aurora-mysql.tools.actioncode.datetime)  | MySQL doesn’t provide an equivalent option for `CREATE TABLE…​TIMESTAMP WITH TIME ZONE` in Oracle but you can use `CONVERT_TZ` to achieve the same results. | 

## Oracle usage
<a name="chap-oracle-aurora-mysql.sql.timezone.oracle"></a>

Oracle uses data types and functions to integrate with time zones. For more information, see [A Time Zones](https://docs.oracle.com/cd/B13866_04/webconf.904/b10877/timezone.htm) in the *Oracle documentation*.

The following data types are variants of TIMESTAMP:
+  `TIMESTAMP WITH LOCAL TIME ZONE` — Data stored in the database is normalized to the database time zone, and the time zone offset is not stored as part of the column data. When users retrieve the data, Oracle returns it in the user’s local session time zone.
+  `TIMESTAMP WITH TIME ZONE` — Includes a time zone offset or time zone region name in its value.

Best practices:
+ Use the `TIMESTAMP WITH TIME ZONE` data type when the application is used across time zones.
+ The `TIMESTAMP WITH TIME ZONE` data type requires 13 bytes of storage; two more bytes of storage than `TIMESTAMP WITH LOCAL TIME ZONE` data types.

**Note**  
The retrieved time zone offset is the difference in hours and minutes between local time and UTC.

### Time zone functions
<a name="chap-oracle-aurora-mysql.sql.timezone.oracle.functions"></a>


| Function | Description | 
| --- | --- | 
|  `NEW_TIME`  | Converts date and time from one time zone to another. | 
|  `FROM_TZ`  | Converts a TZ to a `TIMESTAMP WITH TIME ZONE` value. | 
|  `CURRENT_TIMESTAMP`  | Returns the current date and time in the session time zone. | 
|  `DBTIMEZONE`  | Returns the current date and time in the database time zone. | 
|  `SYS_EXTRACT_UTC`  | Returns the UTC date and time. | 
|  `TO_TIMESTAMP_TZ`  | Converts a character string of `CHAR`, `VARCHAR2`, `NCHAR`, or `NVARCHAR2` to `TIMESTAMP WITH TIME ZONE`. | 

### Examples
<a name="chap-oracle-aurora-mysql.sql.timezone.oracle.examples"></a>

Create a table using `TIMESTAMP WITH LOCAL TIME ZONE`. Note that the last inserted row is displayed as a local session timestamp. It is the only row inserted using a specific time zone that is not `LOCAL`.

```
CREATE TABLE tz_local
(id NUMBER, tz_col TIMESTAMP WITH LOCAL TIME ZONE);

INSERT INTO tz_local VALUES(1, '01-JAN-2018 2:00:00');
INSERT INTO tz_local VALUES(2, TIMESTAMP '2018-01-01 2:00:00');
INSERT INTO tz_local VALUES(3, TIMESTAMP '2018-01-01 2:00:00 -08:00');

COMMIT;

SELECT * FROM tz_local;

ID  TZ_COL
1   2018-01-01 02:00:00
2   2018-01-01 02:00:00
3   2018-01-01 05:00:00
```

Create a table using `TIMESTAMP WITH TIME ZONE`. Note that the last inserted row is displayed as a local session timestamp. It is the only row that inserted using a specific time zone.

```
ALTER SESSION SET TIME_ZONE='-4:00';
CREATE TABLE tz_tbl (id NUMBER, tz_col TIMESTAMP WITH TIME ZONE);

INSERT INTO tz_tbl VALUES(1, '01-JAN-2018 2:00:00 AM -5:00');
INSERT INTO tz_tbl VALUES(2, TIMESTAMP '2018-01-01 3:00:00');
INSERT INTO tz_tbl VALUES(3, TIMESTAMP '2018-01-01 2:00:00 -8:00');

COMMIT;

SELECT * FROM tz_tbl;
ID  TZ_COL
1   01-JAN-03 02:00.00:000000 AM -07:00
2   01-JAN-03 02:00:00.000000 AM -07:00
3   01-JAN-03 02:00:00.000000 AM -08:00
```

## MySQL usage
<a name="chap-oracle-aurora-mysql.sql.timezone.mysql"></a>

MySQL uses time zone data type and functions similar to Oracle. Unlike Oracle, MySQL does not have many time zone options. Most functionality can be achieved when querying and not when running DDLs such as `CREATE TABLE` command in Oracle.

When the server starts, it places the host time zone in the system\_time\_zone system variable. This variable can be modified by setting the time zone operating system environment variable.

There is no equivalent option for Oracle `CREATE TABLE…​TIMESTAMP WITH TIME ZONE`.

### Comparison of time zone functions
<a name="chap-oracle-aurora-mysql.sql.timezone.mysql.functions"></a>


| Oracle function | MySQL function | 
| --- | --- | 
|  `NEW_TIME`  | You can use `CONVERT_TZ`, but you have to specify the source time zone. | 
|  `FROM_TZ`  |  `CONVERT_TZ`  | 
|  `DBTIMEZONE`  |  `CONVERT_TZ(CURRENT_TIME(),@@global.time_zone,@@global.time_zone)`  | 
|  `SYS_EXTRACT_UTC`  |  `CONVERT_TZ(CURRENT_TIME(),@@global.time_zone,'+00:00')`  | 
|  `TO_TIMESTAMP_TZ`  |  `CONVERT_TZ(STR_TO_DATE('17-09-2010 23:15','%d-%m-%Y %H:%i'),@@global.time_zone,'+03:00')`  | 

### Examples
<a name="chap-oracle-aurora-mysql.sql.timezone.mysql.examples"></a>

Query the global and session level time zone.

```
SELECT @@global.time_zone, @@session.time_zone;

@@global.time_zone  @@session.time_zone
SYSTEM              Europe/Moscow
```

For more information, see [MySQL Server Time Zone Support](https://dev.mysql.com/doc/refman/5.7/en/time-zone-support.html) and [Date and Time Functions](https://dev.mysql.com/doc/refman/5.7/en/date-and-time-functions.html) in the *MySQL documentation*.