# Migrating data to Amazon Aurora with PostgreSQL

compatibility

You have several options for migrating data from your existing database to an
Amazon Aurora PostgreSQL-Compatible Edition DB cluster. Your migration options also depend on the database that you
are migrating from and the size of the data that you are migrating. Following are your
options:

**[Migrating
an RDS for PostgreSQL DB instance using a snapshot](AuroraPostgreSQL.Migrating.RDSPostgreSQL.Import.md "AuroraPostgreSQL.Migrating.RDSPostgreSQL.Import.md")**

You can migrate data directly from an RDS for PostgreSQL DB snapshot to an
Aurora PostgreSQL DB cluster.

**[Migrating an RDS for PostgreSQL DB instance using an Aurora read
replica](AuroraPostgreSQL.Migrating.RDSPostgreSQL.md "AuroraPostgreSQL.Migrating.RDSPostgreSQL.md")**

You can also migrate from an RDS for PostgreSQL DB instance by creating an
Aurora PostgreSQL read replica of an RDS for PostgreSQL DB instance. When the replica lag
between the RDS for PostgreSQL DB instance and the Aurora PostgreSQL read replica is zero,
you can stop replication. At this point, you can make the Aurora read replica a
standalone Aurora PostgreSQL DB cluster for reading and writing.

**[Importing data from Amazon S3
into Aurora PostgreSQL](USER_PostgreSQL.md "USER_PostgreSQL.md")**

You can migrate data by importing it from Amazon S3 into a table belonging to an
Aurora PostgreSQL DB cluster.

**Migrating from a database that is not PostgreSQL-compatible**

You can use AWS Database Migration Service (AWS DMS) to migrate data from a database that is not PostgreSQL-compatible.
For more information on AWS DMS, see
[What is AWS Database Migration Service?](../../../dms/latest/userguide/Welcome.md "../../../dms/latest/userguide/Welcome.md")
in the _AWS Database Migration Service User Guide_.

###### Note

Enabling Kerberos authentication isn't currently supported on Aurora PostgreSQL DB cluster during migration from RDS for PostgreSQL.
You can enable Kerberos authentication only on a standalone Aurora PostgreSQL DB cluster.

For a list of AWS Regions where Aurora is available, see [Amazon Aurora](../../../general/latest/gr/rande.md#aurora "../../../general/latest/gr/rande.md#aurora") in the
_AWS General Reference_.

###### Important

If you plan to migrate an RDS for PostgreSQL DB instance to an Aurora PostgreSQL DB cluster in
the near future, we strongly recommend that you turn off auto minor version upgrades for
the DB instance early in the migration planning phase. Migration to Aurora PostgreSQL might
be delayed if the RDS for PostgreSQL version isn't yet supported by Aurora PostgreSQL.

For information about Aurora PostgreSQL versions, see [Engine versions for Amazon Aurora PostgreSQL](AuroraPostgreSQL.Updates.md "AuroraPostgreSQL.Updates.md").
