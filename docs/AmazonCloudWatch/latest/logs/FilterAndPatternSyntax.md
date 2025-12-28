# Filter pattern syntax for metric filters, subscription filters, filter log events, and Live Tail

###### Note

For information about how to query your log groups with the Amazon CloudWatch Logs Insights
query language, see
[CloudWatch Logs Insights language query syntax](CWL_QuerySyntax.md "CWL_QuerySyntax.md").

With CloudWatch Logs, you can use [metric filters](MonitoringLogData.md "MonitoringLogData.md") to transform log data into actionable metrics,
[subscription filters](SubscriptionFilters.md "SubscriptionFilters.md") to route log events to other AWS services,
[filter log events](SearchDataFilterPattern.md "SearchDataFilterPattern.md") to search for log events,
and [Live Tail](CloudWatchLogs_LiveTail.md "CloudWatchLogs_LiveTail.md") to interactively view your logs in real-time as they are ingested.

Filter patterns make up the syntax
that metric filters, subscription filters, log events, and Live Tail use
to match terms
in log events.
Terms can be words, exact phrases, or numeric values.
Regular expressions (regex) can be used to create standalone filter patterns, or can be incorporated with JSON and space-delimited filter patterns.

Create filter patterns
with the terms
that you want
to match.
Filter patterns only return the log events
that contain the terms you define.
You can test filter patterns
in the CloudWatch console.

###### Topics

