Amazon Lookout for Metrics is no longer available to new customers. Existing Amazon Lookout for Metrics customers will be able to use the service until September 12, 2025, when we will end support for Amazon Lookout for Metrics. To help transition off of Amazon Lookout for Metrics, please read [Transitioning off Amazon Lookout for Metrics](https://aws.amazon.com/blogs/machine-learning/transitioning-off-amazon-lookout-for-metrics/ "https://aws.amazon.com/blogs/machine-learning/transitioning-off-amazon-lookout-for-metrics/").

# Using Amazon Athena with Lookout for Metrics

You can use Amazon Athena (Athena) as a datasource for an Amazon Lookout for Metrics detector. With Athena, you can
choose columns to monitor (_measures_) and columns that segment measure
values (_dimensions_). The detector monitors the values in these columns to
find anomalies in your data.

To use an Athena database with Lookout for Metrics, the table must have a timestamp column that is partitioned for queries.
This allows Lookout for Metrics to get records for an interval without scanning the entire table.

If you have a table with a large number of partitions that grows over time, consider using AWS Glue partition
indexing and filtering. AWS Glue partition indexing allows Athena to optimize partition processing and improve
query performance on highly partitioned tables. For more information, see [AWS Glue partition indexing and filtering](../../../athena/latest/ug/glue-best-practices.md#glue-best-practices-partition-index "../../../athena/latest/ug/glue-best-practices.md#glue-best-practices-partition-index").

Partition projection with Amazon Athena is another option that speeds up query processing of highly partitioned
tables. In partition projection, partition values and locations are calculated from configuration rather than read
from a repository like the AWS Glue Data Catalog. For more information, see [Partition projection with Amazon Athena](../../../athena/latest/ug/partition-projection.md "../../../athena/latest/ug/partition-projection.md").

The detector imports data at the end of each interval. You configure an **offset** to allow
time after an interval ends for all data to be written. For example, if you choose an offset of 30 seconds, the
detector waits 30 seconds after the end of each interval before reading data for that interval.

Before you configure the dataset, you need to know the following information.

######

- **Database name** – The name of the database where the source Athena table is kept.
- **Data catalog** – The name of the catalog where the source database is
  kept.
- **Table name** – The name of the table that contains the source
  data.
- **Workgroup name** – The name of the workgroup where the prepared
  statement is saved.
- **Amazon S3 results path** – The name of the Amazon S3 bucket where the Athena
  query results are stored. You can also use the result location that is configured for the workgroup.

###### To create an Athena dataset

1. Open the [Lookout for Metrics console Detectors](https://console.aws.amazon.com/lookoutmetrics/home#detectors "https://console.aws.amazon.com/lookoutmetrics/home#detectors") page.
2. Choose a detector.
3. Choose **Add dataset**.
4. Choose **Amazon Athena**
5. Follow the instructions to create the datasource.
   To configure metrics in Lookout for Metrics, you choose columns to be measures and dimensions. Each measure is a column with a
   numerical value that you want to monitor for anomalies. Each dimension is a column with a string value that segments
   the measure(s). A metric in Lookout for Metrics is a combination of a measure value and a dimension value, aggregated within an
   interval. For example, _average availability in Colorado_, or _maximum temperature in
   furnace 17_.

The detector reads new data from Athena periodically, by getting objects from the folder for
the most recent completed interval. If it detects any anomalies in the metrics for the interval,
it records an anomaly and sends [anomaly alerts](detectors-alerts.md "detectors-alerts.md"), if
configured.

When you activate the detector, it uses data from several intervals to learn, before attempting to find anomalies.
For a five minute interval, the training process takes approximately one day. Training time varies
[depending on the detector's interval](gettingstarted-quotas.md#gettingstarted-quotas-coldstart "gettingstarted-quotas.md#gettingstarted-quotas-coldstart").

For more information about Athena, see [Getting
started with Amazon Athena](../../../athena/latest/ug/GetStartedWithS3.md "../../../athena/latest/ug/GetStartedWithS3.md") in the Amazon Athena User Guide.

###### Sections

- [Configuring permissions](#services-ate-permissions "#services-ate-permissions")
- [Training a detector with an Athena datasource](#services-ate-detector "#services-ate-detector")
- [Running a backtest](#services-ate-backtest "#services-ate-backtest")

## Configuring permissions

When you add an Athena dataset to your detector, the Lookout for Metrics console creates a [service role](permissions-service.md "permissions-service.md") with permission to read data from the bucket through Athena,
and permission to use AWS Key Management Service (AWS KMS) to encrypt and decrypt data.

The console creates a role for the dataset, and a separate role for each alert that you
configure. You can create a single role for the detector that gives it all of the permissions
that it needs. To use a custom role, create an IAM role that Lookout for Metrics has permission to assume,
and add permission to use Athena and AWS KMS.

If you require federated access to call Amazon Athena, you might need to configure your own IAM roles. For more
information, see [Using Amazon Athena Federated Query](../../../athena/latest/ug/connect-to-a-data-source.md "../../../athena/latest/ug/connect-to-a-data-source.md") in the Athena User Guide.

## Training a detector with an Athena datasource

When using an Athena datasource, the following number of days are used to train a detector:

- **5 minute interval** – 10.42 days
- **10 minute interval** – 20.48 days
- **1 hour interval** – 125 days
- **1 day interval** – 455 days

For example, if a datasource has a 5 minute interval, data from the previous 10.42 days is used to train a
detector. If the datasource contains fewer than 10.42 days of data, a detector is trained on all of the available
data.

The datasource must meet the [minimum data requirements](gettingstarted-quotas.md#gettingstarted-quotas-backtest "gettingstarted-quotas.md#gettingstarted-quotas-backtest") in order to trian a detector.

## Running a backtest

In backtest mode, a detector uses historical data to learn and find anomalies. You provide
recent data for a large number of intervals at a single path. In backtest mode, Lookout for Metrics splits
historical data into two subsets. 70 percent of the data is used to train the detector. The
detector then analyzes the other 30 percent to identify anomalies. You can use test mode to
validate the detector's results and verify its accuracy.

For backtest mode, you can provide between 285 and 3000 intervals worth of data. The data
can be in one file or multiple files in the same folder. This gives the detector at least 200
intervals of data to learn with. The detector always uses older data for learning and newer
data for testing.
