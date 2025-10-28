# Amazon CloudWatch agent

The Amazon CloudWatch agent on Amazon EMR is a tool that can monitor the Amazon EC2 instances in your
EMR cluster. You can store and view the metrics that you collect with the CloudWatch agent in
CloudWatch. For more information about the CloudWatch agent, see the [_Amazon CloudWatch User Guide_](../../../AmazonCloudWatch/latest/monitoring/Install-CloudWatch-Agent.md "../../../AmazonCloudWatch/latest/monitoring/Install-CloudWatch-Agent.md").

###### Note

You incur additional charges if you use other AWS services to publish, query, or view Amazon CloudWatch agent metrics. See the following pages for more pricing information.

- [Amazon CloudWatch Pricing](https://aws.amazon.com/cloudwatch/pricing/ "https://aws.amazon.com/cloudwatch/pricing/")
- [Amazon Managed Service for Prometheus Pricing](https://aws.amazon.com/prometheus/pricing/ "https://aws.amazon.com/prometheus/pricing/")
- [Amazon Managed Grafana Pricing](https://aws.amazon.com/grafana/pricing/ "https://aws.amazon.com/grafana/pricing/")
  These metrics are separate from the free metrics that Amazon EMR provides under the `AWS/ElasticMapReduce` namespace in CloudWatch. For more information about the
  metrics that the CloudWatch agent doesn't publish, see [Monitoring Amazon EMR metrics with CloudWatch](../ManagementGuide/UsingEMR_ViewingMetrics.md "../ManagementGuide/UsingEMR_ViewingMetrics.md").

With Amazon EMR 7.0 and higher, you can install a custom version of the Amazon CloudWatch agent on your cluster to collect metrics
from your EMR cluster. CloudWatchAgent is supported on Runtime Role Clusters for EMR 7.6 and above. The agent collects the metrics from all nodes in the cluster, gathers them on the primary node,
and publishes the metrics from that node to the cloud.

You can install the agent when you create a new cluster in the console, or when you use
the `create-cluster` API. For more information, see [Create an EMR cluster that uses
Amazon CloudWatch agent](AmazonCloudWatchAgent-create.md "AmazonCloudWatchAgent-create.md"). By default, an Amazon EMR cluster that runs the release 7.x series publishes [34 system-level metrics](AmazonCloudWatchAgent-metrics.md "AmazonCloudWatchAgent-metrics.md") to CloudWatch at 60-second
intervals, but you can configure the agent to publish different metrics. Another option is to publish metrics to Amazon Managed Service for Prometheus, and you can
choose which metrics to publish as well.
For different use cases and setups, you might configure the agent to
view and query the metrics in the CloudWatch console, Amazon Managed Grafana, or through the APIs for CloudWatch or Amazon Managed Service for Prometheus. These AWS services
incur charges when you use them to store and query metrics.

The CloudWatch agent on Amazon EMR can publish
system metrics as well as JMX metrics for the following services on your Amazon EMR cluster.

- Hadoop DataNode
- Hadoop NameNode
- Yarn NodeManager
- Yarn ResourceManager
- HBase Master – Amazon EMR 7.1+ only
- HBase RegionServer – Amazon EMR 7.1+ only
- HBase ThriftServer – Amazon EMR 7.1+ only
  For more information about available metrics and how to configure the CloudWatch agent on Amazon EMR, see [Configuring CloudWatch agent for Amazon EMR](AmazonCloudWatchAgent-config.md "AmazonCloudWatchAgent-config.md").

The following table lists the version of AmazonCloudWatchAgent included in the latest release of the Amazon EMR 7.x series, along with the components that Amazon EMR installs with AmazonCloudWatchAgent.

For the version of components installed with AmazonCloudWatchAgent in this release, see [Release 7.10.0 Component Versions](emr-7100-release.md "emr-7100-release.md").

| AmazonCloudWatchAgent version information for emr-7.10.0 | Amazon EMR Release Label                | AmazonCloudWatchAgent Version                                                                                                                                                                                                                                                                                                     | Components Installed With AmazonCloudWatchAgent                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| -------------------------------------------------------- | --------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| emr-7.10.0                                               | AmazonCloudWatchAgent 1.300032.2-amzn-0 | adot-java-agent, emrfs, emr-amazon-cloudwatch-agent, emr-ddb, emr-goodies, emr-kinesis, emr-s3-dist-cp, hadoop-client, hadoop-hdfs-datanode, hadoop-hdfs-library, hadoop-hdfs-namenode, hadoop-httpfs-server, hadoop-kms-server, hadoop-mapred, hadoop-yarn-nodemanager, hadoop-yarn-resourcemanager, hadoop-yarn-timeline-server | ###### Topics <br>• [Create an EMR cluster that uses Amazon CloudWatch agent](AmazonCloudWatchAgent-create.md "AmazonCloudWatchAgent-create.md") <br>• [Default metrics for CloudWatch agent with Amazon EMR](AmazonCloudWatchAgent-metrics.md "AmazonCloudWatchAgent-metrics.md") <br>• [Configuring CloudWatch agent for Amazon EMR](AmazonCloudWatchAgent-config.md "AmazonCloudWatchAgent-config.md") <br>• [Considerations and limitations](AmazonCloudWatchAgent-considerations.md "AmazonCloudWatchAgent-considerations.md") <br>• [CloudWatch agent release history](AmazonCloudWatchAgent-release-history.md "AmazonCloudWatchAgent-release-history.md") |
