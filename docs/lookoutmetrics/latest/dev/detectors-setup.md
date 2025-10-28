Amazon Lookout for Metrics is no longer available to new customers. Existing Amazon Lookout for Metrics customers will be able to use the service until September 12, 2025, when we will end support for Amazon Lookout for Metrics. To help transition off of Amazon Lookout for Metrics, please read [Transitioning off Amazon Lookout for Metrics](https://aws.amazon.com/blogs/machine-learning/transitioning-off-amazon-lookout-for-metrics/ "https://aws.amazon.com/blogs/machine-learning/transitioning-off-amazon-lookout-for-metrics/").

# Setting up a detector

An _anomaly detector_ is an Amazon Lookout for Metrics resource that
monitors a dataset to find anomalies.

By default, detectors use a key managed by Lookout for Metrics. To use a key that you manage in your own
account, [create a symmetric key in AWS KMS](../../../kms/latest/developerguide/create-keys.md "../../../kms/latest/developerguide/create-keys.md") and
grant Lookout for Metrics permission to use it.

###### Topics

- [Creating a detector](#detectors-create "#detectors-create")
- [Creating a dataset](#dataset-create "#dataset-create")

## Creating a detector

To create a detector, you provide a name, description, and interval. To start the detector
and begin finding anomalies, add a dataset and notifications and activate the detector.

###### To create a detector

1. Open the [Lookout for Metrics console Detectors](https://console.aws.amazon.com/lookoutmetrics/home#detectors "https://console.aws.amazon.com/lookoutmetrics/home#detectors") page.
2. Choose **Create detector**.
3. Provide the following information:.

######

    * **Name** – A name for the detector.
    * **Description** – A description of the
     detector.
    * **Interval** – The amount of time between
     attempts to detect anomalies.

4. (Optional) Lookout for Metrics encrypts all imported data with an AWS Key Management Service (AWS KMS) key. To choose
   an encryption key, select **Customize encryption settings**. You can't
   change the encryption key later.
5. Choose **Create**.

### Detector Statuses

After creating a detector, Lookout for Metrics initializes the detector, uses data for training, and
activates the detector so that it can begin identifying anomalies. When you create a detector,
Lookout for Metrics displays the following statuses:

1. **Initializing** - Lookout for Metrics begins initializing your anomaly
   detector based on your datasource, measure, and dimension configurations. It also ingests
   all historical data that you provided.
2. **Learning** - After initialization, the detector begins
   learning by ingesting continuous data. Learning time varies depending on the detector's
   interval setting and whether you provided historical data.
3. **Active** - After the detector has ingested a sufficient
   amount of data, the status changes to **Active**”and the detector begins
   identifying anomalies.

Lookout for Metrics usually requires at least 300 cumulative data points before a detector's status
changes to **Active**. For example, if you provide 200 data points of
historical data, the detector need to ingest 100 data points of continuous data before it is
active. For the daily time interval, the detector's status changes to
**Active** after 14 days of learning.

If no historical data is available, the learning stage takes the following amount of time:

- **5-minute interval**: 25 hours
- **10-minute interval**: 50 hours
- **1-hour interval**: 12.5 days
- **Daily interval**: 14 days

If you are backtesting, also refer to the [backtesting data requirements](gettingstarted-quotas.md#gettingstarted-quotas-backtest "gettingstarted-quotas.md#gettingstarted-quotas-backtest").

## Creating a dataset

A detector imports data from a datasource, transforms it, and stores it in a dataset. The
datasource can be an Amazon Simple Storage Service (Amazon S3) bucket that you store data in, a database, or another
AWS service that Lookout for Metrics supports.

###### Note

To communicate with other services, Lookout for Metrics needs permissions from an AWS Identity and Access Management (IAM)
service role. When you use the console to configure a dataset, you can create a new service
role or choose an existing one.

For more information, see [Service roles for Amazon Lookout for Metrics](permissions-service.md "permissions-service.md").

###### To create a dataset

1. Open the [Lookout for Metrics console Detectors](https://console.aws.amazon.com/lookoutmetrics/home#detectors "https://console.aws.amazon.com/lookoutmetrics/home#detectors") page.
2. Choose a detector.
3. Choose **Create dataset**.
4. Provide the following information:

######

    * **Name** – A name for the dataset.
    * **Description** – A description of the
     dataset.
    * **Timezone** – The timezone where the data is
     generated. When a detector analyzes data, it verifies that each data point falls
     within the current interval.

5. Choose a datasource. The datasource can be an Amazon S3 bucket, an AWS service that Lookout for Metrics
   supports, or a database.
6. Configure the datasource and then choose **Next**. Options vary
   depending on the datasource that you choose. Common settings include the following:
   - **Interval** – The amount of time between
     analysis attempts. Use the same setting as the detector's interval.
   - **Offset** – The minimum number of seconds
     that the detector waits at the end of each interval before accessing data. Using an
     offset is supported only for Amazon S3, Amazon Redshift, and Athena datasources.
   - **Permissions** – A [service role](permissions-service.md "permissions-service.md") that gives Lookout for Metrics permission to
     access either the datasource or a secret that contains credentials for the
     datasource.

7. Provide the metrics that the detector analyzes:
   - **Measures** – The primary metrics that the
     detector analyzes to find anomalies.
   - **Dimensions** – The secondary metrics, which
     segment the data by, for example, location or demographic.
   - **Timestamp** – The metric that specifies when
     the data point was created.

8. Choose **Next**.
9. Choose **Save and activate**.

To get started with Amazon S3 as a datasource, see [Managing a dataset in Amazon S3](detectors-dataset.md "detectors-dataset.md"). For other datasources, see [Using Amazon Lookout for Metrics with other services](lookoutmetrics-services.md "lookoutmetrics-services.md").
