# ALTER TABLE ADD COLUMNS

Adds one or more columns to an existing Iceberg table.

## Synopsis

```
ALTER TABLE [`db_name`.]`table_name` ADD COLUMNS (`col_name` `data_type` [,...])
```

## Examples

The following example adds a `comment` column of type
`string` to an Iceberg table.

```
ALTER TABLE iceberg_table ADD COLUMNS (comment string)
```

The following example adds a `point` column of type
`struct` to an Iceberg table.

```
ALTER TABLE iceberg_table
ADD COLUMNS (point struct<x: double, y: double>)
```

The following example adds a `points` column that is an array of
structs to an Iceberg table.

```
ALTER TABLE iceberg_table
ADD COLUMNS (points array<struct<x: double, y: double>>)
```
