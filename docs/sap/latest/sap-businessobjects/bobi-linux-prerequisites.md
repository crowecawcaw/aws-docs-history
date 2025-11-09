# Prerequisites

Before you start implementing your SAP BOBI Platform systems, we recommend that you review these prerequisites to ensure there are minimal interruptions and delays.

## General AWS Knowledge

Before you follow the configuration instructions in this guide, we recommend that you become familiar with the following AWS services. (If you are new to AWS, see [Getting Started with AWS](https://aws.amazon.com/getting-started/ "https://aws.amazon.com/getting-started/").)

- [Amazon ECS](https://aws.amazon.com/documentation/ec2/ "https://aws.amazon.com/documentation/ec2/")
- [Amazon VPC](https://aws.amazon.com/documentation/vpc/ "https://aws.amazon.com/documentation/vpc/")
- [AWS Identity and Access Management](https://aws.amazon.com/iam/ "https://aws.amazon.com/iam/")
- [Amazon EBS](../../../AWSEC2/latest/UserGuide/AmazonEBS.md "../../../AWSEC2/latest/UserGuide/AmazonEBS.md")
- [Amazon S3](https://aws.amazon.com/s3/ "https://aws.amazon.com/s3/")
- [AWS Systems Manager](https://aws.amazon.com/systems-manager/ "https://aws.amazon.com/systems-manager/")
- [AWS CloudFormation](https://aws.amazon.com/documentation/cloudformation/ "https://aws.amazon.com/documentation/cloudformation/")
- [Amazon FSx for NetApp ONTAP](../../../fsx/latest/ONTAPGuide/what-is-fsx-ontap.md "../../../fsx/latest/ONTAPGuide/what-is-fsx-ontap.md")

## Recommended Reading

We also recommend you first read some key overview and best practice guides:

- [SAP on AWS Overview and Planning Guide](../general/sap-on-aws-overview.md "../general/sap-on-aws-overview.md")
- [Getting Started with Architecting SAP on the AWS Cloud](https://aws.amazon.com/blogs/awsforsap/getting-started-with-architecting-sap-on-the-aws-cloud/ "https://aws.amazon.com/blogs/awsforsap/getting-started-with-architecting-sap-on-the-aws-cloud/")
- [Best Practices for Linux on Amazon EC2](../../../AWSEC2/latest/UserGuide/ec2-best-practices.md "../../../AWSEC2/latest/UserGuide/ec2-best-practices.md")

### SAP Notes

The SAP notes listed in Table 1 have useful information regarding SAP BOBI deployment in AWS.

| Table 1: SAP Notes for SAP BOBI deployment on AWS                                                                | SAP Note                                                                         | Description |
| ---------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | ----------- |
| [1588667](https://launchpad.support.sap.com/#/notes/1588667 "https://launchpad.support.sap.com/#/notes/1588667") | SAP on AWS: Overview of related SAP notes and web links                          |
| [1656099](https://launchpad.support.sap.com/#/notes/1656099 "https://launchpad.support.sap.com/#/notes/1656099") | SAP on AWS: Supported products, platforms, and landscapes                        |
| [2442979](https://launchpad.support.sap.com/#/notes/2442979 "https://launchpad.support.sap.com/#/notes/2442979") | Amazon S3 recommendations for SAP BusinessObjects Business Intelligence Platform |
| [2438592](https://launchpad.support.sap.com/#/notes/2438592 "https://launchpad.support.sap.com/#/notes/2438592") | BI Platform 4.2 Cloud Support                                                    |

## Technical Requirements

- Ensure that any services you will use for your SAP BOBI Platform deployment are not constrained by default AWS service limits. You can find the details at [Service endpoints and quotas](../../../general/latest/gr/aws-service-information.md "../../../general/latest/gr/aws-service-information.md"). You can increase soft limits by submitting a support ticket to AWS.
- Make sure that the following information is available in relevance to your existing AWS resources. You will need this information while executing AWS Command Line Interface (AWS CLI) commands to create your Amazon EC2 and Amazon Elastic Block Store (Amazon EBS) resources:

| Information You Need | Description                                                                                                                                                                                                                                                                                                                                                        |
| -------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Region ID            | AWS Region where you want to deploy your AWS resources.                                                                                                                                                                                                                                                                                                            |
| Availability Zone    | [Availability Zone](../../../AWSEC2/latest/UserGuide/using-regions-availability-zones.md "../../../AWSEC2/latest/UserGuide/using-regions-availability-zones.md") within your target region where you want to deploy your resources.                                                                                                                                |
| Amazon VPC ID        | Amazon Virtual Private Cloud (Amazon VPC) where you want to deploy your Amazon EC2 instance for SAP installation.                                                                                                                                                                                                                                                  |
| Subnet ID            | Subnet where you want to deploy your Amazon EC2 instance.                                                                                                                                                                                                                                                                                                          |
| AMI ID               | Amazon Machine Image (AMI) that will be used to launch your Amazon EC2 instance. You can find latest Linux AMIs on [AWS Marketplace](https://aws.amazon.com/marketplace/b/2649367011?page=1&filters=operating_system&operating_system=SUSE%2CRHEL "https://aws.amazon.com/marketplace/b/2649367011?page=1&filters=operating_system&operating_system=SUSE%2CRHEL"). |
| Key Pair             | Make sure that you have generated the key pair in your target region, and that you have access to the private key.                                                                                                                                                                                                                                                 |
| Security Group ID    | Name of the security group that you want to assign to your Amazon EC2 instance.                                                                                                                                                                                                                                                                                    |
| Access key ID        | Access key for your AWS account that will be used with AWS CLI tools.                                                                                                                                                                                                                                                                                              |
| Secret access key    | Secret key for your AWS account that will be used with AWS CLI tools.                                                                                                                                                                                                                                                                                              |

    + Ensure that you have a key pair that you can use to launch your Amazon EC2 instances. See [Amazon EC2 Key Pairs for Linux Instances](../../../AWSEC2/latest/UserGuide/ec2-key-pairs.md "../../../AWSEC2/latest/UserGuide/ec2-key-pairs.md") if you need to create a key.
    + Ensure that you have the network details like VPC ID, Subnet ID, and so on, of the VPC where you plan to launch your Amazon EC2 instances to host your SAP BOBI Platform applications.
    + Ensure that the required ports are open on the security group attached to your Amazon EC2 instance to allow log in to the operating system.
    + For distributed or high availability (HA) installations, ensure that the security group attached to each application servers allows communication over the required ports between them. The easiest way to do this is to create a rule that references a security group as its own source and allow traffic on the required ports for that rule.

- If you intend to use the AWS CLI to launch your instances, then ensure that you have installed and configured AWS CLI with the appropriate credentials. See [Configuring the AWS CLI](../../../cli/latest/userguide/cli-chap-getting-started.md "../../../cli/latest/userguide/cli-chap-getting-started.md") for more details.
- If you intend to use the AWS Management Console to launch your instances, then ensure that your IAM user has permission to launch and configure Amazon EC2, Amazon EBS, and so on. See the [IAM documentation](../../../IAM/latest/UserGuide/introduction.md "../../../IAM/latest/UserGuide/introduction.md") for more details.
- Ensure that you have the required SAP software available either via an Amazon Simple Storage Service (Amazon S3) bucket or on a file share accessible from an Amazon EC2 instance. If you use Amazon S3, make sure to assign appropriate IAM role permissions to the EC2 instance to allow S3 access.
- All enterprise customers use DNS service. You can create a hosted zone in Amazon Route 53. You can optionally use AWS Directory Service for Microsoft Active Directory, also known as AWS Managed Microsoft AD. This service lets your directory-aware workloads and AWS resources use managed Active Directory in the AWS Cloud. For more details on this service, see [AWS Directory Service](https://aws.amazon.com/directoryservice/ "https://aws.amazon.com/directoryservice/") and [Create Your AWS Managed Microsoft AD directory](../../../directoryservice/latest/admin-guide/ms_ad_getting_started_create_directory.md "../../../directoryservice/latest/admin-guide/ms_ad_getting_started_create_directory.md").
