# Resilience in AWS Outposts

For high availability, you can order additional Outposts servers.
Outpost capacity configurations are designed to operate in production environments,
and support N+1 instances for each instance family when you provision the capacity to do so.
AWS recommends that you allocate sufficient additional capacity for your mission-critical
applications to enable recovery and failover if there is an underlying host issue. You can
use the Amazon CloudWatch capacity availability metrics and set alarms to monitor the health of your
applications, create CloudWatch actions to configure automatic recovery options, and monitor the
capacity utilization of your Outposts over time.

When you create an Outpost, you select an Availability Zone from an AWS Region. This
Availability Zone supports control plane operations such as responding to API calls,
monitoring the Outpost, and updating the Outpost. To benefit from the resiliency provided by
Availability Zones, you can deploy applications on multiple Outposts, each attached to a
different Availability Zone. This enables you to build additional application resilience and
avoid a dependence on a single Availability Zone. For more information about Regions and
Availability Zones, see [AWS
Global Infrastructure](https://aws.amazon.com/about-aws/global-infrastructure/ "https://aws.amazon.com/about-aws/global-infrastructure/").

Outposts servers include instance store volumes but do not support
Amazon EBS volumes. The data on instance store volumes persists after an instance reboot but does not
persist after instance termination. To retain the long-term data on your instance store volumes
beyond the lifetime of the instance, be sure to back up the data to persistent storage, such as
an Amazon S3 bucket or a network storage device in your on-premises network.
