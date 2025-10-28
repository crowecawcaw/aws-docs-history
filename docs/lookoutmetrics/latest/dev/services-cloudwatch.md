Amazon Lookout for Metrics is no longer available to new customers. Existing Amazon Lookout for Metrics customers will be able to use the service until September 12, 2025, when we will end support for Amazon Lookout for Metrics. To help transition off of Amazon Lookout for Metrics, please read [Transitioning off Amazon Lookout for Metrics](https://aws.amazon.com/blogs/machine-learning/transitioning-off-amazon-lookout-for-metrics/ "https://aws.amazon.com/blogs/machine-learning/transitioning-off-amazon-lookout-for-metrics/").

# Using Amazon CloudWatch with Lookout for Metrics

You can use Amazon CloudWatch metrics as a datasource for an Amazon Lookout for Metrics detector. Most AWS services
send metrics to CloudWatch automatically when you use them. You can create a dataset from these
metrics, or from metrics that you send to CloudWatch. You can send metrics to CloudWatch from your
application code, or from software such as [StatsD](../../../AmazonCloudWatch/latest/monitoring/CloudWatch-Agent-custom-metrics-statsd.md "../../../AmazonCloudWatch/latest/monitoring/CloudWatch-Agent-custom-metrics-statsd.md") or [collectd](../../../AmazonCloudWatch/latest/monitoring/CloudWatch-Agent-custom-metrics-collectd.md "../../../AmazonCloudWatch/latest/monitoring/CloudWatch-Agent-custom-metrics-collectd.md").

###### Topics

- [Adding a CloudWatch datasource](#services-cloudwatch-datasource "#services-cloudwatch-datasource")
- [Training a detector with a CloudWatch
  datasource](#services-cloudwatch-training "#services-cloudwatch-training")
- [Running a backtest](#services-cw-backtest "#services-cw-backtest")

## Adding a CloudWatch datasource

In CloudWatch, a metric can have a name and value, and optionally can also have a dimension name
and dimension value. For example, Amazon EC2 has a metric named `CPUUtilization` with a
value that is a number between 0 and 100, and a dimension named `InstanceId` that
has the unique ID of an instance.

###### To create a CloudWatch dataset

1. Open the [Lookout for Metrics console Detectors](https://console.aws.amazon.com/lookoutmetrics/home#detectors "https://console.aws.amazon.com/lookoutmetrics/home#detectors") page.
2. Choose a detector.
3. Choose **Add dataset**.
4. For **Datasource**, choose **CloudWatch**.
5. Follow the instructions to create the datasource.

To configure metrics in Lookout for Metrics, you choose a CloudWatch namespace and dimension first, and then
choose one or more CloudWatch metrics to be measures for the dataset. For CloudWatch metrics that apply to
all resources in an AWS Region, or otherwise don't have a dimension in CloudWatch, you set
**Dimensions** to **None**.

For example, in AWS Lambda you can monitor concurrency by function, by resource (function
version or alias), or across all functions in a Region. If you choose
`ConcurrentExecutions` as a measure and `Function Name` as a
dimension, then the detector monitors _concurrency for function-a_ and
_concurrency for function-b_ as two Lookout for Metrics metrics.

The detector reads new data from CloudWatch periodically, by reading the values of metrics that
occur in each interval. It aggregates the values of each metric for the interval and looks for
anomalies. It records anomalies and sends [anomaly
alerts](detectors-alerts.md "detectors-alerts.md"), if configured.

When you activate the detector, it uses data from several intervals to learn, before attempting to find anomalies.
For a five minute interval, the training process takes approximately one day. Training time varies
[depending on the detector's interval](gettingstarted-quotas.md#gettingstarted-quotas-coldstart "gettingstarted-quotas.md#gettingstarted-quotas-coldstart").

When you add a CloudWatch dataset to your detector, the Lookout for Metrics console creates a [service role](permissions-service.md "permissions-service.md") with permission to read metrics.

###### Sections

- [Training a detector with a CloudWatch
  datasource](#services-cloudwatch-training "#services-cloudwatch-training")
- [Running a backtest](#services-cw-backtest "#services-cw-backtest")

## Training a detector with a CloudWatch

datasource

When using a CloudWatch datasource, the following number of days are used to train a
detector:

- **5 minute interval** - 10.42 days
- **10 minute interval** - 20.48 days
- **1 hour interval** - 125 days
- **1 day interval** - 455 days

For example, if a datasource has a 5 minute interval, data from the previous 10.42 days will
be used to train a detector. If the datasource contains fewer than 10.42 days of data, a detector
will be trained using the available data.

The datasource must meet the [minumum data
requirements](gettingstarted-quotas.md#gettingstarted-quotas-backtest "gettingstarted-quotas.md#gettingstarted-quotas-backtest") in order to train a detector.

## Running a backtest

In backtest mode, a detector uses historical data to learn and find anomalies. You provide
recent data for a large number of intervals at a single path. In backtest mode, Lookout for Metrics splits
historical data into two subsets. 70 percent of the data is used to train the detector. The
detector then analyzes the other 30 percent to identify anomalies. You can use test mode to
validate the detector's results and verify its accuracy.

When using a CloudWatch datasource, the following number of days are used to train a detector:

- **5 minute interval** - 10.42 days
- **10 minute interval** - 20.48 days
- **1 hour interval** - 125 days
- **1 day interval** - 455 days

For example, if a datasource has a 5 minute interval, data from the previous 10.42 days will be used to train
a detector. If the datasource contains fewer than 10.42 days of data, a detector will be trained using the
available data. The Cloudwatch metrics must be present in at least 285 intervals worth of data, but not more than
3000 intervals worth of data. This gives the detector at least 200 intervals of data to learn with. The detector
always uses older data for learning and newer data for testing.
