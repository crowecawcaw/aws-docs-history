# RLIKE

The RLIKE operator allows you to check if a string matches a specified regular expression
pattern.

Returns `true` if str matches `regexp`, or `false`
otherwise.

## Syntax

```
rlike(str, regexp)
```

## Arguments

_str_

A string expression

_regexp_

A string expression. The regex string should be a Java regular expression.

String literals (including regex patterns) are unescaped in our SQL parser. For example,
to match "\abc", a regular expression for _regexp_ can be
"^\abc$".

## Examples

The following example sets the value of the
`spark.sql.parser.escapedStringLiterals` configuration parameter to
`true`. This parameter is specific to the Spark SQL engine. The
`spark.sql.parser.escapedStringLiterals` parameter in Spark SQL controls how the SQL
parser handles escaped string literals. When set to `true`, the parser will interpret
backslash characters (`\`) within string literals as escape characters, allowing you
to include special characters like newlines, tabs, and quotation marks within your string
values.

```
SET spark.sql.parser.escapedStringLiterals=true;
spark.sql.parser.escapedStringLiterals  true
```

For example, with `spark.sql.parser.escapedStringLiterals=true`, you could use
the following string literal in your SQL query:

```
SELECT 'Hello, world!\n'

```

The newline character `\n` would be interpreted as a literal newline character
in the output.

The following example performs a regular expression pattern match. The first argument is
passed to the RLIKE operator. It's a string that represents a file path, where the actual
username is replaced with the pattern '\*\*\*\*'. The second argument is the regular expression
pattern used for the matching. The output (`true`) indicates that the first string
(`'%SystemDrive%\Users\****'`) matches the regular expression pattern
(`'%SystemDrive%\\Users.*'`).

```
SELECT rlike('%SystemDrive%\Users\John', '%SystemDrive%\Users.*');
true
```
