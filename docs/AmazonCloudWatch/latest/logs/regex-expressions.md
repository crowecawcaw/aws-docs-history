# Supported regular expressions (regex) syntax

Use regular expressions when you need flexible pattern matching that goes beyond exact text matches. Regex is particularly useful for:

- **Variable formats:** Match IP addresses, timestamps, or IDs with different formats
- **Partial matches:** Find log entries containing specific patterns anywhere in the text
- **Complex conditions:** Match ranges of values, optional characters, or alternative spellings
  For example, use `%\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}%` to match any IP address format, or `%[Ee]rror|[Ff]ail%` to catch both "Error"/"error" and "Fail"/"fail" in logs.

You can match terms in your log events using a regex pattern surrounded with `%` (percentage signs before and after the regex pattern). The following example shows a filter pattern that returns all log events containing the **AUTHORIZED** keyword:

```

%AUTHORIZED%

```

This filter pattern returns log event messages, such as:

- `[ERROR 401] UNAUTHORIZED REQUEST`
- `[SUCCESS 200] AUTHORIZED REQUEST`
  Expand the following section to view details about the specific regex operators and syntax rules supported in CloudWatch Logs filter patterns.

When using regex to search and filter log data, you must surround your
expressions with `%`.

Filter patterns with regex can only include the following:

- Alphanumeric characters – An alphanumeric character is a
  character that is either a letter (from A to Z or a to z) or a digit
  (from 0 to 9).
- Supported symbol characters – These include: '`:`',
  '`_`', '`#`', '`=`',
  '`@`','`/`', '`;`',
  '`,`', and '`-`'. For example,
  `%something!%` would be rejected since '`!`'
  is not supported.
- Supported operators – These include: '`^`',
  '`$`', '`?`', '`[`',
  '`]`', '`{`', '`}`',
  '`|`', '`\`', '`*`',
  '`+`', and '`.`'.
  The `(` and `)` operators are not supported. You cannot
  use parentheses to define a subpattern.

Multi-byte characters are not supported.

###### Note

**Quotas**

There is a maximum of 5 filter patterns containing regex for each log
group when creating metric filters or subscription filters.

There is a limit of 2 regex for each filter pattern when creating a
delimited or JSON filter pattern for metric filters and subscription filters
or when filtering log events or Live Tail.

**Usage of supported operators**

- `^`: Anchors the match to the beginning of a string. For
  example, `%^[hc]at%` matches "hat" and "cat", but only at the
  beginning of a string.
- `$`: Anchors the match to the end of a string. For example,
  `%[hc]at$%` matches "hat" and "cat", but only at the end
  of a string.
- `?`: Matches zero or one occurrence of the preceding term.
  For example, `%colou?r%` can match both "color" and
  "colour".
- `[]`: Defines a character class. Matches the character list
  or character range contained within the brackets. For example,
  `%[abc]%` matches "a", "b", or "c"; `%[a-z]%`
  matches any lowercase letter from "a" to "z"; and
  `%[abcx-z]%`matches "a", "b", "c", "x", "y", or
  "z".
- `{m, n}`: Matches the preceding term at least
  _m_ and not more than _n_
  times. For example, `%a{3,5}%` matches only "aaa", "aaaa",
  and "aaaaa".

###### Note

Either _m_ or _n_ can be
omitted if you chose not to define a minimum or maximum.

- `|`: Boolean "Or", which matches the term on either side of
  the vertical bar. For example:
  - `%gra|ey%` can match "gray" or "grey"
  - `%^starting|^initializing|^shutting down%` can
    match "starting ...", or "initializing ...", or "shutting
    down", but won't match "skipping initializing ..."
  - `%abcc|ab[^c]$` can match "abcc ..." and "aba
    ..." but won't match "aac ..."

- `\`: Escape character, which allows you to use the literal
  meaning of an operator instead of its special meaning. For example,
  `%\[.\]%` matches any single character surrounded by "["
  and "]" since the brackets are escaped, such as "[a]", "[b]", "[7]",
  "[@]", "[]]", and "[ ]".

###### Note

`%10\.10\.0\.1%` is the correct way to create a regex
to match the IP address 10.10.0.1.

- `*`: Matches zero or more instances of the preceding term.
  For example, `%ab*c%` can match "ac", "abc", and "abbbc";
  `%ab[0-9]*%` can match "ab", "ab0", and "ab129".
- `+`: Matches one or more instances of the preceding term.
  For example, `%ab+c%` can match "abc", "abbc", and "abbbc",
  but not "ac".
- `.`: Matches any single character. For example,
  `%.at%` matches any three character string ending with
  "at", including "hat", "cat", "bat", "4at", "#at" and " at" (starting
  with a space).

###### Note

When creating a regex to match IP addresses, it is important to
escape the `.` operator. For example,
`%10.10.0.1%` can match "10010,051" which might not
be the actual intended purpose of the expression.

- `\d`, `\D`: Matches a digit/non-digit character.
  For example, `%\d%` is equivalent to `%[0-9]%` and
  `%\D%` is equivalent to `%[^0-9]%`.

###### Note

The uppercase operator denotes the inverse of its lowercase
counterpart.

- `\s`, `\S`: Matches a whitespace
  character/non-whitespace character.

###### Note

The uppercase operator denotes the inverse of its lowercase
counterpart. Whitespace characters include the tab
(`\t`), space(), and newline
(`\n`) characters.

- `\w`, `\W`: Matches an alphanumeric
  character/non-alphanumeric character. For example, `%\w%` is
  equivalent to `%[a-zA-Z_0-9]%` and `%\W%` is
  equivalent to `%[^a-zA-Z_0-9]%`.

###### Note

The uppercase operator denotes the inverse of its lowercase
counterpart.

- `\xhh`: Matches the ASCII mapping for a two-digit
  hexadecimal character. `\x` is the escape sequence which
  indicates that the following characters represent the hexadecimal value
  for ASCII. `hh` specifies the two hexadecimal digits (0-9 and
  A-F) which point to a character in the ASCII table.

###### Note

You can use `\xhh` to match symbol characters that are
not supported by the filter pattern. For example,
`%\x3A%` matches `:`; and
`%\x28%` matches `(`.
