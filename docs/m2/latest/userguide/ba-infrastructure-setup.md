AWS Mainframe Modernization Service (Managed Runtime Environment experience) is no longer open to new customers. For
capabilities similar to AWS Mainframe Modernization Service (Managed Runtime Environment experience) explore AWS Mainframe Modernization Service (Self-Managed
Experience). Existing customers can continue to use the service as normal. For more information, see [AWS Mainframe Modernization
availability change](mainframe-modernization-availability-change.md "mainframe-modernization-availability-change.md").

# Infrastructure setup requirements for

AWS Blu Age Runtime (non-managed)

This topic describes the minimum infrastructure configuration required to run AWS Blu Age Runtime (non-managed). The
following procedures describe how to set up AWS Blu Age Runtime (non-managed) on your compute of choice to deploy a
modernized application on the AWS Blu Age Runtime. The resources that you create must be in an Amazon VPC that
has a subnet that is dedicated to your application domain.

###### Topics

- [Infrastructure requirements](#infrastructure-requirements "#infrastructure-requirements")
- [Running AWS Blu Age Runtime on Amazon EC2](#ba-running-on-ec2 "#ba-running-on-ec2")
- [Running AWS Blu Age Runtime on Amazon ECS on Amazon EC2](#ba-running-on-ecs-on-ec2 "#ba-running-on-ecs-on-ec2")
- [Running AWS Blu Age Runtime on Amazon EKS on Amazon EC2](#ba-running-on-eks-on-ec2 "#ba-running-on-eks-on-ec2")
- [Running AWS Blu Age Runtime on Amazon ECS managed by
  AWS Fargate](#ba-running-on-fargate "#ba-running-on-fargate")

## Infrastructure requirements

###### Create a security group

If you plan to work on Amazon EC2 instances on Amazon EKS, skip this procedure because the
Amazon EKS cluster creation process creates a security group on your behalf. Use that
security group in the following procedures instead of creating a new one.

1. Open the Amazon VPC console at
   [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/ "https://console.aws.amazon.com/vpc/").
2. In the left navigation pane, under **Security**, choose
   **Security groups**.
3. In the central pane, choose **Create security group**.
4. In the **Security group name** field, enter
   `M2BluagePrivateLink-SG`.
5. In the **Inbound rules** section, choose **Add
   rule**.
6. For **Type**, choose HTTPS.
7. For **Source** enter your VPC CIDR.
8. In the **Outbound rules** section, choose **Add
   rule**.
9. For **Type**, choose HTTPS.
10. For **Destination**, enter
    `0.0.0.0/0`.
11. Choose **Create security group**.

###### Create an IAM role

1. Open the IAM console at
   [https://console.aws.amazon.com/iam/](https://console.aws.amazon.com/iam/ "https://console.aws.amazon.com/iam/").
2. In the left navigation pane, under **Access management**,
   choose **Roles**.
3. In the central pane, choose **Create role**.
4. In the **Use case** section, depending on your compute
   choice, choose one of the following:
   - **EC2** (for Amazon EC2 and Amazon EKS on Amazon EC2)
   - **Elastic Container Service** and then **EC2
     Role for Elastic Container Service** (for Amazon ECS on
     Amazon EC2)
   - **Elastic Container Service** and then
     **Elastic Container Service Task** (for Amazon ECS
     managed by Fargate)

5. Choose **Next**.
6. Enter a name for the role, then choose **Create
   role**.

## Running AWS Blu Age Runtime on Amazon EC2

To create an Amazon EC2 instance, use the following steps.

###### Create an Amazon EC2 instance

1. Open the Amazon EC2 console at
   [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/ "https://console.aws.amazon.com/ec2/").
2. Choose **Launch instance**.
3. For **Instance type**, choose an EC2 available instance type.
4. In the **Key pair** section, either choose an existing key
   pair or create a new one.
5. In the **Network settings** section, choose **Select existing security group**.
6. For **Common security groups**, choose
   **M2BluagePrivateLink-SG**.
7. Expand the **Advanced details** section.
8. For **IAM instance profile**, choose the IAM role that you
   created earlier.
9. Choose **Launch instance**.

###### Install the application on the Amazon EC2 instance

1.  When the state of the Amazon EC2 instance changes to **Running**,
    connect to the instance.
2.  Install the following software components on the instance:

        * Java Runtime Environment (JRE) 17.
        * Apache Tomcat 10.
        * AWS Blu Age Runtime (on Amazon EC2). Install the AWS Blu Age runtime at the root of Apache Tomcat
         installation folder (some files will be added while others will be
         overwritten).

    To install the additional webapps delivered alongside the AWS Blu Age Runtime archive, set
    up a secondary instance of the Apache Tomcat server, and decompress the webapps
    archive at that location. For detailed instructions, see [AWS Blu Age Runtime artifacts](ba-runtime-artifacts.md "ba-runtime-artifacts.md").

## Running AWS Blu Age Runtime on Amazon ECS on Amazon EC2

1. Create an Amazon ECS cluster, with **Amazon EC2 instances** as an
   underlying infrastructure. See [Getting started with Windows on Amazon EC2](../../../AmazonECS/latest/developerguide/getting-started-ecs-ec2-v2.md#getting-started-ec2-cluster-v2 "../../../AmazonECS/latest/developerguide/getting-started-ecs-ec2-v2.md#getting-started-ec2-cluster-v2") in the
   Amazon Elastic Container Service Developer Guide.
2. Specify the IAM role that you created in the previous steps.
3. Choose an EC2 instance type.
4. In **Network settings for Amazon EC2 instances**, choose the
   security group that you created in the previous steps.

## Running AWS Blu Age Runtime on Amazon EKS on Amazon EC2

1. Create an Amazon EKS cluster. See [Creating an Amazon EKS cluster](../../../eks/latest/userguide/create-cluster.md "../../../eks/latest/userguide/create-cluster.md") in the _Amazon EKS User Guide_.
2. As mentioned previously, a security group is created on your behalf.
3. Create a node group. Specify the IAM role that you created in the previous
   steps.
4. Choose an EC2 instance type.
5. Amazon EKS will automatically assign the security group to the spawned Amazon EC2
   instances.

## Running AWS Blu Age Runtime on Amazon ECS managed by

AWS Fargate

Create an Amazon ECS cluster with **AWS Fargate (serverless)** as an
underlying infrastructure. See [Getting started with Fargate](../../../AmazonECS/latest/developerguide/getting-started-fargate.md "../../../AmazonECS/latest/developerguide/getting-started-fargate.md") in the _Amazon Elastic Container Service Developer Guide_.
