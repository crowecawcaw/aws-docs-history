# ALTER TABLE CHANGE COLUMN

Changes the name, type, order, or comment for a column in a table.

## Synopsis

```
ALTER TABLE [`db_name`.]`table_name`
  CHANGE [COLUMN] `col_old_name` `col_new_name` `column_type`
  [COMMENT `col_comment`] [FIRST|AFTER `column_name`]
```

## Examples

The following example changes the column name `area` to `zip`,
makes the data type integer, and places the renamed column after the `id`
column.

```
ALTER TABLE example_table CHANGE COLUMN area zip int AFTER id
```

The following example adds a comment to the `zip` column in the metadata
for `example_table`. To see the comment, use the AWS CLI [`aws athena get-table-metadata`](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/athena/get-table-metadata.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/athena/get-table-metadata.html") command or visit the schema
for the table in the AWS Glue console.

```
ALTER TABLE example_table CHANGE COLUMN zip zip int COMMENT 'USA zipcode'
```
