# UNBASE64 function

The UNBASE64 function converts an argument from a base 64 string to a binary.

Base64 encoding is commonly used to represent binary data (such as images, files, or
encrypted information) in a textual format that is safe for transmission over various
communication channels (such as email, URL parameters, or database storage).

The UNBASE64 function allows you to reverse this process and recover the original binary
data. This type of functionality can be useful in scenarios where you need to work with
data that has been encoded in Base64 format, such as when integrating with external systems
or APIs that use Base64 as a data transfer mechanism.

## Syntax

```
unbase64(expr)
```

## Arguments

_expr_

A STRING expression in a base64 format.

## Return type

`BINARY`

## Example

In the following example, the Base64-encoded string `'U3BhcmsgU1FM'` is
converted back to the original string `'Spark SQL'`.

```
SELECT unbase64('U3BhcmsgU1FM');
 Spark SQL
```
