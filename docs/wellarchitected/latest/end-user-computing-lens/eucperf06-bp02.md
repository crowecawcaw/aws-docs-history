# EUCPERF06-BP02 Minimize latency between EUC instances and dependent services

In most cases, EUC users require connections to resources outside their EUC instances.
Common dependencies include web or application servers, database servers, and storage
services.

**Level of risk exposed if this best practice is not
established:** Medium

## Implementation guidance

When possible, deploy these dependencies in the same AWS Region and ideally the same
Availability Zone. If the system of record must reside elsewhere, consider deploying
caches or replicas. For example, if your Active Directory domain controllers are on your
on-premises network, deploy replicas on Amazon EC2.

When connecting to Amazon S3, use gateway VPC endpoints. For more information on
configuring gateway endpoints, see [Gateway endpoints for
Amazon S3](../../../vpc/latest/privatelink/vpc-endpoints-s3.md "../../../vpc/latest/privatelink/vpc-endpoints-s3.md").
