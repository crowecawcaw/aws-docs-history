# Monitoring EMR HBase with Amazon CloudWatch

Starting from EMR 7.0, Amazon EMR provide the Amazon CloudWatch Agent to send metrics to CloudWatch or Prometheus, replacing the Ganglia monitoring system. You can find more details
in the [Amazon CloudWatch Agent Configuration Guide](AmazonCloudWatchAgent-config-700.md "AmazonCloudWatchAgent-config-700.md").

The EMR 7.0 Amazon CloudWatch agent provided basic integration and setting it up required manual effort, like downloading components and using bootstrap actions. However, from EMR 7.1 onwards,
the process is simplified. Using the Amazon CloudWatch Agent in EMR 7.1 makes it easy to monitor both system-level and application-specific metrics, including those for HBase. By using
the EMR configuration API, you can quickly set up and customize the metrics collection process, and choose where to send the data—either to Amazon CloudWatch or Prometheus. This flexibility
helps you keep a close eye on your HBase clusters, ensuring they run smoothly and efficiently.

Using the EMR configuration API to handle the entire setup, making the process much smoother. The CloudWatch Agent in EMR 7.1 supports three main types of metrics:

- **System Metrics** – These include key indicators of system performance, such as: CPU usage, Disk usage, Memory usage,
  Network I/O, Processes, and Swap usage.
- **Hadoop Daemon Metrics** – These metrics relate to the various components of Hadoop, including: DataNode metrics, NameNode metrics, YARN NodeManager metrics,
  and YARN ResourceManager metrics.
- **HBase Metrics** – These metrics provide insights into HBase’s performance: HBase Master metrics, HBase Region Server metrics, HBase REST Server
  metrics, and HBase Thrift Server metrics.

Using the AWS CLI
All the metrics for Hadoop and HBase are JMX-based, which means they use Java Management Extensions to provide detailed insights. Here’s how you can set up Amazon CloudWatch
Agent to monitor HBase:

- Refer to [Prerequisites](AmazonCloudWatchAgent-create.md "AmazonCloudWatchAgent-create.md") before creating a cluster with Amazon CloudWatch Agent. Use a `create-cluster`
  command similar to the sample that appears after this list.
- Refer the [Configurations](AmazonCloudWatchAgent-config.md "AmazonCloudWatchAgent-config.md") supported for an HBase cluster.
- Refer to the sample that follows for example configurations to set up HBase monitoring. Refer to the example configurations for the `--configuration`
  input.

```
aws emr create-cluster --name "HBase cluster with CloudWatch agent" \
--release-label emr-7.1.0 \
--applications Name=HBase Name=AmazonCloudWatchAgent \
--ec2-attributes KeyName=myKey --instance-type m7g.2xlarge \
--configurations file://./configurations.json \
--instance-count 3 --use-default-roles
```

For more information on JSON sample configurations for metrics, see [Set up metrics](emr-hbase-setting-up-metrics.md "emr-hbase-setting-up-metrics.md").

Using the console
To create a cluster with Amazon CloudWatch agent from the console, perform these steps:

###### Create a cluster with the CloudWatch agent from the console

1. Sign in to the AWS Management Console, and open the Amazon EMR console at
   [https://console.aws.amazon.com/emr](https://console.aws.amazon.com/emr "https://console.aws.amazon.com/emr").
2. Choose **Create cluster**.
3. Under **Name and applications**, choose an Amazon EMR release of 7.0.0 or higher.
4. Under **Application bundle**, select HBase and additional apps that you want to install to your cluster, and include CloudWatch agent
   with your selections.
5. Expand **Software settings**. You can then enter the configuration directly by using either JSON or a shorthand syntax demonstrated
   in shadow text in the console. Otherwise, you can provide an Amazon S3 URI for a file with a JSON `Configurations` object. For more information on JSON sample configurations for metrics, see [Set up metrics](emr-hbase-setting-up-metrics.md "emr-hbase-setting-up-metrics.md").
6. Proceed to create the cluster to serve your use case needs.
