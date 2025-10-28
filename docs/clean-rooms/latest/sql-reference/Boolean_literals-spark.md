# Boolean literals

The following rules are for working with Boolean literals that are supported by AWS Clean Rooms
Spark SQL.

Use a Boolean literal to specify a Boolean value, such as `TRUE` or
`FALSE`.

## Syntax

```
TRUE | FALSE

```

## Example

The following example shows a column with a specified value of `TRUE`
.

````
SELECT TRUE AS col;
+----+
| col| +----+
|true| +----+ ```
````
