# LOG10

```
LOG10 ( <number-expression> )

```

Returns the base 10 logarithm of the input argument. If the argument is negative or 0, an
exception is raised. Returns null if the input argument is null.

## Examples

| Function                     | Result             |
| ---------------------------- | ------------------ | --------------------------------------------------------------------------------------------------------------------------- |
| LOG10(1)                     | 0.0                |
| LOG10(100)                   | 2.0                |
| log10(cast('23' as decimal)) | 1.3617278360175928 | ## ###### Note LOG10 is not a SQL:2008 standard function; it is an Amazon Kinesis Data Analytics extension to the standard. |
