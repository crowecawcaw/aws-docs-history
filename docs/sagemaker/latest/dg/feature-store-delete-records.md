# Delete records from your feature groups

You can use the Amazon SageMaker Feature Store API to delete records from your feature groups. A feature group is
an object that contains your machine learning (ML) data, where the columns of your data are
described by features and your data are contained in records. A record contains values for
features that are associated with a specific record identifier.

There are two storage configurations for your feature groups: online store and offline store.
The online store only keeps the record with the latest event time and is typically used for
real-time lookup for ML inference. The offline store keeps all records and acts as a historical
database and is typically used for feature exploration, ML training, and batch inference.

For more information on Feature Store concepts, see [Ingestion diagrams](feature-store-concepts.md#feature-store-concepts-ingestion "feature-store-concepts.md#feature-store-concepts-ingestion").

There are two ways to delete records from your feature groups, and the behavior is different
depending on the storage configuration. In the following topics we will describe how to soft and
hard delete records from the online and offline stores and provide examples.

###### Topics

- [Delete records from the online
  store](#feature-store-delete-records-online-store "#feature-store-delete-records-online-store")
- [Delete records from the offline
  store](#feature-store-delete-records-offline-store "#feature-store-delete-records-offline-store")

## Delete records from the online

store

You can soft or hard delete a record from the online store using the
`DeleteRecord` API by using the `DeletionMode` request parameter to
specify `SoftDelete` (default) or `HardDelete`. For more information on the
`DeleteRecord` API, see [`DeleteRecord`](../APIReference/API_feature_store_DeleteRecord.md "../APIReference/API_feature_store_DeleteRecord.md") in the Amazon SageMaker API Reference.

With the online store:

- When you soft delete (default), the record is no longer retrievable by GetRecord or
  BatchGetRecord and the feature column values are set to `null`, except for the
  `RecordIdentifer` and `EventTime` feature values.
- When you hard delete, the record is completely removed from the online store.

In both cases Feature Store appends the deleted record marker to the `OfflineStore`. The
deleted record marker is a record with the same `RecordIdentifer` as the original, but
with `is_deleted` value set to `True`, `EventTime` set to the
delete input `EventTime`, and other feature values set to `null`.

Note that the `EventTime` specified in `DeleteRecord` should be set
later than the `EventTime` of the existing record in the `OnlineStore` for
that same `RecordIdentifer`. If it is not, the deletion does not occur:

- For `SoftDelete`, the existing (not deleted) record remains in the
  `OnlineStore`, though the delete record marker is still written to the
  `OfflineStore`.
- `HardDelete` returns `EventTime`: `400
ValidationException` to indicate that the delete operation failed. No delete record
  marker is written to the `OfflineStore`.

The following examples use the SDK for Python (Boto3) [`delete_record`](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker-featurestore-runtime/client/delete_record.html#delete-record "https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker-featurestore-runtime/client/delete_record.html#delete-record") operation to delete a record from a feature group. To
delete a record from a feature group, you will need:

- Feature group name (`feature-group-name`)
- Record identifier value as a string
  (`record-identifier-value`)
- Deletion event time (`deletion-event-time`)

The deletion event time should be later than the event time of the record you wish to
delete.

### Online store soft delete

example

For soft delete you will need use the `DeleteRecord` API and can use the default
`DeletionMode` or set the `DeletionMode` to `SoftDelete`.

```
import boto3
client = boto3.client('sagemaker-featurestore-runtime')

client.delete_record(
    FeatureGroupName='`feature-group-name`',
    RecordIdentifierValueAsString='`record-identifier-value`',
    EventTime='`deletion-event-time`',
    TargetStores=[
        'OnlineStore',
    ],
    DeletionMode='SoftDelete'
)
```

### Online store hard delete

example

For hard delete you will need use the `DeleteRecord` API and set the
`DeletionMode` to `HardDelete`.

```
import boto3
client = boto3.client('sagemaker-featurestore-runtime')

client.delete_record(
    FeatureGroupName='`feature-group-name`',
    RecordIdentifierValueAsString='`record-identifier-value`',
    EventTime='`deletion-event-timestamp`',
    TargetStores=[
        'OnlineStore',
    ],
    DeletionMode='HardDelete'
)
```

## Delete records from the offline

store

With Amazon SageMaker Feature Store you can soft and hard delete a record from the `OfflineStore`
Iceberg table format. With the `OfflineStore` Iceberg table format:

- When you soft delete a record the latest version of the Iceberg table file will not
  contain the record, but previous versions will still contain the record and can be accessed
  using time travel. For information on time travel, see [Querying Iceberg table data and
  performing time travel](../../../athena/latest/ug/querying-iceberg-table-data.md "../../../athena/latest/ug/querying-iceberg-table-data.md") in the Athena user guide.
- When you hard delete a record you are removing previous versions of the Iceberg table that
  contain the record. In this case you should specify which versions of the Iceberg table you
  wish to delete.

### Obtain your

Iceberg table name

To soft and hard delete from your `OfflineStore` Iceberg table, you will need to
obtain your Iceberg table name, `iceberg-table-name`. The
following instructions assumes you have already used Feature Store to create a feature group using the
offline store storage configuration using the Iceberg table format, with
`DisableGlueTableCreation = False` (default). For more information on creating
feature groups, see [Get started with Amazon SageMaker Feature Store](feature-store-getting-started.md "feature-store-getting-started.md").

To obtain your `iceberg-table-name`, use the [`DescribeFeatureGroup`](../APIReference/API_DescribeFeatureGroup.html.md "../APIReference/API_DescribeFeatureGroup.html.md") API to obtain [`DataCatalogConfig`](../APIReference/API_DataCatalogConfig.md "../APIReference/API_DataCatalogConfig.md"). This contains the metadata of the Glue table which
serves as data catalog for the `OfflineStore`. The `TableName` within the
`DataCatalogConfig` is your
`iceberg-table-name`.

### Amazon Athena offline store soft

and hard delete example

The following instructions use Amazon Athena to soft delete then hard delete a record from the
`OfflineStore` Iceberg table. This assumes that the record you intend to delete in
your `OfflineStore` is a deleted record marker. For information on the deleted record
marker in your `OfflineStore`, see [Delete records from the online
store](#feature-store-delete-records-online-store "#feature-store-delete-records-online-store").

1. Obtain your Iceberg table name,
   `iceberg-table-name`. For information on how to obtain
   your Iceberg table name, see [Obtain your
   Iceberg table name](#feature-store-delete-records-offline-store-get-iceberg-table-name "#feature-store-delete-records-offline-store-get-iceberg-table-name").
2. Run the `DELETE` command to soft delete the records on the
   `OfflineStore`, such that the latest version (or snapshot) of the Iceberg table
   will not contain the records. The following example deletes the records where
   `is_deleted` is `'True'` and the previous event-time versions of the
   those records .You may add additional conditions based on other features to restrict the
   deletion. For more information on using `DELETE` with Athena, see
   `DELETE` in the Athena user guide.

```
DELETE FROM `iceberg-table-name` WHERE `record-id-feature-name` IS IN ( SELECT `record-id-feature-name` FROM `iceberg-table-name` WHERE is_deleted = 'True')
```

The soft deleted records are still viewable on previous file versions by performing time
travel. For information on performing time travel, see [Querying Iceberg table data and
performing time travel](../../../athena/latest/ug/querying-iceberg-table-data.md "../../../athena/latest/ug/querying-iceberg-table-data.md") in the Athena user guide. 3. Remove the record from previous versions of your Iceberg tables to hard delete the record
from `OfflineStore`:

    1. Run the `OPTIMIZE` command to rewrite the data files into a more optimized
     layout, based on their size and number of associated delete files. For more information on
     optimizing Iceberg tables and the syntax, see [Optimizing Iceberg
     tables](../../../athena/latest/ug/querying-iceberg-data-optimization.md "../../../athena/latest/ug/querying-iceberg-data-optimization.md") in the Athena user guide.



    ```
    OPTIMIZE `iceberg-table-name` REWRITE DATA USING BIN_PACK
    ```
    2. (Optional, only need to run once) Run the `ALTER TABLE` command to alter the
     Iceberg table set values, and set when previous file versions are to be hard deleted
     according to your specifications. This can be done by assigning values to
     `vacuum_min_snapshots_to_keep` and `vacuum_max_snapshot_age_seconds`
     properties. For more information on altering your Iceberg table set properties, see [ALTER TABLE SET PROPERTIES](../../../athena/latest/ug/querying-iceberg-managing-tables.md#querying-iceberg-alter-table-set-properties "../../../athena/latest/ug/querying-iceberg-managing-tables.md#querying-iceberg-alter-table-set-properties") in the Athena user guide. For more information on
     Iceberg table property key-value pairs, see [Table properties](../../../athena/latest/ug/querying-iceberg-creating-tables.md#querying-iceberg-table-properties "../../../athena/latest/ug/querying-iceberg-creating-tables.md#querying-iceberg-table-properties") in the Athena user guide.



    ```
    ALTER TABLE `iceberg-table-name` SET TBLPROPERTIES (
      'vacuum_min_snapshots_to_keep'='`your-specified-value`',
      'vacuum_max_snapshot_age_seconds'='`your-specified-value`'
    )
    ```
    3. Run the `VACUUM` command to remove no longer needed data files for your
     Iceberg tables, not referenced by the current version. The `VACUUM` command
     should run after the deleted record is no longer referenced in the current snapshot. For
     example, `vacuum_max_snapshot_age_seconds` after the deletion. For more
     information on `VACUUM` with Athena and the syntax, see [`VACUUM`](../../../athena/latest/ug/vacuum-statement.md "../../../athena/latest/ug/vacuum-statement.md").



    ```
    VACUUM `iceberg-table-name`
    ```

### Apache Spark offline store

soft and hard delete example

To soft and then hard delete a record from the `OfflineStore` Iceberg table
using Apache Spark, you can follow the same instructions as in the [Amazon Athena offline store soft
and hard delete example](#feature-store-delete-records-offline-store-athena "#feature-store-delete-records-offline-store-athena") above, but using Spark
procedures. For a full list of procedures, see [Spark Procedures](https://iceberg.apache.org/docs/1.3.1/spark-procedures/ "https://iceberg.apache.org/docs/1.3.1/spark-procedures/") in the
Apache Iceberg documentation.

- When soft deleting from the `OfflineStore`: instead of using the
  `DELETE` command in Athena, use the [`DELETE
FROM`](https://iceberg.apache.org/docs/latest/spark-writes/#delete-from "https://iceberg.apache.org/docs/latest/spark-writes/#delete-from") command in Apache Spark.
- To remove the record from previous versions of your Iceberg tables to hard delete the
  record from `OfflineStore`:
  - When changing your Iceberg table configuration: instead of using the `ALTER
TABLE` command from Athena, use [`expire_snapshots`](https://iceberg.apache.org/docs/1.3.1/spark-procedures/#expire_snapshots "https://iceberg.apache.org/docs/1.3.1/spark-procedures/#expire_snapshots") procedure.
  - To remove no longer needed data files from your Iceberg tables: instead of using the
    `VACUUM` command in Athena, use the [`remove_orphan_files`](https://iceberg.apache.org/docs/1.3.1/spark-procedures/#remove_orphan_files "https://iceberg.apache.org/docs/1.3.1/spark-procedures/#remove_orphan_files") procedure.
