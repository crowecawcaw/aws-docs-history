

# FLOOR function
<a name="FLOOR"></a>

The FLOOR function rounds a number down to the next whole number. 

## Syntax
<a name="FLOOR-synopsis"></a>

```
FLOOR (number)
```

## Argument
<a name="FLOOR-argument"></a>

 *number*   
The number or expression that evaluates to a number. It can be the SMALLINT, INTEGER, BIGINT, DECIMAL, FLOAT4, or FLOAT8 type. 

## Return type
<a name="FLOOR-return-type"></a>

FLOOR returns the same data type as its argument. 

## Example
<a name="FLOOR-example"></a>

The example shows the value of the commission paid for a given sales transaction before and after using the FLOOR function. 

```
select commission from sales
where salesid=10000;

floor
-------
28.05
(1 row)

select floor(commission) from sales
where salesid=10000;

floor
-------
28
(1 row)
```