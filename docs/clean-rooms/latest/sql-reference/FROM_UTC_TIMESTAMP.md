# FROM_UTC_TIMESTAMP function

The FROM_UTC_TIMESTAMP function converts the input date from UTC (Coordinated Universal
Time) to the specified time zone.

This function is useful when you need to convert date and time values from UTC to a
specific time zone. This can be important when working with data that originates from
different parts of the world and needs to be presented in the appropriate local
time.

## Syntax

```
from_utc_timestamp(timestamp, timezone
```

## Arguments

_timestamp_

A TIMESTAMP expression with a UTC timestamp.

_timezone_

A STRING expression that is a valid timezone to which the input date or
timestamp should be converted.

## Returns

The FROM_UTC_TIMESTAMP function returns a TIMESTAMP.

## Example

The following example converts the input date from UTC to the specified time zone
(`'Asia/Seoul'`), which in this case is 9 hours ahead of UTC. The
resulting output is the date and time in the Seoul time zone, which is `2016-08-31
 09:00:00`.

```
SELECT from_utc_timestamp('2016-08-31', 'Asia/Seoul');
 2016-08-31 09:00:00
```
