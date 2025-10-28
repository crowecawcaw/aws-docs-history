# Creating instance profiles for AWS Database Migration Service

You can create multiple instance profiles in the AWS DMS console. Make sure that you select
an instance profile to use for each migration project that you create in AWS DMS.

###### To create an instance profile

1. Sign in to the AWS Management Console and open the AWS DMS console at [https://console.aws.amazon.com/dms/v2/](https://console.aws.amazon.com/dms/v2/ "https://console.aws.amazon.com/dms/v2/").
2. In the navigation pane, choose **Instance profiles**.
3. Choose **Create instance profile**.
4. On the **Create instance profile** page, enter a descriptive
   value for **Name** for your instance profile.
5. For **Network type**, choose **Dual-stack mode** to
   create an instance profile that supports IPv4 and IPv6 addressing. Keep the default option
   to create an instance profile that supports only IPv4 addressing.
6. Next, choose **Virtual private cloud (VPC)** to run your instance of
   the selected network type. Then choose a **Subnet group** and
   **VPC security groups** for your instance profile.

To connect to Amazon RDS databases, use the subnet configuration appropriate for
your RDS setup, whether public or private. For connecting to on-premises
databases, If use a private subnet group and ensure that your network is
configured to allow AWS DMS access to the source on-premises database through the
NAT gateway's public IP address. For more information, see [Create a VPC based on Amazon VPC](set-up.md#set-up-vpc "set-up.md#set-up-vpc"). 7. (Optional) In you create a migration project for DMS Schema Conversion, then for
**Schema conversion settings - optional**, choose an Amazon S3 bucket
to store information from your migration project. Then choose the AWS Identity and Access Management (IAM) role
that provides access to this Amazon S3 bucket. For more information, see [Create an Amazon S3 bucket](set-up.md#set-up-s3-bucket "set-up.md#set-up-s3-bucket"). 8. Choose **Create instance profile**.
After you create your instance profile, you can modify or delete it.

###### To modify an instance profile

1. Sign in to the AWS Management Console and open the AWS DMS console at [https://console.aws.amazon.com/dms/v2/](https://console.aws.amazon.com/dms/v2/ "https://console.aws.amazon.com/dms/v2/").
2. Choose **Instance profiles**. The **Instance profiles** page
   opens.
3. Choose your instance profile, and then choose **Modify**.
4. Update the name of your instance profile, edit the VPC or Amazon S3 bucket settings.
5. Choose **Save changes**.

###### To delete an instance profile

1. Sign in to the AWS Management Console and open the AWS DMS console at [https://console.aws.amazon.com/dms/v2/](https://console.aws.amazon.com/dms/v2/ "https://console.aws.amazon.com/dms/v2/").
2. Choose **Instance profiles**. The **Instance profiles** page
   opens.
3. Choose your instance profile, and then choose **Delete**.
4. Choose **Delete** to confirm your choice.
