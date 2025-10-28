# Using an Amazon DocumentDB database as a target for homogeneous data migrations in AWS DMS

You can use an Amazon DocumentDB (with MongoDB compatibility) database and DocumentDB Elastic cluster as a migration target for
homogeneous data migrations in AWS DMS.

To run homogeneous data migrations for an Amazon DocumentDB target, you can create either a user account with administrator privileges,
or a user with read/write permissions only on the database to migrate.

Homogeneous data migrations supports all of the BSON data types that Amazon DocumentDB supports. For a list of these
data types, see
[Data Types](../../../documentdb/latest/developerguide/mongo-apis.md#mongo-apis-data-types "../../../documentdb/latest/developerguide/mongo-apis.md#mongo-apis-data-types") in the _Amazon DocumentDB Developer Guide_.

To use shard features of DocumentDB Elastic cluster for migrating non-sharded collection from the source,
create a shard collection to migrate prior to starting the data migration task. For more information about
shard collection in an Amazon DocumentDB Elastic cluster, see
[Step 5: Shard your collection](../../../documentdb/latest/developerguide/elastic-get-started.md#elastic-get-started-step6 "../../../documentdb/latest/developerguide/elastic-get-started.md#elastic-get-started-step6") in the _Amazon DocumentDB Developer Guide_.

For an Amazon DocumentDB target, AWS DMS supports the `none` or `require` SSL modes.
