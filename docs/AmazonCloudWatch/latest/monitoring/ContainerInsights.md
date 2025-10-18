# Container Insights

Use CloudWatch Container Insights to collect, aggregate, and summarize metrics and logs from your
 containerized applications and microservices. Container Insights is available for Amazon Elastic Container Service
 (Amazon ECS), Amazon Elastic Kubernetes Service (Amazon EKS), RedHat OpenShift on AWS (ROSA), and Kubernetes platforms on Amazon EC2.
 Container Insights supports collecting metrics from clusters deployed on AWS Fargate for both
 Amazon ECS and Amazon EKS.

CloudWatch automatically collects metrics for many resources, such as CPU, memory, disk, and
 network. Container Insights also provides diagnostic information, such as container restart
 failures, to help you isolate issues and resolve them quickly. You can also set CloudWatch alarms on
 metrics that Container Insights collects.

Container Insights collects data as *performance log events* using [embedded metric format](CloudWatch_Embedded_Metric_Format.md "CloudWatch_Embedded_Metric_Format.md"). These performance
 log events are entries that use a structured JSON schema that enables high-cardinality data to
 be ingested and stored at scale. From this data, CloudWatch creates aggregated metrics at the cluster,
 node, pod, task, and service level as CloudWatch metrics. The metrics that Container Insights collects
 are available in CloudWatch automatic dashboards, and are also viewable in the
 **Metrics** section of the CloudWatch console. Metrics are not visible until the
 container tasks have been running for some time.

When you deploy Container Insights, it automatically creates a log group for the performance
 log events. You don't need to create this log group yourself.

To help you manage your Container Insights costs, CloudWatch does not automatically create all
 possible metrics from the log data. However, you can view additional metrics and additional
 levels of granularity by using CloudWatch Logs Insights to analyze the raw performance log events.

With the original version of Container Insights, metrics collected and logs ingested are
 charged as custom metrics. With Container Insights with enhanced observability for Amazon EKS,
 Container Insights metrics and logs are charged per observation instead of being charged per
 metric stored or log ingested. For more information about CloudWatch pricing, see [Amazon CloudWatch Pricing](https://aws.amazon.com/cloudwatch/pricing/ "https://aws.amazon.com/cloudwatch/pricing/").

In Amazon EKS, RedHatOpenshift on AWS, and Kubernetes, Container Insights uses a containerized
 version of the CloudWatch agent to discover all of the running containers in a cluster. It then
 collects performance data at every layer of the performance stack.

Container Insights supports encryption with the AWS KMS key for the logs and metrics that
 it collects. To enable this encryption, you must manually enable AWS KMS encryption for the log
 group that receives Container Insights data. This causes Container Insights to encrypt this data
 using the provided KMS key. Only symmetric keys are supported. Do not use asymmetric
 KMS keys to encrypt your log groups.

For more information, see [Encrypt Log
 Data in CloudWatch Logs Using AWS KMS](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/encrypt-log-data-kms.html "https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/encrypt-log-data-kms.html").


## Supported platforms


Container Insights is available for Amazon Elastic Container Service, Amazon Elastic Kubernetes Service, RedHat OpenShift on AWS, and
 Kubernetes platforms on Amazon EC2 instances.



* For Amazon ECS, Container Insights collects metrics at the cluster, task, and service
 levels on both Linux and Windows Server instances. Container Insights collects metrics at
 the instance level only on Linux instances. Network metrics are available for containers
 that use `bridge` network mode and `awsvpc` network mode, but are
 not available for containers that use `host` network mode.
* For Amazon Elastic Kubernetes Service, and Kubernetes platforms on Amazon EC2 instances, Container Insights is
 supported on both Linux and Windows instances.

## CloudWatch agent container image


Amazon provides a CloudWatch agent container image on Amazon Elastic Container Registry. For more information, see
 [cloudwatch-agent](https://gallery.ecr.aws/cloudwatch-agent/cloudwatch-agent "https://gallery.ecr.aws/cloudwatch-agent/cloudwatch-agent") on Amazon ECR.
