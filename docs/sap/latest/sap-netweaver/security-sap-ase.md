# Security and compliance

The following are additional AWS security resources to help you achieve the optimum level of security for your SAP NetWeaver environment on AWS:

- [AWS Cloud Security](https://aws.amazon.com/security/ "https://aws.amazon.com/security/")
- [CIS AWS Foundations](https://d0.awsstatic.com/whitepapers/compliance/AWS_CIS_Foundations_Benchmark.pdf "https://d0.awsstatic.com/whitepapers/compliance/AWS_CIS_Foundations_Benchmark.pdf")
- [AWS Well-Architected Framework](../../../wellarchitected/latest/security-pillar/welcome.md "../../../wellarchitected/latest/security-pillar/welcome.md")

## Infrastructure hardening

In some cases, you can further lock down the operating system configuration. For instance, to avoid sharing the credentials of your AWS account with an SAP administrator who needs to log on to an Amazon EC2 instance. Refer to [Security in Amazon EC2](../../../AWSEC2/latest/UserGuide/ec2-security.md "../../../AWSEC2/latest/UserGuide/ec2-security.md") and [Best Practice 6.2 – Build and protect the operating system](../../../wellarchitected/latest/sap-lens/best-practice-6-2.md "../../../wellarchitected/latest/sap-lens/best-practice-6-2.md") to learn more.

You can also use an automated solution provided by AWS – [Amazon Inspector](https://aws.amazon.com/inspector/ "https://aws.amazon.com/inspector/").

## Encryption

The important aspect of securing your workloads is encrypting your data, both at rest and in transit. For more details, refer to the following resources.

- [Amazon EBS encryption](../../../AWSEC2/latest/UserGuide/EBSEncryption.md "../../../AWSEC2/latest/UserGuide/EBSEncryption.md")
- [Data encryption in Amazon EFS](../../../efs/latest/ug/encryption.md "../../../efs/latest/ug/encryption.md")
- [Data encryption in Amazon S3](../../../AmazonS3/latest/userguide/UsingEncryption.md "../../../AmazonS3/latest/userguide/UsingEncryption.md")
- [Protect your SAP data at rest and in transit](../../../wellarchitected/latest/sap-lens/design-principle-8.md "../../../wellarchitected/latest/sap-lens/design-principle-8.md")

_You can also refer to the following SAP resources._

- _[SAP Note 2481596 – SYB: Encrypted data transfer between SAP system and SAP ASE database](https://launchpad.support.sap.com/#/notes/2481596 "https://launchpad.support.sap.com/#/notes/2481596") (requires SAP portal access)_
- [SAP Adaptive Server Enterprise – Database Encryption](https://help.sap.com/docs/SAP_ASE/833788dd3e9c413799014a0fd002d0b2/a7b86bb3bc2b1014b9b08178723a5ee2.html "https://help.sap.com/docs/SAP_ASE/833788dd3e9c413799014a0fd002d0b2/a7b86bb3bc2b1014b9b08178723a5ee2.html")

## Security group

A [security group](../../../vpc/latest/userguide/VPC_SecurityGroups.md "../../../vpc/latest/userguide/VPC_SecurityGroups.md") acts as a virtual firewall for your instance to control inbound and outbound traffic. Security groups act at the instance level, not the subnet level.

SAP system is often separated into multiple subnets, with the database in a separate subnet to the application servers, and other components, such as a web dispatcher in another subnet, possibly with external access.

If workloads are scaled horizontally, or high availability is necessary, you may choose to include multiple, functionally similar, Amazon EC2 instances in the same security group. In this case, you must add a rule to your security groups.

If Linux is used, some configuration changes may be necessary in the security groups, route tables, and network ACLs. For more information, see [Security group rules for different use cases](../../../AWSEC2/latest/UserGuide/security-group-rules-reference.md "../../../AWSEC2/latest/UserGuide/security-group-rules-reference.md").

## Network ACL

A [network access control list (ACL)](../../../vpc/latest/userguide/vpc-network-acls.md "../../../vpc/latest/userguide/vpc-network-acls.md") is an optional layer of security for your Amazon VPC that acts as a firewall for controlling traffic in and out of one or more subnets (they’re stateless firewalls at the subnet level). You may set up network ACLs with rules similar to your security groups in order to add an additional layer of security to your Amazon VPC.

See [Amazon VPC Subnet Zoning Patterns for SAP on AWS](https://aws.amazon.com/blogs/awsforsap/vpc-subnet-zoning-patterns-for-sap-on-aws/ "https://aws.amazon.com/blogs/awsforsap/vpc-subnet-zoning-patterns-for-sap-on-aws/") to understand the network considerations for SAP workloads.

## API call logging

AWS CloudTrail is a web service that records AWS API calls for your account and delivers log files to you. The recorded information includes the identity of the caller, time of the call, source IP address, request parameters, and response elements returned by the AWS service. With CloudTrail, you can get a history of AWS API calls for your account, including API calls made via AWS Management Console, AWS SDKs, command line tools, and higher-level AWS services (such as, AWS CloudFormation). The AWS API call history produced by CloudTrail enables security analysis, resource change tracking, and compliance auditing.

For more information, see [What Is AWS CloudTrail?](../../../awscloudtrail/latest/userguide/cloudtrail-user-guide.md "../../../awscloudtrail/latest/userguide/cloudtrail-user-guide.md")

## Notification on access

You can use [Amazon SNS](https://aws.amazon.com/sns "https://aws.amazon.com/sns") or any third-party application to set up notifications on SSH login to your email address or mobile phone.
