

# Operators
<a name="functions-jsonata-operators"></a>

## Arithmetic
<a name="functions-jsonata-operators-arithmetic"></a>


| Operator | Description | Example | Result | 
| --- | --- | --- | --- | 
| \+ | Addition | 5 \+ 3 | 8 | 
| - | Subtraction | 10 - 4 | 6 | 
| \* | Multiplication | 6 \* 7 | 42 | 
| / | Division | 15 / 4 | 3.75 | 
| % | Modulo | 17 % 5 | 2 | 

## Comparison
<a name="functions-jsonata-operators-comparison"></a>


| Operator | Description | Example | 
| --- | --- | --- | 
| = | Equal to | media.contextual.garm.risk = "LOW" | 
| \!= | Not equal to | stop\_reason \!= "max\_tokens" | 
| < | Less than | $count(media.frames) < 4 | 
| > | Greater than | usage.output\_tokens > 200 | 
| <= | Less than or equal to | $count(media.clip.events) <= 2 | 
| >= | Greater than or equal to | media.clip.eventState.period >= 4 | 

## Boolean and membership
<a name="functions-jsonata-operators-boolean"></a>


| Operator | Description | Example | 
| --- | --- | --- | 
| and | Logical AND | $exists(media.transcript) and $length(media.transcript) > 20 | 
| or | Logical OR | risk = "HIGH" or risk = "FLOOR" | 
| in | Tests membership in an array | "Basketball" in media.contextual.categories | 
| \~> | Chains a value into a function as its first argument | media.transcript \~> $lowercase \~> $trim | 

Use parentheses to control precedence.

```
$count(media.clip.events) > 0 and (risk = "LOW" or risk = "MEDIUM")
```

**Note**  
There is no `not` keyword. Use the `$not()` function.