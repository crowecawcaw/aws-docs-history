

# LOG10
<a name="sql-reference-log10"></a>

```
LOG10 ( <number-expression> )
```

Returns the base 10 logarithm of the input argument. If the argument is negative or 0, an exception is raised. Returns null if the input argument is null.

## Examples
<a name="sql-reference-log10-examples"></a>


|  Function  |  Result  | 
| --- | --- | 
| LOG10(1) | 0.0 | 
| LOG10(100) | 2.0 | 
| log10(cast('23' as decimal)) | 1.3617278360175928 | 

## 
<a name="sql-reference-log10-notes"></a>

**Note**  
LOG10 is not a SQL:2008 standard function; it is an Amazon Kinesis Data Analytics extension to the standard.