

# OPTIMIZE
<a name="optimize-statement"></a>

Optimizes rows in an Apache Iceberg table by rewriting data files into a more optimized layout based on their size and number of associated delete files.

**Note**  
`OPTIMIZE` is transactional and is supported only for Apache Iceberg tables.

## Syntax
<a name="optimize-statement-syntax"></a>

The following syntax summary shows how to optimize data layout for an Iceberg table.

```
OPTIMIZE [{{db_name}}.]{{table_name}} REWRITE DATA USING BIN_PACK
  [WHERE {{predicate}}]
```

**Note**  
Only partition columns are allowed in the `WHERE` clause {{predicate}}. Specifying a non-partition column will cause the query to fail. 

The compaction action is charged by the amount of data scanned during the rewrite process. The `REWRITE DATA` action uses predicates to select for files that contain matching rows. If any row in the file matches the predicate, the file is selected for optimization. Thus, to control the number of files affected by the compaction operation, you can specify a `WHERE` clause.

## Configuring compaction properties
<a name="optimize-statement-configuring-compaction-properties"></a>

To control the size of the files to be selected for compaction and the resulting file size after compaction, you can use table property parameters. You can use the [ALTER TABLE SET TBLPROPERTIES](querying-iceberg-alter-table-set-properties.md) command to configure the related [table properties](querying-iceberg-creating-tables.md#querying-iceberg-table-properties).

## Additional resources
<a name="optimize-statement-additional-resources"></a>

[Optimize Iceberg tables](querying-iceberg-data-optimization.md)