

# List databases and searching a specified database
<a name="querying-glue-catalog-querying-available-databases-including-rdbms"></a>

The examples in this section show how to list the databases in metadata by schema name.

**Example – Listing databases**  
The following example query lists the databases from the `information_schema.schemata` table.  

```
SELECT schema_name
FROM   information_schema.schemata
LIMIT  10;
```
The following table shows sample results.  



|  |  | 
| --- |--- |
| 6 | alb-databas1 | 
| 7 | alb\_original\_cust | 
| 8 | alblogsdatabase | 
| 9 | athena\_db\_test | 
| 10 | athena\_ddl\_db | 

**Example – Searching a specified database**  
In the following example query, `rdspostgresql` is a sample database.  

```
SELECT schema_name
FROM   information_schema.schemata
WHERE  schema_name = 'rdspostgresql'
```
The following table shows sample results.  



|  | schema\_name | 
| --- | --- | 
| 1 | rdspostgresql | 