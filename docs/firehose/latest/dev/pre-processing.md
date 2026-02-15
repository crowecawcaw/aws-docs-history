# Pre-process data with Agents

The agent can pre-process the records parsed from monitored files before sending them
to your Firehose stream. You can enable this feature by adding the
`dataProcessingOptions` configuration setting to your file flow. One or
more processing options can be added, and they are performed in the specified
order.

The agent supports the following processing options. Because the agent is open source,
you can further develop and extend its processing options. You can download the agent
from [Kinesis Agent](https://github.com/awslabs/amazon-kinesis-agent "https://github.com/awslabs/amazon-kinesis-agent").

###### Processing Options

`SINGLELINE`

Converts a multi-line record to a single-line record by removing newline
characters, leading spaces, and trailing spaces.

```
{
    "optionName": "SINGLELINE"
}
```

`CSVTOJSON`

Converts a record from delimiter-separated format to JSON format.

```
{
    "optionName": "CSVTOJSON",
    "customFieldNames": [ "`field1`", "`field2`", `...` ],
    "delimiter": "`yourdelimiter`"
}
```

`customFieldNames`

[Required] The field names used as keys in each JSON key value
pair. For example, if you specify `["f1", "f2"]`, the
record "v1, v2" is converted to
`{"f1":"v1","f2":"v2"}`.

`delimiter`

The string used as the delimiter in the record. The default is
a comma (,).

`LOGTOJSON`

Converts a record from a log format to JSON format. The supported log
formats are **Apache Common Log**, **Apache Combined
Log**, **Apache Error Log**, and **RFC3164
Syslog**.

```
{
    "optionName": "LOGTOJSON",
    "logFormat": "`logformat`",
    "matchPattern": "`yourregexpattern`",
    "customFieldNames": [ "`field1`", "`field2`", `…` ]
}
```

`logFormat`

[Required] The log entry format. The following are possible
values:

- `COMMONAPACHELOG` — The Apache Common
  Log format. Each log entry has the following pattern by
  default: "`%{host} %{ident} %{authuser}
[%{datetime}] \"%{request}\" %{response}
%{bytes}`".
- `COMBINEDAPACHELOG` — The Apache
  Combined Log format. Each log entry has the following
  pattern by default: "`%{host} %{ident} %{authuser}
[%{datetime}] \"%{request}\" %{response} %{bytes}
%{referrer} %{agent}`".
- `APACHEERRORLOG` — The Apache Error
  Log format. Each log entry has the following pattern by
  default: "`[%{timestamp}] [%{module}:%{severity}]
[pid %{processid}:tid %{threadid}] [client:
%{client}] %{message}`".
- `SYSLOG` — The RFC3164 Syslog format.
  Each log entry has the following pattern by default:
  "`%{timestamp} %{hostname}
%{program}[%{processid}]: %{message}`".

`matchPattern`

Overrides the default pattern for the specified log format.
Use this setting to extract values from log entries if they use
a custom format. If you specify `matchPattern`, you
must also specify `customFieldNames`.

`customFieldNames`

The custom field names used as keys in each JSON key value
pair. You can use this setting to define field names for values
extracted from `matchPattern`, or override the
default field names of predefined log formats.

###### Example: LOGTOJSON Configuration

Here is one example of a `LOGTOJSON` configuration for an Apache Common
Log entry converted to JSON format:

```
{
    "optionName": "LOGTOJSON",
    "logFormat": "COMMONAPACHELOG"
}
```

Before conversion:

```
64.242.88.10 - - [07/Mar/2004:16:10:02 -0800] "GET /mailman/listinfo/hsdivision HTTP/1.1" 200 6291
```

After conversion:

```
{"host":"64.242.88.10","ident":null,"authuser":null,"datetime":"07/Mar/2004:16:10:02 -0800","request":"GET /mailman/listinfo/hsdivision HTTP/1.1","response":"200","bytes":"6291"}
```

###### Example: LOGTOJSON Configuration With Custom

Fields

Here is another example `LOGTOJSON` configuration:

```
{
    "optionName": "LOGTOJSON",
    "logFormat": "COMMONAPACHELOG",
    "customFieldNames": ["f1", "f2", "f3", "f4", "f5", "f6", "f7"]
}
```

With this configuration setting, the same Apache Common Log entry from the
previous example is converted to JSON format as follows:

```
{"f1":"64.242.88.10","f2":null,"f3":null,"f4":"07/Mar/2004:16:10:02 -0800","f5":"GET /mailman/listinfo/hsdivision HTTP/1.1","f6":"200","f7":"6291"}
```

###### Example: Convert Apache Common Log

Entry

The following flow configuration converts an Apache Common Log entry to a
single-line record in JSON format:

```
{
    "flows": [
        {
            "filePattern": "`/tmp/app.log*`",
            "deliveryStream": "`my-delivery-stream`",
            "dataProcessingOptions": [
                {
                    "optionName": "LOGTOJSON",
                    "logFormat": "COMMONAPACHELOG"
                }
            ]
        }
    ]
}
```

###### Example: Convert Multi-Line Records

The following flow configuration parses multi-line records whose first line starts
with "`[SEQUENCE=`". Each record is first converted to a single-line
record. Then, values are extracted from the record based on a tab delimiter.
Extracted values are mapped to specified `customFieldNames` values to
form a single-line record in JSON format.

```
{
    "flows": [
        {
            "filePattern": "`/tmp/app.log*`",
            "deliveryStream": "`my-delivery-stream`",
            "multiLineStartPattern": "`\\[SEQUENCE=`",
            "dataProcessingOptions": [
                {
                    "optionName": "SINGLELINE"
                },
                {
                    "optionName": "CSVTOJSON",
                    "customFieldNames": [ "`field1`", "`field2`", "`field3`" ],
                    "delimiter": "`\\t`"
                }
            ]
        }
    ]
}
```

###### Example: LOGTOJSON Configuration with Match

Pattern

Here is one example of a `LOGTOJSON` configuration for an Apache Common
Log entry converted to JSON format, with the last field (bytes) omitted:

```
{
    "optionName": "LOGTOJSON",
    "logFormat": "COMMONAPACHELOG",
    "matchPattern": "^([\\d.]+) (\\S+) (\\S+) \\[([\\w:/]+\\s[+\\-]\\d{4})\\] \"(.+?)\" (\\d{3})",
    "customFieldNames": ["host", "ident", "authuser", "datetime", "request", "response"]
}
```

Before conversion:

```
123.45.67.89 - - [27/Oct/2000:09:27:09 -0400] "GET /java/javaResources.html HTTP/1.0" 200
```

After conversion:

```
{"host":"123.45.67.89","ident":null,"authuser":null,"datetime":"27/Oct/2000:09:27:09 -0400","request":"GET /java/javaResources.html HTTP/1.0","response":"200"}
```
