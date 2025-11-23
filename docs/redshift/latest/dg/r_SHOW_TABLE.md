Amazon Redshift will no longer support the creation of new Python UDFs starting November 1, 2025.
If you would like to use Python UDFs, create the UDFs prior to that date.
Existing Python UDFs will continue to function as normal. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# SHOW TABLE

Shows the definition of a table, including table attributes, table constraints, column
attributes, and column constraints. You can use the output of the SHOW TABLE statement to
recreate the table.

Collation information is shown for any CHAR, VARCHAR or SUPER column.

For more information on table creation, see [CREATE TABLE](r_CREATE_TABLE_NEW.md "r_CREATE_TABLE_NEW.md").

## Syntax

```
SHOW TABLE [*schema\_name*.]*table\_name*
```

## Parameters

_schema_name_

(Optional) The name of the related schema.

_table_name_

The name of the table to show.

## Examples

Following is an example of the SHOW TABLE output for the table
`sales`.

```
show table sales;
```

```
CREATE TABLE public.sales (
salesid integer NOT NULL ENCODE az64,
listid integer NOT NULL ENCODE az64 distkey,
sellerid integer NOT NULL ENCODE az64,
buyerid integer NOT NULL ENCODE az64,
eventid integer NOT NULL ENCODE az64,
dateid smallint NOT NULL,
qtysold smallint NOT NULL ENCODE az64,
pricepaid numeric(8,2) ENCODE az64,
commission numeric(8,2) ENCODE az64,
saletime timestamp without time zone ENCODE az64
)
DISTSTYLE KEY SORTKEY ( dateid );
```

Following is an example of the SHOW TABLE output for the table `category`
in the schema `public`. The collation of the database is CASE_SENSITIVE.

```
show table public.category;
```

```
CREATE TABLE public.category (
catid smallint NOT NULL distkey,
catgroup character varying(10) ENCODE lzo COLLATE case_sensitive,
catname character varying(10) ENCODE lzo COLLATE case_sensitive,
catdesc character varying(50) ENCODE lzo COLLATE case_sensitive
)
DISTSTYLE KEY SORTKEY ( catid );
```

The following example creates table `foo` with a primary key.

```
create table foo(a int PRIMARY KEY, b int);
```

The SHOW TABLE results display the create statement with all properties of the
`foo` table.

```
show table foo;
```

```
CREATE TABLE public.foo (
a integer NOT NULL ENCODE az64,
b integer ENCODE az64, PRIMARY KEY (a)
)
DISTSTYLE AUTO;
```

The following example creates table `collation` with explicit collation CASE_INSENSITIVE for column `a`.
The collation of the database is CASE_SENSITIVE.

```
CREATE TABLE public.collation (a CHAR COLLATE CASE_INSENSITIVE, b CHAR);
```

The SHOW TABLE results display the create statement with all properties of the
`collation` table.

```
show table public.collation;
```

```
CREATE TABLE public.collation (
a character(1) ENCODE lzo COLLATE case_insensitive,
b character(1) ENCODE lzo COLLATE case_sensitive
)
DISTSTYLE AUTO;
```
