# AWS Elastic Disaster Recovery in AWS GovCloud (US)

AWS Elastic Disaster Recovery minimizes downtime and data loss with fast, reliable recovery of on-premises and cloud-based applications using affordable storage, minimal compute, and point-in-time recovery.

## How AWS Elastic Disaster Recovery differs for AWS GovCloud (US)

- In AWS GovCloud (US) Regions, you must launch all Amazon EC2 instances for recovery, drill, failback and AWS Elastic Disaster Recovery service resources in an Amazon Virtual Private Cloud (Amazon VPC). In some cases, your account might have a default VPC; otherwise, you must create a VPC before launching instances or setting up the AWS Elastic Disaster Recovery staging area.
- Use SSL (HTTPS) or Federal Information Processing System (FIPS) protocols when you make calls to the service in the AWS GovCloud (US) Regions (us-gov-west-1, us-gov-east-1). In other AWS Regions, you can use HTTP or HTTPS.
- Cross-Partition failback features between commercial and AWS GovCloud (US) partitions are not supported. Cross-Region failback features within the AWS GovCloud (US) partition are available between AWS GovCloud (US) Regions (us-gov-west-1 and us-gov-east-1).
- AWS Elastic Disaster Recovery source servers can only be extended to other GovCloud AWS accounts when using multiple staging accounts.
- AWS Elastic Disaster Recovery trusted account features are only supported between other GovCloud AWS accounts.
- The Provisioned IOPS SSD (io2) EBS volume type is not available in the AWS GovCloud (US) Regions.
- AWS Elastic Disaster Recovery leverages the following AWS services in AWS GovCloud (US). Please refer to the individual service for GovCloud differentiators:
  - [Amazon EC2](govcloud-ec2.md "govcloud-ec2.md")
  - [AWS Key Management Service](govcloud-kms.md "govcloud-kms.md")
  - [Amazon EBS](govcloud-ebs.md "govcloud-ebs.md")
  - [Amazon VPC](govcloud-vpc.md "govcloud-vpc.md")
  - [AWS Direct Connect](govcloud-dc.md "govcloud-dc.md")
  - [AWS Site-to-Site VPN](govcloud-vpn.md "govcloud-vpn.md")
  - [AWS Systems Manager](govcloud-ssm.md "govcloud-ssm.md")
  - [Cloudwatch](govcloud-cw.md "govcloud-cw.md")

## Documentation for AWS Elastic Disaster Recovery

[AWS Elastic Disaster Recovery documentation](../../../drs/latest/userguide/what-is-drs.md "../../../drs/latest/userguide/what-is-drs.md").

## Determining if your account has a default Amazon VPC

In AWS GovCloud (US) Regions, you must launch all Amazon EC2 instances in an Amazon Virtual Private Cloud (Amazon VPC). In some cases, your account might have a default VPC, where you launch all your Amazon EC2 instances. If your account doesn't have a default VPC, you must create a VPC before you can launch Amazon EC2 instances. For more information, see [What is Amazon VPC?](../../../vpc/latest/userguide/what-is-amazon-vpc.md "../../../vpc/latest/userguide/what-is-amazon-vpc.md") in the Amazon VPC User Guide.

If you don't want a default VPC for your AWS Elastic Disaster Recovery account in AWS GovCloud (US), you can delete the default VPC and default subnets. The default VPC and subnets will not be recreated. However, you still need to create a VPC before launching instances.

If you deleted your default VPC, you can create a new one. For more information, see [Creating a Default VPC](../../../vpc/latest/userguide/default-vpc.md#create-default-vpc "../../../vpc/latest/userguide/default-vpc.md#create-default-vpc").

## Export-controlled content

For AWS Services architected within the AWS GovCloud (US) Regions, the following list explains how certain components of data may leave the AWS GovCloud (US) Regions in the normal course of the service offerings. The list can be used as a guide to help meet applicable customer compliance obligations. Data not included in the following list remains within the AWS GovCloud (US) Regions.

- Amazon EC2 metadata is not permitted to contain export-controlled data. This metadata includes all configuration data that you enter when creating and maintaining your AWS Elastic Disaster Recovery source servers.
- Do not enter export-controlled data in the following fields:
  - Source server names
  - Key and Value of Tags associated with your resources.
  - Name and Description of Security Groups and Security Group Rules
  - Refer to AWS Elastic Disaster Recovery leveraged AWS services for service-specific export-controlled data fields.
