# Perform other DDL operations on

Iceberg tables

In addition to the schema evolution operations described in [Evolve Iceberg table
schema](querying-iceberg-evolving-table-schema.md "querying-iceberg-evolving-table-schema.md"), you can also perform the
following DDL operations on Apache Iceberg tables in Athena.

## Database level operations

When you use [DROP DATABASE](drop-database.md "drop-database.md") with
the `CASCADE` option , any Iceberg table data is also removed. The
following DDL operations have no effect on Iceberg tables.

- [CREATE DATABASE](create-database.md "create-database.md")
- [ALTER DATABASE SET
  DBPROPERTIES](alter-database-set-dbproperties.md "alter-database-set-dbproperties.md")
- [SHOW DATABASES](show-databases.md "show-databases.md")
- [SHOW TABLES](show-tables.md "show-tables.md")
- [SHOW VIEWS](show-views.md "show-views.md")

## Partition related operations

Because Iceberg tables use [hidden partitioning](https://iceberg.apache.org/docs/latest/partitioning/#icebergs-hidden-partitioning "https://iceberg.apache.org/docs/latest/partitioning/#icebergs-hidden-partitioning"), you do not have to work with physical partitions
directly. As a result, Iceberg tables in Athena do not support the following
partition-related DDL operations:

- [SHOW PARTITIONS](show-partitions.md "show-partitions.md")
- [ALTER TABLE ADD PARTITION](alter-table-add-partition.md "alter-table-add-partition.md")
- [ALTER TABLE DROP
  PARTITION](alter-table-drop-partition.md "alter-table-drop-partition.md")
- [ALTER TABLE RENAME
  PARTITION](alter-table-rename-partition.md "alter-table-rename-partition.md")

If you would like to see Iceberg [partition evolution](https://iceberg.apache.org/docs/latest/evolution/#partition-evolution "https://iceberg.apache.org/docs/latest/evolution/#partition-evolution") in Athena, send feedback to [athena-feedback@amazon.com](mailto:athena-feedback@amazon.com "mailto:athena-feedback@amazon.com").

## Unload

Iceberg tables

Iceberg tables can be unloaded to files in a folder on Amazon S3. For information, see
[UNLOAD](unload.md "unload.md").

## MSCK

REPAIR

Because Iceberg tables keep track of table layout information, running [MSCK REPAIR TABLE](msck-repair-table.md "msck-repair-table.md") as one does with
Hive tables is not necessary and is not supported.
