# Security & Compliance

The following AWS security resources help you achieve the level of security you require for your SAP NetWeaver environment on AWS:

- [AWS Cloud Security](https://aws.amazon.com/security/ "https://aws.amazon.com/security/")
- [CIS AWS Foundations Benchmark](../../../securityhub/latest/userguide/securityhub-standards-cis.md "../../../securityhub/latest/userguide/securityhub-standards-cis.md")
- [Introduction to AWS Security](../../../whitepapers/latest/introduction-aws-security/welcome.md "../../../whitepapers/latest/introduction-aws-security/welcome.md")
- [Best Practices for Security, Identity, & Compliance](https://aws.amazon.com/architecture/security-identity-compliance/ "https://aws.amazon.com/architecture/security-identity-compliance/")
- [https://d1.awsstatic.com/whitepapers/architecture/](https://d1.awsstatic.com/whitepapers/architecture/ "https://d1.awsstatic.com/whitepapers/architecture/")
  AWS-Security-Pillar.pdf[AWS Well-Architected Framework Security Pillar]
- [Network and security features for Windows and Amazon EC2](../../../AWSEC2/latest/WindowsGuide/ec2-network-and-security.md "../../../AWSEC2/latest/WindowsGuide/ec2-network-and-security.md")

## OS Hardening

You may want to lock down the OS configuration further, for example, to avoid providing a NetWeaver administrator with root credentials when logging into an instance.

We provide guidance on how to best secure your Windows EC2 instances:

- Read our [best practices guide for securing Windows on EC2](https://aws.amazon.com/answers/security/aws-securing-windows-instances/ "https://aws.amazon.com/answers/security/aws-securing-windows-instances/")
- Use [Amazon Inspector](https://aws.amazon.com/inspector/faqs/ "https://aws.amazon.com/inspector/faqs/"), an automated security assessment service that helps you test the network accessibility of your Amazon EC2 instances and the security state of your applications running on the instances.

## Encryption

Security is a priority on AWS. A core aspect of securing your workloads is encrypting your data, both at rest and in transit.

When you create an [encrypted EBS volume](../../../AWSEC2/latest/UserGuide/EBSEncryption.md "../../../AWSEC2/latest/UserGuide/EBSEncryption.md") and attach it to a supported instance type, the following types of data are encrypted:

- Data at rest inside the volume
- All data in transit between the volume and the instance
- All snapshots created from the volume
- All volumes created from those snapshots

Encryption operations occur on the servers that host EC2 instances, ensuring the security of both data at rest and data in transit between an instance and its attached EBS storage. You can expect the same IOPS performance on encrypted volumes as on unencrypted volumes, with a minimal effect on latency. Encryption and decryption are handled transparently and they require no additional action from you or your applications.

Similarly, all Amazon FSx file systems are encrypted at rest with keys managed using AWS Key Management Service (AWS KMS). Data is automatically encrypted before being written to the file system, and automatically decrypted as it is read. These processes are handled transparently by Amazon FSx, so you don’t have to modify your applications.

For Amazon S3, you can protect data in transit by using SSL or client-side encryption, and protect data at rest by using either server-side encryption or client-side encryption.

You can find more information about encryption from the specific service documentation:

- [Encrypting Amazon FSx Data at Rest and Data in Transit](../../../fsx/latest/WindowsGuide/encryption.md "../../../fsx/latest/WindowsGuide/encryption.md")
- [Protecting Amazon S3 Data Using Encryption](../../../AmazonS3/latest/dev/UsingEncryption.md "../../../AmazonS3/latest/dev/UsingEncryption.md")
- [Amazon EBS Encryption](../../../AWSEC2/latest/UserGuide/EBSEncryption.md "../../../AWSEC2/latest/UserGuide/EBSEncryption.md")

## Security Groups/Network ACLs

A [security group](../../../vpc/latest/userguide/VPC_SecurityGroups.md "../../../vpc/latest/userguide/VPC_SecurityGroups.md") acts as a virtual firewall for your instance to control inbound and outbound traffic. Security groups act at the instance level, not the subnet level.

Customers often separate the SAP system into multiple subnets, with the database in a separate subnet to the application servers, and other components such as a Web Dispatcher in another subnet, possibly with external access.

If you scale workloads horizontally or require high availability, you may choose to include multiple, functionally similar, EC2 instances in the same security group. In this case, you’ll need to add a rule to your security groups.

Some configuration changes may be necessary in the security groups, route tables, and network ACLs. You can refer to the operating system product documentation, or other sources such as the [Security Group Rules Reference](../../../AWSEC2/latest/UserGuide/security-group-rules-reference.md "../../../AWSEC2/latest/UserGuide/security-group-rules-reference.md") in the Amazon Elastic Compute Cloud (EC2) documentation, for more information.

A [network access control list (ACL)](../../../vpc/latest/userguide/vpc-network-acls.md "../../../vpc/latest/userguide/vpc-network-acls.md") is an optional layer of security for your VPC that acts as a firewall for controlling traffic in and out of one or more subnets (they’re stateless firewalls at the subnet level). You may set up network ACLs with rules similar to your security groups in order to add an additional layer of security to your VPC.

## API Call Logging

[AWS CloudTrail](https://aws.amazon.com/cloudtrail/ "https://aws.amazon.com/cloudtrail/") is a web service that records AWS API calls for your account and delivers log files to you. The recorded information includes the identity of the API caller, the time of the API call, the source IP address of the API caller, the request parameters, and the response elements returned by the AWS service.

With AWS CloudTrail, you can get a history of AWS API calls for your account, including API calls made via the AWS Management Console, AWS SDKs, command line tools, and higher-level AWS services (such as AWS CloudFormation). The AWS API call history produced by CloudTrail enables security analysis, resource change tracking, and compliance auditing.

## Notifications on Access

You can use Amazon Simple Notification Service (Amazon SNS) or third-party applications to set up notifications on SSH login to your email address or mobile phone.
