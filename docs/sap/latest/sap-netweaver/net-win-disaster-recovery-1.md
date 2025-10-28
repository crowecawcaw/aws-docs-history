# Disaster Recovery

## Network Fileshare Copy Out-of-Region

To ensure that you have an independent backup of your data in the secondary Region, you should back up your shared filesystem, as this won’t be included in any AMIs or individual EBS snapshots.

To back up your Amazon FSx filesystem, you can rely on the included backup feature. However, this backs up to Amazon S3 in-region. To support out-of-region disaster recovery (DR), you will need to perform a file-level backup of your Amazon FSx filesystem in your secondary Region. You can do this by accessing the filesystem via cross-region VPC peering and then running a file-level copy from an Amazon EC2 instance running in the secondary Region to Amazon S3. This action can be automated and scheduled using AWS Systems Manager Run Command in combination with Amazon CloudWatch Events.

## Fail-back Plan

When your primary Region returns to normal operations, you may consider failing back to it. In the event of a disaster that triggered a recovery to another Region, you copy the AMIs and shared filesystems from the secondary Region back to the primary. In other words, you’ll reverse what was the regular process before the disaster. It’s important to update your change management or change control processes to reflect this.

## AMI Copy

When your primary AWS Region is affected by an availability event, AMIs allow you to quickly recover your SAP NetWeaver application servers in your DR Region. For recovery across Regions, ensure that the latest AMIs are copied to the disaster recovery Region using the [AMI copy](../../../AWSEC2/latest/UserGuide/CopyingAMIs.md "../../../AWSEC2/latest/UserGuide/CopyingAMIs.md") feature. New AMIs should be created when there are filesystem level changes to the SAP NetWeaver application servers. This can be caused by:

- SAP kernel changes
- Database client software updates
- Operating system patches

To ensure that you reliably create a new AMI when these events happen, add the AMI creation as a step in your change management process. It’s important that if using a mechanism like this that you integrate the out-of-region AMI copy with this process.

If having the lowest possible recovery time objective (RTO) is a priority, consider keeping at least one application server running in the secondary Region to minimize the recovery time.

## AWS Elastic Disaster Recovery

AWS Elastic Disaster Recovery (Elastic Disaster Recovery) minimizes downtime and data loss with fast, reliable recovery of on-premises and cloud-based applications using affordable storage, minimal compute, and point-in-time recovery.

You can increase IT resilience when you use AWS Elastic Disaster Recovery to replicate on-premises or cloud-based applications running on supported operating systems. Use the AWS Management Console to configure replication and launch settings, monitor data replication, and launch instances for drills or recovery.

For more information, see the following resources.

- [What is Elastic Disaster Recovery?](../../../drs/latest/userguide/what-is-drs.md "../../../drs/latest/userguide/what-is-drs.md")
- [Disaster recovery for SAP workloads on AWS using AWS Elastic Disaster Recovery](../general/dr-sap.md "../general/dr-sap.md")
