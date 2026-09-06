

# LAST\_VALUE
<a name="sql-reference-last-value"></a>

```
LAST_VALUE ( <value-expression> )  OVER <window-specification>
```

LAST\_VALUE returns the evaluation of the <value expression> from the last row that qualifies for the aggregate. 


| Null Treatment Option | Effect | 
| --- | --- | 
| LAST\_VALUE(x) IGNORE NULLS OVER <window-specification> | Returns last non null value of x in <window-specification> | 
| LAST\_VALUE(x) RESPECT NULLS OVER <window-specification> | Returns last value, including null of x in <window-specification> | 
| LAST\_VALUE(x) OVER <window-specification> | Returns last value, including null of x in <window-specification> | 