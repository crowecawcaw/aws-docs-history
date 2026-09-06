

# Security and Compliance
<a name="net-win-security-and-compliance"></a>

These additional AWS security resources can help you achieve the level of security that you require for your SAP NetWeaver environment on AWS:
+  [AWS Cloud Security Center](https://aws.amazon.com/security/) 
+  [CIS AWS Foundations Benchmark](https://docs.aws.amazon.com/securityhub/latest/userguide/cis-aws-foundations-benchmark.html) 
+  [Introduction to AWS Security](https://docs.aws.amazon.com/whitepapers/latest/introduction-aws-security/welcome.html) 
+  [AWS Well-Architected Framework Security Pillar](https://docs.aws.amazon.com/wellarchitected/latest/security-pillar/welcome.html) 
+  [Network and Security topic](https://docs.aws.amazon.com/AWSEC2/latest/WindowsGuide/ec2-network-and-security.html) from the *Amazon EC2 User Guide for Windows Instances* 

## OS Hardening
<a name="net-win-os-hardening"></a>

You may want to lock down the OS configuration further, for example, to avoid providing a NetWeaver administrator with root credentials when logging into an instance.

We provide guidance on how to best secure your Windows EC2 instances:
+ Read our [best practices guide for securing Windows on EC2](https://aws.amazon.com/answers/security/aws-securing-windows-instances/).
+ Read our general [best practices guide for securing EC2 instances](https://aws.amazon.com/answers/security/aws-securing-ec2-instances/).
+ Use [Amazon Inspector](https://aws.amazon.com/inspector/faqs/), an automated security assessment service that helps you test the network accessibility of your EC2 instances and the security state of your applications running on the instances.

You can also refer to the following SAP note:
+  [1837765](https://me.sap.com/notes/1837765): Security policies for <SID>adm and SapService<SID> on Windows

## Encryption
<a name="net-win-encryption"></a>

Cloud security at AWS is the highest priority. A core aspect of securing your workloads is encrypting your data—​both at rest and in transit.

When you create an [encrypted EBS volume](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/EBSEncryption.html) and attach it to a supported instance type, the following types of data are encrypted:
+ Data at rest inside the volume
+ All data moving between the volume and the instance
+ All snapshots created from the volume
+ All volumes created from those snapshots

Encryption operations occur on the servers that host EC2 instances, ensuring the security of both data at rest, and data in transit between an instance and its attached EBS storage. You can expect the same IOPS performance on encrypted volumes as on unencrypted volumes, with a minimal effect on latency. Encryption and decryption are handled transparently and require no additional action from you or your applications.

Similarly, all Amazon FSx file systems are encrypted at rest with keys that are managed using AWS Key Management Service (AWS KMS). Data is automatically encrypted before being written to the file system, and automatically decrypted as it is read. These processes are handled transparently by Amazon FSx, so that you don’t have to modify your applications.

For Amazon S3, you can protect data in transit by using SSL/TLS or client-side encryption, and protect data at rest by using either server-side or client-side encryption.

You can find more information about encryption from the specific service documentation:
+  [Encrypting Amazon FSx Data at Rest and Data in Transit](https://docs.aws.amazon.com/fsx/latest/WindowsGuide/encryption.html) 
+  [Protecting Amazon S3 Data Using Encryption](https://docs.aws.amazon.com/AmazonS3/latest/dev/UsingEncryption.html) 
+  [Amazon EBS Encryption](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/EBSEncryption.html) 

## Security Groups / NACLs
<a name="net-win-security-groups-nacls"></a>

A [security group](https://docs.aws.amazon.com/vpc/latest/userguide/VPC_SecurityGroups.html) acts as a virtual firewall for your instance to control inbound and outbound traffic. Security groups act at the instance level, not the subnet level.

Customers often separate the SAP system into multiple subnets, with the database in a subnet separate from the application servers, and other components, such as a Web Dispatcher, in another subnet—​possibly with external access.

If workloads are scaled horizontally, or high availability is necessary, you might consider including multiple, functionally similar, EC2 instances in the same security group. In this case, you’ll need to add a rule to your security groups.

If Microsoft Windows Server is used, some configuration changes may be necessary in the security groups, route tables, and network access control lists (ACLs). You can refer to the operating system product documentation or other sources, such as the [Security Group Rules Reference](https://docs.aws.amazon.com/AWSEC2/latest/WindowsGuide/security-group-rules-reference.html) in the Amazon EC2 documentation, for more information.

A [network access control list (ACL)](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-network-acls.html) is an optional layer of security for your VPC that acts as a firewall for controlling traffic in and out of one or more subnets (they’re stateless firewalls at the subnet level). You might set up network ACLs with rules similar to your security groups in order to add an additional layer of security to your VPC.

For further information on network considerations for SAP workloads, see our SAP on AWS network documentation.

## API Call Logging
<a name="net-win-api-call-logging"></a>

 AWS CloudTrail is a web service that records AWS API calls for your account and delivers log files to you. The information recorded includes the identity of the API caller, the time of the API call, the source IP address of the API caller, the request parameters, and the response elements returned by the AWS service.

With CloudTrail, you can get a history of AWS API calls for your account, including API calls made via the AWS Management Console, AWS SDKs, command line tools, and higher-level AWS services, such as AWS CloudFormation. The AWS API call history provided by CloudTrailenables security analysis, resource change tracking, and compliance auditing.

## Notifications on Access
<a name="net-win-notifications-on-access"></a>

You can use Amazon Simple Notification Service (Amazon SNS) or third-party applications to send notifications about SSH logins to your email address or mobile phone number.