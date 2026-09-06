

 Amazon Redshift will no longer support the use of Python UDFs after June 30, 2026. We will start enforcing it in phases. For more information on the details of Python end of life and migration options, see the [ blog post ](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/) that was published on June 30, 2025. 

# SHOW SCHEMAS
<a name="r_SHOW_SCHEMAS"></a>

Shows a list of schemas in a database, along with some schema attributes.

Each output row consists of database name, schema name, schema owner, schema type, schema ACL, source database, and schema option. For more information about these attributes, see [SVV\_ALL\_SCHEMAS](r_SVV_ALL_SCHEMAS.md).

If more than 10,000 schemas can result from the SHOW SCHEMAS command, then an error is returned.

## Required permissions
<a name="r_SHOW_SCHEMAS-privileges"></a>

To view a schema in an Amazon Redshift table, the current user must satisfy one of the following criteria:
+ Be a superuser.
+ Be the owner of the schema.
+ Granted USAGE privilege on the schema.

## Syntax
<a name="r_SHOW_SCHEMAS-synopsis"></a>

```
SHOW SCHEMAS FROM DATABASE database_name [LIKE 'filter_pattern'] [LIMIT row_limit ]
```

## Parameters
<a name="r_SHOW_SCHEMAS-parameters"></a>

 *database\_name*   
The name of the database that contains the tables to list.   
To show tables in an AWS Glue Data Catalog, specify (`awsdatacatalog`) as the database name, and make sure the system configuration `data_catalog_auto_mount` is set to `true`. For more information, see [ALTER SYSTEM](r_ALTER_SYSTEM.md).

 *filter\_pattern*   
A valid UTF-8 character expression with a pattern to match schema names. The LIKE option performs a case-sensitive match that supports the following pattern-matching metacharacters:      
[See the AWS documentation website for more details](http://docs.aws.amazon.com/redshift/latest/dg/r_SHOW_SCHEMAS.html)
If *filter\_pattern* does not contain metacharacters, then the pattern only represents the string itself; in that case LIKE acts the same as the equals operator. 

 *row\_limit*   
The maximum number of rows to return. The *row\_limit* can be 0–10,000. 

## Examples
<a name="r_SHOW_SCHEMAS-examples"></a>

Following example shows the schemas from the Amazon Redshift database named `dev` .

```
SHOW SCHEMAS FROM DATABASE dev;

 database_name |     schema_name      | schema_owner | schema_type |         schema_acl          | source_database | schema_option 
---------------+----------------------+--------------+-------------+-----------------------------+-----------------+---------------
 dev           | pg_automv            |            1 | local       |                             |                 | 
 dev           | pg_catalog           |            1 | local       | jpuser=UC/jpuser~=U/jpuser  |                 | 
 dev           | public               |            1 | local       | jpuser=UC/jpuser~=UC/jpuser |                 | 
 dev           | information_schema   |            1 | local       | jpuser=UC/jpuser~=U/jpuser  |                 | 
 dev           | schemad79cd6d93bf043 |            1 | local       |                             |                 |
```

Following example shows the schemas in the AWS Glue Data Catalog database named `awsdatacatalog`. The maximum number of output rows is `5`.

```
SHOW SCHEMAS FROM DATABASE awsdatacatalog LIMIT 5;

 database_name  |     schema_name      | schema_owner | schema_type | schema_acl | source_database | schema_option 
----------------+----------------------+--------------+-------------+------------+-----------------+---------------
 awsdatacatalog | 000_too_many_glue_db |              | EXTERNAL    |            |                 | 
 awsdatacatalog | 123_default          |              | EXTERNAL    |            |                 | 
 awsdatacatalog | adhoc                |              | EXTERNAL    |            |                 | 
 awsdatacatalog | all_shapes_10mb      |              | EXTERNAL    |            |                 | 
 awsdatacatalog | all_shapes_1g        |              | EXTERNAL    |            |                 |
```