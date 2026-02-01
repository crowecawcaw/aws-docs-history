Amazon Redshift will no longer support the creation of new Python UDFs starting Patch 198.
Existing Python UDFs will continue to function until June 30, 2026. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# FROM clause

The FROM clause in a query lists the table references (tables, views, and subqueries)
that data is selected from. If multiple table references are listed, the tables must be
joined, using appropriate syntax in either the FROM clause or the WHERE clause. If no
join criteria are specified, the system processes the query as a cross-join (Cartesian
product).

###### Topics

- [Syntax](#r_FROM_clause30-synopsis "#r_FROM_clause30-synopsis")
- [Parameters](#r_FROM_clause30-parameters "#r_FROM_clause30-parameters")
- [Usage notes](#r_FROM_clause_usage_notes "#r_FROM_clause_usage_notes")
- [PIVOT and UNPIVOT examples](r_FROM_clause-pivot-unpivot-examples.md "r_FROM_clause-pivot-unpivot-examples.md")
- [JOIN examples](r_Join_examples.md "r_Join_examples.md")
- [UNNEST examples](r_FROM_clause-unnest-examples.md "r_FROM_clause-unnest-examples.md")

## Syntax

```
FROM *table\_reference* [, ...]
```

where _table_reference_ is one of the following:

```
*with\_subquery\_table\_name* [ *table\_alias* ]
*table\_name* [ * ] [ *table\_alias* ]
( *subquery* ) [ *table\_alias* ]
*table\_reference* [ NATURAL ] *join\_type table\_reference*
   [ ON *join\_condition* | USING ( *join\_column* [, ...] ) ]
*table\_reference*  *join\_type* *super\_expression*
   [ ON *join\_condition* ]
*table\_reference* PIVOT (
   *aggregate(expr)* [ [ AS ] *aggregate\_alias* ]
   FOR *column\_name* IN ( *expression* [ AS ] *in\_alias* [, ...] )
) [ *table\_alias* ]
*table\_reference* UNPIVOT [ INCLUDE NULLS | EXCLUDE NULLS ] (
   *value\_column\_name*
   FOR *name\_column\_name* IN ( *column\_reference* [ [ AS ]
   *in\_alias* ] [, ...] )
) [ *table\_alias* ]
UNPIVOT *expression* AS *value\_alias* [ AT *attribute\_alias* ]
( *super\_expression*.*attribute\_name* ) AS *value\_alias* [ AT *index\_alias* ]
UNNEST ( *column\_reference* )
  [AS] *table\_alias* ( *unnested\_column\_name* )
UNNEST ( *column\_reference* ) WITH OFFSET
  [AS] *table\_alias* ( *unnested\_column\_name*, [*offset\_column\_name*] )
```

The optional _table_alias_ can be used to give temporary names to tables and complex table references and, if desired, their columns as well, like the following:

```
[ AS ] *alias* [ ( column_alias [, ...] ) ]
```

## Parameters

_with_subquery_table_name_

A table defined by a subquery in the [WITH clause](r_WITH_clause.md "r_WITH_clause.md").

_table_name_

Name of a table or view.

_alias_

Temporary alternative name for a table or view. An alias must be supplied
for a table derived from a subquery. In other table references, aliases are
optional. The AS keyword is always optional. Table aliases provide a
convenient shortcut for identifying tables in other parts of a query, such
as the WHERE clause. For example:

```
select * from sales s, listing l
where s.listid=l.listid
```

_column_alias_

Temporary alternative name for a column in a table or view.

_subquery_

A query expression that evaluates to a table. The table exists only for
the duration of the query and is typically given a name or
_alias_. However, an alias isn't required. You
can also define column names for tables that derive from subqueries. Naming
column aliases is important when you want to join the results of subqueries
to other tables and when you want to select or constrain those columns
elsewhere in the query.

A subquery may contain an ORDER BY clause, but this clause may have no
effect if a LIMIT or OFFSET clause isn't also specified.

NATURAL

Defines a join that automatically uses all pairs of identically named
columns in the two tables as the joining columns. No explicit join condition
is required. For example, if the CATEGORY and EVENT tables both have columns
named CATID, a natural join of those tables is a join over their CATID
columns.

###### Note

If a NATURAL join is specified but no identically named pairs of
columns exist in the tables to be joined, the query defaults to a
cross-join.

_join_type_

Specify one of the following types of join:

- [INNER] JOIN
- LEFT [OUTER] JOIN
- RIGHT [OUTER] JOIN
- FULL [OUTER] JOIN
- CROSS JOIN

Cross-joins are unqualified joins; they return the Cartesian product of the two
tables.

Inner and outer joins are qualified joins. They are qualified either implicitly
(in natural joins); with the ON or USING syntax in the FROM clause; or with a WHERE
clause condition.

An inner join returns matching rows only, based on the join condition or list of
joining columns. An outer join returns all of the rows that the equivalent inner join
would return plus non-matching rows from the "left" table, "right" table, or both
tables. The left table is the first-listed table, and the right table is the
second-listed table. The non-matching rows contain NULL values to fill the gaps in
the output columns.

ON _join_condition_

Type of join specification where the joining columns are stated as a
condition that follows the ON keyword. For example:

```
sales join listing
on sales.listid=listing.listid and sales.eventid=listing.eventid
```

USING ( _join_column_ [, ...] )

Type of join specification where the joining columns are listed in
parentheses. If multiple joining columns are specified, they are delimited
by commas. The USING keyword must precede the list. For example:

```
sales join listing
using (listid,eventid)
```

PIVOT

Rotates output from rows to columns, for the purpose of representing tabular data
in a format that is easy to read. Output is represented horizontally across
multiple columns. PIVOT is similar to a GROUP BY query with an aggregation, using an
aggregate expression to specify an output format. However,
in contrast to GROUP BY, the results are returned in columns instead of rows.

For examples that show how to query with PIVOT and UNPIVOT,
see [PIVOT and UNPIVOT examples](r_FROM_clause-pivot-unpivot-examples.md "r_FROM_clause-pivot-unpivot-examples.md").

UNPIVOT

_Rotating columns into rows with UNPIVOT_ – The operator transforms result columns, from an input table or query
results, into rows, to make the output easier to read. UNPIVOT combines
the data of its input columns into two result columns: a name column and a
value column. The name column contains column names from the
input, as row entries. The value column contains values from the input columns, such
as results of an aggregation. For example, the counts of items in various categories.

_Object unpivoting with UNPIVOT (SUPER)_ – You can perform object unpivoting, where _expression_ is a SUPER expression referring to another FROM clause item. For
more information, see [Object unpivoting](query-super.md#unpivoting "query-super.md#unpivoting"). It also has examples that show how to query semi-structured data, such as data that's JSON-formatted.

_super_expression_

A valid SUPER expression. Amazon Redshift returns one row for each
value in the specified attribute. For more
information on the SUPER data type, see [SUPER type](r_SUPER_type.md "r_SUPER_type.md").
For more information about unnested SUPER values, see
[Unnesting queries](query-super.md#unnest "query-super.md#unnest").

_attribute_name_

The name of an attribute in the SUPER expression.

_index_alias_

Alias for the index that signifies the value's
position in the SUPER expression.

UNNEST

Expands a nested structure, typically a SUPER array, into columns containing the unnested elements. For more information on unnesting
SUPER data, see [Querying semi-structured data](query-super.md "query-super.md").
For examples, see [UNNEST examples](r_FROM_clause-unnest-examples.md "r_FROM_clause-unnest-examples.md").

_unnested_column_name_

The name of the column that contains the unnested elements.

UNNEST ... WITH OFFSET

Adds an offset column to the unnested output,
with the offset representing the zero-based index of each
element in the array. This variant is useful when you want
to see the position of elements within an array.
For more information on unnesting
SUPER data, see [Querying semi-structured data](query-super.md "query-super.md").
For examples, see [UNNEST examples](r_FROM_clause-unnest-examples.md "r_FROM_clause-unnest-examples.md").

_offset_column_name_

A custom name for the offset column that lets you
explicitly define how the index column will appear
in the output. This parameter is optional.
By default, the offset column name is `offset_col`.

## Usage notes

Joining columns must have comparable data types.

A NATURAL or USING join retains only one of each pair of joining columns in the
intermediate result set.

A join with the ON syntax retains both joining columns in its intermediate result
set.

See also [WITH clause](r_WITH_clause.md "r_WITH_clause.md").
