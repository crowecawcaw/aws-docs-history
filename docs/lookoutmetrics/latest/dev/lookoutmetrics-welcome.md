Amazon Lookout for Metrics is no longer available to new customers. Existing Amazon Lookout for Metrics customers will be able to use the service until September 12, 2025, when we will end support for Amazon Lookout for Metrics. To help transition off of Amazon Lookout for Metrics, please read [Transitioning off Amazon Lookout for Metrics](https://aws.amazon.com/blogs/machine-learning/transitioning-off-amazon-lookout-for-metrics/ "https://aws.amazon.com/blogs/machine-learning/transitioning-off-amazon-lookout-for-metrics/").

# What is Amazon Lookout for Metrics?

Amazon Lookout for Metrics is a service that finds anomalies in your data, determines their root causes, and enables you to
quickly take action. Built from the same technology used by Amazon.com, Amazon Lookout for Metrics reﬂects 20 years of expertise in
anomaly detection and machine learning.

In Lookout for Metrics, you create detectors that monitor data to find anomalies. You configure the detector with a datasource
and choose the values that it monitors (the dataset's _measures_). The detector can monitor all
values of a measure overall, or use other data to sort measures into groups. For example, you can choose to monitor
the availability of an application worldwide, or use a location field in your data as a
_dimension_ to monitor availability separately in each AWS Region or Availability Zone. Each
combination of measure and dimension value is called a _metric_.

To gain an understanding of your data and better find anomalies, a detector uses your data to learn. When you
create a detector, you choose an interval from between 5 minutes and 1 day, which determines how often the detector
imports data and finds anomalies. Depending on the interval that you choose, a detector spends between a few hours
and a few days learning about your data. To speed up the learning process, you can provide _historical
data_. You can also use historical data to run a detector in backtest mode to see how well it works on
your data.

When Lookout for Metrics finds an anomaly, it gives it a severity score to indicate how unexpected it is, based on the
detector's understanding of your data. When multiple metrics are affected by an anomaly, the detector collects them
in a group. To send anomaly alerts when high severity anomalies occur, you can add alerts to the detector. Alerts
can run a Lambda function or send a notification to an Amazon SNS topic. Anomaly alerts summarize all affected metrics for
an anomaly, which reduces the amount of similar alerts that it sends.

Lookout for Metrics can monitor data from many different domains, stored in many different formats. In addition to monitoring
operational metrics for emergent issues, you can find anomalies in sales data, marketing data, and customer
engagement metrics.

Lookout for Metrics integrates with other services to provide additional datasources and alert channels. Lookout for Metrics supports the
following services as datasources.

######

- [Using Amazon Athena with Lookout for Metrics](services-athena.md "services-athena.md") – Analyze data retrieved by your queries.
- [Amazon S3](services-s3.md "services-s3.md") – Read metrics data from text objects in a bucket. Supports
  using historical data for training and testing a detector.
- [Amazon CloudWatch](services-cloudwatch.md "services-cloudwatch.md") – Analyze CloudWatch metrics sent by an AWS service, AWS
  resource, or an application.
- [Amazon Relational Database Service (Amazon RDS)](services-rds.md "services-rds.md") – Analyze items in a relational database. The
  following database engines are supported:

######

    + **Amazon Aurora**
    + **MySQL**
    + **PostgreSQL**
    + **MariaDB**
    + **Microsoft SQL Server**

- [Amazon Redshift](services-redshift.md "services-redshift.md") – Analyze items in a Amazon Redshift data warehouse.
- [Amazon AppFlow](services-appflow.md "services-appflow.md") – Analyze data flow from a web service with an Amazon AppFlow
  data flow. The following services are supported:

      + **Salesforce**
      + **Marketo**
      + **Dynatrace**
      + **Singular**
      + **Zendesk**
      + **Servicenow**
      + **Infor Nexus**
      + **Trendmicro**
      + **Veeva**
      + **Google Analytics**
      + **Amplitude**

  To get started with Lookout for Metrics and learn more about the service, continue to [Getting started with Lookout for Metrics](lookoutmetrics-gettingstarted.md "lookoutmetrics-gettingstarted.md").
