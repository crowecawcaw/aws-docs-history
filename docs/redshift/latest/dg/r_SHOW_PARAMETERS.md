

 Amazon Redshift will no longer support the use of Python UDFs after June 30, 2026. We will start enforcing it in phases. For more information on the details of Python end of life and migration options, see the [ blog post ](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/) that was published on June 30, 2025. 

# SHOW PARAMETERS
<a name="r_SHOW_PARAMETERS"></a>

Shows a list of parameters for a function/procedure, along with some information about the parameters.

Each output row has columns database\_name, schema\_name, procedure\_name or function\_name, parameter\_name, ordinal\_position, parameter\_type (IN/OUT), data\_type, character\_maximum\_length, numeric\_precision, numeric\_scale, and remarks.

## Required permissions
<a name="r_SHOW_PARAMETERS-required-permissions"></a>

To view a function/procedure in a redshift schema, the current user must satisfy one of the following criteria:
+ Be a superuser
+ Be the owner of the function
+ Granted USAGE privilege on the parent schema and granted EXECUTE on the function

## Syntax
<a name="r_SHOW_PARAMETERS-synopsis"></a>

```
SHOW PARAMETERS OF {FUNCTION| PROCEDURE}
[database_name.]schema_name.function_name(argtype [, ...] )
[LIKE 'filter_pattern'];
```

## Parameters
<a name="r_SHOW_PARAMETERS-parameters"></a>

*database\_name*  
The name of the database that contains the function to list.

*schema\_name*  
The name of the schema that contains the function to list.

*filter\_pattern*  
A valid UTF-8 character expression with a pattern to match parameter names. The LIKE option performs a case-sensitive match that supports the following pattern-matching metacharacters:      
[See the AWS documentation website for more details](http://docs.aws.amazon.com/redshift/latest/dg/r_SHOW_PARAMETERS.html)

## Examples
<a name="r_SHOW_PARAMETERS-examples"></a>

The following example shows parameters of procedure demo\_db.demo\_schema.f1:

```
SHOW PARAMETERS OF PROCEDURE demo_db.demo_schema.f1(VARCHAR, DECIMAL, DECIMAL, DECIMAL);
 database_name | schema_name | procedure_name |  parameter_name  | ordinal_position | parameter_type |          data_type          | character_maximum_length | numeric_precision | numeric_scale 
---------------+-------------+----------------+------------------+------------------+----------------+-----------------------------+--------------------------+-------------------+---------------
 demo_db       | demo_schema | f1             | operation        |                1 | IN             | character varying           |                       10 |                   |              
 demo_db       | demo_schema | f1             | value1           |                2 | IN             | numeric                     |                          |                18 |             0
 demo_db       | demo_schema | f1             | value2           |                3 | IN             | numeric                     |                          |                18 |             0
 demo_db       | demo_schema | f1             | result           |                4 | INOUT          | numeric                     |                          |                18 |             0
 demo_db       | demo_schema | f1             | operation_status |                5 | OUT            | character varying           |                       50 |                   |              
 demo_db       | demo_schema | f1             | calculation_time |                6 | OUT            | timestamp without time zone |                          |                   |              
 demo_db       | demo_schema | f1             | is_successful    |                7 | OUT            | boolean                     |                          |                   |
```

The following example shows parameters of procedure demo\_schema.f1 with names starting with 'val':

```
SHOW PARAMETERS OF PROCEDURE demo_schema.f1(VARCHAR, DECIMAL, DECIMAL, DECIMAL) like 'val%';
 database_name | schema_name | procedure_name | parameter_name | ordinal_position | parameter_type | data_type | character_maximum_length | numeric_precision | numeric_scale 
---------------+-------------+----------------+----------------+------------------+----------------+-----------+--------------------------+-------------------+---------------
 demo_db       | demo_schema | f1             | value1         |                2 | IN             | numeric   |                          |                18 |             0
 demo_db       | demo_schema | f1             | value2         |                3 | IN             | numeric   |                          |                18 |             0
```

The following example shows parameters of function demo\_schema.f2:

```
SHOW PARAMETERS OF FUNCTION demo_schema.f2(INT, VARCHAR, DECIMAL, DATE, TIMESTAMP, BOOLEAN);
 database_name | schema_name | function_name | parameter_name  | ordinal_position | parameter_type |          data_type          | character_maximum_length | numeric_precision | numeric_scale 
---------------+-------------+---------------+-----------------+------------------+----------------+-----------------------------+--------------------------+-------------------+---------------
 demo_db       | demo_schema | f2            |                 |                0 | RETURN         | character varying           |                       -1 |                   |              
 demo_db       | demo_schema | f2            | int_param       |                1 | IN             | integer                     |                          |                32 |             0
 demo_db       | demo_schema | f2            | varchar_param   |                2 | IN             | character varying           |                       -1 |                   |              
 demo_db       | demo_schema | f2            | decimal_param   |                3 | IN             | numeric                     |                          |                   |              
 demo_db       | demo_schema | f2            | date_param      |                4 | IN             | date                        |                          |                   |              
 demo_db       | demo_schema | f2            | timestamp_param |                5 | IN             | timestamp without time zone |                          |                   |              
 demo_db       | demo_schema | f2            | boolean_param   |                6 | IN             | boolean                     |                          |                   |
```