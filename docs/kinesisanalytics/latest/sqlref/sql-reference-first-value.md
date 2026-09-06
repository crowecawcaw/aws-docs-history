

# FIRST\_VALUE
<a name="sql-reference-first-value"></a>

```
FIRST_VALUE( <value-expression>) <null treatment> OVER <window-specification>
```

FIRST\_VALUE returns the evaluation of the <value expression> from the first row that qualifies for the aggregate. FIRST\_VALUE requires the OVER clause, and is considered an [Analytic Functions](sql-reference-analytic-functions.md). FIRST\_VALUE has a null treatment option defined in the following table.


| Null treatment option | Effect | 
| --- | --- | 
| FIRST\_VALUE(x) IGNORE NULLS OVER <window-specification> | Returns first non null value of x in <window-specification> | 
| FIRST\_VALUE(x) RESPECT NULLS OVER <window-specification> | Returns first value, including null of x in <window-specification> | 
| FIRST\_VALUE(x) OVER <window-specification> | Returns first value, including null of x in <window-specification> | 