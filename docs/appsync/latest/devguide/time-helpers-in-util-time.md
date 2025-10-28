# Time helpers in $util.time

###### Note

We now primarily support the APPSYNC_JS runtime and its documentation. Please
consider using the APPSYNC_JS runtime and its guides [here](resolver-reference-js-version.md "resolver-reference-js-version.md").

The `$util.time` variable contains datetime methods to help generate
timestamps, convert between datetime formats, and parse datetime strings. The syntax for
datetime formats is based on [DateTimeFormatter](https://docs.oracle.com/javase/8/docs/api/java/time/format/DateTimeFormatter.html "https://docs.oracle.com/javase/8/docs/api/java/time/format/DateTimeFormatter.html") which you can reference for further documentation. We provide
some examples below, as well as a list of available methods and descriptions.

## Time utils

**`$util.time.nowISO8601() : String`**

Returns a String representation of UTC in [ISO8601
format](https://en.wikipedia.org/wiki/ISO_8601 "https://en.wikipedia.org/wiki/ISO_8601").

**`$util.time.nowEpochSeconds() : long`**

Returns the number of seconds from the epoch of 1970-01-01T00:00:00Z
to now.

**`$util.time.nowEpochMilliSeconds() : long`**

Returns the number of milliseconds from the epoch of
1970-01-01T00:00:00Z to now.

**`$util.time.nowFormatted(String) : String`**

Returns a string of the current timestamp in UTC using the specified
format from a String input type.

**`$util.time.nowFormatted(String, String) : String`**

Returns a string of the current timestamp for a timezone using the
specified format and timezone from String input types.

**`$util.time.parseFormattedToEpochMilliSeconds(String, String) :
 Long`**

Parses a timestamp passed as a String along with a format containing a
time zone, then returns the timestamp as milliseconds since epoch.

**`$util.time.parseFormattedToEpochMilliSeconds(String, String, String) :
 Long`**

Parses a timestamp passed as a String along with a format and time
zone, then returns the timestamp as milliseconds since epoch.

**`$util.time.parseISO8601ToEpochMilliSeconds(String) : Long`**

Parses an ISO8601 timestamp passed as a String, then returns the
timestamp as milliseconds since epoch.

**`$util.time.epochMilliSecondsToSeconds(long) : long`**

Converts an epoch milliseconds timestamp to an epoch seconds
timestamp.

**`$util.time.epochMilliSecondsToISO8601(long) : String`**

Converts an epoch milliseconds timestamp to an ISO8601
timestamp.

**`$util.time.epochMilliSecondsToFormatted(long, String) : String`**

Converts an epoch milliseconds timestamp, passed as long, to a
timestamp formatted according to the supplied format in UTC.

**`$util.time.epochMilliSecondsToFormatted(long, String, String) :
 String`**

Converts an epoch milliseconds timestamp, passed as a long, to a
timestamp formatted according to the supplied format in the supplied
timezone.

## Standalone function examples

```
$util.time.nowISO8601()                                            : 2018-02-06T19:01:35.749Z
$util.time.nowEpochSeconds()                                       : 1517943695
$util.time.nowEpochMilliSeconds()                                  : 1517943695750
$util.time.nowFormatted("yyyy-MM-dd HH:mm:ssZ")                    : 2018-02-06 19:01:35+0000
$util.time.nowFormatted("yyyy-MM-dd HH:mm:ssZ", "+08:00")          : 2018-02-07 03:01:35+0800
$util.time.nowFormatted("yyyy-MM-dd HH:mm:ssZ", "Australia/Perth") : 2018-02-07 03:01:35+0800
```

## Conversion examples

```
#set( $nowEpochMillis = 1517943695758 )
$util.time.epochMilliSecondsToSeconds($nowEpochMillis)                                     : 1517943695
$util.time.epochMilliSecondsToISO8601($nowEpochMillis)                                     : 2018-02-06T19:01:35.758Z
$util.time.epochMilliSecondsToFormatted($nowEpochMillis, "yyyy-MM-dd HH:mm:ssZ")           : 2018-02-06 19:01:35+0000
$util.time.epochMilliSecondsToFormatted($nowEpochMillis, "yyyy-MM-dd HH:mm:ssZ", "+08:00") : 2018-02-07 03:01:35+0800
```

## Parsing examples

```
$util.time.parseISO8601ToEpochMilliSeconds("2018-02-01T17:21:05.180+08:00")                          : 1517476865180
$util.time.parseFormattedToEpochMilliSeconds("2018-02-02 01:19:22+0800", "yyyy-MM-dd HH:mm:ssZ")     : 1517505562000
$util.time.parseFormattedToEpochMilliSeconds("2018-02-02 01:19:22", "yyyy-MM-dd HH:mm:ss", "+08:00") : 1517505562000
```

## Usage with AWS AppSync defined scalars

The following formats are compatible with `AWSDate`,
`AWSDateTime`, and `AWSTime`.

```
$util.time.nowFormatted("yyyy-MM-dd[XXX]", "-07:00:30")               : 2018-07-11-07:00
$util.time.nowFormatted("yyyy-MM-dd'T'HH:mm:ss[XXXXX]", "-07:00:30")  : 2018-07-11T15:14:15-07:00:30
```
