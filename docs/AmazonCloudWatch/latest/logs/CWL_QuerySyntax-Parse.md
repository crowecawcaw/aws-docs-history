# parse

Use `parse` to extract data from a log field and create an
extracted field that you can process in your query. If a log event doesn't
match the specified pattern, you still see it in the results, but without
the extracted fields.
**`parse`** supports both glob mode
using wildcards, and regular expressions. For information about regular
expression syntax, see [Supported regular expressions (regex) syntax](FilterAndPatternSyntax.md#regex-expressions "FilterAndPatternSyntax.md#regex-expressions").

You can parse nested JSON fields with a regular expression.

**Example: Parsing a nested JSON
field**

The code snippet shows how to parse a JSON log event that's been
flattened during ingestion.

```
{'fieldsA': 'logs', 'fieldsB': [{'fA': 'a1'}, {'fA': 'a2'}]}
```

The code snippet shows a query with a regular expression that extracts
the values for `fieldsA` and `fieldsB` to create the
extracted fields `fld` and `array`.

```
parse @message "'fieldsA': '*', 'fieldsB': ['*']" as fld, array
```

**Named capturing groups**

When you use **`parse`** with a regular
expression, you can use named capturing groups to capture a pattern into a
field. The syntax is `parse @message
 (?<*Name*>*pattern*)`

The following example uses a capturing group on a VPC flow log to extract
the ENI into a field named `NetworkInterface`.

```
parse @message /(?<NetworkInterface>eni-.*?) / | display NetworkInterface, @message
```

###### Note

JSON log events are flattened during ingestion. Currently, parsing
nested JSON fields with a glob expression isn't supported. You can only
parse JSON log events that include no more than 200 log event fields.
When you parse nested JSON fields, you must format the regular
expression in your query to match the format of your JSON log event.

## Examples of the parse command

**Use a glob expression to extract the fields
`@user`, `@method`, and
`@latency` from the log field `@message`
and return the average latency for each unique combination of
`@method` and `@user`.**

```
parse @message "user=*, method:*, latency := *" as @user,
    @method, @latency | stats avg(@latency) by @method,
    @user
```

**Use a regular expression to extract the fields
`@user2`, `@method2`, and
`@latency2` from the log field `@message`
and return the average latency for each unique combination of
`@method2` and `@user2`.**

```
parse @message /user=(?<user2>.*?), method:(?<method2>.*?),
    latency := (?<latency2>.*?)/ | stats avg(latency2) by @method2,
    @user2
```

**Extracts the fields `loggingTime`,
`loggingType` and `loggingMessage`,
filters down to log events that contain `ERROR` or
`INFO` strings, and then displays only the
`loggingMessage` and `loggingType` fields
for events that contain an `ERROR`
string.**

```
FIELDS @message
    | PARSE @message "* [*] *" as loggingTime, loggingType, loggingMessage
    | FILTER loggingType IN ["ERROR", "INFO"]
    | DISPLAY loggingMessage, loggingType = "ERROR" as isError
```

## Parsing from specific fields

By default, the `parse` command operates on
`@message`. However, you can parse from any named field
by specifying the field name as the first argument. This includes
discovered fields, fields extracted by a previous `parse`
command, and fields present in structured (JSON) log events.

**Syntax**

Glob mode:

```
parse `fieldName` "`pattern`" as `alias1`, `alias2`
```

Regex mode:

```
parse `fieldName` /`regex`/
```

**Supported fields**

You can use the following types of fields as the source for
`parse`:

- Discovered fields such as `@message`,
  `@logStream`, `@logGroup`, and
  `@timestamp`
- User-extracted fields from a previous `parse` or
  `fields` command
- Any field present in structured (JSON) log events that has
  been flattened during ingestion

**Behavior**

- If the target field is null or missing for a log event, the
  extracted fields are null and the row passes through
  unmodified.
- If the target field doesn't match the pattern, the extracted
  fields are null and the row passes through unmodified.
- In glob mode, the number of `*` wildcards must
  equal the number of aliases.
- In regex mode, use named capture groups
  `(?<`name`>...)`
  to define extracted fields.

**Examples**

**Parse from
`@logStream`**

Extract environment and service information from the log stream
name.

```
fields @timestamp, @logStream
| parse @logStream "*/*/*/*" as env, service, instance, shard
| stats count(*) by env, service
```

**Parse from a previously extracted
field (chained parse)**

Extract a field from `@message`, then parse that
extracted field further.

```
fields @message
| parse @message "url=*" as url
| parse url "/api/*/users/*" as apiVersion, userId
| display apiVersion, userId
```

**Parse from a structured (JSON) log
field**

Parse a field that was automatically extracted from a JSON log
event during ingestion.

```
fields @timestamp, userAgent
| parse userAgent "Mozilla/* (*) */*" as version, os, engine, engineVersion
| stats count(*) by os
```

**Regex mode with field
targeting**

Use a regular expression with named capture groups to parse a
specific field.

```
fields @timestamp, requestUri
| parse requestUri /\/api\/(?<version>v\d+)\/(?<resource>[^\/]+)/
| stats count(*) by version, resource
```
