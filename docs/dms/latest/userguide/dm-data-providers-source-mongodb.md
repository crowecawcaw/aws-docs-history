# Using a MongoDB compatible database as a source for homogeneous data migrations in AWS DMS

You can use a MongoDB-compatible database as a source for Homogeneous data migrations in AWS DMS.
In this case, your source data provider can be an on-premises, Amazon EC2 for MongoDB database or
Amazon DocumentDB (with MongoDB compatibility) database.

For supported database versions, see [Source data providers for DMS homogeneous data migrations](CHAP_Introduction.md#CHAP_Introduction.Sources.HomogeneousDataMigrations "CHAP_Introduction.md#CHAP_Introduction.Sources.HomogeneousDataMigrations").

The following sections describe specific configuration prerequisites for self-managed MongoDB databases
and AWS-managed Amazon DocumentDB databases.

###### Topics

- [Using a self-managed
  MongoDB database as a source for homogeneous data migrations in AWS DMS](#dm-data-providers-source-mongodb-sm "#dm-data-providers-source-mongodb-sm")
- [Using an Amazon DocumentDB
  database as a source for homogeneous data migrations in AWS DMS](#dm-data-providers-source-mongodb-aws "#dm-data-providers-source-mongodb-aws")
- [Features for using a
  MongoDB-compatible database as a source for homogeneous data migrations](#dm-data-providers-source-mongodb-features "#dm-data-providers-source-mongodb-features")
- [Limitations for using a
  MongoDB-compatible database as a source for homogeneous data migrations](#dm-data-providers-source-mongodb-limitations "#dm-data-providers-source-mongodb-limitations")
- [Best practices for using a
  MongoDB-compatible database as a source for homogeneous data migrations](#dm-data-providers-source-mongodb-bestpractices "#dm-data-providers-source-mongodb-bestpractices")

## Using a self-managed

MongoDB database as a source for homogeneous data migrations in AWS DMS

This section describes how to configure your MongoDB databases that are hosted
on-premises or on Amazon EC2 instances.

Check the version of your source MongoDB database. Make sure that AWS DMS supports your source MongoDB
database version as described in [Source data providers for DMS homogeneous data migrations](CHAP_Introduction.md#CHAP_Introduction.Sources.HomogeneousDataMigrations "CHAP_Introduction.md#CHAP_Introduction.Sources.HomogeneousDataMigrations").

To run homogeneous data migrations with a MongoDB source, you can create either a user account with
root privileges, or a user with permissions only on the database to migrate. For more information about
user creation, see [Permissions needed when using
MongoDB as a source for AWS DMS](CHAP_Source.md#CHAP_Source.MongoDB.PrerequisitesCDC "CHAP_Source.md#CHAP_Source.MongoDB.PrerequisitesCDC").

To use ongoing replication or CDC with MongoDB, AWS DMS requires access to the MongoDB operations log (oplog).
For more information, see [Configuring a
MongoDB replica set for CDC](CHAP_Source.md#CHAP_Source.MongoDB.PrerequisitesCDC.ReplicaSet "CHAP_Source.md#CHAP_Source.MongoDB.PrerequisitesCDC.ReplicaSet").

For information about MongoDB authentication methods, see
[Security requirements when using
MongoDB as a source for AWS DMS](CHAP_Source.md#CHAP_Source.MongoDB.Security "CHAP_Source.md#CHAP_Source.MongoDB.Security").

For MongoDB as a source, homogeneous data migrations supports all of the datatypes that Amazon DocumentDB supports.

For MongoDB as a source, to store user credentials in Secrets Manager, you need to provide them in plain text,
using the **Other type of secrets** type. For more information, see
[Using secrets to access AWS Database Migration Service
endpoints](security_iam_secretsmanager.md "security_iam_secretsmanager.md").

The following code sample demonstrates how to store database secrets using plain text.

```
{
  "username": "dbuser",
  "password": "dbpassword"
}
```

## Using an Amazon DocumentDB

database as a source for homogeneous data migrations in AWS DMS

This section describes how to configure your Amazon DocumentDB database instances for use as a source for
homogeneous data migrations.

Use the master username for the Amazon DocumentDB instance as the user account for the MongoDB-compatible
source data provider for homogeneous data migrations in AWS DMS. The master user account has the required roles that
allow it to set up CDC. If you use an account other than the master user account, then the
account must have the root role. For more information on the user creation as a root account,
see [Setting permissions to use
Amazon DocumentDB as a source](CHAP_Source.md#CHAP_Source.DocumentDB.Permissions "CHAP_Source.md#CHAP_Source.DocumentDB.Permissions").

To turn on logical replication, set the `change_stream_log_retention_duration` parameter in
your database parameter group to a setting appropriate for your transaction workload. Changing this static parameter
requires you to reboot your DB instance to take effect.
Before starting data migration for all the task types including Full Load Only, enable
Amazon DocumentDB change streams for all collections within a given database, or only for selected collections.
For more information about enabling change streams for Amazon DocumentDB, see
[Enabling Change Streams](../../../documentdb/latest/developerguide/change_streams.md#change_streams-enabling "../../../documentdb/latest/developerguide/change_streams.md#change_streams-enabling") in the _Amazon DocumentDB developer guide_.

###### Note

AWS DMS uses the Amazon DocumentDB change stream to capture changes during ongoing replication.
If Amazon DocumentDB flushes out the records from the change stream before DMS reads them, your tasks
will fail. We recommend setting the `change_stream_log_retention_duration` parameter
to retain changes for at least 24 hours.

To use Amazon DocumentDB for homogeneous data migration, store user credentials in Secrets Manager under
**Credentials for Amazon DocumentDB database**.

## Features for using a

MongoDB-compatible database as a source for homogeneous data migrations

- You can migrate all the secondary indexes that Amazon DocumentDB supports during the Full load phase.
- AWS DMS migrates collections in parallel. homogeneous data migrations calculates segments at runtime
  based on the average size of each document in the collection for maximum performance.
- DMS can replicate the secondary indexes that you create in the CDC phase. DMS supports
  this feature in MongoDB version 6.0.
- DMS supports documents with a nesting level greater than 97.

## Limitations for using a

MongoDB-compatible database as a source for homogeneous data migrations

- Documents can't have field names with a `$` prefix.
- AWS DMS doesn't support time series collection migration.
- AWS DMS doesn't support `create`, `drop`, or
  `rename collection` DDL events during the CDC phase.
- AWS DMS doesn't suport inconsistent datatypes in the collection for the `_id`
  field. For example, the following unsupported collection has multiple data types for the `_id`
  field.

```
rs0 [direct: primary] test> db.collection1.aggregate([
...   {
...     $group: {
...       _id: { $type: "$_id" },
...       count: { $sum: 1 }
...     }
...   }
... ])
[ { _id: 'string', count: 6136 }, { _id: 'objectId', count: 848033 } ]
```

- For CDC-only tasks, AWS DMS only supports the `immediate` start mode.
- AWS DMS doesn't support documents with invalid UTF8 characters.
- AWS DMS doesn't support sharded collections.

## Best practices for using a

MongoDB-compatible database as a source for homogeneous data migrations

- For multiple large databases and collections hosted on same MongoDB instance,
  we recommend you use selection rules for each database and collection to split the task
  between multiple data migration tasks and projects. You can tune your database and
  collection divisions for maximum performance.
