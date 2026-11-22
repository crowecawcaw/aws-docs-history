

# Metrics Insights sample queries

This section contains examples of useful CloudWatch Metrics Insights queries that you can copy and use directly or copy and modify in query editor. Some of these examples are already available in the console, and you can access them by choosing **Add query** in the **Metrics** view.

## Application Load Balancer examples
<a name="cloudwatch-metrics-insights-queryexamples-applicationloadbalancer"></a>

**Total requests across all load balancers**

```sql
SELECT SUM(RequestCount) 
FROM SCHEMA("AWS/ApplicationELB", LoadBalancer)
```

**Top 10 most active load balancers **

```sql
SELECT MAX(ActiveConnectionCount) 
FROM SCHEMA("AWS/ApplicationELB", LoadBalancer) 
GROUP BY LoadBalancer 
ORDER BY SUM() DESC 
LIMIT 10
```

## AWS API usage examples
<a name="cloudwatch-metrics-insights-queryexamples-APIusage"></a>

**Top 20 AWS APIs by the number of calls in your account**

```sql
SELECT COUNT(CallCount) 
FROM SCHEMA("AWS/Usage", Class, Resource, Service, Type) 
WHERE Type = 'API' 
GROUP BY Service, Resource 
ORDER BY COUNT() DESC 
LIMIT 20
```

**CloudWatch APIs sorted by calls**

```sql
SELECT COUNT(CallCount) 
FROM SCHEMA("AWS/Usage", Class, Resource, Service, Type) 
WHERE Type = 'API' AND Service = 'CloudWatch' 
GROUP BY Resource 
ORDER BY COUNT() DESC
```

## DynamoDB examples
<a name="cloudwatch-metrics-insights-queryexamples-DynamoDB"></a>

**Top 10 tables by consumed reads**

```sql
SELECT SUM(ProvisionedWriteCapacityUnits)
FROM SCHEMA("AWS/DynamoDB", TableName) 
GROUP BY TableName
ORDER BY MAX() DESC LIMIT 10
```

**Top 10 tables by returned bytes**

```sql
SELECT SUM(ReturnedBytes)
FROM SCHEMA("AWS/DynamoDB", TableName) 
GROUP BY TableName
ORDER BY MAX() DESC LIMIT 10
```

**Top 10 tables by user errors**

```sql
SELECT SUM(UserErrors)
FROM SCHEMA("AWS/DynamoDB", TableName) 
GROUP BY TableName
ORDER BY MAX() DESC LIMIT 10
```

## Amazon Elastic Block Store examples
<a name="cloudwatch-metrics-insights-queryexamples-EBS"></a>

**Top 10 Amazon EBS volumes by bytes written**

```sql
SELECT SUM(VolumeWriteBytes) 
FROM SCHEMA("AWS/EBS", VolumeId) 
GROUP BY VolumeId 
ORDER BY SUM() DESC 
LIMIT 10
```

**Average Amazon EBS volume write time**

```sql
SELECT AVG(VolumeTotalWriteTime) 
FROM SCHEMA("AWS/EBS", VolumeId)
```

## Amazon EC2 examples
<a name="cloudwatch-metrics-insights-queryexamples-EC2"></a>

**CPU utilization of EC2 instances sorted by highest **

```sql
SELECT AVG(CPUUtilization) 
FROM SCHEMA("AWS/EC2", InstanceId) 
GROUP BY InstanceId 
ORDER BY AVG() DESC
```

**Average CPU utilization across the entire fleet**

```sql
SELECT AVG(CPUUtilization) 
FROM SCHEMA("AWS/EC2", InstanceId)
```

**Top 10 instances by highest CPU utilization**

```sql
SELECT MAX(CPUUtilization) 
FROM SCHEMA("AWS/EC2", InstanceId) 
GROUP BY InstanceId 
ORDER BY MAX() DESC 
LIMIT 10
```

**In this case, the CloudWatch agent is collecting a `CPUUtilization` metric per application. This query filters the average of this metric for a specific application name.**

```sql
SELECT AVG(CPUUtilization)
FROM "AWS/CWAgent"
WHERE ApplicationName = 'eCommerce'
```

## Amazon Elastic Container Service examples
<a name="cloudwatch-metrics-insights-queryexamples-ECS"></a>

