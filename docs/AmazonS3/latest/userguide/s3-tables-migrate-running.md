

# Running a table migration
<a name="s3-tables-migrate-running"></a>

**To migrate a table by using the Amazon S3 console**

1. Sign in to the AWS Management Console and open the Amazon S3 console at [https://console.aws.amazon.com/s3/](https://console.aws.amazon.com/s3/).

1. In the navigation pane, choose **Table buckets**.

1. Choose the name of the destination table bucket.

1. Choose **Create table**, and then choose **Migrate existing table**.

1. For **Source table**, choose the AWS Glue database and the Apache Hive table that you want to migrate.

1. For **Destination table**, choose the namespace and enter a name for the table.

1. For **IAM role**, choose an existing role that has the required permissions, or choose **Create new IAM role**. For the permissions, see [Required permissions](s3-tables-migrate-setting-up.md#s3-tables-migrate-required-permissions).

1. For **Report location**, choose the general purpose bucket for the reports. (Optional) Enter a prefix.

1. Choose **Start migration**.

To sync or complete the migration, choose the destination table, and then choose **Sync** or **Complete migration**.

**To migrate a table by using the AWS CLI**

1. Start the migration. Specify the migration role, the destination table, the source AWS Glue table, and where to write the reports. The migration job creates the destination table in the namespace that you specify.

   ```
   aws s3tables start-table-migration \
       --role-arn arn:aws:iam::{{111122223333}}:role/{{S3TablesMigrationRole}} \
       --destination-table '{"tableBucketARN":"arn:aws:s3tables:{{us-east-1}}:{{111122223333}}:bucket/{{amzn-s3-demo-table-bucket}}","namespace":"{{example_namespace}}","name":"{{example_table}}"}' \
       --source-type glueTable --source '{"glueTable":{"catalogId":"{{111122223333}}","databaseName":"{{example_database}}","tableName":"{{example_source_table}}"}}' \
       --migration-output '{"bucket":"arn:aws:s3:::{{amzn-s3-demo-bucket}}","prefixes":{"tableCompatibilityReport":"{{migration-reports}}","objectCompatibilityReport":"{{migration-reports}}","objectMigrationReport":"{{migration-reports}}"}}'
   ```

   The response returns a `migrationId` that you use to track the migration. You can also set the following options in the start command:
   + **Review the compatibility reports before copying data** – Add `--review-migration-plan`, and then approve the migration in step 2.
   + **Specify the destination schema** – Add `schema` to `--destination-table`.
   + **Choose migration policy** – Add `--data-migration '{"migrationPolicies":{"unmatchedSourceFieldsPolicy":"drop","incompatibleValuesPolicy":"setNull"}}'`. For more information, see [Migration policy](s3-tables-migrate-how-it-works.md#s3-tables-migrate-migration-policies).
   + **Change compression and compaction** – Add `properties` to `--destination-table`, or `maintenanceSettings` to `--data-migration`. For more information, see [Destination and migration settings](s3-tables-migrate-setting-up.md#s3-tables-migrate-compaction-settings).

1. (Optional) If you started the migration with `--review-migration-plan`, review the compatibility reports, and then approve the migration. To approve it, set the requested state to `queued`.

   ```
   aws s3tables update-table-migration \
       --migration-id {{example-migration-id}} \
       --requested-state queued
   ```

   The migration moves to `queued`, and then to `migrating` when the copy begins. To stop the migration instead, set `--requested-state` to `cancelled`. You can approve a migration only in the `pendingReview` state. For what happens when you cancel a table migration, see [Data from failed or cancelled migrations](#s3-tables-migrate-failed-data).

1. Monitor the migration until it reaches the `succeeded` state.

   ```
   aws s3tables get-table-migration \
       --migration-id {{example-migration-id}}
   ```

   The response includes the migration's state, planning and migration statistics, whether it's a start or a sync, and the location of each report after it's written. If the migration fails, the response also includes a `failureReason`. For more information, see [Troubleshooting](#s3-tables-migrate-troubleshooting).

1. (Optional) Sync the table to copy source data that changed since the previous start or sync. Specify the migration role, the destination table ARN, and where to write the reports.

   ```
   aws s3tables sync-table-migration \
       --role-arn arn:aws:iam::{{111122223333}}:role/{{S3TablesMigrationRole}} \
       --table-arn arn:aws:s3tables:{{us-east-1}}:{{111122223333}}:bucket/{{amzn-s3-demo-table-bucket}}/table/{{example-table-id}} \
       --migration-output '{"bucket":"arn:aws:s3:::{{amzn-s3-demo-bucket}}","prefixes":{"tableCompatibilityReport":"{{migration-reports}}","objectCompatibilityReport":"{{migration-reports}}","objectMigrationReport":"{{migration-reports}}"}}'
   ```

   A sync uses the source, migration policy, and settings that you specified when you started the migration. For more information, see [Migration policy](s3-tables-migrate-how-it-works.md#s3-tables-migrate-migration-policies). Each sync returns a new `migrationId`, which you monitor the same way as a start. To review the compatibility reports before a sync copies data, add `--review-migration-plan`, and then approve the sync as described in step 2.

1. Verify the destination table.

1. Complete the migration.

   ```
   aws s3tables complete-table-migration \
       --table-arn arn:aws:s3tables:{{us-east-1}}:{{111122223333}}:bucket/{{amzn-s3-demo-table-bucket}}/table/{{example-table-id}}
   ```

   Completing a migration can't be undone. Completing makes the destination table read-write and turns on automatic table maintenance. After you complete the migration, you can query and write to the table with any engine that supports Apache Iceberg.

## Monitoring a migration
<a name="s3-tables-migrate-monitoring"></a>

To track a start or sync, call `GetTableMigration` and check `state` and the planning and migration statistics. For each state, see [Migration states](#s3-tables-migrate-states). You can also view a migration's state, statistics, and reports in the Amazon S3 console.

## Migration states
<a name="s3-tables-migrate-states"></a>

Each start and sync reports its progress as a state.


| State | Description | 
| --- | --- | 
| new | S3 Tables accepted the request and are validating the source and destination. | 
| planning | The migration job is identifying and checking the source objects, and writing the compatibility reports. | 
| pendingReview | Planning is done, and the migration is waiting for you to approve or cancel it. Only when you set reviewMigrationPlan to true. | 
| queued | The migration is approved and waiting to start copying data. | 
| migrating | The migration job is copying data into the destination table and committing it. | 
| succeeded | Every planned object migrated. | 
| failed | The migration stopped because of an error. For the cause, see failureReason. | 
| cancelling | You cancelled the migration, and it's stopping. | 
| cancelled | The migration stopped because you cancelled it. | 

You can cancel a start or sync in the `new`, `planning`, `pendingReview`, `queued`, or `migrating` state.

## Troubleshooting
<a name="s3-tables-migrate-troubleshooting"></a>

When a migration fails, `failureReason` in the `GetTableMigration` response includes a code that tells you where to look:
+ **A report found issues (`tableCompatibilityReport`, `objectCompatibilityReport`, `objectMigrationReport`)** – Review the report named in the code, and fix the issues that it lists.
+ **Permissions or resources (`rolePermissions`, `sourcePermissions`, `destinationPermissions`, `resourceNotFound`, `reportBucketNotSupported`)** – Check the migration role's trust policy and permissions, the bucket and key policies, and the names, Regions, and requirements of the resources that you specified. The `detail` field names the resource involved.
+ **The source can't be migrated (`sourceNotSupported`)** – See [Considerations and limitations](s3-tables-migrate-setting-up.md#s3-tables-migrate-considerations).
+ **Internal error (`internalError`)** – Try again, and contact AWS Support if the error persists.

After you fix the cause, continue as described in [Data from failed or cancelled migrations](#s3-tables-migrate-failed-data).

## Data from failed or cancelled migrations
<a name="s3-tables-migrate-failed-data"></a>

When a migration fails or is cancelled, the destination table keeps the data that migration already committed. To continue, call `ListTableMigrations` and check `hasValidPlan` for each earlier start or sync:
+ If the destination table exists and `hasValidPlan` is `true` for an earlier start or sync, fix the cause of any failure, and then sync the table.
+ If the destination table exists but `hasValidPlan` is `false` for every earlier start or sync, fix the cause of the failure, delete the destination table, and then start a new migration.
+ If the destination table doesn't exist, start a new migration.

A sync migrates the objects that didn't migrate and any objects that you added, and removes the data of objects that you deleted. You can also delete the destination table at any time. Deleting it deletes the migrated data and ends the migration. To migrate the table again, start a new migration.