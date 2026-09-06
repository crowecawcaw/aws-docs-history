

# Step 5: Create an Instance Profile
<a name="dm-postgresql-step-5"></a>

Before you create an instance profile, configure a subnet group for your instance profile.

 **To create a subnet group** 

1. Sign in to the AWS Management Console and open the AWS DMS console at [https://console.aws.amazon.com/dms/v2/](https://console.aws.amazon.com/dms/v2/).

1. Choose your AWS Region.

1. In the navigation pane, choose **Subnet groups**, and then choose **Create subnet group**.

1. For **Name**, enter `DataMigrationSubnetGroup`.

1. For **Description**, enter `A group of private subnets`.

1. For **VPC**, choose `dm-vpc`. You created this VPC in [Step 1](dm-postgresql-step-1.md).

1. For **Add subnets**, choose two private subnet IDs.

1. Choose **Create subnet group**.

Before you create your migration project, you set up an instance profile. An instance profile specifies network and security settings for your migration project.

 **To create an instance profile** 

1. Sign in to the AWS Management Console and open the AWS DMS console at [https://console.aws.amazon.com/dms/v2/](https://console.aws.amazon.com/dms/v2/).

1. Choose your AWS Region.

1. In the navigation pane, choose **Instance profiles**, and then choose **Create instance profile**.

1. For **Name**, enter a unique name for your instance profile. For example, enter `dm-instance-profile`.

1. For **Virtual private cloud (VPC)**, choose `dm-vpc`. You created this VPC in [Step 1](dm-postgresql-step-1.md).

1. For **Subnet group**, choose the `DataMigrationSubnetGroup` subnet group that you created before.

1. Choose **Create instance profile**.

Use this instance profile when you create your migration project in [Step 7](dm-postgresql-step-7.md).