

# NULLIF
<a name="sql-reference-nullif"></a>

```
NULLIF ( <value-expression>, <value-expression> )
```

Returns null if the two input arguments are equal, otherwise returns the first value. Both arguments must be of comparable type, or an exception is raised.

## Examples
<a name="sql-reference-nullif-examples"></a>


| Function | Result | 
| --- | --- | 
| NULLIF(4,2) | 4 | 
| NULLIF(4,4) | <null> | 
| NULLIF('amy','fred') | amy | 
| NULLIF('amy', cast(null as varchar(3))) | amy | 
| NULLIF(cast(null as varchar(3)),'fred') | <null> | 