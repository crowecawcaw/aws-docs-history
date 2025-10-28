# Prerequisites for creating an Amazon RDS for Db2 DB

instance

The following items are prerequisites before creating a DB instance.

###### Topics

- [Administrator account](#db2-prereqs-admin-account "#db2-prereqs-admin-account")
- [Additional considerations](#db2-prereqs-additional-considerations "#db2-prereqs-additional-considerations")

## Administrator account

When you create a DB instance, you must designate an administrator account for the
instance. Amazon RDS grants `DBADM` authority to this local database administrator
account.

The administrator account has the following characteristics, capabilities, and
limitations:

- Is a local user and not an AWS account.
- Doesn't have Db2 instance-level authorities such as `SYSADM`,
  `SYSMAINT`, or `SYSCTRL`.
- Can't stop or start a Db2 instance.
- Can't drop a Db2 database if you specified the name when you created the DB
  instance.
- Has full access to the Db2 database including catalog tables and
  views.
- Can create local users and groups by using Amazon RDS stored procedures.
- Can grant and revoke authorities and privileges.

The administrator account can perform the following tasks:

- Create, modify, or delete DB instances.
- Create DB snapshots.
- Initiate point-in-time restores.
- Create automated backups of DB snapshots.
- Create manual backups of DB snapshots.
- Use other Amazon RDS features.

## Additional considerations

Before creating a DB instance, consider the following items:

- Each Amazon RDS for Db2 DB instance can host up to 50 Db2 databases. For more
  information, see [Multiple databases on an Amazon RDS for Db2 DB
  instance](db2-multiple-databases.md "db2-multiple-databases.md").
- Initial database name
  - If you don't provide a database name when you create a DB instance,
    Amazon RDS doesn't create a database.
  - Don't provide a database name under the following
    circumstances:
    - You want to modify the `db2_compatibility_vector`
      parameter. For more information, see [Setting the
      db2_compatibility_vector parameter](db2-known-issues-limitations.md#db2-known-issues-limitations-db2-compatibility-vector "db2-known-issues-limitations.md#db2-known-issues-limitations-db2-compatibility-vector").

- In the bring your own license (BYOL) model, you must first create a custom
  parameter group that contains your IBM Customer ID and your IBM Site ID. For more
  information, see [Bring your own license (BYOL) for
  Db2](db2-licensing.md#db2-licensing-options-byol "db2-licensing.md#db2-licensing-options-byol").
- In the Db2 license through AWS Marketplace model, you need an active AWS Marketplace subscription
  for the particular IBM Db2 edition that you want to use. If you don't already have
  one, [subscribe to Db2 in
  AWS Marketplace](db2-licensing.md#db2-marketplace-subscribing-registering "db2-licensing.md#db2-marketplace-subscribing-registering") for the IBM Db2 edition that you want to use. For more
  information, see [Db2 license through AWS Marketplace](db2-licensing.md#db2-licensing-options-marketplace "db2-licensing.md#db2-licensing-options-marketplace").
