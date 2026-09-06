

# Container, queue, and database metrics for Amazon MWAA
<a name="accessing-metrics-cw-container-queue-db"></a>

In addition to Apache Airflow metrics, you can monitor the underlying components of your Amazon Managed Workflows for Apache Airflow environments using CloudWatch, which collects raw data and processes data into readable, near real-time metrics. With these environment metrics, you'll have greater visibility into key performance indicators to help you appropriately size your environments and debug issues with your workflows. These metrics apply to all supported Apache Airflow versions on Amazon MWAA.



Amazon MWAA will provide CPU and memory utilization for each Amazon Elastic Container Service (Amazon ECS) container and Amazon Aurora PostgreSQL instance, and Amazon Simple Queue Service (Amazon SQS) metrics for the number of messages and the age of the oldest message, Amazon Relational Database Service (Amazon RDS) metrics for database connections, disk queue depth, write operations, latency, and throughput, and Amazon RDS Proxy metrics. These metrics also include the number of base workers, additional workers, schedulers, and webservers.

These statistics are kept for 15 months, so that you can access historical information and gain a better perspective on why a schedule is failing, and troubleshoot underlying issues. You can also set alarms that monitor for certain thresholds, and send notifications or take actions when those thresholds are met. For more information, refer to the [Amazon CloudWatch User Guide](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/).

