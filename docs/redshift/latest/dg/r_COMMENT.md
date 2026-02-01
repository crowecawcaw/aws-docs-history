Amazon Redshift will no longer support the creation of new Python UDFs starting Patch 198.
Existing Python UDFs will continue to function until June 30, 2026. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# COMMENT

Creates or changes a comment about a database object.

## Syntax

```
COMMENT ON
{
TABLE *object\_name* |
COLUMN *object\_name*.*column\_name* |
CONSTRAINT *constraint\_name* ON *table\_name* |
DATABASE *object\_name* |
VIEW *object\_name*
}
IS '*text*' | NULL
```

## Parameters

_object_name_

Name of the database object being commented on. You can add a comment to the
following objects:

- TABLE
- COLUMN (also takes a _column_name_).
- CONSTRAINT (also takes a _constraint_name_ and
  _table_name_).
- DATABASE
- VIEW
- SCHEMA

IS '_text_' | NULL

The comment text that you want to add or replace for the specified object.
The _text_ string is data type TEXT. Enclose the comment in
single quotation marks. Set the value to NULL to remove the comment
text.

_column_name_

Name of the column being commented on. Parameter of COLUMN. Follows a table
specified in `object_name`.

_constraint_name_

Name of the constraint that is being commented on. Parameter of
CONSTRAINT.

_table_name_

Name of a table containing the constraint. Parameter of CONSTRAINT.

## Usage notes

You must be a superuser or the owner of a database object to add or update a
comment.

Comments on databases may only be applied to the current database. A warning message
is displayed if you attempt to comment on a different database. The same warning is
displayed for comments on databases that don't exist.

Comments on external tables, external columns, and columns of late binding views are
not supported.

## Examples

The following example adds a comment to the SALES table.

```
COMMENT ON TABLE sales IS 'This table stores tickets sales data';
```

The following example displays the comment on the SALES table.

```
select obj_description('public.sales'::regclass);

obj_description
-------------------------------------
This table stores tickets sales data

```

The following example removes a comment from the SALES table.

```
COMMENT ON TABLE sales IS NULL;
```

The following example adds a comment to the EVENTID column of the SALES table.

```
COMMENT ON COLUMN sales.eventid IS 'Foreign-key reference to the EVENT table.';
```

The following example displays a comment on the EVENTID column (column number 5) of
the SALES table.

```
select col_description( 'public.sales'::regclass, 5::integer );

col_description
-----------------------------------------
Foreign-key reference to the EVENT table.

```

The following example adds a descriptive comment to the EVENT table.

```
comment on table event is 'Contains listings of individual events.';
```

To view comments, query the PG_DESCRIPTION system catalog. The following example
returns the description for the EVENT table.

```
select * from pg_catalog.pg_description
where objoid =
(select oid from pg_class where relname = 'event'
and relnamespace =
(select oid from pg_catalog.pg_namespace where nspname = 'public') );

objoid | classoid | objsubid | description
-------+----------+----------+----------------------------------------
116658 |     1259 |        0 | Contains listings of individual events.
```
