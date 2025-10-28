# Time helpers in util.time

The `util.time` variable contains datetime methods to help generate
timestamps, convert between datetime formats, and parse datetime strings. The syntax for
datetime formats is based on [DateTimeFormatter](https://docs.oracle.com/javase/8/docs/api/java/time/format/DateTimeFormatter.html "https://docs.oracle.com/javase/8/docs/api/java/time/format/DateTimeFormatter.html") which you can reference for further documentation.

## Time utils list

**`util.time.nowISO8601()`**

Returns a String representation of UTC in [ISO8601
format](https://en.wikipedia.org/wiki/ISO_8601 "https://en.wikipedia.org/wiki/ISO_8601").

**`util.time.nowEpochSeconds()`**

Returns the number of seconds from the epoch of 1970-01-01T00:00:00Z
to now.

**`util.time.nowEpochMilliSeconds()`**

Returns the number of milliseconds from the epoch of
1970-01-01T00:00:00Z to now.

**`util.time.nowFormatted(String)`**

Returns a string of the current timestamp in UTC using the specified
format from a String input type.

**`util.time.nowFormatted(String,
 String)`**

Returns a string of the current timestamp for a timezone using the
specified format and timezone from String input types.

**`util.time.parseFormattedToEpochMilliSeconds(String,
 String)`**

Parses a timestamp passed as a String along with a format containing a
time zone, then returns the timestamp as milliseconds since epoch.

**`util.time.parseFormattedToEpochMilliSeconds(String, String,
 String)`**

Parses a timestamp passed as a String along with a format and time
zone, then returns the timestamp as milliseconds since epoch.

**`util.time.parseISO8601ToEpochMilliSeconds(String)`**

Parses an ISO8601 timestamp passed as a String, then returns the
timestamp as milliseconds since epoch.

**`util.time.epochMilliSecondsToSeconds(long)`**

Converts an epoch milliseconds timestamp to an epoch seconds
timestamp.

**`util.time.epochMilliSecondsToISO8601(long)`**

Converts an epoch milliseconds timestamp to an ISO8601
timestamp.

**`util.time.epochMilliSecondsToFormatted(long,
 String)`**

Converts an epoch milliseconds timestamp, passed as long, to a
timestamp formatted according to the supplied format in UTC.

**`util.time.epochMilliSecondsToFormatted(long,
 String, String)`**

Converts an epoch milliseconds timestamp, passed as a long, to a
timestamp formatted according to the supplied format in the supplied
timezone.
