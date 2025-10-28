# ENCODE function

The ENCODE function is used to convert a string to its binary representation using a
specified character encoding.

This function is useful when you need to work with binary data or when you need to
convert between different character encodings. For example, you might use the ENCODE
function when storing data in a database that requires binary storage, or when you need to
transfer data between systems that use different character encodings.

## Syntax

```
encode(str, charset)
```

## Arguments

_str_

A STRING expression to be encoded.

_charset_

A STRING expression specifying the encoding.

Supported character set encodings (case-insensitive):
`'US-ASCII'`, `'ISO-8859-1'`, `'UTF-8'`,
`'UTF-16BE'`, `'UTF-16LE'`, and
`'UTF-16'`.

## Return type

The ENCODE function returns a BINARY.

## Example

The following example converts the string `'abc'` to its binary
representation using the `'utf-8'` encoding, which in this case results in
the original string being returned. This is because the `'utf-8'` encoding is
a variable-width character encoding that can represent the entire ASCII character set
(which includes the letters `'a'`, `'b'`, and `'c'`)
using a single byte per character. Therefore, the binary representation of
`'abc'` using `'utf-8'` is the same as the original
string.

```
SELECT encode('abc', 'utf-8');
 abc
```
