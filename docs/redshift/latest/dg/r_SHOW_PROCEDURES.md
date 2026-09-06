

 Amazon Redshift will no longer support the use of Python UDFs after June 30, 2026. We will start enforcing it in phases. For more information on the details of Python end of life and migration options, see the [ blog post ](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/) that was published on June 30, 2025. 

# SHOW PROCEDURES
<a name="r_SHOW_PROCEDURES"></a>

Shows a list of procedures in a schema, along with information about the listed objects.

Each output row has columns `database_name`, `schema_name`, `procedure_name`, `number_of_arguments`, `argument_list`, `return_type`, remarks.

If more than 10,000 rows would results from SHOW PROCEDURES, then the command raises an error.

## Required permissions
<a name="r_SHOW_PROCEDURES-required-permissions"></a>

To view a procedure in a Redshift schema, the current user must satisfy one of the following criteria:
+ Be a superuser
+ Be the owner of the procedure
+ Granted USAGE privilege on the parent schema and granted EXECUTE on the procedure

## Syntax
<a name="r_SHOW_PROCEDURES-synopsis"></a>

```
SHOW PROCEDURES FROM SCHEMA
[database_name.]schema_name
[LIKE 'filter_pattern'] [LIMIT row_limit]
```

## Parameters
<a name="r_SHOW_PROCEDURES-parameters"></a>

database\_name  
The name of the database that contains the procedures to list.

schema\_name  
The name of the schema that contains the procedures to list.

filter\_pattern  
A valid UTF-8 character expression with a pattern to match procedure names. The LIKE option performs a case-sensitive match that supports the following pattern-matching metacharacters:      
[See the AWS documentation website for more details](http://docs.aws.amazon.com/redshift/latest/dg/r_SHOW_PROCEDURES.html)
Note that the filter\_pattern only matches the procedure name.

row\_limit  
The maximum number of rows to return. The *row\_limit* can be 0–10,000.

## Examples
<a name="r_SHOW_PROCEDURES-examples"></a>

The following example shows procedures from schema demo\_db.demo\_schema:

```
SHOW PROCEDURES FROM SCHEMA demo_db.demo_schema;
 database_name | schema_name |  procedure_name   | number_of_arguments |                argument_list                 |                           return_type                            | remarks 
---------------+-------------+-------------------+---------------------+----------------------------------------------+------------------------------------------------------------------+---------
 demo_db       | demo_schema | f1                |                   4 | character varying, numeric, numeric, numeric | numeric, character varying, timestamp without time zone, boolean | 
 demo_db       | demo_schema | sp_get_result_set |                   2 | integer, refcursor                           | refcursor                                                        | 
 demo_db       | demo_schema | sp_process_data   |                   2 | numeric, numeric                             | numeric, character varying                                       |
```

The following example shows procedures from schema demo\_schema with names ending in 'data':

```
SHOW PROCEDURES FROM SCHEMA demo_schema like '%data';
 database_name | schema_name | procedure_name  | number_of_arguments |  argument_list   |        return_type         | remarks 
---------------+-------------+-----------------+---------------------+------------------+----------------------------+---------
 demo_db       | demo_schema | sp_process_data |                   2 | numeric, numeric | numeric, character varying |
```