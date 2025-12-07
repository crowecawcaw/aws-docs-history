# Configurable

parser-type processors

This section contains information about the configurable data parser processors that you can use in a log event
transformer.

###### Contents

- [parseJSON](CloudWatch-Logs-Transformation-Configurable.md#CloudWatch-Logs-Transformation-parseJSON "CloudWatch-Logs-Transformation-Configurable.md#CloudWatch-Logs-Transformation-parseJSON")
- [grok](CloudWatch-Logs-Transformation-Configurable.md#CloudWatch-Logs-Transformation-Grok "CloudWatch-Logs-Transformation-Configurable.md#CloudWatch-Logs-Transformation-Grok")
  - [Grok examples](CloudWatch-Logs-Transformation-Configurable.md#Grok-Examples "CloudWatch-Logs-Transformation-Configurable.md#Grok-Examples")
    - [Example 1: Use grok to extract a field
      from unstructured logs](CloudWatch-Logs-Transformation-Configurable.md#Grok-Example1 "CloudWatch-Logs-Transformation-Configurable.md#Grok-Example1")
    - [Example 2: Use grok in combination with
      parseJSON to extract fields from a JSON log event](CloudWatch-Logs-Transformation-Configurable.md#Grok-Example3 "CloudWatch-Logs-Transformation-Configurable.md#Grok-Example3")
    - [Example 3: Grok pattern with dotted
      annotation in FIELD_NAME](CloudWatch-Logs-Transformation-Configurable.md#Grok-Example4 "CloudWatch-Logs-Transformation-Configurable.md#Grok-Example4")

  - [Supported grok patterns](CloudWatch-Logs-Transformation-Configurable.md#Grok-Patterns "CloudWatch-Logs-Transformation-Configurable.md#Grok-Patterns")
    - [Common log format examples](CloudWatch-Logs-Transformation-Configurable.md#Common-Log-Examples "CloudWatch-Logs-Transformation-Configurable.md#Common-Log-Examples")
      - [Apache log example](CloudWatch-Logs-Transformation-Configurable.md#Apache-Log-Example "CloudWatch-Logs-Transformation-Configurable.md#Apache-Log-Example")
      - [NGINX log example](CloudWatch-Logs-Transformation-Configurable.md#NGINX-Log-Example "CloudWatch-Logs-Transformation-Configurable.md#NGINX-Log-Example")
      - [Syslog Protocol (RFC 5424)
        log example](CloudWatch-Logs-Transformation-Configurable.md#syslog5424-Log-Example "CloudWatch-Logs-Transformation-Configurable.md#syslog5424-Log-Example")

- [csv](CloudWatch-Logs-Transformation-Configurable.md#CloudWatch-Logs-Transformation-csv "CloudWatch-Logs-Transformation-Configurable.md#CloudWatch-Logs-Transformation-csv")
- [parseKeyValue](CloudWatch-Logs-Transformation-Configurable.md#CloudWatch-Logs-Transformation-parseKeyValue "CloudWatch-Logs-Transformation-Configurable.md#CloudWatch-Logs-Transformation-parseKeyValue")

## parseJSON

The **parseJSON** processor parses JSON log events and
inserts extracted JSON key-value pairs under the destination. If you don't
specify a destination, the processor places the key-value pair under the root
node. When using `parseJSON` as the first processor, you must parse
the entire log event using `@message` as the source field. After the
initial JSON parsing, you can then manipulate specific fields in subsequent
processors.

The original `@message` content is not changed, the new keys are
added to the message.

| Field       | Description                                                                                                                      | Required? | Default            | Limits                                             |
| ----------- | -------------------------------------------------------------------------------------------------------------------------------- | --------- | ------------------ | -------------------------------------------------- |
| source      | Path to the field in the log event that will be parsed. Use<br>dot notation to access child fields. For example,<br>`store.book` | No        | `@message`         | Maximum length: 128<br>Maximum nested key depth: 3 |
| destination | The destination field of the parsed JSON                                                                                         | No        | `Parent JSON node` | Maximum length: 128<br>Maximum nested key depth: 3 |

**Example**

Suppose an ingested log event looks like this:

```
{
    "outer_key": {
        "inner_key": "inner_value"
    }
}
```

Then if we have this **parseJSON** processor:

```
[
   {
        "parseJSON": {
            "destination": "new_key"
        }
   }
]
```

The transformed log event would be the following.

```
{
    "new_key": {
        "outer_key": {
            "inner_key": "inner_value"
        }
    }
}
```

## grok

Use the grok processor to parse and structure unstructured data using pattern
matching. This processor can also extract fields from log messages.

| Field  | Description                                     | Required? | Default    | Limits                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         | Notes                                                                 |
| ------ | ----------------------------------------------- | --------- | ---------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------- |
| source | Path of the field to apply Grok matching on     | No        | `@message` | Maximum length: 128<br>Maximum nested key depth: 3                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| match  | The grok pattern to match against the log event | Yes       |            | Maximum length: 512<br>Maximum grok patterns: 20<br>Some grok pattern types have individual usage limits. Any<br>combination of the following patterns can be used as many as<br>five times: {URI, URIPARAM, URIPATHPARAM, SPACE, DATA,<br>GREEDYDATA, GREEDYDATA_MULTILINE}<br>Grok patterns don't support type conversions.<br>For common log format patterns (APACHE_ACCESS_LOG,<br>NGINX_ACCESS_LOG, SYSLOG5424), only DATA, GREEDYDATA, or<br>GREEDYDATA_MULTILINE patterns are supported to be included<br>after the common log pattern. | [See all supported Grok<br>patterns](#Grok-Patterns "#Grok-Patterns") |

**Structure of a Grok Pattern**

This is the supported grok pattern structure:

```
%{PATTERN_NAME:FIELD_NAME}
```

- **PATTERN_NAME**: Refers to a pre-defined
  regular expression for matching a specific type of data. Only predefined
  [grok patterns](#Grok-Patterns "#Grok-Patterns") are supported. Creating custom
  patterns is not allowed.
- **FIELD_NAME**: Assigns a name to the
  extracted value. `FIELD_NAME` is optional, but if you don't
  specify this value then the extracted data will be dropped from the
  transformed log event. If `FIELD_NAME` uses dotted notation
  (e.g., "parent.child"), it is considered as a JSON path.
- **Type Conversion**: Explicit type
  conversions are not be supported. Use [TypeConverter processor](CloudWatch-Logs-Transformation-Datatype.md#CloudWatch-Logs-Transformation-typeConverter "CloudWatch-Logs-Transformation-Datatype.md#CloudWatch-Logs-Transformation-typeConverter") to convert the datatype of any
  value extracted by grok.

To create more complex matching expressions, you can combine several grok
patterns. As many as 20 grok patterns can be combined to match a log event. For
example, this combination of patterns `%{NUMBER:timestamp} [%{NUMBER:db}
 %{IP:client_ip}:%{NUMBER:client_port}] %{GREEDYDATA:data}` can be used
to extract fields from a Redis slow log entry like this:

`1629860738.123456 [0 127.0.0.1:6379] "SET" "key1" "value1"`

### Grok examples

#### Example 1: Use grok to extract a field

from unstructured logs

Sample log:

```
293750 server-01.internal-network.local OK "[Thread-000] token generated"
```

Transformer used:

```
[
     {
         "grok": {
             "match": "%{NUMBER:version} %{HOSTNAME:hostname} %{NOTSPACE:status} %{QUOTEDSTRING:logMsg}"
         }
    }
]
```

Output:

```
{
  "version": "293750",
  "hostname": "server-01.internal-network.local",
  "status": "OK",
  "logMsg": "[Thread-000] token generated"
}
```

Sample log:

```
23/Nov/2024:10:25:15 -0900 172.16.0.1 200
```

Transformer used:

```
[
    {
        "grok": {
            "match": "%{HTTPDATE:timestamp} %{IPORHOST:clientip} %{NUMBER:response_status}"
        }
    }
]
```

Output:

```
{
  "timestamp": "23/Nov/2024:10:25:15 -0900",
  "clientip": "172.16.0.1",
  "response_status": "200"
}
```

#### Example 2: Use grok in combination with

parseJSON to extract fields from a JSON log event

Sample log:

```
{
    "timestamp": "2024-11-23T16:03:12Z",
    "level": "ERROR",
    "logMsg": "GET /page.html HTTP/1.1"
}
```

Transformer used:

```
[
     {
        "parseJSON": {}
    },
    {
         "grok": {
            "source": "logMsg",
             "match": "%{WORD:http_method} %{NOTSPACE:request} HTTP/%{NUMBER:http_version}"
         }
    }
]
```

Output:

```
{
  "timestamp": "2024-11-23T16:03:12Z",
  "level": "ERROR",
  "logMsg": "GET /page.html HTTP/1.1",
  "http_method": "GET",
  "request": "/page.html",
  "http_version": "1.1"
}
```

#### Example 3: Grok pattern with dotted

annotation in FIELD_NAME

Sample log:

```
192.168.1.1 GET /index.html?param=value 200 1234
```

Transformer used:

```
[
    {
        "grok": {
            "match": "%{IP:client.ip} %{WORD:method} %{URIPATHPARAM:request.uri} %{NUMBER:response.status} %{NUMBER:response.bytes}"
        }
    }
]
```

Output:

```
{
  "client": {
    "ip": "192.168.1.1"
  },
  "method": "GET",
  "request": {
    "uri": "/index.html?param=value"
  },
  "response": {
    "status": "200",
    "bytes": "1234"
  }
}
```

### Supported grok patterns

The following tables list the patterns that are supported by the
`grok` processor.

**General grok patterns**

| Grok Pattern         | Description                                                                                                                                                                                   | Maximum pattern limit | Example                                                                                                                                  |
| -------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------- | ---------------------------------------------------------------------------------------------------------------------------------------- |
| USERNAME or USER     | Matches one or more characters that can include lowercase<br>letters (a-z), uppercase letters (A-Z), digits (0-9), dots<br>(.), underscores (\_), or hyphens (-)                              | 20                    | Input: `user123.name-TEST`<br>Pattern: `%{USERNAME:name}`<br>Output: `{"name":<br>"user123.name-TEST"}`                                  |
| INT                  | Matches an optional plus or minus sign followed by one or<br>more digits.                                                                                                                     | 20                    | Input: `-456`<br>Pattern: `%{INT:num}`<br>Output: `{"num": "-456"}`                                                                      |
| BASE10NUM            | Matches an integer or a floating-point number with<br>optional sign and decimal point                                                                                                         | 20                    | Input: `-0.67`<br>Pattern: `%{BASE10NUM:num}`<br>Output: `{"num": "-0.67"}`                                                              |
| BASE16NUM            | Matches decimal and hexadecimal numbers with an optional<br>sign (+ or -) and an optional 0x prefix                                                                                           | 20                    | Input: `+0xA1B2`<br>Pattern: `%{BASE16NUM:num}`<br>Output: `{"num": "+0xA1B2"}`                                                          |
| POSINT               | Matches whole positive integers without leading zeros,<br>consisting of one or more digits (1-9 followed by<br>0-9)                                                                           | 20                    | Input: `123`<br>Pattern: `%{POSINT:num}`<br>Output: `{"num": "123"}`                                                                     |
| NONNEGINT            | Matches any whole numbers (consisting of one or more<br>digits 0-9) including zero and numbers with leading<br>zeros.                                                                         | 20                    | Input: `007`<br>Pattern: `%{NONNEGINT:num}`<br>Output: `{"num": "007"}`                                                                  |
| WORD                 | Matches whole words composed of one or more word<br>characters (\w), including letters, digits, and<br>underscores                                                                            | 20                    | Input: `user_123`<br>Pattern: `%{WORD:user}`<br>Output: `{"user": "user_123"}`                                                           |
| NOTSPACE             | Matches one or more non-whitespace characters.                                                                                                                                                | 5                     | Input: `hello_world123`<br>Pattern: `%{NOTSPACE:msg}`<br>Output: `{"msg": "hello_world123"}`                                             |
| SPACE                | Matches zero or more whitespace characters.                                                                                                                                                   | 5                     | Input: `" "`<br>Pattern: `%{SPACE:extra}`<br>Output: `{"extra": " "}`                                                                    |
| DATA                 | Matches any character (except newline) zero or more<br>times, non-greedy.                                                                                                                     | 5                     | Input: `abc def ghi`<br>Pattern: `%{DATA:x} %{DATA:y}`<br>Output: `{"x": "abc", "y": "def<br>ghi"}`                                      |
| GREEDYDATA           | Matches any character (except newline) zero or more<br>times, greedy.                                                                                                                         | 5                     | Input: `abc def ghi`<br>Pattern: `%{GREEDYDATA:x}<br>%{GREEDYDATA:y}`<br>Output: `{"x": "abc def", "y":<br>"ghi"}`                       |
| GREEDYDATA_MULTILINE | Matches any character (including newline) zero or more<br>times, greedy.                                                                                                                      | 1                     | Input:<br>`abc`<br>`def`<br>`ghi`<br>Pattern:<br>`%{GREEDYDATA_MULTILINE:data}`<br>Output: `{"data": "abc\ndef\nghi"}`                   |
| QUOTEDSTRING         | Matches quoted strings (single or double quotes) with<br>escaped characters.                                                                                                                  | 20                    | Input: `"Hello, world!"`<br>Pattern: `%{QUOTEDSTRING:msg}`<br>Output: `{"msg": "Hello, world!"}`                                         |
| UUID                 | Matches a standard UUID format: 8 hexadecimal characters,<br>followed by three groups of 4 hexadecimal characters, and<br>ending with 12 hexadecimal characters, all separated by<br>hyphens. | 20                    | Input:<br>`550e8400-e29b-41d4-a716-446655440000`<br>Pattern: `%{UUID:id}`<br>Output: `{"id":<br>"550e8400-e29b-41d4-a716-446655440000"}` |
| URN                  | Matches URN (Uniform Resource Name) syntax.                                                                                                                                                   | 20                    | Input: `urn:isbn:0451450523`<br>Pattern: `%{URN:urn}`<br>Output: `{"urn":<br>"urn:isbn:0451450523"}`                                     |

**AWS grok patterns**

| Pattern | Description                                                                                                                                                                                                                                                                               | Maximum pattern limit | Example                                                                                                                                                         |
| ------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| ARN     | Matches AWS Amazon Resource Names (ARNs), capturing<br>the partition (`aws`, `aws-cn`, or<br>`aws-us-gov`), service, Region, account<br>ID, and up to 5 hierarchical resource identifiers<br>separated by slashes. It will not match ARNs that are<br>missing information between colons. | 5                     | Input:<br>`arn:aws:iam:us-east-1:123456789012:user/johndoe`<br>Pattern: `%{ARN:arn}`<br>Output: `{"arn":<br>"arn:aws:iam:us-east-1:123456789012:user/johndoe"}` |

**Networking grok patterns**

| Grok Pattern     | Description                                                                                                                                                                | Maximum pattern limit | Example                                                                                                                                                  |
| ---------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------- |
| CISCOMAC         | Matches a MAC address in 4-4-4 hexadecimal<br>format.                                                                                                                      | 20                    | Input: `0123.4567.89AB`<br>Pattern: `%{CISCOMAC:MacAddress}`<br>Output: `{"MacAddress":<br>"0123.4567.89AB"}`                                            |
| WINDOWSMAC       | Matches a MAC address in hexadecimal format with<br>hyphens                                                                                                                | 20                    | Input: `01-23-45-67-89-AB`<br>Pattern: `%{WINDOWSMAC:MacAddress}`<br>Output: `{"MacAddress":<br>"01-23-45-67-89-AB"}`                                    |
| COMMONMAC        | Matches a MAC address in hexadecimal format with<br>colons.                                                                                                                | 20                    | Input: `01:23:45:67:89:AB`<br>Pattern: `%{COMMONMAC:MacAddress}`<br>Output: `{"MacAddress":<br>"01:23:45:67:89:AB"}`                                     |
| MAC              | Matches one of CISCOMAC, WINDOWSMAC or COMMONMAC grok<br>patterns                                                                                                          | 20                    | Input: `01:23:45:67:89:AB`<br>Pattern: `%{MAC:m1}`<br>Output: `{"m1":"01:23:45:67:89:AB"}`                                                               |
| IPV6             | Matches IPv6 addresses, including compressed forms and<br>IPv4-mapped IPv6 addresses.                                                                                      | 5                     | Input:<br>`2001:db8:3333:4444:5555:6666:7777:8888`<br>Pattern: `%{IPV6:ip}`<br>Output: `{"ip":<br>"2001:db8:3333:4444:5555:6666:7777:8888"}`             |
| IPV4             | Matches an IPv4 address.                                                                                                                                                   | 20                    | Input: `192.168.0.1`<br>Pattern: `%{IPV4:ip}`<br>Output: `{"ip": "192.168.0.1"}`                                                                         |
| IP               | Matches either IPv6 addresses as supported by %{IPv6} or<br>IPv4 addresses as supported by %{IPv4}                                                                         | 5                     | Input: `192.168.0.1`<br>Pattern: `%{IP:ip}`<br>Output: `{"ip": "192.168.0.1"}`                                                                           |
| HOSTNAME or HOST | Matches domain names, including subdomains                                                                                                                                 | 5                     | Input:<br>`server-01.internal-network.local`<br>Pattern: `%{HOST:host}`<br>Output: `{"host":<br>"server-01.internal-network.local"}`                     |
| IPORHOST         | Matches either a hostname or an IP address                                                                                                                                 | 5                     | Input:<br>`2001:db8:3333:4444:5555:6666:7777:8888`<br>Pattern: `%{IPORHOST:ip}`<br>Output: `{"ip":<br>"2001:db8:3333:4444:5555:6666:7777:8888"}`         |
| HOSTPORT         | Matches an IP address or hostname as supported by<br>%{IPORHOST} pattern followed by a colon and a port number,<br>capturing the port as "PORT" in the output.             | 5                     | Input: `192.168.1.1:8080`<br>Pattern: `%{HOSTPORT:ip}`<br>Output:<br>`{"ip":"192.168.1.1:8080","PORT":"8080"}`                                           |
| URIHOST          | Matches an IP address or hostname as supported by<br>%{IPORHOST} pattern, optionally followed by a colon and a<br>port number, capturing the port as "port" if<br>present. | 5                     | Input: `example.com:443 10.0.0.1`<br>Pattern: `%{URIHOST:host}<br>%{URIHOST:ip}`<br>Output:<br>`{"host":"example.com:443","port":"443","ip":"10.0.0.1"}` |

**Path grok patterns**

| Grok Pattern | Description                                                                                                      | Maximum pattern limit | Example                                                                                                                                                                                                                       |
| ------------ | ---------------------------------------------------------------------------------------------------------------- | --------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| UNIXPATH     | Matches URL paths, potentially including query<br>parameters.                                                    | 20                    | Input: `/search?q=regex`<br>Pattern: `%{UNIXPATH:path}`<br>Output: `{"path":"/search?q=regex"}`                                                                                                                               |
| WINPATH      | Matches Windows file paths.                                                                                      | 5                     | Input:<br>`C:\Users\John\Documents\file.txt`<br>Pattern: `%{WINPATH:path}`<br>Output: `{"path":<br>"C:\\Users\\John\\Documents\\file.txt"}`                                                                                   |
| PATH         | Matches either URL or Windows file paths                                                                         | 5                     | Input: `/search?q=regex`<br>Pattern: `%{PATH:path}`<br>Output: `{"path":"/search?q=regex"}`                                                                                                                                   |
| TTY          | Matches Unix device paths for terminals and<br>pseudo-terminals.                                                 | 20                    | Input: `/dev/tty1`<br>Pattern: `%{TTY:path}`<br>Output: `{"path":"/dev/tty1"}`                                                                                                                                                |
| URIPROTO     | Matches letters, optionally followed by a plus (+)<br>character and additional letters or plus (+)<br>characters | 20                    | Input: `web+transformer`<br>Pattern: `%{URIPROTO:protocol}`<br>Output:<br>`{"protocol":"web+transformer"}`                                                                                                                    |
| URIPATH      | Matches the path component of a URI                                                                              | 20                    | Input:<br>`/category/sub-category/product_name`<br>Pattern: `%{URIPATH:path}`<br>Output:<br>`{"path":"/category/sub-category/product_name"}`                                                                                  |
| URIPARAM     | Matches URL query parameters                                                                                     | 5                     | Input:<br>`?param1=value1&param2=value2`<br>Pattern: `%{URIPARAM:url}`<br>Output:<br>`{"url":"?param1=value1&param2=value2"}`                                                                                                 |
| URIPATHPARAM | Matches a URI path optionally followed by query<br>parameters                                                    | 5                     | Input:<br>`/category/sub-category/product?id=12345&color=red`<br>Pattern: `%{URIPATHPARAM:path}`<br>Output:<br>`{"path":"/category/sub-category/product?id=12345&color=red"}`                                                 |
| URI          | Matches a complete URI                                                                                           | 5                     | Input:<br>`https://user:password@example.com/path/to/resource?param1=value1&param2=value2`<br>Pattern: `%{URI:uri}`<br>Output:<br>`{"path":"https://user:password@example.com/path/to/resource?param1=value1&param2=value2"}` |

**Date and time grok patterns**

| Grok Pattern       | Description                                                                                                                                        | Maximum pattern limit                               | Example                                                                                                                                                                                                                                                                                                     |
| ------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| MONTH              | Matches full or abbreviated english month names as whole<br>words                                                                                  | 20                                                  | Input: `Jan`<br>Pattern: `%{MONTH:month}`<br>Output: `{"month":"Jan"}`<br>Input: `January`<br>Pattern: `%{MONTH:month}`<br>Output: `{"month":"January"}`                                                                                                                                                    |
| MONTHNUM           | Matches month numbers from 1 to 12, with optional leading<br>zero for single-digit months.                                                         | 20                                                  | Input: `5`<br>Pattern: `%{MONTHNUM:month}`<br>Output: `{"month":"5"}`<br>Input: `05`<br>Pattern: `%{MONTHNUM:month}`<br>Output: `{"month":"05"}`                                                                                                                                                            |
| MONTHNUM2          | Matches two-digit month numbers from 01 to 12.                                                                                                     | 20                                                  | Input: `05`<br>Pattern: `%{MONTHNUM2:month}`<br>Output: `{"month":"05"}`                                                                                                                                                                                                                                    |
| MONTHDAY           | Matches day of the month from 1 to 31, with optional<br>leading zero.                                                                              | 20                                                  | Input: `31`<br>Pattern: `%{MONTHDAY:monthDay}`<br>Output: `{"monthDay":"31"}`                                                                                                                                                                                                                               |
| YEAR               | Matches year in two or four digits                                                                                                                 | 20                                                  | Input: `2024`<br>Pattern: `%{YEAR:year}`<br>Output: `{"year":"2024"}`<br>Input: `24`<br>Pattern: `%{YEAR:year}`<br>Output: `{"year":"24"}`                                                                                                                                                                  |
| DAY                | Matches full or abbreviated day names.                                                                                                             | 20                                                  | Input: `Tuesday`<br>Pattern: `%{DAY:day}`<br>Output: `{"day":"Tuesday"}`                                                                                                                                                                                                                                    |
| HOUR               | Matches hour in 24-hour format with an optional leading<br>zero (0)0-23.                                                                           | 20                                                  | Input: `22`<br>Pattern: `%{HOUR:hour}`<br>Output: `{"hour":"22"}`                                                                                                                                                                                                                                           |
| MINUTE             | Matches minutes (00-59).                                                                                                                           | 20                                                  | Input: `59`<br>Pattern: `%{MINUTE:min}`<br>Output: `{"min":"59"}`                                                                                                                                                                                                                                           |
| SECOND             | Matches a number representing seconds (0)0-60, optionally<br>followed by a decimal point or colon and one or more digits<br>for fractional minutes | 20                                                  | Input: `3`<br>Pattern: `%{SECOND:second}`<br>Output: `{"second":"3"}`<br>Input: `30.5`<br>Pattern: `%{SECOND:minSec}`<br>Output: `{"minSec":"30.5"}`<br>Input: `30:5`<br>Pattern: `%{SECOND:minSec}`<br>Output: `{"minSec":"30:5"}`                                                                         |
| TIME               | Matches a time format with hours, minutes, and seconds in<br>the format (H)H:mm:(s)s. Seconds include leap second<br>(0)0-60.                      | 20                                                  | Input: `09:45:32`<br>Pattern: `%{TIME:time}`<br>Output: `{"time":"09:45:32"}`                                                                                                                                                                                                                               |
| DATE_US            | Matches a date in the format of (M)M/(d)d/(yy)yy or<br>(M)M-(d)d-(yy)yy.                                                                           | 20                                                  | Input: `11/23/2024`<br>Pattern: `%{DATE_US:date}`<br>Output: `{"date":"11/23/2024"}`<br>Input: `1-01-24`<br>Pattern: `%{DATE_US:date}`<br>Output: `{"date":"1-01-24"}`                                                                                                                                      |
| DATE_EU            | Matches date in format of (d)d/(M)M/(yy)yy,<br>(d)d-(M)M-(yy)yy, or (d)d.(M)M.(yy)yy.                                                              | 20                                                  | Input: `23/11/2024`<br>Pattern: `%{DATE_EU:date}`<br>Output: `{"date":"23/11/2024"}`<br>Input: `1.01.24`<br>Pattern: `%{DATE_EU:date}`<br>Output: `{"date":"1.01.24"}`                                                                                                                                      |
| ISO8601_TIMEZONE   | Matches UTC offset 'Z' or time zone offset with optional<br>colon in format [+-](H)H(:)mm.                                                         | 20                                                  | Input: `+05:30`<br>Pattern: `%{ISO8601_TIMEZONE:tz}`<br>Output: `{"tz":"+05:30"}`<br>Input: `-530`<br>Pattern: `%{ISO8601_TIMEZONE:tz}`<br>Output: `{"tz":"-530"}`<br>Input: `Z`<br>Pattern: `%{ISO8601_TIMEZONE:tz}`<br>Output: `{"tz":"Z"}`                                                               |
| ISO8601_SECOND     | Matches a number representing seconds (0)0-60, optionally<br>followed by a decimal point or colon and one or more digits<br>for fractional seconds | 20                                                  | Input: `60`<br>Pattern: `%{ISO8601_SECOND:second}`<br>Output: `{"second":"60"}`                                                                                                                                                                                                                             |
| TIMESTAMP_ISO8601  | Matches ISO8601 datetime format<br>(yy)yy-(M)M-(d)dT(H)H:mm:((s)s)(Z                                                                               | [+-](H)H:mm) with optional<br>seconds and timezone. | 20                                                                                                                                                                                                                                                                                                          | Input: `2023-05-15T14:30:00+05:30`<br>Pattern:<br>`%{TIMESTAMP_ISO8601:timestamp}`<br>Output:<br>`{"timestamp":"2023-05-15T14:30:00+05:30"}`<br>Input: `23-5-1T1:25+5:30`<br>Pattern:<br>`%{TIMESTAMP_ISO8601:timestamp}`<br>Output:<br>`{"timestamp":"23-5-1T1:25+5:30"}`<br>Input: `23-5-1T1:25Z`<br>Pattern:<br>`%{TIMESTAMP_ISO8601:timestamp}`<br>Output:<br>`{"timestamp":"23-5-1T1:25Z"}` |
| DATE               | Matches either a date in the US format using %{DATE_US}<br>or in the EU format using %{DATE_EU}                                                    | 20                                                  | Input: `11/29/2024`<br>Pattern: `%{DATE:date}`<br>Output: `{"date":"11/29/2024"}`<br>Input: `29.11.2024`<br>Pattern: `%{DATE:date}`<br>Output: `{"date":"29.11.2024"}`                                                                                                                                      |
| DATESTAMP          | Matches %{DATE} followed by %{TIME} pattern, separated by<br>space or hyphen.                                                                      | 20                                                  | Input: `29-11-2024 14:30:00`<br>Pattern: `%{DATESTAMP:dateTime}`<br>Output: `{"dateTime":"29-11-2024<br>14:30:00"}`                                                                                                                                                                                         |
| TZ                 | Matches common time zone abbreviations (PST, PDT, MST,<br>MDT, CST CDT, EST, EDT, UTC).                                                            | 20                                                  | Input: `PDT`<br>Pattern: `%{TZ:tz}`<br>Output: `{"tz":"PDT"}`                                                                                                                                                                                                                                               |
| DATESTAMP_RFC822   | Matches date and time in format: Day MonthName (D)D<br>(YY)YY (H)H:mm:(s)s Timezone                                                                | 20                                                  | Input: `Monday Jan 5 23 1:30:00 CDT`<br>Pattern:<br>`%{DATESTAMP_RFC822:dateTime}`<br>Output: `{"dateTime":"Monday Jan 5 23 1:30:00<br>CDT"}`<br>Input: `Mon January 15 2023 14:30:00<br>PST`<br>Pattern:<br>`%{DATESTAMP_RFC822:dateTime}`<br>Output: `{"dateTime":"Mon January 15 2023<br>14:30:00 PST"}` |
| DATESTAMP_RFC2822  | Matches RFC2822 date-time format: Day, (d)d MonthName<br>(yy)yy (H)H:mm:(s)s Z                                                                     | [+-](H)H:mm                                         | 20                                                                                                                                                                                                                                                                                                          | Input: `Mon, 15 May 2023 14:30:00<br>+0530`<br>Pattern:<br>`%{DATESTAMP_RFC2822:dateTime}`<br>Output: `{"dateTime":"Mon, 15 May 2023 14:30:00<br>+0530"}`<br>Input: `Monday, 15 Jan 23 14:30:00<br>Z`<br>Pattern:<br>`%{DATESTAMP_RFC2822:dateTime}`<br>Output: `{"dateTime":"Monday, 15 Jan 23 14:30:00<br>Z"}`                                                                                 |
| DATESTAMP_OTHER    | Matches date and time in format: Day MonthName (d)d<br>(H)H:mm:(s)s Timezone (yy)yy                                                                | 20                                                  | Input: `Mon May 15 14:30:00 PST<br>2023`<br>Pattern:<br>`%{DATESTAMP_OTHER:dateTime}`<br>Output: `{"dateTime":"Mon May 15 14:30:00 PST<br>2023"}`                                                                                                                                                           |
| DATESTAMP_EVENTLOG | Matches compact datetime format without separators:<br>(yy)yyMM(d)d(H)Hmm(s)s                                                                      | 20                                                  | Input: `20230515143000`<br>Pattern:<br>`%{DATESTAMP_EVENTLOG:dateTime}`<br>Output:<br>`{"dateTime":"20230515143000"}`                                                                                                                                                                                       |

**Log grok patterns**

| Grok Pattern    | Description                                                                                                                                                                                                                                                                                                                                                     | Maximum pattern limit | Example                                                                                                                                                                                                            |
| --------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| LOGLEVEL        | Matches standard log levels in different capitalizations<br>and abbreviations, including the following:<br>`Alert/ALERT`, `Trace/TRACE`,<br>`Debug/DEBUG`, `Notice/NOTICE`,<br>`Info/INFO`,<br>`Warn/Warning/WARN/WARNING`,<br>`Err/Error/ERR/ERROR`,<br>`Crit/Critical/CRIT/CRITICAL`,<br>`Fatal/FATAL`, `Severe/SEVERE`,<br>`Emerg/Emergency/EMERG/EMERGENCY` | 20                    | Input: `INFO`<br>Pattern: `%{LOGLEVEL:logLevel}`<br>Output: `{"logLevel":"INFO"}`                                                                                                                                  |
| HTTPDATE        | Matches date and time format often used in log files.<br>Format: (d)d/MonthName/(yy)yy:(H)H:mm:(s)s Timezone<br>MonthName: Matches full or abbreviated english month names<br>(Example: "Jan" or "January") Timezone: Matches %{INT} grok<br>pattern                                                                                                            | 20                    | Input: `23/Nov/2024:14:30:00 +0640`<br>Pattern: `%{HTTPDATE:date}`<br>Output: `{"date":"23/Nov/2024:14:30:00<br>+0640"}`                                                                                           |
| SYSLOGTIMESTAMP | Matches date format with MonthName (d)d (H)H:mm:(s)s<br>MonthName: Matches full or abbreviated english month names<br>(Example: "Jan" or "January")                                                                                                                                                                                                             | 20                    | Input: `Nov 29 14:30:00`<br>Pattern:<br>`%{SYSLOGTIMESTAMP:dateTime}`<br>Output: `{"dateTime":"Nov 29<br>14:30:00"}`                                                                                               |
| PROG            | Matches a program name consisting of string of letters,<br>digits, dot, underscore, forward slash, percent sign, and<br>hyphen characters.                                                                                                                                                                                                                      | 20                    | Input: `user.profile/settings-page`<br>Pattern: `%{PROG:program}`<br>Output:<br>`{"program":"user.profile/settings-page"}`                                                                                         |
| SYSLOGPROG      | Matches PROG grok pattern optionally followed by a<br>process ID in square brackets.                                                                                                                                                                                                                                                                            | 20                    | Input:<br>`user.profile/settings-page[1234]`<br>Pattern:<br>`%{SYSLOGPROG:programWithId}`<br>Output:<br>`{"programWithId":"user.profile/settings-page[1234]","program":"user.profile/settings-page","pid":"1234"}` |
| SYSLOGHOST      | Matches either a %{HOST} or %{IP} pattern                                                                                                                                                                                                                                                                                                                       | 5                     | Input:<br>`2001:db8:3333:4444:5555:6666:7777:8888`<br>Pattern: `%{SYSLOGHOST:ip}`<br>Output: `{"ip":<br>"2001:db8:3333:4444:5555:6666:7777:8888"}`                                                                 |
| SYSLOGFACILITY  | Matches syslog priority in decimal format. The value<br>should be enclosed in angular brackets (<>).                                                                                                                                                                                                                                                            | 20                    | Input: `<13.6>`<br>Pattern: `%{SYSLOGFACILITY:syslog}`<br>Output:<br>`{"syslog":"<13.6>","facility":"13","priority":"6"}`                                                                                          |

**Common log grok patterns**

You can use pre-defined custom grok patterns to match Apache, NGINX and
Syslog Protocol (RFC 5424) log formats. When you use these specific
patterns, they must be the first patterns in your matching configuration,
and no other patterns can precede them. Also, you can follow them only with
exactly one **DATA**. **GREEDYDATA** or
**GREEDYDATA_MULTILINE** pattern.

| Grok pattern      | Description                                | Maximum pattern limit |
| ----------------- | ------------------------------------------ | --------------------- |
| APACHE_ACCESS_LOG | Matches Apache access logs                 | 1                     |
| NGINX_ACCESS_LOG  | Matches NGINX access logs                  | 1                     |
| SYSLOG5424        | Matches Syslog Protocol (RFC 5424)<br>logs | 1                     |

The following shows valid and invalid examples for using these common log
format patterns.

```
"%{NGINX_ACCESS_LOG} %{DATA}" // Valid
"%{SYSLOG5424}%{DATA:logMsg}" // Valid
"%{APACHE_ACCESS_LOG} %{GREEDYDATA:logMsg}" // Valid
"%{APACHE_ACCESS_LOG} %{SYSLOG5424}" // Invalid (multiple common log patterns used)
"%{NGINX_ACCESS_LOG} %{NUMBER:num}" // Invalid (Only GREEDYDATA and DATA patterns are supported with common log patterns)
"%{GREEDYDATA:logMsg} %{SYSLOG5424}" // Invalid (GREEDYDATA and DATA patterns are supported only after common log patterns)
```

#### Common log format examples

##### Apache log example

Sample log:

```
127.0.0.1 - - [03/Aug/2023:12:34:56 +0000] "GET /page.html HTTP/1.1" 200 1234
```

Transformer:

```
[
     {
        "grok": {
            "match": "%{APACHE_ACCESS_LOG}"
        }
    }
]
```

Output:

```
{
    "request": "/page.html",
    "http_method": "GET",
    "status_code": 200,
    "http_version": "1.1",
    "response_size": 1234,
    "remote_host": "127.0.0.1",
    "timestamp": "2023-08-03T12:34:56Z"
}
```

##### NGINX log example

Sample log:

```
192.168.1.100 - Foo [03/Aug/2023:12:34:56 +0000] "GET /account/login.html HTTP/1.1" 200 42 "https://www.amazon.com/" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36"
```

Transformer:

```
[
     {
        "grok": {
            "match": "%{NGINX_ACCESS_LOG}"
        }
    }
]
```

Output:

```
{
    "request": "/account/login.html",
    "referrer": "https://www.amazon.com/",
    "agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36",
    "http_method": "GET",
    "status_code": 200,
    "auth_user": "Foo",
    "http_version": "1.1",
    "response_size": 42,
    "remote_host": "192.168.1.100",
    "timestamp": "2023-08-03T12:34:56Z"
}
```

##### Syslog Protocol (RFC 5424)

log example

Sample log:

```
<165>1 2003-10-11T22:14:15.003Z mymachine.example.com evntslog - ID47 [exampleSDID@32473 iut="3" eventSource= "Application" eventID="1011"][examplePriority@32473 class="high"]
```

Transformer:

```
[
     {
        "grok": {
            "match": "%{SYSLOG5424}"
        }
    }
]
```

Output:

```
{
  "pri": 165,
  "version": 1,
  "timestamp": "2003-10-11T22:14:15.003Z",
  "hostname": "mymachine.example.com",
  "app": "evntslog",
  "msg_id": "ID47",
  "structured_data": "exampleSDID@32473 iut=\"3\" eventSource= \"Application\" eventID=\"1011\"",
  "message": "[examplePriority@32473 class=\"high\"]"
}
```

## csv

The **csv** processor parses comma-separated values (CSV)
from the log events into columns.

| Field          | Description                                                                                   | Required? | Default                    | Limits                                                                         |
| -------------- | --------------------------------------------------------------------------------------------- | --------- | -------------------------- | ------------------------------------------------------------------------------ |
| source         | Path to the field in the log event that will be<br>parsed                                     | No        | `@message`                 | Maximum length: 128<br>Maximum nested key depth: 3                             |
| delimiter      | The character used to separate each column in the original<br>comma-separated value log event | No        | `,`                        | Maximum length: 1 unless the value is `\t`<br>or `\s`                          |
| quoteCharacter | Character used as a text qualifier for a single column of<br>data                             | No        | `"`                        | Maximum length: 1                                                              |
| columns        | List of names to use for the columns in the transformed log<br>event.                         | No        | `[column_1, column_2 ...]` | Maximum CSV columns: 100<br>Maximum length: 128<br>Maximum nested key depth: 3 |

Setting `delimiter` to `\t` will separate each column on
a tab character, and `\t` will separate each column on a single space
character.

**Example**

Suppose part of an ingested log event looks like this:

```
'Akua Mansa':28:'New York: USA'
```

Suppose we use only the **csv** processor:

```
[
     {
        "csv": {
            "delimiter": ":",
            "quoteCharacter": "'"
        }
    }
]
```

The transformed log event would be the following.

```
{
  "column_1": "Akua Mansa",
  "column_2": "28",
  "column_3": "New York: USA"
}
```

## parseKeyValue

Use the **parseKeyValue** processor to parse a specified
field into key-value pairs. You can customize the processor to parse field
information with the following options.

| Field             | Description                                                                                                  | Required? | Default    | Limits                                             |
| ----------------- | ------------------------------------------------------------------------------------------------------------ | --------- | ---------- | -------------------------------------------------- |
| source            | Path to the field in the log event that will be<br>parsed                                                    | No        | `@message` | Maximum length: 128<br>Maximum nested key depth: 3 |
| destination       | The destination field to put the extracted key-value pairs<br>into                                           | No        |            | Maximum length: 128                                |
| fieldDelimiter    | The field delimiter string that is used between key-value<br>pairs in the original log events                | No        | `&`        | Maximum length: 128                                |
| keyValueDelimiter | The delimiter string to use between the key and value in each<br>pair in the transformed log event           | No        | `=`        | Maximum length: 128                                |
| nonMatchValue     | A value to insert into the value field in the result,<br>when a key-value pair is not successfully<br>split. | No        |            | Maximum length: 128                                |
| keyPrefix         | If you want to add a prefix toall transformed keys,<br>specify it here.                                      | No        |            | Maximum length: 128                                |
| overwriteIfExists | Whether to overwrite the value if the destination key already<br>exists                                      | No        | `false`    |                                                    |

**Example**

Take the following example log event:

```
key1:value1!key2:value2!key3:value3!key4
```

Suppose we use the following processor configuration:

```
[
    {
        "parseKeyValue": {
            "destination": "new_key",
            "fieldDelimiter": "!",
            "keyValueDelimiter": ":",
            "nonMatchValue": "defaultValue",
            "keyPrefix": "parsed_"
        }
    }
]
```

The transformed log event would be the following.

```
{
  "new_key": {
    "parsed_key1": "value1",
    "parsed_key2": "value2",
    "parsed_key3": "value3",
    "parsed_key4": "defaultValue"
  }
}
```
