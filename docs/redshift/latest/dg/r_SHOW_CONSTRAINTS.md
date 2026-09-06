

 Amazon Redshift will no longer support the use of Python UDFs after June 30, 2026. We will start enforcing it in phases. For more information on the details of Python end of life and migration options, see the [ blog post ](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/) that was published on June 30, 2025. 

# SHOW CONSTRAINTS
<a name="r_SHOW_CONSTRAINTS"></a>

Shows a list of primary key and foreign key constraints in a table.

## Required permissions
<a name="r_SHOW_CONSTRAINTS-required-permissions"></a>

To execute SHOW CONSTRAINTS on a table, the current user must satisfy one of the following criteria:
+ Be a superuser
+ Be the owner of the table
+ Be granted USAGE privilege on the parent schema and SELECT privilege on the table

## Syntax
<a name="r_SHOW_CONSTRAINTS-synopsis"></a>

```
SHOW CONSTRAINTS {PRIMARY KEYS | FOREIGN KEYS [EXPORTED]}
FROM TABLE
{ database_name.schema_name.table_name | schema_name.table_name }
[LIMIT row_limit]
```

## Parameters
<a name="r_SHOW_CONSTRAINTS-parameters"></a>

*database\_name*  
The name of the database containing the target table

*schema\_name*  
The name of the schema containing the target table

*table\_name*  
The name of the target table

EXPORTED  
When EXPORTED is specified, then list all foreign keys from other tables that reference the target table.

*row\_limit*  
The maximum number of rows to return. The *row\_limit* can be 0–10,000.

## Examples
<a name="r_SHOW_CONSTRAINTS-examples"></a>

The following example shows primary key constraints from table demo\_db.demo\_schema.pk1:

```
SHOW CONSTRAINTS PRIMARY KEYS FROM TABLE demo_db.demo_schema.pk1;
 database_name | schema_name | table_name | pk_name  | column_name | key_seq 
---------------+-------------+------------+----------+-------------+---------
 demo_db       | demo_schema | pk1        | pk1_pkey | i           |       1
 demo_db       | demo_schema | pk1        | pk1_pkey | j           |       2
 demo_db       | demo_schema | pk1        | pk1_pkey | c           |       3
```

The following example shows foreign key constraints from table demo\_schema.fk2:

```
SHOW CONSTRAINTS FOREIGN KEYS FROM TABLE demo_schema.fk2;
 pk_database_name | pk_schema_name | pk_table_name | pk_column_name | fk_database_name | fk_schema_name | fk_table_name | fk_column_name | key_seq |  fk_name   | pk_name  | update_rule | delete_rule | deferrability 
------------------+----------------+---------------+----------------+------------------+----------------+---------------+----------------+---------+------------+----------+-------------+-------------+---------------
 demo_db          | demo_schema    | pk1           | i              | demo_db          | demo_schema    | fk2           | i              |       1 | fk2_i_fkey | pk1_pkey |             |             | 
 demo_db          | demo_schema    | pk1           | j              | demo_db          | demo_schema    | fk2           | j              |       2 | fk2_i_fkey | pk1_pkey |             |             | 
 demo_db          | demo_schema    | pk1           | c              | demo_db          | demo_schema    | fk2           | c              |       3 | fk2_i_fkey | pk1_pkey |             |             |
```

The following example shows exported foreign key constraints from table demo\_schema.pk1:

```
SHOW CONSTRAINTS FOREIGN KEYS EXPORTED FROM TABLE demo_schema.pk1;
 pk_database_name | pk_schema_name | pk_table_name | pk_column_name | fk_database_name | fk_schema_name | fk_table_name | fk_column_name | key_seq |     fk_name     | pk_name  | update_rule | delete_rule | deferrability 
------------------+----------------+---------------+----------------+------------------+----------------+---------------+----------------+---------+-----------------+----------+-------------+-------------+---------------
 demo_db          | demo_schema    | pk1           | i              | demo_db          | demo_schema    | fk2           | i              |       1 | fk2_i_fkey      | pk1_pkey |             |             | 
 demo_db          | demo_schema    | pk1           | j              | demo_db          | demo_schema    | fk2           | j              |       2 | fk2_i_fkey      | pk1_pkey |             |             | 
 demo_db          | demo_schema    | pk1           | c              | demo_db          | demo_schema    | fk2           | c              |       3 | fk2_i_fkey      | pk1_pkey |             |             | 
 demo_db          | demo_schema    | pk1           | i              | demo_db          | demo_schema    | other_fk      | i              |       1 | other_fk_i_fkey | pk1_pkey |             |             | 
 demo_db          | demo_schema    | pk1           | j              | demo_db          | demo_schema    | other_fk      | j              |       2 | other_fk_i_fkey | pk1_pkey |             |             | 
 demo_db          | demo_schema    | pk1           | c              | demo_db          | demo_schema    | other_fk      | c              |       3 | other_fk_i_fkey | pk1_pkey |             |             |
```