

# Built-in function and system object rules
<a name="sc-default-rules-builtins-sqlserver"></a>

DMS Schema Conversion applies default rules to convert Microsoft SQL Server built-in functions and system objects when it converts a source schema to Amazon Aurora PostgreSQL or Amazon RDS for PostgreSQL. The following sections list the source objects in each category and show how DMS Schema Conversion converts each one.

Each table uses the following columns:
+ **Source** – the SQL Server built-in function or system object.
+ **Conversion** – how DMS Schema Conversion converts the object. A value of `Same name` means a direct mapping, `Renamed` means the object maps to a target with a different name, `Rewritten` means DMS Schema Conversion rewrites the object as a target expression, `Extension pack` means the conversion uses a function from the DMS Schema Conversion extension pack, and `Not converted` means DMS Schema Conversion does not convert the object automatically.
+ **Target** – the target object or expression that DMS Schema Conversion produces.
+ **Action item** – the action item code that DMS Schema Conversion reports for the object. An action item can mean that the object needs manual work, or be informational about an object that DMS Schema Conversion converted.

## Terms used in this topic
<a name="sc-default-rules-builtins-terms-sqlserver"></a>

The following table defines the terms that describe each conversion outcome.


| Term | Meaning | 
| --- | --- | 
| Same name | Converted automatically to a target object of the same name. | 
| Renamed | Converted automatically to a differently named target equivalent. | 
| Rewritten | Replaced by an equivalent native expression. | 
| Extension pack | DMS Schema Conversion converts the call to a function in the AWS DMS extension pack, a helper schema that emulates source functions with no PostgreSQL equivalent (aws\_oracle\_ext for Oracle sources, aws\_sqlserver\_ext for SQL Server sources). Apply the extension pack to your target database before you run the converted code. | 
| Not converted | No automatic conversion. An action item is raised and the code needs manual work. | 

## Aggregate
<a name="sc-default-rules-builtins-sqlserver-aggregate"></a>

The following table lists each source object in the Aggregate category and shows how DMS Schema Conversion converts it.


| Source | Conversion | Target | Action item | 
| --- | --- | --- | --- | 
| AVG | Same name | AVG | None | 
| CHECKSUM\_AGG | Not converted | Not applicable | 7811: PostgreSQL doesn't support the CHECKSUM\_AGG function. DMS SC skips this unsupported function in the converted code | 
| COUNT | Same name | COUNT | None | 
| COUNT\_BIG | Renamed | COUNT | None | 
| GROUPING\_ID | Not converted | Not applicable | 7811: PostgreSQL doesn't support the GROUPING\_ID function. DMS SC skips this unsupported function in the converted code | 
| MAX | Same name | MAX | None | 
| MIN | Same name | MIN | None | 
| STDEV | Renamed | STDDEV\_SAMP | None | 
| STDEVP | Renamed | STDDEV\_POP | None | 
| SUM | Same name | SUM | None | 
| VAR | Renamed | VAR\_SAMP | None | 
| VARP | Renamed | VAR\_POP | None | 

## Account and profiles
<a name="sc-default-rules-builtins-sqlserver-account-and-profiles"></a>

The following table lists each source object in the Account and profiles category and shows how DMS Schema Conversion converts it.


| Source | Conversion | Target | Action item | 
| --- | --- | --- | --- | 
| MSDB.DBO.SYSMAIL\_ADD\_ACCOUNT\_SP | Extension pack | aws\_sqlserver\_ext.SYSMAIL\_ADD\_ACCOUNT\_SP | None | 
| MSDB.DBO.SYSMAIL\_ADD\_PROFILEACCOUNT\_SP | Extension pack | aws\_sqlserver\_ext.SYSMAIL\_ADD\_PROFILEACCOUNT\_SP | None | 
| MSDB.DBO.SYSMAIL\_ADD\_PROFILE\_SP | Extension pack | aws\_sqlserver\_ext.SYSMAIL\_ADD\_PROFILE\_SP | None | 
| MSDB.DBO.SYSMAIL\_DELETE\_ACCOUNT\_SP | Extension pack | aws\_sqlserver\_ext.SYSMAIL\_DELETE\_ACCOUNT\_SP | None | 
| MSDB.DBO.SYSMAIL\_DELETE\_PROFILEACCOUNT\_SP | Extension pack | aws\_sqlserver\_ext.SYSMAIL\_DELETE\_PROFILEACCOUNT\_SP | None | 
| MSDB.DBO.SYSMAIL\_DELETE\_PROFILE\_SP | Extension pack | aws\_sqlserver\_ext.SYSMAIL\_DELETE\_PROFILE\_SP | None | 
| MSDB.DBO.SYSMAIL\_HELP\_ACCOUNT\_SP | Extension pack | aws\_sqlserver\_ext.SYSMAIL\_HELP\_ACCOUNT\_SP | None | 
| MSDB.DBO.SYSMAIL\_HELP\_PROFILEACCOUNT\_SP | Extension pack | aws\_sqlserver\_ext.SYSMAIL\_HELP\_PROFILEACCOUNT\_SP | None | 
| MSDB.DBO.SYSMAIL\_HELP\_PROFILE\_SP | Extension pack | aws\_sqlserver\_ext.SYSMAIL\_HELP\_PROFILE\_SP | None | 
| MSDB.DBO.SYSMAIL\_UPDATE\_ACCOUNT\_SP | Extension pack | aws\_sqlserver\_ext.SYSMAIL\_UPDATE\_ACCOUNT\_SP | None | 
| MSDB.DBO.SYSMAIL\_UPDATE\_PROFILEACCOUNT\_SP | Extension pack | aws\_sqlserver\_ext.SYSMAIL\_UPDATE\_PROFILEACCOUNT\_SP | None | 
| MSDB.DBO.SYSMAIL\_UPDATE\_PROFILE\_SP | Extension pack | aws\_sqlserver\_ext.SYSMAIL\_UPDATE\_PROFILE\_SP | None | 
| MSDB.DBO.SYSMAIL\_VERIFY\_ACCOUNT\_SP | Not converted | Not applicable | 7900: PostgreSQL doesn't support functionality similar to SQL Server Database Mail | 
| MSDB.DBO.SYSMAIL\_VERIFY\_ADDRESSPARAMS\_SP | Not converted | Not applicable | 7900: PostgreSQL doesn't support functionality similar to SQL Server Database Mail | 
| MSDB.DBO.SYSMAIL\_VERIFY\_PROFILE\_SP | Not converted | Not applicable | 7900: PostgreSQL doesn't support functionality similar to SQL Server Database Mail | 

## Configuration functions
<a name="sc-default-rules-builtins-sqlserver-configuration-functions"></a>

The following table lists each source object in the Configuration functions category and shows how DMS Schema Conversion converts it.


| Source | Conversion | Target | Action item | 
| --- | --- | --- | --- | 
| @@DATEFIRST | Not converted | Not applicable | 7811: PostgreSQL doesn't support the @@DATEFIRST function. DMS SC skips this unsupported function in the converted code | 
| @@DBTS | Rewritten | INT8SEND(PG\_SNAPSHOT\_XMAX(PG\_CURRENT\_SNAPSHOT())::TEXT::BIGINT-1) | None | 
| @@LANGID | Not converted | Not applicable | 7811: PostgreSQL doesn't support the @@LANGID function. DMS SC skips this unsupported function in the converted code | 
| @@LANGUAGE | Not converted | Not applicable | 7811: PostgreSQL doesn't support the @@LANGUAGE function. DMS SC skips this unsupported function in the converted code | 
| @@LOCK\_TIMEOUT | Not converted | Not applicable | 7811: PostgreSQL doesn't support the @@LOCK\_TIMEOUT function. DMS SC skips this unsupported function in the converted code | 
| @@MAX\_CONNECTIONS | Not converted | Not applicable | 7811: PostgreSQL doesn't support the @@MAX\_CONNECTIONS function. DMS SC skips this unsupported function in the converted code | 
| @@MAX\_PRECISION | Not converted | Not applicable | 7811: PostgreSQL doesn't support the @@MAX\_PRECISION function. DMS SC skips this unsupported function in the converted code | 
| @@NESTLEVEL | Not converted | Not applicable | 7811: PostgreSQL doesn't support the @@NESTLEVEL function. DMS SC skips this unsupported function in the converted code | 
| @@OPTIONS | Not converted | Not applicable | 7811: PostgreSQL doesn't support the @@OPTIONS function. DMS SC skips this unsupported function in the converted code | 
| @@REMSERVER | Not converted | Not applicable | 7811: PostgreSQL doesn't support the @@REMSERVER function. DMS SC skips this unsupported function in the converted code | 
| @@SERVERNAME | Not converted | Not applicable | 7811: PostgreSQL doesn't support the @@SERVERNAME function. DMS SC skips this unsupported function in the converted code | 
| @@SERVICENAME | Not converted | Not applicable | 7811: PostgreSQL doesn't support the @@SERVICENAME function. DMS SC skips this unsupported function in the converted code | 
| @@SPID | Renamed | pg\_backend\_pid() | None | 
| @@TEXTSIZE | Not converted | Not applicable | 7811: PostgreSQL doesn't support the @@TEXTSIZE function. DMS SC skips this unsupported function in the converted code | 
| @@VERSION | Not converted | Not applicable | 7811: PostgreSQL doesn't support the @@VERSION function. DMS SC skips this unsupported function in the converted code | 

## Cursor functions
<a name="sc-default-rules-builtins-sqlserver-cursor-functions"></a>

The following table lists each source object in the Cursor functions category and shows how DMS Schema Conversion converts it.


| Source | Conversion | Target | Action item | 
| --- | --- | --- | --- | 
| @@CURSOR\_ROWS | Not converted | Not applicable | 7811: PostgreSQL doesn't support the @@CURSOR\_ROWS function. DMS SC skips this unsupported function in the converted code | 
| @@FETCH\_STATUS | Rewritten | (case FOUND::int when 0 then -1 else 0 end) | None | 

## Date and time
<a name="sc-default-rules-builtins-sqlserver-date-and-time"></a>

The following table lists each source object in the Date and time category and shows how DMS Schema Conversion converts it.


