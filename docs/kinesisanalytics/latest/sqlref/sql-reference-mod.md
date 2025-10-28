# MOD

```
MOD ( <dividend>, <divisor> )
 <dividend> := <integer-expression>
 <divisor>  := <integer-expression>

```

Returns the remainder when the first argument (the dividend is divided by the second numeric
argument (the divisor). If the divisor is zero, a divide by zero error is raised.

## Examples

| Function  | Result |
| --------- | ------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| MOD(4,2)  | 0      |
| MOD(5,3)  | 2      |
| MOD(-4,3) | -1     |
| MOD(5,12) | 5      | ## Limitations The Amazon Kinesis Data Analytics MOD function only supports arguments of scale 0 (integers). This is a departure from the SQL:2008 standard, which supports any numeric argument. Other numeric arguments can be CAST to an integer, of course. |
