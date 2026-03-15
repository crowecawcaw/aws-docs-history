# Creating an IAM role for AWS DMS to manage Amazon VPC

You must create an IAM role for AWS DMS to manage the VPC settings for your resources. This
role must be available for successful migration.

###### Creating the `dms-vpc-role` for database migration

1. Sign in to the AWS Management Console and open the IAM console at [https://console.aws.amazon.com/iam/](https://console.aws.amazon.com/iam/ "https://console.aws.amazon.com/iam/").
2. In the navigation pane of the console, choose **Roles** and then choose **Create role**.
3. Choose the **AWS service** option for the **Select trusted entity** option.

For **Use case**, select **DMS**. 4. For the **Add permissions** step, select `AmazonDMSVPCManagementRole` and choose **Next**. 5. In the **Name, review, and create** page, set the **Role name** to `dms-vpc-role`
and choose **Create role**.
