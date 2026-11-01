

# Creating a subnet group for an AWS DMS migration project
<a name="subnet-group"></a>

Before you create an instance profile, configure a subnet group for your instance profile.

**To create a subnet group**

1. Sign in to the AWS Management Console and open the AWS DMS console at [https://console.aws.amazon.com/dms/v2/](https://console.aws.amazon.com/dms/v2/).

1. In the navigation pane, choose **Subnet groups**, and then choose **Create subnet group**.

1. For **Name**, enter a unique name of your subnet group.

1. For **Description**, enter a brief description of your subnet group.

1. For **VPC**, choose a VPC that has at least one subnet in at least two Availability Zones.

1. For **Add subnets**, choose subnets to include in the subnet group. You must choose subnets in at least two Availability Zones.

   Choose subnets that provide network connectivity between your replication instance and your source and target databases. The subnet type (public or private) does not by itself determine connectivity to Amazon RDS or on-premises databases; make sure the subnets you choose can reach your databases. 

1. Choose **Create subnet group**.