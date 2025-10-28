Amazon Redshift will no longer support the creation of new Python UDFs starting November 1, 2025.
If you would like to use Python UDFs, create the UDFs prior to that date.
Existing Python UDFs will continue to function as normal. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# CREATE VIEW

Creates a view in a database. The view isn't physically materialized; the query
that defines the view is run every time the view is referenced in a query. To create a view
with an external table, include the WITH NO SCHEMA BINDING clause.

To create a standard view, you need access to the underlying tables, or to underlying
views. To query a standard view, you need select permissions for the view itself, but you
don't need select permissions for the underlying tables. In a case where you create a
view that references a table or view in another schema, or if you create a view that
references a materialized view, you need usage
permissions. To query a late binding view, you need select permissions for the late binding
view itself. You should also make sure the owner of the late binding view has select
permissions for the referenced objects (tables, views, or user-defined functions). For more
information about late-binding views, see [Usage notes](#r_CREATE_VIEW_usage_notes "#r_CREATE_VIEW_usage_notes").

## Required permissions

To use CREATE VIEW, one of the following permissions is required.

- To create a view using CREATE [ OR REPLACE ] VIEW:
  - Superuser
  - Users with the CREATE [ REPLACE ] VIEW permission

- To replace an existing view using CREATE OR REPLACE VIEW:
  - Superuser
  - Users with the CREATE [ OR REPLACE ] VIEW permission
  - View owner

If a user wants to access a view that incorporates a user-defined function, the user
must have the EXECUTE permission on that function.

## Syntax

```
CREATE [ OR REPLACE ] VIEW *name* [ ( *column\_name* [, ...] ) ] AS *query*
[ WITH NO SCHEMA BINDING ]
```

## Parameters

OR REPLACE

If a view of the same name already exists, the view is replaced. You can
only replace a view with a new query that generates the identical set of
columns, using the same column names and data types. CREATE OR REPLACE VIEW
locks the view for reads and writes until the operation completes.

When a view is replaced, its other properties such as ownership and granted
privileges are preserved.

_name_

The name of the view. If a schema name is given (such as
`myschema.myview`) the view is created using the specified
schema. Otherwise, the view is created in the current schema. The view name
must be different from the name of any other view or table in the same schema.

If you specify a view name that begins with '# ', the view is created as a
temporary view that is visible only in the current session.

For more information about valid names, see [Names and identifiers](r_names.md "r_names.md"). You can't create tables or views in the
system databases template0, template1, padb_harvest, or sys:internal.

_column_name_

Optional list of names to be used for the columns in the view. If no column
names are given, the column names are derived from the query. The maximum
number of columns you can define in a single view is 1,600.

_query_

A query (in the form of a SELECT statement) that evaluates to a table. This
table defines the columns and rows in the view.

WITH NO SCHEMA BINDING

Clause that specifies that the view isn't bound to the underlying
database objects, such as tables and user-defined functions. As a result, there
is no dependency between the view and the objects it references. You can create
a view even if the referenced objects don't exist. Because there is no
dependency, you can drop or alter a referenced object without affecting the
view. Amazon Redshift doesn't check for dependencies until the view is queried.
Recursive common table expressions (rCTE) are not supported with late-binding
views. To view details about late-binding views, run the [PG_GET_LATE_BINDING_VIEW_COLS](PG_GET_LATE_BINDING_VIEW_COLS.md "PG_GET_LATE_BINDING_VIEW_COLS.md") function.

When you include the WITH NO SCHEMA BINDING clause, tables and views
referenced in the SELECT statement must be qualified with a schema name. The
schema must exist when the view is created, even if the referenced table
doesn't exist. For example, the following statement returns an error.

```
create view myevent as select eventname from event
with no schema binding;
```

The following statement runs successfully.

```
create view myevent as select eventname from public.event
with no schema binding;
```

###### Note

You can't update, insert into, or delete from a view.

## Usage notes

### Late-binding views

A late-binding view doesn't check the underlying database objects, such as
tables and other views, until the view is queried. As a result, you can alter or drop
the underlying objects without dropping and recreating the view. If you drop
underlying objects, queries to the late-binding view will fail. If the query to the
late-binding view references columns in the underlying object that aren't
present, the query will fail.

If you drop and then re-create a late-binding view's underlying table or
view, the new object is created with default access permissions. You might need to
grant permissions to the underlying objects for users who will query the view.

To create a late-binding view, include the WITH NO SCHEMA BINDING clause. The
following example creates a view with no schema binding.

```
create view event_vw as select * from public.event
with no schema binding;
```

```
`select * from event_vw limit 1;`

eventid | venueid | catid | dateid | eventname     | starttime
--------+---------+-------+--------+---------------+--------------------
      2 |     306 |     8 |   2114 | Boris Godunov | 2008-10-15 20:00:00
```

The following example shows that you can alter an underlying table without
recreating the view.

```
alter table event rename column eventname to title;
```

```
`select * from event_vw limit 1;`

eventid | venueid | catid | dateid | title         | starttime
--------+---------+-------+--------+---------------+--------------------
      2 |     306 |     8 |   2114 | Boris Godunov | 2008-10-15 20:00:00
```

You can reference Amazon Redshift Spectrum external tables only in a late-binding view. One
application of late-binding views is to query both Amazon Redshift and Redshift Spectrum tables. For
example, you can use the [UNLOAD](r_UNLOAD.md "r_UNLOAD.md") command
to archive older data to Amazon S3. Then, create a Redshift Spectrum external table that references
the data on Amazon S3 and create a view that queries both tables. The following example
uses a UNION ALL clause to join the Amazon Redshift `SALES` table and the Redshift Spectrum
`SPECTRUM.SALES` table.

```
create view sales_vw as
select * from public.sales
union all
select * from spectrum.sales
with no schema binding;
```

For more information about creating Redshift Spectrum external tables, including the
`SPECTRUM.SALES` table, see [Getting started with Amazon Redshift
Spectrum](c-getting-started-using-spectrum.md "c-getting-started-using-spectrum.md").

###### Important

When you create a standard view from a late-binding view, the standard view’s
definition contains the definition of the late-binding view at the time the
standard view was made, including the owner of the late-binding view. If you make
a change in the underlying late-binding view, those changes will not be used in
the standard view until you re-create the standard view. Therefore, when the
standard view is queried, it will always use the late-binding view's definition
and the late-binding view's owner for permission checking at the time of that
standard view creation.

To update the standard view to refer to the latest definition of the late-binding
view, run CREATE OR REPLACE VIEW with the initial view definition you used to create
the standard view.

See the following example of creating a standard view from a late-binding
view.

```
create view sales_vw_lbv as
select * from public.sales
with no schema binding;

show view sales_vw_lbv;
                            Show View DDL statement
--------------------------------------------------------------------------------
 create view sales_vw_lbv as select * from public.sales with no schema binding;
(1 row)

create view sales_vw as
select * from sales_vw_lbv;

show view sales_vw;
                                               Show View DDL statement
---------------------------------------------------------------------------------------------------------------------
 SELECT sales_vw_lbv.price, sales_vw_lbv."region" FROM (SELECT sales.price, sales."region" FROM sales) sales_vw_lbv;
(1 row)
```

Note that the late-binding view as shown in the DDL statement for the standard
view is defined when the standard view is created, and won’t update with any changes
you make to the late-binding view afterward.

## Examples

The example commands use a sample set of objects and data called the
_TICKIT_ database. For more information, see [Sample database](c_sampledb.md "c_sampledb.md").

The following command creates a view called _myevent_ from a table
called EVENT.

```
create view myevent as select eventname from event
where eventname = 'LeAnn Rimes';
```

The following command creates a view called _myuser_ from a table
called USERS.

```
create view myuser as select lastname from users;
```

The following command creates or replaces a view called _myuser_
from a table called USERS.

```
create or replace view myuser as select lastname from users;
```

The following example creates a view with no schema binding.

```
create view myevent as select eventname from public.event
with no schema binding;
```
