# POWER

```
 POWER ( <base>, <exponent> )
 <base> := <number-expression>
 <exponent> := <number-expression>

```

Returns the value of the first argument (the base) raised to the power of the second argument (the exponent). Returns null if either the
base or the exponent is null, and raises an exception if the base is zero and the exponent is negative, or if the base is negative and the exponent is not a whole number.

## Examples

| Function        | Result             |
| --------------- | ------------------ |
| POWER(3,2)      | 9                  |
| POWER(-2,3)     | -8                 |
| POWER(4,-2)     | 1/16 ..or.. 0.0625 |
| POWER(10.1,2.5) | 324.19285157140644 |
