Amazon Redshift will no longer support the creation of new Python UDFs starting Patch 198.
Existing Python UDFs will continue to function until June 30, 2026. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# USE

Changes the database on which queries run. SHOW USE points to the database that most
recently is used with the USE command. RESET USE resets the used database. This means that if the database is not specified in the SQL, the objects are searched
in the current database.

## Syntax

```
USE *database*
```

## Examples

Suppose there are three databases, `dev` and `pdb`, and
`pdb2`. Let there be two tables `t` in the public schemas of
each of the databases. First, insert data into tables across different databases:

```
dev=# insert into dev.public.t values (1);
INSERT 0 1
dev=# insert into pdb.public.t values (2);
INSERT 0 1
```

Without explicitly setting a database, the system uses your connected database. Check
your current database context:

```
dev=# show use;
Use Database

(1 row)
dev=> show search_path;
search_path
$user, public
(1 row)
```

When querying table `t` without specifying a database, the system uses the
table in your current database:

```
dev=# select * from t;
c
----
1
(1 row)
```

Use the `use` command to switch databases without changing your
connection:

```
dev=# use pdb;
USE
dev=# show use;
 Use Database
--------------
 pdb
(1 row)
dev=# select * from t;
id
----
2
(1 row)
```

You can also explicitly specify the schema:

```
dev=# select * from public.t;
id
----
2
(1 row)
```

You can now create tables in different schemas within your current database:

```
dev=# create table s1.t(id int);
CREATE TABLE
dev=# insert into pdb.s1.t values (3);
INSERT 0 1
```

The search path determines which schema's objects are accessed when you don't specify
a schema:

```
dev=# set search_path to public, s1;
SET
dev=# select * from t;
 id
----
  2
(1 row)
```

Change the order of schemas to access different tables:

```
dev=# set search_path to s1, public;
SET
dev=# show search_path;
 search_path
-------------
 s1, public
(1 row)
dev=# select * from t;
 id
----
  3
(1 row)
```

Switch to another database while maintaining your original connection:

```
dev=# show use;
 Use Database
--------------
 pdb
(1 row)
dev=# use pdb2;
USE
dev=# show use;
 Use Database
--------------
 pdb2
(1 row)
```

When switching databases, the search path resets to default:

```
dev=# show search_path;
  search_path
---------------
 $user, public
(1 row)
```

Create a table and insert data in your current database:

```
dev=# create table pdb2.public.t(id int);
CREATE TABLE
dev=# insert into pdb2.public.t values (4);
INSERT 0 1
dev=# select * from t;
 id
----
  4
(1 row)
```

In transactions, you can write to the current database and read from any database
using three-part notation. This also includes the connected database:

```
dev=# show use;
 Use Database
--------------
 pdb2
(1 row)

dev=# BEGIN;
BEGIN
dev=# select * from t;
 id
----
  4
(1 row)

dev=# insert into t values (5);
INSERT 0 1
dev=# select * from t;
 id
----
  4
  5
(2 rows)

dev=# select * from pdb.public.t;
 id
----
  2
(1 row)

dev=# select * from dev.public.t;
 id
----
  1
(1 row)
```

Reset to your connected database. Note that this does not only revert to the
previously used database `pdb`, but resets to the connected database. The
search path also changes to the default one:

```
dev=# RESET USE;
RESET
dev=# select * from t;
c
----
1
(1 row)
dev=# show use;
 Use Database
--------------

(1 row)

dev=# show search_path;
  search_path
---------------
 $user, public
(1 row)
```

You can change databases at the start of a transaction, but not after running
queries:

```
dev=# BEGIN;
BEGIN
dev=# use pdb;
USE
dev=# use pdb2;
USE
dev=# use pdb;
USE
dev=# select * from t;
 id
----
  2
(1 row)
dev=# use pdb2;
ERROR:  USEd Database cannot be set or reset inside a transaction after another command.
dev=# rollback;
ROLLBACK
(1 row)
```

### Data Catalog example

First, create tables in different schemas and catalogs to demonstrate cross-catalog queries. Start by creating tables in the connected database.

```

dev=# CREATE TABLE dev.public.t (col INT);
dev=# INSERT INTO dev.public.t VALUES (1);
dev=# CREATE SCHEMA write_schema;
dev=# CREATE TABLE dev.write_schema.t (state char (2));
dev=# INSERT INTO dev.write_schema.t VALUES ('WA');

```

Now, create similar tables in a different catalog. This demonstrates how to work with cross-catalog databases.

```

dev=# CREATE TABLE my_db@my_catalog.public.t (col INT);
dev=# INSERT INTO my_db@my_catalog.public.t VALUES (100);
dev=# CREATE SCHEMA my_db@my_catalog.write_schema;
dev=# CREATE TABLE my_db@my_catalog.write_schema.t (state char (2));
dev=# INSERT INTO my_db@my_catalog.write_schema.t VALUES ('CA');

```

Check the current database context. Without explicitly setting a database, the system uses the connected database.

```

dev=# SHOW USE;
 Use Database
--------------

(1 row)

dev=# SHOW search_path;
  search_path
---------------
 $user, public
(1 row)

dev=# SELECT * FROM t;
 col
-----
   1
(1 row)

```

Set the USEd database to query the tables in a different catalog.

```

dev=# USE my_db@my_catalog;

dev=# SHOW USE;
            Use Database
-------------------------------------
 my_db@my_catalog
(1 row)

dev=# SHOW search_path;
  search_path
---------------
 $user, public
(1 row)

```

When querying table t, results come from the cross-catalog database.

```

dev=# SELECT * FROM t;
 col
-----
 100
(1 row)

dev=# SELECT * FROM public.t;
 col
-----
 100
(1 row)

dev=# SELECT * FROM my_db@my_catalog.public.t;
 col
-----
 100
(1 row)

```

Change the search path to access tables in different schemas within the USEd database.

```

dev=# SET search_path to write_schema;

dev=# SHOW search_path;
 search_path
--------------
 write_schema
(1 row)

dev=# SELECT * FROM t;
 state
-------
 CA
(1 row)

dev=# SELECT * FROM write_schema.t;
 state
-------
 CA
(1 row)

dev=# SELECT * FROM my_db@my_catalog.write_schema.t;
 state
-------
 CA
(1 row)

```

Even though USE is set to a cross-catalog database, it's still possible to explicitly query the original database.

```

dev=# SELECT * FROM dev.write_schema.t;
 state
-------
 WA
(1 row)

```

Reset the USEd database to again refer to objects in the connected database.

```

dev=# RESET USE;

dev=# SHOW USE;
 Use Database
--------------

(1 row)

```

Note that the search_path gets reset when USE is reset.

```

dev=# SHOW search_path;
  search_path
---------------
 $user, public
(1 row)

```

After resetting, queries now refer to the original connected database.

```

dev=# SELECT * FROM t;
 col
-----
   1
(1 row)

dev=# SELECT * FROM public.t;
 col
-----
   1
(1 row)

dev=# SELECT * FROM dev.public.t;
 col
-----
   1
(1 row)

```

You can modify the search path in the original database to access different schemas.

```

dev=# SET search_path to write_schema;

dev=# SHOW search_path;
 search_path
--------------
 write_schema
(1 row)

dev=# SELECT * FROM t;
 state
-------
 WA
(1 row)

dev=# SELECT * FROM write_schema.t;
 state
-------
 WA
(1 row)

dev=# SELECT * FROM dev.write_schema.t;
 state
-------
 WA
(1 row)
```
