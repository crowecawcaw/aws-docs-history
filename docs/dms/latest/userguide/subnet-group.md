# Creating a subnet group for an AWS DMS migration project

Before you create an instance profile, configure a subnet group for your instance profile.

###### To create a subnet group

1. Sign in to the AWS Management Console and open the AWS DMS console at [https://console.aws.amazon.com/dms/v2/](https://console.aws.amazon.com/dms/v2/ "https://console.aws.amazon.com/dms/v2/").
2. In the navigation pane, choose **Subnet groups**, and then choose
   **Create subnet group**.
3. For **Name**, enter a unique name of your subnet group.
4. For **Description**, enter a brief description of your subnet
   group.
5. For **VPC**, choose a VPC that has at least one subnet in at least
   two Availability Zones.
6. For **Add subnets**, choose subnets to include in the subnet group.
   You must choose subnets in at least two Availability Zones.

To connect to Amazon RDS databases, add public subnets into your subnet group.
To connect to on-premises databases, add private subnets into your subnet group. 7. Choose **Create subnet group**.
