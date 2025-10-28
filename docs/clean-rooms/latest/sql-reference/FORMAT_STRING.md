# FORMAT_STRING function

The FORMAT_STRING function creates a formatted string by substituting placeholders in a
template string with the provided arguments. It returns a formatted string from
printf-style format strings.

The FORMAT_STRING function works by replacing the placeholders in the template string
with the corresponding values passed as arguments. This type of string formatting can be
useful when you need to dynamically construct strings that include a mix of static text and
dynamic data, such as when generating output messages, reports, or other types of
informative text. The FORMAT_STRING function provides a concise and readable way to create
these types of formatted strings, making it easier to maintain and update the code that
generates the output.

## Syntax

```
format_string(strfmt, obj, ...)
```

## Arguments

_strfmt_

A STRING expression.

_obj_

A STRING or numeric expression.

## Return type

FORMAT_STRING returns a STRING.

## Example

The following example contains a template string that contains two placeholders:
`%d` for a decimal (integer) value, and `%s` for a string
value. The `%d` placeholder is replaced with the decimal (integer) value
(`100`), and the %s placeholder is replaced with the string value
(`"days"`). The output is a template string with the placeholders replaced
by the provided arguments: `"Hello World 100 days"`.

```
SELECT format_string("Hello World %d %s", 100, "days");
 Hello World 100 days
```
