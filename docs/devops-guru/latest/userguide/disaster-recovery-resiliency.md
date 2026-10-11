

End of support notice: Amazon DevOps Guru will stop accepting new customers on October 29, 2026. Current customers will not be impacted and can continue using Amazon DevOps Guru until September 30, 2027. After September 30, 2027 you will no longer be able to access Amazon DevOps Guru. For more information, see [Amazon DevOps Guru end of support](devops-guru-end-of-support.md).

# Resilience in Amazon DevOps Guru
<a name="disaster-recovery-resiliency"></a>

The AWS global infrastructure is built around AWS Regions and Availability Zones. AWS Regions provide multiple physically separated and isolated Availability Zones, which are connected with low-latency, high-throughput, and highly redundant networking. DevOps Guru operates in multiple Availability Zones and stores artifact data and metadata in Amazon S3 and Amazon DynamoDB. Your encrypted data is redundantly stored across multiple facilities and multiple devices in each facility, making it highly available and highly durable.

For more information about AWS Regions and Availability Zones, see [AWS Global Infrastructure](https://aws.amazon.com/about-aws/global-infrastructure/).