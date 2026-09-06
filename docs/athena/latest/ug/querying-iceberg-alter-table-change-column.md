

# ALTER TABLE CHANGE COLUMN
<a name="querying-iceberg-alter-table-change-column"></a>

Changes the name, type, order or comment of a column in an Iceberg table.

**Note**  
`ALTER TABLE REPLACE COLUMNS` is not supported. Because `REPLACE COLUMNS` removes all columns and then adds new ones, it is not supported for Iceberg. `CHANGE COLUMN` is the preferred syntax for schema evolution. 

## Synopsis
<a name="querying-iceberg-alter-table-change-column-synopsis"></a>

```
ALTER TABLE [{{db_name}}.]{{table_name}}
  CHANGE [COLUMN] {{col_old_name}} {{col_new_name}} {{column_type}} 
  [COMMENT {{col_comment}}] [FIRST|AFTER {{column_name}}]
```

## Example
<a name="querying-iceberg-alter-table-change-column-example"></a>

```
ALTER TABLE iceberg_table CHANGE comment blog_comment string AFTER id
```