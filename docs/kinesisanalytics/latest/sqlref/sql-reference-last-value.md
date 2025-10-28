# LAST_VALUE

```
LAST_VALUE ( <value-expression> )  OVER <window-specification>
```

LAST_VALUE returns the evaluation of the <value expression> from the last row that
qualifies for the aggregate.

| Null Treatment Option                                   | Effect                                                            |
| ------------------------------------------------------- | ----------------------------------------------------------------- |
| LAST_VALUE(x) IGNORE NULLS OVER <window-specification>  | Returns last non null value of x in <window-specification>        |
| LAST_VALUE(x) RESPECT NULLS OVER <window-specification> | Returns last value, including null of x in <window-specification> |
| LAST_VALUE(x) OVER <window-specification>               | Returns last value, including null of x in <window-specification> |
