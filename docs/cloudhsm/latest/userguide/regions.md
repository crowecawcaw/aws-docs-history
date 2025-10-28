# Supported Regions for AWS CloudHSM

For information about the supported Regions for AWS CloudHSM, see [AWS CloudHSM Regions and Endpoints](../../../general/latest/gr/cloudhsm.md "../../../general/latest/gr/cloudhsm.md") in the _AWS General Reference_, or the [Region Table](https://aws.amazon.com/about-aws/global-infrastructure/regional-product-services/ "https://aws.amazon.com/about-aws/global-infrastructure/regional-product-services/").

AWS CloudHSM might not be available in all Availability Zones in a given Region. However, this should not affect performance,
as AWS CloudHSM automatically load balances across all HSMs in a cluster.

Like most AWS resources, clusters and HSMs are regional resources. You cannot reuse or
extend a cluster across Regions. You must perform all the required steps listed in
[Getting started with AWS CloudHSM](getting-started.md "getting-started.md") to create a cluster
in a new Region.

For disaster recovery purposes, AWS CloudHSM allows you to copy backups of your AWS CloudHSM Cluster from one region to another.
For more information, see [AWS CloudHSM cluster backups](backups.md "backups.md").
