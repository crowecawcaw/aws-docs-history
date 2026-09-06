

For similar capabilities to Amazon Timestream for LiveAnalytics, consider Amazon Timestream for InfluxDB. It offers simplified data ingestion and single-digit millisecond query response times for real-time analytics. Learn more [here](https://docs.aws.amazon.com/timestream/latest/developerguide/timestream-for-influxdb.html).

# Date / time functions
<a name="date-time-functions"></a>

**Note**  
Timestream for LiveAnalytics does not support negative time values. Any operation resulting in negative time results in error.

Timestream for LiveAnalytics uses UTC timezone for date and time. Timestream supports the following functions for date and time.

**Topics**
+ [General and conversion](#date-time-functions-general)
+ [Interval and duration](#date-time-functions-interval-duration)
+ [Formatting and parsing](#date-time-functions-formatting-parsing)
+ [Extraction](#date-time-functions-extraction)

## General and conversion
<a name="date-time-functions-general"></a>

Timestream for LiveAnalytics supports the following general and conversion functions for date and time.


| Function | Output data type | Description | 
| --- | --- | --- | 
| current\_date | date | Returns current date in UTC. No parentheses used.<pre>SELECT current_date</pre><br />Example result: `2022-07-07` This is also a reserved keyword. For a list of reserved keywords, see [Reserved keywords](ts-limits.md#limits.reserved).  | 
| current\_time | time | Returns current time in UTC. No parentheses used.<pre>SELECT current_time</pre><br />Example result: `17:41:52.827000000` This is also a reserved keyword. For a list of reserved keywords, see [Reserved keywords](ts-limits.md#limits.reserved).  | 
| current\_timestamp or now() | timestamp | Returns current timestamp in UTC.<pre>SELECT current_timestamp</pre><br />Example result: `2022-07-07 17:42:32.939000000` This is also a reserved keyword. For a list of reserved keywords, see [Reserved keywords](ts-limits.md#limits.reserved).  | 
| current\_timezone() | varchar<br />The value will be 'UTC.' | Timestream uses UTC timezone for date and time.<pre>SELECT current_timezone()</pre><br />Example result: `UTC` | 
| date(varchar(x)), date(timestamp) | date | <pre>SELECT date(TIMESTAMP '2022-07-07 17:44:43.771000000')</pre>Example result: `2022-07-07` | 
| last\_day\_of\_month(timestamp), last\_day\_of\_month(date) | date | <pre>SELECT last_day_of_month(TIMESTAMP '2022-07-07 17:44:43.771000000')</pre>Example result: `2022-07-31` | 
| from\_iso8601\_timestamp(string) | timestamp | Parses the ISO 8601 timestamp into internal timestamp format.<pre>SELECT from_iso8601_timestamp('2022-06-17T08:04:05.000000000+05:00')</pre><br />Example result: `2022-06-17 03:04:05.000000000` | 
| from\_iso8601\_date(string) | date | Parses the ISO 8601 date string into internal timestamp format for UTC 00:00:00 of the specified date.<pre>SELECT from_iso8601_date('2022-07-17')</pre><br />Example result: `2022-07-17` | 
| to\_iso8601(timestamp), to\_iso8601(date) | varchar | Returns an ISO 8601 formatted string for the input.<pre>SELECT to_iso8601(from_iso8601_date('2022-06-17'))</pre><br />Example result: `2022-06-17` | 
| from\_milliseconds(bigint) | timestamp | <pre>SELECT from_milliseconds(1)</pre>Example result: `1970-01-01 00:00:00.001000000` | 
| from\_nanoseconds(bigint) | timestamp | <pre>select from_nanoseconds(300000001)</pre>Example result: `1970-01-01 00:00:00.300000001` | 
| from\_unixtime(double) | timestamp | Returns a timestamp which corresponds to the provided unixtime.<pre>SELECT from_unixtime(1)</pre><br />Example result: `1970-01-01 00:00:01.000000000` | 
| localtime | time | Returns current time in UTC. No parentheses used.<pre>SELECT localtime</pre><br />Example result: `17:58:22.654000000` This is also a reserved keyword. For a list of reserved keywords, see [Reserved keywords](ts-limits.md#limits.reserved).  | 
| localtimestamp | timestamp | Returns current timestamp in UTC. No parentheses used.<pre>SELECT localtimestamp</pre><br />Example result: `2022-07-07 17:59:04.368000000` This is also a reserved keyword. For a list of reserved keywords, see [Reserved keywords](ts-limits.md#limits.reserved).  | 
| to\_milliseconds(interval day to second), to\_milliseconds(timestamp) | bigint | <pre>SELECT to_milliseconds(INTERVAL '2' DAY + INTERVAL '3' HOUR)</pre>Example result: `183600000`<pre>SELECT to_milliseconds(TIMESTAMP '2022-06-17 17:44:43.771000000')</pre><br />Example result: `1655487883771` | 
| to\_nanoseconds(interval day to second), to\_nanoseconds(timestamp) | bigint | <pre>SELECT to_nanoseconds(INTERVAL '2' DAY + INTERVAL '3' HOUR)</pre>Example result: `183600000000000`<pre>SELECT to_nanoseconds(TIMESTAMP '2022-06-17 17:44:43.771000678')</pre><br />Example result: `1655487883771000678` | 
| to\_unixtime(timestamp) | double | Returns unixtime for the provided timestamp.<pre>SELECT to_unixtime('2022-06-17 17:44:43.771000000')</pre><br />Example result: `1.6554878837710001E9` | 
| date\_trunc(unit, timestamp) | timestamp | Returns the timestamp truncated to unit, where unit is one of [second, minute, hour, day, week, month, quarter, or year].<pre>SELECT date_trunc('minute', TIMESTAMP '2022-06-17 17:44:43.771000000')</pre><br />Example result: `2022-06-17 17:44:00.000000000` | 

## Interval and duration
<a name="date-time-functions-interval-duration"></a>

Timestream for LiveAnalytics supports the following interval and duration functions for date and time.


| Function | Output data type | Description | 
| --- | --- | --- | 
| date\_add(unit, bigint, date), date\_add(unit, bigint, time), date\_add(varchar(x), bigint, timestamp) | timestamp | Adds a bigint of units, where unit is one of [second, minute, hour, day, week, month, quarter, or year].<pre>SELECT date_add('hour', 9, TIMESTAMP '2022-06-17 00:00:00')</pre><br />Example result: `2022-06-17 09:00:00.000000000` | 
| date\_diff(unit, date, date) , date\_diff(unit, time, time) , date\_diff(unit, timestamp, timestamp) | bigint | Returns a difference, where unit is one of [second, minute, hour, day, week, month, quarter, or year].<pre>SELECT date_diff('day', DATE '2020-03-01', DATE '2020-03-02')</pre><br />Example result: `1` | 
| parse\_duration(string) | interval | Parses the input string to return an `interval` equivalent.<pre>SELECT parse_duration('42.8ms')</pre><br />Example result: `0 00:00:00.042800000`<pre>SELECT typeof(parse_duration('42.8ms'))</pre><br />Example result: `interval day to second` | 
| bin(timestamp, interval) | timestamp | Rounds down the `timestamp` parameter's integer value to the nearest multiple of the `interval` parameter's integer value.<br />The meaning of this return value may not be obvious. It is calculated using integer arithmetic first by dividing the timestamp integer by the interval integer and then by multiplying the result by the interval integer.<br />Keeping in mind that a timestamp specifies a UTC point in time as a number of fractions of a second elapsed since the POSIX epoch (January 1, 1970), the return value will seldom align with calendar units. For example, if you specify an interval of 30 days, all the days since the epoch are divided into 30-day increments, and the start of the most recent 30-day increment is returned, which has no relationship to calendar months.<br />Here are some examples:<pre>bin(TIMESTAMP '2022-06-17 10:15:20', 5m)     ==> 2022-06-17 10:15:00.000000000<br />bin(TIMESTAMP '2022-06-17 10:15:20', 1d)     ==> 2022-06-17 00:00:00.000000000<br />bin(TIMESTAMP '2022-06-17 10:15:20', 10day)  ==> 2022-06-17 00:00:00.000000000<br />bin(TIMESTAMP '2022-06-17 10:15:20', 30day)  ==> 2022-05-28 00:00:00.000000000</pre> | 
| ago(interval) | timestamp | Returns the value corresponding to current\_timestamp `interval`.<pre>SELECT ago(1d)</pre><br />Example result: `2022-07-06 21:08:53.245000000` | 
| interval literals such as 1h, 1d, and 30m | interval | Interval literals are a convenience for parse\_duration(string). For example, `1d` is the same as `parse_duration('1d')`. This allows the use of the literals wherever an interval is used. For example, `ago(1d)` and `bin({{<timestamp>}}, 1m)`. | 

Some interval literals act as shorthand for parse\_duration. For example, `parse_duration('1day')`, `1day`, `parse_duration('1d')`, and `1d` each return `1 00:00:00.000000000` where the type is `interval day to second`. Space is allowed in the format provided to `parse_duration`. For example `parse_duration('1day')` also returns `00:00:00.000000000`. But `1 day` is not an interval literal.

The units related to `interval day to second` are ns, nanosecond, us, microsecond, ms, millisecond, s, second, m, minute, h, hour, d, and day.

There is also `interval year to month`. The units related to interval year to month are y, year, and month. For example, `SELECT 1year` returns `1-0`. `SELECT 12month` also returns `1-0`. `SELECT 8month` returns `0-8`.

Although the unit of `quarter` is also available for some functions such as `date_trunc` and `date_add`, `quarter` is not available as part of an interval literal.

## Formatting and parsing
<a name="date-time-functions-formatting-parsing"></a>

Timestream for LiveAnalytics supports the following formatting and parsing functions for date and time.


| Function | Output data type | Description | 
| --- | --- | --- | 
| date\_format(timestamp, varchar(x)) | varchar | For more information about the format specifiers used by this function, see [https://trino.io/docs/current/functions/datetime.html\#mysql-date-functions](https://trino.io/docs/current/functions/datetime.html#mysql-date-functions)<pre>SELECT date_format(TIMESTAMP '2019-10-20 10:20:20', '%Y-%m-%d %H:%i:%s')</pre><br />Example result: `2019-10-20 10:20:20` | 
| date\_parse(varchar(x), varchar(y)) | timestamp | For more information about the format specifiers used by this function, see [https://trino.io/docs/current/functions/datetime.html\#mysql-date-functions](https://trino.io/docs/current/functions/datetime.html#mysql-date-functions)<pre>SELECT date_parse('2019-10-20 10:20:20', '%Y-%m-%d %H:%i:%s')</pre><br />Example result: `2019-10-20 10:20:20.000000000` | 
| format\_datetime(timestamp, varchar(x)) | varchar | For more information about the format string used by this function, see [http://joda-time.sourceforge.net/apidocs/org/joda/time/format/DateTimeFormat.html](http://joda-time.sourceforge.net/apidocs/org/joda/time/format/DateTimeFormat.html)<pre>SELECT format_datetime(parse_datetime('1968-01-13 12', 'yyyy-MM-dd HH'), 'yyyy-MM-dd HH')</pre><br />Example result: `1968-01-13 12` | 
| parse\_datetime(varchar(x), varchar(y)) | timestamp | For more information about the format string used by this function, see [http://joda-time.sourceforge.net/apidocs/org/joda/time/format/DateTimeFormat.html](http://joda-time.sourceforge.net/apidocs/org/joda/time/format/DateTimeFormat.html)<pre>SELECT parse_datetime('2019-12-29 10:10 PST', 'uuuu-LL-dd HH:mm z')</pre><br />Example result: `2019-12-29 18:10:00.000000000` | 

## Extraction
<a name="date-time-functions-extraction"></a>

Timestream for LiveAnalytics supports the following extraction functions for date and time. The extract function is the basis for the remaining convenience functions.


| Function | Output data type | Description | 
| --- | --- | --- | 
| extract | bigint | Extracts a field from a timestamp, where field is one of [YEAR, QUARTER, MONTH, WEEK, DAY, DAY\_OF\_MONTH, DAY\_OF\_WEEK, DOW, DAY\_OF\_YEAR, DOY, YEAR\_OF\_WEEK, YOW, HOUR, MINUTE, or SECOND].<pre>SELECT extract(YEAR FROM '2019-10-12 23:10:34.000000000')</pre><br />Example result: `2019` | 
| day(timestamp), day(date), day(interval day to second) | bigint | <pre>SELECT day('2019-10-12 23:10:34.000000000')</pre>Example result: `12` | 
| day\_of\_month(timestamp), day\_of\_month(date), day\_of\_month(interval day to second) | bigint | <pre>SELECT day_of_month('2019-10-12 23:10:34.000000000')</pre>Example result: `12` | 
| day\_of\_week(timestamp), day\_of\_week(date) | bigint | <pre>SELECT day_of_week('2019-10-12 23:10:34.000000000')</pre>Example result: `6` | 
| day\_of\_year(timestamp), day\_of\_year(date) | bigint | <pre>SELECT day_of_year('2019-10-12 23:10:34.000000000')</pre>Example result: `285` | 
| dow(timestamp), dow(date) | bigint | Alias for day\_of\_week | 
| doy(timestamp), doy(date) | bigint | Alias for day\_of\_year | 
| hour(timestamp), hour(time), hour(interval day to second) | bigint | <pre>SELECT hour('2019-10-12 23:10:34.000000000')</pre>Example result: `23` | 
| millisecond(timestamp), millisecond(time), millisecond(interval day to second) | bigint | <pre>SELECT millisecond('2019-10-12 23:10:34.000000000')</pre>Example result: `0` | 
| minute(timestamp), minute(time), minute(interval day to second) | bigint | <pre>SELECT minute('2019-10-12 23:10:34.000000000')</pre>Example result: `10` | 
| month(timestamp), month(date), month(interval year to month) | bigint | <pre>SELECT month('2019-10-12 23:10:34.000000000')</pre>Example result: `10` | 
| nanosecond(timestamp), nanosecond(time), nanosecond(interval day to second) | bigint | <pre>SELECT nanosecond(current_timestamp)</pre>Example result: `162000000` | 
| quarter(timestamp), quarter(date) | bigint | <pre>SELECT quarter('2019-10-12 23:10:34.000000000')</pre>Example result: `4` | 
| second(timestamp), second(time), second(interval day to second) | bigint | <pre>SELECT second('2019-10-12 23:10:34.000000000')</pre>Example result: `34` | 
| week(timestamp), week(date) | bigint | <pre>SELECT week('2019-10-12 23:10:34.000000000')</pre>Example result: `41` | 
| week\_of\_year(timestamp), week\_of\_year(date) | bigint | Alias for week | 
| year(timestamp), year(date), year(interval year to month) | bigint | <pre>SELECT year('2019-10-12 23:10:34.000000000')</pre>Example result: `2019` | 
| year\_of\_week(timestamp), year\_of\_week(date) | bigint | <pre>SELECT year_of_week('2019-10-12 23:10:34.000000000')</pre>Example result: `2019` | 
| yow(timestamp), yow(date) | bigint | Alias for year\_of\_week | 