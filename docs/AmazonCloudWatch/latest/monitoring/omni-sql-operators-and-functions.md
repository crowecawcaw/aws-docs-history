

# Operators and functions

This page lists the operators and functions you can use in a CloudWatch Omni query. Each table lists representative functions in the family, not every function. For more information about hashing and encoding functions, see [Hash and encoding functions](omni-sql-hash-and-encoding-functions.md). Function names are not case sensitive. Some functions need a numeric field. For more information about when to cast a field, see column types in [SQL query reference](omni-sql-query-reference.md).

Every function on this page works on all three CloudWatch Omni tables: `logs.default`, `traces.default`, and `default`.

This page describes the following function families.

**Topics**
+ [String functions](#omni-sql-operators-and-functions-string-functions)
+ [Regular expression functions](#omni-sql-operators-and-functions-regular-expression-functions)
+ [Math functions](#omni-sql-operators-and-functions-math-functions)
+ [Conditional functions](#omni-sql-operators-and-functions-conditional-functions)
+ [Date and time functions](#omni-sql-operators-and-functions-date-and-time-functions)
+ [Aggregate functions](#omni-sql-operators-and-functions-aggregate-functions)
+ [Window functions](#omni-sql-operators-and-functions-window-functions)
+ [Array and struct functions](#omni-sql-operators-and-functions-array-and-struct-functions)
+ [JSON functions](#omni-sql-operators-and-functions-json-functions)
+ [IP address functions](#omni-sql-operators-and-functions-ip-address-functions)

## Example data
<a name="omni-sql-operators-and-functions-example-data"></a>

The examples on this page assume that your telemetry contains records like the following.

**Log example** (`logs.default`). The `@message` field holds the same JSON as text.

```json
{
  "request_id": "abc-123",
  "path": "/api/orders/1042",
  "status_code": 503,
  "latency_ms": 1840.5,
  "user_id": "u-1042",
  "user": { "id": "u-1042" },
  "retries": 2,
  "client_ip": "192.0.2.23"
}
```

**Trace example** (`traces.default`)

```json
{
  "traceId": "4bf92f3577b34da6a3ce929d0e0e4736",
  "spanId": "00f067aa0ba902b7",
  "name": "GET /api/orders/{id}",
  "kind": "SERVER",
  "startTimeUnixNano": 1792519316000000000,
  "endTimeUnixNano": 1792519317840500000,
  "resource": { "attributes": { "service.name": "orders-api" } },
  "attributes": { "http.status_code": 503 }
}
```

## String functions
<a name="omni-sql-operators-and-functions-string-functions"></a>

The following table describes the string functions.


| Function | Description | 
| --- | --- | 
| concat(a, b, ...), a \|\| b | Joins strings. | 
| concat\_ws(separator, a, b, ...) | Joins strings with a separator between them. | 
| length(s), char\_length(s) | Returns the number of characters. | 
| lower(s), upper(s), initcap(s) | Converts a string to lowercase, to uppercase, or to initial capitals. | 
| left(s, n), right(s, n) | Returns the first or last n characters. | 
| substring(s, start, length), substring(s FROM start FOR length), substr(s, start, length) | Returns part of a string, starting at position start, where the first character is 1. | 
| lpad(s, n, fill), rpad(s, n, fill) | Pads a string on the left or right with fill to length n. | 
| trim(s), trim([BOTH \| LEADING \| TRAILING] characters FROM s) | Removes spaces, or the characters you list, from both ends, the start, or the end of a string. | 
| ltrim(s), rtrim(s), btrim(s) | Removes leading, trailing, or both leading and trailing spaces. | 
| replace(s, from, to) | Replaces every occurrence of a substring. | 
| split\_part(s, delimiter, n) | Returns the nth part of a string split on a delimiter. | 
| starts\_with(s, prefix), ends\_with(s, suffix) | Returns true when a string starts with prefix or ends with suffix. | 
| contains(s, substring) | Returns true when the string contains the substring. | 
| strpos(s, substring), position(substring IN s) | Returns the position of a substring, or 0 if it is missing. | 
| reverse(s), repeat(s, n), translate(s, from, to) | Reverses a string, repeats it n times, or replaces each character in from with the matching character in to. | 
| levenshtein(a, b) | Returns the edit distance between two strings, which is the number of single-character changes that turn one string into the other. | 
| soundex(s) | Returns the Soundex code of a string, which encodes how the string sounds so that names that sound alike get the same code. | 
| mask(s) | Replaces letters and digits with placeholder characters. | 
| isblank(s), isempty(s) | Returns 1 when a string is empty or null. isblank also counts whitespace-only strings. | 
| parse\_url(url, part) | Returns one part of a URL, such as 'HOST'. | 
| url\_encode(s), url\_decode(s) | Encodes a string for use in a URL by replacing special characters with % codes (percent-encoding), or decodes such a string. | 

The following example counts requests for each API area, such as `orders`, in paths that start with `/api/`.

```sql
SELECT lower(split_part(path, '/', 3)) AS area,
       COUNT(*) AS requests
FROM "logs.default"
WHERE `@timestamp` BETWEEN NOW() - INTERVAL '1' HOUR AND NOW()
  AND starts_with(path, '/api/')
GROUP BY 1
ORDER BY requests DESC
```

## Regular expression functions
<a name="omni-sql-operators-and-functions-regular-expression-functions"></a>

The following table describes the regular expression functions.


| Function | Description | 
| --- | --- | 
| regexp\_like(s, pattern) | Returns true when the string matches the pattern. In WHERE, s \~ pattern does the same. | 
| regexp\_match(s, pattern) | Returns the capture groups (the parts of the pattern in parentheses) of the first match as an array. | 
| regexp\_replace(s, pattern, replacement) | Replaces the first match. Add the 'g' flag as a fourth argument to replace every match. | 
| regexp\_count(s, pattern) | Returns the number of matches. | 
| regexp\_instr(s, pattern) | Returns the position of the first match. | 
| regexp\_substr(s, pattern) | Returns the first match. | 
| regexp\_extract\_all(s, pattern) | Returns every match as an array. | 
| regexp\_matches(s, pattern) | Returns the capture groups of every match as an array of arrays. | 
| regexp\_split\_to\_array(s, pattern) | Splits a string on a pattern and returns the parts as an array. | 

The following example counts requests for each API route, with each number in the path replaced by `:id`.

```sql
SELECT regexp_replace(path, '[0-9]+', ':id', 'g') AS route,
       COUNT(*) AS requests
FROM "logs.default"
WHERE `@timestamp` BETWEEN NOW() - INTERVAL '1' HOUR AND NOW()
  AND regexp_like(path, '^/api/')
GROUP BY 1
ORDER BY requests DESC
```

## Math functions
<a name="omni-sql-operators-and-functions-math-functions"></a>

The following table describes the math functions.


| Function | Description | 
| --- | --- | 
| \+, -, \*, /, % | Adds, subtracts, multiplies, divides, or returns the remainder (%). | 
| abs(x) | Returns the absolute value. | 
| round(x, digits), trunc(x) | Rounds to digits decimal places, or drops the fractional part. | 
| ceil(x), floor(x) | Rounds up or down to a whole number. | 
| bround(x, digits) | Rounds to digits decimal places, and rounds a value that is exactly halfway to the nearest even digit (banker's rounding). Cast the field to DOUBLE first. | 
| power(x, y), sqrt(x), cbrt(x), exp(x) | Returns x to the power y, the square root, the cube root, or e to the power x. | 
| ln(x), log10(x), log2(x), log(base, x) | Returns the natural, base-10, base-2, or base-base logarithm. | 
| expm1(x), log1p(x) | Returns exp(x) - 1 or ln(1 \+ x), accurate for values of x near 0. Cast the field to DOUBLE first. | 
| hypot(x, y) | Returns the square root of x squared plus y squared. Cast the field to DOUBLE first. | 
| pmod(a, b) | Returns the remainder of a divided by b, with the same sign as b. Cast the field to DOUBLE first. | 
| gcd(a, b) | Returns the greatest common divisor of two integers. Cast the field to BIGINT first. | 
| signum(x) | Returns -1, 0, or 1 for the sign of a number. | 
| csc(x), sec(x) | Returns the cosecant or secant of an angle in radians. Cast the field to DOUBLE first. | 
| sigmoid(x) | Returns the logistic sigmoid, 1 / (1 \+ exp(-x)). Cast the field to DOUBLE first. | 
| isnan(x), is\_finite(x), is\_infinite(x) | Returns true when a number is NaN (not a number), finite, or infinite. Cast the field to DOUBLE first. | 
| pi(), e(), tau() | Returns the constant pi, e, or tau, which is 2 times pi. | 
| random() | Returns a random number between 0 and 1. | 
| clamp(x, low, high) | Limits a number to a range. Cast the field to DOUBLE first. | 
| safe\_div(a, b) | Divides a by b, and returns null instead of failing when b is 0. Cast the field to DOUBLE first. | 
| pct\_change(current, previous) | Returns the percentage change from previous to current. Cast the field to DOUBLE first. | 
| width\_bucket(x, low, high, count) | Splits the range from low to high into count equal-width buckets and returns the number of the bucket that x falls in. Cast the field to DOUBLE first. | 
| to\_hex(n), bin(n) | Returns an integer as hexadecimal or binary text. Cast the field to BIGINT first. | 
| conv(s, from\_base, to\_base) | Converts a number written as text from one base to another, such as conv('ff', 16, 10). | 

The following example returns the 20 slowest requests, with latency in seconds.

```sql
SELECT request_id,
       round(CAST(latency_ms AS DOUBLE) / 1000, 2) AS latency_s
FROM "logs.default"
WHERE `@timestamp` BETWEEN NOW() - INTERVAL '1' HOUR AND NOW()
ORDER BY latency_s DESC
LIMIT 20
```

## Conditional functions
<a name="omni-sql-operators-and-functions-conditional-functions"></a>

The following table describes the conditional functions.


| Function | Description | 
| --- | --- | 
| CASE WHEN ... THEN ... ELSE ... END | Returns the value for the first condition that is true. | 
| coalesce(a, b, ...), nvl(a, b) | Returns the first value that is not null. | 
| nvl2(a, if\_not\_null, if\_null) | Returns one of two values depending on whether a is null. | 
| nullif(a, b) | Returns null when a equals b, otherwise a. | 
| greatest(a, b, ...), least(a, b, ...) | Returns the largest or smallest value. | 

The following example counts requests by outcome and user, and uses `anonymous` when a request has no user ID.

```sql
SELECT CASE
         WHEN status_code >= 500 THEN 'server error'
         WHEN status_code >= 400 THEN 'client error'
         ELSE 'ok'
       END AS outcome,
       coalesce(user_id, 'anonymous') AS user_id,
       COUNT(*) AS requests
FROM "logs.default"
WHERE `@timestamp` BETWEEN NOW() - INTERVAL '1' HOUR AND NOW()
GROUP BY 1, 2
```

## Date and time functions
<a name="omni-sql-operators-and-functions-date-and-time-functions"></a>

The following table describes the date and time functions.


| Function | Description | 
| --- | --- | 
| now(), current\_date() | Returns the current time or date. | 
| INTERVAL '<n>' <unit> | Represents a length of time that you add to or subtract from a timestamp, such as NOW() - INTERVAL '1' DAY. | 
| to\_timestamp(s) | Converts a string such as '2026-01-01T00:00:00Z' to a timestamp. | 
| to\_timestamp\_seconds(n), to\_timestamp\_millis(n), from\_unixtime(n) | Converts epoch seconds or milliseconds to a timestamp. | 
| to\_unixtime(ts) | Converts a timestamp to epoch seconds. | 
| date\_trunc(unit, ts) | Rounds a timestamp down to a unit such as 'minute' or 'hour'. | 
| date\_bin(interval, ts) | Rounds a timestamp down to a bucket of any size, such as 5 minutes. | 
| dateceil(ts, interval) | Rounds a timestamp up to a bucket of the size you set, such as INTERVAL '1' HOUR. | 
| date\_part(unit, ts), extract(unit FROM ts) | Returns one part of a timestamp, such as the hour. | 
| to\_char(ts, format), to\_date(s) | Formats a timestamp as text with a format such as '%Y-%m-%d', or converts text to a date. | 
| unix\_millis(ts), unix\_micros(ts) | Returns the number of milliseconds or microseconds since the Unix epoch. | 
| make\_date(year, month, day) | Builds a date from its parts. | 
| make\_timestamp(year, month, day, hour, minute, second) | Builds a timestamp from its parts. | 
| make\_interval(years, months, weeks, days, hours, minutes, seconds) | Builds an interval from its parts. | 
| date\_add(date, days), date\_sub(date, days) | Adds days to or subtracts days from a date. | 
| date\_diff(end, start) | Returns the number of days between two dates. | 
| add\_months(date, months) | Adds months to a date. | 
| months\_between(ts1, ts2) | Returns the number of months between two timestamps, including a fractional part. | 
| last\_day(date) | Returns the last day of the month that contains the date. | 
| next\_day(date, weekday) | Returns the first date after date that falls on the weekday you name, such as 'Monday'. | 
| convert\_timezone(from\_zone, to\_zone, ts) | Converts a timestamp from one time zone to another, such as 'America/New\_York'. | 
| from\_utc\_timestamp(ts, zone), to\_utc\_timestamp(ts, zone) | Converts a UTC timestamp to the time zone you name, or a timestamp in that time zone to UTC. | 

The following example counts requests in 5-minute buckets over the last 3 hours.

```sql
SELECT date_bin(INTERVAL '5 minutes', `@timestamp`) AS bucket,
       COUNT(*) AS requests
FROM "logs.default"
WHERE `@timestamp` BETWEEN NOW() - INTERVAL '3' HOUR AND NOW()
GROUP BY 1
ORDER BY 1
```

## Aggregate functions
<a name="omni-sql-operators-and-functions-aggregate-functions"></a>

Add `FILTER (WHERE ...)` after any aggregate function to include only some rows.

The following table describes the aggregate functions.


| Function | Description | 
| --- | --- | 
| count(\*), count(x), count(DISTINCT x) | Counts rows, values that are not null, or distinct values. | 
| sum(x), avg(x), min(x), max(x) | Returns the sum, average, minimum, or maximum. | 
| stddev(x), var\_samp(x) | Returns the standard deviation or the variance. | 
| median(x) | Returns the median. Cast the field to DOUBLE first. | 
| approx\_percentile\_cont(x, p) | Returns an approximate percentile, where p is a fraction such as 0.95 for the 95th percentile. Cast the field to DOUBLE first. | 
| approx\_distinct(x) | Returns an approximate count of distinct values. | 
| string\_agg(x, separator), array\_agg(x) | Collects values into one string or one array. | 
| bool\_and(condition) | Returns true when the condition is true for every row. | 
| first\_value(x ORDER BY y) | Returns the value from the first row in the order you set. | 
| pattern(field) | Groups similar log messages in a field, such as @message, into patterns. A pattern is text structure that recurs across the messages. Wrap the function in UNNEST to return one row per pattern. | 

The following example returns the average span duration, in milliseconds, for each service.

```sql
SELECT resource['attributes']['service.name'] AS service,
       avg(endTimeUnixNano - startTimeUnixNano) / 1e6 AS avg_ms
FROM "traces.default"
WHERE `@timestamp` BETWEEN NOW() - INTERVAL '1' HOUR AND NOW()
GROUP BY 1
ORDER BY avg_ms DESC
```

## Window functions
<a name="omni-sql-operators-and-functions-window-functions"></a>

A window function needs an `OVER` clause. `PARTITION BY` in the `OVER` clause splits the rows into partitions, and the function runs on each partition separately. Aggregate functions such as `count`, `sum`, `avg`, and `min` also work as window functions when you add `OVER`.

The following table describes the window functions.


| Function | Description | 
| --- | --- | 
| row\_number() | Numbers the rows in each partition, starting at 1. | 
| rank(), dense\_rank(), percent\_rank() | Ranks rows. Tied rows get the same rank. | 
| ntile(n) | Splits the rows into n groups of about the same size. | 
| lag(x), lead(x) | Returns the value from the previous or next row. | 
| first\_value(x) | Returns the value from the first row in the window. | 
| count(\*) OVER (...), sum(x) OVER (...), avg(x) OVER (...), min(x) OVER (...) | Returns a running or partition-wide count, total, average, or minimum. | 

The following example returns the three slowest requests for each path.

```sql
SELECT path, request_id, latency_ms
FROM (
  SELECT path, request_id, latency_ms,
         ROW_NUMBER() OVER (
           PARTITION BY path
           ORDER BY CAST(latency_ms AS DOUBLE) DESC
         ) AS rn
  FROM "logs.default"
  WHERE `@timestamp` BETWEEN NOW() - INTERVAL '1' HOUR AND NOW()
) ranked
WHERE rn <= 3
```

## Array and struct functions
<a name="omni-sql-operators-and-functions-array-and-struct-functions"></a>

To read a key from an attribute map, use bracket syntax such as `attributes['http.status_code']`. For more information about bracket syntax, see [SQL query reference](omni-sql-query-reference.md).

The following table describes the array and struct functions.


| Function | Description | 
| --- | --- | 
| make\_array(a, b, ...) | Builds an array. | 
| array\_length(arr), cardinality(arr) | Returns the number of elements. | 
| array\_has(arr, value) | Returns true when the array contains the value. | 
| array\_element(arr, n) | Returns the element at position n, starting at 1. | 
| array\_to\_string(arr, separator), string\_to\_array(s, separator) | Converts between arrays and strings. | 
| UNNEST(arr) | Expands an array into one row per element. | 
| array\_sum(arr), array\_product(arr), array\_avg(arr) | Returns the sum, product, or average of the elements. | 
| array\_cum\_sum(arr) | Returns the running sum of the elements. | 
| array\_difference(arr) | Returns the difference between each element and the one before it. | 
| array\_count(arr, value) | Counts the elements that equal a value. | 
| array\_filter(arr, threshold) | Keeps only the elements greater than a threshold. | 
| array\_first(arr), array\_last(arr) | Returns the first or last element that is not null. | 
| array\_fold(arr, initial) | Returns the sum of the elements plus an initial value. | 
| named\_struct('name', value, ...) | Builds a struct with named fields. | 

The following example counts requests by the number of parts in each path.

```sql
SELECT cardinality(string_to_array(path, '/')) AS depth,
       COUNT(*) AS requests
FROM "logs.default"
WHERE `@timestamp` BETWEEN NOW() - INTERVAL '1' HOUR AND NOW()
GROUP BY 1
```

## JSON functions
<a name="omni-sql-operators-and-functions-json-functions"></a>

CloudWatch Omni stores each field of a JSON record as its own column, including nested fields. To read a nested field, use bracket syntax, such as `user['id']`, instead of a JSON function. Bracket syntax runs faster and follows the access rules for your space. These functions read values from a field that holds JSON text, such as `@message`. To read a nested value, list each key as its own argument.

The following table describes the JSON functions.


| Function | Description | 
| --- | --- | 
| json\_get\_str(json, key, ...) | Returns a string value. | 
| json\_get\_int(json, key, ...) | Returns an integer value. | 
| json\_get\_float(json, key, ...) | Returns a floating-point value. | 
| json\_get\_bool(json, key, ...) | Returns a Boolean value. | 
| json\_get\_json(json, key, ...) | Returns a value as JSON text. | 
| json\_get(json, key, ...) | Returns a value of any type. | 
| json\_as\_text(json, key, ...) | Returns a value as text. | 
| json\_contains(json, key, ...) | Returns true when the key exists. | 
| json\_length(json) | Returns the number of elements in a JSON array or object. | 
| json\_keys(json) | Returns the keys of a JSON object as an array. | 
| json\_array\_first\_matching(array, key, value), json\_array\_last\_matching(array, key, value) | Returns the first or last object in a JSON array whose key equals value. | 

The following example reads values from `@message`, including a nested value.

```sql
SELECT json_get_str(`@message`, 'user', 'id') AS user_id,
       json_get_int(`@message`, 'retries') AS retries
FROM "logs.default"
WHERE `@timestamp` BETWEEN NOW() - INTERVAL '15' MINUTE AND NOW()
  AND json_contains(`@message`, 'user')
LIMIT 100
```

## IP address functions
<a name="omni-sql-operators-and-functions-ip-address-functions"></a>

These functions read IP addresses stored as text.

The following table describes the IP address functions.


| Function | Description | 
| --- | --- | 
| ipv4\_string\_to\_num(s), ipv4\_num\_to\_string(n) | Converts an IPv4 address between dotted-decimal text, such as '192.0.2.1', and its integer value. | 
| ipv4\_anonymize\_class\_c(s) | Replaces the last part of an IPv4 address with xxx. | 
| cut\_ipv6(s, bytes\_v6, bytes\_v4) | Sets the last bytes\_v6 bytes of an IPv6 address to zero, or the last bytes\_v4 bytes of an IPv4-mapped IPv6 address (an IPv6 address that contains an IPv4 address). | 

The following example counts requests for each client network, with the last part of each IP address replaced by `xxx`.

```sql
SELECT ipv4_anonymize_class_c(client_ip) AS network,
       COUNT(*) AS requests
FROM "logs.default"
WHERE `@timestamp` BETWEEN NOW() - INTERVAL '1' HOUR AND NOW()
GROUP BY 1
ORDER BY requests DESC
```