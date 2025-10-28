# Create an instance profile for

DMS Schema Conversion

Before you create an instance profile, configure a subnet group for your instance
profile. For more information about creating a subnet group for your AWS DMS migration
project, see [Creating a subnet group](subnet-group.md "subnet-group.md").

You can create an instance profile as described in the following procedure. In this
instance profile, you specify network and security settings for your DMS Schema Conversion
project.

###### To create an instance profile

1. Sign in to the AWS Management Console and open the AWS DMS console at [https://console.aws.amazon.com/dms/v2/](https://console.aws.amazon.com/dms/v2/ "https://console.aws.amazon.com/dms/v2/").
2. In the navigation pane, choose **Instance profiles**, and
   then choose **Create instance profile**.
3. For **Name**, enter a unique name for your instance profile.
   For example, enter `sc-instance`.
4. For **Network type**, choose **IPv4** to
   create an instance profile that supports only IPv4 addressing. To create an
   instance profile that supports IPv4 and IPv6 addressing, choose
   **Dual-stack mode**.
5. For **Virtual private cloud (VPC)**, choose the VPC that you
   created in the prerequisites step.
6. For **Subnet group**, choose the subnet group for your
   instance profile. To connect to Amazon RDS databases, use a subnet group that
   includes public subnets. To connect to on-premises databases, use a subnet group
   that includes private subnets.
7. Choose **Create instance profile**.
   To create a migration project, use this instance profile.
