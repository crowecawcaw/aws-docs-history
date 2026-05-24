# parse

Use `parse` to extract data from a log field and create
extracted fields that you can process in your query. The
`parse` command supports three modes: glob expressions,
regular expressions, and logfmt.

If `fieldName` is omitted, `@message` is
used by default. You can parse from any named field by specifying the
field name as the first argument.

If a log event doesn't match the specified pattern, you still see
it in the results, but without the extracted fields.

## Glob mode

Use wildcards (`*`) as placeholders for values you
want to extract, and assign them to named fields with
`as`.

**Syntax**

```
parse `fieldName` "`pattern`" as `alias1`, `alias2`
```

The number of `*` wildcards must equal the number of
aliases.

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

Use a regular expression with named capture groups to extract
fields. For information about regular expression syntax, see
[Supported regular expressions (regex) syntax](FilterAndPatternSyntax.md#regex-expressions "FilterAndPatternSyntax.md#regex-expressions").

**Syntax**

```
parse `fieldName` /`regex`/
```

Use named capture groups
`(?<`name`>...)` to define
extracted fields.

**Examples**

**Use named capture groups to extract
fields**

```
parse @message /user=(?<user2>.*?), method:(?<method2>.*?),
    latency := (?<latency2>.*?)/ | stats avg(latency2) by @method2,
    @user2
```

**Use a named capture group to extract the
ENI from a VPC flow log**

```
parse @message /(?<NetworkInterface>eni-.*?) /
| display NetworkInterface, @message
```

## Logfmt mode

Use `parse logfmt` to parse logfmt-formatted log lines
into key-value pairs. Logfmt is a structured logging format where
each line contains space-separated `key=value`
pairs.

**Syntax**

```
parse `fieldName` logfmt as `alias`
```

The result is a map that you access with dot notation
(for example, `lf.level`, `lf.msg`).

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
