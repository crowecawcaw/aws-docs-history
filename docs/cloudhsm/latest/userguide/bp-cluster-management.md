# AWS CloudHSM cluster management best practices

Follow the best practices in this section when creating, accessing, and managing your AWS CloudHSM cluster.


## Scale your cluster to handle peak traffic


Several factors can influence the maximum throughput that your cluster can handle, including client instance size, cluster size, network topography, and the cryptographic operations you require for your use case.


As a starting point, refer to the topic [AWS CloudHSM performance information](performance.md "performance.md") for performance estimates on common cluster sizes and configurations. 
 We recommend you load test your cluster with the peak load you anticipate to determine whether your current architecture is resilient and at the right scale.


## Architect your cluster for high availability


**Add redundancy to account for maintenance**: AWS may replace your HSM for scheduled maintenance or if it detects a problem. As a general rule, your cluster size should have at least +1 redundancy. 
 For example, if you require two HSMs for your service to operate at peak times, your ideal cluster size will then be three. If you follow the best practices relating to availability, 
 these HSM replacements should not impact your service. However, in-progress operations on the replaced HSM may fail and must be retried.


**Spread your HSMs across many Availability Zones**: Consider how your service will be able to operate during an Availability Zone outage. 
 AWS recommends that you spread your HSMs across as many Availability Zones as possible. For a cluster with three HSMs, you should spread HSMs across three Availability Zones. 
 Depending on your system, you may require additional redundancy.


## Have at least three HSMs to ensure durability for newly generated keys


For applications that require durability of newly generated keys, we recommend having at least three HSMs spread
 across different Availability Zones in a region.


## Secure access to your cluster


**Use private subnets to limit access to your instance**: Launch your HSMs and client instances in the private subnets of your VPC. 
 This limits access to your HSMs from the outside world.


**Use VPC endpoints to access APIs**: The AWS CloudHSM data plane was designed to operate without needing access to the internet or AWS APIs. 
 If your client instance requires access to the AWS CloudHSM API, you can use VPC endpoints to access the API without requiring internet access on your client instance. 
 See [AWS CloudHSM and VPC endpoints](cloudhsm-vpc-endpoint.md "cloudhsm-vpc-endpoint.md") for more information.


## Reduce costs by scaling to your needs


There are no upfront costs to use AWS CloudHSM. You pay an hourly fee for each HSM you launch until you terminate the HSM. 
 If your service does not require continuous usage of AWS CloudHSM, you can reduce costs by scaling down (deleting) your HSMs to zero when they are not needed. 
 When HSMs are again needed, you can restore your HSMs from a backup. If, for example, you have a workload requiring you to sign code once a month, specifically on the last day of the month, 
 you can scale up your cluster before, scale it down by deleting your HSMs after the work is completed, and then restore your cluster to perform signing operations again at the end of the next month. 
 


AWS CloudHSM automatically makes periodic backups of the HSMs in the cluster. When adding a new HSM at a later date, AWS CloudHSM will restore the latest backup onto the new HSM so that you can
 resume usage from the same place you left it. To calculate your AWS CloudHSM architecture costs, see [AWS CloudHSM Pricing](https://aws.amazon.com/cloudhsm/pricing/ "https://aws.amazon.com/cloudhsm/pricing/").


Related resources:



* [General overview of backups](backups.md "backups.md")
* [Backup retention policy](manage-backup-retention.md "manage-backup-retention.md")
* [Copying AWS CloudHSM cluster backups across AWS
 Regions](copy-backup-to-region.md "copy-backup-to-region.md")