| Source | Conversion | Target | Action item | 
| --- | --- | --- | --- | 
| CURRENT\_TIMESTAMP | Rewritten | CURRENT\_TIMESTAMP(3) | None | 
| DATEADD(DAY / DD / D, …) | Rewritten | ⟨date⟩ \+ (⟨number⟩::numeric \|\| ' DAY')::interval | None | 
| DATEADD(DAYOFYEAR / DY / Y, …) | Rewritten | ⟨date⟩ \+ (⟨number⟩::numeric \|\| ' DAY')::interval | None | 
| DATEADD(HOUR / HH, …) | Rewritten | ⟨date⟩ \+ (⟨number⟩::numeric \|\| ' HOUR')::interval | None | 
| DATEADD(MICROSECOND / MCS, …) | Rewritten | ⟨date⟩ \+ (⟨number⟩::numeric \|\| ' MICROSECOND')::interval | None | 
| DATEADD(MILLISECOND / MS, …) | Rewritten | ⟨date⟩ \+ (⟨number⟩::numeric \|\| ' MILLISECOND')::interval | None | 
| DATEADD(MINUTE / MI / N, …) | Rewritten | ⟨date⟩ \+ (⟨number⟩::numeric \|\| ' MINUTE')::interval | None | 
| DATEADD(MONTH / MM / M, …) | Rewritten | ⟨date⟩ \+ (⟨number⟩::numeric \|\| ' MONTH')::interval | None | 
| DATEADD(NANOSECOND / NS, …) | Not converted | Not applicable | 7811: PostgreSQL doesn't support the DATEADD(NANOSECOND / NS, …) function. DMS SC skips this unsupported function in the converted code | 
| DATEADD(QUARTER / QQ / Q, …) | Rewritten | ⟨date⟩ \+ (⟨number⟩::numeric \* 3 \|\| ' MONTH')::interval | None | 
| DATEADD(SECOND / SS / S, …) | Rewritten | ⟨date⟩ \+ (⟨number⟩::numeric \|\| ' SECOND')::interval | None | 
| DATEADD(WEEK / WK / WW, …) | Rewritten | ⟨date⟩ \+ (⟨number⟩::numeric \|\| ' WEEK')::interval | None | 
| DATEADD(WEEKDAY / DW, …) | Rewritten | ⟨date⟩ \+ (⟨number⟩::numeric \|\| ' DAY')::interval | None | 
| DATEADD(YEAR / YYYY / YY, …) | Rewritten | ⟨date⟩ \+ (⟨number⟩::numeric \|\| ' YEAR')::interval | None | 
| DATEADD(…) in an unsupported date arithmetic expression | Not converted | Not applicable | 7774: DMS SC can't convert arithmetic operations with mixed types of operands | 
| DATEDIFF | Extension pack | aws\_sqlserver\_ext.datediff('day',⟨startdate⟩::TIMESTAMP,⟨enddate⟩::TIMESTAMP) | None | 
| DATEFROMPARTS | Renamed | make\_date | None | 
| DATENAME(DAY / DD / D, …) | Rewritten | cast(date\_part('day',⟨date⟩::DATE) as varchar(2)) | None | 
| DATENAME(DAYOFYEAR / DY / Y, …) | Rewritten | to\_char(⟨date⟩::DATE,'DDD') | None | 
| DATENAME(HOUR / HH, …) | Rewritten | cast(date\_part('H',⟨date⟩::TIMESTAMP) as varchar(2)) | None | 
| DATENAME(MICROSECOND / MCS, …) | Rewritten | cast(cast(to\_char(⟨date⟩::TIMESTAMP,'US') as int) as varchar(6)) | None | 
| DATENAME(MILLISECOND / MS, …) | Rewritten | cast(cast(to\_char(⟨date⟩::TIMESTAMP,'MS') as int) as varchar(3)) | None | 
| DATENAME(MINUTE / N, …) | Rewritten | cast(date\_part('minute',⟨date⟩::TIMESTAMP) as varchar(2)) | None | 
| DATENAME(MONTH / MM / M, …) | Rewritten | to\_char(⟨date⟩::DATE,'Month') | None | 
| DATENAME(NANOSECOND / NS, …) | Not converted | Not applicable | 7811: PostgreSQL doesn't support the DATENAME(NANOSECOND / NS, …) function. DMS SC skips this unsupported function in the converted code | 
| DATENAME(QUARTER / QQ / Q, …) | Rewritten | to\_char(⟨date⟩::DATE,'q') | None | 
| DATENAME(SECOND / SS / S, …) | Rewritten | cast(cast(to\_char(⟨date⟩::TIMESTAMP,'SS') as int) as varchar(2)) | None | 
| DATENAME(TZOFFSET / TZ, …) | Rewritten | to\_char(⟨date⟩::TIMESTAMP,'OF') | None | 
| DATENAME(WEEK / WK / WW, …) | Rewritten | cast(date\_part('week',⟨date⟩::DATE) as varchar(2)) | None | 
| DATENAME(WEEKDAY / DW, …) | Rewritten | to\_char(⟨date⟩::TIMESTAMP,'Day') | None | 
| DATENAME(YEAR / YYYY / YY, …) | Rewritten | to\_char(⟨date⟩::DATE,'YYYY') | None | 
| DATEPART(DAY / DD / D, …) | Rewritten | date\_part('day',⟨date⟩::TIMESTAMP) | None | 
| DATEPART(DAYOFYEAR / DY / Y, …) | Rewritten | cast(to\_char(⟨date⟩::TIMESTAMP,'DDD') as int) | None | 
| DATEPART(HOUR / HH, …) | Rewritten | date\_part('H',⟨date⟩::TIMESTAMP) | None | 
| DATEPART(ISO\_WEEK / ISOWK / ISOWW, …) | Rewritten | EXTRACT(WEEK FROM ⟨date⟩) | None | 
| DATEPART(MICROSECOND / MCS, …) | Rewritten | cast(to\_char(⟨date⟩::TIMESTAMP,'US') as int) | None | 
| DATEPART(MILLISECOND / MS, …) | Rewritten | cast(to\_char(⟨date⟩::TIMESTAMP,'MS') as int) | None | 
| DATEPART(MINUTE / MI / N, …) | Rewritten | date\_part('minute',⟨date⟩::TIMESTAMP) | None | 
| DATEPART(MONTH / MM / M, …) | Rewritten | date\_part('month',⟨date⟩::TIMESTAMP) | None | 
| DATEPART(NANOSECOND / NS, …) | Not converted | Not applicable | 7811: PostgreSQL doesn't support the DATEPART(NANOSECOND / NS, …) function. DMS SC skips this unsupported function in the converted code | 
| DATEPART(QUARTER / QQ / Q, …) | Rewritten | date\_part('quarter',⟨date⟩::TIMESTAMP) | None | 
| DATEPART(SECOND / SS / S, …) | Rewritten | cast(to\_char(⟨date⟩::TIMESTAMP,'SS') as int) | None | 
| DATEPART(TZOFFSET / TZ, …) | Not converted | Not applicable | 7811: PostgreSQL doesn't support the DATEPART(TZOFFSET / TZ, …) function. DMS SC skips this unsupported function in the converted code | 
| DATEPART(WEEK / WK / WW, …) | Rewritten | cast(to\_char(⟨date⟩::TIMESTAMP, 'WW') as int) | None | 
| DATEPART(WEEKDAY / DW, …) | Rewritten | cast(to\_char(⟨date⟩::TIMESTAMP,'D') as int) | None | 
| DATEPART(YEAR / YYYY / YY, …) | Rewritten | date\_part('year',⟨n⟩::TIMESTAMP) | None | 
| DATETIME2FROMPARTS | Extension pack | aws\_sqlserver\_ext.datetime2fromparts(⟨y⟩, ⟨m⟩, ⟨d⟩, ⟨h⟩, ⟨min⟩, ⟨sec⟩, ⟨frc⟩, ⟨prcn⟩) | None | 
| DATETIMEFROMPARTS | Extension pack | aws\_sqlserver\_ext.datetimefromparts(⟨y⟩, ⟨m⟩, ⟨d⟩, ⟨h⟩, ⟨min⟩, ⟨sec⟩, ⟨msec⟩) | None | 
| DATETIMEOFFSETFROMPARTS | Rewritten | make\_timestamp(⟨y⟩, ⟨m⟩, ⟨d⟩, ⟨h⟩, ⟨min⟩, ⟨sec⟩) | None | 
| DAY | Same name | DAY | None | 
| DAY(DATE argument) | Rewritten | date\_part('day',⟨n⟩) | None | 
| EOMONTH(⟨date⟩) with a date/time typed argument | Rewritten | (date\_trunc('MONTH',⟨date⟩) \+ INTERVAL '1 MONTH - 1 day')::DATE | None | 
| EOMONTH(⟨date⟩) with any other argument type | Rewritten | (date\_trunc('MONTH',⟨date⟩::TIMESTAMP) \+ INTERVAL '1 MONTH - 1 day')::DATE | None | 
| EOMONTH(⟨date⟩, ⟨months⟩) with a date/time typed argument | Rewritten | (date\_trunc('MONTH',⟨date⟩) \+ (1\+⟨number⟩::numeric \|\| ' Month - 1 day')::interval)::DATE | None | 
| EOMONTH(⟨date⟩, ⟨months⟩) with any other argument type | Rewritten | (date\_trunc('MONTH',⟨date⟩::TIMESTAMP) \+ (1\+⟨number⟩::numeric \|\| ' Month - 1 day')::interval)::DATE | None | 
| GETDATE | Rewritten | clock\_timestamp() | None | 
| GETUTCDATE | Rewritten | timezone('UTC', CURRENT\_TIMESTAMP(6)) | None | 
| ISDATE | Not converted | Not applicable | 7811: PostgreSQL doesn't support the ISDATE function. DMS SC skips this unsupported function in the converted code | 
| MONTH | Same name | MONTH | None | 
| MONTH(DATE argument) | Rewritten | date\_part('month',⟨n⟩) | None | 
| SMALLDATETIMEFROMPARTS | Rewritten | make\_timestamp(⟨y⟩, ⟨m⟩, ⟨d⟩, ⟨h⟩, ⟨min⟩, 0) | None | 
| SP\_HELPDB | Not converted | Not applicable | 7904: DMS SC can't convert the SP\_HELPDB system object | 
| SP\_OASTOP | Not converted | Not applicable | 7904: DMS SC can't convert the SP\_OASTOP system object | 
| SWITCHOFFSET | Not converted | Not applicable | 7811: PostgreSQL doesn't support the SWITCHOFFSET function. DMS SC skips this unsupported function in the converted code | 
| SYSCOLUMNS | Not converted | Not applicable | 7904: DMS SC can't convert the SYSCOLUMNS system object | 
| SYSDATETIME | Rewritten | clock\_timestamp() | None | 
| SYSDATETIMEOFFSET | Rewritten | current\_timestamp(6) | None | 
| SYSFILES | Not converted | Not applicable | 7904: DMS SC can't convert the SYSFILES system object | 
| SYSUTCDATETIME | Rewritten | timezone('UTC', LOCALTIMESTAMP(6)) | None | 
| TIMEFROMPARTS | Extension pack | aws\_sqlserver\_ext.timefromparts(⟨h⟩, ⟨min⟩, ⟨sec⟩, ⟨frc⟩, ⟨prcn⟩) | None | 
| TODATETIMEOFFSET | Not converted | Not applicable | 7811: PostgreSQL doesn't support the TODATETIMEOFFSET function. DMS SC skips this unsupported function in the converted code | 
| YEAR | Same name | YEAR | None | 
| YEAR(DATE argument) | Rewritten | date\_part('year',⟨n⟩) | None | 

## Database Mail messenger objects
<a name="sc-default-rules-builtins-sqlserver-database-mail-messenger-objects"></a>

The following table lists each source object in the Database Mail messenger objects category and shows how DMS Schema Conversion converts it.


| Source | Conversion | Target | Action item | 
| --- | --- | --- | --- | 
| MSDB.DBO.SP\_SEND\_DBMAIL | Extension pack | aws\_sqlserver\_ext.SP\_SEND\_DBMAIL | None | 
| MSDB.DBO.SYSMAIL\_ALLITEMS | Extension pack | aws\_sqlserver\_ext.SYSMAIL\_ALLITEMS | None | 
| MSDB.DBO.SYSMAIL\_DELETE\_LOG\_SP | Not converted | Not applicable | 7900: PostgreSQL doesn't support functionality similar to SQL Server Database Mail | 
| MSDB.DBO.SYSMAIL\_DELETE\_MAILITEMS\_SP | Extension pack | aws\_sqlserver\_ext.SYSMAIL\_DELETE\_MAILITEMS\_SP | None | 
| MSDB.DBO.SYSMAIL\_EVENT\_LOG | Not converted | Not applicable | 7900: PostgreSQL doesn't support functionality similar to SQL Server Database Mail | 
| MSDB.DBO.SYSMAIL\_FAILEDITEMS | Extension pack | aws\_sqlserver\_ext.SYSMAIL\_FAILEDITEMS | None | 
| MSDB.DBO.SYSMAIL\_HELP\_QUEUE\_SP | Not converted | Not applicable | 7900: PostgreSQL doesn't support functionality similar to SQL Server Database Mail | 
| MSDB.DBO.SYSMAIL\_LOGMAILEVENT\_SP | Not converted | Not applicable | 7900: PostgreSQL doesn't support functionality similar to SQL Server Database Mail | 
| MSDB.DBO.SYSMAIL\_MAILATTACHMENTS | Extension pack | aws\_sqlserver\_ext.SYSMAIL\_MAILATTACHMENTS | None | 
| MSDB.DBO.SYSMAIL\_SENTITEMS | Extension pack | aws\_sqlserver\_ext.SYSMAIL\_SENTITEMS | None | 
| MSDB.DBO.SYSMAIL\_UNSENTITEMS | Extension pack | aws\_sqlserver\_ext.SYSMAIL\_UNSENTITEMS | None | 

## JSON functions
<a name="sc-default-rules-builtins-sqlserver-json-functions"></a>

In the JSON functions category, DMS Schema Conversion does not automatically convert any source objects. You must convert these objects manually. The following table lists these source objects.


| Source | Conversion | Target | Action item | 
| --- | --- | --- | --- | 
| ISJSON | Not converted | Not applicable | 7939: DMS SC can't convert the ISJSON JSON system function | 
| JSON\_MODIFY | Not converted | Not applicable | 7939: DMS SC can't convert the JSON\_MODIFY JSON system function | 
| JSON\_QUERY | Not converted | Not applicable | 7939: DMS SC can't convert the JSON\_QUERY JSON system function | 
| JSON\_VALUE | Not converted | Not applicable | 7939: DMS SC can't convert the JSON\_VALUE JSON system function | 

## Mathematical
<a name="sc-default-rules-builtins-sqlserver-mathematical"></a>

The following table lists each source object in the Mathematical category and shows how DMS Schema Conversion converts it.


| Source | Conversion | Target | Action item | 
| --- | --- | --- | --- | 
| ABS | Same name | ABS | None | 
| ACOS | Same name | ACOS | None | 
| ASIN | Same name | ASIN | None | 
| ATAN | Same name | ATAN | None | 
| ATN2 | Renamed | ATAN2 | None | 
| CEILING | Same name | CEILING | None | 
| COS | Same name | COS | None | 
| COT | Same name | COT | None | 
| DEGREES | Same name | DEGREES | None | 
| EXP | Same name | EXP | None | 
| FLOOR | Same name | FLOOR | None | 
| LOG(⟨expr⟩) | Renamed | LN | None | 
| LOG(⟨expr⟩, ⟨base⟩) | Rewritten | LOG(⟨base⟩, ⟨expr⟩) | None | 
| LOG10 | Rewritten | LOG(10, ⟨expr⟩) | None | 
| PI | Same name | PI | None | 
| POWER | Same name | POWER | None | 
| RADIANS | Same name | RADIANS | None | 
| RAND() | Renamed | RANDOM | None | 
| RAND(⟨seed⟩) | Rewritten | (SELECT random() FROM (SELECT setseed((⟨expr⟩) / 2147483649.))) | None | 
| ROUND(⟨expr⟩, ⟨length⟩) | Same name | ROUND | None | 
| ROUND(⟨expr⟩, ⟨length⟩, ⟨function⟩) | Extension pack | aws\_sqlserver\_ext.ROUND3 | None | 
| SIGN | Same name | SIGN | None | 
| SIN | Same name | SIN | None | 
| SQRT | Same name | SQRT | None | 
| SQUARE | Rewritten | POWER(⟨exp⟩, 2) | None | 
| TAN | Same name | TAN | None | 

## Metadata functions
<a name="sc-default-rules-builtins-sqlserver-metadata-functions"></a>

The following table lists each source object in the Metadata functions category and shows how DMS Schema Conversion converts it.


| Source | Conversion | Target | Action item | 
| --- | --- | --- | --- | 
| @@PROCID | Not converted | Not applicable | 7811: PostgreSQL doesn't support the @@PROCID function. DMS SC skips this unsupported function in the converted code | 
| APP\_NAME | Not converted | Not applicable | 7811: PostgreSQL doesn't support the APP\_NAME function. DMS SC skips this unsupported function in the converted code | 
| DB\_NAME | Renamed | current\_database | None | 
| SERVERPROPERTY | Not converted | Not applicable | 7811: PostgreSQL doesn't support the SERVERPROPERTY function. DMS SC skips this unsupported function in the converted code | 

## Other
<a name="sc-default-rules-builtins-sqlserver-other"></a>

The following table lists each source object in the Other category and shows how DMS Schema Conversion converts it.


