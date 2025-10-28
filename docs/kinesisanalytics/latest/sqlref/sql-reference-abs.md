# ABS

Returns the absolute value of the input argument. Returns `null` if the input
argument is null.

```
ABS ( `<numeric-expression>`  `<interval-expression>`
      )
```

## Examples

| Function                              | Result                          |
| ------------------------------------- | ------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| ABS(2.0)                              | 2.0                             |
| ABS(-1.0)                             | 1.0                             |
| ABS(0)                                | 0                               |
| ABS(-3 \* 3)                          | 9                               |
| ABS(INTERVAL '-3 4:20' DAY TO MINUTE) | INTERVAL '3 4:20' DAY TO MINUTE | If you use `cast as VARCHAR` in SQLline to show the output, the value is returned as `+3 04:20`. `values(cast(ABS(INTERVAL '-3 4:20' DAY TO MINUTE) AS VARCHAR(8))); +-----------+ EXPR$0 +-----------+ +3 04:20 +-----------+ 1 row selected` |
