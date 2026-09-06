

**AWS Mainframe Modernization self-managed experience** is no longer open to new customers. For capabilities similar to AWS Mainframe Modernization self-managed experience, explore capabilities from vendor-direct offerings and from AWS Transform. Existing customers can continue to use the service as normal. For more information, see [AWS Mainframe Modernization availability change](https://docs.aws.amazon.com/m2/latest/userguide/mainframe-modernization-availability-change.html). 

**AWS Mainframe Modernization Service (Managed Runtime Environment experience)** is no longer open to new customers. For capabilities similar to AWS Mainframe Modernization Service (Managed Runtime Environment experience) explore AWS Mainframe Modernization Service (Self-Managed Experience). Existing customers can continue to use the service as normal. For more information, see [AWS Mainframe Modernization availability change](https://docs.aws.amazon.com/m2/latest/userguide/mainframe-modernization-availability-change.html). 

# Infrastructure setup requirements for AWS Transform for mainframe Runtime
<a name="ba-infrastructure-setup"></a>

This topic describes the minimum infrastructure configuration required to run AWS Transform for mainframe Runtime. The following procedures describe how to set up AWS Transform for mainframe Runtime on your compute of choice to deploy a modernized application on the AWS Transform for mainframe Runtime. The resources that you create must be in an Amazon VPC that has a subnet that is dedicated to your application domain.

**Topics**
+ [Infrastructure requirements](#infrastructure-requirements)
+ [Running AWS Transform for mainframe Runtime on Amazon EC2](#ba-running-on-ec2)
+ [Running AWS Transform for mainframe Runtime on Amazon ECS on Amazon EC2](#ba-running-on-ecs-on-ec2)
+ [Running AWS Transform for mainframe Runtime on Amazon EKS on Amazon EC2](#ba-running-on-eks-on-ec2)
+ [Running AWS Transform for mainframe Runtime on Amazon ECS managed by AWS Fargate](#ba-running-on-fargate)

## Infrastructure requirements
<a name="infrastructure-requirements"></a>

**Create a security group**

If you plan to work on Amazon EC2 instances on Amazon EKS, skip this procedure because the Amazon EKS cluster creation process creates a security group on your behalf. Use that security group in the following procedures instead of creating a new one.

1. Open the Amazon VPC console at [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/).

1. In the left navigation pane, under **Security**, choose **Security groups**.

1. In the central pane, choose **Create security group**.

1. In the **Security group name** field, enter **M2BluagePrivateLink-SG**.

1. In the **Inbound rules** section, choose **Add rule**.

1. For **Type**, choose HTTPS.

1. For **Source** enter your VPC CIDR.

1. In the **Outbound rules** section, choose **Add rule**.

1. For **Type**, choose HTTPS.

1. For **Destination**, enter **0.0.0.0/0**.

1. Choose **Create security group**.

**Create an IAM role**

1. Open the IAM console at [https://console.aws.amazon.com/iam/](https://console.aws.amazon.com/iam/).

1. In the left navigation pane, under **Access management**, choose **Roles**.

1. In the central pane, choose **Create role**.

1. In the **Use case** section, depending on your compute choice, choose one of the following:
   + **EC2** (for Amazon EC2 and Amazon EKS on Amazon EC2)
   + **Elastic Container Service** and then **EC2 Role for Elastic Container Service** (for Amazon ECS on Amazon EC2)
   + **Elastic Container Service** and then **Elastic Container Service Task** (for Amazon ECS managed by Fargate)

1. Choose **Next**.

1. Enter a name for the role, then choose **Create role**.

## Running AWS Transform for mainframe Runtime on Amazon EC2
<a name="ba-running-on-ec2"></a>

To create an Amazon EC2 instance, use the following steps. 

**Create an Amazon EC2 instance**

1. Open the Amazon EC2 console at [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/).

1. Choose **Launch instance**.

1. For **Instance type**, choose an EC2 available instance type.

1. In the **Key pair** section, either choose an existing key pair or create a new one.

1. In the **Network settings** section, choose **Select existing security group**.

1. For **Common security groups**, choose **M2BluagePrivateLink-SG**.

1. Expand the **Advanced details** section.

1. For **IAM instance profile**, choose the IAM role that you created earlier.

1. Choose **Launch instance**.

**Install the application on the Amazon EC2 instance**

1. When the state of the Amazon EC2 instance changes to **Running**, connect to the instance.

1. Install the following software components on the instance (Refer to the versions mentioned into the [AWS Transform for mainframe release notes](ba-release-notes.md)):
   + Java Runtime Environment (JRE).
   + Apache Tomcat.
   + AWS Transform for mainframe Runtime (on Amazon EC2). Install the AWS Transform for mainframe runtime at the root of Apache Tomcat installation folder (some files will be added while others will be overwritten).

   To install the additional webapps delivered alongside the AWS Transform for mainframe Runtime archive, set up a secondary instance of the Apache Tomcat server, and decompress the webapps archive at that location. For detailed instructions, see [AWS Transform for mainframe Runtime artifacts](ba-runtime-artifacts.md).

## Running AWS Transform for mainframe Runtime on Amazon ECS on Amazon EC2
<a name="ba-running-on-ecs-on-ec2"></a>

1. Create an Amazon ECS cluster, with **Amazon EC2 instances** as an underlying infrastructure. See [Getting started with Windows on Amazon EC2](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/getting-started-ecs-ec2-v2.html#getting-started-ec2-cluster-v2) in the Amazon Elastic Container Service Developer Guide.

1. Specify the IAM role that you created in the previous steps.

1. Choose an EC2 instance type.

1. In **Network settings for Amazon EC2 instances**, choose the security group that you created in the previous steps.

## Running AWS Transform for mainframe Runtime on Amazon EKS on Amazon EC2
<a name="ba-running-on-eks-on-ec2"></a>

1. Create an Amazon EKS cluster. See [Creating an Amazon EKS cluster](https://docs.aws.amazon.com/eks/latest/userguide/create-cluster.html) in the *Amazon EKS User Guide*.

1. As mentioned previously, a security group is created on your behalf.

1. Create a node group. Specify the IAM role that you created in the previous steps.

1. Choose an EC2 instance type.

1. Amazon EKS will automatically assign the security group to the spawned Amazon EC2 instances.

## Running AWS Transform for mainframe Runtime on Amazon ECS managed by AWS Fargate
<a name="ba-running-on-fargate"></a>

Create an Amazon ECS cluster with **AWS Fargate (serverless)** as an underlying infrastructure. See [Getting started with Fargate](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/getting-started-fargate.html) in the *Amazon Elastic Container Service Developer Guide*.