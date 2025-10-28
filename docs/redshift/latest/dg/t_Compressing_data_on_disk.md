Amazon Redshift will no longer support the creation of new Python UDFs starting November 1, 2025.
If you would like to use Python UDFs, create the UDFs prior to that date.
Existing Python UDFs will continue to function as normal. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# Column compression to reduce the size of stored data

_Compression_ is a column-level operation that
reduces the size of data when it is stored. Compression conserves storage space and
reduces the size of data that is read from storage, which reduces the amount of disk I/O
and therefore improves query performance.

ENCODE AUTO is the default for tables. When a table is set to ENCODE AUTO, Amazon Redshift automatically manages compression encoding
for all columns in the table.
For more information, see [CREATE TABLE](r_CREATE_TABLE_NEW.md "r_CREATE_TABLE_NEW.md")
and [ALTER TABLE](r_ALTER_TABLE.md "r_ALTER_TABLE.md").

However, if you specify compression encoding for any column in the table, the table is no
longer set to ENCODE AUTO. Amazon Redshift no longer automatically manages compression encoding for all columns in the table.

You can apply a compression type, or _encoding_, to the columns in
a table manually when you create the table. Or you can use the COPY command to analyze
and apply compression automatically. For more information, see [Let COPY choose compression
encodings](c_best-practices-use-auto-compression.md "c_best-practices-use-auto-compression.md"). For details about applying
automatic compression, see [Loading tables with automatic
compression](c_Loading_tables_auto_compress.md "c_Loading_tables_auto_compress.md").

###### Note

We strongly recommend using the COPY command to apply automatic
compression.

You might choose to apply compression encodings manually if the new table shares the
same data characteristics as another table. Or you might do so if you discover in
testing that the compression encodings applied during automatic compression are not the
best fit for your data. If you choose to apply compression encodings manually, you can
run the [ANALYZE COMPRESSION](r_ANALYZE_COMPRESSION.md "r_ANALYZE_COMPRESSION.md")
command against an already populated table and use the results to choose compression
encodings.

To apply compression manually, you specify compression encodings for individual
columns as part of the CREATE TABLE statement. The syntax is as follows.

```
CREATE TABLE *table\_name* (*column\_name*
*data\_type* ENCODE *encoding-type*)[, ...]
```

Here, _encoding-type_ is taken from the keyword table in the
following section.

For example, the following statement creates a two-column table, PRODUCT. When data is
loaded into the table, the PRODUCT_ID column is not compressed, but the PRODUCT_NAME
column is compressed, using the byte dictionary encoding (BYTEDICT).

```
create table product(
product_id int encode raw,
product_name char(20) encode bytedict);
```

You can specify the encoding for a column when it is added to a table using the
ALTER TABLE command.

```
ALTER TABLE table-name ADD [ COLUMN ] column_name column_type ENCODE *encoding-type*
```

###### Topics

- [Compression encodings](c_Compression_encodings.md "c_Compression_encodings.md")
- [Testing compression encodings](t_Verifying_data_compression.md "t_Verifying_data_compression.md")
