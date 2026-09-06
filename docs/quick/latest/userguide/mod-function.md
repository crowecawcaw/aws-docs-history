

# Mod
<a name="mod-function"></a>

Use the `mod` function to find the remainder after dividing the number by the divisor. You can use the `mod` function or the modulo operator (%) interchangeably.

## Syntax
<a name="mod-function-syntax"></a>

```
mod({{number}}, {{divisor}})
```

```
{{number}}%{{divisor}}
```

## Arguments
<a name="mod-function-arguments"></a>

 *number*   
The number is the positive integer that you want to divide and find the remainder for. 

 *divisor*   
The divisor is the positive integer that you are dividing by. If the divisor is zero, this function returns an error on dividing by 0.

## Example
<a name="mod-function-example"></a>

The following examples return the modulo of 17 when dividing by 6. The first example uses the % operator, and the second example uses the mod function.

```
17%6
```

```
mod( 17, 6 )
```

The following value is returned.

```
5
```