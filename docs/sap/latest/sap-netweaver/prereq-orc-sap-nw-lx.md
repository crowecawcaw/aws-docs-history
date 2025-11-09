# Prerequisites

We recommend familiarizing yourself with these guides:

- [SAP on AWS Overview and Planning](../general/sap-on-aws-overview.md "../general/sap-on-aws-overview.md")
- [Getting Started with Architecting SAP on the AWS Cloud](https://aws.amazon.com/blogs/awsforsap/getting-started-with-architecting-sap-on-the-aws-cloud/ "https://aws.amazon.com/blogs/awsforsap/getting-started-with-architecting-sap-on-the-aws-cloud/")
- [Best practices for Amazon EC2](../../../AWSEC2/latest/UserGuide/ec2-best-practices.md "../../../AWSEC2/latest/UserGuide/ec2-best-practices.md")
- [Migrating Oracle Database Workloads to Oracle Linux on AWS](https://d1.awsstatic.com/whitepapers/migrating-oracle-database-workloads-to-oracle-linux-on-aws.pdf "https://d1.awsstatic.com/whitepapers/migrating-oracle-database-workloads-to-oracle-linux-on-aws.pdf")
- [Determining the IOPS Needs for Oracle Database on AWS](../../../whitepapers/latest/determining-iops-needs-oracle-db-on-aws/determining-iops-needs-oracle-db-on-aws.md "../../../whitepapers/latest/determining-iops-needs-oracle-db-on-aws/determining-iops-needs-oracle-db-on-aws.md")
- [SAP Note 2606828 - Oracle Database Roadmap for SAP NetWeaver](https://launchpad.support.sap.com/#/notes/2606828 "https://launchpad.support.sap.com/#/notes/2606828") (SAP portal access required)

## Technical requirements

Before you begin deploying Oracle database for SAP applications on AWS, ensure that you meet the following requirements:

- If necessary, request a service limit increase by creating a support ticket. This is to ensure that the AWS services required for Oracle database deployment are not constrained by the default limit. For more information, see [AWS service quotas](../../../general/latest/gr/aws_service_limits.md "../../../general/latest/gr/aws_service_limits.md"). For example, you may have to increase the Amazon EC2 instance limit before your Oracle deployment.
- You will need the following information for your existing resources while running the AWS CLI commands to create Amazon EC2 and Amazon Elastic Block Store [(Amazon EBS)](https://aws.amazon.com/ebs/ "https://aws.amazon.com/ebs/") resources.

Information| **Information** | **Description** |
| AWS Region | Region where you want to deploy your AWS resources. |
| Availability Zone (AZ) | Availability Zone within your target Region where you want to deploy your resources. |
| Amazon VPC id | Amazon VPC where you want to deploy your Amazon EC2 instances for SAP installation. |
| VPS subnet id | Subnet where you want to deploy your Amazon EC2 instances. |
| Linux AMI id | Amazon Machine Image (AMI) that will be used to launch your Amazon EC2 instances. You can find the latest Linux AMIs on [AWS Marketplace](https://aws.amazon.com/marketplace "https://aws.amazon.com/marketplace"). |
| Key pair | Make sure that you have generated the key pair in your target Region and that you have access to the private key. |
| Security group id | Name of the security group that you want to assign to your Amazon EC2 instances. |
| Access key ID | Access key for your AWS account that will be used with AWS CLI tools. |
| Secret access key | Secret key for your AWS account that will be used with AWS CLI tools. |

- Create security groups and open ports to enable communication. For existing security groups, ensure that the required ports are open. For a list of ports, refer to [TCP/IP ports of all SAP products](https://help.sap.com/viewer/ports "https://help.sap.com/viewer/ports") and [Managing Oracle Database Port Numbers](https://docs.oracle.com/database/121/SSDBI/app_port.htm#SSDBI7924 "https://docs.oracle.com/database/121/SSDBI/app_port.htm#SSDBI7924").
- Ensure that you have installed and configured AWS CLI with required credentials, if you plan to use it to launch instances. For more information, see [Installing the AWS CLI](../../../cli/latest/userguide/cli-chap-install.md "../../../cli/latest/userguide/cli-chap-install.md").
- If you plan to use the AWS Management Console, ensure that you have the essential credentials and permissions to launch and configure AWS services. For more information, see [Access management for AWS resources](../../../IAM/latest/UserGuide/access.md "../../../IAM/latest/UserGuide/access.md").
- Ensure that you have the software files required for installation readily available. You can stage these in [Amazon S3](https://aws.amazon.com/s3/ "https://aws.amazon.com/s3/") or [Amazon Elastic File System](https://aws.amazon.com/efs/ "https://aws.amazon.com/efs/") (Amazon EFS). Amazon EFS can be easily shared on all of your installation hosts. For more information, see [Create your Amazon EFS file system](../../../efs/latest/ug/gs-step-two-create-efs-resources.md "../../../efs/latest/ug/gs-step-two-create-efs-resources.md").
- Oracle for SAP on AWS is supported on an OEL OS. For more information, see [SAP Note 1656099](https://launchpad.support.sap.com/#/notes/1656099 "https://launchpad.support.sap.com/#/notes/1656099") and [SAP Note 2358420](https://launchpad.support.sap.com/#/notes/2358420 "https://launchpad.support.sap.com/#/notes/2358420") (login required). If you are currently using a different OS, you can procure licenses and perform a migration. For more information, see [Migrating Oracle Database Workloads](https://d1.awsstatic.com/whitepapers/migrating-oracle-database-workloads-to-oracle-linux-on-aws.pdf "https://d1.awsstatic.com/whitepapers/migrating-oracle-database-workloads-to-oracle-linux-on-aws.pdf"). To use AMIs published by Oracle, see [Launch an Oracle Linux instance in AWS](https://community.oracle.com/tech/apps-infra/discussion/4417739/launch-an-oracle-linux-instance-in-aws "https://community.oracle.com/tech/apps-infra/discussion/4417739/launch-an-oracle-linux-instance-in-aws").
