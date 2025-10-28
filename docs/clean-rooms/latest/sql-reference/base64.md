# BASE64 function

The BASE64 function converts an expression to a base 64 string using [RFC2045 Base64 transfer encoding for
MIME](https://datatracker.ietf.org/doc/html/rfc2045 "https://datatracker.ietf.org/doc/html/rfc2045").

## Syntax

```
base64(expr)

```

## Arguments

_expr_

A BINARY expression or a STRING which the function will interpret as
BINARY.

## Return type

`STRING`

## Example

To convert the given string input into its Base64 encoded representation. use the
following example. The result is the Base64 encoded representation of the input string
'Spark SQL', which is 'U3BhcmsgU1FM'.

```
SELECT base64('Spark SQL');
 U3BhcmsgU1FM
```
