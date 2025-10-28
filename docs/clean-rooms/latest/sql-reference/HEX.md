# HEX function

The HEX function converts a numeric value (either an integer or a floating-point number)
to its corresponding hexadecimal string representation.

Hexadecimal is a numeral system that uses 16 distinct symbols (0-9 and A-F) to represent
numeric values. It is commonly used in computer science and programming to represent binary
data in a more compact and human-readable format.

## Syntax

```
hex(expr)
```

## Arguments

_expr_

A BIGINT, BINARY, or STRING expression.

## Return type

HEX returns a STRING. The function returns the hexadecimal representation of the
argument.

## Example

The following example takes the integer value 17 as input and applies the HEX()
function to it. The output is `11`, which is the hexadecimal representation
of the input value `17`.

```
SELECT hex(17);
 11
```

The following example converts the string `'Spark_SQL'` to its hexadecimal
representation. The output is `537061726B2053514C`, which is the hexadecimal
representation of the input string `'Spark_SQL'`.

```
SELECT hex('Spark_SQL');
 537061726B2053514C
```

In this example, the string 'Spark_SQL' is converted as follows:

- 'S' -> 53
- 'p' -> 70
- 'a' -> 61
- 'r' -> 72 '
- k' -> 6B
- '\_' -> 20
- 'S' -> 53
- 'Q' -> 51
- 'L' -> 4C

The concatenation of these hexadecimal values results in the final output
"`537061726B2053514C"`.
