# DECODE function

The DECODE function is the counterpart to the ENCODE function, which is used to convert
a string to a binary format using a specific character encoding. The DECODE function takes
the binary data and converts it back to a readable string format using the specified
character encoding.

This function is useful when you need to work with binary data stored in a database and
need to present it in a human-readable format, or when you need to convert data between
different character encodings.

## Syntax

```
decode(expr, charset)
```

## Arguments

_expr_

A BINARY expression encoded in charset.

_charset_

A STRING expression.

Supported character set encodings (case-insensitive):
`'US-ASCII'`, `'ISO-8859-1'`, `'UTF-8'`,
`'UTF-16BE'`, `'UTF-16LE'`, and
`'UTF-16'`.

## Return type

The DECODE function returns a STRING.

## Example

The following example has a table called `messages` with a column called
`message_text` that stores message data in a binary format using the UTF-8
character encoding. The DECODE function converts the binary data back to a readable
string format. The output of this query is the readable text of the message stored in
the messages table, with the ID `123`, converted from the binary format to a
string using the `'utf-8'` encoding.

```
SELECT decode(message_text, 'utf-8') AS message
FROM messages
WHERE message_id = 123;
```
