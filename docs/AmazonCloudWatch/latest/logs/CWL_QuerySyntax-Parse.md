

# parse
<a name="CWL_QuerySyntax-Parse"></a>

Use `parse` to extract data from a log field and create extracted fields that you can process in your query. The `parse` command supports four modes: glob expressions, regular expressions, logfmt, and CSV.

If `fieldName` is omitted, `@message` is used by default. You can parse from any named field by specifying the field name as the first argument.

If a log event doesn't match the specified pattern, you still see it in the results, but without the extracted fields.

## Glob mode
<a name="CWL_QuerySyntax-parse-glob"></a>

Use wildcards (`*`) as placeholders for values you want to extract, and assign them to named fields with `as`.

**Syntax**

```
parse {{fieldName}} "{{pattern}}" as {{alias1}}, {{alias2}}
```

The number of `*` wildcards must equal the number of aliases.

**Examples**

```
parse @message "user=*, method:*, latency := *" as @user,
    @method, @latency | stats avg(@latency) by @method, @user
```

```
parse @logStream "*/*/*/*" as env, service, instance, shard
| stats count(*) by env, service
```

**Chained parse**

Extract a field, then parse the extracted field further.

```
parse @message "url=*" as url
| parse url "/api/*/users/*" as apiVersion, userId
| display apiVersion, userId
```

## Regex mode
<a name="CWL_QuerySyntax-parse-regex"></a>

Use a regular expression with named capture groups to extract fields. For information about regular expression syntax, see [Supported regular expressions (regex) syntax](FilterAndPatternSyntax.md#regex-expressions).

**Syntax**

```
parse {{fieldName}} /{{regex}}/
```

Use named capture groups `(?<{{name}}>...)` to define extracted fields.

**Examples**

**Use named capture groups to extract fields**

```
parse @message /user=(?<user2>.*?), method:(?<method2>.*?),
    latency := (?<latency2>.*?)/ | stats avg(latency2) by @method2,
    @user2
```

**Use a named capture group to extract the ENI from a VPC flow log**

```
parse @message /(?<NetworkInterface>eni-.*?) /
| display NetworkInterface, @message
```

**Multi-match mode**

Use multi-match mode to extract all matches of a regular expression from a field, producing multiple rows per log event. Add the keyword `multi` after the regex pattern.

**Syntax**

```
parse {{fieldName}} /{{regex}}/ multi
```

**Examples**

**Extract all IP addresses from a log line (multi-match)**

```
parse @message /(\d+\.\d+\.\d+\.\d+)/ as ip_addr multi
| stats count(*) by ip_addr
```

## Logfmt mode
<a name="CWL_QuerySyntax-parse-logfmt"></a>

Use `parse logfmt` to parse logfmt-formatted log lines into key-value pairs. Logfmt is a structured logging format where each line contains space-separated `key=value` pairs.

**Syntax**

```
parse {{fieldName}} logfmt as {{alias}}
```

The result is a map that you access with dot notation (for example, `lf.level`, `lf.msg`).

**Examples**

```
parse @message logfmt as lf
| filter lf.level = "error"
| display lf.msg, lf.duration
```

```
parse @message logfmt as lf
| stats count(*) by lf.host
```

## CSV mode
<a name="CWL_QuerySyntax-parse-csv"></a>

Use `parse csv` to parse CSV-formatted log lines into structured fields. Each comma-separated value is assigned to the corresponding alias.

**Syntax**

```
parse {{fieldName}} csv as {{alias1}}, {{alias2}}, {{alias3}}
```

**Examples**

```
parse @message csv as timestamp, level, message
| filter level = "ERROR"
| display timestamp, message
```

```
parse @message csv as host, method, path, status, duration
| stats avg(duration) by method
```

## JSON field extraction
<a name="CWL_QuerySyntax-parse-json-field"></a>

Use `json field={{fieldName}}` for explicit chained JSON extraction from a previously parsed object field. This enables you to extract nested keys from a structured field without re-parsing the raw message.

**Syntax**

```
json field={{fieldName}} "{{key.subkey}}" as {{alias}}
```

**Examples**

```
parse @message /(?<payload>\{.*\})/ as payload
| json field=payload "user.name" as username
| display username
```

```
json field=requestContext "identity.sourceIp" as caller_ip
| stats count(*) by caller_ip
```