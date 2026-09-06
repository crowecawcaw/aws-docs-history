

# COT function
<a name="COT"></a>

COT is a trigonometric function that returns the cotangent of a number. The input parameter must be nonzero. 

## Syntax
<a name="COT-synopsis"></a>

```
COT(number)
```

## Argument
<a name="COT-argument"></a>

 *number*   
The input parameter is a `DOUBLE PRECISION` number. 

## Return type
<a name="COT-return-type"></a>

`DOUBLE PRECISION`

## Examples
<a name="COT-examples"></a>

To return the cotangent of 1, use the following example. 

```
SELECT COT(1);

+--------------------+
|        cot         |
+--------------------+
| 0.6420926159343306 |
+--------------------+
```