# Database architecture for

Amazon RDS Custom for Oracle

RDS Custom for Oracle supports both the Oracle multitenant and non-multitenant architecture.

###### Topics

- [Supported Oracle database
  architectures](#custom-oracle.db-architecture.types "#custom-oracle.db-architecture.types")
- [Supported engine
  types](#custom-oracle.db-architecture.engine-types "#custom-oracle.db-architecture.engine-types")
- [Supported features in the
  Oracle multitenant architecture](#custom-oracle.db-architecture.features "#custom-oracle.db-architecture.features")

## Supported Oracle database

architectures

The _Oracle multitenant architecture_, also called
the _CDB architecture_, allows an Oracle database to function as a
container database (CDB). A CDB includes pluggable databases (PDBs). A PDB is a
collection of schemas and objects that appears to an application as a traditional Oracle
database. For more information, see [Introduction to the Multitenant Architecture](https://docs.oracle.com/en/database/oracle/oracle-database/19/multi/introduction-to-the-multitenant-architecture.html "https://docs.oracle.com/en/database/oracle/oracle-database/19/multi/introduction-to-the-multitenant-architecture.html") in the _Oracle
Multitenant Administrator’s Guide_.

The CDB and non-CDB architectures are mutually exclusive. If an Oracle database isn't
a CDB, it's a non-CDB and so can't contain PDBs. In RDS Custom for Oracle, only Oracle Database 19c supports the
CDB architecture. Thus, if you create DB instances using previous Oracle database releases,
you can create only non-CDBs. For more information, see [Multitenant architecture considerations](custom-creating.md#custom-creating.overview "custom-creating.md#custom-creating.overview").

## Supported engine

types

When you create an Amazon RDS Custom for Oracle CEV or DB instance, choose either a CDB engine type or a
non-CDB engine type:

- `custom-oracle-ee-cdb` and
  `custom-oracle-se2-cdb`

These engine types specify the Oracle multitenant architecture. This option is
available only for Oracle Database 19c. When you create an RDS for Oracle DB instance using
the multitenant architecture, your CDB includes the following containers:

    + CDB root (`CDB$ROOT`)
    + PDB seed (`PDB$SEED`)
    + Initial PDB

You can create more PDBs using the Oracle SQL command `CREATE PLUGGABLE
 DATABASE`. You can't use RDS APIs to create or delete PDBs.

- `custom-oracle-ee` and `custom-oracle-se2`

These engine types specify the traditional non-CDB architecture. A non-CDB
can't contain pluggable databases (PDBs).

For more information, see [Multitenant architecture considerations](custom-creating.md#custom-creating.overview "custom-creating.md#custom-creating.overview").

## Supported features in the

Oracle multitenant architecture

An RDS Custom for Oracle CDB instance supports the following features:

- Backups
- Restoring and point-time-restore (PITR) from backups
- Read replicas
- Minor version upgrades
