# Option 3: Manually connect an instance to

an RDS database by creating security groups

The objective of Option 3 is to learn how to manually configure the connection between an
EC2 instance and an RDS database by manually reproducing the configuration of the
automatic connection feature.

###### Tasks

- [Before you begin](#option3-before-you-begin "#option3-before-you-begin")
- [Task 1 (Optional): Launch an EC2 instance](#option3-task1-launch-ec2-instance "#option3-task1-launch-ec2-instance")
- [Task 2 (Optional): Create an RDS database](#option3-task2-create-rds-database "#option3-task2-create-rds-database")
- [Task 3:
  Manually connect your EC2 instance to your RDS database](#option3-task3-connect-rds-database-to-ec2-instance "#option3-task3-connect-rds-database-to-ec2-instance")
- [Task 4 (Optional): Clean up](#tutorial-ec2-rds-clean-up "#tutorial-ec2-rds-clean-up")

## Before you begin

You'll need the following to complete this tutorial:

- An EC2 instance that is in the same VPC as the RDS database. You can either use an
  existing EC2 instance or follow the steps in Task 1 to create a new
  instance.
- An RDS database that is in the same VPC as the EC2 instance. You can either use an
  existing RDS database or follow the steps in Task 2 to create a new
  database.
- Permissions to call the following operations:
  - `ec2:AssociateRouteTable`
  - `ec2:AuthorizeSecurityGroupEgress`
  - `ec2:CreateRouteTable`
  - `ec2:CreateSecurityGroup`
  - `ec2:CreateSubnet`
  - `ec2:DescribeInstances`
  - `ec2:DescribeNetworkInterfaces`
  - `ec2:DescribeRouteTables`
  - `ec2:DescribeSecurityGroups`
  - `ec2:DescribeSubnets`
  - `ec2:ModifyNetworkInterfaceAttribute`
  - `ec2:RevokeSecurityGroupEgress`

## Task 1 (_Optional_): Launch an EC2 instance

###### Note

Launching an instance is not the focus of this tutorial. If you already have an Amazon EC2
instance and would like to use it in this tutorial, you can skip this task.

The objective of this task is to launch an EC2 instance so that you can complete Task 3
where you configure the connection between your EC2 instance and your Amazon RDS
database. The steps in this task configure the EC2 instance as follows:

- Instance name: `tutorial-instance`
- AMI: Amazon Linux 2
- Instance type: `t2.micro`
- Auto-assign public IP: Enabled
- Security group with the following three rules:
  - Allow SSH from your IP address
  - Allow HTTPS traffic from anywhere
  - Allow HTTP traffic from anywhere

###### Important

In a production environment, you should configure your instance to meet your
specific needs.

###### To launch an EC2 instance

1. Sign in to the AWS Management Console and open the Amazon EC2 console at
   [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/ "https://console.aws.amazon.com/ec2/").
2. On the **EC2 Dashboard**, choose **Launch
   instance**.
3. Under **Name and tags**, for **Name**, enter a name to
   identify your instance. For this tutorial, name the instance
   `tutorial-instance-manual-1`. While the instance name is
   not mandatory, the name will help you easily identify it.
4. Under **Application and OS Images**, choose an AMI that meets your web
   server needs. This tutorial uses **Amazon
   Linux**.
5. Under **Instance type**, for **Instance type**, select
   an instance type that meets your web server needs. This tutorial uses
   `t2.micro`.

###### Note

Depending on when you created your account, you might be eligible to
use Amazon EC2 under the Free Tier.

If your created your AWS account before July 15,
2025 and it's less than 12 months old, you can use Amazon EC2 under the
Free Tier by selecting the **t2.micro** instance type,
or the **t3.micro** instance type in Regions where
**t2.micro** is unavailable. Be aware that when you
launch a **t3.micro** instance, it defaults to [Unlimited mode](burstable-performance-instances-unlimited-mode.md "burstable-performance-instances-unlimited-mode.md"), which might incur
additional charges based on CPU usage. If an instance type can be used
under the Free Tier, it is labeled **Free tier
eligible**.

If you created your AWS account on or after July 15, 2025, you can
use **t3.micro**, **t3.small**,
**t4g.micro**, **t4g.small**,
**c7i-flex.large**, and
**m7i-flex.large** instance types for 6 months or
until your credits are used up.

For more information, see [Free Tier benefits before and after July
15, 2025](ec2-free-tier-usage.md#ec2-free-tier-comparison "ec2-free-tier-usage.md#ec2-free-tier-comparison"). 6. Under **Key pair (login)**, for **Key pair name**,
choose your key pair. 7. Under **Network settings**, do the following:

    1. For **Network** and
     **Subnet**, if you haven’t made changes to
     your default VPC or subnets, you can keep the default settings.


    If you have made changes to your default VPC or subnets, check the following:


    	1. The instance must be in the same VPC as the RDS database. By default you have only
    	 one VPC.
    	2. The VPC that you’re launching your instance into must have an internet gateway
    	 attached to it so that you can access your web server
    	 from the internet. Your default VPC is automatically set
    	 up with an internet gateway.
    	3. To ensure that your instance receives a public IP address, for **Auto-assign
    	 public IP**, check that **Enable** is
    	 selected. If **Disable** is selected, choose
    	 **Edit** (to the right of **Network
    	 Settings**), and then, for **Auto-assign public
    	 IP**, choose **Enable**.
    2. To connect to your instance by using SSH, you need a security group rule that authorizes
     SSH (Linux) or RDP (Windows) traffic from your computer’s public IPv4
     address. By default, when you launch an instance, a new security group
     is created with a rule that allows inbound SSH traffic from
     anywhere.


    To make sure that only your IP address can connect to your instance,
     under **Firewall (security groups)**, from the
     drop-down list next to the **Allow SSH traffic from**
     checkbox, choose **My IP**.
    3. To allow traffic from the internet to your instance, select the
     following checkboxes:




    	* **Allow HTTPs traffic from the internet**
    	* **Allow HTTP traffic from the
    	 internet**

8. In the **Summary** panel, review your instance configuration and then
   choose **Launch instance**.
9. Choose **View all instances** to close the confirmation page and return
   to the console. Your instance will first be in a `pending`
   state, and will then go into the `running` state.

If the instance fails to launch or the state immediately goes to `terminated`
instead of `running`, see [Troubleshoot Amazon EC2 instance launch issues](troubleshooting-launch.md "troubleshooting-launch.md").

For more information about launching an instance, see [Launch an EC2 instance using the launch
instance wizard in the console](ec2-launch-instance-wizard.md "ec2-launch-instance-wizard.md").

![This animation shows how to launch an EC2 instance. For the text version of this animation, see the steps in the preceding procedure.](images/tutorial-launch-instance.gif)

## Task 2 (_Optional_): Create an RDS database

###### Note

Creating an RDS database is not the focus of this part of the tutorial. If you already have
an RDS database and would like to use it for this tutorial, you can skip this
task.

The objective of this task is to create an RDS database. You'll use this instance in Task 3
when you connect it to your EC2 instance. The steps in this task configure the RDS database as follows:

- Engine type: MySQL
- Template: Free tier
- DB instance identifier: `tutorial-database-manual`
- DB instance class: `db.t3.micro`

###### Important

In a production environment, you should configure your instance to meet your
specific needs.

###### To create a MySQL DB instance

1. Open the Amazon RDS console at
   [https://console.aws.amazon.com/rds/](https://console.aws.amazon.com/rds/ "https://console.aws.amazon.com/rds/").
2. From the Region selector (at top right), choose the AWS Region in which you created the
   EC2 instance. The EC2 instance and the DB instance must be in the same
   Region.
3. On the dashboard, choose **Create database**.
4. Under **Choose a database creation method**, choose **Easy
   create**. When you choose this option, the automatic
   connection feature to automatically configure the connection is not
   available.
5. Under **Engine options**, for **Engine type**, choose
   **MySQL**.
6. For **DB instance size**, choose **Free tier**.
7. For **DB instance identifier** enter a name for the RDS database. For
   this tutorial, enter
   `tutorial-database-manual`.
8. For **Master username**, leave the default name,
   which is `admin`.
9. For **Master password**, enter a password that you can remember for
   this tutorial, and then, for **Confirm
   password**, enter the password again.
10. Choose **Create database**.

On the **Databases** screen, the **Status** of the new
DB instance is **Creating** until the DB instance is
ready to use. When the status changes to **Available**,
you can connect to the DB instance. Depending on the DB instance class
and the amount of storage, it can take up to 20 minutes before the new
instance is available.

![This animation shows how to create a DB instance. For the text version of this animation, see the steps in the preceding procedure.](/images/AWSEC2/latest/UserGuide/images/tutorial-create-db-step2.gif)

## Task 3: Manually connect

your EC2 instance to your RDS database by creating security groups and assigning
them to the instances

The objective of this task is to reproduce the connection configuration of the automatic
connection feature by performing the following manually: You create two new
security groups, and then add a security group each to the EC2 instance and the
RDS database.

###### To create two new security groups and assign one each to the EC2 instance and RDS

database

1. Open the Amazon EC2 console at
   [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/ "https://console.aws.amazon.com/ec2/").
2. First create the security group to add to the EC2 instance, as
   follows:
   1. In the navigation pane, choose **Security
      Groups**.
   2. Choose **Create security
      group**.
   3. For **Security group name**, enter a
      descriptive name for the security group. For this tutorial,
      enter
      `ec2-rds-manual-configuration`.
   4. For **Description**, enter a brief description. For this tutorial,
      enter `EC2 instance security group to allow EC2
instance to securely connect to RDS
database`.
   5. Choose **Create security group**. You'll come back to this security
      group to add an outbound rule after you've created the RDS
      database security group.

3. Now, create the security group to add to the RDS database, as follows:
   1. In the navigation pane, choose **Security
      Groups**.
   2. Choose **Create security
      group**.
   3. For **Security group name**, enter a
      descriptive name for the security group. For this tutorial,
      enter
      `rds-ec2-manual-configuration`.
   4. For **Description**, enter a brief description. For this tutorial,
      enter `RDS database security group to allow EC2
instance to securely connect to RDS
database`.
   5. Under **Inbound rules**, choose
      **Add rule**, and do the
      following:
      1. For **Type**, choose
         **MYSQL/Aurora**.
      2. For **Source**, choose the EC2 instance security group
         **ec2-rds-manual-configuration**
         that you created in Step 2 of this procedure.

   6. Choose **Create security group**.

4. Edit the EC2 instance security group to add an outbound rule, as follows:
   1. In the navigation pane, choose **Security
      Groups**.
   2. Select the EC2 instance security group (you named it
      `ec2-rds-manual-configuration`), and
      choose the **Outbound rules** tab.
   3. Choose **Edit outbound rules**.
   4. Choose **Add rule**, and do the following:
      1. For **Type**, choose
         **MYSQL/Aurora**.
      2. For **Destination**, choose the RDS database security group
         **rds-ec2-manual-configuration**
         that you created in Step 3 of this procedure.
      3. Choose **Save rules**.

5. Add the EC2 instance security group to the EC2 instance as follows:
   1. In the navigation pane, choose
      **Instances**.
   2. Select your EC2 instance, and choose
      **Actions**,
      **Security**, **Change security
      groups**.
   3. Under **Associated security groups**,
      choose the **Select security groups**
      field, choose
      **ec2-rds-manual-configuration** that
      you created earlier, and then choose **Add security
      group**.
   4. Choose **Save**.

6. Add the RDS database security group to the RDS database as follows:
   1. Open the Amazon RDS console at
      [https://console.aws.amazon.com/rds/](https://console.aws.amazon.com/rds/ "https://console.aws.amazon.com/rds/").
   2. In the navigation pane, choose **Databases** and select your
      database.
   3. Choose **Modify**.
   4. Under **Connectivity**, for **Security group**, choose
      **rds-ec2-manual-configuration** that
      you created earlier, and then choose
      **Continue**.
   5. Under **Scheduling of modifications**,
      choose **Apply immediately**.
   6. Choose **Modify DB instance**.You have now completed the manual steps that mimic the automatic steps that occur when
      you use the automatic connection feature.

You have completed Option 3 of this tutorial. If you've completed Options 1, 2, and 3, and
you no longer need the resources that were created in this tutorial, you should delete them
to prevent incurring unnecessary costs. For more information, see
[Task 4 (Optional): Clean up](#tutorial-ec2-rds-clean-up "#tutorial-ec2-rds-clean-up").

## Task 4 (_Optional_): Clean up

###### Warning

**Terminating an instance is permanent and irreversible.**

After you terminate an instance, you can no longer connect to it, and it can't be recovered.
All attached Amazon EBS volumes that are configured to be deleted on termination are also permanently
deleted and can't be recovered. All data stored on instance store volumes is permanently lost.
For more information, see [How instance termination
works](how-ec2-instance-termination-works.md "how-ec2-instance-termination-works.md").

Before you terminate an instance, ensure that you have backed up all data that you need to
retain after the termination to persistent storage.

Now that you have completed the tutorial, it is good practice to clean up (delete) any resources you
no longer want to use. Cleaning up AWS resources prevents your account from incurring
any further charges.

If you launched an EC2 instance specifically for this tutorial, you can terminate it to stop incurring any charges associated with it.

###### To terminate an instance using the console

1. Open the Amazon EC2 console at
   [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/ "https://console.aws.amazon.com/ec2/").
2. In the navigation pane, choose **Instances**.
3. Select the instance that you created for this tutorial, and choose **Instance
   state**, **Terminate instance**.
4. Choose **Terminate** when prompted for confirmation.

If you created an RDS database specifically for this tutorial, you can delete it to stop
incurring any charges associated with it.

###### To delete an RDS database using the console

1. Open the Amazon RDS console at
   [https://console.aws.amazon.com/rds/](https://console.aws.amazon.com/rds/ "https://console.aws.amazon.com/rds/").
2. In the navigation pane, choose **Databases**.
3. Select the RDS database that you created for this tutorial, and choose
   **Actions**, **Delete**.
4. Enter `delete me` in the box, and then choose **Delete**.
