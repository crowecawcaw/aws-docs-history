**Introducing a new console experience for AWS WAF**

You can now use the updated experience to access AWS WAF functionality anywhere in the console.
For more details, see [Working with the console](working-with-console.md "working-with-console.md").

# Using pre-parse text transformations in AWS WAF

Pre-parse text transformations normalize the raw query string before AWS WAF
parses it into individual query arguments. These transformations address parser
differential attacks and HTTP Parameter Pollution (HPP), where attackers encode
or manipulate query string delimiters to bypass inspection rules.

You can use pre-parse text transformations only when the request component
is `SingleQueryArgument` or `AllQueryArguments`. AWS WAF
applies pre-parse text transformations before standard text transformations. You
can specify up to 10 pre-parse text transformations per rule statement. Each
pre-parse text transformation adds 10 WCUs to the rule statement cost.

In the API, you configure pre-parse text transformations using the optional
`PreParseTextTransformations` setting in your rule statement.

###### Note

If you don't need any pre-parse normalization, don't specify a pre-parse
text transformation. The default behavior is `NONE`, which passes
the raw query string to the parser without modification.

The following pre-parse text transformations are available.

None – `NONE`

AWS WAF inspects the web request as received, without any pre-parse text transformations.

URL decode – `URL_DECODE`

AWS WAF URL-decodes the raw query string before parsing. Decodes
%HH sequences (for example, %26 becomes & and %3D becomes =).
This might expose new query parameter boundaries that were
previously encoded.

URL decode Unicode – `URL_DECODE_UNI`

Like `URL_DECODE`, but also decodes Unicode-encoded
sequences (%uHHHH). If the code is in the full-width ASCII code
range of `FF01-FF5E`, the higher byte is used to detect
and adjust the lower byte. Otherwise, only the lower byte is used
and the higher byte is zeroed.

Combine duplicate query arguments by comma – `COMBINE_DUPLICATE_QUERY_ARGS_BY_COMMA`

AWS WAF merges all values for duplicate query parameter keys into
a single comma-separated (0x2C) string at the first occurrence position,
then removes the later duplicates. For example,
`a=1&b=2&a=3` becomes
`a=1,3&b=2`. Use this transformation when your
backend combines duplicate query parameters into arrays. This is
common in .NET, API Gateway, and Express.js. AWS WAF
inspects the combined value as a single unit.

Replace semicolons with ampersands – `REPLACE_SEMICOLONS_WITH_AMPERSANDS`

AWS WAF replaces all semicolons (0x3B) in the raw query string with
ampersands (0x26) before parsing. Some web frameworks and services,
including AWS API Gateway REST APIs, treat semicolons as query
parameter delimiters equivalent to ampersands. This transformation
normalizes the query string. AWS WAF then splits on semicolons the
same way your backend does, ensuring consistent parameter
parsing.
