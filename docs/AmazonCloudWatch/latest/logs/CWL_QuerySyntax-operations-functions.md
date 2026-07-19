# Boolean, comparison, numeric, datetime, and other functions

CloudWatch Logs Insights supports many other operations and functions in queries, as
explained in the following sections.

###### Topics

- [Arithmetic operators](#CWL_QuerySyntax-operations-arithmetic "#CWL_QuerySyntax-operations-arithmetic")
- [Boolean operators](#CWL_QuerySyntax-operations-Boolean "#CWL_QuerySyntax-operations-Boolean")
- [Comparison operators](#CWL_QuerySyntax-operations-comparison "#CWL_QuerySyntax-operations-comparison")
- [Numeric operators](#CWL_QuerySyntax-operations-numeric "#CWL_QuerySyntax-operations-numeric")
- [Structure types](#CWL_QuerySyntax-structure-types "#CWL_QuerySyntax-structure-types")
- [Datetime functions](#CWL_QuerySyntax-datetime "#CWL_QuerySyntax-datetime")
- [General functions](#CWL_QuerySyntax-general-functions "#CWL_QuerySyntax-general-functions")
- [JSON functions](#CWL_QuerySyntax-json-functions "#CWL_QuerySyntax-json-functions")
- [IP address string functions](#CWL_QuerySyntax-IPaddress-functions "#CWL_QuerySyntax-IPaddress-functions")
- [String functions](#CWL_QuerySyntax-string-functions "#CWL_QuerySyntax-string-functions")

## Arithmetic operators

Arithmetic operators accept numeric data types as arguments and
return numeric results. Use arithmetic operators in the
`filter` and `fields` commands and as
arguments for other functions.

| Operation  | Description                                    |
| ---------- | ---------------------------------------------- |
| `a + b`    | Addition                                       |
| `a<br>• b` | Subtraction                                    |
| `a<br>• b` | Multiplication                                 |
| `a / b`    | Division                                       |
| `a ^ b`    | Exponentiation (`2 ^ 3` returns<br>`8`)        |
| `a % b`    | Remainder or modulus (`10 % 3` returns<br>`1`) |

## Boolean operators

Use the Boolean operators `**and**`,
`**or**`, and
`**not**`.

###### Note

Use Boolean operators only in functions that return a value of
**TRUE** or **FALSE**.

## Comparison operators

Comparison operators accept all data types as arguments and return a
Boolean result. Use comparison operations in the `filter`
command and as arguments for other functions.

| Operator | Description              |
| -------- | ------------------------ |
| `=`      | Equal                    |
| `!=`     | Not equal                |
| `<`      | Less than                |
| `>`      | Greater than             |
| `<=`     | Less than or equal to    |
| `>=`     | Greater than or equal to |

## Numeric operators

Numeric operations accept numeric data types as arguments and return
numeric results. Use numeric operations in the `filter` and
`fields` commands and as arguments for other functions.

| Operation                                                           | Result type | Description                                                                                                                              |
| ------------------------------------------------------------------- | ----------- | ---------------------------------------------------------------------------------------------------------------------------------------- |
| `abs(a: number)`                                                    | number      | Absolute value                                                                                                                           |
| `ceil(a: number)`                                                   | number      | Round to ceiling (the smallest integer that is<br>greater than the value of `a`)                                                         |
| `floor(a: number)`                                                  | number      | Round to floor (the largest integer that is<br>smaller than the value of `a`)                                                            |
| `greatest(a: number, ...numbers:<br>number[])`                      | number      | Returns the largest value                                                                                                                |
| `least(a: number, ...numbers: number[])`                            | number      | Returns the smallest value                                                                                                               |
| `log(a: number)`                                                    | number      | Natural log                                                                                                                              |
| `round(a: number [, d: number])`                                    | number      | Rounds the value of<br>`a`. With one argument,<br>rounds to the nearest integer. With two<br>arguments, rounds to `d`<br>decimal places. |
| `sqrt(a: number)`                                                   | number      | Square root                                                                                                                              |
| `haversine(lat1: number, lon1: number, lat2: number, lon2: number)` | number      | Computes the great-circle distance in<br>kilometers between two geographic points<br>specified by latitude and longitude in<br>degrees.  |
| `toNumber(fieldName: string)`                                       | number      | Converts a string field value to a numeric<br>value.                                                                                     |
| `toInt(fieldName: string)`                                          | number      | Converts a field value to an integer<br>(32-bit).                                                                                        |
| `toLong(fieldName: string)`                                         | number      | Converts a field value to a long integer<br>(64-bit).                                                                                    |
| `toDouble(fieldName: string)`                                       | number      | Converts a field value to a double-precision<br>floating point number.                                                                   |

## Structure types

A map or list is a structure type in CloudWatch Logs Insights that allows you to
access and use attributes for queries.

###### Example: To get a map or list

Use `jsonParse` to parse a field that's a json string
into a map or a list.

```
fields jsonParse(@message) as json_message
```

###### Example: To access attributes

Use the dot access operator (map.attribute) to access items in a
map.. If an attribute in a map contains special characters, use
backticks to enclose the attribute name
(map.attributes.`special.char`).

```
fields jsonParse(@message) as json_message
| stats count() by json_message.status_code
```

Use the bracket access operator (list[index]) to retrieve an item at
a specific position within the list.

```
fields jsonParse(@message) as json_message
| filter json_message.users[1].action = "PutData"
```

Wrap special characters in backticks (``) when special characters are
present in the key name.

```
fields jsonParse(@message) as json_message
| filter json_message.`user.id` = "123"
```

###### Example: empty results

Maps and lists are treated as null for string, number, and
datetime functions.

```
fields jsonParse(@message) as json_message
| display toupper(json_message)
```

Comparing map and list to any other fields result in
`false`.

###### Note

Using map and list in `dedup`,`pattern`,
`sort`, and `stats` isn't supported.

## Datetime functions

**Datetime functions**

Use datetime functions in the `fields` and
`filter`commands and as arguments for other functions.
Use these functions to create time buckets for queries with aggregate
functions. Use time periods that consist of a number and one of the
following:

- `ms` for milliseconds
- `s` for seconds
- `m` for minutes
- `h` for hours

For example, `10m` is 10 minutes, and `1h` is 1
hour.

###### Note

Use the most appropriate time unit for your datetime function.
CloudWatch Logs caps your request according to the time unit that you choose.
For example, it caps 60 as the maximum value for any request that
uses `s`. So, if you specify `bin(300s)`,
CloudWatch Logs actually implements this as 60 seconds, because 60 is the
number of seconds in a minute so CloudWatch Logs won't use a number higher
than 60 with `s`. To create a 5-minute bucket, use
`bin(5m)` instead.

The cap for `ms` is 1000, the caps for `s`
and `m` are 60, and the cap for `h` is 24.

The following table contains a list of the different datetime
functions that you can use in query commands. The table lists each
function's result type and contains a description of each function.

###### Tip

When you create a query command, you can use the time interval
selector to select a time period that you want to query. For
example, you can set a time period between 5 and 30-minute
intervals; 1, 3, and 12-hour intervals; or a custom time frame. You
also can set time periods between specific dates.

| Function                                                                  | Result type | Description                                                                                                                                                                                                                                                                                                                                                             |
| ------------------------------------------------------------------------- | ----------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `bin(period: Period)`                                                     | Timestamp   | Rounds the value of `@timestamp` to the<br>given time period and then truncates. For example,<br>`bin(5m)` rounds the value of<br>`@timestamp` to the nearest 5<br>minutes.<br>You can use this to group multiple log entries<br>together in a query. The following example returns<br>the count of exceptions per hour:<br>```<br>filter @message like /Exception/<br> | stats count(*) as exceptionCount by bin(1h)<br>       | sort exceptionCount desc<br>```<br>The following time units and abbreviations are<br>supported with the `bin` function. For<br>all units and abbreviations that include more than<br>one character, adding s to pluralize is supported.<br>So both `hr` and `hrs` work to<br>specify hours.<br>• `millisecond`<br>`ms`<br>`msec`<br>• `second`<br>`s`<br>`sec`<br>• `minute`<br>`m`<br>`min`<br>• `hour`<br>`h`<br>`hr`<br>• `day`<br>`d`<br>• `week`<br>`w`<br>• `month`<br>`mo`<br>`mon`<br>• `quarter`<br>`q`<br>`qtr`<br>• `year`<br>`y`<br>`yr` |
| `datefloor(timestamp: Timestamp, period:<br>Period)`                      | Timestamp   | Truncates the timestamp to the given period. For<br>example, `datefloor(@timestamp, 1h)`<br>truncates all values of `@timestamp` to<br>the bottom of the hour.                                                                                                                                                                                                          |
| `dateceil(timestamp: Timestamp, period:<br>Period)`                       | Timestamp   | Rounds up the timestamp to the given period and<br>then truncates. For example,<br>`dateceil(@timestamp, 1h)` truncates<br>all values of `@timestamp` to the top of<br>the hour.                                                                                                                                                                                        |
| `fromMillis(fieldName:<br>number)`                                        | Timestamp   | Interprets the input field as the number of<br>milliseconds since the Unix epoch and converts it to<br>a timestamp.                                                                                                                                                                                                                                                     |
| `toMillis(fieldName:<br>Timestamp)`                                       | number      | Converts the timestamp found in the named field<br>into a number representing the milliseconds since<br>the Unix epoch. For example,<br>`toMillis(@timestamp)` converts the<br>timestamp<br>`2022-01-14T13:18:031.000-08:00` to<br>`1642195111000`.                                                                                                                     |
| `now()`                                                                   | number      | Returns the time that the query processing was<br>started, in epoch seconds. This function takes no<br>arguments.<br>You can use this to filter your query results<br>according to the current time.<br>For example, the following query returns all 4xx<br>errors from the past two hours:<br>```<br>parse @message "Status Code: *;" as statusCode\n<br>              | filter statusCode >= 400 and statusCode <= 499 \n<br> | filter toMillis(@timestamp) >= (now()<br>• 1000<br>• 7200000)<br>``<br>The following example returns all log entries from<br>the past five hours that contain either the word<br>`error` or `failure`<br>``<br>fields @timestamp, @message<br>                                                                                                                                                                                                                                                                                                       | filter @message like /(?i)(error | failure)/<br> | filter toMillis(@timestamp) >= (now()<br>• 1000<br>• 18000000)<br>``` |
| `parseDate(fieldName: string, format:<br>string [, timezone: string])`    | number      | Parses a date string to epoch milliseconds using<br>a Java DateTimeFormatter pattern. The optional<br>`timezone` argument specifies the time<br>zone to use for parsing.<br>Example: `fields parseDate(field, "yyyy-MM-dd", "UTC") as epoch`                                                                                                                            |
| `formatDate(timestamp: LogField, format:<br>string [, timezone: string])` | string      | Formats a timestamp using a strftime-style format<br>string. Also available as the alias<br>`strftime`. The optional<br>`timezone` argument specifies the time<br>zone for formatting.<br>Example: `fields formatDate(@timestamp, "%Y-%m-%d", "UTC") as date`                                                                                                           |

###### Note

Currently, CloudWatch Logs Insights doesn't support filtering logs with human
readable timestamps.

## General functions

**General functions**

Use general functions in the `fields` and
`filter` commands and as arguments for other functions.

| Function                                                            | Result type | Description                                                                                                                                                                                    |
| ------------------------------------------------------------------- | ----------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `ispresent(fieldName: LogField)`                                    | Boolean     | Returns `true` if the field exists                                                                                                                                                             |
| `coalesce(fieldName: LogField, ...fieldNames:<br>LogField[])`       | LogField    | Returns the first non-null value from the list                                                                                                                                                 |
| `case(cond1, val1, cond2, val2, ...,<br>[default])`                 | LogField    | Evaluates conditions in order and returns the<br>value for the first true condition. If no condition<br>is true and a default is provided, returns the<br>default. Supports up to 10 branches. |
| `if(condition: Boolean, trueValue: LogField, falseValue: LogField)` | LogField    | Evaluates a condition and returns<br>`trueValue` if the condition is true,<br>or `falseValue` otherwise.                                                                                       |
| `isNumeric(fieldName: LogField)`                                    | Boolean     | Returns `true` if the field value<br>can be parsed as a number.<br>Example: `filter isNumeric(@duration)`                                                                                      |
| `messageSize(fieldName: LogField)`                                  | number      | Returns the byte length of a string field.<br>Example: `fields messageSize(@message) as size`                                                                                                  |
| `queryStartTime()`                                                  | number      | Returns the query window start time as epoch<br>milliseconds.                                                                                                                                  |
| `queryEndTime()`                                                    | number      | Returns the query window end time as epoch<br>milliseconds.                                                                                                                                    |
| `queryTimeRange()`                                                  | number      | Returns the query window duration in milliseconds.                                                                                                                                             |

## JSON functions

**JSON functions**

Use JSON functions in the `fields` and `filter`
commands and as arguments for other functions.

| Function                                                   | Result type | Description                                                                                                                                                                                                                                          |
| ---------------------------------------------------------- | ----------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `jsonParse(fieldName: string)`                             | Map         | List                                                                                                                                                                                                                                                 | Empty                                          | Returns a map or list when the input is a string<br>representation of JSON object or a JSON array.<br>Returns an empty value, if the input is not one of<br>the representation. |
| `jsonStringify(fieldName: Map                              | List)`      | String                                                                                                                                                                                                                                               | Returns a JSON string from a map or list data. |
| `jsonArraySize(fieldName: LogField)`                       | number      | Returns the element count of a JSON array<br>string field.<br>Example: `fields jsonArraySize(Operation) as arrayLen`                                                                                                                                 |
| `jsonArrayContains(fieldName: LogField, value:<br>string)` | Boolean     | Returns `true` (1) if the JSON array<br>in the field contains the specified value. Returns<br>`false` (0) for invalid JSON, non-array,<br>or empty array. Uses case-sensitive<br>comparison.<br>Example: `filter jsonArrayContains(@roles, "admin")` |

## IP address string functions

**IP address string functions**

Use IP address string functions in the `filter` and
`fields` commands and as arguments for other functions.

| Function                                               | Result type | Description                                                                                                                                                                                                                                                                     |
| ------------------------------------------------------ | ----------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `isValidIp(fieldName:<br>string)`                      | boolean     | Returns `true` if the field is a valid<br>IPv4 or IPv6 address.                                                                                                                                                                                                                 |
| `isValidIpV4(fieldName:<br>string)`                    | boolean     | Returns `true` if the field is a valid<br>IPv4 address.                                                                                                                                                                                                                         |
| `isValidIpV6(fieldName:<br>string)`                    | boolean     | Returns `true` if the field is a valid<br>IPv6 address.                                                                                                                                                                                                                         |
| `isIpInSubnet(fieldName: string, subnet:<br>string)`   | boolean     | Returns `true` if the field is a valid<br>IPv4 or IPv6 address within the specified v4 or v6<br>subnet. When you specify the subnet, use CIDR<br>notation such as `192.0.2.0/24` or<br>`2001:db8::/32`, where<br>`192.0.2.0` or `2001:db8::`<br>is the start of the CIDR block. |
| `isIpv4InSubnet(fieldName: string, subnet:<br>string)` | boolean     | Returns `true` if the field is a valid<br>IPv4 address within the specified v4 subnet. When<br>you specify the subnet, use CIDR notation such as<br>`192.0.2.0/24` where<br>`192.0.2.0` is the start of the CIDR<br>block..                                                     |
| `isIpv6InSubnet(fieldName: string, subnet:<br>string)` | boolean     | Returns `true` if the field is a valid<br>IPv6 address within the specified v6 subnet. When<br>you specify the subnet, use CIDR notation such as<br>`2001:db8::/32` where<br>`2001:db8::` is the start of the CIDR<br>block.                                                    |
| `ipv4ToNumber(fieldName: string)`                      | number      | Converts an IPv4 address string to its numeric<br>representation.                                                                                                                                                                                                               |
| `isPrivateIP(fieldName: string)`                       | boolean     | Returns `true` if the IP address is in<br>a private range (RFC 1918).                                                                                                                                                                                                           |
| `isPublicIP(fieldName: string)`                        | boolean     | Returns `true` if the IP address is<br>publicly routable.                                                                                                                                                                                                                       |
| `isReservedIP(fieldName: string)`                      | boolean     | Returns `true` if the IP address is in<br>a reserved range.                                                                                                                                                                                                                     |

## String functions

**String functions**

Use string functions in the `fields` and
`filter` commands and as arguments for other functions.

| Function                                                                                                                           | Result type | Description                                                                                                                                                                                                                                                                                                                                       |
| ---------------------------------------------------------------------------------------------------------------------------------- | ----------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `isempty(fieldName:<br>string)`                                                                                                    | Number      | Returns `1` if the field is missing or<br>is an empty string.                                                                                                                                                                                                                                                                                     |
| `isblank(fieldName:<br>string)`                                                                                                    | Number      | Returns `1` if the field is missing, an<br>empty string, or contains only white space.                                                                                                                                                                                                                                                            |
| `concat(str: string, ...strings:<br>string[])`                                                                                     | string      | Concatenates the strings.                                                                                                                                                                                                                                                                                                                         |
| `ltrim(str: string)`<br>`ltrim(str: string, trimChars:<br>string)`                                                                 | string      | If the function does not have a second argument,<br>it removes white space from the left of the string.<br>If the function has a second string argument, it<br>does not remove white space. Instead, it removes the<br>characters in `trimChars` from the left<br>of `str`. For example,<br>`ltrim("xyZxyfooxyZ","xyZ")` returns<br>`"fooxyZ"`.   |
| `rtrim(str: string)`<br>`rtrim(str: string, trimChars:<br>string)`                                                                 | string      | If the function does not have a second argument,<br>it removes white space from the right of the string.<br>If the function has a second string argument, it<br>does not remove white space. Instead, it removes the<br>characters of `trimChars` from the right<br>of `str`. For example,<br>`rtrim("xyZfooxyxyZ","xyZ")` returns<br>`"xyZfoo"`. |
| `trim(str: string)`<br>`trim(str: string, trimChars:<br>string)`                                                                   | string      | If the function does not have a second argument,<br>it removes white space from both ends of the string.<br>If the function has a second string argument, it<br>does not remove white space. Instead, it removes the<br>characters of `trimChars` from both sides<br>of `str`. For example,<br>`trim("xyZxyfooxyxyZ","xyZ")` returns<br>`"foo"`.  |
| `strlen(str: string)`                                                                                                              | number      | Returns the length of the string in Unicode code<br>points.                                                                                                                                                                                                                                                                                       |
| `toupper(str: string)`                                                                                                             | string      | Converts the string to uppercase.                                                                                                                                                                                                                                                                                                                 |
| `tolower(str: string)`                                                                                                             | string      | Converts the string to lowercase.                                                                                                                                                                                                                                                                                                                 |
| `substr(str: string, startIndex:<br>number)`<br>`substr(str: string, startIndex: number,<br>length: number)`                       | string      | Returns a substring from the index specified by<br>the number argument to the end of the string. If the<br>function has a second number argument, it contains<br>the length of the substring to be retrieved. For<br>example, `substr("xyZfooxyZ",3, 3)`<br>returns `"foo"`.                                                                      |
| `replace(fieldName: string, searchValue:<br>string, replaceValue:<br>string)`                                                      | string      | Replaces all instances of `searchValue`<br>in `fieldName: string` with<br>`replaceValue`.<br>For example, the function<br>`replace(logGroup,"smoke_test","Smoke")`<br>searches for log events where the field<br>`logGroup` contains the string value<br>`smoke_test` and replaces the value<br>with the string `Smoke`.                          |
| `regexReplace(fieldName: string, pattern:<br>string, replacement:<br>string)`                                                      | string      | Replaces all substrings matching the regular<br>expression `pattern` with<br>`replacement`. Uses RE2 regex<br>syntax.                                                                                                                                                                                                                             |
| `strcontains(str: string, searchValue:<br>string)`<br>`strcontains(str: string, searchValue:<br>string, caseInsensitive: boolean)` | number      | Returns 1 if `str` contains<br>`searchValue` and 0 otherwise. If the<br>third parameter is set to `true`, the<br>match is case-insensitive.                                                                                                                                                                                                       |
| `startsWith(str: string, searchValue:<br>string)`                                                                                  | number      | Returns 1 if `str` starts with<br>`searchValue` and 0 otherwise.                                                                                                                                                                                                                                                                                  |
| `endsWith(str: string, searchValue:<br>string)`                                                                                    | number      | Returns 1 if `str` ends with<br>`searchValue` and 0 otherwise.                                                                                                                                                                                                                                                                                    |
| `urlencode(str: string)`                                                                                                           | string      | URL-encodes the string.                                                                                                                                                                                                                                                                                                                           |
| `urldecode(str: string)`                                                                                                           | string      | URL-decodes the string.                                                                                                                                                                                                                                                                                                                           |
| `base64encode(str: string)`                                                                                                        | string      | Base64-encodes the string.                                                                                                                                                                                                                                                                                                                        |
| `base64decode(str: string)`                                                                                                        | string      | Base64-decodes the string.                                                                                                                                                                                                                                                                                                                        |
| `split(str: string, delimiter: string)`                                                                                            | array       | Splits a string by the specified delimiter and<br>returns an array of substrings.                                                                                                                                                                                                                                                                 |
| `hexToAscii(value:<br>string)`                                                                                                     | string      | Converts a hexadecimal string to ASCII<br>text.<br>Example: `fields hexToAscii("48656c6c6f") as text`                                                                                                                                                                                                                                             |
| `hexToDec(value:<br>string)`                                                                                                       | number      | Converts a hexadecimal string to a decimal<br>number.<br>Example: `fields hexToDec("0xff") as dec`                                                                                                                                                                                                                                                |
| `decToHex(value:<br>number)`                                                                                                       | string      | Converts a decimal integer to a lowercase hex<br>string with `0x` prefix. Negative<br>numbers produce `-0x` prefix.<br>Non-integers are truncated.<br>Example: `fields decToHex(255) as hex`                                                                                                                                                      |
