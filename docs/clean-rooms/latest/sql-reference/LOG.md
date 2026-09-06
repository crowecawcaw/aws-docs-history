

# LOG function
<a name="LOG"></a>

Returns the logarithm of `expr` with `base`.

## Syntax
<a name="LOG-synopsis"></a>

```
LOG(base, expr)
```

## Argument
<a name="LOG-argument"></a>

 *expr*   
The expression must have an integer, decimal, or floating-point data type. 

 *base*   
The base for the logarithm calculation. Must be a positive number (not equal to 1) of double precision data type. 

## Return type
<a name="LOG-return-type"></a>

The LOG function returns a double precision number. 

## Example
<a name="LOG-example"></a>

The following example returns the base 10 logarithm of the number 100: 

```
select log(10, 100);
--------
2
(1 row)
```