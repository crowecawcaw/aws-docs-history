# Overview of RDS for Oracle CDBs

You can create an RDS for Oracle DB instance as a container database (CDB) when you run Oracle
Database 19c or higher. Starting with Oracle Database 21c, all databases are CDBs. A CDB
differs from a non-CDB because it can contain pluggable databases (PDBs), which are called
_tenant databases_ in RDS for Oracle. A PDB is a portable collection
of schemas and objects that appears to an application as a separate database.

You create your initial tenant database (PDB) when you create your CDB instance. In
RDS for Oracle, your client application interacts with a PDB rather than the CDB. Your experience
with a PDB is mostly identical to your experience with a non-CDB.

###### Topics

- [Multi-tenant configuration of
  the CDB architecture](#multi-tenant-configuration "#multi-tenant-configuration")
- [Single-tenant configuration of the
  CDB architecture](#Oracle.Concepts.single-tenant "#Oracle.Concepts.single-tenant")
- [Creation and conversion options for
  CDBs](#oracle-cdb-creation-conversion "#oracle-cdb-creation-conversion")
- [User accounts and privileges in a
  CDB](#Oracle.Concepts.single-tenant.users "#Oracle.Concepts.single-tenant.users")
- [Parameter group families in a
  CDB](#Oracle.Concepts.single-tenant.parameters "#Oracle.Concepts.single-tenant.parameters")
- [Limitations of RDS for Oracle
  CDBs](#Oracle.Concepts.single-tenant-limitations "#Oracle.Concepts.single-tenant-limitations")

## Multi-tenant configuration of

the CDB architecture

RDS for Oracle supports the _multi-tenant configuration_ of the Oracle
multitenant architecture, also called the _CDB architecture_. In this
configuration, your RDS for Oracle CDB instance can contain 1–30 tenant databases, depending on the database edition and any required option licenses. In Oracle database, a tenant database is a PDB. Your
DB instance must use Oracle database release 19.0.0.0.ru-2022-01.rur-2022.r1 or higher.

###### Note

The Amazon RDS configuration is called "multi-tenant" rather than "multitenant" because it is a
capability of Amazon RDS, not just the Oracle DB engine. Similarly, the RDS term "tenant"
refers to any tenant in an RDS configuration, not just Oracle PDBs. In the RDS documentation,
the unhyphenated term "Oracle multitenant" refers exclusively to the Oracle database CDB
architecture, which is compatible with both on-premises and RDS deployments.

You can configure the following settings:

- Tenant database name
- Tenant database master username
- Tenant database master password (optionally integrated with Secrets Manager)
- Tenant database character set
- Tenant database national character set

The tenant database character set can be different from the CDB character set. The
same applies to the national character set. After you create your initial tenant
database, you can create, modify, or delete tenant databases using RDS APIs. The CDB
name defaults to `RDSCDB` and can't be changed. For more information, see
[Settings for DB instances](USER_CreateDBInstance.md "USER_CreateDBInstance.md") and [Modifying an RDS for Oracle tenant
database](oracle-cdb-configuring.modifying.md "oracle-cdb-configuring.modifying.md").

## Single-tenant configuration of the

CDB architecture

RDS for Oracle supports a legacy configuration of the Oracle multitenant architecture called
the _single-tenant configuration_. In this configuration, an
RDS for Oracle CDB instance can contain only one tenant (PDB). You can't create more PDBs later.

## Creation and conversion options for

CDBs

Oracle Database 21c supports only CDBs, whereas Oracle Database 19c supports both CDBs
and non-CDBs. All RDS for Oracle CDB instances support both the multi-tenant and single-tenant
configurations.

### Creation, conversion,

and upgrade options for the Oracle database architecture

The following table shows the different architecture options for creating and
upgrading RDS for Oracle databases.

| Release             | Database creation options   | Architecture conversion options                       | Major version upgrade targets |
| ------------------- | --------------------------- | ----------------------------------------------------- | ----------------------------- |
| Oracle Database 21c | CDB architecture only       | N/A                                                   | N/A                           |
| Oracle Database 19c | CDB or non-CDB architecture | Non-CDB to CDB architecture (April 2021 RU or higher) | Oracle Database 21c CDB       |

As shown in the preceding table, you can't directly upgrade a non-CDB to a CDB in
a new major database version. But you can convert an Oracle Database 19c non-CDB to
an Oracle Database 19c CDB, and then upgrade the Oracle Database 19c CDB to an
Oracle Database 21c CDB. For more information, see [Converting an RDS for Oracle non-CDB to a CDB](oracle-cdb-converting.md "oracle-cdb-converting.md").

### Conversion options

for CDB architecture configurations

The following table shows the different options for converting the architecture
configuration of an RDS for Oracle DB instance.

| Current architecture and configuration    | Conversion to the single-tenant configuration of the CDB<br>architecture | Conversion to the multi-tenant configuration of the CDB<br>architecture | Conversion to the non-CDB architecture |
| ----------------------------------------- | ------------------------------------------------------------------------ | ----------------------------------------------------------------------- | -------------------------------------- |
| Non-CDB                                   | Supported                                                                | Supported\*                                                             | N/A                                    |
| CDB using the single-tenant configuration | N/A                                                                      | Supported                                                               | Not supported                          |
| CDB using the multi-tenant configuration  | Not supported                                                            | N/A                                                                     | Not supported                          |

\* You can't convert a non-CDB to the multi-tenant configuration in a single
operation. When you convert a non-CDB to a CDB, the CDB is in the single-tenant
configuration. You can then convert the single-tenant to the multi-tenant
configuration in a separate operation.

## User accounts and privileges in a

CDB

In the Oracle multitenant architecture, all user accounts are either _common
users_ or _local users_. A CDB common user is a
database user whose single identity and password are known in the CDB root and in every
existing and future PDB. In contrast, a local user exists only in a single PDB.

The RDS master user is a local user account in the PDB, which you name when you create
your DB instance. If you create new user accounts, these users will also be local users
residing in the PDB. You can't use any user accounts to create new PDBs or modify the
state of the existing PDB.

The `rdsadmin` user is a common user account. You can run RDS for Oracle packages
that exist in this account, but you can't log in as `rdsadmin`. For more
information, see [About Common Users and Local Users](https://docs.oracle.com/en/database/oracle/oracle-database/19/dbseg/managing-security-for-oracle-database-users.html#GUID-BBBD9904-F2F3-442B-9AFC-8ACDD9A588D8 "https://docs.oracle.com/en/database/oracle/oracle-database/19/dbseg/managing-security-for-oracle-database-users.html#GUID-BBBD9904-F2F3-442B-9AFC-8ACDD9A588D8") in the Oracle documentation.

For master users in both the multi-tenant and single-tenant configurations, you can
use credentials that are self-managed or managed by AWS Secrets Manager. In the single-tenant
configuration, you use instance-level CLI commands such as
`create-db-instance` for managed master passwords. In the multi-tenant
configuration, you use tenant database commands such as
`create-tenant-database` for managed master passwords. For more
information about Secrets Manager integration, see [Managing the master user password for an
RDS for Oracle tenant database with Secrets Manager](rds-secrets-manager.md#rds-secrets-manager-tenant "rds-secrets-manager.md#rds-secrets-manager-tenant").

## Parameter group families in a

CDB

CDBs have their own parameter group families and default parameter values. The CDB
parameter group families are as follows:

- oracle-ee-cdb-21
- oracle-se2-cdb-21
- oracle-ee-cdb-19
- oracle-se2-cdb-19

## Limitations of RDS for Oracle

CDBs

RDS for Oracle supports a subset of features available in an on-premises CDB.

### CDB limitations

The following limitations apply to RDS for Oracle at the CDB level:

- You can’t connect to a CDB. You always connect to the tenant database
  (PDB) rather than the CDB. Specify the endpoint for the PDB just as for a
  non-CDB. The only difference is that you specify
  _pdb_name_ for the database name, where
  _pdb_name_ is the name you chose for your PDB.
- You can't convert a CDB in the multi-tenant configuration to a CDB in the
  single-tenant conversion. Conversion to the multi-tenant configuration is
  one-way and irreversible.
- You can't enable or convert to the multi-tenant configuration if your
  DB instance uses an Oracle database release lower than
  19.0.0.0.ru-2022-01.rur-2022.r1.
- You can't use Oracle Data Guard in the multi-tenant configuration, but you
  can use it in the single-tenant configuration.
- You can't use Database Activity Streams in a CDB.
- You can't enable auditing from within `CDB$ROOT`. You must enable
  auditing within each PDB individually.

### Tenant database (PDB)

limitations

The following limitations apply to tenant databases in the RDS for Oracle multi-tenant
configuration:

- You can't defer tenant database operations to the maintenance window. All
  changes occur immediately.
- You can't add a tenant database to a CDB that uses the single-tenant
  configuration.
- You can't add or modify multiple tenant databases in a single operation.
  You can only add or modify them one at a time.
- You can't modify a tenant database to be named `CDB$ROOT` or
  `PDB$SEED`.
- You can't delete a tenant database if it is the only tenant in the
  CDB.
- Not all DB instance class types have sufficient resources to support multiple
  PDBs in an RDS for Oracle CDB instance. An increased PDB count affects the
  performance and stability of the smaller instance classes and increases the
  time of most instance-level operations, for example, database
  upgrades.
- You can't use multiple AWS accounts to create PDBs in the same CDB. PDBs
  must be owned by the same account as the DB instance that the PDBs are hosted
  on.
- All PDBs in a CDB use the same endpoint and database listener.
- The following operations aren't supported at the PDB level but are
  supported at the CDB level:
  - Backup and recovery
  - Database upgrades
  - Maintenance actions

- The following features aren't supported at the PDB level but are supported
  at the CDB level:
  - Option groups (options are installed on all PDBs on your CDB
    instance)
  - Parameter groups (all parameters are derived from the parameter
    group associated with your CDB instance)

- PDB-level operations that are supported in the on-premises CDB
  architecture but aren't supported in an RDS for Oracle CDB include the
  following:

###### Note

The following list is not exhaustive.

    + Application PDBs
    + Proxy PDBs
    + Starting and stopping a PDB
    + Unplugging and plugging in PDBs


    To move data into or out of your CDB, use the same techniques as
     for a non-CDB. For more information about migrating data, see [Importing data into Oracle on Amazon RDS](Oracle.Procedural.md "Oracle.Procedural.md").
    + Setting options at the PDB level


    The PDB inherits options settings from the CDB option group. For
     more information about setting options, see [Parameter groups for Amazon RDS](USER_WorkingWithParamGroups.md "USER_WorkingWithParamGroups.md"). For best
     practices, see [Working with DB parameter groups](CHAP_BestPractices.md#CHAP_BestPractices.DBParameterGroup "CHAP_BestPractices.md#CHAP_BestPractices.DBParameterGroup").
    + Configuring parameters in a PDB


    The PDB inherits parameter settings from the CDB. For more
     information about setting option, see [Adding options to Oracle DB instances](Appendix.Oracle.md "Appendix.Oracle.md").
    + Configuring different listeners for PDBs in the same CDB
    + Oracle Flashback features
