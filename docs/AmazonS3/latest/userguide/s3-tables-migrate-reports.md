

# Migration reports and statistics
<a name="s3-tables-migrate-reports"></a>

## Migration statistics
<a name="s3-tables-migrate-statistics"></a>

When you call `GetTableMigration`, the response includes two sets of statistics. Planning statistics describe the source objects that planning scanned and included. Both planning and migration statistics describe a single start or sync. A sync counts the objects that it adds or re-migrates, so an object that several syncs re-migrate is counted in each of them.

### Planning statistics
<a name="s3-tables-migrate-planning-stats"></a>


| Statistic | Description | 
| --- | --- | 
| objectsScanned | The number of source objects that planning scanned under the table location. | 
| objectsPlanned | The number of source objects that planning included in the migration. | 
| partitionCount | The number of AWS Glue partitions that planning included in the migration. | 

### Migration statistics
<a name="s3-tables-migrate-migration-stats"></a>


| Statistic | Description | 
| --- | --- | 
| objectsMigrated | The number of source objects that were copied and are available for querying. | 
| objectsFailedMigration | The number of source objects that failed to migrate. | 
| objectsPendingMigration | The number of planned source objects that are remaining. | 

## Migration reports
<a name="s3-tables-migrate-reports-overview"></a>

A migration job writes the following reports that you can use to review and validate a migration:
+ **Table compatibility report** – Written at the end of the planning state, before any data is copied. Lists any issues with your table definition and shows how each column's data type maps to the destination table.
+ **Object compatibility report** – Written at the end of the planning state, before any data is copied. Lists every source object that was scanned in planning, whether the object is included in the migration job, and any issue that prevents it from migrating, such as an archived storage class or unsupported encryption.
+ **Object migration report** – Written when a start or sync operation completes. Lists every source object that the migration job attempted, whether it migrated, how its data was transformed, and why it failed. This report is not written if the operation fails in the planning state.