**Average CPU utilization across all ECS clusters **

```sql
SELECT AVG(CPUUtilization) 
FROM SCHEMA("AWS/ECS", ClusterName)
```

**Top 10 clusters by memory utilization**

```sql
SELECT AVG(MemoryUtilization) 
FROM SCHEMA("AWS/ECS", ClusterName) 
GROUP BY ClusterName 
ORDER BY AVG() DESC
LIMIT 10
```

**Top 10 services by CPU utilization**

```sql
SELECT AVG(CPUUtilization) 
FROM SCHEMA("AWS/ECS", ClusterName, ServiceName) 
GROUP BY ClusterName, ServiceName 
ORDER BY AVG() DESC 
LIMIT 10
```

**Top 10 services by running tasks (Container Insights)**

```sql
SELECT AVG(RunningTaskCount) 
FROM SCHEMA("ECS/ContainerInsights", ClusterName, ServiceName) 
GROUP BY ClusterName, ServiceName 
ORDER BY AVG() DESC 
LIMIT 10
```

## Amazon Elastic Kubernetes Service Container Insights examples
<a name="cloudwatch-metrics-insights-queryexamples-EKSCI"></a>

**Average CPU utilization across all EKS clusters **

```sql
SELECT AVG(pod_cpu_utilization) 
FROM SCHEMA("ContainerInsights", ClusterName)
```

**Top 10 clusters by node CPU utilization**

```sql
SELECT AVG(node_cpu_utilization) 
FROM SCHEMA("ContainerInsights", ClusterName) 
GROUP BY ClusterName
ORDER BY AVG() DESC LIMIT 10
```

**Top 10 clusters by pod memory utilization**

```sql
SELECT AVG(pod_memory_utilization) 
FROM SCHEMA("ContainerInsights", ClusterName) 
GROUP BY ClusterName
ORDER BY AVG() DESC LIMIT 10
```

**Top 10 nodes by CPU utilization**

```sql
SELECT AVG(node_cpu_utilization) 
FROM SCHEMA("ContainerInsights", ClusterName, NodeName) 
GROUP BY ClusterName, NodeName 
ORDER BY AVG() DESC LIMIT 10
```

**Top 10 pods by memory utilization**

```sql
SELECT AVG(pod_memory_utilization) 
FROM SCHEMA("ContainerInsights", ClusterName, PodName) 
GROUP BY ClusterName, PodName 
ORDER BY AVG() DESC LIMIT 10
```

## EventBridge examples
<a name="cloudwatch-metrics-insights-queryexamples-EventBridge"></a>

**Top 10 rules by invocations**

```sql
SELECT SUM(Invocations)
FROM SCHEMA("AWS/Events", RuleName) 
GROUP BY RuleName
ORDER BY MAX() DESC LIMIT 10
```

**Top 10 rules by failed invocations**

```sql
SELECT SUM(FailedInvocations)
FROM SCHEMA("AWS/Events", RuleName) 
GROUP BY RuleName
ORDER BY MAX() DESC LIMIT 10
```

**Top 10 rules by matched rules**

```sql
SELECT SUM(MatchedEvents)
FROM SCHEMA("AWS/Events", RuleName) 
GROUP BY RuleName
ORDER BY MAX() DESC LIMIT 10
```

## Kinesis examples
<a name="cloudwatch-metrics-insights-queryexamples-Kinesis"></a>

**Top 10 streams by bytes written**

```sql
SELECT SUM("PutRecords.Bytes") 
FROM SCHEMA("AWS/Kinesis", StreamName) 
GROUP BY StreamName
ORDER BY SUM() DESC LIMIT 10
```

**Top 10 streams by earliest items in the stream**

```sql
SELECT MAX("GetRecords.IteratorAgeMilliseconds") 
FROM SCHEMA("AWS/Kinesis", StreamName) 
GROUP BY StreamName
ORDER BY MAX() DESC LIMIT 10
```

## Lambda examples
<a name="cloudwatch-metrics-insights-queryexamples-Lambda"></a>

**Lambda functions ordered by number of invocations**

```sql
SELECT SUM(Invocations) 
FROM SCHEMA("AWS/Lambda", FunctionName) 
GROUP BY FunctionName 
ORDER BY SUM() DESC
```

