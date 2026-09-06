

 Amazon Redshift will no longer support the use of Python UDFs after June 30, 2026. We will start enforcing it in phases. For more information on the details of Python end of life and migration options, see the [ blog post ](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/) that was published on June 30, 2025. 

# SHOW FUNCTIONS
<a name="r_SHOW_FUNCTIONS"></a>

Shows a list of functions in a schema, along with information about the listed objects.

Each output row has columns database\_name, schema\_name, function\_name, number\_of\_arguments, argument\_list, return\_type, remarks.

If more than 10,000 rows would results from SHOW FUNCTIONS, then the command raises an error.

## Required permissions
<a name="r_SHOW_FUNCTIONS-required-permissions"></a>

To view a function in a Redshift schema, the current user must satisfy one of the following criteria:
+ Be a superuser
+ Be the owner of the function
+ Granted USAGE privilege on the parent schema and granted EXECUTE on the function

## Syntax
<a name="r_SHOW_FUNCTIONS-synopsis"></a>

```
SHOW FUNCTIONS FROM SCHEMA
[database_name.]schema_name
[LIKE 'filter_pattern'] [LIMIT row_limit]
```

## Parameters
<a name="r_SHOW_FUNCTIONS-parameters"></a>

*database\_name*  
The name of the database that contains the functions to list.

*schema\_name*  
The name of the schema that contains the functions to list.

*filter\_pattern*  
A valid UTF-8 character expression with a pattern to match function names. The LIKE option performs a case-sensitive match that supports the following pattern-matching metacharacters:      
[See the AWS documentation website for more details](http://docs.aws.amazon.com/redshift/latest/dg/r_SHOW_FUNCTIONS.html)
Note that the filter\_pattern only matches the function name.

*row\_limit*  
The maximum number of rows to return. The *row\_limit* can be 0–10,000.

## Examples
<a name="r_SHOW_FUNCTIONS-examples"></a>

The following example shows functions from schema demo\_db.demo\_schema:

```
SHOW FUNCTIONS FROM SCHEMA demo_db.demo_schema;
 database_name | schema_name |    function_name     | number_of_arguments |                                  argument_list                                  |    return_type    | remarks 
---------------+-------------+----------------------+---------------------+---------------------------------------------------------------------------------+-------------------+---------
 demo_db       | demo_schema | f2                   |                   6 | integer, character varying, numeric, date, timestamp without time zone, boolean | character varying | 
 demo_db       | demo_schema | f_calculate_discount |                   2 | numeric, integer                                                                | numeric           | 
 demo_db       | demo_schema | f_days_between       |                   2 | date, date                                                                      | integer           |
```

The following example shows functions from schema demo\_schema with names ending in 'discount':

```
SHOW FUNCTIONS FROM SCHEMA demo_schema like '%discount';
 database_name | schema_name |    function_name     | number_of_arguments |  argument_list   | return_type | remarks 
---------------+-------------+----------------------+---------------------+------------------+-------------+---------
 demo_db       | demo_schema | f_calculate_discount |                   2 | numeric, integer | numeric     |
```