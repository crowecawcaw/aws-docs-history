

# ALTER TABLE ADD COLUMNS
<a name="querying-iceberg-alter-table-add-columns"></a>

Adds one or more columns to an existing Iceberg table.

## Synopsis
<a name="querying-iceberg-alter-table-add-columns-synopsis"></a>

```
ALTER TABLE [{{db_name}}.]{{table_name}} ADD COLUMNS ({{col_name}} {{data_type}} [,...])
```

## Examples
<a name="querying-iceberg-alter-table-add-columns-example"></a>

The following example adds a `comment` column of type `string` to an Iceberg table.

```
ALTER TABLE iceberg_table ADD COLUMNS (comment string)
```

The following example adds a `point` column of type `struct` to an Iceberg table.

```
ALTER TABLE iceberg_table 
ADD COLUMNS (point struct<x: double, y: double>)
```

The following example adds a `points` column that is an array of structs to an Iceberg table.

```
ALTER TABLE iceberg_table 
ADD COLUMNS (points array<struct<x: double, y: double>>)
```