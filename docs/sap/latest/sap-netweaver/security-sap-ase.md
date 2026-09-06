

# Security and compliance
<a name="security-sap-ase"></a>

The following are additional AWS security resources to help you achieve the optimum level of security for your SAP NetWeaver environment on AWS:
+  [AWS Cloud Security](https://aws.amazon.com/security/) 
+  [CIS AWS Foundations Benchmark](https://docs.aws.amazon.com/securityhub/latest/userguide/cis-aws-foundations-benchmark.html) 
+  [AWS Well-Architected Framework](https://docs.aws.amazon.com/wellarchitected/latest/security-pillar/welcome.html) 

## Infrastructure hardening
<a name="infrastructure-sap-ase"></a>

In some cases, you can further lock down the operating system configuration. For instance, to avoid sharing the credentials of your AWS account with an SAP administrator who needs to log on to an Amazon EC2 instance. Refer to [Security in Amazon EC2](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-security.html) and [Best Practice 6.2 – Build and protect the operating system](https://docs.aws.amazon.com/wellarchitected/latest/sap-lens/best-practice-6-2.html) to learn more.

You can also use an automated solution provided by AWS – [Amazon Inspector](https://aws.amazon.com/inspector/).

## Encryption
<a name="encryption-sap-ase"></a>

The important aspect of securing your workloads is encrypting your data, both at rest and in transit. For more details, refer to the following resources.
+  [Amazon EBS encryption](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/EBSEncryption.html) 
+  [Data encryption in Amazon EFS](https://docs.aws.amazon.com/efs/latest/ug/encryption.html) 
+  [Data encryption in Amazon S3](https://docs.aws.amazon.com/AmazonS3/latest/userguide/UsingEncryption.html) 
+  [Protect your SAP data at rest and in transit](https://docs.aws.amazon.com/wellarchitected/latest/sap-lens/design-principle-8.html) 

 *You can also refer to the following SAP resources.* 
+  * [SAP Note 2481596 – SYB: Encrypted data transfer between SAP system and SAP ASE database](https://me.sap.com/notes/2481596) (requires SAP portal access)* 
+  [SAP Adaptive Server Enterprise – Database Encryption](https://help.sap.com/docs/SAP_ASE/833788dd3e9c413799014a0fd002d0b2/a7b86bb3bc2b1014b9b08178723a5ee2.html) 

## Security group
<a name="security-group-sap-ase"></a>

A [security group](https://docs.aws.amazon.com/vpc/latest/userguide/VPC_SecurityGroups.html) acts as a virtual firewall for your instance to control inbound and outbound traffic. Security groups act at the instance level, not the subnet level.

SAP system is often separated into multiple subnets, with the database in a separate subnet to the application servers, and other components, such as a web dispatcher in another subnet, possibly with external access.

If workloads are scaled horizontally, or high availability is necessary, you may choose to include multiple, functionally similar, Amazon EC2 instances in the same security group. In this case, you must add a rule to your security groups.

If Linux is used, some configuration changes may be necessary in the security groups, route tables, and network ACLs. For more information, see [Security group rules for different use cases](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/security-group-rules-reference.html).

## Network ACL
<a name="network-acl-sap-ase"></a>

A [network access control list (ACL)](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-network-acls.html) is an optional layer of security for your Amazon VPC that acts as a firewall for controlling traffic in and out of one or more subnets (they’re stateless firewalls at the subnet level). You may set up network ACLs with rules similar to your security groups in order to add an additional layer of security to your Amazon VPC.

See [Amazon VPC Subnet Zoning Patterns for SAP on AWS](https://aws.amazon.com/blogs/awsforsap/vpc-subnet-zoning-patterns-for-sap-on-aws/) to understand the network considerations for SAP workloads.

## API call logging
<a name="api-log-sap-ase"></a>

 AWS CloudTrail is a web service that records AWS API calls for your account and delivers log files to you. The recorded information includes the identity of the caller, time of the call, source IP address, request parameters, and response elements returned by the AWS service. With CloudTrail, you can get a history of AWS API calls for your account, including API calls made via AWS Management Console, AWS SDKs, command line tools, and higher-level AWS services (such as, AWS CloudFormation). The AWS API call history produced by CloudTrail enables security analysis, resource change tracking, and compliance auditing.

For more information, see [What Is AWS CloudTrail?](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-user-guide.html) 

## Notification on access
<a name="notification-sap-ase"></a>

You can use [Amazon SNS](https://aws.amazon.com/sns) or any third-party application to set up notifications on SSH login to your email address or mobile phone.