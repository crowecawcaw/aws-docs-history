# Source Declarations

In Amazon Kinesis Agent for Microsoft Windows, _source declarations_ describe where and what log, event,
and metric data should be collected. They also optionally specify information for parsing that
data so that it can be transformed. The following sections describe configurations for the
built-in source types that are available in Kinesis Agent for Windows. Because Kinesis Agent for Windows is extensible, you can add custom
source types. Each source type typically requires specific key-value pairs in the configuration
objects that are relevant for that source type.

All source declarations must contain at least the following key-value pairs:

`Id`

A unique string that identifies a particular source object within the configuration
file.

`SourceType`

The name of the source type for this source object. The source type specifies the origin
of the log, event, or metric data that is being collected by this source object. It also
controls what other aspects of the source can be declared.

For examples of complete configuration files that use different kinds of source
declarations, see [Streaming from Various Sources to
Kinesis Data Streams](configuring-kaw-examples.md#configuring-kaw-examples-sources "configuring-kaw-examples.md#configuring-kaw-examples-sources").

###### Topics

- [DirectorySource Configuration](#directory-source-configuration "#directory-source-configuration")
- [ExchangeLogSource Configuration](#exchange-source-configuration "#exchange-source-configuration")
- [W3SVCLogSource Configuration](#iis-source-configuration "#iis-source-configuration")
- [UlsSource Configuration](#sharepoint-source-configuration "#sharepoint-source-configuration")
- [WindowsEventLogSource Configuration](#window-event-source-configuration "#window-event-source-configuration")
- [WindowsEventLogPollingSource Configuration](#eventlogpolling-source-configuration "#eventlogpolling-source-configuration")
- [WindowsETWEventSource Configuration](#etw-source-configuration "#etw-source-configuration")
- [WindowsPerformanceCounterSource
  Configuration](#performance-counter-source-configuration "#performance-counter-source-configuration")
- [Kinesis Agent for Windows Built-In Metrics Source](#kinesis-agent-builin-metrics-source "#kinesis-agent-builin-metrics-source")
- [List of Kinesis Agent for Windows Metrics](#kinesis-agent-metric-list "#kinesis-agent-metric-list")
- [Bookmark Configuration](#advanced-source-configuration "#advanced-source-configuration")

## DirectorySource Configuration

### Overview

The `DirectorySource` source type gathers logs from files that are stored in the
specified directory. Because log files come in many different formats, the
`DirectorySource` declaration lets you specify the format of the data in the log
file. Then you can transform the log contents to a standard format such as JSON or XML before
streaming to various AWS services.

The following is an example `DirectorySource` declaration:

```
{
	   "Id": "myLog",
	   "SourceType": "DirectorySource",
	   "Directory": "C:\\Program Data\\MyCompany\\MyService\\logs",
	   "FileNameFilter": "*.log",
	   "IncludeSubdirectories": true,
	   "IncludeDirectoryFilter": "cpu\\cpu-1;cpu\\cpu-2;load;memory",
	   "RecordParser": "Timestamp",
	   "TimestampFormat": "yyyy-MM-dd HH:mm:ss.ffff",
	   "Pattern": "\\d{4}-\\d{2}-\\d(2}",
	   "ExtractionPattern": "",
	   "TimeZoneKind": "UTC",
	   "SkipLines": 0,
	   "Encoding": "utf-16",
	   "ExtractionRegexOptions": "Multiline"
}
```

All `DirectorySource` declarations can provide the following key-value
pairs:

`SourceType`

Must be the literal string `"DirectorySource"` (required).

`Directory`

The path to the directory containing the log files (required).

`FileNameFilter`

Optionally limits the set of files in the directory where log data is collected based on a wild card file-naming pattern. If you have multiple log file name patterns, this feature allows you to use a single `DirectorySource`, as shown in the following example.

```
FileNameFilter: "*.log|*.txt"
```

System administrators sometimes compress log files before archiving them. If you specify `"*.*"` in `FileNameFilter`, known compressed files are now excluded. This feature prevents `.zip`, `.gz`, and `.bz2` files from being streamed accidentally. If this key-value pair is not specified, data from all files in the directory are collected by default.

`IncludeSubdirectories`
Specifies to monitor subdirectories to arbitrary depth limited by the operating system. This feature is useful for monitoring web servers with multiple websites. You can also use the `IncludeDirectoryFilter` attribute to monitor only certain subdirectories specified in the filter.

`RecordParser`

Specifies how the `DirectorySource` source type should parse the log files
that are found in the specified directory. This key-value pair is required, and the valid
values are as follows:

- `SingleLine` — Each line of the log file is a log record.
- `SingleLineJson` — Each line of the log file is a JSON-formatted log
  record. This parser is useful when you want to add additional key-value pairs to the JSON
  using object decoration. For more information, see [Configuring Sink
  Decorations](sink-object-declarations.md#configuring-kinesis-agent-windows-decoration-configuration "sink-object-declarations.md#configuring-kinesis-agent-windows-decoration-configuration"). For an example that
  uses the `SingleLineJson` record parser, see [Tutorial: Stream JSON Log Files to Amazon S3 Using
  Kinesis Agent for Windows](directory-source-to-s3-tutorial.md "directory-source-to-s3-tutorial.md").
- `Timestamp` — One or more lines can include a log record. The log
  record starts with a timestamp. This option requires specifying the
  `TimestampFormat` key-value pair.
- `Regex` — Each record starts with text that matches a particular
  regular expression. This option requires specifying the `Pattern` key-value
  pair.
- `SysLog` — Indicates that the log file is written in the [syslog](https://en.wikipedia.org/wiki/Syslog "https://en.wikipedia.org/wiki/Syslog") standard format. The log file is
  parsed into records based on that specification.
- `Delimited` — A simpler version of the Regex record parser where data
  items in the log records are separated by a consistent delimiter. This option is easier to
  use and executes faster than the Regex parser, and it is preferred when this option is
  available. When using this option, you must specify the `Delimiter` key-value
  pair.

`TimestampField`

Specifies which JSON field contains the timestamp for the record. This is only used with
the `SingleLineJson`
`RecordParser`. This key-value pair is optional. If it is not specified, Kinesis Agent for Windows
uses the time when the record was read for the timestamp. One advantage of specifying this
key-value pair is that latency statistics generated by Kinesis Agent for Windows are more accurate.

`TimestampFormat`

Specifies how to parse the date and time associated with the record. The value is either the string `epoch`
or a .NET
date/time format string. If the value is `epoch`, time is parsed based on UNIX Epoch time. For more information about
UNIX Epoch time, see [Unix time](https://en.wikipedia.org/wiki/Unix_time "https://en.wikipedia.org/wiki/Unix_time"). For more information about .NET date/time format strings, see [Custom Date and Time Format Strings](https://docs.microsoft.com/en-us/dotnet/standard/base-types/custom-date-and-time-format-strings "https://docs.microsoft.com/en-us/dotnet/standard/base-types/custom-date-and-time-format-strings") in the Microsoft .NET documentation). This
key-value pair is required only if the `Timestamp` record parser is specified, or the `SingleLineJson` record parser is specified along with
the `TimestampField` key-value pair.

`Pattern`

Specifies a regular expression that must match the first line of a potentially multi-line
record. This key-value pair is only required for the `Regex` record parser.

`ExtractionPattern`

Specifies a regular expression that should use named groups. The record is parsed using
this regular expression and the named groups form the fields of the parsed record. These
fields are then used as the basis for constructing JSON or XML objects or documents that are
then streamed by sinks to various AWS services. This key-value pair is optional, and is available with the `Regex` record parser and the Timestamp parser.

The `Timestamp` group name is specially processed, as it indicates to the
`Regex` parser which field contains the date and time for each record in each log
file.

`Delimiter`

Specifies the character or string that separates each item in each log record. This
key-value pair must be (and can only be) used with the `Delimited` record parser.
Use the two-character sequence `\t` to represent the tab character.

`HeaderPattern`

Specifies a regular expression for matching the line in the log file that contains the
set of headers for the record. If the log file does not contain any header information, use
the `Headers` key-value pair to specify the implicit headers. The
`HeaderPattern` key-value pair is optional and only valid for the
`Delimited` record parser.

###### Note

An empty (0 length) header entry for a column causes the data for that column to be
filtered from the final output of the `DirectorySource` parsed output.

`Headers`

Specifies the names for the columns of data parsed using the specified delimiter. This
key-value pair is optional and only valid for the `Delimited` record parser.

###### Note

An empty (0 length) header entry for a column causes the data for that column to be
filtered from the final output of the `DirectorySource` parsed output.

`RecordPattern`

Specifies a regular expression that identifies lines in the log file that contain record
data. Other than the optional header line identified by `HeaderPattern`, lines
that do not match the specified `RecordPattern` are ignored during record
processing. This key-value pair is optional and only valid for the `Delimited`
record parser. If it is not provided, the default is to consider any line that does not match
the optional `HeaderPattern` or the optional `CommentPattern` to be a
line that contains parseable record data.

`CommentPattern`

Specifies a regular expression that identifies lines in the log file that should be
excluded before parsing the data in the log file. This key-value pair is optional and only
valid for the `Delimited` record parser. If it is not provided, the default is to
consider any line that does not match the optional `HeaderPattern` to be a line
that contains parseable record data, unless `RecordPattern` is specified.

`TimeZoneKind`

Specifies whether the timestamp in the log file should be considered in the local time
zone or the UTC time zone. This is optional and defaults to UTC. The only valid values for
this key-value pair are `Local` or `UTC`. The timestamp is never
altered if `TimeZoneKind` is either not specified or if the value is UTC. The
timestamp is converted to UTC when the `TimeZoneKind` value is `Local`
and the sink receiving the timestamp is CloudWatch Logs, or the parsed record is sent to other sinks.
Dates and times that are embedded in messages are not converted.

`SkipLines`

When specified, controls the number of lines ignored at the start of each log file before
record parsing occurs. This is optional, and the default value is 0.

Encoding
By default, Kinesis Agent for Windows can automatically detect the encoding from bytemark. However, the automatic encoding may not work correctly on some older unicode formats. The following example specifies the encoding required to stream a Microsoft SQL Server log.

```
"Encoding": "utf-16"
```

For a list of encoding names, see [List of encodings](https://docs.microsoft.com/en-us/dotnet/api/system.text.encoding?view=netframework-4.8#list-of-encodings "https://docs.microsoft.com/en-us/dotnet/api/system.text.encoding?view=netframework-4.8#list-of-encodings") in Microsoft .NET documentation.

ExtractionRegexOptions
You can use `ExtractionRegexOptions` to simplify regular expressions. This key-value pair is optional. The default is `"None"`.

The following example specifies that the `"."` expression matches any character including `\r\n`.

```
"ExtractionRegexOptions" = "`Multiline`"
```

For a list of the possible fields for ExtractionRegexOptions, see the [RegExOptions Enum](https://docs.microsoft.com/en-us/dotnet/api/system.text.regularexpressions.regexoptions?view=netframework-4.7.2#fields "https://docs.microsoft.com/en-us/dotnet/api/system.text.regularexpressions.regexoptions?view=netframework-4.7.2#fields") in Microsoft .NET documentation.

### `Regex` Record Parser

You can parse unstructured text logs using the `Regex` record parser along with
the `TimestampFormat`, `Pattern`, and `ExtractionPattern`
key-value pairs. For example, suppose that your log file looks like the following:

```

[FATAL][2017/05/03 21:31:00.534][0x00003ca8][0000059c][][ActivationSubSystem][GetActivationForSystemID][0] 'ActivationException.File: EQCASLicensingSubSystem.cpp'
[FATAL][2017/05/03 21:31:00.535][0x00003ca8][0000059c][][ActivationSubSystem][GetActivationForSystemID][0] 'ActivationException.Line: 3999'

```

You can specify the following regular expression for the `Pattern` key-value pair
to help break the log file into individual log records:

```

^\[\w+\]\[(?<TimeStamp>\d{4}/\d{2}/\d{2} \d{2}:\d{2}:\d{2}\.\d{3})\]

```

This regular expression matches the following sequence:

1. The start of the string being evaluated.
2. One or more word characters surrounded by square brackets.
3. A timestamp surrounded by square brackets. The timestamp matches the following sequence:
   1. A four-digit year
   2. A forward slash
   3. A two-digit month
   4. A forward slash
   5. A two-digit day
   6. A space character
   7. A two-digit hour
   8. A colon
   9. A two-digit minute
   10. A colon
   11. A two-digit second
   12. A period
   13. A three-digit millisecond

You can specify the following format for the `TimestampFormat` key-value pair to
convert the textual timestamp into a date and time:

```
yyyy/MM/dd HH:mm:ss.fff
```

You can use the following regular expression for extracting the fields of the log record via
the `ExtractionPattern` key-value pair.

```
^\[(?<Severity>\w+)\]\[(?<TimeStamp>\d{4}/\d{2}/\d{2} \d{2}:\d{2}:\d{2}\.\d{3})\]\[[^]]*\]\[[^]]*\]\[[^]]*\]\[(?<SubSystem>\w+)\]\[(?<Module>\w+)\]\[[^]]*\] '(?<Message>.*)'$
```

This regular expression matches the following groups in sequence:

1. `Severity` — One or more word characters surrounded by square brackets.
2. `TimeStamp` — See the previous description for the timestamp.
3. Three unnamed square bracketed sequences of zero or more characters are skipped.
4. `SubSystem` — One or more word characters surrounded by square brackets.
5. `Module` — One or more word characters surrounded by square brackets.
6. One unnamed square bracketed sequence of zero or more characters is skipped.
7. One unnamed space is skipped.
8. `Message` — Zero or more characters surrounded by single quotes.

The following source declaration combines these regular expressions and the date time format to provide the complete instructions to Kinesis Agent for Windows for parsing this kind of log file.

```
{
    "Id": "PrintLog",
    "SourceType": "DirectorySource",
    "Directory": "C:\\temp\\PrintLogTest",
    "FileNameFilter": "*.log",
    "RecordParser": "Regex",
    "TimestampFormat": "yyyy/MM/dd HH:mm:ss.fff",
    "Pattern": "^\\[\\w+\\]\\[(?<TimeStamp>\\d{4}/\\d{2}/\\d{2} \\d{2}:\\d{2}:\\d{2}\\.\\d{3})\\]",
    "ExtractionPattern": "^\\[(?<Severity>\\w+)\\]\\[(?<TimeStamp>\\d{4}/\\d{2}/\\d{2} \\d{2}:\\d{2}:\\d{2}\\.\\d{3})\\]\\[[^]]*\\]\\[[^]]*\\]\\[[^]]*\\]\\[(?<SubSystem>\\w+)\\]\\[(?<Module>\\w+)\\]\\[[^]]*\\] '(?<Message>.*)'$",
    "TimeZoneKind": "UTC"
}
```

###### Note

Backslashes in JSON-formatted files must be escaped with an additional backslash.

For more information about regular expressions, see [Regular Expression Language - Quick Reference](https://docs.microsoft.com/en-us/dotnet/standard/base-types/regular-expression-language-quick-reference "https://docs.microsoft.com/en-us/dotnet/standard/base-types/regular-expression-language-quick-reference") in the Microsoft .NET
documentation.

### `Delimited` Record Parser

You can use the `Delimited` record parser to parse semistructured log and data
files where there is a consistent character sequence separating each column of data in each row
of data. For example, CSV files use a comma to separate each column of data, and TSV files use a
tab.

Suppose that you want to parse a Microsoft [NPS Database Format](<https://docs.microsoft.com/en-us/previous-versions/windows/it-pro/windows-server-2008-R2-and-2008/cc771748(v=ws.10)> "https://docs.microsoft.com/en-us/previous-versions/windows/it-pro/windows-server-2008-R2-and-2008/cc771748(v=ws.10)") log file produced by a Network policy server. Such a file might
look like the following:

```
"NPS-MASTER","IAS",03/22/2018,23:07:55,1,"user1","Domain1\user1",,,,,,,,0,"192.168.86.137","Nate - Test 1",,,,,,,1,,0,"311 1 192.168.0.213 03/15/2018 08:14:29 1",,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,"Use Windows authentication for all users",1,,,,
"NPS-MASTER","IAS",03/22/2018,23:07:55,3,,"Domain1\user1",,,,,,,,0,"192.168.86.137","Nate - Test 1",,,,,,,1,,16,"311 1 192.168.0.213 03/15/2018 08:14:29 1",,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,"Use Windows authentication for all users",1,,,,
```

The following example `appsettings.json` configuration file includes a
`DirectorySource` declaration that uses the `Delimited` record parser to
parse this text into an object representation. It then streams JSON-formatted data to
Firehose:

```
{
    "Sources": [
        {
            "Id": "NPS",
            "SourceType": "DirectorySource",
            "Directory": "C:\\temp\\NPS",
            "FileNameFilter": "*.log",
            "RecordParser": "Delimited",
            "Delimiter": ",",
            "Headers": "ComputerName,ServiceName,Record-Date,Record-Time,Packet-Type,User-Name,Fully-Qualified-Distinguished-Name,Called-Station-ID,Calling-Station-ID,Callback-Number,Framed-IP-Address,NAS-Identifier,NAS-IP-Address,NAS-Port,Client-Vendor,Client-IP-Address,Client-Friendly-Name,Event-Timestamp,Port-Limit,NAS-Port-Type,Connect-Info,Framed-Protocol,Service-Type,Authentication-Type,Policy-Name,Reason-Code,Class,Session-Timeout,Idle-Timeout,Termination-Action,EAP-Friendly-Name,Acct-Status-Type,Acct-Delay-Time,Acct-Input-Octets,Acct-Output-Octets,Acct-Session-Id,Acct-Authentic,Acct-Session-Time,Acct-Input-Packets,Acct-Output-Packets,Acct-Terminate-Cause,Acct-Multi-Ssn-ID,Acct-Link-Count,Acct-Interim-Interval,Tunnel-Type,Tunnel-Medium-Type,Tunnel-Client-Endpt,Tunnel-Server-Endpt,Acct-Tunnel-Conn,Tunnel-Pvt-Group-ID,Tunnel-Assignment-ID,Tunnel-Preference,MS-Acct-Auth-Type,MS-Acct-EAP-Type,MS-RAS-Version,MS-RAS-Vendor,MS-CHAP-Error,MS-CHAP-Domain,MS-MPPE-Encryption-Types,MS-MPPE-Encryption-Policy,Proxy-Policy-Name,Provider-Type,Provider-Name,Remote-Server-Address,MS-RAS-Client-Name,MS-RAS-Client-Version",
            "TimestampField": "{Record-Date} {Record-Time}",
            "TimestampFormat": "MM/dd/yyyy HH:mm:ss"
        }
    ],
    "Sinks": [
        {
            "Id": "npslogtest",
            "SinkType": "KinesisFirehose",
            "Region": "us-west-2",
            "StreamName": "npslogtest",
            "Format": "json"
        }
    ],
    "Pipes": [
        {
            "Id": "W3SVCLog1ToKinesisStream",
            "SourceRef": "NPS",
            "SinkRef": "npslogtest"
        }
    ]
}
```

JSON-formatted data streamed to Firehose looks like the following:

```
{
    "ComputerName": "NPS-MASTER",
    "ServiceName": "IAS",
    "Record-Date": "03/22/2018",
    "Record-Time": "23:07:55",
    "Packet-Type": "1",
    "User-Name": "user1",
    "Fully-Qualified-Distinguished-Name": "Domain1\\user1",
    "Called-Station-ID": "",
    "Calling-Station-ID": "",
    "Callback-Number": "",
    "Framed-IP-Address": "",
    "NAS-Identifier": "",
    "NAS-IP-Address": "",
    "NAS-Port": "",
    "Client-Vendor": "0",
    "Client-IP-Address": "192.168.86.137",
    "Client-Friendly-Name": "Nate - Test 1",
    "Event-Timestamp": "",
    "Port-Limit": "",
    "NAS-Port-Type": "",
    "Connect-Info": "",
    "Framed-Protocol": "",
    "Service-Type": "",
    "Authentication-Type": "1",
    "Policy-Name": "",
    "Reason-Code": "0",
    "Class": "311 1 192.168.0.213 03/15/2018 08:14:29 1",
    "Session-Timeout": "",
    "Idle-Timeout": "",
    "Termination-Action": "",
    "EAP-Friendly-Name": "",
    "Acct-Status-Type": "",
    "Acct-Delay-Time": "",
    "Acct-Input-Octets": "",
    "Acct-Output-Octets": "",
    "Acct-Session-Id": "",
    "Acct-Authentic": "",
    "Acct-Session-Time": "",
    "Acct-Input-Packets": "",
    "Acct-Output-Packets": "",
    "Acct-Terminate-Cause": "",
    "Acct-Multi-Ssn-ID": "",
    "Acct-Link-Count": "",
    "Acct-Interim-Interval": "",
    "Tunnel-Type": "",
    "Tunnel-Medium-Type": "",
    "Tunnel-Client-Endpt": "",
    "Tunnel-Server-Endpt": "",
    "Acct-Tunnel-Conn": "",
    "Tunnel-Pvt-Group-ID": "",
    "Tunnel-Assignment-ID": "",
    "Tunnel-Preference": "",
    "MS-Acct-Auth-Type": "",
    "MS-Acct-EAP-Type": "",
    "MS-RAS-Version": "",
    "MS-RAS-Vendor": "",
    "MS-CHAP-Error": "",
    "MS-CHAP-Domain": "",
    "MS-MPPE-Encryption-Types": "",
    "MS-MPPE-Encryption-Policy": "",
    "Proxy-Policy-Name": "Use Windows authentication for all users",
    "Provider-Type": "1",
    "Provider-Name": "",
    "Remote-Server-Address": "",
    "MS-RAS-Client-Name": "",
    "MS-RAS-Client-Version": ""
}
```

### `SysLog` Record Parser

For the `SysLog` record parser, the parsed output from the source includes the
following information:

| Attribute         | Type   | Description                                                         |
| ----------------- | ------ | ------------------------------------------------------------------- |
| `SysLogTimeStamp` | String | The original date and time from the syslog-formatted log file.      |
| `Hostname`        | String | The name of computer where the syslog-formatted log file resides.   |
| `Program`         | String | The name of the application or service that generated the log file. |
| `Message`         | String | The log message generated by the application or service.            |
| `TimeStamp`       | String | The parsed date and time in ISO 8601 format.                        |

The following is an example of SysLog data transformed into JSON:

```
{
    "SysLogTimeStamp": "Jun 18 01:34:56",
    "Hostname": "myhost1.example.mydomain.com",
    "Program": "mymailservice:",
    "Message": "Info: ICID 123456789 close",
    "TimeStamp": "2017-06-18T01:34.56.000"
}
```

### Summary

The following is a summary of the key-value pairs available for the
`DirectorySource` source and the `RecordParser`s related to those
key-value pairs.

| Key Name            | RecordParser                                                                                              | Notes                                                            |
| ------------------- | --------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------- |
| `SourceType`        | Required for all                                                                                          | Must have the value `DirectorySource`                            |
| `Directory`         | Required for all                                                                                          |                                                                  |
| `FileNameFilter`    | Optional for all                                                                                          |                                                                  |
| `RecordParser`      | Required for all                                                                                          |                                                                  |
| `TimestampField`    | Optional for `SingleLineJson`                                                                             |                                                                  |
| `TimestampFormat`   | Required for `Timestamp`, and required for `SingleLineJson` if<br>`TimestampField` is specified           |                                                                  |
| `Pattern`           | Required for `Regex`                                                                                      |                                                                  |
| `ExtractionPattern` | Optional for `Regex`                                                                                      | Required for `Regex` if sink specifies `json` or `xml`<br>format |
| `Delimiter`         | Required for `Delimited`                                                                                  |                                                                  |
| `HeaderPattern`     | Optional for `Delimited`                                                                                  |                                                                  |
| `Headers`           | Optional for `Delimited`                                                                                  |                                                                  |
| `RecordPattern`     | Optional for `Delimited`                                                                                  |                                                                  |
| `CommentPattern`    | Optional for `Delimited`                                                                                  |                                                                  |
| `TimeZoneKind`      | Optional for `Regex`, `Timestamp`, `SysLog`, and<br>`SingleLineJson` when a timestamp field is identified |                                                                  |
| `SkipLines`         | Optional for all                                                                                          |                                                                  |

## ExchangeLogSource Configuration

The `ExchangeLogSource` type is used to collect logs from Microsoft Exchange.
Exchange produces logs in several different kinds of log formats. This source type parses all of
them. Although it is possible to parse them using the `DirectorySource` type with the
`Regex` record parser, it is much simpler to use the `ExchangeLogSource`.
This is because you don't need to design and provide regular expressions for the log file
formats. The following is an example `ExchangeLogSource` declaration:

```
{
   "Id": "MyExchangeLog",
   "SourceType": "ExchangeLogSource",
   "Directory": "C:\\temp\\ExchangeLogTest",
   "FileNameFilter": "*.log"
}
```

All exchange declarations can provide the following key-value pairs:

`SourceType`

Must be the literal string `"ExchangeLogSource"` (required).

`Directory`

The path to the directory containing the log files (required).

`FileNameFilter`

Optionally limits the set of files in the directory where log data is collected based on
a wildcard file-naming pattern. If this key-value pair is not specified, then by default, log
data from all files in the directory is collected.

`TimestampField`

The name of the column containing the date and time for the record. This key-value pair
is optional and need not be specified if the field name is `date-time` or
`DateTime`. Otherwise, it is required.

## W3SVCLogSource Configuration

The `W3SVCLogSource` type is used to collect logs from Internet Information
Services (IIS) for Windows.

The following is an example `W3SVCLogSource` declaration:

```
{
   "Id": "MyW3SVCLog",
   "SourceType": "W3SVCLogSource",
   "Directory": "C:\\inetpub\\logs\\LogFiles\\W3SVC1",
   "FileNameFilter": "*.log"
}
```

All `W3SVCLogSource` declarations can provide the following key-value
pairs:

`SourceType`

Must be the literal string `"W3SVCLogSource"` (required).

`Directory`

The path to the directory containing the log files (required).

`FileNameFilter`

Optionally limits the set of files in the directory where log data is collected based on
a wildcard file-naming pattern. If this key-value pair is not specified, then by default, log
data from all files in the directory is collected.

## UlsSource Configuration

The `UlsSource` type is used to collect logs from Microsoft SharePoint. The
following is an example `UlsSource` declaration:

```
{
    "Id": "UlsSource",
    "SourceType": "UlsSource",
    "Directory": "C:\\temp\\uls",
    "FileNameFilter": "*.log"
}
```

All `UlsSource` declarations can provide the following key-value pairs:

`SourceType`

Must be the literal string `"UlsSource"` (required).

`Directory`

The path to the directory containing the log files (required).

`FileNameFilter`

Optionally limits the set of files in the directory where log data is collected based on
a wildcard file-naming pattern. If this key-value pair is not specified, then by default, log
data from all files in the directory is collected.

## WindowsEventLogSource Configuration

The `WindowsEventLogSource` type is used to collect events from the Windows
Event Log service. The following is an example `WindowsEventLogSource` declaration:

```
{
    "Id": "mySecurityLog",
    "SourceType": "WindowsEventLogSource",
    "LogName": "Security"
}
```

All `WindowsEventLogSource` declarations can provide the following key-value
pairs:

`SourceType`

Must be the literal string `"WindowsEventLogSource"` (required).

`LogName`

Events are collected from the specified log. Common values include
`Application`, `Security`, and `System`, but you can specify
any valid Windows event log name. This key-value pair is required.

`Query`

Optionally limits what events are output from the `WindowsEventLogSource`. If
this key-value pair is not specified, then by default, all events are output. For information
about the syntax of this value, see [Event Queries and Event
XML](<https://msdn.microsoft.com/en-us/library/bb399427(v=vs.90).aspx> "https://msdn.microsoft.com/en-us/library/bb399427(v=vs.90).aspx") in the Windows documentation. For information about log level definitions, see
[Event
Types](https://docs.microsoft.com/en-us/windows/desktop/eventlog/event-types "https://docs.microsoft.com/en-us/windows/desktop/eventlog/event-types") in the Windows documentation.

`IncludeEventData`

Optionally enables the collection and streaming of provider-specific event data
associated with events from the specified Windows event log when the value of this key-value
pair is `"true"`. Only event data that can be successfully serialized is included.
This key-value pair is optional, and if it is not specified, the provider-specific event data
is not collected.

###### Note

Including event data could significantly increase the amount of data streamed from this source. The maximum size of an event can be 262,143 bytes with event data included.

The parsed output from the `WindowsEventLogSource` contains the following
information:

| Attribute          | Type            | Description                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| ------------------ | --------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `EventId`          | Int             | The identifier of the type of event.                                                                                                                                                                                                                                                                                                                                                                                                           |
| `Description`      | String          | Text that describes the details of the event.                                                                                                                                                                                                                                                                                                                                                                                                  |
| `LevelDisplayName` | String          | The category of event (one of Error, Warning, Information, Success Audit, Failure<br>Audit).                                                                                                                                                                                                                                                                                                                                                   |
| `LogName`          | String          | Where the event was recorded (typical values are `Application`,<br>`Security`, and `System`, but there are many possibilities).                                                                                                                                                                                                                                                                                                                |
| `MachineName`      | String          | Which computer recorded the event.                                                                                                                                                                                                                                                                                                                                                                                                             |
| `ProviderName`     | String          | Which application or service recorded the event.                                                                                                                                                                                                                                                                                                                                                                                               |
| `TimeCreated`      | String          | When the event occurred in ISO 8601 format.                                                                                                                                                                                                                                                                                                                                                                                                    |
| `Index`            | Int             | Where the entry is located in the log.                                                                                                                                                                                                                                                                                                                                                                                                         |
| `UserName`         | String          | Who made the entry if known.                                                                                                                                                                                                                                                                                                                                                                                                                   |
| `Keywords`         | String          | The type of event. Standard values include `AuditFailure` (failed security<br>audit events), `AuditSuccess` (successful security audit events),<br>`Classic` (events raised with the `RaiseEvent` function),<br>`Correlation Hint` (transfer events), `SQM` (Service Quality Mechanism<br>events), `WDI Context` (Windows Diagnostic Infrastructure context events), and<br>`WDI Diag` (Windows Diagnostic Infrastructure diagnostics events). |
| `EventData`        | List of objects | Optional provider-specific extra data about the log event. This is only included if the<br>value for the `IncludeEventData` key-value pair is `"true"`.                                                                                                                                                                                                                                                                                        |

The following is an example event transformed into JSON:

```
{[
    "EventId": 7036,
    "Description": "The Amazon SSM Agent service entered the stopped state.",
    "LevelDisplayName": "Informational",
    "LogName": "System",
    "MachineName": "mymachine.mycompany.com",
    "ProviderName": "Service Control Manager",
    "TimeCreated": "2017-10-04T16:42:53.8921205Z",
    "Index": 462335,
    "UserName": null,
    "Keywords": "Classic",
    "EventData": [
    "Amazon SSM Agent",
    "stopped",
    "rPctBAMZFhYubF8zVLcrBd3bTTcNzHvY5Jc2Br0aMrxxx=="
]}
```

## WindowsEventLogPollingSource Configuration

`WindowsEventLogPollingSource` uses a polling-based mechanism to gather all new events from the event log that match the configured parameters. The polling interval is updated dynamically between 100 ms and 5000 ms depending on how many events were gathered during the last poll. The following is an example `WindowsEventLogPollingSource` declaration:

```
{
    "Id": "MySecurityLog",
    "SourceType": "WindowsEventLogPollingSource",
    "LogName": "Security",
    "IncludeEventData": "true",
    "Query": "",
    "CustomFilters": "ExcludeOwnSecurityEvents"
}
```

All `WindowsEventLogPollingSource` declarations can provide the following
key-value pairs:

`SourceType`

Must be the literal string `"WindowsEventLogPollingSource"`
(required).

`LogName`

Specifies the log. Valid options are `Application`, `Security`, `System`, or other valid logs.

`IncludeEventData`

Optional. When `true`, specifies that extra EventData when streamed as JSON and XML is included. Default is `false`.

`Query`
Optional. Windows event logs support querying events using XPath expressions, which you can specify using `Query`. For more information, see [Event Queries and Event XML](<https://docs.microsoft.com/en-us/previous-versions/bb399427(v=vs.90)> "https://docs.microsoft.com/en-us/previous-versions/bb399427(v=vs.90)") in Microsoft documentation.

`CustomFilters`

Optional. A list of filters separated by a semi-colon (`;`). The following filters can be specified.

`ExcludeOwnSecurityEvents`
Excludes security events generated by Kinesis Agent for Windows itself.

## WindowsETWEventSource Configuration

The `WindowsETWEventSource` type is used to collect application and service
event traces using a feature named Event Tracing for Windows (ETW). For more information, see
[Event
Tracing](https://docs.microsoft.com/en-us/windows/desktop/etw/event-tracing-portal "https://docs.microsoft.com/en-us/windows/desktop/etw/event-tracing-portal") in the Windows documentation.

The following is an example `WindowsETWEventSource` declaration:

```
{
    "Id": "ClrETWEventSource",
    "SourceType": "WindowsETWEventSource",
    "ProviderName": "Microsoft-Windows-DotNETRuntime",
    "TraceLevel": "Verbose",
    "MatchAnyKeyword": 32768
}
```

All `WindowsETWEventSource` declarations can provide the following key-value
pairs:

`SourceType`

Must be the literal string `"WindowsETWEventSource"` (required).

`ProviderName`

Specifies which event provider to use to collect trace events. This must be a valid ETW
provider name for an installed provider. To determine which providers are installed, execute
the following in a Windows command prompt window:

```
logman query providers
```

`TraceLevel`

Specifies what categories of trace events should be collected. Allowed values include
`Critical`, `Error`, `Warning`, `Informational`,
and `Verbose`. The exact meaning depends on the ETW provider that is
selected.

`MatchAnyKeyword`

This value is a 64-bit number, in which each bit represents an individual keyword. Each
keyword describes a category of events to be collected. For the supported keywords and their
values and how they related to `TraceLevel`, see the documentation for that
provider. For example, for information about the CLR ETW provider, see [CLR ETW Keywords and Levels](https://docs.microsoft.com/en-us/dotnet/framework/performance/clr-etw-keywords-and-levels "https://docs.microsoft.com/en-us/dotnet/framework/performance/clr-etw-keywords-and-levels") in the Microsoft .NET Framework documentation.

In the previous example, 32768 (0x00008000) represents the `ExceptionKeyword`
for the CLR ETW provider that instructs the provider to collect information about exceptions
thrown. Although JSON doesn't natively support hex constants, you can specify them for
`MatchAnyKeyword` by placing them in a string. You can also specify several
constants separated by commas. For example, use the following to specify both the
`ExceptionKeyword` and `SecurityKeyword` (0x00000400):

```
{
   "Id": "MyClrETWEventSource",
   "SourceType": "WindowsETWEventSource",
   "ProviderName": "Microsoft-Windows-DotNETRuntime",
   "TraceLevel": "Verbose",
   "MatchAnyKeyword": "0x00008000, 0x00000400"
}
```

To ensure that all specified keywords are enabled for a provider, multiple keyword values
are combined using OR and passed to that provider.

The output from the `WindowsETWEventSource` contains the following information
for each event:

| Attribute           | Type      | Description                                                                                                                                                                        |
| ------------------- | --------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `EventName`         | String    | What kind of event occurred.                                                                                                                                                       |
| `ProviderName`      | String    | Which provider detected the event.                                                                                                                                                 |
| `FormattedMessage`  | String    | A textual summary of the event.                                                                                                                                                    |
| `ProcessID`         | Int       | Which process reported the event.                                                                                                                                                  |
| `ExecutingThreadID` | Int       | Which thread within the process reported the event.                                                                                                                                |
| `MachineName`       | String    | The name of the desktop or server that is reporting the event.                                                                                                                     |
| `Payload`           | Hashtable | A table with a string key and any kind of object as a value. The key is the payload<br>item name, and the value is the payload item's value. The payload is provider<br>dependent. |

The following is an example event transformed into JSON:

```
{
     "EventName": "Exception/Start",
     "ProviderName": "Microsoft-Windows-DotNETRuntime",
     "FormattedMessage": "ExceptionType=System.Exception;\r\nExceptionMessage=Intentionally unhandled exception.;\r\nExceptionEIP=0x2ab0499;\r\nExceptionHRESULT=-2,146,233,088;\r\nExceptionFlags=CLSCompliant;\r\nClrInstanceID=9 ",
     "ProcessID": 3328,
     "ExecutingThreadID": 6172,
     "MachineName": "MyHost.MyCompany.com",
     "Payload":
      {
        "ExceptionType": "System.Exception",
        "ExceptionMessage": "Intentionally unhandled exception.",
        "ExceptionEIP": 44762265,
        "ExceptionHRESULT": -2146233088,
        "ExceptionFlags": 16,
        "ClrInstanceID": 9
      }
}
```

## WindowsPerformanceCounterSource

Configuration

The `WindowsPerformanceCounterSource` type collects performance counter metrics
from Windows. The following is an example `WindowsPerformanceCounterSource`
declaration:

```
{
	"Id": "MyPerformanceCounter",
	"SourceType": "WindowsPerformanceCounterSource",
	"Categories": [{
			"Category": "Server",
			"Counters": ["Files Open", "Logon Total", "Logon/sec", "Pool Nonpaged Bytes"]
		},
		{
			"Category": "System",
			"Counters": ["Processes", "Processor Queue Length", "System Up Time"]
		},
		{
			"Category": "LogicalDisk",
			"Instances": "*",
			"Counters": [
				"% Free Space", "Avg. Disk Queue Length",
				{
					"Counter": "Disk Reads/sec",
					"Unit": "Count/Second"
				},
				"Disk Writes/sec"
			]
		},
		{
			"Category": "Network Adapter",
			"Instances": "^Local Area Connection\* \d$",
			"Counters": ["Bytes Received/sec", "Bytes Sent/sec"]
		}
	]
}
```

All `WindowsPerformanceCounterSource` declarations can provide the following
key-value pairs:

`SourceType`

Must be the literal string `"WindowsPerformanceCounterSource"`
(required).

`Categories`

Specifies a set of performance counter metric groups to gather from Windows. Each metric
group contains the following key-value pairs:

`Category`

Specifies the counter set of metrics to be collected (required).

`Instances`

Specifies the set of objects of interest when there are a unique set of performance
counters per object. For example, when the category is `LogicalDisk`, there are
a set of performance counters per disk drive. This key-value pair is optional. You can use
the wildcards `*` and `?` to match multiple instances. To aggregate
values across all instances, specify `_Total`.

You can also use `InstanceRegex`, which accepts regular expressions that contain the `*` wild card character as part of the instance name.

`Counters`

Specifies which metrics to gather for the specified category. This key-value pair is
required. You can use the wildcards `*` and `?` to match multiple
counters. You can specify `Counters` using only the name, or by using the name
and unit. If counter units are not specified, Kinesis Agent for Windows attempts to infer the units from the
name. If those inferences are incorrect, then the unit can be explicitly specified. You can
change `Counter` names if you want. The more complex representation of a counter
is an object with the following key-value pairs:

`Counter`

The name of the counter. This key-value pair is required.

`Rename`

The name of the counter to present to the sink. This key-value pair is
optional.

`Unit`

The meaning of the value that is associated with the counter. For a complete list
of valid unit names, see the unit documentation in [MetricDatum](../../../AmazonCloudWatch/latest/APIReference/API_MetricDatum.md "../../../AmazonCloudWatch/latest/APIReference/API_MetricDatum.md") in the _Amazon CloudWatch API Reference_.

The following is an example of a complex counter specification:

```

{
   "Counter": "Disk Reads/sec,
   "Rename": "Disk Reads per second",
   "Unit": "Count/Second"
}

```

`WindowsPerformanceCounterSource` can only be used with a pipe that specifies an
Amazon CloudWatch sink. Use a separate sink if Kinesis Agent for Windows built-in metrics are also streamed to CloudWatch. Examine
the Kinesis Agent for Windows log after service startup to determine what units have been inferred for counters when
units have not been specified in the `WindowsPerformanceCounterSource` declarations.
Use PowerShell to determine the valid names for categories, instances, and counters.

To see information about all categories, including counters associated with counter sets,
execute this command in a PowerShell window:

```

    Get-Counter -ListSet * | Sort-Object

```

To determine what instances are available for each of the counters in the counter set,
execute a command similar to the following example in a PowerShell window:

```

    Get-Counter -Counter "\Process(*)\% Processor Time"

```

The value of the `Counter` parameter should be one of the paths from a
`PathsWithInstances` member listed by the previous `Get-Counter -ListSet`
command invocation.

## Kinesis Agent for Windows Built-In Metrics Source

In addition to ordinary metrics sources such as the
`WindowsPerformanceCounterSource` type (see [WindowsPerformanceCounterSource
Configuration](#performance-counter-source-configuration "#performance-counter-source-configuration")), the CloudWatch sink type can receive
metrics from a special source that gathers metrics about Kinesis Agent for Windows itself. Kinesis Agent for Windows metrics are also
available in the `KinesisTap` category of Windows performance counters.

The `MetricsFilter` key-value pair for the CloudWatch sink declarations specifies which
metrics are streamed to CloudWatch from the built-in Kinesis Agent for Windows metrics source. The value is a string that
contains one or more filter expressions separated by semicolons; for example:

`"MetricsFilter": "`_FilterExpression1_`;`_FilterExpression2_`"`

A metric that matches one or more filter expressions is streamed to CloudWatch.

Single instance metrics are global in nature and not tied to a particular source or sink.
Multiple instance metrics are dimensional based on the source or sink declaration
`Id`. Each source or sink type can have a different set of metrics.

For a list of built-in Kinesis Agent for Windows metric names, see [List of Kinesis Agent for Windows Metrics](#kinesis-agent-metric-list "#kinesis-agent-metric-list").

For single instance metrics, the filter expression is the name of the metric; for
example:

```

"MetricsFilter": "SourcesFailedToStart;SinksFailedToStart"

```

For multiple instance metrics, the filter expression is the name of the metric, a period
(`.`), and then the `Id` of the source or sink declaration that generated
that metric. For example, assuming there is a sink declaration with an `Id` of
`MyFirehose`:

```

"MetricsFilter": "KinesisFirehoseRecordsFailedNonrecoverable.MyFirehose"

```

You can use special wildcard patterns that are designed to distinguish between single and
multiple instance metrics.

- Asterisk (`*`) matches zero or more characters except period
  (`.`).
- Question mark (`?`) matches one character except period.
- Any other character only matches itself.
- `_Total` is a special token that causes the aggregation of all matching
  multiple instance values across the dimension.

The following example matches all single instance metrics:

```
"MetricsFilter": "*"
```

Because an asterisk does not match the period character, only single instance metrics are
included.

The following example matches all multiple instance metrics:

```
"MetricsFilter": "*.*"
```

The following example matches all metrics (single and multiple):

```
"MetricsFilter": "*;*.*"
```

The following example aggregates all multiple instance metrics across all sources and
sinks:

```
"MetricsFilter": "*._Total"
```

The following example aggregates all Firehose metrics for all Firehose sinks:

```
"MetricsFilter": "*Firehose*._Total"
```

The following example matches all single and multiple instance error metrics:

```
"MetricsFilter": "*Failed*;*Error*.*;*Failed*.*"
```

The following example matches all non-recoverable error metrics aggregated across all
sources and sinks:

```
"MetricsFilter": "*Nonrecoverable*._Total"
```

For information about how to specify a pipe that uses the Kinesis Agent for Windows built-in metric source, see
[Configuring Kinesis Agent for Windows Metric Pipes](pipe-object-declarations.md#kinesis-agent-metric-pipe-configuration "pipe-object-declarations.md#kinesis-agent-metric-pipe-configuration").

## List of Kinesis Agent for Windows Metrics

The following is a list of single instance and multiple instance metrics that are available
for Kinesis Agent for Windows.

### Single Instance Metrics

The following single instance metrics are available:

`KinesisTapBuildNumber`

The version number of Kinesis Agent for Windows.

`PipesConnected`

How many pipes have connected their source to their sink successfully.

`PipesFailedToConnect`

How many pipes have connected their source to their sink unsuccessfully.

`SinkFactoriesFailedToLoad`

How many sink types did not load into Kinesis Agent for Windows successfully.

`SinkFactoriesLoaded`

How many sink types loaded into Kinesis Agent for Windows successfully.

`SinksFailedToStart`

How many sinks did not begin successfully, usually due to incorrect sink
declarations.

`SinksStarted`

How many sinks began successfully.

`SourcesFailedToStart`

How many sources did not begin successfully, usually due to incorrect source
declarations.

`SourcesStarted`

How many sources began successfully.

`SourceFactoriesFailedToLoad`

How many source types did not load into Kinesis Agent for Windows successfully.

`SourceFactoriesLoaded`

How many source types loaded successfully into Kinesis Agent for Windows.

### Multiple Instance Metrics

The following multiple instance metrics are available:

#### DirectorySource Metrics

`DirectorySourceBytesRead`

How many bytes were read during the interval for this
`DirectorySource`.

`DirectorySourceBytesToRead`

How many known numbers of bytes are available to read that have not been read yet by
Kinesis Agent for Windows.

`DirectorySourceFilesToProcess`

How many known files to examine that have not yet been examined yet by Kinesis Agent for Windows.

`DirectorySourceRecordsRead`

How many records have been read during the interval for this
`DirectorySource`.

#### WindowsEventLogSource Metrics

`EventLogSourceEventsError`

How many Windows event log events were not read successfully.

`EventLogSourceEventsRead`

How many Windows event log events were read successfully.

#### KinesisFirehose Sink Metrics

`KinesisFirehoseBytesAccepted`

How many bytes were accepted during the interval.

`KinesisFirehoseClientLatency`

How much time passed between record generation and record streaming to the Firehose
service.

`KinesisFirehoseLatency`

How much time passed between the start and end of record streaming for the Firehose
service.

`KinesisFirehoseNonrecoverableServiceErrors`

How many times records could not be sent without error to the Firehose service despite
retries.

`KinesisFirehoseRecordsAttempted`

How many records tried to be streamed to the Firehose service.

`KinesisFirehoseRecordsFailedNonrecoverable`

How many records were not successfully streamed to the Firehose service despite
retries.

`KinesisFirehoseRecordsFailedRecoverable`

How many records were successfully streamed to the Firehose service, but only with
retries.

`KinesisFirehoseRecordsSuccess`

How many records were successfully streamed to the Firehose service without
retries.

`KinesisFirehoseRecoverableServiceErrors`

How many times records could successfully be sent to the Firehose service, but only with
retries.

#### KinesisStream Metrics

`KinesisStreamBytesAccepted`

How many bytes were accepted during the interval.

`KinesisStreamClientLatency`

How much time passed between record generation and record streaming to the Kinesis Data Streams
service.

`KinesisStreamLatency`

How much time passed between the start and end of record streaming for the Kinesis Data Streams
service.

`KinesisStreamNonrecoverableServiceErrors`

How many times records could not be sent without error to the Kinesis Data Streams service despite
retries.

`KinesisStreamRecordsAttempted`

How many records tried to be streamed to the Kinesis Data Streams service.

`KinesisStreamRecordsFailedNonrecoverable`

How many records were not successfully streamed to the Kinesis Data Streams service despite
retries.

`KinesisStreamRecordsFailedRecoverable`

How many records were successfully streamed to the Kinesis Data Streams service, but only with
retries.

`KinesisStreamRecordsSuccess`

How many records were successfully streamed to the Kinesis Data Streams service without
retries.

`KinesisStreamRecoverableServiceErrors`

How many times records could successfully be sent to the Kinesis Data Streams service, but only with
retries.

#### CloudWatchLog Metrics

`CloudWatchLogBytesAccepted`

How many bytes were accepted during the interval.

`CloudWatchLogClientLatency`

How much time passed between record generation and record streaming to the CloudWatch Logs
service.

`CloudWatchLogLatency`

How much time passed between the start and end of record streaming for the CloudWatch Logs
service.

`CloudWatchLogNonrecoverableServiceErrors`

How many times records could not be sent without error to the CloudWatch Logs service despite
retries.

`CloudWatchLogRecordsAttempted`

How many records tried to be streamed to the CloudWatch Logs service.

`CloudWatchLogRecordsFailedNonrecoverable`

How many records were not successfully streamed to the CloudWatch Logs service despite
retries.

`CloudWatchLogRecordsFailedRecoverable`

How many records were successfully streamed to the CloudWatch Logs service, but only with
retries.

`CloudWatchLogRecordsSuccess`

How many records were successfully streamed to the CloudWatch Logs service without
retries.

`CloudWatchLogRecoverableServiceErrors`

How many times records could successfully be sent to the CloudWatch Logs service, but only with
retries.

#### CloudWatch Metrics

`CloudWatchLatency`

How much time on average passed between the start and end of metric streaming for the
CloudWatch service.

`CloudWatchNonrecoverableServiceErrors`

How many times metrics could not be sent without error to the CloudWatch service despite
retries.

`CloudWatchRecoverableServiceErrors`

How many times metrics were sent without error to the CloudWatch service but only with
retries.

`CloudWatchServiceSuccess`

How many times metrics were sent without error to the CloudWatch service with no retries
needed.

## Bookmark Configuration

By default, Kinesis Agent for Windows sends log records to sinks that are created after the agent starts.
Sometimes it is useful to send earlier log records, for example, log records that are created
during the time period when Kinesis Agent for Windows stops during an automatic update. The bookmark feature tracks
what records have been sent to sinks. When Kinesis Agent for Windows is in bookmark mode and starts up, it sends all
log records that were created after Kinesis Agent for Windows stopped, along with any subsequently created log
records. To control this behavior, file-based source declarations can optionally include the
following key-value pairs:

`InitialPosition`

Specifies the initial situation for the bookmark. Possible values are as follows:

`EOS`

Specifies end of stream (EOS). Only log records created while the agent is
running are sent to sinks.

`0`

All available log records and events are initially sent. Then a bookmark is created to
ensure that every new log record and event created after the bookmark was created are
eventually sent, whether or not Kinesis Agent for Windows is running.

`Bookmark`

The bookmark is initialized to just after the latest log record or event. Then a
bookmark is created to ensure that every new log record and event created after the
bookmark was created are eventually sent, whether or not Kinesis Agent for Windows is running.

Bookmarks are enabled by default. Files are stored in the `%ProgramData%\Amazon\KinesisTap` directory.

`Timestamp`

Log records and events that are created after the
`InitialPositionTimestamp` value (definition follows) are sent. Then a bookmark
is created to ensure that every new log record and event created after the bookmark was
created are eventually sent whether or not Kinesis Agent for Windows is running.

`InitialPositionTimestamp`

Specifies the earliest log record or event timestamp that you want. Specify this
key-value pair only when `InitialPosition` has a value of
`Timestamp`.

`BookmarkOnBufferFlush`

This setting can be added to any bookmarkable source. When set to `true`, ensures that bookmark updates occur only when a sink successfully ships an event to AWS. You can only subscribe a single sink to a source. If you are shipping logs to multiple destinations, duplicate your sources to avoid potential issues with data loss.

When Kinesis Agent for Windows has been stopped for a long time, it might be necessary to delete those bookmarks
because log records and events that are bookmarked might no longer exist. Bookmark files for a
given _source id_ are located in
`%PROGRAMDATA%\Amazon\AWSKinesisTap\*source
 id*.bm`.

Bookmarks do not work on files that are renamed or truncated. Because of the nature of ETW
events and performance counters, they cannot be bookmarked.
