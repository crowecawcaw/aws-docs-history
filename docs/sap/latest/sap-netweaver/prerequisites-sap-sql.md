

# Prerequisites
<a name="prerequisites-sap-sql"></a>

## Specialized Knowledge
<a name="specialized-knowledge"></a>

Before you follow the instructions in this guide, we recommend that you become familiar with the following AWS services. (If you are new to AWS, see [Getting Started with AWS](https://aws.amazon.com/getting-started/).)
+  [Amazon EC2](https://aws.amazon.com/documentation/ec2/) 
+  [Amazon EBS](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/AmazonEBS.html) 
+  [Amazon FSx](https://aws.amazon.com/fsx/) 
+  [Amazon VPC](https://aws.amazon.com/documentation/vpc/) 
+  [AWS CloudFormation](https://aws.amazon.com/documentation/cloudformation/) 
+  [AWS Systems Manager](https://docs.aws.amazon.com/systems-manager/latest/APIReference/Welcome.html) 
+  [Amazon Simple Storage Service (Amazon S3)](https://docs.aws.amazon.com/AmazonS3/latest/dev/Welcome.html) 
+  [AWS Identity and Access Management (IAM)](https://docs.aws.amazon.com/IAM/latest/UserGuide/introduction.html) 

## Technical Requirements
<a name="technical-requirements"></a>

Before you start to deploy Microsoft SQL Server database for SAP applications on AWS, ensure that you meet the following requirements:
+ Windows Server 2008 R2, 2012 R2, or 2016 operating system
+ Microsoft SQL Server 2008 R2 or higher database
+ Install [AWS SAP Data provider](https://docs.aws.amazon.com/sap/latest/general/aws-data-provider.html) on Amazon EC2 instances after installing SQL Server database
+ If you plan to deploy domain installation, you should have a user ID that is a member of domain admins. Otherwise, the domain admin should create groups and user IDs (such as <sapsid>adm, SAPService<SAPSID>, and so on) as required for SAP in advance. See [SAP installation guide](https://help.sap.com/viewer/nwguidefinder) for more details.
+  AWS Account with permission to create resources.
+ Access to SAP installation media for database and application
+  AWS Business Support or AWS Enterprise Support plan