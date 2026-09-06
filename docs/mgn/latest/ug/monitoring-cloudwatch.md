

NEW - You can now accelerate your migration and modernization with AWS Transform. Read [Getting Started](https://docs.aws.amazon.com/transform/latest/userguide/getting-started.html) in the *AWS Transform User Guide*.

# Monitoring Application Migration Service with Amazon CloudWatch
<a name="monitoring-cloudwatch"></a>

You can monitor AWS Transform MGN using CloudWatch, which collects raw data and processes it into readable, near real-time metrics. These statistics are kept for 15 months, so that you can access historical information and gain a better perspective on how your web application or service is performing. You can also set alarms that watch for certain thresholds, and send notifications or take actions when those thresholds are met. For more information, see the [Amazon CloudWatch User Guide](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/).

AWS Transform MGN supports six CloudWatch metrics in the AWS/MGN namespace. 

AWS Transform MGN includes the following metrics across all Source servers. The following metrics are dimensionless. 


| Metric name | Description | 
| --- | --- | 
| ActiveSourceServerCount | Number of Source servers that are not archived. | 
| TotalSourceServerCount | Number of source servers, including those that are archived. | 

AWS Transform MGN includes the following metrics by individual source server. The following metrics have a single dimension: **SourceServerID. **


| Metric name | Description | 
| --- | --- | 
| LagDuration | The amount of time that has passed since the last consistent snapshot. | 
| Backlog | The amount of data yet to be synced. | 
| DurationSinceLastTest | The amount of time that has passed since the last Test instance launch. | 
| ElapsedReplicationDuration | The cumulative amount of time this server has been replicating for (from which billing information is derived). | 