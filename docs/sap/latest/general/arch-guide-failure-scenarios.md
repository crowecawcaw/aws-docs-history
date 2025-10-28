# Failure scenarios

For the failure scenarios below, the primary consideration is the physical unavailability of the compute and/or storage capacity within the Availability Zones.

## Availability Zone failure

An Availability Zone failure can be caused by a significant availability degradation of one or more AWS services utilized by your resources within that Availability Zone. For example:

- Several Amazon EC2 instances have failed with [System Status Check errors](../../../AWSEC2/latest/UserGuide/monitoring-system-instance-status-check.md "../../../AWSEC2/latest/UserGuide/monitoring-system-instance-status-check.md") or are unreachable and cannot be restarted.
- Several Amazon Elastic Block Store (Amazon EBS) volumes with [Volume Status Check errors](../../../AWSEC2/latest/UserGuide/monitoring-volume-status.md#monitoring-volume-checks "../../../AWSEC2/latest/UserGuide/monitoring-volume-status.md#monitoring-volume-checks") have failed.

## Amazon Elastic Block Store failure

Loss of one or more Amazon EBS volumes attached to a single Amazon EC2 instance may result in the unavailability of a critical component (i.e. the database) of the SAP system.

## Amazon EC2 failure

Loss of a single Amazon EC2 instance may result in the unavailability of a critical component (i.e. the database or SAP Central Services) of the SAP system.

## Logical data loss

You should also consider the potential for logical data loss where the underlying hardware capacity still exists but the primary copies of the data have been corrupted or lost. This data loss could be due to malicious activity within your AWS account or due to human error.

To protect against logical data loss, it is recommended that regular copies of the data are backed up to an Amazon S3 bucket. This bucket is replicated (using [Single-Region or Cross-Region replication](arch-guide-architecture-guidelines-and-decisions.md#arch-guide-s3-replication "arch-guide-architecture-guidelines-and-decisions.md#arch-guide-s3-replication")) to another Amazon S3 bucket owned by a separate AWS account. With the appropriate AWS Identity and Access Management (IAM) controls between the two AWS accounts, this strategy ensures that not all copies of the data are lost due to malicious activity or human error.
