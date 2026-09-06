

# Offline store
<a name="feature-store-storage-configurations-offline-store"></a>

The offline store is used for historical data when sub-second retrieval is not needed. It is typically used for data exploration, model training, and batch inference. 

When you enable both the online and offline stores for your feature group, both stores sync to avoid discrepancies between training and serving data. Please note that an online store feature group with the `InMemory` storage type enabled does not currently support a corresponding feature group in the offline store (no online to offline replication). For more information about ML model serving in Amazon SageMaker Feature Store, see [Online store](feature-store-storage-configurations-online-store.md).

The offline store contains the following `TableFormat` options. For information about the offline store contents, see [`OfflineStoreConfig`](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_OfflineStoreConfig.html) in the Amazon SageMaker API Reference.

## Glue table format
<a name="feature-store-storage-configurations-offline-store-glue-table-format"></a>

The `Glue` format (default) is a standard Hive type table format for AWS Glue. With AWS Glue, you can discover, prepare, move, and integrate data from multiple sources. It also includes additional productivity and data ops tooling for authoring, running jobs, and implementing business workflows. For more information about AWS Glue, see [What is AWS Glue?](https://docs.aws.amazon.com/glue/latest/dg/what-is-glue.html).

## Iceberg table format
<a name="feature-store-storage-configurations-offline-store-iceberg-table-format"></a>

The `Iceberg` format (recommended) is an open table format for very large analytic tables. With `Iceberg`, you can compact the small data files into fewer large files in the partition, resulting in significantly faster queries. This compaction operation is concurrent and does not affect ongoing read and write operations on the feature group. For more information about optimizing Iceberg tables, see the [Amazon Athena](https://docs.aws.amazon.com/athena/latest/ug/querying-iceberg-data-optimization.html) and [AWS Lake Formation](https://docs.aws.amazon.com/lake-formation/latest/dg/data-compaction.html) user guides.

`Iceberg` manages large collections of files as tables and supports modern analytical data lake operations. If you choose the `Iceberg` option when creating new feature groups, Amazon SageMaker Feature Store creates the `Iceberg` tables using Parquet file format, and registers the tables with the AWS Glue Data Catalog. For more information about `Iceberg` table formats, see [Using Apache Iceberg tables](https://docs.aws.amazon.com/athena/latest/ug/querying-iceberg.html). 

**Important**  
Note that for feature groups in `Iceberg` table format, you must specify `String` as the feature type for the event time. If you specify any other type, you can't create the feature group successfully.