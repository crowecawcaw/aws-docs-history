# Option 1: Automatically connect an instance to

an RDS database using the EC2 console

The objective of Option 1 is to explore the automatic connection feature in the EC2 console
that automatically configures the connection between your EC2 instance and RDS
database to allow traffic from the EC2 instance to the RDS database. In Option 3,
you'll learn how to manually configure the connection.

###### Tasks

- [Before you begin](#option1-before-you-begin "#option1-before-you-begin")
- [Task 1 (Optional):
  Create an RDS database](#option1-task1-create-rds-database "#option1-task1-create-rds-database")
- [Task 2 (Optional): Launch an EC2 instance](#option1-task2-launch-ec2-instance "#option1-task2-launch-ec2-instance")
- [Task 3: Automatically
  connect your EC2 instance to your RDS database](#option1-task3-connect-ec2-instance-to-rds-database "#option1-task3-connect-ec2-instance-to-rds-database")
- [Task 4: Verify the connection
  configuration](#option1-task4-verify-connection-configuration "#option1-task4-verify-connection-configuration")
- [Task 5 (Optional): Clean up](#option2-task5-cleanup "#option2-task5-cleanup")

## Before you begin

You'll need the following to complete this tutorial:

- An RDS database that is in the same VPC as the EC2 instance. You can
  either use an existing RDS database or follow the steps in Task 1 to create
  a new RDS database.
- An EC2 instance that is in the same VPC as the RDS database. You can either use an
  existing EC2 instance or follow the steps in Task 2 to create a new EC2
  instance.
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

## Task 1 (_Optional_):

Create an RDS database

###### Note

Creating a Amazon RDS database is not the focus of this tutorial. If you already
have an RDS database and would like to use it in this tutorial, you can skip
this task.

If you use an existing RDS database, make sure that it is in the same VPC
as your EC2 instance so that you can use the automatic connection
feature.

The objective of this task is to create an RDS database so that you can
complete Task 3 where you configure the connection between your EC2 instance and
your RDS database. The steps in this task configure the RDS database as follows:

- Engine type: MySQL
- Template: Free tier
- DB instance identifier:
  `tutorial-database-1`
- DB instance class: `db.t3.micro`

###### Important

In a production environment, you should configure your database to meet
your specific needs.

###### To create a MySQL RDS database

1. Open the Amazon RDS console at
   [https://console.aws.amazon.com/rds/](https://console.aws.amazon.com/rds/ "https://console.aws.amazon.com/rds/").
2. From the Region selector (at top right), choose an AWS Region. The database and the
   EC2 instance must be in the same Region in order to use the automatic
   connection feature in the EC2 console.
3. On the dashboard, choose **Create database**.
4. Under **Choose a database creation method**, check
   that **Standard create** is selected. If you choose
   **Easy create**, the VPC selector is not available.
   You must ensure that your database is in the same VPC as your EC2
   instance in order to use the automatic connection feature in the EC2
   console.
5. Under **Engine options**, for **Engine
   type**, choose **MySQL**.
6. Under **Templates**, choose a sample template to meet your needs. For
   this tutorial, choose **Free tier** to create an RDS
   database at no cost. However, note that the Free Tier is only available for
   accounts that qualify for the Free Tier. You can read more by choosing the
   **Info** link in the **Free tier**
   box.
7. Under **Settings**, do the following:
   1. For **DB instance identifier**, enter a name
      for the database. For this tutorial, enter
      `tutorial-database-1`.
   2. For **Master username**, leave the default
      name, which is `admin`.
   3. For **Master password**, enter a password
      that you can remember for this tutorial, and then, for
      **Confirm password**, enter the password
      again.

8. Under **Instance configuration**, for **DB instance
   class**, leave the default, which is
   **db.t3.micro**.If your
   account qualifies for the Free Tier, you can use this database class for
   free. For more information, see [AWS Free Tier](https://aws.amazon.com/free/ "https://aws.amazon.com/free/").
9. Under **Connectivity**, for **Compute
   resource**, choose **Don't connect to an EC2
   compute resource** because you'll connect the EC2 instance
   and the RDS database later in Task 3.

(Later, in Option 2 of this tutorial, you'll try out the automatic connection feature in
the RDS console by choosing **Connect to an EC2 compute
resource**.) 10. For **Virtual private cloud (VPC)**, choose a VPC. The VPC must have a
DB subnet group. To use the automatic connection feature, your EC2
instance and RDS database must be in the same VPC. 11. Keep all the default values for the other fields on this page. 12. Choose **Create database**.

On the **Databases** screen, the **Status** of the new
database is **Creating** until the database is ready to
use. When the status changes to **Available**, you can
connect to the database. Depending on the database class and the amount
of storage, it can take up to 20 minutes before the new database is
available.

![This animation shows how to create an RDS database. For the text version of this animation, see the steps in the preceding procedure.](images/tutorial-create-rds-database.gif)

## Task 2 (_Optional_): Launch an EC2 instance

###### Note

Launching an instance is not the focus of this tutorial. If you already have an Amazon EC2
instance and would like to use it in this tutorial, you can skip this task.

If you use an existing EC2 instance, make sure that it is in the same VPC
as your RDS database so that you can use the automatic connection
feature.

The objective of this task is to launch an EC2 instance so that you can complete Task 3
where you configure the connection between your EC2 instance and your Amazon RDS
database. The steps in this task configure the EC2 instance as follows:

- Instance name: `tutorial-instance-1`
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

1. Open the Amazon EC2 console at
   [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/ "https://console.aws.amazon.com/ec2/").
2. From the Region selector (at top right), choose an AWS Region. The instance and the RDS
   database must be in the same Region in order to use the automatic
   connection feature in the EC2 console.
3. On the **EC2 Dashboard**, choose **Launch
   instance**.
4. Under **Name and tags**, for **Name**, enter a name to
   identify your instance. For this tutorial, name the instance
   `tutorial-instance-1`. While the instance name
   is not mandatory, when you select your instance in the EC2 console, the
   name will help you easily identify it.
5. Under **Application and OS Images**, choose an AMI that meets your web
   server needs. This tutorial uses **Amazon Linux 2**.
6. Under **Instance type**, for **Instance type**, select
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
15, 2025](ec2-free-tier-usage.md#ec2-free-tier-comparison "ec2-free-tier-usage.md#ec2-free-tier-comparison"). 7. Under **Key pair (login)**, for **Key pair name**,
choose your key pair. 8. Under **Network settings**, do the following:

    1. For **Network** and
     **Subnet**, if you haven’t made changes to
     your default VPC or subnets, you can keep the default settings.


    If you have made changes to your default VPC or subnets, check the following:


    	1. The instance must be in the same VPC as the RDS database to use the automatic
    	 connection feature. By default you have only one
    	 VPC.
    	2. The VPC that you’re launching your instance into must have an internet gateway
    	 attached to it so that you can access your web server
    	 from the internet. Your default VPC is automatically set
    	 up with an internet gateway.
    	3. To ensure that your instance receives a public IP address, for **Auto-assign
    	 public IP**, check that
    	 **Enable** is selected. If
    	 **Disable** is selected, choose
    	 **Edit** (to the right of
    	 **Network Settings**), and then,
    	 for **Auto-assign public IP**, choose
    	 **Enable**.
    2. To connect to your instance by using SSH, you need a security
     group rule that authorizes SSH (Linux) or RDP (Windows) traffic
     from your computer’s public IPv4 address. By default, when you
     launch an instance, a new security group is created with a rule
     that allows inbound SSH traffic from anywhere.


    To make sure that only your IP address can connect to your instance,
     under **Firewall (security groups)**, from the
     drop-down list next to the **Allow SSH traffic from**
     checkbox, choose **My IP**.
    3. To allow traffic from the internet to your instance, select the
     following checkboxes:




    	* **Allow HTTPs traffic from the internet**
    	* **Allow HTTP traffic from the
    	 internet**

9. In the **Summary** panel, review your instance configuration and then
   choose **Launch instance**.
10. Keep the confirmation page open. You'll need it for the next task when you automatically
    connect your instance to your database.

If the instance fails to launch or the state immediately goes to `terminated`
instead of `running`, see [Troubleshoot Amazon EC2 instance launch issues](troubleshooting-launch.md "troubleshooting-launch.md").

For more information about launching an instance, see [Launch an EC2 instance using the launch
instance wizard in the console](ec2-launch-instance-wizard.md "ec2-launch-instance-wizard.md").

![This animation shows how to launch an EC2 instance. For the text version of this animation, see the steps in the preceding procedure.](images/tutorial-launch-instance.gif)

## Task 3: Automatically

connect your EC2 instance to your RDS database

The objective of this task is to use the automatic connection feature in the EC2 console
to automatically configure the connection between your EC2 instance and your RDS
database.

###### To automatically connect an EC2 instance to an RDS database using the EC2 console

1. On the instance launch confirmation page (it should be open from the
   previous task), choose **Connect an RDS
   database**.

If you closed the confirmation page, follow these steps:

    1. Open the Amazon EC2 console at
     [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/ "https://console.aws.amazon.com/ec2/").
    2. In the navigation pane, choose **Instances**.
    3. Select the EC2 instance that you just created, and then choose
     **Actions**,
     **Networking**, **Connect RDS
     database**.


    If **Connect RDS database** is not available, check that the EC2
     instance is in the **Running** state.

2. For **Database role**, choose **Instance**. _Instance_ in this case refers to the
   database instance.
3. For **RDS database**, choose the RDS database that you created in Task
4.

###### Note

The EC2 instance and the RDS database must be in the same VPC in order to connect to
each other. 4. Choose **Connect**.

![This animation shows how to select an existing EC2 instance in the EC2 console and use the automatic connection feature to connect the EC2 instance to an RDS database. For the text version of this animation, see the steps in the preceding procedure.](images/tutorial-connect-new-ec2-rds.gif)

## Task 4: Verify the connection

configuration

The objective of this task is to verify that the two security groups were created and
assigned to the instance and database.

When you use the automatic connection feature in the console to configure the
connectivity, the security groups are automatically created and assigned to the
instance and database, as follows:

- Security group
  **rds-ec2-`x`** is created
  and added to the RDS database. It has one inbound rule that references
  the **ec2-rds-`x`** security
  group as its source. This allows traffic from the EC2 instance with the
  **ec2-rds-`x`**
  security group to reach the RDS database.
- Security group
  **ec2-rds-`x`** is created
  and added to the EC2 instance. It has one outbound rule that references
  the **rds-ec2-`x`** security
  group as its destination. This allows traffic from the EC2 instance to
  reach the RDS database with the
  **rds-ec2-`x`**
  security group.

###### To verify the connection configuration using the console

1. Open the Amazon RDS console at
   [https://console.aws.amazon.com/rds/](https://console.aws.amazon.com/rds/ "https://console.aws.amazon.com/rds/").
2. In the navigation page, choose **Databases**.
3. Choose the RDS database that you created for this tutorial.
4. On the **Connectivity & security** tab, under
   **Security**, **VPC security
   groups**, verify that a security group called
   **rds-ec2-`x`** is
   displayed.
5. Choose the **rds-ec2-`x`** security group. The
   **Security Groups** screen in the EC2 console
   opens.
6. Choose the **rds-ec2-`x`**
   security group to open it.
7. Choose the **Inbound rules** tab.
8. Verify that the following security group rule exists, as
   follows:
   - Type: **MYSQL/Aurora**
   - Port range: **3306**
   - Source: **`sg-0987654321example` /
     ec2-rds-`x`** –
     This is the security group that is assigned to the EC2 instance
     that you verified in the preceding steps.
   - Description: **Rule to allow connections from EC2 instances with
     `sg-1234567890example`
     attached**

9. Open the Amazon EC2 console at
   [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/ "https://console.aws.amazon.com/ec2/").
10. In the navigation pane, choose **Instances**.
11. Choose the EC2 instance that you selected to connect to the RDS database in the previous
    task, and choose the **Security** tab.
12. Under **Security details**, **Security groups**,
    verify that a security group called
    **ec2-rds-`x`** is in
    the list. `x` is a number.
13. Choose the **ec2-rds-`x`**
    security group to open it.
14. Choose the **Outbound rules** tab.
15. Verify that the following security group rule exists, as
    follows:
    - Type: **MYSQL/Aurora**
    - Port range: **3306**
    - Destination: **`sg-1234567890example` /
      rds-ec2-`x`**
    - Description: **Rule to allow connections to
      `database-tutorial` from any
      instances this security group is attached
      to**

By verifying that these security groups and security group rules exist and that they are
assigned to the RDS database and EC2 instance as described in this
procedure, you can verify that the connection was automatically
configured by using the automatic connection feature.

![This animation shows how to verify the connection configuration. For the text version of this animation, see the steps in the preceding procedure.](/images/AWSEC2/latest/UserGuide/images/tutorial-verify-automatic-connection.gif)

You have completed Option 1 of this tutorial. You can now either complete Option 2, which
teaches you how to use the RDS console to automatically connect an EC2 instance
to an RDS database, or you can complete Option 3, which teaches you how to
manually configure the security groups that were automatically created in Option

1.

## Task 5 (_Optional_): Clean up

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
