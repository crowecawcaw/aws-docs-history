# Performing common

database tasks for Amazon RDS for Db2 DB instances

You can perform certain common DBA tasks related to databases on your Amazon RDS for Db2 DB
instances. To deliver a managed service experience, Amazon RDS doesn't provide shell access to DB
instances. Also, the master user can't run commands or utilities requiring
`SYSADM`, `SYSMAINT`, or `SYSCTRL` authorities.

For information about common tasks for buffer pools, databases, and tablespaces, see the following topics.

###### Topics

- [Common tasks for buffer pools](db2-managing-buffer-pools.md "db2-managing-buffer-pools.md")
- [Common tasks for databases](db2-managing-databases.md "db2-managing-databases.md")
- [Common tasks for tablespaces](db2-managing-tablespaces.md "db2-managing-tablespaces.md")

## Managing storage

Db2 uses automatic storage to manage the physical storage for database objects such as
tables, indexes, and temporary files. Instead of manually allocating storage space and
keeping track of which storage paths are being used, automatic storage allows the Db2 system
to create and manage storage paths as needed. This can simplify administration of Db2
databases and reduce the likelihood of errors due to human mistakes. For more information,
see [Automatic storage](https://www.ibm.com/docs/en/db2/11.5?topic=overview-automatic-storage "https://www.ibm.com/docs/en/db2/11.5?topic=overview-automatic-storage") in the IBM Db2 documentation.

With RDS for Db2, you can dynamically increase the storage size with automatic expansion
of the logical volumes and the file system. For more information, see [Working with storage for Amazon RDS DB instances](USER_PIOPS.md "USER_PIOPS.md").
