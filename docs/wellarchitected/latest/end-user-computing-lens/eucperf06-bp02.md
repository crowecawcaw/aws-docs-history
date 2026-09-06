

# EUCPERF06-BP02 Minimize latency between EUC instances and dependent services
<a name="eucperf06-bp02"></a>

 In most cases, EUC users require connections to resources outside their EUC instances. Common dependencies include web or application servers, database servers, and storage services. 

 **Level of risk exposed if this best practice is not established:** Medium 

## Implementation guidance
<a name="implementation-guidance-16"></a>

When possible, deploy these dependencies in the same AWS Region and ideally the same Availability Zone. If the system of record must reside elsewhere, consider deploying caches or replicas. For example, if your Active Directory domain controllers are on your on-premises network, deploy replicas on Amazon EC2. 

 When connecting to Amazon S3, use gateway VPC endpoints. For more information on configuring gateway endpoints, see [Gateway endpoints for Amazon S3](https://docs.aws.amazon.com/vpc/latest/privatelink/vpc-endpoints-s3.html).