# RDS for Oracle database architecture

The _Oracle multitenant architecture_, also known as the
_CDB architecture_, enables an Oracle database to function as a
_multitenant container database (CDB)_. A CDB can include
customer-created _pluggable databases (PDBs)_. A
_non-CDB_ is an Oracle database that uses the traditional
architecture, which can't contain PDBs. For more information about the multitenant
architecture, see [_Oracle Multitenant Administrator’s Guide_](https://docs.oracle.com/en/database/oracle/oracle-database/19/multi/introduction-to-the-multitenant-architecture.html#GUID-267F7D12-D33F-4AC9-AA45-E9CD671B6F22 "https://docs.oracle.com/en/database/oracle/oracle-database/19/multi/introduction-to-the-multitenant-architecture.html#GUID-267F7D12-D33F-4AC9-AA45-E9CD671B6F22").

For Oracle Database 19c and higher, you can create an RDS for Oracle DB instance that uses the CDB architecture.
In RDS for Oracle, PDBs are referred to as _tenant databases_. Your client
applications connect at the tenant database (PDB) level rather than the CDB level. RDS for Oracle
supports the following configurations of the CDB architecture:

**Multi-tenant configuration**

Amazon RDS allows a CDB instance to contain between 1–30 tenant databases, depending on the database edition and any required option licenses. You can use RDS APIs to add, modify, and
remove tenant databases. The multi-tenant configuration in RDS for Oracle doesn't
support application PDBs or proxy PDBs, which are special types of PDBs. For
more information about application PDBs and proxy PDBs, see [Types of PDBs](https://docs.oracle.com/en/database/oracle/oracle-database/19/multi/overview-of-the-multitenant-architecture.html#GUID-D0F40745-FC70-4BE0-85D3-3745DE3312AC "https://docs.oracle.com/en/database/oracle/oracle-database/19/multi/overview-of-the-multitenant-architecture.html#GUID-D0F40745-FC70-4BE0-85D3-3745DE3312AC") in the Oracle Database documentation.

###### Note

The Amazon RDS configuration is called "multi-tenant" rather than "multitenant" because it is a
capability of Amazon RDS, not just the Oracle DB engine. Similarly, the RDS term "tenant"
refers to any tenant in an RDS configuration, not just Oracle PDBs. In the RDS documentation,
the unhyphenated term "Oracle multitenant" refers exclusively to the Oracle database CDB
architecture, which is compatible with both on-premises and RDS deployments.

**Single-tenant configuration**

Amazon RDS limits an RDS for Oracle CDB instance to 1 tenant database (PDB). You can't
add more PDBs using RDS APIs. The single-tenant configuration uses the same RDS
APIs as the non-CDB architecture. Thus, the experience of working with a CDB in
the single-tenant configuration is mostly the same as working with a
non-CDB.

You can convert a CDB that uses the single-tenant configuration to the
multi-tenant configuration, thus allowing you to add PDBs to your CDB.
This architecture change is permanent and irreversible. For more information, see [Converting the single-tenant configuration to multi-tenant](oracle-single-tenant-converting.md "oracle-single-tenant-converting.md").

###### Note

You can't access the CDB itself.

In Oracle Database 21c and higher, all databases are CDBs. In contrast, you can create an Oracle Database 19c DB instance as either a CDB or non-CDB. You can't upgrade a non-CDB to a CDB, but you
convert an Oracle Database 19c non-CDB to a CDB, and then upgrade it. You can't convert a
CDB to a non-CDB.

For more information, see the following resources:

- [Working with CDBs in RDS for Oracle](oracle-multitenant.md "oracle-multitenant.md")
- [Limitations of RDS for Oracle CDBs](Oracle.Concepts.md#Oracle.Concepts.single-tenant-limitations "Oracle.Concepts.md#Oracle.Concepts.single-tenant-limitations")
- [Creating an Amazon RDS DB instance](USER_CreateDBInstance.md "USER_CreateDBInstance.md")
