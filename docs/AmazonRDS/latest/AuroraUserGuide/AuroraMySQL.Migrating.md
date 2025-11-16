# Migrating data from an external MySQL database to an Amazon Aurora MySQL DB cluster

If your database supports the InnoDB or MyISAM tablespaces, you have these options for
migrating your data to an Amazon Aurora MySQL DB cluster:

- You can create a dump of your data using the `mysqldump` utility, and then import that data into an
  existing Amazon Aurora MySQL DB cluster. For more information, see
  [Logical migration from MySQL to Amazon Aurora MySQL by using
  mysqldump](AuroraMySQL.Migrating.ExtMySQL.md "AuroraMySQL.Migrating.ExtMySQL.md").
- You can copy the full and incremental backup files from your database to an Amazon S3 bucket, and then restore to an
  Amazon Aurora MySQL DB cluster from those files. This option can be considerably faster than migrating data using
  `mysqldump`. For more information, see
  [Physical migration from MySQL by using Percona XtraBackup and Amazon S3](AuroraMySQL.Migrating.ExtMySQL.md "AuroraMySQL.Migrating.ExtMySQL.md").

###### Topics

- [Physical migration from MySQL by using Percona XtraBackup and Amazon S3](AuroraMySQL.Migrating.ExtMySQL.md "AuroraMySQL.Migrating.ExtMySQL.md")
- [Logical migration from MySQL to Amazon Aurora MySQL by using
  mysqldump](AuroraMySQL.Migrating.ExtMySQL.md "AuroraMySQL.Migrating.ExtMySQL.md")
