

# Setting up Amazon VPC for JDBC connections to Amazon RDS data stores from AWS Glue
<a name="setup-vpc-for-glue-access"></a>

 When using JDBC to connect to databases in Amazon RDS, you will need to perform additional setup. To enable AWS Glue components to communicate with Amazon RDS, you must set up access to your Amazon RDS data stores in Amazon VPC. To enable AWS Glue to communicate between its components, specify a security group with a self-referencing inbound rule for all TCP ports. By creating a self-referencing rule, you can restrict the source to the same security group in the VPC. A self-referencing rule will not open the VPC to all networks. The default security group for your VPC might already have a self-referencing inbound rule for ALL Traffic. 

**To set up access between AWS Glue and Amazon RDS data stores**

1. Sign in to the AWS Management Console and open the Amazon RDS console at [https://console.aws.amazon.com/rds/](https://console.aws.amazon.com/rds/).

1. In the Amazon RDS console, identify the security group(s) used to control access to your Amazon RDS database.

   In the left navigation pane, choose **Databases**, then select the instance you would like to connect to from the list in the main pane.

   In the database detail page, find **VPC security groups** on the **Connectivity & security** tab.

1. Based on your network architecture, identify which associated security group is best to modify to allow access for the AWS Glue service. Save its name, {{database-security-group}} for future reference. If there is no appropriate security group, follow the directions to [Provide access to your DB instance in your VPC by creating a security group](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/CHAP_SettingUp.html) in the Amazon RDS documentation.

1. Sign in to the AWS Management Console and open the Amazon VPC console at [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/).

1. In the Amazon VPC console, identify how to update {{database-security-group}}.

   In the left navigation pane, choose **Security groups**, then select {{database-security-group}} from the list in the main pane.

1. Identify the security group ID for {{database-security-group}}, {{database-sg-id}}. Save it for future reference.

   In the security group detail page, find **Security group ID**.

1. Alter the inbound rules for {{database-security-group}}, add a self-referencing rule to allow AWS Glue components to communicate. Specifically, add or confirm that there is a rule where **Type** is `All TCP`, **Protocol** is `TCP`, **Port Range** includes all ports, and **Source** is {{database-sg-id}}. Verify that the security group you have entered for **Source** is the same as the security group you are editing.

   In the security group detail page, select **Edit inbound rules**.

   The inbound rule looks similar to this:    
[See the AWS documentation website for more details](http://docs.aws.amazon.com/glue/latest/dg/setup-vpc-for-glue-access.html)

1. Add rules for outbound traffic.

   In the security group detail page, select **Edit outbound rules**.

   If you security group allows all outbound traffic, you do not need separate rules. For example:    
[See the AWS documentation website for more details](http://docs.aws.amazon.com/glue/latest/dg/setup-vpc-for-glue-access.html)

   If your network architecture is designed for you to restrict outbound traffic, create the following outbound rules:

   Create a self-referencing rule where **Type** is `All TCP`, **Protocol** is `TCP`, **Port Range** includes all ports, and **Destination** is {{database-sg-id}}. Verify that the security group you have entered for **Destination** is the same as the security group you are editing.

    If using an Amazon S3 VPC endpoint, add an HTTPS rule to allow traffic from the VPC to Amazon S3. Create a rule where **Type** is `HTTPS`, **Protocol** is `TCP`, **Port Range** is `443` and **Destination** is the ID of the managed prefix list for the Amazon S3 gateway endpoint, {{s3-prefix-list-id}}. For more information about prefix lists and Amazon S3 gateway endpoints, see [Gateway endpoints for Amazon S3](https://docs.aws.amazon.com/vpc/latest/privatelink/vpc-endpoints-s3.html) in the Amazon VPC documentation.

   For example:    
[See the AWS documentation website for more details](http://docs.aws.amazon.com/glue/latest/dg/setup-vpc-for-glue-access.html)