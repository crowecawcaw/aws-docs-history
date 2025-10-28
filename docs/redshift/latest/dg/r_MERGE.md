Amazon Redshift will no longer support the creation of new Python UDFs starting November 1, 2025.
If you would like to use Python UDFs, create the UDFs prior to that date.
Existing Python UDFs will continue to function as normal. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# MERGE

Conditionally merges rows from a source table into a target table. Traditionally, this
can only be achieved by using multiple insert, update or delete statements separately. For
more information on the operations that MERGE lets you combine, see [UPDATE](r_UPDATE.md "r_UPDATE.md"), [DELETE](r_DELETE.md "r_DELETE.md"), and [INSERT](r_INSERT_30.md "r_INSERT_30.md").

## Syntax

```
MERGE INTO *target\_table*
USING *source\_table* [ [ AS ] *alias* ]
ON *match\_condition*
[ WHEN MATCHED THEN { UPDATE SET *col\_name* = { *expr* } [,...] | DELETE }
WHEN NOT MATCHED THEN INSERT [ ( *col\_name* [,...] ) ] VALUES ( { *expr* } [, ...] ) |
REMOVE DUPLICATES ]
```

## Parameters

_target_table_

The temporary or permanent table that the MERGE statement merges
into.

_source_table_

The temporary or permanent table supplying the rows to merge into
_target_table_. _source_table_ can
also be a Spectrum table.

_alias_

The temporary alternative name for _source_table_.

This parameter is optional. Preceding _alias_ with AS is
also optional.

_match_condition_

Specifies equal predicates between the source table column and target table
column that are used to determine whether the rows in
_source_table_ can be matched with rows in
_target_table_. If the condition is met, MERGE runs
_matched_clause_ for that row. Otherwise MERGE runs
_not_matched_clause_ for that row.

WHEN MATCHED

Specifies the action to be run when the match condition between a source
row and a target row evaluates to True. You can specify either an UPDATE action
or a DELETE action.

UPDATE

Updates the matched row in _target_table_. Only values
in the _col_name_ you specify are updated.

DELETE

Deletes the matched row in _target_table_.

WHEN NOT MATCHED

Specifies the action to be run when the match condition is evaluated to
False or Unknown. You can only specify the INSERT insert action for this
clause.

INSERT

Inserts into _target_table_ rows from
_source_table_ that don't match any rows in
_target_table_, according to
_match_condition_. The target
_col_name_ can be listed in any order. If you don’t
provide any _col_name_ values, the default order is all the
table’s columns in their declared order.

_col_name_

One or more column names that you want to modify. Don't include the table
name when specifying the target column.

_expr_

The expression defining the new value for
_col_name_.

REMOVE DUPLICATES

Specifies that the MERGE command runs in simplified mode. Simplified mode
has the following requirements:

- _target_table_ and _source_table_
  must have the same number of columns, compatible column types, and the same column order.
- Omit the WHEN clause and the UPDATE and INSERT clauses from your
  MERGE command.
- Use the REMOVE DUPLICATES clause in your MERGE command.

In simplified mode, MERGE does the following:

- Rows in _target_table_ that have a match in
  _source_table_ are updated to match the values in
  _source_table_.
- Rows in _source_table_ that don't have a match in
  _target_table_ are inserted into
  _target_table_.
- When multiple rows in _target_table_ match the
  same row in _source_table_, the duplicate rows are
  removed. Amazon Redshift keeps one row and updates it. Duplicate rows that don’t
  match a row in _source_table_ remain unchanged.

Using REMOVE DUPLICATES gives better performance than using WHEN MATCHED and
WHEN NOT MATCHED. We recommend using REMOVE DUPLICATES if
_target_table_ and _source_table_ are
compatible and you don't need to preserve duplicate rows in
_target_table_.

## Usage notes

