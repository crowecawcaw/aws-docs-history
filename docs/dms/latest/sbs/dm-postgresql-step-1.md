

# Step 1: Create AWS Resources
<a name="dm-postgresql-step-1"></a>

In this step, you create and configure the required AWS resources for homogeneous data migrations in AWS DMS.

**Topics**
+ [Creating a VPC](#dm-postgresql-step-1-vpc)
+ [Creating an IAM policy](#dm-postgresql-step-1-iam-policy)
+ [Creating an IAM role](#dm-postgresql-step-1-iam-role)

## Creating a VPC
<a name="dm-postgresql-step-1-vpc"></a>

In this section, you create a virtual private cloud (VPC). This VPC is based on the Amazon Virtual Private Cloud (Amazon VPC) service and contains your AWS resources. Make sure that you create this VPC in one of the AWS Regions that support homogeneous data migrations in AWS DMS. For more information, see the [list of supported Regions](https://docs.aws.amazon.com/dms/latest/userguide/data-migrations.html#data-migrations-supported-regions).

To migrate your on-premises source database, make sure that you configure a private network to connect to your target database. For more information, see the [Using an on-premises source data provider](https://docs.aws.amazon.com/dms/latest/userguide/dm-network.html#dm-network-on-premises).

 **To create a VPC for homogeneous data migrations** 

1. Sign in to the AWS Management Console and open the Amazon VPC console at [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/).

1. Choose your AWS Region.

1. Choose **Create VPC**.

1. On the **Create VPC** page, enter the following settings:
   +  **Resources to create** — **VPC and more** 
   +  **Name tag auto-generation** — Choose **Auto-generate** and enter a globally unique name. For example, enter `dm-vpc`.
   +  **IPv4 CIDR block** — `10.0.1.0/24` 
   +  **NAT gateways** — **In 1 AZ** 
   +  **VPC endpoints** — **None** 

1. Keep the rest of the settings as they are, and choose **Create VPC**.

Use this VPC when you create your target Amazon RDS database in [Step 3](dm-postgresql-step-3.md) and your subnet group in [Step 5](dm-postgresql-step-5.md).

## Creating an IAM policy
<a name="dm-postgresql-step-1-iam-policy"></a>

In this section, you create an AWS Identity and Access Management (IAM) policy that AWS DMS requires to run homogeneous data migrations.

 **To create an IAM policy for homogeneous data migrations** 

1. Sign in to the AWS Management Console and open the IAM console at [https://console.aws.amazon.com/iam/](https://console.aws.amazon.com/iam/).

1. In the navigation pane, choose **Policies**.

1. Choose **Create policy**.

1. On the **Create policy** page, choose the **JSON** tab.

1. Paste the following JSON into the editor.

```
{
    "Version": "2012-10-17",		 	 	 
    "Statement": [
        {
            "Effect": "Allow",
            "Action": [
                "ec2:DescribeRouteTables",
                "ec2:DescribeSecurityGroups",
                "ec2:DescribeVpcPeeringConnections",
                "ec2:DescribeVpcs",
                "ec2:DescribePrefixLists",
                "logs:DescribeLogGroups"
            ],
            "Resource": "*"
        },
        {
            "Effect": "Allow",
            "Action": [
                "servicequotas:GetServiceQuota"
            ],
            "Resource": "arn:aws:servicequotas:*:*:vpc/L-0EA8095F"
        },
        {
            "Effect": "Allow",
            "Action": [
                "logs:CreateLogGroup",
                "logs:DescribeLogStreams"
            ],
            "Resource": "arn:aws:logs:*:*:log-group:dms-data-migration-*"
        },
        {
            "Effect": "Allow",
            "Action": [
                "logs:CreateLogStream",
                "logs:PutLogEvents"
            ],
            "Resource": "arn:aws:logs:*:*:log-group:dms-data-migration-*:log-stream:dms-data-migration-*"
        },
        {
            "Effect": "Allow",
            "Action": "cloudwatch:PutMetricData",
            "Resource": "*"
        },
        {
            "Effect": "Allow",
            "Action": [
                "ec2:CreateRoute",
                "ec2:DeleteRoute"
            ],
            "Resource": "arn:aws:ec2:*:*:route-table/*"
        },
        {
            "Effect": "Allow",
            "Action": [
                "ec2:CreateTags"
            ],
            "Resource": [
                "arn:aws:ec2:*:*:security-group/*",
                "arn:aws:ec2:*:*:security-group-rule/*",
                "arn:aws:ec2:*:*:route-table/*",
                "arn:aws:ec2:*:*:vpc-peering-connection/*",
                "arn:aws:ec2:*:*:vpc/*"
            ]
        },
        {
            "Effect": "Allow",
            "Action": [
                "ec2:AuthorizeSecurityGroupEgress",
                "ec2:AuthorizeSecurityGroupIngress"
            ],
            "Resource": "arn:aws:ec2:*:*:security-group-rule/*"
        },
        {
            "Effect": "Allow",
            "Action": [
                "ec2:AuthorizeSecurityGroupEgress",
                "ec2:AuthorizeSecurityGroupIngress",
                "ec2:RevokeSecurityGroupEgress",
                "ec2:RevokeSecurityGroupIngress"
            ],
            "Resource": "arn:aws:ec2:*:*:security-group/*"
        },
        {
            "Effect": "Allow",
            "Action": [
                "ec2:AcceptVpcPeeringConnection",
                "ec2:ModifyVpcPeeringConnectionOptions"
            ],
            "Resource": "arn:aws:ec2:*:*:vpc-peering-connection/*"
        },
        {
            "Effect": "Allow",
            "Action": "ec2:AcceptVpcPeeringConnection",
            "Resource": "arn:aws:ec2:*:*:vpc/*"
        }
    ]
}
```

1. Choose **Next** The **Review, and create** page opens.

1. For **Name**, enter `HomogeneousDataMigrationsPolicy`, and choose **Create policy**.

Use this IAM policy when you create the IAM role.

## Creating an IAM role
<a name="dm-postgresql-step-1-iam-role"></a>

In this section, you create an IAM role for homogeneous data migrations. AWS DMS uses this IAM role to access database credentials stored in AWS Secrets Manager, store log files in Amazon CloudWatch, and interact with Amazon EC2.

 **To create an IAM role that provides access to AWS Secrets Manager ** 

1. Sign in to the AWS Management Console and open the IAM console at [https://console.aws.amazon.com/iam/](https://console.aws.amazon.com/iam/).

1. In the navigation pane, choose **Roles**.

1. Choose **Create role**.

1. On the **Select trusted entity** page, choose ** AWS service**. For **Use case**, Choose **DMS**.

1. Choose **Next**. The **Add permissions** page opens.

1. Choose **HomogeneousDataMigrationsPolicy** that you created before. Also, choose **SecretsManagerReadWrite**.

1. Choose **Next**. The **Name, review, and create** page opens.

1. For **Role name**, enter `HomogeneousDataMigrationsRole` and choose **Create role**.

1. On the **Roles** page, enter `HomogeneousDataMigrationsRole` for **Role name**. Choose **HomogeneousDataMigrationsRole**.

1. Choose the **Trust relationships** tab and choose **Edit trust policy**.

1. On the **Edit trust policy** page, paste the following JSON into the editor, replacing the existing text.

```
{
    "Version": "2012-10-17",		 	 	 
    "Statement": [
        {
            "Sid": "",
            "Effect": "Allow",
            "Principal": {
                "Service": [
                    "dms-data-migrations.amazonaws.com",
                    "dms.your_region.amazonaws.com"
                ]
            },
            "Action": "sts:AssumeRole"
        }
    ]
}
```

\+ Replace {{your\_region}} with the name of your Region, such as `us-east-1`. . Choose **Update policy**.

Use this IAM role when you create your instance profile in [Step 5](dm-postgresql-step-5.md) and your migration project in [Step 7](dm-postgresql-step-7.md).