**Topics**
+ [Terms](#accessing-metrics-cw-container-queue-db-terms)
+ [Dimensions](#accessing-metrics-cw-container-queue-db-dimensions)
+ [Accessing metrics in the CloudWatch console](#accessing-metrics-cw-container-queue-db-console)
+ [List of metrics](#accessing-metrics-cw-container-queue-db-list)

## Terms
<a name="accessing-metrics-cw-container-queue-db-terms"></a>

**Namespace**  
A namespace is a container for the CloudWatch metrics of an AWS service. For Amazon MWAA, the namespace is `AWS/MWAA`.

**CloudWatch metrics**  
A CloudWatch metric represents a time-ordered set of data points that are specific to CloudWatch.

**Dimension**  
A dimension is a name/value pair that is part of the identity of a metric.

**Unit**  
A statistic has a unit of measure. For Amazon MWAA, units include *Count*.

## Dimensions
<a name="accessing-metrics-cw-container-queue-db-dimensions"></a>

This section describes the CloudWatch dimensions grouping for Amazon MWAA metrics in CloudWatch.


| Dimension | Description | 
| --- | --- | 
| Cluster | Metrics for the minimum three Amazon ECS container that an Amazon MWAA environment uses to run Apache Airflow components: scheduler, worker, and web server. | 
| Queue | Metrics for the Amazon SQS queues that decouple the scheduler from workers. When workers read the messages, they are considered in-flight and not available for other workers. Messages become available for other workers to read if they are not deleted before the 12-hour visibility timeout. | 
| Database | Metrics the Aurora clusters used by Amazon MWAA. This includes metrics for the primary database instance and a read replica to support the read operations. Amazon MWAA publishes database metrics for both READER and WRITER instances. | 

## Accessing metrics in the CloudWatch console
<a name="accessing-metrics-cw-container-queue-db-console"></a>

This section describes how to access your Amazon MWAA metrics in CloudWatch.

**To access performance metrics for a dimension**

1. Open the [Metrics page](https://console.aws.amazon.com/cloudwatch/home#metricsV2:graph=~()) on the CloudWatch console.

1. Select your AWS Region.

1. Choose the **AWS/MWAA** namespace.

1. In the **All metrics** tab, choose a dimension. For example, **Cluster**.

1. Choose a CloudWatch metric for a dimension. For example, *NumSchedulers* or *CPUUtilization*. Then, choose **Graph all search results**.

1. Choose the **Graphed metrics** tab to access performance metrics.

## List of metrics
<a name="accessing-metrics-cw-container-queue-db-list"></a>

The following tables list the cluster, queue, and database service metrics for Amazon MWAA. To access descriptions for metrics directly emitted from Amazon ECS, Amazon SQS, or Amazon RDS, choose the respective documentation link.

**Topics**
+ [Cluster metrics](#container-list)
+ [Database metrics](#db-list)
+ [Queue metrics](#queue-list)
+ [Application Load Balancer metrics](#alb-list)

### Cluster metrics
<a name="container-list"></a>

The following metrics apply to each scheduler, base worker, additional worker, and web server. For more information about these metrics, see [Amazon ECS monitoring](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/cloudwatch-metrics.html#available_cloudwatch_metrics) and [Amazon ECS Container Insights](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/Container-Insights-metrics-ECS.html).


| Namespace | Metric | Unit | 
| --- | --- | --- | 
| `AWS/MWAA` | `CPUUtilization` | Percent | 
| `AWS/MWAA` | `MemoryUtilization` | Percent | 
| `AWS/MWAA` | `EphemeralStorageUtilized` | Megabytes | 
| `AWS/MWAA` | `EphemeralStorageReserved` | Megabytes | 
| `AWS/MWAA` | `NetworkTxBytes` | Bytes/Second | 
| `AWS/MWAA` | `NetworkRxBytes` | Bytes/Second | 

#### Evaluating the number of additional worker and webserver containers
<a name="additional-worker-scheduler-sample-count"></a>

You can use the component metrics provided in the **Cluster** dimension, as described in the following procedure, to assess how many additional workers, or webservers, an environment is using at a given point in time. You can do this by graphing either the **CPUUtilization** or the **MemoryUtilization** metric and setting the statistic type to **Sample Count**. The resulting value is the total number of `RUNNING` tasks for the `AdditionalWorker` component. Understanding the number of additional worker instances utilized by your environment can help you gauge how your environment scales and you can use to optimize the number of additional workers.

------
#### [ Workers ]

**To evaluate the number of additional workers using the AWS Management Console**

1. Choose the **AWS/MWAA** namespace.

1. In the **All metrics** tab, choose the **Cluster** dimension.

1. In the **Cluster** dimension, for the **AdditionalWorker**, choose either the **CPUUtilization** or the **MemoryUtilization** metric.

1. On the **Graphed metrics** tab, set **Period** to **1 Minute** and **Statistic** to **Sample Count**.

------
#### [ webservers ]

**To evaluate the number of additional webservers using the AWS Management Console**

1. Choose the **AWS/MWAA** namespace.

1. In the **All metrics** tab, choose the **Cluster** dimension.

1. In the **Cluster** dimension, for the **AdditionalWebservers**, choose either the **CPUUtilization** or the **MemoryUtilization** metric.

1. On the **Graphed metrics** tab, set **Period** to **1 Minute** and **Statistic** to **Sample Count**.

------

For more information, refer to [Service `RUNNING` task count](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/cloudwatch-metrics.html#cw_running_task_count) in the *Amazon Elastic Container Service Developer Guide*.

### Database metrics
<a name="db-list"></a>

The following metrics apply to each database instance associated with the Amazon MWAA environment.


| Namespace | Metric | Unit | 
| --- | --- | --- | 
| `AWS/MWAA` | `CPUUtilization` | Percent | 
| `AWS/MWAA` | `DatabaseConnections` | Count | 
| `AWS/MWAA` | `DiskQueueDepth` | Count | 
| `AWS/MWAA` | `FreeableMemory` | Bytes | 
| `AWS/MWAA` | `VolumeWriteIOPS` | Count per five minutes | 
| `AWS/MWAA` | `WriteIOPS` | Count per second | 
| `AWS/MWAA` | `WriteLatency` | Seconds | 
| `AWS/MWAA` | `WriteThroughput` | Bytes per second | 

### Queue metrics
<a name="queue-list"></a>

For more information about units and descriptions for the following queue metrics, refer to [Available CloudWatch metrics for Amazon SQS](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-available-cloudwatch-metrics.html) in the *Amazon Simple Queue Service Developer Guide*.


| Namespace | Metric | Unit | 
| --- | --- | --- | 
| `AWS/MWAA` | `ApproximateAgeOfOldestTask` | Seconds | 
| `AWS/MWAA` | `RunningTasks` | Count | 
| `AWS/MWAA` | `QueuedTasks` | Count | 

### Application Load Balancer metrics
<a name="alb-list"></a>

Application Load Balancer metrics apply to the web servers running in your environment. Amazon MWAA uses these metrics to for scaling your web servers based on the amount of traffic. For more information about units and descriptions for the following load balancer metrics, refer to [CloudWatch metrics for your Application Load Balancer](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/load-balancer-cloudwatch-metrics.html) in the *Application Load Balancers User Guide*.


| Namespace | Metric | Unit | 
| --- | --- | --- | 
| `AWS/MWAA` | `ActiveConnectionCount` | Count | 