# VARIABLE_COLUMN_LOG_PARSE

```
 VARIABLE_COLUMN_LOG_PARSE(
  <character-expression>, <columns>, <delimiter-string>
  [ , <escape-string>, <quote-string> ] )
  <columns> := <number of columns> | <list of columns>
  <number of columns> := <numeric value expression>
  <list of columns> := '<column description>[, ...]'
  <column description> := <identifier> TYPE <data type> [ NOT NULL ]
  <delimiter string> := <character-expression>
  <escape-string> := <character-expression>
  <quote-string> := '<begin quote character> [ <end quote character> ]'
```

VARIABLE_COLUMN_LOG_PARSE splits an input string (its first argument,
<character-expression>) into fields separated by a delimiter character or delimiter
string. Thus it handles comma-separated values or tab-separated values. It can be combined with
[FIXED_COLUMN_LOG_PARSE](sql-reference-fixed-column-log-parse.md "sql-reference-fixed-column-log-parse.md") to handle something like maillog, where some
fields are fixed-length and others are variable-length.

###### Note

Parsing of binary files is not supported.

The arguments <escape-string> and <quote-string> are optional. Specifying an
<escape-string> allows the value of a field to contain an embedded delimiter. As a simple
example, if the <delimiter-string> specified a comma, and the <escape-string>
specified a backslash, then an input of "a,b' would be split into two fields "a" and "b", but an
input of "a\,b" would result in a single field "a,b".

Since Amazon Kinesis Data Analytics supports [Expressions and Literals](sql-reference-expressions.md "sql-reference-expressions.md"), a tab can also be a delimiter, specified using a
unicode escape, e.g., u&'\0009', which is a string consisting only of a tab
character.

Specifying a <quote-string> is another way to hide an embedded delimiter. The
<quote-string> should be a one or two character expression: the first is used as the
<begin quote character> character; the second, if present, is used as the <end quote
 character> character. If only one character is supplied, it is used as both to begin and to
end quoted strings. When the input includes a quoted string, that is, a string enclosed in the
characters specified as <quote-string>, then that string appears in one field, even if it
contains a delimiter.

Note that the <begin quote character> and <end quote character> are single
characters and can be different. The <begin quote character> can be used to start and end
the quoted string, or the <begin quote character> can start the quoted string and the
<end quote character> used to end that quoted string.

When a list of columns <list of columns> is supplied as the second parameter
<columns>, the column specifications (<column description>) for types DATE, TIME,
and TIMESTAMP support a format parameter allowing the user to specify exact time component
layout. The parser uses the Java class [java.lang.SimpleDateFormat](https://docs.oracle.com/javase/8/docs/api/java/text/SimpleDateFormat.html "https://docs.oracle.com/javase/8/docs/api/java/text/SimpleDateFormat.html") to parse the strings for those types. [Date and Time Patterns](sql-reference-parse-timestamp-format.md "sql-reference-parse-timestamp-format.md") gives a full description of timestamp format
strings, with examples. The following is an example of a column definition with a format
string:

```
    "name" TYPE TIMESTAMP 'dd/MMM/yyyy:HH:mm:ss'
```

By default, the output columns are named COLUMN1, COLUMN2, COLUMN3, etc., each of SQL data
type VARCHAR(1024).