| Source | Conversion | Target | Action item | 
| --- | --- | --- | --- | 
| APPROX\_COUNT\_DISTINCT | Not converted | Not applicable | 7811: PostgreSQL doesn't support the APPROX\_COUNT\_DISTINCT function. DMS SC skips this unsupported function in the converted code | 
| APPROX\_PERCENTILE\_CONT | Not converted | Not applicable | 7811: PostgreSQL doesn't support the APPROX\_PERCENTILE\_CONT function. DMS SC skips this unsupported function in the converted code | 
| APPROX\_PERCENTILE\_DISC | Not converted | Not applicable | 7811: PostgreSQL doesn't support the APPROX\_PERCENTILE\_DISC function. DMS SC skips this unsupported function in the converted code | 
| ASSEMBLYPROPERTY | Not converted | Not applicable | 7811: PostgreSQL doesn't support the ASSEMBLYPROPERTY function. DMS SC skips this unsupported function in the converted code | 
| ASYMKEYPROPERTY | Not converted | Not applicable | 7811: PostgreSQL doesn't support the ASYMKEYPROPERTY function. DMS SC skips this unsupported function in the converted code | 
| ASYMKEY\_ID | Not converted | Not applicable | 7811: PostgreSQL doesn't support the ASYMKEY\_ID function. DMS SC skips this unsupported function in the converted code | 
| BINARY\_CHECKSUM | Not converted | Not applicable | 7811: PostgreSQL doesn't support the BINARY\_CHECKSUM function. DMS SC skips this unsupported function in the converted code | 
| BIT\_COUNT | Not converted | Not applicable | 7811: PostgreSQL doesn't support the BIT\_COUNT function. DMS SC skips this unsupported function in the converted code | 
| CERTENCODED | Not converted | Not applicable | 7811: PostgreSQL doesn't support the CERTENCODED function. DMS SC skips this unsupported function in the converted code | 
| CERTPRIVATEKEY | Not converted | Not applicable | 7811: PostgreSQL doesn't support the CERTPRIVATEKEY function. DMS SC skips this unsupported function in the converted code | 
| CERTPROPERTY | Not converted | Not applicable | 7811: PostgreSQL doesn't support the CERTPROPERTY function. DMS SC skips this unsupported function in the converted code | 
| CERT\_ID | Not converted | Not applicable | 7811: PostgreSQL doesn't support the CERT\_ID function. DMS SC skips this unsupported function in the converted code | 
| CHECKSUM | Rewritten | ('x'\|\|SUBSTR(MD5(⟨expr⟩),1,8))::BIT(32)::INTEGER | None | 
| CHOOSE | Not converted | Not applicable | 7811: PostgreSQL doesn't support the CHOOSE function. DMS SC skips this unsupported function in the converted code | 
| COALESCE | Same name | COALESCE | None | 
| COLLATIONPROPERTY | Not converted | Not applicable | 7811: PostgreSQL doesn't support the COLLATIONPROPERTY function. DMS SC skips this unsupported function in the converted code | 
| COLUMNPROPERTY | Not converted | Not applicable | 7811: PostgreSQL doesn't support the COLUMNPROPERTY function. DMS SC skips this unsupported function in the converted code | 
| COLUMNS\_UPDATED | Not converted | Not applicable | 7909: DMS SC can't convert UPDATE(column) OR COLUMNS\_UPDATED statements | 
| COL\_LENGTH | Not converted | Not applicable | 7811: PostgreSQL doesn't support the COL\_LENGTH function. DMS SC skips this unsupported function in the converted code | 
| COL\_NAME | Not converted | Not applicable | 7811: PostgreSQL doesn't support the COL\_NAME function. DMS SC skips this unsupported function in the converted code | 
| COMPRESS | Not converted | Not applicable | 7811: PostgreSQL doesn't support the COMPRESS function. DMS SC skips this unsupported function in the converted code | 
| CONNECTIONPROPERTY | Not converted | Not applicable | 7811: PostgreSQL doesn't support the CONNECTIONPROPERTY function. DMS SC skips this unsupported function in the converted code | 
| CURRENT\_REQUEST\_ID | Not converted | Not applicable | 7811: PostgreSQL doesn't support the CURRENT\_REQUEST\_ID function. DMS SC skips this unsupported function in the converted code | 
| CURRENT\_TIMEZONE | Not converted | Not applicable | 7811: PostgreSQL doesn't support the CURRENT\_TIMEZONE function. DMS SC skips this unsupported function in the converted code | 
| CURRENT\_TIMEZONE\_ID | Not converted | Not applicable | 7811: PostgreSQL doesn't support the CURRENT\_TIMEZONE\_ID function. DMS SC skips this unsupported function in the converted code | 
| CURRENT\_TRANSACTION\_ID | Not converted | Not applicable | 7811: PostgreSQL doesn't support the CURRENT\_TRANSACTION\_ID function. DMS SC skips this unsupported function in the converted code | 
| CURRENT\_USER | Not converted | Not applicable | 7811: PostgreSQL doesn't support the CURRENT\_USER function. DMS SC skips this unsupported function in the converted code | 
| CURSOR\_STATUS | Not converted | Not applicable | 7811: PostgreSQL doesn't support the CURSOR\_STATUS function. DMS SC skips this unsupported function in the converted code | 
| DATABASEPROPERTYEX | Not converted | Not applicable | 7811: PostgreSQL doesn't support the DATABASEPROPERTYEX function. DMS SC skips this unsupported function in the converted code | 
| DATABASE\_PRINCIPAL\_ID | Not converted | Not applicable | 7811: PostgreSQL doesn't support the DATABASE\_PRINCIPAL\_ID function. DMS SC skips this unsupported function in the converted code | 
| DATEDIFF\_BIG | Not converted | Not applicable | 7811: PostgreSQL doesn't support the DATEDIFF\_BIG function. DMS SC skips this unsupported function in the converted code | 
| DATETRUNC | Not converted | Not applicable | 7811: PostgreSQL doesn't support the DATETRUNC function. DMS SC skips this unsupported function in the converted code | 
| DATE\_BUCKET | Not converted | Not applicable | 7811: PostgreSQL doesn't support the DATE\_BUCKET function. DMS SC skips this unsupported function in the converted code | 
| DB\_ID | Not converted | Not applicable | 7811: PostgreSQL doesn't support the DB\_ID function. DMS SC skips this unsupported function in the converted code | 
| DECOMPRESS | Not converted | Not applicable | 7811: PostgreSQL doesn't support the DECOMPRESS function. DMS SC skips this unsupported function in the converted code | 
| DECRYPTBYASYMKEY | Not converted | Not applicable | 7811: PostgreSQL doesn't support the DECRYPTBYASYMKEY function. DMS SC skips this unsupported function in the converted code | 
| DECRYPTBYCERT | Not converted | Not applicable | 7811: PostgreSQL doesn't support the DECRYPTBYCERT function. DMS SC skips this unsupported function in the converted code | 
| DECRYPTBYKEY | Not converted | Not applicable | 7811: PostgreSQL doesn't support the DECRYPTBYKEY function. DMS SC skips this unsupported function in the converted code | 
| DECRYPTBYKEYAUTOASYMKEY | Not converted | Not applicable | 7811: PostgreSQL doesn't support the DECRYPTBYKEYAUTOASYMKEY function. DMS SC skips this unsupported function in the converted code | 
| DECRYPTBYKEYAUTOCERT | Not converted | Not applicable | 7811: PostgreSQL doesn't support the DECRYPTBYKEYAUTOCERT function. DMS SC skips this unsupported function in the converted code | 
| DECRYPTBYPASSPHRASE | Not converted | Not applicable | 7811: PostgreSQL doesn't support the DECRYPTBYPASSPHRASE function. DMS SC skips this unsupported function in the converted code | 
| DENSE\_RANK | Same name | DENSE\_RANK | None | 
| ENCRYPTBYASYMKEY | Not converted | Not applicable | 7811: PostgreSQL doesn't support the ENCRYPTBYASYMKEY function. DMS SC skips this unsupported function in the converted code | 
| ENCRYPTBYCERT | Not converted | Not applicable | 7811: PostgreSQL doesn't support the ENCRYPTBYCERT function. DMS SC skips this unsupported function in the converted code | 
| ENCRYPTBYKEY | Not converted | Not applicable | 7811: PostgreSQL doesn't support the ENCRYPTBYKEY function. DMS SC skips this unsupported function in the converted code | 
| ENCRYPTBYPASSPHRASE | Not converted | Not applicable | 7811: PostgreSQL doesn't support the ENCRYPTBYPASSPHRASE function. DMS SC skips this unsupported function in the converted code | 
| ERROR\_LINE | Rewritten | error\_catch$ERROR\_LINE | None | 
| ERROR\_MESSAGE | Rewritten | error\_catch$ERROR\_MESSAGE | None | 
| ERROR\_NUMBER | Rewritten | error\_catch$ERROR\_NUMBER | None | 
| ERROR\_PROCEDURE | Rewritten | error\_catch$ERROR\_PROCEDURE | None | 
| ERROR\_SEVERITY | Rewritten | error\_catch$ERROR\_SEVERITY | None | 
| ERROR\_STATE | Rewritten | error\_catch$ERROR\_STATE | None | 
| EVENTDATA | Not converted | Not applicable | 7811: PostgreSQL doesn't support the EVENTDATA function. DMS SC skips this unsupported function in the converted code | 
| FILEGROUPPROPERTY | Not converted | Not applicable | 7811: PostgreSQL doesn't support the FILEGROUPPROPERTY function. DMS SC skips this unsupported function in the converted code | 
| FILEGROUP\_ID | Not converted | Not applicable | 7811: PostgreSQL doesn't support the FILEGROUP\_ID function. DMS SC skips this unsupported function in the converted code | 
| FILEGROUP\_NAME | Not converted | Not applicable | 7811: PostgreSQL doesn't support the FILEGROUP\_NAME function. DMS SC skips this unsupported function in the converted code | 
| FILEPROPERTY | Not converted | Not applicable | 7811: PostgreSQL doesn't support the FILEPROPERTY function. DMS SC skips this unsupported function in the converted code | 
| FILEPROPERTYEX | Not converted | Not applicable | 7811: PostgreSQL doesn't support the FILEPROPERTYEX function. DMS SC skips this unsupported function in the converted code | 
| FILE\_ID | Not converted | Not applicable | 7811: PostgreSQL doesn't support the FILE\_ID function. DMS SC skips this unsupported function in the converted code | 
| FILE\_IDEX | Not converted | Not applicable | 7811: PostgreSQL doesn't support the FILE\_IDEX function. DMS SC skips this unsupported function in the converted code | 
| FILE\_NAME | Not converted | Not applicable | 7811: PostgreSQL doesn't support the FILE\_NAME function. DMS SC skips this unsupported function in the converted code | 
| FORMATMESSAGE | Not converted | Not applicable | 7811: PostgreSQL doesn't support the FORMATMESSAGE function. DMS SC skips this unsupported function in the converted code | 
| FULLTEXTCATALOGPROPERTY | Not converted | Not applicable | 7811: PostgreSQL doesn't support the FULLTEXTCATALOGPROPERTY function. DMS SC skips this unsupported function in the converted code | 
| FULLTEXTSERVICEPROPERTY | Not converted | Not applicable | 7811: PostgreSQL doesn't support the FULLTEXTSERVICEPROPERTY function. DMS SC skips this unsupported function in the converted code | 
| GETANSINULL | Not converted | Not applicable | 7811: PostgreSQL doesn't support the GETANSINULL function. DMS SC skips this unsupported function in the converted code | 
| GET\_BIT | Not converted | Not applicable | 7811: PostgreSQL doesn't support the GET\_BIT function. DMS SC skips this unsupported function in the converted code | 
| HAS\_DBACCESS | Not converted | Not applicable | 7811: PostgreSQL doesn't support the HAS\_DBACCESS function. DMS SC skips this unsupported function in the converted code | 
| HAS\_PERMS\_BY\_NAME | Not converted | Not applicable | 7811: PostgreSQL doesn't support the HAS\_PERMS\_BY\_NAME function. DMS SC skips this unsupported function in the converted code | 
| HOST\_ID | Not converted | Not applicable | 7811: PostgreSQL doesn't support the HOST\_ID function. DMS SC skips this unsupported function in the converted code | 
| HOST\_NAME | Not converted | Not applicable | 7811: PostgreSQL doesn't support the HOST\_NAME function. DMS SC skips this unsupported function in the converted code | 
| IDENT\_CURRENT | Not converted | Not applicable | 7811: PostgreSQL doesn't support the IDENT\_CURRENT function. DMS SC skips this unsupported function in the converted code | 
| IDENT\_INCR | Not converted | Not applicable | 7811: PostgreSQL doesn't support the IDENT\_INCR function. DMS SC skips this unsupported function in the converted code | 
| IDENT\_SEED | Not converted | Not applicable | 7811: PostgreSQL doesn't support the IDENT\_SEED function. DMS SC skips this unsupported function in the converted code | 
| INDEXKEY\_PROPERTY | Not converted | Not applicable | 7811: PostgreSQL doesn't support the INDEXKEY\_PROPERTY function. DMS SC skips this unsupported function in the converted code | 
| INDEXPROPERTY | Not converted | Not applicable | 7811: PostgreSQL doesn't support the INDEXPROPERTY function. DMS SC skips this unsupported function in the converted code | 
| INDEX\_COL | Not converted | Not applicable | 7811: PostgreSQL doesn't support the INDEX\_COL function. DMS SC skips this unsupported function in the converted code | 
| ISNULL | Renamed | COALESCE | None | 
| ISNUMERIC(…) with any other number of arguments | Not converted | Not applicable | 7811: PostgreSQL doesn't support the ISNUMERIC(…) function. DMS SC skips this unsupported function in the converted code | 
| ISNUMERIC(⟨expr⟩) | Extension pack | aws\_sqlserver\_ext.isnumeric(⟨expr⟩) | None | 
| IS\_MEMBER | Not converted | Not applicable | 7811: PostgreSQL doesn't support the IS\_MEMBER function. DMS SC skips this unsupported function in the converted code | 
| IS\_OBJECTSIGNED | Not converted | Not applicable | 7811: PostgreSQL doesn't support the IS\_OBJECTSIGNED function. DMS SC skips this unsupported function in the converted code | 
| IS\_ROLEMEMBER | Not converted | Not applicable | 7811: PostgreSQL doesn't support the IS\_ROLEMEMBER function. DMS SC skips this unsupported function in the converted code | 
| IS\_SRVROLEMEMBER | Not converted | Not applicable | 7811: PostgreSQL doesn't support the IS\_SRVROLEMEMBER function. DMS SC skips this unsupported function in the converted code | 
| JSON\_OBJECT | Not converted | Not applicable | 7811: PostgreSQL doesn't support the JSON\_OBJECT function. DMS SC skips this unsupported function in the converted code | 
| JSON\_PATH\_EXISTS | Not converted | Not applicable | 7811: PostgreSQL doesn't support the JSON\_PATH\_EXISTS function. DMS SC skips this unsupported function in the converted code | 
| KEY\_GUID | Not converted | Not applicable | 7811: PostgreSQL doesn't support the KEY\_GUID function. DMS SC skips this unsupported function in the converted code | 
| KEY\_ID | Not converted | Not applicable | 7811: PostgreSQL doesn't support the KEY\_ID function. DMS SC skips this unsupported function in the converted code | 
| KEY\_NAME | Not converted | Not applicable | 7811: PostgreSQL doesn't support the KEY\_NAME function. DMS SC skips this unsupported function in the converted code | 
| LEFT\_SHIFT | Not converted | Not applicable | 7811: PostgreSQL doesn't support the LEFT\_SHIFT function. DMS SC skips this unsupported function in the converted code | 
| LOGINPROPERTY | Not converted | Not applicable | 7811: PostgreSQL doesn't support the LOGINPROPERTY function. DMS SC skips this unsupported function in the converted code | 
| MIN\_ACTIVE\_ROWVERSION | Not converted | Not applicable | 7811: PostgreSQL doesn't support the MIN\_ACTIVE\_ROWVERSION function. DMS SC skips this unsupported function in the converted code | 
| NEWID | Renamed | uuid\_generate\_v4 | 7831: Make sure that you install the uuid-ossp extension to use the newid() function | 
| NEWSEQUENTIALID | Not converted | Not applicable | 7811: PostgreSQL doesn't support the NEWSEQUENTIALID function. DMS SC skips this unsupported function in the converted code | 
| NTILE | Same name | NTILE | None | 
| NULLIF | Same name | NULLIF | None | 
| OBJECTPROPERTY | Not converted | Not applicable | 7811: PostgreSQL doesn't support the OBJECTPROPERTY function. DMS SC skips this unsupported function in the converted code | 
| OBJECTPROPERTYEX | Not converted | Not applicable | 7811: PostgreSQL doesn't support the OBJECTPROPERTYEX function. DMS SC skips this unsupported function in the converted code | 
| OBJECT\_DEFINITION | Not converted | Not applicable | 7811: PostgreSQL doesn't support the OBJECT\_DEFINITION function. DMS SC skips this unsupported function in the converted code | 
| OBJECT\_ID | Extension pack | aws\_sqlserver\_ext.object\_id | None | 
| OBJECT\_NAME | Not converted | Not applicable | 7811: PostgreSQL doesn't support the OBJECT\_NAME function. DMS SC skips this unsupported function in the converted code | 
| OBJECT\_SCHEMA\_NAME | Not converted | Not applicable | 7811: PostgreSQL doesn't support the OBJECT\_SCHEMA\_NAME function. DMS SC skips this unsupported function in the converted code | 
| ORIGINAL\_DB\_NAME | Not converted | Not applicable | 7811: PostgreSQL doesn't support the ORIGINAL\_DB\_NAME function. DMS SC skips this unsupported function in the converted code | 
| ORIGINAL\_LOGIN | Not converted | Not applicable | 7811: PostgreSQL doesn't support the ORIGINAL\_LOGIN function. DMS SC skips this unsupported function in the converted code | 
| PARSENAME | Not converted | Not applicable | 7811: PostgreSQL doesn't support the PARSENAME function. DMS SC skips this unsupported function in the converted code | 
| PERCENTILE\_CONT | Not converted | Not applicable | 7811: PostgreSQL doesn't support the PERCENTILE\_CONT function. DMS SC skips this unsupported function in the converted code | 
| PERCENTILE\_DISC | Not converted | Not applicable | 7811: PostgreSQL doesn't support the PERCENTILE\_DISC function. DMS SC skips this unsupported function in the converted code | 
| PERMISSIONS | Not converted | Not applicable | 7811: PostgreSQL doesn't support the PERMISSIONS function. DMS SC skips this unsupported function in the converted code | 
| PUBLISHINGSERVERNAME | Not converted | Not applicable | 7811: PostgreSQL doesn't support the PUBLISHINGSERVERNAME function. DMS SC skips this unsupported function in the converted code | 
| PWDCOMPARE | Not converted | Not applicable | 7811: PostgreSQL doesn't support the PWDCOMPARE function. DMS SC skips this unsupported function in the converted code | 
| PWDENCRYPT | Not converted | Not applicable | 7811: PostgreSQL doesn't support the PWDENCRYPT function. DMS SC skips this unsupported function in the converted code | 
| RANK | Same name | RANK | None | 
| RIGHT\_SHIFT | Not converted | Not applicable | 7811: PostgreSQL doesn't support the RIGHT\_SHIFT function. DMS SC skips this unsupported function in the converted code | 
| ROWCOUNT\_BIG | Not converted | Not applicable | 7811: PostgreSQL doesn't support the ROWCOUNT\_BIG function. DMS SC skips this unsupported function in the converted code | 
| ROW\_NUMBER | Same name | ROW\_NUMBER | None | 
| SCHEMA\_ID | Not converted | Not applicable | 7811: PostgreSQL doesn't support the SCHEMA\_ID function. DMS SC skips this unsupported function in the converted code | 
| SCHEMA\_NAME | Not converted | Not applicable | 7811: PostgreSQL doesn't support the SCHEMA\_NAME function. DMS SC skips this unsupported function in the converted code | 
| SESSIONPROPERTY | Not converted | Not applicable | 7811: PostgreSQL doesn't support the SESSIONPROPERTY function. DMS SC skips this unsupported function in the converted code | 
| SESSION\_CONTEXT | Not converted | Not applicable | 7811: PostgreSQL doesn't support the SESSION\_CONTEXT function. DMS SC skips this unsupported function in the converted code | 
| SESSION\_USER | Not converted | Not applicable | 7811: PostgreSQL doesn't support the SESSION\_USER function. DMS SC skips this unsupported function in the converted code | 
| SET\_BIT | Not converted | Not applicable | 7811: PostgreSQL doesn't support the SET\_BIT function. DMS SC skips this unsupported function in the converted code | 
| SIGNBYASYMKEY | Not converted | Not applicable | 7811: PostgreSQL doesn't support the SIGNBYASYMKEY function. DMS SC skips this unsupported function in the converted code | 
| SIGNBYCERT | Not converted | Not applicable | 7811: PostgreSQL doesn't support the SIGNBYCERT function. DMS SC skips this unsupported function in the converted code | 
| SP\_SEQUENCE\_GET\_RANGE | Extension pack | aws\_sqlserver\_ext.sp\_sequence\_get\_range(⟨seq\_name⟩, ⟨seq\_range⟩) | None | 
| SQL\_VARIANT\_PROPERTY | Not converted | Not applicable | 7811: PostgreSQL doesn't support the SQL\_VARIANT\_PROPERTY function. DMS SC skips this unsupported function in the converted code | 
| STATS\_DATE | Not converted | Not applicable | 7811: PostgreSQL doesn't support the STATS\_DATE function. DMS SC skips this unsupported function in the converted code | 
| STRING\_ESCAPE | Not converted | Not applicable | 7811: PostgreSQL doesn't support the STRING\_ESCAPE function. DMS SC skips this unsupported function in the converted code | 
| SUSER\_ID | Not converted | Not applicable | 7811: PostgreSQL doesn't support the SUSER\_ID function. DMS SC skips this unsupported function in the converted code | 
| SUSER\_NAME | Not converted | Not applicable | 7811: PostgreSQL doesn't support the SUSER\_NAME function. DMS SC skips this unsupported function in the converted code | 
| SUSER\_SID | Not converted | Not applicable | 7811: PostgreSQL doesn't support the SUSER\_SID function. DMS SC skips this unsupported function in the converted code | 
| SUSER\_SNAME | Rewritten | CURRENT\_USER | None | 
| SUSER\_SNAME(…) with 1 argument | Rewritten | NULL | None | 
| SYMKEYPROPERTY | Not converted | Not applicable | 7811: PostgreSQL doesn't support the SYMKEYPROPERTY function. DMS SC skips this unsupported function in the converted code | 
| SYSFOREIGNKEYS | Extension pack | aws\_sqlserver\_ext.SYS\_SYSFOREIGNKEYS | None | 
| SYSINDEXES | Extension pack | aws\_sqlserver\_ext.SYS\_SYSINDEXES | None | 
| SYSOBJECTS | Extension pack | aws\_sqlserver\_ext.SYS\_SYSOBJECTS | None | 
| SYSPROCESSES | Extension pack | aws\_sqlserver\_ext.SYS\_SYSPROCESSES | None | 
| SYSTEM\_USER | Not converted | Not applicable | 7811: PostgreSQL doesn't support the SYSTEM\_USER function. DMS SC skips this unsupported function in the converted code | 
| TERTIARY\_WEIGHTS | Not converted | Not applicable | 7811: PostgreSQL doesn't support the TERTIARY\_WEIGHTS function. DMS SC skips this unsupported function in the converted code | 
| TRIGGER\_NESTLEVEL | Not converted | Not applicable | 7811: PostgreSQL doesn't support the TRIGGER\_NESTLEVEL function. DMS SC skips this unsupported function in the converted code | 
| TYPEPROPERTY | Not converted | Not applicable | 7811: PostgreSQL doesn't support the TYPEPROPERTY function. DMS SC skips this unsupported function in the converted code | 
| TYPE\_ID | Not converted | Not applicable | 7811: PostgreSQL doesn't support the TYPE\_ID function. DMS SC skips this unsupported function in the converted code | 
| TYPE\_NAME | Not converted | Not applicable | 7811: PostgreSQL doesn't support the TYPE\_NAME function. DMS SC skips this unsupported function in the converted code | 
| USER\_ID | Not converted | Not applicable | 7811: PostgreSQL doesn't support the USER\_ID function. DMS SC skips this unsupported function in the converted code | 
| USER\_NAME | Not converted | Not applicable | 7811: PostgreSQL doesn't support the USER\_NAME function. DMS SC skips this unsupported function in the converted code | 
| VERIFYSIGNEDBYASYMKEY | Not converted | Not applicable | 7811: PostgreSQL doesn't support the VERIFYSIGNEDBYASYMKEY function. DMS SC skips this unsupported function in the converted code | 
| VERIFYSIGNEDBYCERT | Not converted | Not applicable | 7811: PostgreSQL doesn't support the VERIFYSIGNEDBYCERT function. DMS SC skips this unsupported function in the converted code | 
| XACT\_STATE | Not converted | Not applicable | 7811: PostgreSQL doesn't support the XACT\_STATE function. DMS SC skips this unsupported function in the converted code | 

