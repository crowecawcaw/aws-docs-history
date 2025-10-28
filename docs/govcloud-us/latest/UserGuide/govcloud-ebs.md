# Amazon EBS in AWS GovCloud (US)

Amazon Elastic Block Store (Amazon EBS) provides block level storage volumes for use with EC2 instances. EBS volumes are highly available and reliable storage volumes that can be attached to any running instance that is in the same Availability Zone. EBS volumes that are attached to an EC2 instance are exposed as storage volumes that persist independently from the life of the instance. With Amazon EBS, you pay only for what you use.

## How Amazon Elastic Block Store differs for AWS GovCloud (US)

- The [copy snapshot commands](../../../AWSEC2/latest/UserGuide/ebs-copy-snapshot.md "../../../AWSEC2/latest/UserGuide/ebs-copy-snapshot.md")
  can be used, but only allow you to copy snapshots available to your account within AWS GovCloud (US) Regions.
  If you specify a source or destination Region to copy to or from, the commands will return an error.
- Use SSL (HTTPS) when you make calls to the service in AWS GovCloud (US) Regions. In other AWS Regions, you can use HTTP or HTTPS.
- Amazon EBS Multi-Attach is not available.

## Documentation for Amazon Elastic Block Store

For more information related to EBS Data LifeCycle Manager (DLM), see [Amazon EBS Snapshot Lifecyle](../../../AWSEC2/latest/UserGuide/snapshot-lifecycle.md "../../../AWSEC2/latest/UserGuide/snapshot-lifecycle.md").

For Amazon EBS User Guide, see [Amazon Elastic Block Store documentation](../../../AWSEC2/latest/UserGuide/AmazonEBS.md "../../../AWSEC2/latest/UserGuide/AmazonEBS.md").

## Export-controlled content

For AWS Services architected within the AWS GovCloud (US) Regions, the following list explains
how certain components of data may leave the AWS GovCloud (US) Regions in the normal course of the service offerings.
The list can be used as a guide to help meet applicable customer compliance obligations.
Data not included in the following list remains within the AWS GovCloud (US) Regions.

- Amazon EBS metadata is not permitted to contain export-controlled data. This
  metadata includes all configuration data that you enter when creating and
  maintaining your Amazon EBS volumes.
- Do not enter export-controlled data in the following fields:
  - Volume names
  - Snapshot names
  - Image names
  - Image descriptions
