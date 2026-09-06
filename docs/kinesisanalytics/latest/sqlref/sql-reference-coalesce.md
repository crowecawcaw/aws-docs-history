

# COALESCE
<a name="sql-reference-coalesce"></a>

```
COALESCE (
      <value-expression>
      {,<value-expression>}... )
```

The COALESCE function takes a list of expressions (all of which must be of the same type) and returns the first non-null argument from the list. If all of the expressions are null, COALESCE returns null.

## Examples
<a name="sql-reference-coalesce-examples"></a>


| Expression | Result | 
| --- | --- | 
| COALESCE('chair') | chair | 
| COALESCE('chair', null, 'sofa') | chair | 
| COALESCE(null, null, 'sofa') | sofa | 
| COALESCE(null, 2, 5) | 2 | 