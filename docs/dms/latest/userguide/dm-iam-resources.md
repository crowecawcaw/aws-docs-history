

# Creating required IAM resources for homogeneous data migrations in AWS DMS
<a name="dm-iam-resources"></a>

To run homogeneous data migrations, you must create an IAM policy and an IAM role in your account to interact with other AWS services. In this section, you create these required IAM resources.

**Topics**
+ [Creating an IAM policy for homogeneous data migrations in AWS DMS](#dm-resources-iam-policy)
+ [Creating an IAM role for homogeneous data migrations in AWS DMS](#dm-resources-iam-role)

## Creating an IAM policy for homogeneous data migrations in AWS DMS
<a name="dm-resources-iam-policy"></a>

To access your databases and to migrate data, with AWS DMS, you can create a serverless environment for homogeneous data migrations. Also, AWS DMS stores logs, metrics, and progress for each data migration in Amazon CloudWatch. To create a data migration project, AWS DMS needs access to these services.

In this step, you create an IAM policy that provides AWS DMS with access to Amazon EC2 and CloudWatch resources. Next, create an IAM role and attach this policy.

**To create an IAM policy for homogeneous data migrations in AWS DMS**

1. Sign in to the AWS Management Console and open the IAM console at [https://console.aws.amazon.com/iam/](https://console.aws.amazon.com/iam/).

1. In the navigation pane, choose **Policies**.

1. Choose **Create policy**.

1. In the **Create policy** page, choose the **JSON** tab.

1. Paste the following JSON into the editor.

------
#### [ JSON ]

****  

   ```
   {
       "Version":"2012-10-17",		 	 	 
       "Statement": [
           {
               "Effect": "Allow",
               "Action": [
                   "ec2:DescribeVpcs"
               ],
               "Resource": "*"
           },
           {
               "Effect": "Allow",
               "Action": [
                   "logs:CreateLogGroup"
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
           }
       ]
   }
   ```

------

1. Choose **Next**.

1. Enter **HomogeneousDataMigrationsPolicy** for **Policy name**, and choose **Create policy**.

## Creating an IAM role for homogeneous data migrations in AWS DMS
<a name="dm-resources-iam-role"></a>

In this step, you create an IAM role that provides AWS DMS with access to AWS Secrets Manager, Amazon EC2, and CloudWatch.

When creating an IAM role, you must also create a `dms-vpc-role`. For more information, see [Creating an IAM role for AWS DMS to manage Amazon VPC](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_DMS_migration-IAM.dms-vpc-role.html) in the *Amazon Relational Database Service User Guide*.

**To create an IAM role for homogeneous data migrations in AWS DMS**

1. Sign in to the AWS Management Console and open the IAM console at [https://console.aws.amazon.com/iam/](https://console.aws.amazon.com/iam/).

1. In the navigation pane, choose **Roles**.

1. Choose **Create role**.

1. On the **Select trusted entity** page, for **Trusted entity type**, choose **AWS Service**. For **Use cases for other AWS services**, choose **DMS**.

1. Select the **DMS** check box and choose **Next**.

1. On the **Add permissions** page, choose **HomogeneousDataMigrationsPolicy** that you created before.

1. On the **Name, review, and create** page, enter **HomogeneousDataMigrationsRole** for **Role name**, and choose **Create role**.

1. Choose **Update policy**.