If a migration fails, `failureReason` in the `GetTableMigration` response tells you which report to look at. A code of `tableCompatibilityReport`, `objectCompatibilityReport`, or `objectMigrationReport` names the report to review. For every code and how to resolve it, see [Troubleshooting](s3-tables-migrate-running.md#s3-tables-migrate-troubleshooting). For each compatibility report, `migrationOutput` also returns the number of invalid findings (`invalidFindings`) by category: `access`, `metadata`, `data`, and `internal`. Within a report, the following fields are stable and can be used for automation: states, finding categories, and failure reasons. Conversely, finding subcategories, outcomes, and messages can change or be added over time, making these unsuitable for automation. Values that the migration API returns, such as states, failure reasons, and finding categories, are stable.

### Report location and structure
<a name="s3-tables-migrate-reports-location"></a>

In start and sync operations, you specify the output location of the migration reports using the `migrationOutput` parameter. Specify one general purpose bucket. You can optionally specify a prefix for each report. If a prefix is not specified for a report, all reports are written to the root of the bucket. Under each prefix, migration writes the reports for each start and sync in a folder named for its migration ID, as in the following example:

```
{{amzn-s3-demo-bucket}}/
    {{your-optional-prefix}}/
        {{migration-id}}/
            table-compatibility-report/
            object-compatibility-report/
            object-migration-report/
```

After migration writes a report, `GetTableMigration` returns the report's object key and checksum in `migrationOutput`. For the object compatibility report and the object migration report, the key points to the report's manifest. For the table compatibility report, the key points to the report file. Each start and sync is assigned a unique migration ID to prevent overwriting reports.

### Compatibility reports
<a name="s3-tables-migrate-compatibility-reports"></a>

#### Table compatibility report
<a name="s3-tables-migrate-table-compatibility-report"></a>

The table compatibility report shows whether your table can be migrated and what happens to each column. The report is a single CSV file with a header row. Each row is one finding and has the following columns:


| Column | Description | 
| --- | --- | 
| finding\_type | Whether the finding prevents the migration, such as invalid for an unsupported file format, or is informational, such as for a column whose data type widens. | 
| finding\_category | The kind of issue: access for permissions, metadata for your table definition, data for values such as partition values, or internal for an error in S3 Tables. | 
| finding\_subcategory | The check that found an issue, such as glueTableLocation, or a column's data type change, such as schemaTransformation.widened. | 
| details | A JSON object. For an issue, findingDescription explains how to resolve the issue. For a column, details shows the column path, the AWS Glue data type, the data type in the sample object, the destination data type, whether the column is a partition column, the policy that applies, and what happens to the column (outcome). | 

For example:


| `finding_type` | `finding_category` | `finding_subcategory` | `details` | 
| --- | --- | --- | --- | 
| invalid | metadata | glueTableParameters | {"findingDescription":"one or more unsupported Hive Parameters entries were detected (see details.unsupportedKeys); transactional (ACID) tables ... are not supported; fix the table definition before migrating","violations":["transactional=true"],"unsupportedKeys":["transactional=true"]} | 
| informational | metadata | schemaTransformation.widened | {"findingDescription":"the field migrates from the AWS Glue type to its destination type","fName":"quantity","fId":2,"sourceType":"smallint","sampleFileType":null,"destinationType":"int","partitionField":false} | 
| informational | metadata | schemaInference.sample | {"bucket":"amzn-s3-demo-bucket","key":"orders/dt=2026-01-15/part-0.parquet","versionId":"3HL4kqtJlcpXroDTDmJ.rmSpXd3dIbrHY"} | 

For a column change, `outcome` in `details` shows what happens to the column. The following table shows example values.


| `outcome` | What it means | 
| --- | --- | 
| migrated | The column is migrated. | 
| nullForFile | The column is written as null in each source object whose values can't be converted, because incompatibleValuesPolicy is setNull. | 
| dropped | The column isn't migrated, because unmatchedSourceFieldsPolicy is drop. | 
| fail | The column prevents the migration. | 
| excluded | The migration job leaves the column out under every migration policy, such as an index column that pandas wrote. | 

#### Object compatibility report
<a name="s3-tables-migrate-object-compatibility-report"></a>

The object compatibility report's manifest lists the report files and their columns. The report files are CSV files without a header row, with one row for each source object that planning scanned. The number of rows equals `objectsScanned`, and the number of rows for planned objects equals `objectsPlanned`.

The report has the following columns:


| Column | Description | 
| --- | --- | 
| bucket | The source bucket. | 
| key | The object key. | 
| version\_id | The version ID. Empty for an unversioned object. | 
| status | Whether planning included the object in the migration, for example planned. | 
| finding\_type | invalid if the issue prevents migration, or informational if it doesn't. | 
| finding\_category | The kind of issue, such as metadata for an object property. Empty if the object has no issue. | 
| finding\_subcategory | The check that found the issue, such as storageClass, or the reason that the object isn't in the migration. | 
| result\_message | A JSON object with the object's size, last modified date, ETag, storage class, encryption type, and AWS KMS key ARN, and a message that describes the issue and how to resolve it. | 

### Object migration report
<a name="s3-tables-migrate-object-migration-report"></a>

The object migration report's manifest lists each results file, its checksum, the report schema, and the number of objects that migrated and failed. Each results file is a CSV file without a header row, with one row for each source object that migration attempted.

The report has the following columns:


| Column | Description | 
| --- | --- | 
| bucket | The source bucket. | 
| key | The object key. | 
| version\_id | The version ID. Empty for an unversioned object. | 
| status | Whether the object migrated or failed, for example migrated. | 
| http\_status\_code | An HTTP status code for the object, such as 200 for a migrated object, or 500 for a failed object that can succeed if you run another sync. | 
| error\_code | The error code for a failed object, such as sourceAccessDenied or schemaIncompatible. Empty for a migrated object. | 
| result\_message | A JSON message detailing the transformations that migration applied to the object, such as values that were widened or written as null, or columns that were dropped. For a failed object, the message explains why it failed and how to fix it. | 