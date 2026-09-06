

# List tables in a specified database and searching for a table by name
<a name="querying-glue-catalog-listing-tables"></a>

To list metadata for tables, you can query by table schema or by table name.

**Example – Listing tables by schema**  
The following query lists tables that use the `rdspostgresql` table schema.  

```
SELECT table_schema,
       table_name,
       table_type
FROM   information_schema.tables
WHERE  table_schema = 'rdspostgresql'
```
The following table shows a sample result.  



|  | table\_schema | table\_name | table\_type | 
| --- | --- | --- | --- | 
| 1 | rdspostgresql | rdspostgresqldb1\_public\_account | BASE TABLE | 

**Example – Searching for a table by name**  
The following query obtains metadata information for the table `athena1`.  

```
SELECT table_schema,
       table_name,
       table_type
FROM   information_schema.tables
WHERE  table_name = 'athena1'
```
The following table shows a sample result.  



|  | table\_schema | table\_name | table\_type | 
| --- | --- | --- | --- | 
| 1 | default | athena1 | BASE TABLE | 