## SQL Server Agent
<a name="sc-default-rules-builtins-sqlserver-sql-server-agent"></a>

The following table lists each source object in the SQL Server Agent category and shows how DMS Schema Conversion converts it.


| Source | Conversion | Target | Action item | 
| --- | --- | --- | --- | 
| MSDB.DBO.SP\_ADD\_ALERT | Not converted | Not applicable | 7902: PostgreSQL doesn't support functionality similar to SQL Server Agent | 
| MSDB.DBO.SP\_ADD\_CATEGORY | Not converted | Not applicable | 7902: PostgreSQL doesn't support functionality similar to SQL Server Agent | 
| MSDB.DBO.SP\_ADD\_JOB | Extension pack | aws\_sqlserver\_ext.SP\_ADD\_JOB | None | 
| MSDB.DBO.SP\_ADD\_JOBSCHEDULE | Extension pack | aws\_sqlserver\_ext.SP\_ADD\_JOBSCHEDULE | None | 
| MSDB.DBO.SP\_ADD\_JOBSERVER | Not converted | Not applicable | 7902: PostgreSQL doesn't support functionality similar to SQL Server Agent | 
| MSDB.DBO.SP\_ADD\_JOBSTEP | Extension pack | aws\_sqlserver\_ext.SP\_ADD\_JOBSTEP | None | 
| MSDB.DBO.SP\_ADD\_NOTIFICATION | Not converted | Not applicable | 7902: PostgreSQL doesn't support functionality similar to SQL Server Agent | 
| MSDB.DBO.SP\_ADD\_OPERATOR | Not converted | Not applicable | 7902: PostgreSQL doesn't support functionality similar to SQL Server Agent | 
| MSDB.DBO.SP\_ADD\_PROXY | Not converted | Not applicable | 7902: PostgreSQL doesn't support functionality similar to SQL Server Agent | 
| MSDB.DBO.SP\_ADD\_SCHEDULE | Extension pack | aws\_sqlserver\_ext.SP\_ADD\_SCHEDULE | None | 
| MSDB.DBO.SP\_ADD\_TARGETSERVERGROUP | Not converted | Not applicable | 7902: PostgreSQL doesn't support functionality similar to SQL Server Agent | 
| MSDB.DBO.SP\_ADD\_TARGETSVRGRP\_MEMBER | Not converted | Not applicable | 7902: PostgreSQL doesn't support functionality similar to SQL Server Agent | 
| MSDB.DBO.SP\_APPLY\_JOB\_TO\_TARGETS | Not converted | Not applicable | 7902: PostgreSQL doesn't support functionality similar to SQL Server Agent | 
| MSDB.DBO.SP\_ATTACH\_SCHEDULE | Extension pack | aws\_sqlserver\_ext.SP\_ATTACH\_SCHEDULE | None | 
| MSDB.DBO.SP\_CYCLE\_AGENT\_ERRORLOG | Not converted | Not applicable | 7902: PostgreSQL doesn't support functionality similar to SQL Server Agent | 
| MSDB.DBO.SP\_CYCLE\_ERRORLOG | Not converted | Not applicable | 7902: PostgreSQL doesn't support functionality similar to SQL Server Agent | 
| MSDB.DBO.SP\_DELETE\_ALERT | Not converted | Not applicable | 7902: PostgreSQL doesn't support functionality similar to SQL Server Agent | 
| MSDB.DBO.SP\_DELETE\_CATEGORY | Not converted | Not applicable | 7902: PostgreSQL doesn't support functionality similar to SQL Server Agent | 
| MSDB.DBO.SP\_DELETE\_JOB | Extension pack | aws\_sqlserver\_ext.SP\_DELETE\_JOB | None | 
| MSDB.DBO.SP\_DELETE\_JOBSCHEDULE | Extension pack | aws\_sqlserver\_ext.SP\_DELETE\_JOBSCHEDULE | None | 
| MSDB.DBO.SP\_DELETE\_JOBSERVER | Not converted | Not applicable | 7902: PostgreSQL doesn't support functionality similar to SQL Server Agent | 
| MSDB.DBO.SP\_DELETE\_JOBSTEP | Extension pack | aws\_sqlserver\_ext.SP\_DELETE\_JOBSTEP | None | 
| MSDB.DBO.SP\_DELETE\_JOBSTEPLOG | Not converted | Not applicable | 7902: PostgreSQL doesn't support functionality similar to SQL Server Agent | 
| MSDB.DBO.SP\_DELETE\_NOTIFICATION | Not converted | Not applicable | 7902: PostgreSQL doesn't support functionality similar to SQL Server Agent | 
| MSDB.DBO.SP\_DELETE\_OPERATOR | Not converted | Not applicable | 7902: PostgreSQL doesn't support functionality similar to SQL Server Agent | 
| MSDB.DBO.SP\_DELETE\_PROXY | Not converted | Not applicable | 7902: PostgreSQL doesn't support functionality similar to SQL Server Agent | 
| MSDB.DBO.SP\_DELETE\_SCHEDULE | Extension pack | aws\_sqlserver\_ext.SP\_DELETE\_SCHEDULE | None | 
| MSDB.DBO.SP\_DELETE\_TARGETSERVER | Not converted | Not applicable | 7902: PostgreSQL doesn't support functionality similar to SQL Server Agent | 
| MSDB.DBO.SP\_DELETE\_TARGETSERVERGROUP | Not converted | Not applicable | 7902: PostgreSQL doesn't support functionality similar to SQL Server Agent | 
| MSDB.DBO.SP\_DELETE\_TARGETSVRGRP\_MEMBER | Not converted | Not applicable | 7902: PostgreSQL doesn't support functionality similar to SQL Server Agent | 
| MSDB.DBO.SP\_DETACH\_SCHEDULE | Extension pack | aws\_sqlserver\_ext.SP\_DETACH\_SCHEDULE | None | 
| MSDB.DBO.SP\_ENUM\_LOGIN\_FOR\_PROXY | Not converted | Not applicable | 7902: PostgreSQL doesn't support functionality similar to SQL Server Agent | 
| MSDB.DBO.SP\_ENUM\_PROXY\_FOR\_SUBSYSTEM | Not converted | Not applicable | 7902: PostgreSQL doesn't support functionality similar to SQL Server Agent | 
| MSDB.DBO.SP\_ENUM\_SQLAGENT\_SUBSYSTEMS | Not converted | Not applicable | 7902: PostgreSQL doesn't support functionality similar to SQL Server Agent | 
| MSDB.DBO.SP\_GRANT\_LOGIN\_TO\_PROXY | Not converted | Not applicable | 7902: PostgreSQL doesn't support functionality similar to SQL Server Agent | 
| MSDB.DBO.SP\_GRANT\_PROXY\_TO\_SUBSYSTEM | Not converted | Not applicable | 7902: PostgreSQL doesn't support functionality similar to SQL Server Agent | 
| MSDB.DBO.SP\_HELP\_ALERT | Not converted | Not applicable | 7902: PostgreSQL doesn't support functionality similar to SQL Server Agent | 
| MSDB.DBO.SP\_HELP\_CATEGORY | Not converted | Not applicable | 7902: PostgreSQL doesn't support functionality similar to SQL Server Agent | 
| MSDB.DBO.SP\_HELP\_DOWNLOADLIST | Not converted | Not applicable | 7902: PostgreSQL doesn't support functionality similar to SQL Server Agent | 
| MSDB.DBO.SP\_HELP\_JOB | Not converted | Not applicable | 7902: PostgreSQL doesn't support functionality similar to SQL Server Agent | 
| MSDB.DBO.SP\_HELP\_JOBACTIVITY | Not converted | Not applicable | 7902: PostgreSQL doesn't support functionality similar to SQL Server Agent | 
| MSDB.DBO.SP\_HELP\_JOBCOUNT | Not converted | Not applicable | 7902: PostgreSQL doesn't support functionality similar to SQL Server Agent | 
| MSDB.DBO.SP\_HELP\_JOBHISTORY | Not converted | Not applicable | 7902: PostgreSQL doesn't support functionality similar to SQL Server Agent | 
| MSDB.DBO.SP\_HELP\_JOBSCHEDULE | Not converted | Not applicable | 7902: PostgreSQL doesn't support functionality similar to SQL Server Agent | 
| MSDB.DBO.SP\_HELP\_JOBSERVER | Not converted | Not applicable | 7902: PostgreSQL doesn't support functionality similar to SQL Server Agent | 
| MSDB.DBO.SP\_HELP\_JOBSTEP | Not converted | Not applicable | 7902: PostgreSQL doesn't support functionality similar to SQL Server Agent | 
| MSDB.DBO.SP\_HELP\_JOBSTEPLOG | Not converted | Not applicable | 7902: PostgreSQL doesn't support functionality similar to SQL Server Agent | 
| MSDB.DBO.SP\_HELP\_JOBS\_IN\_SCHEDULE | Not converted | Not applicable | 7902: PostgreSQL doesn't support functionality similar to SQL Server Agent | 
| MSDB.DBO.SP\_HELP\_NOTIFICATION | Not converted | Not applicable | 7902: PostgreSQL doesn't support functionality similar to SQL Server Agent | 
| MSDB.DBO.SP\_HELP\_OPERATOR | Not converted | Not applicable | 7902: PostgreSQL doesn't support functionality similar to SQL Server Agent | 
| MSDB.DBO.SP\_HELP\_PROXY | Not converted | Not applicable | 7902: PostgreSQL doesn't support functionality similar to SQL Server Agent | 
| MSDB.DBO.SP\_HELP\_SCHEDULE | Not converted | Not applicable | 7902: PostgreSQL doesn't support functionality similar to SQL Server Agent | 
| MSDB.DBO.SP\_HELP\_TARGETSERVER | Not converted | Not applicable | 7902: PostgreSQL doesn't support functionality similar to SQL Server Agent | 
| MSDB.DBO.SP\_HELP\_TARGETSERVERGROUP | Not converted | Not applicable | 7902: PostgreSQL doesn't support functionality similar to SQL Server Agent | 
| MSDB.DBO.SP\_MANAGE\_JOBS\_BY\_LOGIN | Not converted | Not applicable | 7902: PostgreSQL doesn't support functionality similar to SQL Server Agent | 
| MSDB.DBO.SP\_MSX\_DEFECT | Not converted | Not applicable | 7902: PostgreSQL doesn't support functionality similar to SQL Server Agent | 
| MSDB.DBO.SP\_MSX\_ENLIST | Not converted | Not applicable | 7902: PostgreSQL doesn't support functionality similar to SQL Server Agent | 
| MSDB.DBO.SP\_MSX\_GET\_ACCOUNT | Not converted | Not applicable | 7902: PostgreSQL doesn't support functionality similar to SQL Server Agent | 
| MSDB.DBO.SP\_MSX\_SET\_ACCOUNT | Not converted | Not applicable | 7902: PostgreSQL doesn't support functionality similar to SQL Server Agent | 
| MSDB.DBO.SP\_NOTIFY\_OPERATOR | Not converted | Not applicable | 7902: PostgreSQL doesn't support functionality similar to SQL Server Agent | 
| MSDB.DBO.SP\_POST\_MSX\_OPERATION | Not converted | Not applicable | 7902: PostgreSQL doesn't support functionality similar to SQL Server Agent | 
| MSDB.DBO.SP\_PURGE\_JOBHISTORY | Not converted | Not applicable | 7902: PostgreSQL doesn't support functionality similar to SQL Server Agent | 
| MSDB.DBO.SP\_REMOVE\_JOB\_FROM\_TARGETSS | Not converted | Not applicable | 7902: PostgreSQL doesn't support functionality similar to SQL Server Agent | 
| MSDB.DBO.SP\_RESYNC\_TARGETSERVER | Not converted | Not applicable | 7902: PostgreSQL doesn't support functionality similar to SQL Server Agent | 
| MSDB.DBO.SP\_REVOKE\_LOGIN\_FROM\_PROXY | Not converted | Not applicable | 7902: PostgreSQL doesn't support functionality similar to SQL Server Agent | 
| MSDB.DBO.SP\_REVOKE\_PROXY\_FROM\_SUBSYSTEM | Not converted | Not applicable | 7902: PostgreSQL doesn't support functionality similar to SQL Server Agent | 
| MSDB.DBO.SP\_START\_JOB | Not converted | Not applicable | 7902: PostgreSQL doesn't support functionality similar to SQL Server Agent | 
| MSDB.DBO.SP\_STOP\_JOB | Not converted | Not applicable | 7902: PostgreSQL doesn't support functionality similar to SQL Server Agent | 
| MSDB.DBO.SP\_UPDATE\_ALERT | Not converted | Not applicable | 7902: PostgreSQL doesn't support functionality similar to SQL Server Agent | 
| MSDB.DBO.SP\_UPDATE\_CATEGORY | Not converted | Not applicable | 7902: PostgreSQL doesn't support functionality similar to SQL Server Agent | 
| MSDB.DBO.SP\_UPDATE\_JOB | Extension pack | aws\_sqlserver\_ext.SP\_UPDATE\_JOB | None | 
| MSDB.DBO.SP\_UPDATE\_JOBSCHEDULE | Extension pack | aws\_sqlserver\_ext.SP\_UPDATE\_JOBSCHEDULE | None | 
| MSDB.DBO.SP\_UPDATE\_JOBSTEP | Extension pack | aws\_sqlserver\_ext.SP\_UPDATE\_JOBSTEP | None | 
| MSDB.DBO.SP\_UPDATE\_NOTIFICATION | Not converted | Not applicable | 7902: PostgreSQL doesn't support functionality similar to SQL Server Agent | 
| MSDB.DBO.SP\_UPDATE\_OPERATOR | Not converted | Not applicable | 7902: PostgreSQL doesn't support functionality similar to SQL Server Agent | 
| MSDB.DBO.SP\_UPDATE\_PROXY | Not converted | Not applicable | 7902: PostgreSQL doesn't support functionality similar to SQL Server Agent | 
| MSDB.DBO.SP\_UPDATE\_SCHEDULE | Extension pack | aws\_sqlserver\_ext.SP\_UPDATE\_SCHEDULE | None | 
| MSDB.DBO.SP\_UPDATE\_TARGETSERVERGROUP | Not converted | Not applicable | 7902: PostgreSQL doesn't support functionality similar to SQL Server Agent | 
| MSDB.DBO.SYSJOBHISTORY | Extension pack | aws\_sqlserver\_ext.SYSJOBHISTORY | None | 
| MSDB.DBO.SYSJOBS | Extension pack | aws\_sqlserver\_ext.SYSJOBS | None | 
| MSDB.DBO.SYSJOBSCHEDULES | Extension pack | aws\_sqlserver\_ext.SYSJOBSCHEDULES | None | 
| MSDB.DBO.SYSJOBSTEPS | Extension pack | aws\_sqlserver\_ext.SYSJOBSTEPS | None | 
| MSDB.DBO.SYSSCHEDULES | Extension pack | aws\_sqlserver\_ext.SYSSCHEDULES | None | 

