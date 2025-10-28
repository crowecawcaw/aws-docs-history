# ADVREL07-BP02 Implement a backup strategy which would meet RTO and RPO objectives

Develop comprehensive backup strategies, focusing on data
classification and meeting Recovery Time Objective (RTO) and
Recovery Point Objective (RPO) requirements through appropriate
service selection.

## Implementation guidance

Review the data related to your workload and classify the data
according to usage, retention, and availability needs. Example
classifications might be user profile info, campaign data,
reporting data. Consider how those different data classes are
used within your workload and how the availability of that data
can impact your workload's operation. Use those classifications
to determine the RPO and RTO requirements for your workload.
Identify the AWS services that can meet your requirements, and
deploy resources to the Regions or Availability Zones that can
achieve your RTO and RPO targets. Test the backup and
restoration process to verify that your backup and recovery
strategies will work during a disruptive event.

## Key AWS services

- [AWS Backup](https://aws.amazon.com/backup/ "https://aws.amazon.com/backup/")
- [Amazon EBS](https://aws.amazon.com/ebs/ "https://aws.amazon.com/ebs/")
- [Amazon EC2](https://aws.amazon.com/ec2/ "https://aws.amazon.com/ec2/")
- [Amazon Relational Database Service](https://aws.amazon.com/rds/ "https://aws.amazon.com/rds/")
- [Amazon Elastic File System](https://aws.amazon.com/efs/ "https://aws.amazon.com/efs/")

## Resources

- [Disaster
  Recovery (DR) Architecture on AWS, Part II: Backup and Restore with Rapid Recovery](https://aws.amazon.com/blogs/architecture/disaster-recovery-dr-architecture-on-aws-part-ii-backup-and-restore-with-rapid-recovery/index.html "https://aws.amazon.com/blogs/architecture/disaster-recovery-dr-architecture-on-aws-part-ii-backup-and-restore-with-rapid-recovery/index.html")
- Establishing
  RPO and RTO Targets for Cloud Applications
