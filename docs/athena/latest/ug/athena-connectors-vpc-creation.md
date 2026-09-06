

# Create a VPC for a data source connector or AWS Glue connection
<a name="athena-connectors-vpc-creation"></a>

Some Athena data source connectors and AWS Glue connections require a VPC and a security group. This topic shows you how to create a VPC with a subnet and a security group for the VPC. As part of this process, you retrieve the IDs for the VPC, subnet, and security group that you create. These IDs are required when you configure your AWS Glue connection or data source connector for use with Athena.

**To create a VPC for an Athena data source connector**

1. Sign in to the AWS Management Console and open the Amazon VPC console at [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/).

1. Choose **Create VPC**.

1. On the **Create VPC** page, under **VPC Settings**, for **Resources to create**, choose **VPC and more**.

1. Under **Name tag auto-generation**, for **Auto-generate**, enter a value that will be used to generate name tags for all resources in your VPC.

1. Choose **Create VPC**.

1. When the process completes, choose **View VPC**.

1. In the **Details** section, for **VPC ID**, copy your VPC ID for later reference.

Now you are ready to retrieve the subnet ID for the VPC that you just created.

**To retrieve your VPC subnet ID**

1. In the VPC console navigation pane, choose **Subnets**.

1. Select the name of a subnet whose **VPC** column has the VPC ID that you noted.

1. In the **Details** section, for **Subnet ID**, copy your subnet ID for later reference.

Next, you create a security group for your VPC.

**To create a security group for your VPC**

1. In the VPC console navigation pane, choose **Security**, **Security Groups**.

1. Choose **Create security group**.

1. On the **Create security group** page, enter the following information:
   + For **Security group name**, enter a name for your security group.
   + For **Description**, enter a description for the security group. A description is required.
   + For **VPC**, choose the VPC ID of the VPC that you created for your data source connector.
   + For **Inbound rules** and **Outbound rules**, add any inbound and outbound rules that you require.

1. Choose **Create security group**.

1. On the **Details** page for the security group, copy the **Security group ID** for later reference.

## Important considerations for using VPC with Athena connectors
<a name="vpc-warning-instructions"></a>

The following instructions apply to all Athena connectors, as all connectors can utilize VPC.

**Note**  
When using a VPC with AWS Glue connections, you will need to set up the following PrivateLink endpoints:  
Amazon S3
AWS Glue
AWS Secrets Manager

**Note**  
For **AWS Glue Data Catalog federated connectors without Lambda**, you will also need to set up the following PrivateLink endpoints:  
KMS

Alternatively, you can use public internet access, though this is not recommended for security reasons.

**Warning**  
Using public internet access may expose your resources to additional security risks. It is strongly recommended to use PrivateLink endpoints for enhanced security in your VPC configuration.