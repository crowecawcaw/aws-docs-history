

 Amazon Redshift will no longer support the use of Python UDFs after June 30, 2026. We will start enforcing it in phases. For more information on the details of Python end of life and migration options, see the [ blog post ](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/) that was published on June 30, 2025. 

# SHOW COLUMN GRANTS
<a name="r_SHOW_COLUMN_GRANTS"></a>

Displays grants on a column within a table.

## Required permissions
<a name="r_SHOW_COLUMN_GRANTS-required-permissions"></a>

SHOW GRANTS for a target object will only display grants that are visible to the current user. A grant is visible to the current user if the current user satisfies one of the following criteria:
+ Be a superuser
+ Be the granted user
+ Be granted owner of the granted role
+ Be granted the role targeted by the object grant

## Syntax
<a name="r_SHOW_COLUMN_GRANTS-synopsis"></a>

```
SHOW COLUMN GRANTS ON TABLE
{ database_name.schema_name.table_name | schema_name.table_name }
[FOR {username | ROLE role_name | PUBLIC}]
[LIMIT row_limit]
```

## Parameters
<a name="r_SHOW_COLUMN_GRANTS-parameters"></a>

database\_name  
The name of the database containing the target table

schema\_name  
The name of the schema containing the target table

table\_name  
The name of the target table

username  
Only include grants to username in the output

role\_name  
Only include grants to role\_name in the output

PUBLIC  
Only include grants to PUBLIC in the output

row\_limit  
The maximum number of rows to return. The *row\_limit* can be 0–10,000.

## Examples
<a name="r_SHOW_COLUMN_GRANTS-examples"></a>

The following example shows column grants on table demo\_db.demo\_schema.t100:

```
SHOW COLUMN GRANTS ON TABLE demo_db.demo_schema.t100;
 database_name | schema_name | table_name | column_name | object_type | privilege_type | identity_id | identity_name | identity_type | admin_option | privilege_scope | grantor_name 
---------------+-------------+------------+-------------+-------------+----------------+-------------+---------------+---------------+--------------+-----------------+--------------
 demo_db       | demo_schema | t100       | b           | COLUMN      | UPDATE         |         134 | bob           | user          | f            | COLUMN          | dbadmin
 demo_db       | demo_schema | t100       | a           | COLUMN      | SELECT         |         130 | alice         | user          | f            | COLUMN          | dbadmin
 demo_db       | demo_schema | t100       | a           | COLUMN      | UPDATE         |         130 | alice         | user          | f            | COLUMN          | dbadmin
```

The following example shows column grants on table demo\_schema.t100 for user bob:

```
SHOW COLUMN GRANTS ON TABLE demo_schema.t100 for bob;
 database_name | schema_name | table_name | column_name | object_type | privilege_type | identity_id | identity_name | identity_type | admin_option | privilege_scope | grantor_name 
---------------+-------------+------------+-------------+-------------+----------------+-------------+---------------+---------------+--------------+-----------------+--------------
 demo_db       | demo_schema | t100       | b           | COLUMN      | UPDATE         |         135 | bob           | user          | f            | COLUMN          | dbadmin
```