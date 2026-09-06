

# Creating and setting a target database to work with AWS DMS schema conversion
<a name="dm-data-providers-target"></a>

You can use MySQL-compatible, PostgreSQL, and Amazon DocumentDB databases as a target data provider for homogeneous data migrations in AWS DMS.

For supported database versions, see [Target data providers for DMS homogeneous data migrations](CHAP_Introduction.Targets.md#CHAP_Introduction.Targets.HomogeneousDataMigrations).

Your target data provider can be an Amazon RDS DB instance or an Amazon Aurora DB cluster. Note that the database version of your target data provider must be equal or higher than the database version of your source data provider.

**Topics**
+ [Using a MySQL compatible database as a target for homogeneous data migrations in AWS DMS](dm-data-providers-target-mysql.md)
+ [Using a PostgreSQL database as a target for homogeneous data migrations in AWS DMS](dm-data-providers-target-postgresql.md)
+ [Using an Amazon DocumentDB database as a target for homogeneous data migrations in AWS DMS](dm-data-providers-target-docdb.md)