**Top 10 Lambda functions by longest runtime**

```sql
SELECT AVG(Duration) 
FROM SCHEMA("AWS/Lambda", FunctionName) 
GROUP BY FunctionName 
ORDER BY MAX() DESC 
LIMIT 10
```

**Top 10 Lambda functions by error count**

```sql
SELECT SUM(Errors) 
FROM SCHEMA("AWS/Lambda", FunctionName) 
GROUP BY FunctionName 
ORDER BY SUM() DESC 
LIMIT 10
```

## CloudWatch Logs examples
<a name="cloudwatch-metrics-insights-queryexamples-CloudWatchLogs"></a>

**Top 10 log groups by incoming events**

```sql
SELECT SUM(IncomingLogEvents)
FROM SCHEMA("AWS/Logs", LogGroupName) 
GROUP BY LogGroupName
ORDER BY SUM() DESC LIMIT 10
```

**Top 10 log groups by written bytes**

```sql
SELECT SUM(IncomingBytes)
FROM SCHEMA("AWS/Logs", LogGroupName) 
GROUP BY LogGroupName
ORDER BY SUM() DESC LIMIT 10
```

## Amazon RDS examples
<a name="cloudwatch-metrics-insights-queryexamples-RDS"></a>

**Top 10 Amazon RDS instances by highest CPU utilization**

```sql
SELECT MAX(CPUUtilization)
FROM SCHEMA("AWS/RDS", DBInstanceIdentifier) 
GROUP BY DBInstanceIdentifier
ORDER BY MAX() DESC 
LIMIT 10
```

**Top 10 Amazon RDS clusters by writes**

```sql
SELECT SUM(WriteIOPS)
FROM SCHEMA("AWS/RDS", DBClusterIdentifier) 
GROUP BY DBClusterIdentifier
ORDER BY MAX() DESC 
LIMIT 10
```

## Amazon Simple Storage Service examples
<a name="cloudwatch-metrics-insights-queryexamples-S3"></a>

**Average latency by bucket**

```sql
SELECT AVG(TotalRequestLatency) 
FROM SCHEMA("AWS/S3", BucketName, FilterId) 
WHERE FilterId = 'EntireBucket' 
GROUP BY BucketName 
ORDER BY AVG() DESC
```

**Top 10 buckets by bytes downloaded**

```sql
SELECT SUM(BytesDownloaded) 
FROM SCHEMA("AWS/S3", BucketName, FilterId) 
WHERE FilterId = 'EntireBucket'
GROUP BY BucketName 
ORDER BY SUM() DESC 
LIMIT 10
```

## Amazon Simple Notification Service examples
<a name="cloudwatch-metrics-insights-queryexamples-SNS"></a>

**Total messages published by SNS topics**

```sql
SELECT SUM(NumberOfMessagesPublished) 
FROM SCHEMA("AWS/SNS", TopicName)
```

**Top 10 topics by messages published**

```sql
SELECT SUM(NumberOfMessagesPublished) 
FROM SCHEMA("AWS/SNS", TopicName) 
GROUP BY TopicName 
ORDER BY SUM() DESC 
LIMIT 10
```

**Top 10 topics by message delivery failures**

```sql
SELECT SUM(NumberOfNotificationsFailed) 
FROM SCHEMA("AWS/SNS", TopicName)
GROUP BY TopicName 
ORDER BY SUM() DESC 
LIMIT 10
```

## Amazon SQS examples
<a name="cloudwatch-metrics-insights-queryexamples-SQS"></a>

**Top 10 queues by number of visible messages**

```sql
SELECT AVG(ApproximateNumberOfMessagesVisible)
FROM SCHEMA("AWS/SQS", QueueName) 
GROUP BY QueueName
ORDER BY AVG() DESC 
LIMIT 10
```

**Top 10 most active queues**

```sql
SELECT SUM(NumberOfMessagesSent)
FROM SCHEMA("AWS/SQS", QueueName) 
GROUP BY QueueName
ORDER BY SUM() DESC 
LIMIT 10
```

**Top 10 queues by age of earliest message**

```sql
SELECT AVG(ApproximateAgeOfOldestMessage)
FROM SCHEMA("AWS/SQS", QueueName) 
GROUP BY QueueName
ORDER BY AVG() DESC 
LIMIT 10
```