## String
<a name="sc-default-rules-builtins-sqlserver-string"></a>

The following table lists each source object in the String category and shows how DMS Schema Conversion converts it.


| Source | Conversion | Target | Action item | 
| --- | --- | --- | --- | 
| ASCII | Rewritten | ASCII(case ⟨p1⟩ when '' then null else ⟨p1⟩ end) | None | 
| CHAR | Rewritten | CHR(NULLIF((⟨charcode⟩) \* ((⟨charcode⟩) BETWEEN 1 AND 255)::INT, 0)) | None | 
| CHARINDEX(⟨substr⟩, ⟨string⟩) | Rewritten | STRPOS(⟨p2⟩, ⟨p1⟩) | None | 
| CHARINDEX(⟨substr⟩, ⟨string⟩, ⟨start⟩) | Extension pack | aws\_sqlserver\_ext.STRPOS3(⟨p1⟩, ⟨p2⟩, ⟨p3⟩) | None | 
| CONCAT | Same name | CONCAT | None | 
| DIFFERENCE | Not converted | Not applicable | 7811: PostgreSQL doesn't support the DIFFERENCE function. DMS SC skips this unsupported function in the converted code | 
| FORMAT | Not converted | Not applicable | 7811: PostgreSQL doesn't support the FORMAT function. DMS SC skips this unsupported function in the converted code | 
| LEFT | Same name | LEFT | None | 
| LEN | Renamed | LENGTH | None | 
| LOWER | Same name | LOWER | None | 
| LTRIM | Same name | LTRIM | None | 
| NCHAR | Not converted | Not applicable | 7811: PostgreSQL doesn't support the NCHAR function. DMS SC skips this unsupported function in the converted code | 
| PATINDEX | Extension pack | aws\_sqlserver\_ext.patindex(⟨p1⟩, ⟨p2⟩) | None | 
| QUOTENAME | Renamed | QUOTE\_IDENT | None | 
| QUOTENAME(…) with 2 arguments | Not converted | Not applicable | 7811: PostgreSQL doesn't support the QUOTENAME(…) function. DMS SC skips this unsupported function in the converted code | 
| REPLACE | Rewritten | regexp\_replace(⟨p1⟩,⟨p2⟩,⟨p3⟩,'gi') | None | 
| REPLICATE | Rewritten | REPEAT( ⟨p1⟩, case when ⟨p2⟩<0 then null::int else ⟨p2⟩ end) | None | 
| REVERSE | Same name | REVERSE | None | 
| RIGHT | Same name | RIGHT | None | 
| RTRIM | Same name | RTRIM | None | 
| SOUNDEX | Not converted | Not applicable | 7811: PostgreSQL doesn't support the SOUNDEX function. DMS SC skips this unsupported function in the converted code | 
| SPACE | Rewritten | REPEAT( ' ', case when ⟨p1⟩<0 then null else ⟨p1⟩ end) | None | 
| STR(⟨expr⟩) | Rewritten | to\_char(⟨arg⟩::double precision,'9999999999') | None | 
| STR(⟨expr⟩, ⟨length⟩) with a literal length of 1 to 8000 | Rewritten | to\_char(⟨expression⟩::double precision, ⟨mask⟩) — the mask is 9 repeated ⟨length⟩ times | None | 
| STR(⟨expr⟩, ⟨length⟩) with any other length | Rewritten | to\_char(⟨expression⟩::double precision, null) | None | 
| STR(⟨expr⟩, ⟨length⟩, ⟨decimal⟩) | Extension pack | aws\_sqlserver\_ext.str(⟨expression⟩::double precision, ⟨length⟩, ⟨decimal⟩) | None | 
| STUFF | Rewritten | OVERLAY(⟨p1⟩ placing ⟨p4⟩ from ⟨p2⟩ for ⟨p3⟩) | None | 
| SUBSTRING | Renamed | SUBSTR | None | 
| UNICODE | Not converted | Not applicable | 7811: PostgreSQL doesn't support the UNICODE function. DMS SC skips this unsupported function in the converted code | 
| UPPER | Same name | UPPER | None | 

## Security
<a name="sc-default-rules-builtins-sqlserver-security"></a>

In the Security category, DMS Schema Conversion does not automatically convert any source objects. You must convert these objects manually. The following table lists these source objects.


| Source | Conversion | Target | Action item | 
| --- | --- | --- | --- | 
| MSDB.DBO.SYSMAIL\_ADD\_PRINCIPALPROFILE\_SP | Not converted | Not applicable | 7900: PostgreSQL doesn't support functionality similar to SQL Server Database Mail | 
| MSDB.DBO.SYSMAIL\_DELETE\_PRINCIPALPROFILE\_SP | Not converted | Not applicable | 7900: PostgreSQL doesn't support functionality similar to SQL Server Database Mail | 
| MSDB.DBO.SYSMAIL\_HELP\_PRINCIPALPROFILE\_SP | Not converted | Not applicable | 7900: PostgreSQL doesn't support functionality similar to SQL Server Database Mail | 
| MSDB.DBO.SYSMAIL\_UPDATE\_PRINCIPALPROFILE\_SP | Not converted | Not applicable | 7900: PostgreSQL doesn't support functionality similar to SQL Server Database Mail | 

## Service Broker catalog views
<a name="sc-default-rules-builtins-sqlserver-service-broker-catalog-views"></a>

In the Service Broker catalog views category, DMS Schema Conversion does not automatically convert any source objects. You must convert these objects manually. The following table lists these source objects.


