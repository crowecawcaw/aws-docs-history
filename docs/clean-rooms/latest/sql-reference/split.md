# SPLIT function

The SPLIT function allows you to extract substrings from a larger string and work with
them as an array. The SPLIT function is useful when you need to break down a string into
individual components based on a specific delimiter or pattern.

## Syntax

```
split(str, regex, limit)
```

## Arguments

_str_

A string expression to split.

_regex_

A string representing a regular expression. The _regex_ string should be a Java regular expression.

_limit_

An integer expression which controls the number of times the _regex_ is applied.

- limit > 0: The resulting array's length will not be more than limit,
  and the resulting array's last entry will contain all input beyond the
  last matched _regex_.
- limit <= 0: _regex_ will be
  applied as many times as possible, and the resulting array can be of any
  size.

## Return type

The SPLIT function returns an ARRAY<STRING>.

If `limit > 0`: The resulting array’s length will not be more than limit,
and the resulting array’s last entry will contain all input beyond the last matched
regex.

If `limit <= 0`: regex will be applied as many times as possible, and
the resulting array can be of any size.

## Example

In this example, the SPLIT function splits the input string
`'oneAtwoBthreeC'` wherever it encounters the characters `'A'`,
`'B'`, or `'C'` (as specified by the regular expression pattern
`'[ABC]'`). The resulting output is an array of four elements:
`"one"`, `"two"`, `"three"`, and an empty string
`""`.

```
SELECT split('oneAtwoBthreeC', '[ABC]');
 ["one","two","three",""]
```
