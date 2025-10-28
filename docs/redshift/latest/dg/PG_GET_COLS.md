Amazon Redshift will no longer support the creation of new Python UDFs starting November 1, 2025.
If you would like to use Python UDFs, create the UDFs prior to that date.
Existing Python UDFs will continue to function as normal. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# PG_GET_COLS

Returns the column metadata for a table or view definition.

## Syntax

```
pg_get_cols('*name*')
```

## Arguments

_name_

The name of an Amazon Redshift table or view. For more information, see
[Names and identifiers](r_names.md "r_names.md").

## Return type

VARCHAR

## Usage notes

The PG_GET_COLS function returns one row for each column in the table or view
definition. The row contains a comma-separated list with the schema name, relation
name, column name, data type, and column number.
The formatting of the result of the SQL depends on the SQL client used.

## Examples

The following examples return results for a view named `SALES_VW` in schema `public` and table table named `sales` in schema `mytickit1`
that are created by the user in the connected database `dev`.

The following example returns the column metadata for a view named `SALES_VW`.

```
`select pg_get_cols('sales_vw');`
`pg_get_cols
-----------------------------------------------------------
(public,sales_vw,salesid,integer,1)
(public,sales_vw,listid,integer,2)
(public,sales_vw,sellerid,integer,3)
(public,sales_vw,buyerid,integer,4)
(public,sales_vw,eventid,integer,5)
(public,sales_vw,dateid,smallint,6)
(public,sales_vw,qtysold,smallint,7)
(public,sales_vw,pricepaid,"numeric(8,2)",8)
(public,sales_vw,commission,"numeric(8,2)",9)
(public,sales_vw,saletime,"timestamp without time zone",10)`
```

The following example returns the column metadata for the `SALES_VW` view in table format.

```
`select * from pg_get_cols('sales_vw')
cols(view_schema name, view_name name, col_name name, col_type varchar, col_num int);`
`view_schema | view_name | col_name | col_type | col_num
------------+-----------+------------+-----------------------------+--------
public | sales_vw | salesid | integer | 1
public | sales_vw | listid | integer | 2
public | sales_vw | sellerid | integer | 3
public | sales_vw | buyerid | integer | 4
public | sales_vw | eventid | integer | 5
public | sales_vw | dateid | smallint | 6
public | sales_vw | qtysold | smallint | 7
public | sales_vw | pricepaid | numeric(8,2) | 8
public | sales_vw | commission | numeric(8,2) | 9
public | sales_vw | saletime | timestamp without time zone | 10`
```

The following example returns the column metadata for the `SALES` table in schema `mytickit1`in table format.

```
`select * from pg_get_cols('"mytickit1"."sales"')
cols(view_schema name, view_name name, col_name name, col_type varchar, col_num int);`
`view_schema | view_name | col_name | col_type | col_num
------------+-----------+------------+-----------------------------+--------
mytickit1 | sales | salesid | integer | 1
mytickit1 | sales | listid | integer | 2
mytickit1 | sales | sellerid | integer | 3
mytickit1 | sales | buyerid | integer | 4
mytickit1 | sales | eventid | integer | 5
mytickit1 | sales | dateid | smallint | 6
mytickit1 | sales | qtysold | smallint | 7
mytickit1 | sales | pricepaid | numeric(8,2) | 8
mytickit1 | sales | commission | numeric(8,2) | 9
mytickit1 | sales | saletime | timestamp without time zone | 10`
```
