Amazon Redshift will no longer support the creation of new Python UDFs starting November 1, 2025.
If you would like to use Python UDFs, create the UDFs prior to that date.
Existing Python UDFs will continue to function as normal. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# Resilience in Amazon Redshift

The AWS global infrastructure is built around AWS Regions and Availability Zones
(AZs). AWS Regions provide multiple, physically separated and isolated Availability Zones
that are connected with low latency, high throughput, and highly redundant networking. With
Availability Zones, you can design and operate applications and databases that automatically
fail over between Availability Zones without interruption. Availability Zones are more
highly available, fault tolerant, and scalable than traditional single data center
infrastructures or multiple data center infrastructures.

Almost all AWS Regions have multiple Availability Zones and data centers. You can deploy
your applications across multiple Availability Zones in the same Region for fault tolerance
and low latency.

To move a cluster to another Availability Zone without any loss of data or changes to your applications, you can set up relocation for your cluster. With relocation, you can continue operations when there is an interruption of service on your cluster with minimal impact. When cluster relocation is turned on, Amazon Redshift might choose to relocate clusters in some situations. For more information on relocation in Amazon Redshift, see [Relocating a cluster](managing-cluster-recovery.md "managing-cluster-recovery.md").

In failure scenarios where an unexpected event happens in an Availability Zone, you can set up a multiple Availability Zones (Multi-AZ) deployment to ensure that your Amazon Redshift data warehouse can continue operating. Amazon Redshift deploys equal compute resources in two Availability Zones that can be accessed through a single endpoint. In the event of an entire Availability Zone failure, the remaining compute resources in the second Availability Zone will be available to continue processing workloads. For more information on Multi-AZ deployments, see [Multi-AZ deployment](managing-cluster-multi-az.md "managing-cluster-multi-az.md").

For more information on AWS Regions and Availability Zones, see [AWS global
infrastructure](https://aws.amazon.com/about-aws/global-infrastructure/ "https://aws.amazon.com/about-aws/global-infrastructure/"). For more information on using Amazon Redshift for disaster recovery,
see [Implement disaster recovery with Amazon Redshift](https://aws.amazon.com/blogs/big-data/implement-disaster-recovery-with-amazon-redshift/ "https://aws.amazon.com/blogs/big-data/implement-disaster-recovery-with-amazon-redshift/").

.
