

# Boolean, comparison, numeric, datetime, and other functions
<a name="CWL_QuerySyntax-operations-functions"></a>

 CloudWatch Logs Insights supports many other operations and functions in queries, as explained in the following sections. 

**Topics**
+ [Arithmetic operators](#CWL_QuerySyntax-operations-arithmetic)
+ [Boolean operators](#CWL_QuerySyntax-operations-Boolean)
+ [Comparison operators](#CWL_QuerySyntax-operations-comparison)
+ [Numeric operators](#CWL_QuerySyntax-operations-numeric)
+ [Structure types](#CWL_QuerySyntax-structure-types)
+ [Datetime functions](#CWL_QuerySyntax-datetime)
+ [General functions](#CWL_QuerySyntax-general-functions)
+ [JSON functions](#CWL_QuerySyntax-json-functions)
+ [IP address string functions](#CWL_QuerySyntax-IPaddress-functions)
+ [String functions](#CWL_QuerySyntax-string-functions)

## Arithmetic operators
<a name="CWL_QuerySyntax-operations-arithmetic"></a>

 Arithmetic operators accept numeric data types as arguments and return numeric results. Use arithmetic operators in the `filter` and `fields` commands and as arguments for other functions. 


| Operation | Description | 
| --- | --- | 
| `a + b` | Addition | 
| `a - b` | Subtraction | 
| `a * b` | Multiplication | 
| `a / b` | Division | 
| `a ^ b` |  Exponentiation (`2 ^ 3` returns `8`)  | 
| `a % b` |  Remainder or modulus (`10 % 3` returns `1`)  | 

## Boolean operators
<a name="CWL_QuerySyntax-operations-Boolean"></a>

 Use the Boolean operators `and`, `or`, and `not`. 

**Note**  
 Use Boolean operators only in functions that return a value of **TRUE** or **FALSE**. 

## Comparison operators
<a name="CWL_QuerySyntax-operations-comparison"></a>

 Comparison operators accept all data types as arguments and return a Boolean result. Use comparison operations in the `filter` command and as arguments for other functions. 


| Operator | Description | 
| --- | --- | 
|  `=`  |  Equal  | 
|  `!=`  |  Not equal  | 
|  `<`  |  Less than  | 
| `>` |  Greater than  | 
| `<=` |  Less than or equal to  | 
|  `>=`  |  Greater than or equal to  | 

## Numeric operators
<a name="CWL_QuerySyntax-operations-numeric"></a>

 Numeric operations accept numeric data types as arguments and return numeric results. Use numeric operations in the `filter` and `fields` commands and as arguments for other functions. 


| Operation | Result type | Description | 
| --- | --- | --- | 
|  `abs(a: number)`  |  number  |  Absolute value  | 
|  `ceil(a: number)`  |  number  |  Round to ceiling (the smallest integer that is greater than the value of `a`)  | 
|  `floor(a: number)`  | number |  Round to floor (the largest integer that is smaller than the value of `a`)  | 
|  `greatest(a: number, ...numbers: number[])`  |  number  |  Returns the largest value  | 
|  `least(a: number, ...numbers: number[])`  | number |  Returns the smallest value  | 
|  `log(a: number)`  |  number  |  Natural log  | 
|  `round(a: number [, d: number])`  |  number  |  Rounds the value of `a`. With one argument, rounds to the nearest integer. With two arguments, rounds to `d` decimal places.  | 
|  `sqrt(a: number)`  |  number  |  Square root  | 
|  `haversine(lat1: number, lon1: number, lat2: number, lon2: number)`  |  number  |  Computes the great-circle distance in kilometers between two geographic points specified by latitude and longitude in degrees.  | 
|  `toNumber(fieldName: string)`  |  number  |  Converts a string field value to a numeric value.  | 
|  `toInt(fieldName: string)`  |  number  |  Converts a field value to an integer (32-bit).  | 
|  `toLong(fieldName: string)`  |  number  |  Converts a field value to a long integer (64-bit).  | 
|  `toDouble(fieldName: string)`  |  number  |  Converts a field value to a double-precision floating point number.  | 

## Structure types
<a name="CWL_QuerySyntax-structure-types"></a>

 A map or list is a structure type in CloudWatch Logs Insights that allows you to access and use attributes for queries. 

**Example: To get a map or list**  
 Use `jsonParse` to parse a field that's a json string into a map or a list. 

```
fields jsonParse(@message) as json_message
```

**Example: To access attributes**  
 Use the dot access operator (map.attribute) to access items in a map.. If an attribute in a map contains special characters, use backticks to enclose the attribute name (map.attributes.`special.char`). 

```
fields jsonParse(@message) as json_message
| stats count() by json_message.status_code
```

 Use the bracket access operator (list[index]) to retrieve an item at a specific position within the list. 

```
fields jsonParse(@message) as json_message
| filter json_message.users[1].action = "PutData"
```

 Wrap special characters in backticks (``) when special characters are present in the key name. 

```
fields jsonParse(@message) as json_message
| filter json_message.`user.id` = "123"
```

**Example: empty results**  
 Maps and lists are treated as null for string, number, and datetime functions. 

```
fields jsonParse(@message) as json_message
| display toupper(json_message)
```

 Comparing map and list to any other fields result in `false`. 

**Note**  
 Using map and list in `dedup`,`pattern`, `sort`, and `stats` isn't supported. 

## Datetime functions
<a name="CWL_QuerySyntax-datetime"></a>

 **Datetime functions** 

 Use datetime functions in the `fields` and `filter`commands and as arguments for other functions. Use these functions to create time buckets for queries with aggregate functions. Use time periods that consist of a number and one of the following:
+ `ms` for milliseconds 
+ `s` for seconds 
+ `m` for minutes 
+ `h` for hours 

 For example, `10m` is 10 minutes, and `1h` is 1 hour. 

**Note**  
Use the most appropriate time unit for your datetime function. CloudWatch Logs caps your request according to the time unit that you choose. For example, it caps 60 as the maximum value for any request that uses `s`. So, if you specify `bin(300s)`, CloudWatch Logs actually implements this as 60 seconds, because 60 is the number of seconds in a minute so CloudWatch Logs won't use a number higher than 60 with `s`. To create a 5-minute bucket, use `bin(5m)` instead.  
The cap for `ms` is 1000, the caps for `s` and `m` are 60, and the cap for `h` is 24.

The following table contains a list of the different datetime functions that you can use in query commands. The table lists each function's result type and contains a description of each function. 

**Tip**  
 When you create a query command, you can use the time interval selector to select a time period that you want to query. For example, you can set a time period between 5 and 30-minute intervals; 1, 3, and 12-hour intervals; or a custom time frame. You also can set time periods between specific dates. 


| Function | Result type | Description | 
| --- | --- | --- | 
| `bin(period: Period)` | Timestamp | Rounds the value of `@timestamp` to the given time period and then truncates. For example, `bin(5m)` rounds the value of `@timestamp` to the nearest 5 minutes.<br />You can use this to group multiple log entries together in a query. The following example returns the count of exceptions per hour:<pre>filter @message like /Exception/ <br />    | stats count(*) as exceptionCount by bin(1h)<br />    | sort exceptionCount desc</pre><br />The following time units and abbreviations are supported with the `bin` function. For all units and abbreviations that include more than one character, adding s to pluralize is supported. So both `hr` and `hrs` work to specify hours.+  `millisecond` `ms` `msec` <br />+  `second` `s` `sec` <br />+  `minute` `m` `min` <br />+  `hour` `h` `hr` <br />+  `day` `d`  <br />+  `week` `w`  <br />+  `month` `mo` `mon` <br />+  `quarter` `q` `qtr` <br />+  `year` `y` `yr`  | 
| `datefloor(timestamp: Timestamp, period: Period)` | Timestamp | Truncates the timestamp to the given period. For example, `datefloor(@timestamp, 1h)` truncates all values of `@timestamp` to the bottom of the hour. | 
| `dateceil(timestamp: Timestamp, period: Period)` | Timestamp | Rounds up the timestamp to the given period and then truncates. For example, `dateceil(@timestamp, 1h)` truncates all values of `@timestamp` to the top of the hour. | 
| `fromMillis(fieldName: number)` | Timestamp | Interprets the input field as the number of milliseconds since the Unix epoch and converts it to a timestamp. | 
| `toMillis(fieldName: Timestamp)` | number | Converts the timestamp found in the named field into a number representing the milliseconds since the Unix epoch. For example, `toMillis(@timestamp)` converts the timestamp `2022-01-14T13:18:031.000-08:00` to `1642195111000`. | 
| `now()` | number | Returns the time that the query processing was started, in epoch seconds. This function takes no arguments.<br />You can use this to filter your query results according to the current time.<br />For example, the following query returns all 4xx errors from the past two hours:<pre>parse @message "Status Code: *;" as statusCode\n <br />| filter statusCode >= 400 and statusCode <= 499  \n <br />| filter toMillis(@timestamp) >= (now() * 1000 - 7200000)</pre><br />The following example returns all log entries from the past five hours that contain either the word `error` or `failure`<pre>fields @timestamp, @message <br />| filter @message like /(?i)(error|failure)/ <br />| filter toMillis(@timestamp) >= (now() * 1000 - 18000000)</pre> | 
| `parseDate(fieldName: string, format: string [, timezone: string])` | number | Parses a date string to epoch milliseconds using a Java DateTimeFormatter pattern. The optional `timezone` argument specifies the time zone to use for parsing.<br />Example: `fields parseDate(field, "yyyy-MM-dd", "UTC") as epoch` | 
| `formatDate(timestamp: LogField, format: string [, timezone: string])` | string | Formats a timestamp using a strftime-style format string. Also available as the alias `strftime`. The optional `timezone` argument specifies the time zone for formatting.<br />Example: `fields formatDate(@timestamp, "%Y-%m-%d", "UTC") as date` | 

**Note**  
 Currently, CloudWatch Logs Insights doesn't support filtering logs with human readable timestamps. 

## General functions
<a name="CWL_QuerySyntax-general-functions"></a>

 **General functions** 

 Use general functions in the `fields` and `filter` commands and as arguments for other functions. 


| Function | Result type | Description | 
| --- | --- | --- | 
|  `ispresent(fieldName: LogField)`  |  Boolean  |  Returns `true` if the field exists  | 
|  `coalesce(fieldName: LogField, ...fieldNames: LogField[])`  |  LogField  |  Returns the first non-null value from the list  | 
|  `case(cond1, val1, cond2, val2, ..., [default])`  |  LogField  |  Evaluates conditions in order and returns the value for the first true condition. If no condition is true and a default is provided, returns the default. Supports up to 10 branches.  | 
|  `if(condition: Boolean, trueValue: LogField, falseValue: LogField)`  |  LogField  |  Evaluates a condition and returns `trueValue` if the condition is true, or `falseValue` otherwise.  | 
|  `isNumeric(fieldName: LogField)`  |  Boolean  |  Returns `true` if the field value can be parsed as a number. <br />Example: `filter isNumeric(@duration)` | 
|  `messageSize(fieldName: LogField)`  |  number  |  Returns the byte length of a string field. <br />Example: `fields messageSize(@message) as size` | 
|  `queryStartTime()`  |  number  |  Returns the query window start time as epoch milliseconds.  | 
|  `queryEndTime()`  |  number  |  Returns the query window end time as epoch milliseconds.  | 
|  `queryTimeRange()`  |  number  |  Returns the query window duration in milliseconds.  | 

## JSON functions
<a name="CWL_QuerySyntax-json-functions"></a>

 **JSON functions** 

 Use JSON functions in the `fields` and `filter` commands and as arguments for other functions. 


| Function | Result type | Description | 
| --- | --- | --- | 
|  `jsonParse(fieldName: string)`  |  Map \| List \| Empty  |  Returns a map or list when the input is a string representation of JSON object or a JSON array. Returns an empty value, if the input is not one of the representation.  | 
|  `jsonStringify(fieldName: Map \| List)`  |  String  |  Returns a JSON string from a map or list data.  | 
|  `jsonArraySize(fieldName: LogField)`  |  number  |  Returns the element count of a JSON array string field. <br />Example: `fields jsonArraySize(Operation) as arrayLen` | 
|  `jsonArrayContains(fieldName: LogField, value: string)`  |  Boolean  |  Returns `true` (1) if the JSON array in the field contains the specified value. Returns `false` (0) for invalid JSON, non-array, or empty array. Uses case-sensitive comparison. <br />Example: `filter jsonArrayContains(@roles, "admin")` | 

## IP address string functions
<a name="CWL_QuerySyntax-IPaddress-functions"></a>

 **IP address string functions** 

 Use IP address string functions in the `filter` and `fields` commands and as arguments for other functions. 


| Function | Result type | Description | 
| --- | --- | --- | 
| `isValidIp(fieldName: string)` | boolean | Returns `true` if the field is a valid IPv4 or IPv6 address. | 
| `isValidIpV4(fieldName: string)` | boolean | Returns `true` if the field is a valid IPv4 address. | 
| `isValidIpV6(fieldName: string)` | boolean | Returns `true` if the field is a valid IPv6 address. | 
| `isIpInSubnet(fieldName: string, subnet: string)` | boolean | Returns `true` if the field is a valid IPv4 or IPv6 address within the specified v4 or v6 subnet. When you specify the subnet, use CIDR notation such as `192.0.2.0/24` or `2001:db8::/32`, where `192.0.2.0` or `2001:db8::` is the start of the CIDR block. | 
| `isIpv4InSubnet(fieldName: string, subnet: string)` | boolean | Returns `true` if the field is a valid IPv4 address within the specified v4 subnet. When you specify the subnet, use CIDR notation such as `192.0.2.0/24` where `192.0.2.0` is the start of the CIDR block.. | 
| `isIpv6InSubnet(fieldName: string, subnet: string)` | boolean | Returns `true` if the field is a valid IPv6 address within the specified v6 subnet. When you specify the subnet, use CIDR notation such as `2001:db8::/32` where `2001:db8::` is the start of the CIDR block. | 
| `ipv4ToNumber(fieldName: string)` | number | Converts an IPv4 address string to its numeric representation. | 
| `isPrivateIP(fieldName: string)` | boolean | Returns `true` if the IP address is in a private range (RFC 1918). | 
| `isPublicIP(fieldName: string)` | boolean | Returns `true` if the IP address is publicly routable. | 
| `isReservedIP(fieldName: string)` | boolean | Returns `true` if the IP address is in a reserved range. | 

## String functions
<a name="CWL_QuerySyntax-string-functions"></a>

 **String functions** 

 Use string functions in the `fields` and `filter` commands and as arguments for other functions. 


| Function | Result type | Description | 
| --- | --- | --- | 
| `isempty(fieldName: string)` | Number | Returns `1` if the field is missing or is an empty string. | 
| `isblank(fieldName: string)` | Number | Returns `1` if the field is missing, an empty string, or contains only white space. | 
| `concat(str: string, ...strings: string[])` | string | Concatenates the strings. | 
| `ltrim(str: string)`<br />`ltrim(str: string, trimChars: string)` | string | If the function does not have a second argument, it removes white space from the left of the string. If the function has a second string argument, it does not remove white space. Instead, it removes the characters in `trimChars` from the left of `str`. For example, `ltrim("xyZxyfooxyZ","xyZ")` returns `"fooxyZ"`. | 
| `rtrim(str: string)`<br />`rtrim(str: string, trimChars: string)` | string | If the function does not have a second argument, it removes white space from the right of the string. If the function has a second string argument, it does not remove white space. Instead, it removes the characters of `trimChars` from the right of `str`. For example, `rtrim("xyZfooxyxyZ","xyZ")` returns `"xyZfoo"`. | 
| `trim(str: string)`<br />`trim(str: string, trimChars: string)` | string | If the function does not have a second argument, it removes white space from both ends of the string. If the function has a second string argument, it does not remove white space. Instead, it removes the characters of `trimChars` from both sides of `str`. For example, `trim("xyZxyfooxyxyZ","xyZ")` returns `"foo"`. | 
| `strlen(str: string)` | number | Returns the length of the string in Unicode code points. | 
| `toupper(str: string)` | string | Converts the string to uppercase. | 
| `tolower(str: string)` | string | Converts the string to lowercase. | 
| `substr(str: string, startIndex: number)`<br />`substr(str: string, startIndex: number, length: number)` | string | Returns a substring from the index specified by the number argument to the end of the string. If the function has a second number argument, it contains the length of the substring to be retrieved. For example, `substr("xyZfooxyZ",3, 3)` returns `"foo"`. | 
| `replace(fieldName: string, searchValue: string, replaceValue: string)` | string | Replaces all instances of `searchValue` in `fieldName: string` with `replaceValue`.<br />For example, the function `replace(logGroup,"smoke_test","Smoke")` searches for log events where the field `logGroup` contains the string value `smoke_test` and replaces the value with the string `Smoke`. | 
| `regexReplace(fieldName: string, pattern: string, replacement: string)` | string | Replaces all substrings matching the regular expression `pattern` with `replacement`. Uses RE2 regex syntax. | 
| `strcontains(str: string, searchValue: string)`<br />`strcontains(str: string, searchValue: string, caseInsensitive: boolean)` | number | Returns 1 if `str` contains `searchValue` and 0 otherwise. If the third parameter is set to `true`, the match is case-insensitive. | 
| `startsWith(str: string, searchValue: string)` | number | Returns 1 if `str` starts with `searchValue` and 0 otherwise. | 
| `endsWith(str: string, searchValue: string)` | number | Returns 1 if `str` ends with `searchValue` and 0 otherwise. | 
| `urlencode(str: string)` | string | URL-encodes the string. | 
| `urldecode(str: string)` | string | URL-decodes the string. | 
| `base64encode(str: string)` | string | Base64-encodes the string. | 
| `base64decode(str: string)` | string | Base64-decodes the string. | 
| `split(str: string, delimiter: string)` | array | Splits a string by the specified delimiter and returns an array of substrings. | 
| `hexToAscii(value: string)` | string | Converts a hexadecimal string to ASCII text.<br />Example: `fields hexToAscii("48656c6c6f") as text` | 
| `hexToDec(value: string)` | number | Converts a hexadecimal string to a decimal number.<br />Example: `fields hexToDec("0xff") as dec` | 
| `decToHex(value: number)` | string | Converts a decimal integer to a lowercase hex string with `0x` prefix. Negative numbers produce `-0x` prefix. Non-integers are truncated.<br />Example: `fields decToHex(255) as hex` | 