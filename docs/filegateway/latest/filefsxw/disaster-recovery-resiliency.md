Amazon FSx File Gateway is no longer available to new customers. Existing
customers of FSx File Gateway can continue to use the service normally. For capabilities
similar to FSx File Gateway, visit [this blog post](https://aws.amazon.com/blogs/storage/switch-your-file-share-access-from-amazon-fsx-file-gateway-to-amazon-fsx-for-windows-file-server/ "https://aws.amazon.com/blogs/storage/switch-your-file-share-access-from-amazon-fsx-file-gateway-to-amazon-fsx-for-windows-file-server/").

# Resilience in AWS Storage Gateway

The AWS global infrastructure is built around AWS Regions and Availability
Zones.

An AWS Region is a physical location around the world where data centers are clustered.
Each group of logical data centers is called an Availability Zone (AZ). Each AWS Region
consists of a minimum of three isolated and physically separate AZs within a geographic
area. Unlike other cloud providers, who often define a region as a single data center, the
multiple AZ design of every AWS Region offers distinct advantages. Each AZ has independent
power, cooling, and physical security and is connected via redundant, ultra-low-latency
networks. If your deployment requires a focus on high availability, you can configure
services and resources to in multiple AZs to achieve greater fault-tolerance.

AWS Regions meet the highest levels of infrastructure security, compliance, and data
protection. All traffic between AZs is encrypted. The network performance is sufficient to
accomplish synchronous replication between AZs. AZs make partitioning services and resources
for high availability easy. If your deployment is partitioned across AZs, your resources are
better isolated and protected from issues such as power outages, lightning strikes,
tornadoes, earthquakes, and more. AZs are physically separated by a meaningful distance from
any other AZ, although all are within 100 km (60 miles) of each other.

For more information about AWS Regions and Availability Zones, see [AWS Global
Infrastructure](https://aws.amazon.com/about-aws/global-infrastructure/ "https://aws.amazon.com/about-aws/global-infrastructure/").

In addition to the AWS global infrastructure, Storage Gateway supports VMware vSphere High
Availability (VMware HA) to help protect storage workloads against hardware, hypervisor, or
network failures. For more information, see [Using VMware vSphere High Availability
with Storage Gateway](vmware-ha.md "vmware-ha.md").
