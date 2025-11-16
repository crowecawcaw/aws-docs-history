# RDS for Oracle limitations

In the following sections, you can find important limitations of using RDS for Oracle. For
limitations specific to CDBs, see [Limitations of RDS for Oracle
CDBs](Oracle.Concepts.md#Oracle.Concepts.single-tenant-limitations "Oracle.Concepts.md#Oracle.Concepts.single-tenant-limitations").

###### Note

This list is not exhaustive.

###### Topics

- [Oracle file size limits in Amazon RDS](#Oracle.Concepts.file-size-limits "#Oracle.Concepts.file-size-limits")
- [Block size limits in
  RDS for Oracle](#Oracle.Concepts.block-size-limits "#Oracle.Concepts.block-size-limits")
- [Public synonyms for Oracle-supplied schemas](#Oracle.Concepts.PublicSynonyms "#Oracle.Concepts.PublicSynonyms")
- [Schemas for unsupported features
  in RDS for Oracle](#Oracle.Concepts.unsupported-features "#Oracle.Concepts.unsupported-features")
- [Limitations for DBA privileges in
  RDS for Oracle](#Oracle.Concepts.dba-limitations "#Oracle.Concepts.dba-limitations")
- [Deprecation of TLS 1.0 and 1.1 Transport Layer
  Security in RDS for Oracle](#Oracle.Concepts.tls "#Oracle.Concepts.tls")

## Oracle file size limits in Amazon RDS

The maximum size of a single file on RDS for Oracle DB instances is 16 TiB (tebibytes). This limit is imposed by the ext4 filesystem
used by the instance. Thus, Oracle bigfile data files are limited to 16 TiB. If you try to resize a data file in a bigfile
tablespace to a value over the limit, you receive an error such as the following.

```
ORA-01237: cannot extend datafile 6
ORA-01110: data file 6: '/rdsdbdata/db/mydir/datafile/myfile.dbf'
ORA-27059: could not reduce file size
Linux-x86_64 Error: 27: File too large
Additional information: 2
```

## Block size limits in

RDS for Oracle

The maximum size of a single block on RDS for Oracle DB instances is 8 KB. The 16 KB block size
isn't supported.

## Public synonyms for Oracle-supplied schemas

Don't create or modify public synonyms for Oracle-supplied schemas, including `SYS`,
`SYSTEM`, and `RDSADMIN`. Such actions might result in invalidation of core
database components and affect the availability of your DB instance.

You can create public synonyms referencing objects in your own schemas.

## Schemas for unsupported features

in RDS for Oracle

In general, Amazon RDS doesn't prevent you from creating schemas for unsupported features. However, if you
create schemas for Oracle features and components that require SYS privileges, you can damage the data
dictionary and affect your instance availability. Use only supported features and schemas that are available
in [Adding options to Oracle DB instances](Appendix.Oracle.md "Appendix.Oracle.md").

## Limitations for DBA privileges in

RDS for Oracle

In the database, a _role_ is a collection of privileges that you can grant to or
revoke from a user. An Oracle database uses roles to provide security.

The predefined role `DBA` normally allows all administrative privileges on an Oracle database.
When you create a DB instance, your master user account gets DBA privileges (with some limitations). To
deliver a managed experience, an RDS for Oracle database doesn't provide the following privileges for the
`DBA` role:

- `ALTER DATABASE`
- `ALTER SYSTEM`
- `CREATE ANY DIRECTORY`
- `DROP ANY DIRECTORY`
- `GRANT ANY PRIVILEGE`
- `GRANT ANY ROLE`

Use the master user account for administrative tasks such as creating additional user accounts in the
database. You can't use `SYS`, `SYSTEM`, and other Oracle-supplied administrative
accounts.

## Deprecation of TLS 1.0 and 1.1 Transport Layer

Security in RDS for Oracle

Transport Layer Security protocol versions 1.0 and 1.1 (TLS 1.0 and TLS 1.1) are
deprecated. In accordance with security best practices, Oracle has deprecated the use of
TLS 1.0 and TLS 1.1. To meet your security requirements, we strongly recommends that you
use TLS 1.2 instead.
