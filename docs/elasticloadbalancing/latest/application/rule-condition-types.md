# Condition types for listener rules

Conditions define the criteria that incoming requests must meet for a listener rule to
take effect. If a request matches the conditions for a rule, the request is handled as
specified by the rule's actions. Each rule condition has a type and configuration
information. Application Load Balancers support the following condition types for listener rules.

###### Condition types

`host-header`

Route based on the host name of each request. For more information, see
[Host conditions](#host-conditions "#host-conditions").

`http-header`

Route based on the HTTP headers for each request. For more information,
see [HTTP header conditions](#http-header-conditions "#http-header-conditions").

`http-request-method`

Route based on the HTTP request method of each request. For more
information, see [HTTP request method
conditions](#http-request-method-conditions "#http-request-method-conditions").

`path-pattern`

Route based on path patterns in the request URLs. For more information,
see [Path conditions](#path-conditions "#path-conditions").

`query-string`

Route based on key/value pairs or values in the query strings. For more
information, see [Query string conditions](#query-string-conditions "#query-string-conditions").

`source-ip`

Route based on the source IP address of each request. For more
information, see [Source IP address conditions](#source-ip-conditions "#source-ip-conditions").

###### Condition basics

- Each rule can optionally include zero or one of each of the following conditions:
  `host-header`, `http-request-method`,
  `path-pattern`, and `source-ip`. Each rule can also include
  zero or more of each of the following conditions: `http-header` and
  `query-string`.
- With the `host-header`, `http-header`, and
  `path-pattern` conditions, you can use either value matching or
  regular expression (regex) matching.
- You can specify up to three match evaluations per condition. For example, for each
  `http-header` condition, you can specify up to three strings to be
  compared to the value of the HTTP header in the request. The condition is satisfied if
  one of the strings matches the value of the HTTP header. To require that all of the
  strings are a match, create one condition per match evaluation.
- You can specify up to five match evaluations per rule. For example, you can create a
  rule with five conditions where each condition has one match evaluation.
- You can include wildcard characters in the match evaluations for the
  `http-header`, `host-header`, `path-pattern`, and
  `query-string` conditions. There is a limit of five wildcard characters
  per rule.
- Rules are applied only to visible ASCII characters; control characters (0x00 to 0x1f
  and 0x7f) are excluded.

###### Demos

For demos, see [Advanced request routing](https://exampleloadbalancer.com/advanced_request_routing_demo.html "https://exampleloadbalancer.com/advanced_request_routing_demo.html").

## Host conditions

You can use host conditions to define rules that route requests based on the host
name in the host header (also known as _host-based routing_).
This enables you to support multiple subdomains and different top-level domains
using a single load balancer.

A hostname is not case-sensitive, can be up to 128 characters in length, and can
contain any of the following characters:

- A–Z, a–z, 0–9
- - .
- \* (matches 0 or more characters)
- ? (matches exactly 1 character)

You must include at least one "." character. You can include only alphabetical
characters after the final "." character.

###### Example hostnames

- example.com
- test.example.com
- \*.example.com

The rule \*.example.com matches test.example.com but
doesn't match example.com.

###### Example host header condition

You can specify conditions when you create or modify a rule. For more
information, see the [create-rule](../../../cli/latest/reference/elbv2/create-rule.md "../../../cli/latest/reference/elbv2/create-rule.md") and [modify-rule](../../../cli/latest/reference/elbv2/modify-rule.md "../../../cli/latest/reference/elbv2/modify-rule.md") commands.

Value matching

```
[
  {
      "Field": "host-header",
      "HostHeaderConfig": {
          "Values": ["*.example.com"]
      }
  }
]
```

Regex matching

```
[
  {
      "Field": "host-header",
      "HostHeaderConfig": {
          "RegexValues": ["^(.*)\\.example\\.com$"]
      }
  }
]
```

## HTTP header conditions

You can use HTTP header conditions to configure rules that route requests based on
the HTTP headers for the request. You can specify the names of standard or custom
HTTP header fields. The header name and the match evaluation are not case-sensitive.
The following wildcard characters are supported in the comparison strings: \*
(matches 0 or more characters) and ? (matches exactly 1 character). Wildcard
characters are not supported in the header name.

When the Application Load Balancer attribute `routing.http.drop_invalid_header_fields` is
enabled, it will drop header names that don't conform to the regular expressions
(`A-Z,a-z,0-9`). Header names that don't conform to the regular
expressions can also be added.

###### Example HTTP header condition

You can specify conditions when you create or modify a rule. For more
information, see the [create-rule](../../../cli/latest/reference/elbv2/create-rule.md "../../../cli/latest/reference/elbv2/create-rule.md") and [modify-rule](../../../cli/latest/reference/elbv2/modify-rule.md "../../../cli/latest/reference/elbv2/modify-rule.md") commands. The following condition is satisfied by
requests with a User-Agent header that matches one of the specified
strings.

Value matching

```
[
  {
      "Field": "http-header",
      "HttpHeaderConfig": {
          "HttpHeaderName": "User-Agent",
          "Values": ["*Chrome*", "*Safari*"]
      }
  }
]
```

Regex matching

```
[
  {
      "Field": "http-header",
      "HttpHeaderConfig": {
          "HttpHeaderName": "User-Agent",
          "RegexValues": [".+"]
      }
  }
]
```

## HTTP request method

conditions

You can use HTTP request method conditions to configure rules that route requests
based on the HTTP request method of the request. You can specify standard or custom
HTTP methods. The match evaluation is case-sensitive. Wildcard characters are not
supported; therefore, the method name must be an exact match.

We recommend that you route GET and HEAD requests in the same way, because the
response to a HEAD request may be cached.

###### Example HTTP method condition

You can specify conditions when you create or modify a rule. For more
information, see the [create-rule](../../../cli/latest/reference/elbv2/create-rule.md "../../../cli/latest/reference/elbv2/create-rule.md") and [modify-rule](../../../cli/latest/reference/elbv2/modify-rule.md "../../../cli/latest/reference/elbv2/modify-rule.md") commands. The following condition is satisfied by
requests that use the specified method.

```
[
  {
      "Field": "http-request-method",
      "HttpRequestMethodConfig": {
          "Values": ["CUSTOM-METHOD"]
      }
  }
]
```

## Path conditions

You can use path conditions to define rules that route requests based on the URL
in the request (also known as _path-based routing_).

The path pattern is applied only to the path of the URL, not to its query
parameters. It is applied only to visible ASCII characters; control characters (0x00
to 0x1f and 0x7f) are excluded.

The rule evaluation is performed only after URI normalization occurs.

A path pattern is case-sensitive, can be up to 128 characters in length, and can
contain any of the following characters.

- A–Z, a–z, 0–9
- \_ - . $ / ~ " ' @ : +
- & (using &amp;)
- \* (matches 0 or more characters)
- ? (matches exactly 1 character)

If the protocol version is gRPC, conditions can be specific to a package, service,
or method.

###### Example HTTP path patterns

- `/img/*`
- `/img/*/pics`

###### Example gRPC path patterns

- /package
- /package.service
- /package.service/method

The path pattern is used to route requests but does not alter them. For example,
if a rule has a path pattern of `/img/*`, the rule forwards a
request for `/img/picture.jpg` to the specified target group as a
request for `/img/picture.jpg`.

###### Example path pattern condition

You can specify conditions when you create or modify a rule. For more
information, see the [create-rule](../../../cli/latest/reference/elbv2/create-rule.md "../../../cli/latest/reference/elbv2/create-rule.md") and [modify-rule](../../../cli/latest/reference/elbv2/modify-rule.md "../../../cli/latest/reference/elbv2/modify-rule.md") commands. The following condition is satisfied by
requests with a URL that contains the specified string.

Value matching

```
[
  {
      "Field": "path-pattern",
      "PathPatternConfig": {
          "Values": ["/img/*"]
      }
  }
]
```

Regex matching

```
[
  {
      "Field": "path-pattern",
      "PathPatternConfig": {
          "RegexValues": ["^\\/api\\/(.*)$"]
      }
  }
]
```

## Query string conditions

You can use query string conditions to configure rules that route requests based
on key/value pairs or values in the query string. The match evaluation is not
case-sensitive. The following wildcard characters are supported: \* (matches 0 or
more characters) and ? (matches exactly 1 character).

###### Example query string condition

You can specify conditions when you create or modify a rule. For more
information, see the [create-rule](../../../cli/latest/reference/elbv2/create-rule.md "../../../cli/latest/reference/elbv2/create-rule.md") and [modify-rule](../../../cli/latest/reference/elbv2/modify-rule.md "../../../cli/latest/reference/elbv2/modify-rule.md") commands. The following condition is satisfied by
requests with a query string that includes either a key/value pair of
"version=v1" or any key set to "example".

```
[
  {
      "Field": "query-string",
      "QueryStringConfig": {
          "Values": [
            {
                "Key": "version",
                "Value": "v1"
            },
            {
                "Value": "*example*"
            }
          ]
      }
  }
]
```

## Source IP address conditions

You can use source IP address conditions to configure rules that route requests
based on the source IP address of the request. The IP address must be specified in
CIDR format. You can use both IPv4 and IPv6 addresses. Wildcard characters are not
supported. You cannot specify the `255.255.255.255/32` CIDR for the
source IP rule condition.

If a client is behind a proxy, this is the IP address of the proxy, not the IP
address of the client.

This condition is not satisfied by the addresses in the X-Forwarded-For header. To
search for addresses in the X-Forwarded-For header, use an `http-header`
condition.

###### Example source IP condition

You can specify conditions when you create or modify a rule. For more
information, see the [create-rule](../../../cli/latest/reference/elbv2/create-rule.md "../../../cli/latest/reference/elbv2/create-rule.md") and [modify-rule](../../../cli/latest/reference/elbv2/modify-rule.md "../../../cli/latest/reference/elbv2/modify-rule.md") commands. The following condition is satisfied by
requests with a source IP address in one of the specified CIDR blocks.

```
[
  {
      "Field": "source-ip",
      "SourceIpConfig": {
          "Values": ["192.0.2.0/24", "198.51.100.10/32"]
      }
  }
]
```