- To run MERGE statements, you must be the owner of both
  _source_table_ and _target_table_, or
  have the SELECT permission for those tables. Additionally, you must have UPDATE,
  DELETE, and INSERT permissions for _target_table_ depending on
  the operations included in your MERGE statement.
- _target_table_ can't be a system table, catalog table, or
  external table.
- _source_table_ and _target_table_ can't be
  the same table.
- You can't use the WITH clause in a MERGE statement.
- Rows in _target_table_ can't match multiple rows in
  _source_table_.

Consider the following example:

```
CREATE TABLE target (id INT, name CHAR(10));
CREATE TABLE source (id INT, name CHAR(10));

INSERT INTO target VALUES (1, 'Bob'), (2, 'John');
INSERT INTO source VALUES (1, 'Tony'), (1, 'Alice'), (3, 'Bill');

MERGE INTO target USING source ON target.id = source.id
WHEN MATCHED THEN UPDATE SET id = source.id, name = source.name
WHEN NOT MATCHED THEN INSERT VALUES (source.id, source.name);
ERROR: Found multiple matches to update the same tuple.

MERGE INTO target USING source ON target.id = source.id
WHEN MATCHED THEN DELETE
WHEN NOT MATCHED THEN INSERT VALUES (source.id, source.name);
ERROR: Found multiple matches to update the same tuple.
```

In both MERGE statements, the operation fails because there are multiple rows
in the `source` table with an ID value of `1`.

- _match_condition_ and _expr_ can't partially
  reference SUPER type columns. For example, if your SUPER type object is an array
  or a structure, you can't use individual elements of that column for
  _match_condition_ or _expr_, but you can
  use the entire column.

Consider the following example:

```
CREATE TABLE IF NOT EXISTS target (key INT, value SUPER);
CREATE TABLE IF NOT EXISTS source (key INT, value SUPER);

INSERT INTO target VALUES (1, JSON_PARSE('{"key": 88}'));
INSERT INTO source VALUES (1, ARRAY(1, 'John')), (2, ARRAY(2, 'Bill'));

MERGE INTO target USING source ON target.key = source.key
WHEN matched THEN UPDATE SET value = source.value[0]
WHEN NOT matched THEN INSERT VALUES (source.key, source.value[0]);
ERROR: Partial reference of SUPER column is not supported in MERGE statement.
```

For more information on the SUPER type, see [SUPER type](r_SUPER_type.md "r_SUPER_type.md").

- If _source_table_ is large, defining the join columns from
  both _target_table_ and _source_table_ as
  the distribution keys can improve performance.
- To use the REMOVE DUPLICATES clause, you need SELECT, INSERT, and DELETE
  permissions for _target_table_.
- _source_table_ can be a view or subquery. Following is an
  example of a MERGE statement where _source_table_ is a subquery
  that removes duplicate rows.

```
MERGE INTO target
USING (SELECT id, name FROM source GROUP BY 1, 2) as my_source
ON target.id = my_source.id
WHEN MATCHED THEN UPDATE SET id = my_source.id, name = my_source.name
WHEN NOT MATCHED THEN INSERT VALUES (my_source.id, my_source.name);
```

- The target cannot be a data source of any subquery of the same MERGE statement.
  For example, the following SQL command returns an error like **`ERROR:
Source view/subquery in Merge statement cannot reference target
table.`** because the subquery references `target` instead
  of `source`.

```
MERGE INTO target
USING (SELECT id, name FROM `target` GROUP BY 1, 2) as my_source
ON target.id = my_source.id
WHEN MATCHED THEN UPDATE SET id = my_source.id, name = my_source.name
WHEN NOT MATCHED THEN INSERT VALUES (my_source.id, my_source.name);
```

## Examples

The following example creates two tables, then runs a MERGE operation on them,
updating matching rows in the target table and inserting rows that don't match. Then it
inserts another value into the source table and runs another MERGE operation, this time
deleting matching rows and inserting the new row from the source table.

