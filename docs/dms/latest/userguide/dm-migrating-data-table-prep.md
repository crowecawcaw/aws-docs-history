# Target table preparation mode

You can select Target table preparation mode when you choose to a create data
migration task under the **Advanced Settings** tab in the AWS DMS console
for PostgreSQL, MongoDB, and Amazon DocumentDB migrations.

## Drop tables on target

In Drop tables on target mode, AWS DMS homogeneous migration drops the target tables
and recreates them before starting the migration. This approach ensures that the
target tables are empty at the start of the migration. During homogeneous
migrations, AWS DMS creates all secondary objects, including indexes defined in the
source table metadata, before loading the data to ensure efficient data
migration.

When using the Drop tables on target mode, you might need to configure the target
database. For example, with a PostgreSQL target, AWS DMS cannot create a schema user
for security reasons. In this case, you must pre-create the schema user to match the
source, allowing AWS DMS to create the tables and assign them to a similar role as the
source when the migration begins.

## Truncate

In Truncate mode, AWS DMS homogeneous migration truncates all existing target tables
before the migration begins. This preserves the table structure. This mode is
suitable for full load or full load plus CDC migrations where the target schema is
pre-created. For an Amazon DocumentDB target, if the collection does not exist,
AWS DMS creates the collection without indexes during the migration.

## Do nothing

In Do nothing mode, AWS DMS homogeneous migration assumes that the target tables are
pre-created. If the target tables are not empty, data conflicts may occur during
migration, potentially causing a DMS task error. In this mode, the table structure
remains unchanged, and any existing data is preserved. Do nothing mode is suitable
for CDC-only tasks when the target tables have been backfilled from the source, and
ongoing replication is used to synchronize the source and target. For an Amazon
DocumentDB target, if the collection does not exist, AWS DMS creates the collection
without secondary indexes. Additionally, Do nothing mode can be used during the Full
Load phase when migrating data from a MongoDB sharded collection to Amazon
DocumentDB.
