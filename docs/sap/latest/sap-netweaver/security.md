

# Security
<a name="security"></a>

 AWS provides several [security capabilities](https://aws.amazon.com/security/) and services to securely run your SAP applications on AWS platform. In the context of SQL Server for SAP applications, you can use network services and features such as Amazon VPC, AWS Virtual Private Network, AWS Direct Connect, and Amazon EC2 [security groups, network access controls, route tables,](https://docs.aws.amazon.com/vpc/latest/userguide/VPC_Security.html) and so on, to restrict the access to your database.

## Network Security
<a name="network-security"></a>

Generally, databases for SAP applications do not require direct user access. We recommend that you only allow network traffic to the Amazon EC2 instance running SQL Server from Amazon EC2 instances running SAP application servers (PAS/AAS) and ASCS/SCS.

By default, SQL Server receives communication on TCP port 1433. Depending on your VPC design, you should configure Amazon EC2 security groups, NACLs, and route tables to allow traffic to TCP Port 1433 from SAP application servers (PAS/AAS) and ASCS/SCS.

## Encryption
<a name="encryption"></a>

We recommend that you encrypt your data stored in AWS storage services. See the following documentation for more details:
+  [Encrypting Data at Rest and in Transit for Amazon FSx](https://docs.aws.amazon.com/fsx/latest/WindowsGuide/encryption.html) 
+  [Protecting S3 objects using encryption](https://docs.aws.amazon.com/AmazonS3/latest/dev/UsingEncryption.html) 
+  [Amazon EBS Encryption](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/EBSEncryption.html) 