First create and populate the source and target tables.

```
CREATE TABLE target (id INT, name CHAR(10));
CREATE TABLE source (id INT, name CHAR(10));

INSERT INTO target VALUES (101, 'Bob'), (102, 'John'), (103, 'Susan');
INSERT INTO source VALUES (102, 'Tony'), (103, 'Alice'), (104, 'Bill');

SELECT * FROM target;
 id  |    name
-----+------------
 101 | Bob
 102 | John
 103 | Susan
(3 rows)

SELECT * FROM source;
 id  |    name
-----+------------
 102 | Tony
 103 | Alice
 104 | Bill
(3 rows)
```

Next, merge the source table into the target table, updating the target table with
matching rows and insert rows from the source table that have no match.

```
MERGE INTO target USING source ON target.id = source.id
WHEN MATCHED THEN UPDATE SET id = source.id, name = source.name
WHEN NOT MATCHED THEN INSERT VALUES (source.id, source.name);

SELECT * FROM target;
 id  |    name
-----+------------
 101 | Bob
 102 | Tony
 103 | Alice
 104 | Bill
(4 rows)
```

Note that the rows with id values of 102 and 103 are updated to match the name values
from the target table. Also, a new row with an id value of 104 and name value of Bill is
inserted into the target table.

Next, insert a new row into the source table.

```
INSERT INTO source VALUES (105, 'David');

SELECT * FROM source;
 id  |    name
-----+------------
 102 | Tony
 103 | Alice
 104 | Bill
 105 | David
(4 rows)
```

Finally, run a merge operation deleting matching rows in the target table, and
inserting rows that don't match.

```
MERGE INTO target USING source ON target.id = source.id
WHEN MATCHED THEN DELETE
WHEN NOT MATCHED THEN INSERT VALUES (source.id, source.name);

SELECT * FROM target;
 id  |    name
-----+------------
 101 | Bob
 105 | David
(2 rows)
```

The rows with id values 102, 103, and 104 are deleted from the target table, and a
new row with an id value of 105 and name value of David is inserted into the target
table.

The following example shows the simplified syntax of a MERGE command that uses the
REMOVE DUPLICATES clause.

```
CREATE TABLE target (id INT, name CHAR(10));
CREATE TABLE source (id INT, name CHAR(10));

INSERT INTO target VALUES (30, 'Tony'), (11, 'Alice'), (23, 'Bill');
INSERT INTO source VALUES (23, 'David'), (22, 'Clarence');

MERGE INTO target USING source ON target.id = source.id REMOVE DUPLICATES;

SELECT * FROM target;
id | name
---+------------
30 | Tony
11 | Alice
23 | David
22 | Clarence
(4 rows)
```

The following example shows the simplified syntax of a MERGE command that uses the
REMOVE DUPLICATES clause, removing duplicate rows from _target_table_
if they have matching rows in _source_table_.

```
CREATE TABLE target (id INT, name CHAR(10));
CREATE TABLE source (id INT, name CHAR(10));

INSERT INTO target VALUES (30, 'Tony'), (30, 'Daisy'), (11, 'Alice'), (23, 'Bill'), (23, 'Nikki');
INSERT INTO source VALUES (23, 'David'), (22, 'Clarence');

MERGE INTO target USING source ON target.id = source.id REMOVE DUPLICATES;

SELECT * FROM target;
id | name
---+------------
30 | Tony
30 | Daisy
11 | Alice
23 | David
22 | Clarence
(5 rows)
```

After MERGE runs, there's only one row with an ID value of 23 in
_target_table_. Because there was no row in
_source_table_ with the ID value 30, the two duplicate rows with
ID values of 30 remain in _target_table_.

## See also

[INSERT](r_INSERT_30.md "r_INSERT_30.md"), [UPDATE](r_UPDATE.md "r_UPDATE.md"), [DELETE](r_DELETE.md "r_DELETE.md")
