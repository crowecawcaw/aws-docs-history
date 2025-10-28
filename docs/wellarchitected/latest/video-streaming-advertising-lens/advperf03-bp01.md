# ADVPERF03-BP01 Choose appropriate block storage options to power your advertising workload

Block storage is crucial for data storage in the cloud. Customers
need to choose the appropriate block storage service based on
different types of workloads, as well as their requirements for
storage performance and stability.

## Implementation guidance

[Amazon EBS](https://aws.amazon.com/ebs/ "https://aws.amazon.com/ebs/") provides persistent block-level storage
volumes for use with Amazon Elastic Compute Cloud (Amazon EC2) instances. In the advertising industry, Amazon EBS can be
used to store databases, such as MySQL or PostgreSQL, that power ad servers, bid management
systems, and other critical components. Amazon EBS volumes can be easily scaled and optimized for
different workload patterns, which provides high performance and reliability.

- **Volume types:** Choose the
  appropriate EBS volume type based on your workload. For
  general-purpose workloads, use GP3 volumes. For
  high-performance needs, consider IO2 volumes. If you need
  high performance, you'll need to use
  [EC2
  Instance Store](../../../AWSEC2/latest/UserGuide/InstanceStorage.md "../../../AWSEC2/latest/UserGuide/InstanceStorage.md"). It's ephemeral block storage with a
  much higher performance than EBS.
- **EBS-optimized instances:** Use Amazon EBS-optimized Amazon EC2
  instances to provide dedicated throughput between your instances and Amazon EBS volumes. For
  example, use Amazon EBS-optimized Amazon EC2 instances and provisioned IOPS volumes for real-time
  bidding or ad serving. workloads.
- **Encryption:** Enable encryption by default for all Amazon EBS
  volumes to meet security and compliance requirements.
- **Snapshot management:** Regularly create and manage Amazon EBS
  snapshots for backup and disaster recovery. Use AWS Data Lifecycle Manager to automate
  snapshot management.
- **Performance monitoring:**
  Use Amazon CloudWatch metrics to monitor and optimize EBS
  health and performance.
- **Scaling:** Leverage Amazon EBS Elastic Volumes to increase the
  size of Amazon EBS volumes dynamically without disrupting your applications.

## Resources

- [Amazon EBS volume types](../../../ebs/latest/userguide/ebs-volume-types.md "../../../ebs/latest/userguide/ebs-volume-types.md")
- [Amazon EBS volume performance](../../../ebs/latest/userguide/ebs-performance.md "../../../ebs/latest/userguide/ebs-performance.md")
- [Monitoring
  tools for Amazon EBS](../../../ebs/latest/userguide/monitoring-overview.md "../../../ebs/latest/userguide/monitoring-overview.md")
- [Automate
  backups with Amazon Data Lifecycle Manager](../../../ebs/latest/userguide/snapshot-lifecycle.md "../../../ebs/latest/userguide/snapshot-lifecycle.md")
- [What
  is Amazon Elastic Block Store?](../../../ebs/latest/userguide/work-with-ebs-encr.md "../../../ebs/latest/userguide/work-with-ebs-encr.md")