| Source | Conversion | Target | Action item | 
| --- | --- | --- | --- | 
| SYS.CONVERSATION\_ENDPOINTS | Not converted | Not applicable | 7901: PostgreSQL doesn't support functionality similar to SQL Server Service Broker | 
| SYS.CONVERSATION\_GROUPS | Not converted | Not applicable | 7901: PostgreSQL doesn't support functionality similar to SQL Server Service Broker | 
| SYS.CONVERSATION\_PRIORITIES | Not converted | Not applicable | 7901: PostgreSQL doesn't support functionality similar to SQL Server Service Broker | 
| SYS.MESSAGE\_TYPE\_XML\_SCHEMA\_COLLECTION\_USAGES | Not converted | Not applicable | 7901: PostgreSQL doesn't support functionality similar to SQL Server Service Broker | 
| SYS.REMOTE\_SERVICE\_BINDINGS | Not converted | Not applicable | 7901: PostgreSQL doesn't support functionality similar to SQL Server Service Broker | 
| SYS.ROUTES | Not converted | Not applicable | 7901: PostgreSQL doesn't support functionality similar to SQL Server Service Broker | 
| SYS.SERVICES | Not converted | Not applicable | 7901: PostgreSQL doesn't support functionality similar to SQL Server Service Broker | 
| SYS.SERVICE\_CONTRACTS | Not converted | Not applicable | 7901: PostgreSQL doesn't support functionality similar to SQL Server Service Broker | 
| SYS.SERVICE\_CONTRACT\_MESSAGE\_USAGES | Not converted | Not applicable | 7901: PostgreSQL doesn't support functionality similar to SQL Server Service Broker | 
| SYS.SERVICE\_CONTRACT\_USAGES | Not converted | Not applicable | 7901: PostgreSQL doesn't support functionality similar to SQL Server Service Broker | 
| SYS.SERVICE\_MESSAGE\_TYPES | Not converted | Not applicable | 7901: PostgreSQL doesn't support functionality similar to SQL Server Service Broker | 
| SYS.SERVICE\_QUEUES | Not converted | Not applicable | 7901: PostgreSQL doesn't support functionality similar to SQL Server Service Broker | 
| SYS.SERVICE\_QUEUE\_USAGES | Not converted | Not applicable | 7901: PostgreSQL doesn't support functionality similar to SQL Server Service Broker | 
| SYS.TRANSMISSION\_QUEUE | Not converted | Not applicable | 7901: PostgreSQL doesn't support functionality similar to SQL Server Service Broker | 

## Service Broker related dynamic management views
<a name="sc-default-rules-builtins-sqlserver-service-broker-related-dynamic-management-views"></a>

In the Service Broker related dynamic management views category, DMS Schema Conversion does not automatically convert any source objects. You must convert these objects manually. The following table lists these source objects.


| Source | Conversion | Target | Action item | 
| --- | --- | --- | --- | 
| SYS.DM\_BROKER\_ACTIVATED\_TASKS | Not converted | Not applicable | 7901: PostgreSQL doesn't support functionality similar to SQL Server Service Broker | 
| SYS.DM\_BROKER\_CONNECTIONS | Not converted | Not applicable | 7901: PostgreSQL doesn't support functionality similar to SQL Server Service Broker | 
| SYS.DM\_BROKER\_FORWARDED\_MESSAGES | Not converted | Not applicable | 7901: PostgreSQL doesn't support functionality similar to SQL Server Service Broker | 
| SYS.DM\_BROKER\_QUEUE\_MONITORS | Not converted | Not applicable | 7901: PostgreSQL doesn't support functionality similar to SQL Server Service Broker | 

## Settings
<a name="sc-default-rules-builtins-sqlserver-settings"></a>

In the Settings category, DMS Schema Conversion does not automatically convert any source objects. You must convert these objects manually. The following table lists these source objects.


| Source | Conversion | Target | Action item | 
| --- | --- | --- | --- | 
| MSDB.DBO.SYSMAIL\_CONFIGURE\_SP | Not converted | Not applicable | 7900: PostgreSQL doesn't support functionality similar to SQL Server Database Mail | 
| MSDB.DBO.SYSMAIL\_HELP\_CONFIGURE\_SP | Not converted | Not applicable | 7900: PostgreSQL doesn't support functionality similar to SQL Server Database Mail | 

## Spatial types
<a name="sc-default-rules-builtins-sqlserver-spatial-types"></a>

The following table lists each source object in the Spatial types category and shows how DMS Schema Conversion converts it.


