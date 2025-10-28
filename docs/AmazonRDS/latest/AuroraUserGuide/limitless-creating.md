# Creating Aurora PostgreSQL Limitless Database tables

There are three types of tables that contain your data in Aurora PostgreSQL Limitless Database:

- Standard – This is the default table type in Aurora PostgreSQL Limitless Database. You create standard
  tables using the [CREATE
  TABLE](https://www.postgresql.org/docs/current/sql-createtable.html "https://www.postgresql.org/docs/current/sql-createtable.html") command, and can run Data Description Language (DDL) and Data
  Manipulation Language (DML) operations on them.

Standard tables aren't distributed tables. They're stored on one of the shards chosen internally by the system.

- Sharded – These tables are distributed across multiple shards. Data is split among the shards based on the values of designated
  columns in the table. This set of columns is called a shard key.
- Reference – These tables are replicated on all shards. They're used for infrequently modified reference data, such as product
  catalogs and zip codes.

Join queries between reference and sharded tables can be run on shards, eliminating unnecessary data movement between shards and
routers.
There are two ways to create limitless tables:

- [Creating limitless tables by using variables](limitless-creating-config.md "limitless-creating-config.md") – Use this method when you want to create new
  sharded and reference tables.
- [Converting standard tables to limitless tables](limitless-converting-standard.md "limitless-converting-standard.md") – Use this method when you want to
  convert existing standard tables into sharded and reference tables.
  We also provide [sample schemas](limitless-sample-schemas.md "limitless-sample-schemas.md") for Aurora PostgreSQL Limitless Database.
