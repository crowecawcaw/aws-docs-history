# VALUES

Creates a literal inline table. The table can be anonymous, or you can use the
`AS` clause to specify a table name, column names, or both.

## Synopsis

```
VALUES row [, ...]
```

## Parameters

**row**

The `row` parameter can be a single expression or `(
 column_expression [, ...] )`.

## Examples

Return a table with one column and three rows:

```
VALUES 1, 2, 3
```

Return a table with two columns and three rows:

```
VALUES
    (1, 'a'),
    (2, 'b'),
    (3, 'c')
```

Return a table with the columns `id` and `name`:

```
SELECT * FROM (
    VALUES
        (1, 'a'),
        (2, 'b'),
        (3, 'c')
) AS t (id, name)
```

Create a table called `customers` with the columns `id` and
`name`:

```
CREATE TABLE customers AS
SELECT * FROM (
    VALUES
        (1, 'a'),
        (2, 'b'),
        (3, 'c')
) AS t (id, name)
```

## See also

[INSERT INTO...VALUES](insert-into.md#insert-into-values "insert-into.md#insert-into-values")
