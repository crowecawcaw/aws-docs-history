

# Prerequisites
<a name="bobi-windows-prerequisites"></a>

Before you start implementing your SAP BOBI Platform systems, we recommend that you review these prerequisites to ensure there are minimal interruptions and delays.

## Recommended Reading
<a name="bobi-windows-recommended-reading"></a>

We also recommend you first read some key overview and best practice guides:
+  [SAP on AWS Overview and Planning Guide](https://docs.aws.amazon.com/sap/latest/general/sap-on-aws-overview.html) 
+  [Getting Started with Architecting SAP on the AWS Cloud](https://aws.amazon.com/blogs/awsforsap/getting-started-with-architecting-sap-on-the-aws-cloud/) 
+  [Best Practices for Windows on Amazon EC2](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-best-practices.html) 

SAP Notes listed in the following table have useful information regarding SAP BOBI deployment in AWS.


**SAP Notes for SAP BOBI deployment on AWS**  

| SAP Note | Description | 
| --- | --- | 
|  [1588667](https://me.sap.com/notes/1588667)  | SAP on AWS: Overview of related SAP notes and web links | 
|  [1656099](https://me.sap.com/notes/1656099)  | SAP on AWS: Supported products, platforms, and landscapes | 
|  [2442979](https://me.sap.com/notes/2442979)  | Amazon S3 recommendations for SAP BusinessObjects Business Intelligence Platform | 
|  [2438592](https://me.sap.com/notes/2438592)  | BI Platform 4.2 Cloud Support | 

## Technical Requirements
<a name="bobi-windows-technical-requirements"></a>
+ Ensure that any services you will use for your SAP BOBI Platform deployment are not constrained by default AWS service limits. You can find the details at [AWS Service Limits](https://docs.aws.amazon.com/general/latest/gr/aws_service_limits.html). You can increase soft limits by submitting a support ticket to AWS.
+ Make sure that the following information is available in relevance to your existing AWS resources. You will need this information while executing AWS Command Line Interface (AWS CLI) commands to create your Amazon EC2 and Amazon Elastic Block Store (Amazon EBS) resources:


<table>
<thead>
  <tr><th>Information You Need</th><th>Description</th></tr>
</thead>
<tbody>
  <tr><td>Region ID</td><td> AWS Region where you want to deploy your AWS resources.</td></tr>
  <tr><td>Availability Zone</td><td> <a href="https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-regions-availability-zones.html">Availability Zone</a> within your target region where you want to deploy your resources.</td></tr>
  <tr><td>Amazon VPC ID</td><td>Amazon Virtual Private Cloud (Amazon VPC) where you want to deploy your Amazon EC2 instance for SAP installation.</td></tr>
  <tr><td>Subnet ID</td><td>Subnet where you want to deploy your Amazon EC2 instance.</td></tr>
  <tr><td>AMI ID</td><td>Amazon Machine Image (AMI) that will be used to launch your Amazon EC2 instance. You can find latest Windows AMIs on <a href="https://aws.amazon.com/marketplace/b/2649367011?page=1&amp;filters=operating_system&amp;operating_system=SUSE%2CRHEL">AWS Marketplace</a>.</td></tr>
  <tr><td>Key Pair</td><td>Make sure that you have generated the key pair in your target region, and that you have access to the private key.</td></tr>
  <tr><td>Security Group ID</td><td>Name of the security group that you want to assign to your Amazon EC2 instance.</td></tr>
  <tr><td>Access key ID</td><td>Access key for your AWS account that will be used with AWS CLI tools.</td></tr>
  <tr><td>Secret access key</td><td>Secret key for your AWS account that will be used with AWS CLI CLI tools.</td></tr>
</tbody>
</table>

  + Ensure that you have a key pair that you can use to launch your Amazon EC2 instances. See [Amazon EC2 Key Pairs and Windows Instances](https://docs.aws.amazon.com/AWSEC2/latest/WindowsGuide/ec2-key-pairs.html) if you need to create a key.
  + Ensure that you have the network details like VPC ID, Subnet ID, and so on, of the VPC where you plan to launch your Amazon EC2 instances to host your SAP BOBI Platform applications.
  + Ensure that the required ports are open on the security group attached to your Amazon EC2 instance to allow log in to the operating system.
  + For distributed or high availability (HA) installations, ensure that the security group attached to each application servers allows communication over the required ports between them. The easiest way to do this is to create a rule that references a security group as its own source and allow traffic on the required ports for that rule.
+ If you intend to use the AWS CLI to launch your instances, then ensure that you have installed and configured AWS CLI with the appropriate credentials. See [Configuring the AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-getting-started.html) for more details.
+ If you intend to use the AWS Management Console to launch your instances, then ensure that your IAM user has permission to launch and configure Amazon EC2, Amazon EBS, and so on. See the [IAM documentation](https://docs.aws.amazon.com/IAM/latest/UserGuide/introduction.html) for more details.
+ Ensure that you have the required SAP software available either via an Amazon Simple Storage Service (Amazon S3) bucket or on a file share accessible from an Amazon EC2 instance. If you use Amazon S3, make sure to assign appropriate IAM role permissions to the EC2 instance to allow S3 access.
+ All enterprise customers use DNS service. You can create a hosted zone in Amazon Route 53. You can optionally use AWS Directory Service for Microsoft Active Directory, also known as AWS Managed Microsoft AD. This service lets your directory-aware workloads and AWS resources use managed Active Directory in the AWS Cloud. For more details on this service, see [AWS Directory Service](https://aws.amazon.com/directoryservice/) and [Create Your AWS Managed Microsoft AD directory](https://docs.aws.amazon.com/directoryservice/latest/admin-guide/ms_ad_getting_started_create_directory.html).