| Source | Conversion | Target | Action item | 
| --- | --- | --- | --- | 
| GEOGRAPHY.ASBINARYZM | Rewritten | ST\_AsBinary(⟨spat⟩) | None | 
| GEOGRAPHY.ASGML | Rewritten | ST\_AsGml(⟨spat⟩)::XML | None | 
| GEOGRAPHY.ASTEXTZM | Rewritten | ST\_AsText(⟨spat⟩) | None | 
| GEOGRAPHY.BUFFERWITHCURVES | Rewritten | case when ⟨par1⟩ = 0 then ⟨spat⟩ when ⟨par1⟩ < 1e-11 then ⟨spat⟩ else ST\_Buffer(⟨spat⟩, ⟨par1⟩) end | None | 
| GEOGRAPHY.BUFFERWITHTOLERANCE | Not converted | Not applicable | 7917: PostgreSQL doesn't support the GEOGRAPHY.BUFFERWITHTOLERANCE function | 
| GEOGRAPHY.COLLECTIONAGGREGATE | Not converted | Not applicable | 7917: PostgreSQL doesn't support the GEOGRAPHY.COLLECTIONAGGREGATE function | 
| GEOGRAPHY.CONVEXHULLAGGREGATE | Not converted | Not applicable | 7917: PostgreSQL doesn't support the GEOGRAPHY.CONVEXHULLAGGREGATE function | 
| GEOGRAPHY.CURVETOLINEWITHTOLERANCE | Not converted | Not applicable | 7917: PostgreSQL doesn't support the GEOGRAPHY.CURVETOLINEWITHTOLERANCE function | 
| GEOGRAPHY.ENVELOPEAGGREGATE | Not converted | Not applicable | 7917: PostgreSQL doesn't support the GEOGRAPHY.ENVELOPEAGGREGATE function | 
| GEOGRAPHY.ENVELOPEANGLE | Not converted | Not applicable | 7917: PostgreSQL doesn't support the GEOGRAPHY.ENVELOPEANGLE function | 
| GEOGRAPHY.ENVELOPECENTER | Not converted | Not applicable | 7917: PostgreSQL doesn't support the GEOGRAPHY.ENVELOPECENTER function | 
| GEOGRAPHY.FILTER | Rewritten | (case ST\_Intersects(⟨spat⟩,⟨par1⟩) when true then 1 when false then 0 else null end)::NUMERIC(1) | None | 
| GEOGRAPHY.GEOMFROMGML | Not converted | Not applicable | 7917: PostgreSQL doesn't support the GEOGRAPHY.GEOMFROMGML function | 
| GEOGRAPHY.HASM | Not converted | Not applicable | 7917: PostgreSQL doesn't support the GEOGRAPHY.HASM function | 
| GEOGRAPHY.HASZ | Not converted | Not applicable | 7917: PostgreSQL doesn't support the GEOGRAPHY.HASZ function | 
| GEOGRAPHY.INSTANCEOF | Not converted | Not applicable | 7917: PostgreSQL doesn't support the GEOGRAPHY.INSTANCEOF function | 
| GEOGRAPHY.ISNULL | Rewritten | (case when ⟨spat⟩ is null then null else 0 end)::NUMERIC(1) | None | 
| GEOGRAPHY.ISVALIDDETAILED | Not converted | Not applicable | 7917: PostgreSQL doesn't support the GEOGRAPHY.ISVALIDDETAILED function | 
| GEOGRAPHY.LAT | Rewritten | ST\_Y(geography::⟨spat⟩) | None | 
| GEOGRAPHY.LONG | Rewritten | ST\_X(geography::⟨spat⟩) | None | 
| GEOGRAPHY.M | Not converted | Not applicable | 7917: PostgreSQL doesn't support the GEOGRAPHY.M function | 
| GEOGRAPHY.MAKEVALID | Not converted | Not applicable | 7917: PostgreSQL doesn't support the GEOGRAPHY.MAKEVALID function | 
| GEOGRAPHY.MINDBCOMPABILITYLEVEL | Not converted | Not applicable | 7917: PostgreSQL doesn't support the GEOGRAPHY.MINDBCOMPABILITYLEVEL function | 
| GEOGRAPHY.MINDBCOMPATIBILITYLEVEL | Not converted | Not applicable | 7917: PostgreSQL doesn't support the GEOGRAPHY.MINDBCOMPATIBILITYLEVEL function | 
| GEOGRAPHY.NULL | Renamed | null::GEOGRAPHY | None | 
| GEOGRAPHY.NUMRINGS | Not converted | Not applicable | 7917: PostgreSQL doesn't support the GEOGRAPHY.NUMRINGS function | 
| GEOGRAPHY.PARSE | Rewritten | ST\_GeogFromText('SRID='\|\|4326::VARCHAR\|\|';'\|\|⟨p\_text⟩) | None | 
| GEOGRAPHY.POINT | Rewritten | ST\_SetSRID(ST\_Point(⟨p1⟩, ⟨p2⟩), ⟨p3⟩)::GEOGRAPHY | None | 
| GEOGRAPHY.REDUCE | Not converted | Not applicable | 7917: PostgreSQL doesn't support the GEOGRAPHY.REDUCE function | 
| GEOGRAPHY.REORIENTOBJECT | Not converted | Not applicable | 7917: PostgreSQL doesn't support the GEOGRAPHY.REORIENTOBJECT function | 
| GEOGRAPHY.RINGN | Not converted | Not applicable | 7917: PostgreSQL doesn't support the GEOGRAPHY.RINGN function | 
| GEOGRAPHY.SHORTESTLINE | Not converted | Not applicable | 7917: PostgreSQL doesn't support the GEOGRAPHY.SHORTESTLINE function | 
| GEOGRAPHY.SHORTESTLINETO | Not converted | Not applicable | 7917: PostgreSQL doesn't support the GEOGRAPHY.SHORTESTLINETO function | 
| GEOGRAPHY.STASBINARY | Rewritten | ST\_AsBinary(⟨spat⟩) | None | 
| GEOGRAPHY.STASTEXT | Rewritten | ST\_AsText(⟨spat⟩) | None | 
| GEOGRAPHY.STBUFFER | Rewritten | ST\_Buffer(⟨spat⟩, ⟨par1⟩) | None | 
| GEOGRAPHY.STCONTAINS | Not converted | Not applicable | 7917: PostgreSQL doesn't support the GEOGRAPHY.STCONTAINS function | 
| GEOGRAPHY.STCONVEXHULL | Not converted | Not applicable | 7917: PostgreSQL doesn't support the GEOGRAPHY.STCONVEXHULL function | 
| GEOGRAPHY.STCURVEN | Not converted | Not applicable | 7917: PostgreSQL doesn't support the GEOGRAPHY.STCURVEN function | 
| GEOGRAPHY.STCURVETOLINE | Not converted | Not applicable | 7917: PostgreSQL doesn't support the GEOGRAPHY.STCURVETOLINE function | 
| GEOGRAPHY.STDIFFERENCE | Not converted | Not applicable | 7917: PostgreSQL doesn't support the GEOGRAPHY.STDIFFERENCE function | 
| GEOGRAPHY.STDIMENSION | Rewritten | (case ST\_IsEmpty(⟨spat⟩) when true then -1 else ST\_Dimension(⟨spat⟩) end)::numeric(10) | None | 
| GEOGRAPHY.STDISJOINT | Not converted | Not applicable | 7917: PostgreSQL doesn't support the GEOGRAPHY.STDISJOINT function | 
| GEOGRAPHY.STDISTANCE | Rewritten | ST\_Distance(⟨spat⟩, ⟨par1⟩)::DOUBLE PRECISION | None | 
| GEOGRAPHY.STENDPOINT | Not converted | Not applicable | 7917: PostgreSQL doesn't support the GEOGRAPHY.STENDPOINT function | 
| GEOGRAPHY.STEQUALS | Not converted | Not applicable | 7917: PostgreSQL doesn't support the GEOGRAPHY.STEQUALS function | 
| GEOGRAPHY.STGEOMCOLLFROMTEXT | Not converted | Not applicable | 7917: PostgreSQL doesn't support the GEOGRAPHY.STGEOMCOLLFROMTEXT function | 
| GEOGRAPHY.STGEOMCOLLFROMWKB | Not converted | Not applicable | 7917: PostgreSQL doesn't support the GEOGRAPHY.STGEOMCOLLFROMWKB function | 
| GEOGRAPHY.STGEOMETRYN | Not converted | Not applicable | 7917: PostgreSQL doesn't support the GEOGRAPHY.STGEOMETRYN function | 
| GEOGRAPHY.STGEOMETRYTYPE | Not converted | Not applicable | 7917: PostgreSQL doesn't support the GEOGRAPHY.STGEOMETRYTYPE function | 
| GEOGRAPHY.STGEOMFROMTEXT | Rewritten | ST\_GeogFromText('SRID='\|\|⟨p2⟩::VARCHAR\|\|';'\|\|⟨p1⟩) | None | 
| GEOGRAPHY.STGEOMFROMWKB | Not converted | Not applicable | 7917: PostgreSQL doesn't support the GEOGRAPHY.STGEOMFROMWKB function | 
| GEOGRAPHY.STINTERSECTION | Rewritten | ST\_Intersection(⟨spat⟩, ⟨par1⟩) | None | 
| GEOGRAPHY.STINTERSECTS | Rewritten | (case ST\_Intersects(⟨spat⟩, ⟨par1⟩) when true then 1 when false then 0 else null end)::NUMERIC(1) | None | 
| GEOGRAPHY.STISCLOSED | Not converted | Not applicable | 7917: PostgreSQL doesn't support the GEOGRAPHY.STISCLOSED function | 
| GEOGRAPHY.STISEMPTY | Not converted | Not applicable | 7917: PostgreSQL doesn't support the GEOGRAPHY.STISEMPTY function | 
| GEOGRAPHY.STISVALID | Not converted | Not applicable | 7917: PostgreSQL doesn't support the GEOGRAPHY.STISVALID function | 
| GEOGRAPHY.STLENGTH | Rewritten | ST\_Length(⟨spat⟩)::DOUBLE PRECISION | None | 
| GEOGRAPHY.STLINEFROMTEXT | Not converted | Not applicable | 7917: PostgreSQL doesn't support the GEOGRAPHY.STLINEFROMTEXT function | 
| GEOGRAPHY.STLINEFROMWKB | Not converted | Not applicable | 7917: PostgreSQL doesn't support the GEOGRAPHY.STLINEFROMWKB function | 
| GEOGRAPHY.STMLINEFROMTEXT | Not converted | Not applicable | 7917: PostgreSQL doesn't support the GEOGRAPHY.STMLINEFROMTEXT function | 
| GEOGRAPHY.STMLINEFROMWKB | Not converted | Not applicable | 7917: PostgreSQL doesn't support the GEOGRAPHY.STMLINEFROMWKB function | 
| GEOGRAPHY.STMPOINTFROMTEXT | Not converted | Not applicable | 7917: PostgreSQL doesn't support the GEOGRAPHY.STMPOINTFROMTEXT function | 
| GEOGRAPHY.STMPOINTFROMWKB | Not converted | Not applicable | 7917: PostgreSQL doesn't support the GEOGRAPHY.STMPOINTFROMWKB function | 
| GEOGRAPHY.STMPOLYFROMTEXT | Not converted | Not applicable | 7917: PostgreSQL doesn't support the GEOGRAPHY.STMPOLYFROMTEXT function | 
| GEOGRAPHY.STMPOLYFROMWKB | Not converted | Not applicable | 7917: PostgreSQL doesn't support the GEOGRAPHY.STMPOLYFROMWKB function | 
| GEOGRAPHY.STNUMCURVES | Not converted | Not applicable | 7917: PostgreSQL doesn't support the GEOGRAPHY.STNUMCURVES function | 
| GEOGRAPHY.STNUMGEOMETRIES | Not converted | Not applicable | 7917: PostgreSQL doesn't support the GEOGRAPHY.STNUMGEOMETRIES function | 
| GEOGRAPHY.STNUMPOINTS | Not converted | Not applicable | 7917: PostgreSQL doesn't support the GEOGRAPHY.STNUMPOINTS function | 
| GEOGRAPHY.STOVERLAPS | Not converted | Not applicable | 7917: PostgreSQL doesn't support the GEOGRAPHY.STOVERLAPS function | 
| GEOGRAPHY.STPOINTN | Not converted | Not applicable | 7917: PostgreSQL doesn't support the GEOGRAPHY.STPOINTN function | 
| GEOGRAPHY.STSRID | Not converted | Not applicable | 7917: PostgreSQL doesn't support the GEOGRAPHY.STSRID function | 
| GEOGRAPHY.STSTARTPOINT | Not converted | Not applicable | 7917: PostgreSQL doesn't support the GEOGRAPHY.STSTARTPOINT function | 
| GEOGRAPHY.STSYMDIFFERENCE | Not converted | Not applicable | 7917: PostgreSQL doesn't support the GEOGRAPHY.STSYMDIFFERENCE function | 
| GEOGRAPHY.STUNION | Not converted | Not applicable | 7917: PostgreSQL doesn't support the GEOGRAPHY.STUNION function | 
| GEOGRAPHY.STWITHIN | Not converted | Not applicable | 7917: PostgreSQL doesn't support the GEOGRAPHY.STWITHIN function | 
| GEOGRAPHY.TOSTRING | Rewritten | ST\_AsText(⟨spat⟩) | None | 
| GEOGRAPHY.UNIONAGGREGATE | Not converted | Not applicable | 7917: PostgreSQL doesn't support the GEOGRAPHY.UNIONAGGREGATE function | 
| GEOGRAPHY.Z | Not converted | Not applicable | 7917: PostgreSQL doesn't support the GEOGRAPHY.Z function | 
| GEOMETRY.ASBINARYZM | Rewritten | ST\_AsBinary(⟨spat⟩) | None | 
| GEOMETRY.ASGML | Rewritten | ST\_AsGml(⟨spat⟩)::XML | None | 
| GEOMETRY.ASTEXTZM | Rewritten | ST\_AsText(⟨spat⟩) | None | 
| GEOMETRY.BUFFERWITHCURVES | Rewritten | case when ⟨par1⟩ = 0 then ⟨spat⟩ when ⟨par1⟩ < 1e-11 then ⟨spat⟩ else ST\_Buffer(⟨spat⟩, ⟨par1⟩) end | None | 
| GEOMETRY.BUFFERWITHTOLERANCE | Not converted | Not applicable | 7917: PostgreSQL doesn't support the GEOMETRY.BUFFERWITHTOLERANCE function | 
| GEOMETRY.COLLECTIONAGGREGATE | Rewritten | ST\_Collect(⟨p1⟩) | None | 
| GEOMETRY.CONVEXHULLAGGREGATE | Not converted | Not applicable | 7917: PostgreSQL doesn't support the GEOMETRY.CONVEXHULLAGGREGATE function | 
| GEOMETRY.CURVETOLINEWITHTOLERANCE | Not converted | Not applicable | 7917: PostgreSQL doesn't support the GEOMETRY.CURVETOLINEWITHTOLERANCE function | 
| GEOMETRY.ENVELOPEAGGREGATE | Not converted | Not applicable | 7917: PostgreSQL doesn't support the GEOMETRY.ENVELOPEAGGREGATE function | 
| GEOMETRY.FILTER | Rewritten | (case ST\_Intersects(⟨spat⟩,⟨par1⟩) when true then 1 when false then 0 else null end)::NUMERIC(1) | None | 
| GEOMETRY.GEOMFROMGML | Rewritten | ST\_GeomFromGML(⟨p1⟩, ⟨p2⟩) | None | 
| GEOMETRY.HASM | Rewritten | (case geometryAType(⟨spat⟩) when 'POINT' then case when ST\_M(⟨spat⟩) is not null then 1 else 0 end else 0 end)::NUMERIC(1) | None | 
| GEOMETRY.HASZ | Rewritten | (case geometryAType(⟨spat⟩) when 'POINT' then case when ST\_Z(⟨spat⟩) is not null then 1 else 0 end else 0 end)::NUMERIC(1) | None | 
| GEOMETRY.INSTANCEOF | Not converted | Not applicable | 7917: PostgreSQL doesn't support the GEOMETRY.INSTANCEOF function | 
| GEOMETRY.ISNULL | Rewritten | (case when ⟨spat⟩ is null then null else 0 end)::NUMERIC(1) | None | 
| GEOMETRY.ISVALIDDETAILED | Rewritten | ST\_IsValidDetail(⟨spat⟩)::text | None | 
| GEOMETRY.M | Rewritten | ST\_M(case when geometryType(⟨spat⟩)\!='POINT' then null else ⟨spat⟩ end)::DOUBLE PRECISION | None | 
| GEOMETRY.MAKEVALID | Rewritten | ST\_MakeValid(⟨spat⟩) | None | 
| GEOMETRY.MINDBCOMPABILITYLEVEL | Not converted | Not applicable | 7917: PostgreSQL doesn't support the GEOMETRY.MINDBCOMPABILITYLEVEL function | 
| GEOMETRY.MINDBCOMPATIBILITYLEVEL | Not converted | Not applicable | 7917: PostgreSQL doesn't support the GEOMETRY.MINDBCOMPATIBILITYLEVEL function | 
| GEOMETRY.NULL | Renamed | null::GEOMETRY | None | 
| GEOMETRY.PARSE | Rewritten | ST\_GeomFromText(⟨p\_text⟩, 0) | None | 
| GEOMETRY.POINT | Rewritten | ST\_SetSRID(ST\_Point(⟨p1⟩, ⟨p2⟩), ⟨p3⟩) | None | 
| GEOMETRY.REDUCE | Rewritten | ST\_Simplify(⟨spat⟩, ⟨par1⟩) | None | 
| GEOMETRY.SHORTESTLINETO | Rewritten | ST\_ShortestLine(⟨spat⟩, ⟨par1⟩) | None | 
| GEOMETRY.STASBINARY | Rewritten | ST\_AsBinary(⟨spat⟩) | None | 
| GEOMETRY.STASTEXT | Rewritten | ST\_AsText(⟨spat⟩) | None | 
| GEOMETRY.STBOUNDARY | Rewritten | ST\_Boundary(⟨spat⟩) | None | 
| GEOMETRY.STBUFFER | Rewritten | ST\_Buffer(⟨spat⟩, ⟨par1⟩) | None | 
| GEOMETRY.STCENTROID | Rewritten | ST\_Centroid(⟨spat⟩) | None | 
| GEOMETRY.STCONTAINS | Rewritten | (case ST\_Contains(⟨spat⟩, ⟨par1⟩) when true then 1 when false then 0 else null end)::NUMERIC(1) | None | 
| GEOMETRY.STCONVEXHULL | Rewritten | ST\_ConvexHull(⟨spat⟩) | None | 
| GEOMETRY.STCROSSES | Rewritten | (case ST\_Crosses(⟨spat⟩, ⟨par1⟩) when true then 1 when false then 0 else null end)::NUMERIC(1) | None | 
| GEOMETRY.STCURVEN | Not converted | Not applicable | 7917: PostgreSQL doesn't support the GEOMETRY.STCURVEN function | 
| GEOMETRY.STCURVETOLINE | Rewritten | ST\_CurveToLine(⟨spat⟩) | None | 
| GEOMETRY.STDIFFERENCE | Rewritten | ST\_Difference(⟨spat⟩, ⟨par1⟩) | None | 
| GEOMETRY.STDIMENSION | Rewritten | (case ST\_IsEmpty(⟨spat⟩) when true then -1 else ST\_Dimension(⟨spat⟩) end)::numeric(10) | None | 
| GEOMETRY.STDISJOINT | Rewritten | (case ST\_Disjoint(⟨spat⟩, ⟨par1⟩) when true then 1 when false then 0 else null end)::NUMERIC(1) | None | 
| GEOMETRY.STDISTANCE | Rewritten | ST\_Distance(⟨spat⟩, ⟨par1⟩)::DOUBLE PRECISION | None | 
| GEOMETRY.STENDPOINT | Not converted | Not applicable | 7917: PostgreSQL doesn't support the GEOMETRY.STENDPOINT function | 
| GEOMETRY.STENVELOPE | Rewritten | ST\_Envelope(⟨spat⟩) | None | 
| GEOMETRY.STEQUALS | Rewritten | (case ST\_Equals(⟨spat⟩, ⟨par1⟩) when true then 1 when false then 0 else null end)::NUMERIC(1) | None | 
| GEOMETRY.STEXTERIORRING | Rewritten | ST\_Exteriorring(⟨spat⟩) | None | 
| GEOMETRY.STGEOMCOLLFROMTEXT | Rewritten | ST\_GeomCollFromText(⟨p1⟩, ⟨p2⟩) | None | 
| GEOMETRY.STGEOMCOLLFROMWKB | Rewritten | ST\_GeomCollFromWKB(⟨p1⟩, ⟨p2⟩) | None | 
| GEOMETRY.STGEOMETRYN | Rewritten | ST\_geometryN(⟨spat⟩, ⟨par1⟩::numeric(10)) | None | 
| GEOMETRY.STGEOMETRYTYPE | Rewritten | geometryType(⟨spat⟩)::varchar(4000) | None | 
| GEOMETRY.STGEOMFROMTEXT | Rewritten | ST\_GeomFromText(⟨p1⟩, ⟨p2⟩) | None | 
| GEOMETRY.STGEOMFROMWKB | Rewritten | ST\_GeomFromWKB(⟨p1⟩, ⟨p2⟩) | None | 
| GEOMETRY.STINTERIORRINGN | Rewritten | ST\_InteriorRingN(⟨spat⟩, ⟨par1⟩::numeric(10)) | None | 
| GEOMETRY.STINTERSECTION | Rewritten | ST\_Intersection(⟨spat⟩, ⟨par1⟩) | None | 
| GEOMETRY.STINTERSECTS | Rewritten | (case ST\_Intersects(⟨spat⟩, ⟨par1⟩) when true then 1 when false then 0 else null end)::NUMERIC(1) | None | 
| GEOMETRY.STISCLOSED | Rewritten | (case (case when geometryAType(⟨spat⟩) like '%POINT%' then false else ST\_IsClosed(⟨spat⟩) end) when false then 0 when true then 1 else null end)::NUMERIC(1) | None | 
| GEOMETRY.STISEMPTY | Rewritten | (case ST\_IsEmpty(⟨spat⟩) when true then 1 when false then 0 else null end)::numeric(10) | None | 
| GEOMETRY.STISRING | Rewritten | (case ST\_IsRing(⟨spat⟩) when true then 1 when false then 0 else null end)::NUMERIC(1) | None | 
| GEOMETRY.STISSIMPLE | Rewritten | (case ST\_IsSimple(⟨spat⟩) when true then 1 when false then 0 else null end)::NUMERIC(1) | None | 
| GEOMETRY.STISVALID | Rewritten | (case ST\_Valid(⟨spat⟩) when true then 1 when false then 0 else null end)::NUMERIC(1) | None | 
| GEOMETRY.STLENGTH | Rewritten | ST\_Length(⟨spat⟩)::DOUBLE PRECISION | None | 
| GEOMETRY.STLINEFROMTEXT | Rewritten | ST\_LineFromText(⟨p1⟩, ⟨p2⟩) | None | 
| GEOMETRY.STLINEFROMWKB | Rewritten | ST\_LineFromWKB(⟨p1⟩, ⟨p2⟩) | None | 
| GEOMETRY.STMLINEFROMTEXT | Rewritten | ST\_MLineFromText(⟨p1⟩, ⟨p2⟩) | None | 
| GEOMETRY.STMLINEFROMWKB | Rewritten | case when geometryType(ST\_GeomFromWKB(⟨par1⟩, ⟨par2⟩))\!='MULTILINESTRING' then null else ST\_GeomFromWKB(⟨par1⟩, ⟨par2⟩) end | None | 
| GEOMETRY.STMPOINTFROMTEXT | Rewritten | ST\_MPointFromText(⟨p1⟩, ⟨p2⟩) | None | 
| GEOMETRY.STMPOINTFROMWKB | Rewritten | ST\_MPointFromWKB(⟨p1⟩, ⟨p2⟩) | None | 
| GEOMETRY.STMPOLYFROMTEXT | Rewritten | ST\_MPolyFromText(⟨p1⟩, ⟨p2⟩) | None | 
| GEOMETRY.STMPOLYFROMWKB | Rewritten | ST\_MPolyFromWKB(⟨p1⟩, ⟨p2⟩) | None | 
| GEOMETRY.STNUMCURVES | Not converted | Not applicable | 7917: PostgreSQL doesn't support the GEOMETRY.STNUMCURVES function | 
| GEOMETRY.STNUMGEOMETRIES | Rewritten | ST\_NumGeometries(⟨spat⟩)::numeric(10) | None | 
| GEOMETRY.STNUMINTERIORRING | Rewritten | ST\_NumInteriorRings(⟨spat⟩)::numeric(10) | None | 
| GEOMETRY.STNUMPOINTS | Not converted | Not applicable | 7917: PostgreSQL doesn't support the GEOMETRY.STNUMPOINTS function | 
| GEOMETRY.STOVERLAPS | Rewritten | (case ST\_Overlaps(⟨spat⟩, ⟨par1⟩) when true then 1 when false then 0 else null end)::NUMERIC(1) | None | 
| GEOMETRY.STPOINTN | Not converted | Not applicable | 7917: PostgreSQL doesn't support the GEOMETRY.STPOINTN function | 
| GEOMETRY.STPOINTONSURFACE | Rewritten | ST\_PointOnSurface(⟨spat⟩) | None | 
| GEOMETRY.STRELATE | Rewritten | (case ST\_Relate(⟨spat⟩, ⟨par1⟩, ⟨par2⟩) when true then 1 when false then 0 else null end)::NUMERIC(1) | None | 
| GEOMETRY.STSRID | Rewritten | ST\_Srid(⟨spat⟩)::numeric(10) | None | 
| GEOMETRY.STSTARTPOINT | Rewritten | ST\_Startpoint(⟨spat⟩) | None | 
| GEOMETRY.STSYMDIFFERENCE | Rewritten | ST\_SymDifference(⟨spat⟩, ⟨par1⟩) | None | 
| GEOMETRY.STTOUCHES | Rewritten | (case ST\_Touches(⟨spat⟩, ⟨par1⟩) when true then 1 when false then 0 else null end)::NUMERIC(1) | None | 
| GEOMETRY.STUNION | Rewritten | ST\_union(⟨spat⟩, ⟨par1⟩) | None | 
| GEOMETRY.STWITHIN | Rewritten | (case ST\_Within(⟨spat⟩, ⟨par1⟩) when true then 1 when false then 0 else null end)::NUMERIC(1) | None | 
| GEOMETRY.STX | Rewritten | ST\_X(case when geometryType(⟨spat⟩) \!='POINT' then null else ⟨spat⟩ end)::DOUBLE PRECISION | None | 
| GEOMETRY.STY | Rewritten | ST\_Y(case when geometryType(⟨spat⟩) \!='POINT' then null else ⟨spat⟩ end)::DOUBLE PRECISION | None | 
| GEOMETRY.TOSTRING | Rewritten | ST\_AsText(⟨spat⟩) | None | 
| GEOMETRY.UNIONAGGREGATE | Rewritten | ST\_Union(⟨p1⟩) | None | 
| GEOMETRY.Z | Rewritten | ST\_Z(case when geometryAType(⟨spat⟩)\!='POINT' then null else ⟨spat⟩ end)::DOUBLE PRECISION | None | 