- [Supported regular expressions (regex) syntax](#regex-expressions "#regex-expressions")
- [Using filter patterns to match terms with a regular expression (regex)](#matching-terms-regex "#matching-terms-regex")
- [Using filter patterns to match terms in unstructured log events](#matching-terms-unstructured-log-events "#matching-terms-unstructured-log-events")
- [Using filter patterns to match terms in JSON log events](#matching-terms-json-log-events "#matching-terms-json-log-events")
- [Using filter patterns to match terms in space-delimited log events](#matching-term-space-delimited-log-events "#matching-term-space-delimited-log-events")

## Supported regular expressions (regex) syntax

When using regex to search and filter log data, you must surround your expressions with `%`.

Filter patterns with regex can only include the following:

- Alphanumeric characters – An alphanumeric character is a character that is either a letter (from A to Z or a to z) or a digit (from 0 to 9).
- Supported symbol characters –
  These include:
  '`:`', '`_`', '`#`', '`=`', '`@`','`/`', '`;`', '`,`', and '`-`'.
  For example, `%something!%` would be rejected since '`!`' is not supported.
- Supported operators –
  These include: '`^`', '`$`', '`?`', '`[`', '`]`', '`{`', '`}`', '`|`', '`\`', '`*`', '`+`', and '`.`'.
  The `(` and `)` operators are not supported. You cannot use parentheses to define a subpattern.

Multi-byte characters are not supported.

###### Note

**Quotas**

There is a maximum of 5 filter patterns containing regex for each log group when creating metric filters or subscription filters.

There is a limit of 2 regex for each filter pattern when creating a delimited or JSON filter pattern for
metric filters and subscription filters or when filtering log events or Live Tail.

**Usage of supported operators**

- `^`: Anchors the match to the beginning of a string. For example, `%^[hc]at%` matches "hat" and "cat", but only at the beginning of a string.
- `$`: Anchors the match to the end of a string. For example, `%[hc]at$%` matches "hat" and "cat", but only at the end of a string.
- `?`: Matches zero or one occurrence of the preceding term. For example,
  `%colou?r%` can match both "color" and "colour".
- `[]`: Defines a character class. Matches the character list or character range contained within the brackets.
  For example, `%[abc]%` matches "a", "b", or "c"; `%[a-z]%` matches any lowercase letter from "a" to "z"; and `%[abcx-z]%`matches "a", "b", "c", "x", "y", or "z".
- `{m, n}`: Matches the preceding term at least _m_ and not more than _n_ times. For example, `%a{3,5}%` matches only "aaa", "aaaa", and "aaaaa".

###### Note

Either _m_ or _n_ can be omitted if you chose not to define a minimum or maximum.

- `|`: Boolean "Or", which matches the term on either side of the vertical bar. For example:
  - `%gra|ey%` can match "gray" or "grey"
  - `%^starting|^initializing|^shutting down%` can match match "starting ...", or "initializing ...", or "shutting down", but won't match "skipping initializing ..."
  - `%abcc|ab[^c]$` can match match "abcc ..." and "aba ..." but won't match "aac ..."

- `\`: Escape character, which allows you to use the literal meaning of an operator instead of its special meaning.
  For example, `%\[.\]%` matches any single character surrounded by "[" and "]" since the brackets are escaped, such as "[a]", "[b]", "[7]", "[@]", "[]]", and "[ ]".

###### Note

`%10\.10\.0\.1%` is the correct way to create a regex to match the IP address 10.10.0.1.

- `*`: Matches zero or more instances of the preceding term. For example, `%ab*c%` can match "ac", "abc", and "abbbc";
  `%ab[0-9]*%` can match "ab", "ab0", and "ab129".
- `+`: Matches one or more instances of the preceding term. For example, `%ab+c%` can match "abc", "abbc", and "abbbc", but not "ac".
- `.`: Matches any single character.
  For example, `%.at%` matches any three character string ending with "at", including "hat", "cat", "bat", "4at", "#at" and " at" (starting with a space).

###### Note

When creating a regex to match IP addresses, it is important to escape the `.` operator. For example, `%10.10.0.1%` can match "10010,051" which might not be the actual intended purpose of the expression.

- `\d`, `\D`: Matches a digit/non-digit character.
  For example, `%\d%` is equivalent to `%[0-9]%` and `%\D%` is equivalent to `%[^0-9]%`.

###### Note

The uppercase operator denotes the inverse of its lowercase counterpart.

- `\s`, `\S`: Matches a whitespace character/non-whitespace character.

###### Note

The uppercase operator denotes the inverse of its lowercase counterpart.
Whitespace characters include the tab (`\t`), space(), and newline (`\n`) characters.

- `\w`, `\W`: Matches an alphanumeric character/non-alphanumeric character.
  For example, `%\w%` is equivalent to `%[a-zA-Z_0-9]%` and `%\W%` is equivalent to `%[^a-zA-Z_0-9]%`.

###### Note

The uppercase operator denotes the inverse of its lowercase counterpart.

- `\xhh`: Matches the ASCII mapping for a two-digit hexadecimal character.
  `\x` is the escape sequence which indicates that the following characters represent the hexadecimal value for ASCII.
  `hh` specifies the two hexadecimal digits (0-9 and A-F) which point to a character in the ASCII table.

###### Note

You can use `\xhh` to match symbol characters that are not supported by the filter pattern.
For example, `%\x3A%` matches `:`; and `%\x28%` matches `(`.

## Using filter patterns to match terms with a regular expression (regex)

You can match terms in your log events using a regex pattern surrounded with `%` (percentage signs before and after the regex pattern).
The following code snippet shows an example of a filter pattern that returns all log events consisting of the **AUTHORIZED** keyword.

For a list of supported regular expressions, see [Supported regular expressions](FilterAndPatternSyntax.md#regex-expressions "FilterAndPatternSyntax.md#regex-expressions").

```

  %AUTHORIZED%

```

This filter pattern returns log event messages, such as the following:

- `[ERROR 401] UNAUTHORIZED REQUEST`
- `[SUCCESS 200] AUTHORIZED REQUEST`

## Using filter patterns to match terms in unstructured log events

The following examples contain code snippets
that show
how you can use filter patterns
to match terms
in unstructured log events.

###### Note

Filter patterns are case sensitive.
Enclose exact phrases and terms
that include non-alphanumeric characters
in double quotation marks (**""**).

Example: Match a single term
The following code snippet shows an example
of a single-term filter pattern
that returns all log events
where messages contain the word **_ERROR_**.

```

ERROR

```

This filter pattern matches log event messages,
such as the following:

- `[ERROR 400] BAD REQUEST`
- `[ERROR 401] UNAUTHORIZED REQUEST`
- `[ERROR 419] MISSING ARGUMENTS`
- `[ERROR 420] INVALID ARGUMENTS`

Example: Match multiple terms
The following code snippet shows an example
of a multiple-term filter pattern
that returns all log events
where messages contain the words **_ERROR_** and **_ARGUMENTS_**.

```

ERROR ARGUMENTS

```

The filter returns log event messages,
such as the following:

- `[ERROR 419] MISSING ARGUMENTS`
- `[ERROR 420] INVALID ARGUMENTS`

This filter pattern doesn't return the following log event messages
because they don't contain both
of the terms
specified
in the filter pattern.

- `[ERROR 400] BAD REQUEST`
- `[ERROR 401] UNAUTHORIZED REQUEST`

Example: Match optional terms
You can use pattern matching
to create filter patterns
that return log events
containing optional terms.
Place a question mark ("?") before the terms
that you want to match.
The following code snippet shows an example
of a filter pattern
that returns all log events
where messages
contain the word **_ERROR_** or the word
**_ARGUMENTS_**.

```

?ERROR ?ARGUMENTS

```

This filter pattern matches log event messages, such as the following:

- `[ERROR 400] BAD REQUEST`
- `[ERROR 401] UNAUTHORIZED REQUEST`
- `[ERROR 419] MISSING ARGUMENTS`
- `[ERROR 420] INVALID ARGUMENTS`

###### Note

You cant' combine the question mark ("?") with other filter patterns, such as include and
exclude terms. If you combine "?" with other filter patterns, all question mark
terms will be ignored.

For example, the following filter pattern matches all events containing the word `REQUEST`, but the question mark ("?") filter terms are ignored and have no effect.

```

?ERROR ?ARGUMENTS REQUEST

```

Log event matches

- `[INFO] REQUEST FAILED`
- `[WARN] UNAUTHORIZED REQUEST`
- `[ERROR] 400 BAD REQUEST`

Example: Match exact phrases
The following code snippet shows an example
of a filter pattern
that returns log events
where messages contain the exact phrase
**_INTERNAL SERVER ERROR_**.

```

"INTERNAL SERVER ERROR"

```

This filter pattern returns the following log event message:

- `[ERROR 500] INTERNAL SERVER ERROR`

Example: Include and exclude terms
You can create filter patterns
that return log events
where messages
include some terms
and exclude other terms.
Place a minus symbol (**"-"**)
before the terms
that you want to exclude.
The following code snippet shows an example
of a filter pattern
that returns log events
where messages
include the term **_ERROR_**
and exclude the term **_ARGUMENTS_**.

```

ERROR -ARGUMENTS

```

This filter pattern returns log event messages,
such as the following:

- `[ERROR 400] BAD REQUEST`
- `[ERROR 401] UNAUTHORIZED REQUEST`

This filter pattern doesn't return the following log event messages
because they contain the word **_ARGUMENTS_**.

- `[ERROR 419] MISSING ARGUMENTS`
- `[ERROR 420] INVALID ARGUMENTS`

Example: Match everything
You can match everything
in your log events
with double quotation marks.
The following code snippet shows an example
of a filter pattern
that returns all log events.

```

" "

```

## Using filter patterns to match terms in JSON log events

The following describes how to write
the syntax
for filter patterns
that match JSON terms
containing strings and numeric values.

Writing filter patterns that match strings
You can create filter patterns
to match strings
in JSON log events.
The following code snippet
shows an example
of the syntax
for string-based filter pattern.

```

{ `PropertySelector` `EqualityOperator` `String` }

```

Enclose filter patterns
in curly braces ("{}").
String-based filter patterns
must contain the following parts:

- **Property selector**

Set off property selectors
with a dollar sign
followed by a period ("$.").
Property selectors are alphanumeric strings
that support hyphen ("-") and underscore ("\_") characters.
Strings don't support scientific notation.
Property selectors point
to value nodes
in JSON log events.
Value nodes can be strings or numbers.
Place arrays
after property selectors.
The elements in arrays follow a zero-based numbering system, meaning that the first element
in the array is element 0, the second element is element 1, and so on.
Enclose elements
in brackets ("[]").
If a property selector points
to an array or object,
the filter pattern won't match the log format. If the JSON property contains a period (`"."`), then
the bracket notation may be used to select that property.

###### Note

**Wildcard selector**

You can use the JSON wildcard to select any array element or any JSON object field.

**Quotas**

You can only use up to one wildcard selector in a property selector.

- **Equality operator**

Set off equality operators
with one
of the following symbols: equal ("=")
or not equal ("!=").
Equality operators return a Boolean value (true or false).

- **String**

You can enclose strings
in double quotation marks ("").
Strings
that contain types
other than alphanumeric characters and the underscore symbol
must be placed
in double quotation marks.
Use the asterisk ("\*")
as a wild card
to match text.

###### Note

You can use any conditional regular expression when creating filter patterns to match terms in JSON log events. For a list of supported regular expressions, see [Supported regular expressions](FilterAndPatternSyntax.md#regex-expressions "FilterAndPatternSyntax.md#regex-expressions").

The following code snippet contains an example
of a filter pattern
showing
how you can format a filter pattern to
match a JSON term
with a string.

```

{ $.eventType = "UpdateTrail" }

```

Writing filter patterns that match numeric values
You can create filter patterns
to match numeric values
in JSON log events.
The following code snippet shows an example
of the syntax
for filter patterns
that match numeric values.

```

{ `PropertySelector` `NumericOperator` `Number` }

```

Enclose filter patterns
in curly braces ("{}").
Filter patterns
that match numeric values
must have the following parts:

- **Property selector**

Set off property selectors
with a dollar sign
followed by a period ("$.").
Property selectors are alphanumeric strings
that support hyphen ("-") and underscore ("\_") characters.
Strings don't support scientific notation.
Property selectors point
to value nodes
in JSON log events.
Value nodes can be strings or numbers.
Place arrays
after property selectors.
The elements in arrays follow a zero-based numbering system, meaning that the first
element in the array is element 0, the second element is element 1, and so on.
Enclose elements
in brackets ("[]").
If a property selector points
to an array or object,
the filter pattern won't match the log format. If the JSON property
contains a period (`"."`), then the bracket notation may be used to select that property.

###### Note

**Wildcard selector**

You can use the JSON wildcard to select any array element or any JSON object field.

**Quotas**

You can only use up to one wildcard selector in a property selector.

- **Numeric operator**

Set off numeric operators
with one of the following symbols:
greater than (">"),
less than ("<"),
equal ("="),
not equal ("!="),
greater than or equal to (">="), or less than or equal to ("<=").

- **Number**

You can use integers
that contain plus ("+") or minus ("-") symbols
and follow scientific notation.
Use the asterisk ("\*")
as a wild card
to match numbers.

The following code snippet
contains examples
showing
how you can format filter patterns
to match JSON terms with numeric values.

```
// Filter pattern with greater than symbol
{ $.bandwidth > 75 }
// Filter pattern with less than symbol
{ $.latency < 50 }
// Filter pattern with greater than or equal to symbol
{ $.refreshRate >= 60 }
// Filter pattern with less than or equal to symbol
{ $.responseTime <= 5 }
// Filter pattern with equal sign
{ $.errorCode = 400}
// Filter pattern with not equal sign
{ $.errorCode != 500 }
// Filter pattern with scientific notation and plus symbol
{ $.number[0] = 1e+3 }
// Filter pattern with scientific notation and minus symbol
{ $.number[0] != 1e-3 }

```

The following examples contain code snippets
that show
how filter patterns can match terms
in a JSON log event.

###### Note

If you test an example filter pattern
with the example JSON log event,
you must enter the example JSON log
on a single line.

**JSON log event**

```
{
      "eventType": "UpdateTrail",
      "sourceIPAddress": "111.111.111.111",
      "arrayKey": [
            "value",
            "another value"
      ],
      "objectList": [
           {
             "name": "a",
             "id": 1
           },
           {
             "name": "b",
             "id": 2
           }
      ],
      "SomeObject": null,
      "cluster.name": "c"
}
```

Example: Filter pattern that matches string values
This filter pattern matches the string `"UpdateTrail"` in the property `"eventType"`.

```

{ $.eventType = "UpdateTrail" }

```

Example: Filter pattern that matches string values (IP address)
This filter pattern contains a wild card and matches the property `"sourceIPAddress"`
because it doesn't contain a number
with the prefix `"123.123."`.

```

{ $.sourceIPAddress != 123.123.* }

```

Example: Filter pattern that matches a specific array element with a string value
This filter pattern matches the element `"value"`
in the array `"arrayKey"`.

```

{ $.arrayKey[0] = "value" }

```

Example: Filter pattern that matches a string using regex
This filter pattern matches the string `"Trail"` in the property `"eventType"`.

```

{ $.eventType = %Trail% }

```

Example: Filter pattern that uses a wildcard to match values of any element in the array using regex
The filter pattern contain regex which matches the element `"value"` in the array `"arrayKey"`.

```

{ $.arrayKey[*] = %val.{2}% }

```

Example: Filter pattern that uses a wildcard to match values of any element with a specific prefix and subnet using regex (IP address)
This filter pattern contains regex which matches the element `"111.111.111.111"` in the property `"sourceIPAddress"`.

```

{ $.* = %111\.111\.111\.1[0-9]{1,2}% }

```

###### Note

**Quotas**

You can only use up to one wildcard selector in a property selector.

Example: Filter pattern that matches a JSON property with a period (.) in the key

```

{ $.['cluster.name'] = "c" }

```

Example: Filter pattern that matches JSON logs using IS
You can create filter patterns
that match fields
in JSON logs
with the `IS` variable.
The `IS` variable can match fields
that contain the values `NULL`, `TRUE`, or `FALSE`.
The following filter pattern returns JSON logs
where the value
of `SomeObject` is `NULL`.

```

{ $.SomeObject IS NULL }

```

Example: Filter pattern that matches JSON logs using NOT EXISTS
You can create filter patterns
with the `NOT EXISTS` variable
to return JSON logs
that don't contain specific fields
in the log data.
The following filter pattern uses `NOT EXISTS`
to return JSON logs
that don't contain the field `SomeOtherObject`.

```

{ $.SomeOtherObject NOT EXISTS }

```

###### Note

The variables `IS NOT` and `EXISTS` currently aren't supported.

You can use the logical operators
AND ("&&") and OR ("||")
in filter patterns
to create compound expressions
that match log events
where two or more conditions are true.
Compound expressions support the use
of parentheses ("()")
and the following standard order
of operations: () > && > ||.
The following examples contain
code snippets
that show
how you can use filter patterns
with compound expressions
to match terms
in a JSON object.

**JSON object**

```
{
    "user": {
        "id": 1,
        "email": "John.Stiles@example.com"
    },
    "users": [
        {
         "id": 2,
         "email": "John.Doe@example.com"
        },
        {
         "id": 3,
         "email": "Jane.Doe@example.com"
        }
    ],
    "actions": [
        "GET",
        "PUT",
        "DELETE"
    ],
    "coordinates": [
        [0, 1, 2],
        [4, 5, 6],
        [7, 8, 9]
    ]
}
```

Example: Expression that matches using AND (&&)
This filter pattern
contains a compound expression
that matches `"id"`
in `"user"`
with a numeric value
of `1`
and `"email"` in the first element of the `"users"` array
with the string `"John.Doe@example.com"`.

```


{ ($.user.id = 1) && ($.users[0].email = "John.Doe@example.com") }


```

Example: Expression that matches using OR (||)
This filter pattern
contains a compound expression
that matches `"email"`
in `"user"`
with the string `"John.Stiles@example.com"`.

```


{ $.user.email = "John.Stiles@example.com" || $.coordinates[0][1] = "nonmatch" && $.actions[2] = "nonmatch" }


```

Example: Expression that doesn't match using AND (&&)
This filter pattern contains a compound expression
that doesn't find a match
because the expression doesn't match the third action
in `"actions"`.

```


{ ($.user.email = "John.Stiles@example.com" || $.coordinates[0][1] = "nonmatch") && $.actions[2] = "nonmatch" }


```

###### Note

**Quotas**

You can only use up to one wildcard selector in a property selector, and up to three wildcard selectors in a filter pattern with compound expressions.

Example: Expression that doesn't match using OR (||)
This filter pattern
contains a compound expression that doesn't find a match
because the expression doesn't match the first property
in `"users"` or the third action
in `"actions"`.

```

{ ($.user.id = 2 && $.users[0].email = "nonmatch") || $.actions[2] = "GET" }

```

## Using filter patterns to match terms in space-delimited log events

You can create filter patterns to match terms in space-delimited log events.
The following provides an example space-delimited log event and describes how to write the syntax for filter patterns that match terms in the space-delimited log event.

###### Note

You can use any conditional regular expression when creating filter patterns to match terms in space-delimited log events. For a list of supported regular expressions, see [Supported regular expressions](FilterAndPatternSyntax.md#regex-expressions "FilterAndPatternSyntax.md#regex-expressions").

Example: Space-delimited log event
The following code snippet shows a space-delimited log event
that contains seven fields:
`ip`, `user`, `username`, `timestamp`, `request`, `status_code`, and `bytes`.

```


127.0.0.1 Prod frank [10/Oct/2000:13:25:15 -0700] "GET /index.html HTTP/1.0" 404 1534


```

###### Note

Characters
between brackets ("[]")
and double quotation marks ("")
are considered single fields.

Writing filter patterns that match terms in a space-delimited log event
To create a filter pattern that matches terms in a space-delimited log event,
enclose the filter pattern in brackets ("[]"),
and specify fields with names
that are separated
by commas (",").
The following filter pattern parses seven fields.

```


[ip=%127\.0\.0\.[1-9]%, user, username, timestamp, request =*.html*, status_code = 4*, bytes]


```

You can use numeric operators ( >, <, =, !=, >=, or <=)
and the asterisk (\*)
as a wild card or regex
to give your filter pattern conditions.
In the example filter pattern, `ip` uses regex
that matches IP address range 127.0.0.1 - 127.0.0.9,
`request` contains a wildcard that states it must extract a value with `.html`,
and `status_code` contains a wildcard that states it must extract a value beginning with `4`.

If you don't know the number
of fields
that you're parsing
in a space-delimited log event,
you can use ellipsis (...)
to reference any unnamed field.
Elipsis can reference
as many fields
as needed.
The following example shows a filter pattern with ellipsis
that represent the first four unnamed fields
shown
in the previous example filter pattern.

```

[..., request =*.html*, status_code = 4*, bytes]

```

You also can use the logical operators AND (&&)
and OR (||)
to create compound expressions.
The following filter pattern contains a compound expression
that states the value
of `status_code`
must be `404` or `410`.

```

[ip, user, username, timestamp, request =*.html*, status_code = 404 || status_code = 410, bytes]

```

You can use pattern matching
to create space-delimited filter patterns
that match terms
in a specific order.
Specify the order
of your terms
with indicators.
Use **w1**
to represent your first term
and **w2** and so on
to represent the order
of your subsequent terms.
Place commas (",")
between your terms.
The following examples contain code snippets
that show how you can use pattern matching
with space-delimited filter patterns.

###### Note

You can use any conditional regular expression when creating filter patterns to match terms in space-delimited log events. For a list of supported regular expressions, see [Supported regular expressions](FilterAndPatternSyntax.md#regex-expressions "FilterAndPatternSyntax.md#regex-expressions").

**Space-delimited log event**

```
INFO 09/25/2014 12:00:00 GET /service/resource/67 1200
INFO 09/25/2014 12:00:01 POST /service/resource/67/part/111 1310
WARNING 09/25/2014 12:00:02 Invalid user request
ERROR 09/25/2014 12:00:02 Failed to process request
```

Example: Match terms in order
The following space-delimited filter pattern returns log events
where the first word
in the log events is **_ERROR_**.

```

[w1=ERROR, w2]

```

###### Note

When you create space-delimited filter patterns
that use pattern matching,
you must include a blank indicator
after you specify the order
of your terms.
For example,
if you create a filter pattern
that returns log events
where the first word is **_ERROR_**,
include a blank **w2** indicator
after the **w1** term.

Example: Match terms with AND (&&) and OR (||)
You can use the logical operators
AND ("&&") and OR ("||")
to create space-delimited filter patterns
that contain conditions.
The following filter pattern
returns log events
where the first word
in the events is **_ERROR_** or **_WARNING_**.

```

[w1=ERROR || w1=WARNING, w2]

```

Example: Exclude terms from matches
You can create space-delimited filter patterns
that return log events
excluding one or more terms.
Place a not equal symbol ("!=")
before the term or terms
that you want to exclude.
The following code snippet shows an example
of a filter pattern
that returns log events
where the first words aren't **_ERROR_** and **_WARNING_**.

```

[w1!=ERROR && w1!=WARNING, w2]

```

Example: Match the top level item in a resource URI
The following code snippet shows an example
of a filter pattern
that matches the top level item in a resource URI using regex.

```


[logLevel, date, time, method, url=%/service/resource/[0-9]+$%, response_time]


```

Example: Match the child level item in a resource URI
The following code snippet shows an example
of a filter pattern
that matches the child level item in a resource URI using regex.

```


[logLevel, date, time, method, url=%/service/resource/[0-9]+/part/[0-9]+$%, response_time]


```
