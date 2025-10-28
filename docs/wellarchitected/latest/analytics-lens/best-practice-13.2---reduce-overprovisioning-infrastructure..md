# Best practice 13.2 – Continuously evaluate your provisioned resources and identify overprovisioned workloads

Workload resource utilization can change over time,
especially with the growth of data or after process
optimization has occurred. Your organization should review
resource usage patterns and determine if you require the
same infrastructure footprint to meet your business goals.

## Suggestion 13.2.1 – Evaluate whether compute resources can be downsized

Investigate your resource utilization by inspecting the
metrics provided by Amazon CloudWatch. Evaluate whether
the resources can be downsized to one-level smaller within
the same instance class. For example, reduce Amazon EMR
cluster nodes from m5.16xlarge to m5.12xlarge, or the
number of instances that make up the cluster.

## Suggestion 13.2.2 – Move infrequently used data out of a data warehouse into a data lake

Data that is infrequently used can be moved from the data
warehouse into the data lake. From there, the data can be
queried in place or joined with data in the warehouse. Use
services such as Amazon Redshift Spectrum to query and
join data in the Amazon S3 data lake, or Amazon Athena to
query data at rest in Amazon S3.

## Suggestion 13.2.3 – Merge low utilization infrastructure resources

If you have several workloads that all have
low-utilization resources, determine if you can combine
those workloads to run on shared infrastructure. In many
cases, using a pooled resource model for analytics
workloads will save on infrastructure costs.

## Suggestion 13.2.4 – Move infrequently accessed data into low-cost storage tiers

When designing a data lake or data analytics project,
consider required access patterns, transaction
concurrency, and acceptable transaction latency. These
will inﬂuence where data is stored. It is equally
important to consider how often data will be accessed.
Have a data lifecycle plan to migrate data tiers from
hotter storage to colder, less-expensive storage, while
still meeting all business objectives.

Transitioning between storage tiers is achieved using
Amazon S3 Lifecycle policies. These automatically
transition objects into another tier with lower cost, and
will even delete expired data. Amazon S3
Intelligent-Tiering will analyze the data access patterns
and automatically move objects between tiers.

## Suggestion 13.2.5 – Move to serverless when you don't need always-on infrastructure

For analytics workloads that have intermittent or unpredictable usage patterns, moving to AWS serverless can provide significant cost savings compared to provisioned servers. AWS serverless analytics services like Amazon Athena, EMR Serverless, and Amazon Redshift Serverless are great options that provide on-demand access without having to provision always-on resources. These services automatically start up when needed and shut down when not in use so you don't have to pay for idle capacity.

For example, with Amazon Redshift Serverless, you pay for compute only when the data warehouse is in use. By using Amazon Redshift Serverless for tasks such as loading data and leveraging Amazon Redshift data sharing, you can scale down your main cluster and still maintain the same performance for end users.

For more detail, refer to the following:

- [Easy analytics and cost optimization with Amazon Redshift Serverless](https://aws.amazon.com/blogs/big-data/easy-analytics-and-cost-optimization-with-amazon-redshift-serverless/ "https://aws.amazon.com/blogs/big-data/easy-analytics-and-cost-optimization-with-amazon-redshift-serverless/")
- [Amazon EMR Serverless cost estimator](https://aws.amazon.com/blogs/big-data/amazon-emr-serverless-cost-estimator/ "https://aws.amazon.com/blogs/big-data/amazon-emr-serverless-cost-estimator/")
- [Run queries 3x faster with up to 70% cost savings on the latest Amazon Athena engine](https://aws.amazon.com/blogs/big-data/run-queries-3x-faster-with-up-to-70-cost-savings-on-the-latest-amazon-athena-engine/ "https://aws.amazon.com/blogs/big-data/run-queries-3x-faster-with-up-to-70-cost-savings-on-the-latest-amazon-athena-engine/")
