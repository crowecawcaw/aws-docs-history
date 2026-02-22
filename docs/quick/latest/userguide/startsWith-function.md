# startsWith

`startsWith` evaluates if the expression starts with a substring that
you specify. If the expression starts with the substring, `startsWith`
returns true, and otherwise it returns false.

## Syntax

```
startsWith(`expression`, `substring`, `string-comparison-mode`)
```

## Arguments

_expression_

The expression must be a string. It can be the name of a field
that uses the string data type, a literal value like `'12
 Main Street'`, or a call to another function that
outputs a string.

_substring_

The set of characters to check against the
_expression_. The substring can occur one or
more times in the _expression_.

_string-comparison-mode_

(Optional) Specifies the string comparison mode to use:

- `CASE_SENSITIVE` – String comparisons
  are case-sensitive.
- `CASE_INSENSITIVE` – String comparisons
  are case-insensitive.

This value defaults to `CASE_SENSITIVE` when
blank.

## Return type

Boolean

## Examples

### Default

case sensitive example

The following case sensitive example evaluates if `state_nm`
startsWith `New`.

```
startsWith(`state_nm`, `"New"`)
```

The following are the given field values.

```
New York
new york
```

For these field values, the following values are returned.

```
true
false
```

### Case

insensitive example

The following case insensitive example evaluates if `state_nm`
startsWith `new`.

```
startsWith(`state_nm`, `"new"`, CASE_INSENSITIVE)
```

The following are the given field values.

```
New York
new york
```

For these field values, the following values are returned.

```
true
true
```

### Example

with conditional statements

The `startsWith` function can be used as the conditional
statement within the following If functions: [avgIf](../../../quicksight/latest/user/avgIf-function.md "../../../quicksight/latest/user/avgIf-function.md"), [minIf](../../../quicksight/latest/user/minIf-function.md "../../../quicksight/latest/user/minIf-function.md"), [distinct_countIf](../../../quicksight/latest/user/distinct_countIf-function.md "../../../quicksight/latest/user/distinct_countIf-function.md"), [countIf](../../../quicksight/latest/user/countIf-function.md "../../../quicksight/latest/user/countIf-function.md"),
[maxIf](../../../quicksight/latest/user/maxIf-function.md "../../../quicksight/latest/user/maxIf-function.md"), [medianIf](../../../quicksight/latest/user/medianIf-function.md "../../../quicksight/latest/user/medianIf-function.md"), [stdevIf](../../../quicksight/latest/user/stdevIf-function.md "../../../quicksight/latest/user/stdevIf-function.md"),
[stdevpIf](../../../quicksight/latest/user/stdevpIf-function.md "../../../quicksight/latest/user/stdevpIf-function.md"),
[sumIf](../../../quicksight/latest/user/sumIf-function.md "../../../quicksight/latest/user/sumIf-function.md"), [varIf](../../../quicksight/latest/user/varIf-function.md "../../../quicksight/latest/user/varIf-function.md"), and [varpIf](../../../quicksight/latest/user/varpIf-function.md "../../../quicksight/latest/user/varpIf-function.md").

The following example sums `Sales` only if state_nm starts with
`New`.

```
sumIf(`Sales`,startsWith(`state_nm`, `"New"`))
```

### Does NOT

contain example

The conditional `NOT` operator can be used to evaluate if the
expression does not start with the specified substring.

```
NOT(startsWith(`state_nm`, `"New"`))
```

### Example using

numeric values

Numeric values can be used in the expression or substring arguments by
applying the `toString` function.

```
startsWith(`state_nm`, toString(`5`) )
```
