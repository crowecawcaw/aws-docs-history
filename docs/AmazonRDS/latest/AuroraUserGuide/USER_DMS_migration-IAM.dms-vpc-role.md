

# Creating an IAM role for AWS DMS to manage Amazon VPC
<a name="USER_DMS_migration-IAM.dms-vpc-role"></a>

You must create an IAM role for AWS DMS to manage the VPC settings for your resources. This role must be available for successful migration.

**Creating the `dms-vpc-role` for database migration**

1. Sign in to the AWS Management Console and open the IAM console at [https://console.aws.amazon.com/iam/](https://console.aws.amazon.com/iam/).

1. In the navigation pane of the console, choose **Roles** and then choose **Create role**.

1. Choose the **AWS service** option for the **Select trusted entity** option.

   For **Use case**, select **DMS**.

1. For the **Add permissions** step, select `AmazonDMSVPCManagementRole` and choose **Next**.

1. In the **Name, review, and create** page, set the **Role name** to `dms-vpc-role` and choose **Create role**.

This creates the role for the DMS to manage the VPC settings for the migration.