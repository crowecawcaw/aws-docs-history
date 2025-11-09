Amazon Redshift will no longer support the creation of new Python UDFs starting November 1, 2025.
If you would like to use Python UDFs, create the UDFs prior to that date.
Existing Python UDFs will continue to function as normal. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# Names and identifiers

Names identify database objects, including tables and columns, as well as users
and passwords. The terms _name_ and
_identifier_ can be used interchangeably. There are two types
of identifiers, standard identifiers and quoted or delimited identifiers. Identifiers
must consist of only UTF-8 printable characters. ASCII letters in standard and
delimited identifiers are case-insensitive and are folded to lowercase in the
database. In query results, column names are returned as lowercase by default. To
return column names in uppercase, set the [describe_field_name_in_uppercase](r_describe_field_name_in_uppercase.md "r_describe_field_name_in_uppercase.md") configuration parameter to
`true`.

## Standard identifiers

Standard SQL identifiers adhere to a set of rules and must:

- Begin with an ASCII single-byte alphabetic character or underscore
  character, or a UTF-8 multibyte character two to four bytes long.
- Subsequent characters can be ASCII single-byte alphanumeric characters,
  underscores, or dollar signs, or UTF-8 multibyte characters two to four
  bytes long.
- Be between 1 and 127 bytes in length, not including quotation marks for
  delimited identifiers.
- Contain no quotation marks and no spaces.
- Not be a reserved SQL key word.

## Delimited identifiers

Delimited identifiers (also known as quoted identifiers) begin and end with
double quotation marks ("). If you use a delimited identifier, you must use the
double quotation marks for every reference to that object. The identifier can
contain any standard UTF-8 printable characters other than the double quotation
mark itself. Therefore, you can create column or table names that include
otherwise illegal characters, such as spaces or the percent symbol.

ASCII letters in delimited identifiers are case-insensitive and are folded to
lowercase. To use a double quotation mark in a string, you must precede it with
another double quotation mark character.

## Case-sensitive

identifiers

Case-sensitive identifiers (also known as mixed-case identifiers) can contain
both uppercase and lowercase letters. To use case-sensitive identifiers, you can
set the configuration `enable_case_sensitive_identifier` to
`true`. You can set this configuration for the cluster or for a
session. For more information, see [Default parameter
values](../mgmt/default-param-group-values.md "../mgmt/default-param-group-values.md") in the _Amazon Redshift Management Guide_ and [enable_case_sensitive_identifier](r_enable_case_sensitive_identifier.md "r_enable_case_sensitive_identifier.md").

## System column names

The following PostgreSQL system column names can't be used as column names in
user-defined columns. For more information, see [https://www.postgresql.org/docs/8.0/static/ddl-system-columns.html](https://www.postgresql.org/docs/8.0/static/ddl-system-columns.html "https://www.postgresql.org/docs/8.0/static/ddl-system-columns.html").

- `oid`
- `tableoid`
- `xmin`
- `cmin`
- `xmax`
- `cmax`
- `ctid`

## Examples

This table shows examples of delimited identifiers, the resulting output, and a
discussion:

| Syntax           | Result       | Discussion                                                                                                                                                                   |
| ---------------- | ------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| "group"          | group        | GROUP is a reserved word, so usage of it within an<br>identifier requires double quotation marks.                                                                            |
| """WHERE"""      | "where"      | WHERE is also a reserved word. To include quotation<br>marks in the string, escape each double quotation mark character with<br>additional double quotation mark characters. |
| "This name"      | this name    | Double quotation marks are required to preserve the<br>space.                                                                                                                |
| "This ""IS IT""" | this "is it" | The quotation marks surrounding IS IT must each be<br>preceded by an extra quotation mark in order to become part of the<br>name.                                            |

To create a table named group with a column named this "is it":

```
create table "group" (
"This ""IS IT""" char(10));
```

The following queries return the same result:

```
select "This ""IS IT"""
from "group";

this "is it"
--------------
(0 rows)

```

```
select "this ""is it"""
from "group";

this "is it"
--------------
(0 rows)
```

The following fully qualified `table.column` syntax also returns the
same result:

```
select "group"."this ""is it"""
from "group";

this "is it"
--------------
(0 rows)
```

The following CREATE TABLE command creates a table with a slash in a column
name:

```
create table if not exists city_slash_id(
                  "city/id" integer not null,
                  state char(2) not null);

```
