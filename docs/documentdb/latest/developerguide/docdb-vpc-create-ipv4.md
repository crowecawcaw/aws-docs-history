# Create an IPv4-only VPC for use with a DocumentDB cluster

A common scenario includes a cluster in a virtual private cloud (VPC) based on the Amazon VPC service.
For example, this VPC could share data with a service or application that is running in the same VPC.
In this topic, you create the VPC for this scenario.

###### Topics

- [Step 1: Create a VPC with private and public subnets](#vpc-private-public-subnets "#vpc-private-public-subnets")
- [Step 2: Create a VPC security group for a public application](#create-vpc-sg-public "#create-vpc-sg-public")
- [Step 3: Create a VPC security group for a private cluster](#create-vpc-sg-private "#create-vpc-sg-private")
- [Step 4: Create a subnet group](#create-cluster-subnet-group "#create-cluster-subnet-group")
- [Deleting a VPC](#docdb-delete-vpc "#docdb-delete-vpc")
  Your cluster needs to be available only to your application, and not to the public internet.
  Thus, you create a VPC with both public and private subnets.
  The application is hosted in the public subnet, so that it can reach the public internet.
  The cluster is hosted in a private subnet.
  The application can connect to the cluster because it is hosted within the same VPC.
  But the cluster isn't available to the public internet, providing greater security.

The procedure in this topic configures an additional public and private subnet in a separate Availability Zone.
These subnets aren't used by the procedure.
A DocumentDB subnet group requires a subnet in at least two Availability Zones.
The additional subnet makes it easier to configure more than one DocumentDB instance.

This topic describes configuring a VPC for Amazon DocumentDB clusters.
For more information about Amazon VPC, see the [_Amazon VPC User Guide_](../../../vpc/latest/userguide/what-is-amazon-vpc.md "../../../vpc/latest/userguide/what-is-amazon-vpc.md").

###### Tip

You can set up network connectivity between an Amazon EC2 instance and a DocumentDB cluster automatically when you create the cluster.
The network configuration is similar to the one described in this scenario.
For more information, see [Connect Amazon EC2 automatically](connect-ec2-auto.md "connect-ec2-auto.md").

## Step 1: Create a VPC with private and public subnets

Use the following procedure to create a VPC with both public and private subnets.

**To create a VPC and subnets**

1. Open the Amazon VPC console at [https://console.aws.amazon.com/vpc](https://console.aws.amazon.com//vpc "https://console.aws.amazon.com//vpc").
2. In the top-right corner of the AWS Management Console, choose the Region to create your VPC in.
   This example uses the US West (Oregon) Region.
3. In the upper-left corner, choose **VPC dashboard**.
   To begin creating a VPC, choose **Create VPC**.
4. For **Resources to create** under **VPC settings**, choose **VPC and more**.
5. For the **VPC settings**, set these values:
   - **Name tag auto-generation** — `example`
   - **IPv4 CIDR block** — `10.0.0.0/16`
   - **IPv6 CIDR block** — **No IPv6 CIDR block**
   - **Tenancy** — **Default**
   - **Number of Availability Zones (AZs)** — **2**
   - **Customize AZs** — Keep the default values
   - **Number of public subnets** — **2**
   - **Number of private subnets** — **2**
   - **Customize subnets CIDR blocks** — Keep the default values
   - **NAT gateways ($)** — **None**
   - **VPC endpoints** — **None**
   - **DNS options** — Keep the default values

6. Choose **Create VPC**.

## Step 2: Create a VPC security group for a public application

Next, create a security group for public access.
To connect to public EC2 instances in your VPC, you add inbound rules to your VPC security group.
These allow traffic to connect from the internet.

**To create a VPC security group**

1.  Open the Amazon VPC console at [https://console.aws.amazon.com/vpc](https://console.aws.amazon.com//vpc "https://console.aws.amazon.com//vpc").
2.  Choose **VPC Dashboard**, choose **Security Groups**, and then choose **Create security group**.
3.  On the **Create security group** page, set these values:
    - **Security group name** — `example-securitygroup`
    - **Description** — `Application security group`
    - **VPC** — Choose the VPC that you created earlier, for example: **vpc-example**.

4.  Add inbound rules to the security group.
    1. Determine the IP address to use to connect to EC2 instances in your VPC using Secure Shell (SSH).
       To determine your public IP address, in a different browser window or tab, you can use the service at [https://checkip.amazonaws.com](https://checkip.amazonaws.com "https://checkip.amazonaws.com").
       An example of an IP address is `203.0.113.25/32`.

    In many cases, you might connect through an internet service provider (ISP) or from behind your firewall without a static IP address.
    If so, find the range of IP addresses used by client computers.

    ###### Warning

    If you use `0.0.0.0/0` for SSH access, you make it possible for all IP addresses to access your public instances using SSH.
    This approach is acceptable for a short time in a test environment, but it's unsafe for production environments.
    In production, authorize only a specific IP address or range of addresses to access your instances using SSH. 2. In the **Inbound rules** section, choose **Add rule**. 3. Set the following values for your new inbound rule to allow SSH access to your Amazon EC2 instance.
    After you do this, you can connect to your EC2 instance to install the application and other utilities.
    You also connect to your EC2 instance to upload content for your application.

        * **Type** — `SSH`
        * **Source** — The IP address or range you created from Step a, for example: `203.0.113.25/32`

    4. Choose **Add rule**.
    5. Set the following values for your new inbound rule to allow HTTP access to your application:
       - **Type** — `HTTP`
       - **Source** — `0.0.0.0/0`

5.  Choose **Create security group** to create the security group.

Note the security group ID because you need it later in another procedure.

## Step 3: Create a VPC security group for a private cluster

To keep your cluster private, create a second security group for private access.
To connect to private clusters in your VPC, you add inbound rules to your VPC security group that allow traffic from your application only.

**To create a VPC security group**

1. Open the Amazon VPC console at [https://console.aws.amazon.com/vpc](https://console.aws.amazon.com//vpc "https://console.aws.amazon.com//vpc").
2. Choose **VPC Dashboard**, choose **Security Groups**, and then choose **Create security group**.
3. On the **Create security group** page, set these values:
   - **Security group name** — `example-securitygroup`
   - **Description** — `Instance security group`
   - **VPC** — Choose the VPC that you created earlier, for example: **vpc-example**

4. Add inbound rules to the security group.
   1. In the **Inbound rules** section, choose **Add rule**.
   2. Set the following values for your new inbound rule to allow DocumentDB traffic on port 27017 from your Amazon EC2 instance.
      After you do this, you can connect from your application to your cluster.
      By doing so, you can store and retrieve data from your application to your database.
      - **Type** — `Custom TCP`
      - **Source** — The identifier of the application security group that you created previously in this topic, for example: **sg-9edd5cfb**.

   3. Choose **Add rule**.
   4. Set the following values for your new inbound rule to allow HTTP access to your application:
      - **Type** — `HTTP`
      - **Source** — `0.0.0.0/0`

5. Choose **Create security group** to create the security group.

## Step 4: Create a subnet group

A subnet group is a collection of subnets that you create in a VPC and that you then designate for your clusters.
A subnet group makes it possible for you to specify a particular VPC when creating clusters.

**To create a subnet group**

1. Identify the private subnets for your database in the VPC.
   1. Open the Amazon VPC console at [https://console.aws.amazon.com/vpc](https://console.aws.amazon.com//vpc "https://console.aws.amazon.com//vpc").
   2. Choose **VPC Dashboard**, and then choose **Subnets**.
   3. Note the subnet IDs of the subnets you created in Step 1 named, for example: **example-subnet-private1-us-west-2a** and **example-subnet-private2-us-west-2b**.
      You need the subnet IDs when you create your subnet group.

2. Sign in to the AWS Management Console, and open the Amazon DocumentDB console at [https://console.aws.amazon.com/docdb](https://console.aws.amazon.com/docdb "https://console.aws.amazon.com/docdb").

Make sure that you connect to the Amazon DocumentDB console, not to the Amazon VPC console. 3. In the navigation pane, choose **Subnet groups**. 4. Choose **Create**. 5. On the **Create subnet group** page, set these values in the **Subnet group details** section:

    * **Name** — `example-db-subnet-group`
    * **Description** — `Instance security group`

6. In the **Add subnets** section, set these values:
   - **VPC** — Choose the VPC that you created earlier, for example: **vpc-example**
   - **Availability Zones** — Select both Availability Zones created in Step 1. Example: **us-west-2a** and **us-west-2b**
   - **Subnets** — Choose the private subnets you created in Step 1.

7. Choose **Create**.

Your new subnet group appears in the subnet groups list on the DocumentDB console.
You can choose the subnet group to see details in the details pane.
These details include all of the subnets associated with the group.

###### Note

If you created this VPC to associated it with a DocumentDB cluster, create the cluster by following the instructions in [Creating an Amazon DocumentDB cluster](db-cluster-create.md "db-cluster-create.md").

## Deleting a VPC

You can delete a VPC and the other resources that are used within it, if they are no longer needed.

###### Note

If you added resources in the VPC that you created in this topic, you might need to delete these before you can delete the VPC.
For example, these resources might include Amazon EC2 instances or DocumentDB clusters.
For more information, see [Delete your VPC](../../../vpc/latest/userguide/delete-vpc.md "../../../vpc/latest/userguide/delete-vpc.md") in the _Amazon VPC User Guide_.

**To delete a VPC and related resources**

1. Delete the subnet group:
   1. Sign in to the AWS Management Console, and open the Amazon DocumentDB console at [https://console.aws.amazon.com/docdb](https://console.aws.amazon.com/docdb "https://console.aws.amazon.com/docdb").
   2. In the navigation pane, choose **Subnet groups**.
   3. Select the subnet group you want to delete, such as **example-db-subnet-group**.
   4. Choose **Delete**, and then choose **Delete** in the confirmation window.

2. Note the VPC ID:
   1. Open the Amazon VPC console at [https://console.aws.amazon.com/vpc](https://console.aws.amazon.com//vpc "https://console.aws.amazon.com//vpc").
   2. Choose **VPC Dashboard**, and then choose **Your VPCs**.
   3. In the list, identify the VPC that you created, such as **vpc-example**.
   4. Note the **VPC ID** of the VPC that you created.
      You need the VPC ID in later steps.

3. Delete the security groups:
   1. Open the Amazon VPC console at [https://console.aws.amazon.com/vpc](https://console.aws.amazon.com//vpc "https://console.aws.amazon.com//vpc").
   2. Choose **VPC Dashboard**, and then choose **Security Groups**.
   3. Select the security group for the Amazon DocumentDB cluster, such as **example-securitygroup**.
   4. For **Actions**, choose **Delete security groups**, and then choose **Delete** on the confirmation dialog.
   5. Back on the **Security Groups** page, select the security group for the Amazon EC2 instance, such as **example-securitygroup**.
   6. For **Actions**, choose **Delete security groups**, and then choose **Delete** on the confirmation dialog.

4. Delete the VPC:
   1. Open the Amazon VPC console at [https://console.aws.amazon.com/vpc](https://console.aws.amazon.com//vpc "https://console.aws.amazon.com//vpc").
   2. Choose **VPC Dashboard**, and then choose **Your VPCs**.
   3. Select the VPC you want to delete, such as **vpc-example**.
   4. For **Actions**, choose Delete VPC.

   The confirmation page shows other resources that are associated with the VPC that will also be deleted, including the subnets associated with it. 5. On the confirmation dialog, enter `delete`, and then choose **Delete**.
