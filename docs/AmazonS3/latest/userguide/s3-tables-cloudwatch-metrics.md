# Monitoring metrics with Amazon CloudWatch

You can use Amazon CloudWatch metrics to understand the performance of your table buckets. There are several sets of metrics that you can use CloudWatch with S3 Tables.

**Daily storage metrics for tables and table buckets**

Monitor the amount of data stored in tables and table buckets, including total size in bytes and number of files. These metrics track total storage bytes per access tier and file counts at the table bucket, table, and namespace level. Storage metrics for S3 Tables are reported once per day and are provided to all customers at no additional cost.

**Table maintenance metrics**

Monitor automated maintenance operations performed by Amazon S3 on your tables, such as compaction and snapshot expiration. These metrics track the number of bytes and files processed during maintenance activities. Maintenance metrics for S3 Tables are reported once per day and are provided to all customers at no additional cost.

**Request metrics**

Monitor S3 Tables requests to quickly identify and act on operational issues. These CloudWatch metrics can be optionally enabled for individual table buckets. Request metrics are billed at the same rate as Amazon CloudWatch custom metrics. Request metrics include:

- counts of data plane operations (GET, PUT, HEAD, POST)
- bytes transferred
- latency measurements
- error rates

###### Note

**Best-effort CloudWatch metrics delivery**

CloudWatch metrics are delivered on a best-effort basis. Most requests for an Amazon S3 object that have request metrics result in a data point being sent to CloudWatch.

The completeness and timeliness of metrics are not guaranteed. The data point for a particular request might be returned with a timestamp that is later than when the request was actually processed. The data point for a minute might be delayed before being available through CloudWatch, or it might not be delivered at all. CloudWatch request metrics give you an idea of the nature of traffic against your bucket in near-real time. It is not meant to be a complete accounting of all requests. It follows from the best-effort nature of this feature that the reports available at the Billing & Cost Management Dashboard might include one or more access requests that do not appear in the bucket metrics.

For more information, see the following topics.
