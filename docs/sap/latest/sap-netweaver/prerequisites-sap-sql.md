# Prerequisites

## Specialized Knowledge

Before you follow the instructions in this guide, we recommend that you become familiar with the following AWS services. (If you are new to AWS, see [Getting Started with AWS](https://aws.amazon.com/getting-started/ "https://aws.amazon.com/getting-started/").)

- [Amazon EC2](https://aws.amazon.com/documentation/ec2/ "https://aws.amazon.com/documentation/ec2/")
- [Amazon EBS](../../../AWSEC2/latest/UserGuide/AmazonEBS.md "../../../AWSEC2/latest/UserGuide/AmazonEBS.md")
- [Amazon FSx](https://aws.amazon.com/fsx/ "https://aws.amazon.com/fsx/")
- [Amazon VPC](https://aws.amazon.com/documentation/vpc/ "https://aws.amazon.com/documentation/vpc/")
- [AWS CloudFormation](https://aws.amazon.com/documentation/cloudformation/ "https://aws.amazon.com/documentation/cloudformation/")
- [AWS Systems Manager](../../../systems-manager/latest/APIReference/Welcome.md "../../../systems-manager/latest/APIReference/Welcome.md")
- [Amazon Simple Storage Service (Amazon S3)](../../../AmazonS3/latest/dev/Welcome.md "../../../AmazonS3/latest/dev/Welcome.md")
- [AWS Identity and Access Management (IAM)](../../../IAM/latest/UserGuide/introduction.md "../../../IAM/latest/UserGuide/introduction.md")

## Technical Requirements

Before you start to deploy Microsoft SQL Server database for SAP applications on AWS, ensure that you meet the following requirements:

- Windows Server 2008 R2, 2012 R2, or 2016 operating system
- Microsoft SQL Server 2008 R2 or higher database
- Install [AWS SAP Data provider](../general/aws-data-provider.md "../general/aws-data-provider.md") on Amazon EC2 instances after installing SQL Server database
- If you plan to deploy domain installation, you should have a user ID that is a member of domain admins. Otherwise, the domain admin should create groups and user IDs (such as <sapsid>adm, SAPService<SAPSID>, and so on) as required for SAP in advance. See [SAP installation guide](https://help.sap.com/viewer/nwguidefinder "https://help.sap.com/viewer/nwguidefinder") for more details.
- AWS Account with permission to create resources.
- Access to SAP installation media for database and application
- AWS Business Support or AWS Enterprise Support plan