## System functions
<a name="sc-default-rules-builtins-sqlserver-system-functions"></a>

The following table lists each source object in the System functions category and shows how DMS Schema Conversion converts it.


| Source | Conversion | Target | Action item | 
| --- | --- | --- | --- | 
| @@ERROR in IF @@ERROR <> 0 whose body commits or rolls back | Rewritten | The IF statement is replaced by PL/pgSQL exception handling; the @@ERROR test itself disappears | None | 
| @@ERROR in any other position | Not converted | Not applicable | 7811: PostgreSQL doesn't support the @@ERROR function. DMS SC skips this unsupported function in the converted code | 
| @@IDENTITY | Rewritten | LASTVAL() | None | 
| @@ROWCOUNT after a SELECT used in an IF or PRINT | Rewritten | sql$rowcount | 7834: Converted code of the @@rowcount function might produce different results compared to the source code | 
| @@ROWCOUNT after an INSERT, UPDATE or DELETE | Rewritten | sql$rowcount, set by a GET DIAGNOSTICS sql$rowcount = ROW\_COUNT; statement added before the reference | 7834: Converted code of the @@rowcount function might produce different results compared to the source code | 
| @@ROWCOUNT in any other position | Not converted | Not applicable | 7833: DMS SC can't convert the @@rowcount function in the current context | 
| @@TRANCOUNT | Not converted | Not applicable | 7811: PostgreSQL doesn't support the @@TRANCOUNT function. DMS SC skips this unsupported function in the converted code | 
| CONTEXT\_INFO | Not converted | Not applicable | 7811: PostgreSQL doesn't support the CONTEXT\_INFO function. DMS SC skips this unsupported function in the converted code | 
| EDGE\_ID\_FROM\_PARTS | Not converted | Not applicable | 7933: DMS SC can't convert the EDGE\_ID\_FROM\_PARTS system function of the SQL Graph database | 
| GRAPH\_ID\_FROM\_EDGE\_ID | Not converted | Not applicable | 7933: DMS SC can't convert the GRAPH\_ID\_FROM\_EDGE\_ID system function of the SQL Graph database | 
| GRAPH\_ID\_FROM\_NODE\_ID | Not converted | Not applicable | 7933: DMS SC can't convert the GRAPH\_ID\_FROM\_NODE\_ID system function of the SQL Graph database | 
| NODE\_ID\_FROM\_PARTS | Not converted | Not applicable | 7933: DMS SC can't convert the NODE\_ID\_FROM\_PARTS system function of the SQL Graph database | 
| OBJECT\_ID\_FROM\_EDGE\_ID | Not converted | Not applicable | 7933: DMS SC can't convert the OBJECT\_ID\_FROM\_EDGE\_ID system function of the SQL Graph database | 
| OBJECT\_ID\_FROM\_NODE\_ID | Not converted | Not applicable | 7933: DMS SC can't convert the OBJECT\_ID\_FROM\_NODE\_ID system function of the SQL Graph database | 

## System objects views
<a name="sc-default-rules-builtins-sqlserver-system-objects-views"></a>

The following table lists each source object in the System objects views category and shows how DMS Schema Conversion converts it.


| Source | Conversion | Target | Action item | 
| --- | --- | --- | --- | 
| INFORMATION\_SCHEMA.CHECK\_CONSTRAINTS | Renamed | INFORMATION\_SCHEMA.CHECK\_CONSTRAINTS | None | 
| INFORMATION\_SCHEMA.COLUMNS | Extension pack | aws\_sqlserver\_ext.INFORMATION\_SCHEMA\_COLUMNS | None | 
| INFORMATION\_SCHEMA.CONSTRAINT\_COLUMN\_USAGE | Renamed | INFORMATION\_SCHEMA.CONSTRAINT\_COLUMN\_USAGE | None | 
| INFORMATION\_SCHEMA.CONSTRAINT\_TABLE\_USAGE | Renamed | INFORMATION\_SCHEMA.CONSTRAINT\_TABLE\_USAGE | None | 
| INFORMATION\_SCHEMA.KEY\_COLUMN\_USAGE | Extension pack | aws\_sqlserver\_ext.INFORMATION\_SCHEMA\_KEY\_COLUMN\_USAGE | None | 
| INFORMATION\_SCHEMA.REFERENTIAL\_CONSTRAINTS | Extension pack | aws\_sqlserver\_ext.INFORMATION\_SCHEMA\_REFERENTIAL\_CONSTRAINTS | None | 
| INFORMATION\_SCHEMA.ROUTINES | Extension pack | aws\_sqlserver\_ext.INFORMATION\_SCHEMA\_ROUTINES | None | 
| INFORMATION\_SCHEMA.SCHEMATA | Extension pack | aws\_sqlserver\_ext.INFORMATION\_SCHEMA\_SCHEMATA | None | 
| INFORMATION\_SCHEMA.TABLES | Extension pack | aws\_sqlserver\_ext.INFORMATION\_SCHEMA\_TABLES | None | 
| INFORMATION\_SCHEMA.TABLE\_CONSTRAINTS | Extension pack | aws\_sqlserver\_ext.INFORMATION\_SCHEMA\_TABLE\_CONSTRAINTS | None | 
| INFORMATION\_SCHEMA.VIEWS | Extension pack | aws\_sqlserver\_ext.INFORMATION\_SCHEMA\_VIEWS | None | 
| SYS.ALL\_COLUMNS | Extension pack | aws\_sqlserver\_ext.SYS\_ALL\_COLUMNS | None | 
| SYS.ALL\_OBJECTS | Extension pack | aws\_sqlserver\_ext.SYS\_ALL\_OBJECTS | None | 
| SYS.ALL\_VIEWS | Extension pack | aws\_sqlserver\_ext.SYS\_ALL\_VIEWS | None | 
| SYS.COLUMNS | Extension pack | aws\_sqlserver\_ext.SYS\_COLUMNS | None | 
| SYS.DATABASES | Extension pack | aws\_sqlserver\_ext.SYS\_DATABASES | None | 
| SYS.FOREIGN\_KEYS | Extension pack | aws\_sqlserver\_ext.SYS\_FOREIGN\_KEYS | None | 
| SYS.FOREIGN\_KEY\_COLUMNS | Extension pack | aws\_sqlserver\_ext.SYS\_FOREIGN\_KEY\_COLUMNS | None | 
| SYS.IDENTITY\_COLUMNS | Extension pack | aws\_sqlserver\_ext.SYS\_IDENTITY\_COLUMNS | None | 
| SYS.INDEXES | Extension pack | aws\_sqlserver\_ext.SYS\_INDEXES | None | 
| SYS.KEY\_CONSTRAINTS | Extension pack | aws\_sqlserver\_ext.SYS\_KEY\_CONSTRAINTS | None | 
| SYS.OBJECTS | Extension pack | aws\_sqlserver\_ext.SYS\_OBJECTS | None | 
| SYS.PROCEDURES | Extension pack | aws\_sqlserver\_ext.SYS\_PROCEDURES | None | 
| SYS.SCHEMAS | Extension pack | aws\_sqlserver\_ext.SYS\_SCHEMAS | None | 
| SYS.SP\_SEQUENCE\_GET\_RANGE | Extension pack | aws\_sqlserver\_ext.sp\_sequence\_get\_range(⟨seq\_name⟩, ⟨seq\_range⟩) | None | 
| SYS.SQL\_MODULES | Extension pack | aws\_sqlserver\_ext.SYS\_SQL\_MODULES | None | 
| SYS.SYSFOREIGNKEYS | Extension pack | aws\_sqlserver\_ext.SYS\_SYSFOREIGNKEYS | None | 
| SYS.SYSINDEXES | Extension pack | aws\_sqlserver\_ext.SYS\_SYSINDEXES | None | 
| SYS.SYSOBJECTS | Extension pack | aws\_sqlserver\_ext.SYS\_SYSOBJECTS | None | 
| SYS.SYSPROCESSES | Extension pack | aws\_sqlserver\_ext.SYS\_SYSPROCESSES | None | 
| SYS.SYSTEM\_OBJECTS | Extension pack | aws\_sqlserver\_ext.SYS\_SYSTEM\_OBJECTS | None | 
| SYS.TABLES | Extension pack | aws\_sqlserver\_ext.SYS\_TABLES | None | 
| SYS.TYPES | Extension pack | aws\_sqlserver\_ext.SYS\_TYPES | None | 
| SYS.VIEWS | Extension pack | aws\_sqlserver\_ext.SYS\_VIEWS | None | 

## System state
<a name="sc-default-rules-builtins-sqlserver-system-state"></a>

In the System state category, DMS Schema Conversion does not automatically convert any source objects. You must convert these objects manually. The following table lists these source objects.


| Source | Conversion | Target | Action item | 
| --- | --- | --- | --- | 
| MSDB.DBO.SYSMAIL\_HELP\_STATUS\_SP | Not converted | Not applicable | 7900: PostgreSQL doesn't support functionality similar to SQL Server Database Mail | 
| MSDB.DBO.SYSMAIL\_START\_SP | Not converted | Not applicable | 7900: PostgreSQL doesn't support functionality similar to SQL Server Database Mail | 
| MSDB.DBO.SYSMAIL\_STOP\_SP | Not converted | Not applicable | 7900: PostgreSQL doesn't support functionality similar to SQL Server Database Mail | 

## System statistical functions
<a name="sc-default-rules-builtins-sqlserver-system-statistical-functions"></a>

In the System statistical functions category, DMS Schema Conversion does not automatically convert any source objects. You must convert these objects manually. The following table lists these source objects.


| Source | Conversion | Target | Action item | 
| --- | --- | --- | --- | 
| @@CONNECTIONS | Not converted | Not applicable | 7811: PostgreSQL doesn't support the @@CONNECTIONS function. DMS SC skips this unsupported function in the converted code | 
| @@CPU\_BUSY | Not converted | Not applicable | 7811: PostgreSQL doesn't support the @@CPU\_BUSY function. DMS SC skips this unsupported function in the converted code | 
| @@IDLE | Not converted | Not applicable | 7811: PostgreSQL doesn't support the @@IDLE function. DMS SC skips this unsupported function in the converted code | 
| @@IO\_BUSY | Not converted | Not applicable | 7811: PostgreSQL doesn't support the @@IO\_BUSY function. DMS SC skips this unsupported function in the converted code | 
| @@PACKET\_ERRORS | Not converted | Not applicable | 7811: PostgreSQL doesn't support the @@PACKET\_ERRORS function. DMS SC skips this unsupported function in the converted code | 
| @@PACK\_RECEIVED | Not converted | Not applicable | 7811: PostgreSQL doesn't support the @@PACK\_RECEIVED function. DMS SC skips this unsupported function in the converted code | 
| @@PACK\_SENT | Not converted | Not applicable | 7811: PostgreSQL doesn't support the @@PACK\_SENT function. DMS SC skips this unsupported function in the converted code | 
| @@TIMETICKS | Not converted | Not applicable | 7811: PostgreSQL doesn't support the @@TIMETICKS function. DMS SC skips this unsupported function in the converted code | 
| @@TOTAL\_ERRORS | Not converted | Not applicable | 7811: PostgreSQL doesn't support the @@TOTAL\_ERRORS function. DMS SC skips this unsupported function in the converted code | 
| @@TOTAL\_READ | Not converted | Not applicable | 7811: PostgreSQL doesn't support the @@TOTAL\_READ function. DMS SC skips this unsupported function in the converted code | 
| @@TOTAL\_WRITE | Not converted | Not applicable | 7811: PostgreSQL doesn't support the @@TOTAL\_WRITE function. DMS SC skips this unsupported function in the converted code | 

## System procedures
<a name="sc-default-rules-builtins-sqlserver-system-procedures"></a>

The following table lists each source object in the System procedures category and shows how DMS Schema Conversion converts it.


| Source | Conversion | Target | Action item | 
| --- | --- | --- | --- | 
| SYS.SP\_EXECUTE | Not converted | Not applicable | 7672: PostgreSQL doesn't support EXECUTE statements that run a character string | 
| SYS.SP\_PREPARE | Not converted | Not applicable | 7672: PostgreSQL doesn't support EXECUTE statements that run a character string | 
| SYS.SP\_PREPEXEC | Not converted | Not applicable | 7672: PostgreSQL doesn't support EXECUTE statements that run a character string | 
| SYS.SP\_UNPREPARE | Not converted | Not applicable | 7672: PostgreSQL doesn't support EXECUTE statements that run a character string | 
| SYS.SP\_XML\_PREPAREDOCUMENT | Extension pack | aws\_sqlserver\_ext.sp\_xml\_preparedocument(⟨arg⟩) | None | 
| SYS.SP\_XML\_REMOVEDOCUMENT | Extension pack | aws\_sqlserver\_ext.sp\_xml\_removedocument | None | 

## XML
<a name="sc-default-rules-builtins-sqlserver-xml"></a>

In the XML category, DMS Schema Conversion does not automatically convert any source objects. You must convert these objects manually. The following table lists these source objects.


| Source | Conversion | Target | Action item | 
| --- | --- | --- | --- | 
| XML.EXIST | Not converted | Not applicable | 7708: DMS SC can't convert the usage of the unsupported XML.EXIST data type | 
| XML.MODIFY | Not converted | Not applicable | 7708: DMS SC can't convert the usage of the unsupported XML.MODIFY data type | 
| XML.NODES | Not converted | Not applicable | 7708: DMS SC can't convert the usage of the unsupported XML.NODES data type | 
| XML.QUERY | Not converted | Not applicable | 7708: DMS SC can't convert the usage of the unsupported XML.QUERY data type | 
| XML.VALUE | Not converted | Not applicable | 7708: DMS SC can't convert the usage of the unsupported XML.VALUE data type | 