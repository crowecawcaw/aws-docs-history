# PartiQL support in row filter expressions

You can construct row filter expressions using a subset of PartiQL data types, operators,
and aggregations.
Lake Formation does not allow any user defined or standard partiQL functions in the filter expression. You can use comparison operators to compare columns with
constants (for example, `views >= 10000`), but you can't compare columns with other
columns.

A Row filter expression may be a simple expression or a composite expression. Total length of the expression must be less than 2048 characters.

###### Simple expression

A simple expression will be of the format: `<column name > <comparison operator ><value >`

- **Column name**

It can either a top level data column, a partition column, or a nested column present
in the table schema and must belong to the [Supported data types](#row-filter-supported-datatypes "#row-filter-supported-datatypes") listed below.

- **Comparison operator**

The following are the supported operators: `=, >, <, >=, <=, <>,!=,
 BETWEEN, IN, LIKE, NOT, IS [NOT] NULL`

- All string comparisons and `LIKE` pattern matches are case-sensitive.
  You can't use IS [NOT] NULL operator on partition columns.
- **Column value**

The Column value must match the data type of the column name.

###### Composite expression

A composite expression will be of the format: `( <simple expression >) <AND/OR >(<simple expression >)`. Composite expressions can be further combined using logical operators `AND/OR`.

## Supported data types

Row filters that refer to an AWS Glue Data Catalog table that contains an unsupported data
types will result in an error. The following are the supported data types for table
columns and constants, which are mapped to Amazon Redshift data types:

- `STRING, CHAR, VARCHAR`
- `INT, LONG, BIGINT, FLOAT, DECIMAL, DOUBLE`
- `BOOLEAN`
- `STRUCT`

For more information about data types in Amazon Redshift, see [Data types](../../../redshift/latest/dg/c_Supported_data_types.md "../../../redshift/latest/dg/c_Supported_data_types.md") in _Amazon Redshift
Database Developer Guide_.

## Row filter expressions

###### Example

The following are examples of valid row filter expressions for a table with columns:
`country (String), id (Long), year (partition column of type Integer), month
 (partition column of type Integer)`

- `year > 2010 and country != 'US'`
- `(year > 2010 and country = 'US') or (month < 8 and id > 23)`
- `(country between 'Z' and 'U') and (year = 2018)`
- `(country like '%ited%') and (year > 2000)`

###### Example

The following is a valid examples of row filter expressions for a table with nested columns:
`year > 2010 and customer.customerId <> 1`

Nested fields under partition columns should not be referenced when defining nested row-level expressions.

String constants must be enclosed in single-quotes.

## Reserved keywords

If your row filter expression contains PartiQL keywords, you will receive a parsing error
as column names may conflict with the keywords. When this happens, escape the column names
by using double quotes. Some examples of reserved keywords are “first”, “last”, “asc”,
“missing”. See PartiQL specification for a list of reserved keywords.

## PartiQL reference

For more information about PartiQL, see [https://partiql.org/](https://partiql.org/ "https://partiql.org/").
