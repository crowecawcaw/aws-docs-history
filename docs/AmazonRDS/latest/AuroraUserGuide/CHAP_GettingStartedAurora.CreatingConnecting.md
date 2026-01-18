# Creating and connecting to an Aurora PostgreSQL DB cluster

This tutorial creates an EC2 instance and an Aurora PostgreSQL DB cluster. The tutorial shows you how to access the DB
cluster from the EC2 instance using a standard PostgreSQL client. As a best practice, this
tutorial creates a private DB cluster in a virtual private cloud (VPC). In most cases,
other resources in the same VPC, such as EC2 instances, can access the DB cluster, but resources
outside of the VPC can't access it.

After you complete the tutorial, there is a public and private subnet in each
Availability Zone in your VPC. In one Availability Zone, the EC2 instance is in the
public subnet, and the DB instance is in the private subnet.

###### Important

There's no charge for creating an AWS account. However, by completing this tutorial, you might incur
costs for the AWS resources that you use. You can delete these resources after you complete the tutorial
if they are no longer needed.

The following diagram shows the configuration when the tutorial is complete.

![EC2 instance and Aurora PostgreSQL DB cluster.](images/getting-started-aurora-postgresql.png)
This tutorial allows you to create your resources by using one of the following methods:

1. Use the AWS Management Console ‐
   [Step 1: Create
   an EC2 instance](#CHAP_GettingStarted.Creating.AuroraPostgreSQL.EC2 "#CHAP_GettingStarted.Creating.AuroraPostgreSQL.EC2")and
   [Step 2: Create an
   Aurora PostgreSQL DB cluster](#CHAP_GettingStarted.AuroraPostgreSQL.CreateDBCluster "#CHAP_GettingStarted.AuroraPostgreSQL.CreateDBCluster")
2. Use CloudFormation to create the database instance and EC2 instance ‐
   [(Optional) Create VPC, EC2 instance, and Aurora PostgreSQL cluster using CloudFormation](#CHAP_GettingStartedAurora.CFN.PostgreSQL "#CHAP_GettingStartedAurora.CFN.PostgreSQL")
   The first method uses **Easy create** to create a private Aurora PostgreSQL DB cluster with the AWS Management Console.
   Here, you specify only the DB engine type, DB instance size, and DB cluster identifier.
   **Easy create** uses the default settings for the other configuration options.

When you use **Standard create** instead, you can specify more configuration options when you create a DB cluster.
These options include settings for availability, security, backups, and maintenance.
To create a public DB cluster, you must use **Standard create**.
For information, see [Creating an Amazon Aurora DB cluster](Aurora.md "Aurora.md").

###### Topics

- [Prerequisites](#CHAP_GettingStarted.Prerequisites.AuroraPostgreSQL "#CHAP_GettingStarted.Prerequisites.AuroraPostgreSQL")
- [Step 1: Create
  an EC2 instance](#CHAP_GettingStarted.Creating.AuroraPostgreSQL.EC2 "#CHAP_GettingStarted.Creating.AuroraPostgreSQL.EC2")
- [Step 2: Create an
  Aurora PostgreSQL DB cluster](#CHAP_GettingStarted.AuroraPostgreSQL.CreateDBCluster "#CHAP_GettingStarted.AuroraPostgreSQL.CreateDBCluster")
- [(Optional) Create VPC, EC2 instance, and Aurora PostgreSQL cluster using CloudFormation](#CHAP_GettingStartedAurora.CFN.PostgreSQL "#CHAP_GettingStartedAurora.CFN.PostgreSQL")
- [Step 3: Connect to an Aurora PostgreSQL
  DB cluster](#CHAP_GettingStartedAurora.AuroraPostgreSQL.Connect "#CHAP_GettingStartedAurora.AuroraPostgreSQL.Connect")
- [Step 4: Delete the EC2
  instance and DB cluster](#CHAP_GettingStartedAurora.Deleting.AuroraPostgreSQL "#CHAP_GettingStartedAurora.Deleting.AuroraPostgreSQL")
- [(Optional) Delete the EC2 instance and DB cluster created with CloudFormation](#CHAP_GettingStartedAurora.DeletingCFN.AuroraPostgreSQL "#CHAP_GettingStartedAurora.DeletingCFN.AuroraPostgreSQL")
- [(Optional) Connect your DB cluster to a Lambda function](#CHAP_GettingStartedAurora.ComputeConnect.AuroraPostgreSQL "#CHAP_GettingStartedAurora.ComputeConnect.AuroraPostgreSQL")

## Prerequisites

Before you begin, complete the steps in the following sections:

- [Sign up for an AWS account](CHAP_SettingUp_Aurora.md#sign-up-for-aws "CHAP_SettingUp_Aurora.md#sign-up-for-aws")
- [Create a user with administrative access](CHAP_SettingUp_Aurora.md#create-an-admin "CHAP_SettingUp_Aurora.md#create-an-admin")

## Step 1: Create

an EC2 instance

Create an Amazon EC2 instance that you will use to connect to your database.

###### To create an EC2 instance

1. Sign in to the AWS Management Console and open the Amazon EC2 console at
   [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/ "https://console.aws.amazon.com/ec2/").
2. In the upper-right corner of the AWS Management Console, choose the AWS Region in which you
   want to create the EC2 instance.
3. Choose **EC2 Dashboard**, and then choose **Launch
   instance**, as shown in the following image.

![EC2 Dashboard.](images/Tutorial_WebServer_11.png)

The **Launch an instance** page opens. 4. Choose the following settings on the **Launch an instance**
page.

    1. Under **Name and tags**, for **Name**, enter
     `ec2-database-connect`.
    2. Under **Application and OS Images (Amazon Machine
     Image)**, choose **Amazon Linux**, and then choose the
     **Amazon Linux 2023 AMI**. Keep the default selections for the
     other choices.



    ![Choose an Amazon Machine Image.](images/Tutorial_WebServer_12.png)
    3. Under **Instance type**, choose **t2.micro**.
    4. Under **Key pair (login)**, choose a **Key pair name** to use an existing key
     pair. To create a new key pair for the Amazon EC2 instance, choose **Create new key pair**
     and then use the **Create key pair** window to create it.


    For more information about creating a new key pair, see [Create a key pair](../../../AWSEC2/latest/UserGuide/get-set-up-for-amazon-ec2.md#create-a-key-pair "../../../AWSEC2/latest/UserGuide/get-set-up-for-amazon-ec2.md#create-a-key-pair")
     in the *Amazon EC2 User Guide*.
    5. For **Allow SSH traffic** in **Network
     settings**, choose the source of SSH connections to the EC2
     instance.


    You can choose **My IP** if the displayed IP address is
     correct for SSH connections. Otherwise, you can determine the IP address to
     use to connect to EC2 instances in your VPC using Secure Shell (SSH). To
     determine your public IP address, in a different browser window or tab, you
     can use the service at [https://checkip.amazonaws.com](https://checkip.amazonaws.com/ "https://checkip.amazonaws.com/"). An example of an IP address is
     192.0.2.1/32.


     In many cases, you might connect through an
     internet service provider (ISP) or from behind your firewall without a
     static IP address. If so, make sure to determine the range of IP addresses
     used by client computers.

    ###### Warning

    If you use `0.0.0.0/0` for SSH access, you make it possible
     for all IP addresses to access your public EC2 instances using SSH. This
     approach is acceptable for a short time in a test environment, but it's
     unsafe for production environments. In production, authorize only a
     specific IP address or range of addresses to access your EC2 instances
     using SSH.

    The following image shows an example of the **Network settings**
     section.


    ![Network settings for an EC2 instance.](images/EC2_RDS_Connect_NtwkSettings.png)
    6. Leave the default values for the remaining sections.
    7. Review a summary of your EC2 instance configuration in the **Summary** panel, and when you're ready,
     choose **Launch instance**.

5. On the **Launch Status** page, note the identifier for your new
   EC2 instance, for example: `i-1234567890abcdef0`.

![EC2 instance identifier on Launch Status page.](images/getting-started-ec2-id.png) 6. Choose the EC2 instance identifier to open the list of EC2 instances, and then
select your EC2 instance. 7. In the **Details** tab, note the following values, which you
need when you connect using SSH:

    1. In **Instance summary**, note the value for
     **Public IPv4 DNS**.



    ![EC2 public DNS name on Details tab of Instances page.](images/easy-create-ec2-public-dns.png)
    2. In **Instance details**, note the value for **Key
     pair name**.



    ![EC2 key pair name on Details tab of Instance page.](images/easy-create-ec2-key-pair.png)

8. Wait until the **Instance state** for your EC2 instance has a status
   of **Running** before continuing.

## Step 2: Create an

Aurora PostgreSQL DB cluster

In this example, you use **Easy create** to create an Aurora PostgreSQL DB cluster
with a db.t4g.large DB instance class.

###### To create an Aurora PostgreSQL DB cluster with Easy create

1. Sign in to the AWS Management Console and open the Amazon RDS console at
   [https://console.aws.amazon.com/rds/](https://console.aws.amazon.com/rds/ "https://console.aws.amazon.com/rds/").
2. In the upper-right corner of the Amazon RDS console, choose the AWS Region in which you want to
   create the DB cluster.
3. In the navigation pane, choose **Databases**.
4. Choose **Create database**, and make sure that **Easy create** is chosen.

![Create database section: Easy create option selected.](images/easy-create-option.png) 5. In **Configuration**, choose **Aurora (PostgreSQL
Compatible)** for **Engine type**. 6. For **DB instance size**, choose **Dev/Test**. 7. For **DB cluster identifier**, enter `database-test1`.

The **Create database** page should look similar to the following image.

![Configuration section with selections.](images/easy-create-aurora-postgresql.png) 8. For **Master username**, enter a name for the user, or
keep the default name (`postgres`). 9. To use an automatically generated master password for the DB cluster, select **Auto generate a
password**.

To enter your master password, make sure **Auto generate a password** is cleared, and then enter the same
password in **Master password** and **Confirm password**. 10. To set up a connection with the EC2 instance you created previously, open
**Set up EC2 connection -
_optional_**.

Select **Connect to an EC2 compute resource**. Choose the
EC2 instance you created previously.

![Set up EC2 connection option.](images/EC2_RDS_Setup_Conn-EasyCreate.png) 11. Open **View default settings for Easy create**.

![Easy create default settings.](images/easy-create-view-default-settings-aurora-postgresql.png)

You can examine the default settings used with **Easy create**. The
**Editable after database is created** column shows which
options you can change after you create the database.

    * If a setting has **No** in that column, and you want
     a different setting, you can use **Standard create** to
     create the DB cluster.
    * If a setting has **Yes** in that column, and you want a different
     setting, you can either use **Standard create** to
     create the DB cluster, or modify the DB cluster after you create it to
     change the setting.

12. Choose **Create database**.

To view the master username and password for the DB cluster, choose
**View credential details**.

You can use the username and password that appears to connect to the DB
cluster as the master user.

###### Important

You can't view the master user password again. If you don't record it, you
might have to change it.

If you need to change the master user password
after the DB cluster is available, you can modify the DB cluster to do
so. For more information about modifying a DB cluster, see [Modifying an Amazon Aurora DB cluster](Aurora.md "Aurora.md"). 13. In the **Databases** list, choose the name of the new Aurora PostgreSQL
DB cluster to show its details.

The writer instance has a status of **Creating** until the
DB cluster is ready to use.

![DB cluster details showing Region & AZ and Status.](images/creating-status-aurora-postgresql.png)

When the status of the writer instance changes to **Available**, you can
connect to the DB cluster. Depending on the DB instance class and the amount
of storage, it can take up to 20 minutes before the new DB cluster is
available.

## (Optional) Create VPC, EC2 instance, and Aurora PostgreSQL cluster using CloudFormation

Instead of using the console to create your VPC, EC2 instance, and Aurora PostgreSQL DB cluster, you can use CloudFormation to provision AWS resources by treating infrastructure as code.
To help you organize your AWS resources into smaller and more manageable units, you can use the CloudFormation nested stack functionality.
For more information, see [Creating a stack on the CloudFormation console](../../../AWSCloudFormation/latest/UserGuide/cfn-console-create-stack.md "../../../AWSCloudFormation/latest/UserGuide/cfn-console-create-stack.md") and
[Working with nested stacks](../../../AWSCloudFormation/latest/UserGuide/using-cfn-nested-stacks.md "../../../AWSCloudFormation/latest/UserGuide/using-cfn-nested-stacks.md").

###### Important

CloudFormation is free, but the resources that CloudFormation creates are live. You incur the standard
usage fees for these resources until you terminate them. For more information,
see [Amazon Aurora
Pricing](https://aws.amazon.com/rds/aurora/pricing/ "https://aws.amazon.com/rds/aurora/pricing/").

To create your resources using the CloudFormation console, complete the following steps:

- Step 1: Download the CloudFormation template
- Step 2: Configure your resources using CloudFormation

### Download the CloudFormation template

A CloudFormation template is a JSON or YAML text file that contains the configuration information about the resources you want to create in the stack.
This template also creates a VPC and a bastion host for you along with the Aurora cluster.

To download the template file, open the following link, [Aurora PostgreSQL CloudFormation template](https://github.com/aws-ia/cfn-ps-amazon-aurora-postgresql/blob/main/templates/aurora_postgres-main.template.yaml "https://github.com/aws-ia/cfn-ps-amazon-aurora-postgresql/blob/main/templates/aurora_postgres-main.template.yaml").

In the Github page, click the _Download raw file_ button to save the template YAML file.

### Configure your resources using CloudFormation

###### Note

Before starting this process, make sure you have a Key pair for an EC2 instance in your AWS account. For more information,
see [Amazon EC2 key pairs and Linux instances](../../../AWSEC2/latest/UserGuide/ec2-key-pairs.md "../../../AWSEC2/latest/UserGuide/ec2-key-pairs.md").

When you use the CloudFormation template, you must select the correct parameters to make sure your resources are created properly.
Follow the steps below:

1. Sign in to the AWS Management Console and open the CloudFormation console at [https://console.aws.amazon.com/cloudformation](https://console.aws.amazon.com/cloudformation/ "https://console.aws.amazon.com/cloudformation/").
2. Choose **Create Stack**.
3. In the Specify template section, select **Upload a template file from your computer**, and then choose **Next**.
4. In the **Specify stack details** page, set the following parameters:
   1. Set **Stack name** to **AurPostgreSQLTestStack**.
   2. Under **Parameters**, set **Availability Zones** by selecting two availability zones.
   3. Under **Linux Bastion Host configuration**, for **Key Name**, select a key pair to login to your EC2 instance.
   4. In **Linux Bastion Host configuration** settings,
      set the **Permitted IP range** to your IP address.
      To connect to EC2 instances in your VPC using Secure Shell (SSH), determine your
      public IP address using the service at
      [https://checkip.amazonaws.com](https://checkip.amazonaws.com "https://checkip.amazonaws.com").
      An example of an IP address is 192.0.2.1/32.

   ###### Warning

   If you use `0.0.0.0/0` for SSH access, you make it
   possible for all IP addresses to access your public EC2
   instances using SSH. This approach is acceptable for a short
   time in a test environment, but it's unsafe for production
   environments. In production, authorize only a specific IP
   address or range of addresses to access your EC2 instances using
   SSH. 5. Under **Database General configuration**, set **Database instance class** to **db.t4g.large**. 6. Set **Database name** to `database-test1`. 7. For **Database master username**, enter a name for the master user. 8. Set **Manage DB master user password with Secrets Manager** to `false` for this tutorial. 9. For **Database password**, set a password of your choice. Remember this password for further steps in the tutorial. 10. Set **Multi-AZ deployment** to `false`. 11. Leave all other settings as the default values. Click **Next** to continue.

5. In the **Configure stack options** page, leave all the default options. Click **Next** to continue.
6. In the **Review stack** page, select **Submit** after checking the database and Linux bastion host options.

After the stack creation process completes, view the stacks with names _BastionStack_ and _APGNS_
to note the information you need to connect to the database. For more information, see
[Viewing CloudFormation stack data and resources on the AWS Management Console](../../../AWSCloudFormation/latest/UserGuide/cfn-console-view-stack-data-resources.md "../../../AWSCloudFormation/latest/UserGuide/cfn-console-view-stack-data-resources.md").

## Step 3: Connect to an Aurora PostgreSQL

DB cluster

You can use any standard PostgreSQL client application to connect to the DB cluster. In this example, you
connect to the Aurora PostgreSQL DB cluster using the psql command line client.

###### To connect to the Aurora PostgreSQL DB cluster

1. Find the endpoint (DNS name) and port number of the writer instance for your DB cluster.
   1. Sign in to the AWS Management Console and open the Amazon RDS console at
      [https://console.aws.amazon.com/rds/](https://console.aws.amazon.com/rds/ "https://console.aws.amazon.com/rds/").
   2. In the upper-right corner of the Amazon RDS console, choose the AWS Region for the DB cluster.
   3. In the navigation pane, choose **Databases**.
   4. Choose the Aurora PostgreSQL DB cluster name to display its details.
   5. On the **Connectivity & security** tab, copy the endpoint
      of the writer instance. Also, note the port number. You need both the endpoint and
      the port number to connect to the DB cluster.

   ![Connectivity & security tab showing endpoint name.](images/AuroraPostgreSQLLaunch01.png)

2. Connect to the EC2 instance that you created earlier by following the steps in
   [Connect to your Linux
   instance](../../../AWSEC2/latest/UserGuide/AccessingInstances.md "../../../AWSEC2/latest/UserGuide/AccessingInstances.md") in the _Amazon EC2 User Guide_.

We recommend that you connect to your EC2 instance using SSH. If the SSH client utility is
installed on Windows, Linux, or Mac, you can connect to the instance using the
following command format:

```
ssh -i `location_of_pem_file` ec2-user@`ec2-instance-public-dns-name`
```

For example, assume that `ec2-database-connect-key-pair.pem` is stored
in `/dir1` on Linux, and the public IPv4 DNS for your EC2 instance is
`ec2-12-345-678-90.compute-1.amazonaws.com`. Your SSH command would
look as follows:

```
ssh -i /dir1/ec2-database-connect-key-pair.pem ec2-user@ec2-12-345-678-90.compute-1.amazonaws.com
```

3. Get the latest bug fixes and security updates by updating the software on your EC2 instance.
   To do so, use the following command.

###### Note

The `-y` option installs the updates without asking for confirmation. To
examine updates before installing, omit this option.

```
sudo dnf update -y
```

4. Install the psql command line client from PostgreSQL on Amazon Linux 2023, using the following
   command:

```
sudo dnf install postgresql15
```

5. Connect to the Aurora PostgreSQL DB cluster. For example, enter the following
   command. This action lets you connect to the Aurora PostgreSQL DB cluster using the psql client.

Substitute the endpoint of the writer instance for `endpoint`,
substitute the database name `--dbname` that you want to connect to for `postgres`,
and substitute the master username that you used for `postgres`.
Provide the master password that you used when prompted for a password.

```
psql --host=`endpoint` --port=5432 --dbname=`postgres` --username=`postgres`
```

After you enter the password for the user, you should see output similar to the following.

```
psql (14.3, server 14.6)
SSL connection (protocol: TLSv1.2, cipher: ECDHE-RSA-AES256-GCM-SHA384, bits: 256, compression: off)
Type "help" for help.

postgres=>
```

For more information about connecting to an Aurora PostgreSQL DB cluster, see [Connecting to an Amazon Aurora PostgreSQL
DB cluster](Aurora.md#Aurora.Connecting.AuroraPostgreSQL "Aurora.md#Aurora.Connecting.AuroraPostgreSQL"). If you can't connect to your DB cluster, see
[Can't connect to Amazon RDS DB instance](CHAP_Troubleshooting.md#CHAP_Troubleshooting.Connecting "CHAP_Troubleshooting.md#CHAP_Troubleshooting.Connecting").

For security, it is a best practice to use encrypted connections. Only use an unencrypted PostgreSQL
connection when the client and server are in the same VPC and the network is trusted. For information about
using encrypted connections, see [Securing Aurora PostgreSQL data with
SSL/TLS](AuroraPostgreSQL.md#AuroraPostgreSQL.Security.SSL "AuroraPostgreSQL.md#AuroraPostgreSQL.Security.SSL"). 6. Run SQL commands.

For example, the following SQL command shows the current date and time:

```
SELECT CURRENT_TIMESTAMP;
```

## Step 4: Delete the EC2

instance and DB cluster

After you connect to and explore the sample EC2 instance and DB cluster that you created, delete them so
you're no longer charged for them.

If you used CloudFormation to create resources, skip this step and go to the next step.

###### To delete the EC2 instance

1. Sign in to the AWS Management Console and open the Amazon EC2 console at
   [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/ "https://console.aws.amazon.com/ec2/").
2. In the navigation pane, choose **Instances**.
3. Select the EC2 instance, and choose **Instance state, Terminate instance**.
4. Choose **Terminate** when prompted for confirmation.

For more information about deleting an EC2 instance, see [Terminate your instance](../../../AWSEC2/latest/UserGuide/terminating-instances.md "../../../AWSEC2/latest/UserGuide/terminating-instances.md")
in the _Amazon EC2 User Guide_.

###### To delete a DB cluster

1. Sign in to the AWS Management Console and open the Amazon RDS console at
   [https://console.aws.amazon.com/rds/](https://console.aws.amazon.com/rds/ "https://console.aws.amazon.com/rds/").
2. Choose **Databases** and then choose the
   DB instance associated with the DB cluster.
3. For **Actions**, choose
   **Delete**.
4. Choose **Delete**.

After all of the DB instances associated with a DB cluster are deleted, the DB cluster
is deleted automatically.

## (Optional) Delete the EC2 instance and DB cluster created with CloudFormation

If you used CloudFormation to create resources, delete the CloudFormation stack after
you connect to and explore the sample EC2 instance and DB cluster, so you're no longer charged for them.

###### To delete the CloudFormation resources

1. Open the CloudFormation console.
2. On the **Stacks** page in the CloudFormation console, select the root stack (the stack without the name VPCStack, BastionStack or APGNS).
3. Choose **Delete**.
4. Select **Delete stack** when prompted for confirmation.

For more information about deleting a stack in CloudFormation, see [Deleting a stack on the CloudFormation console](../../../AWSCloudFormation/latest/UserGuide/cfn-console-delete-stack.md "../../../AWSCloudFormation/latest/UserGuide/cfn-console-delete-stack.md")
in the _AWS CloudFormation User Guide_.

## (Optional) Connect your DB cluster to a Lambda function

You can also connect your Aurora PostgreSQL DB cluster to a Lambda serverless compute resource.
Lambda functions allow you to run code without provisioning or managing infrastructure. A Lambda function
also allows you to automatically respond to code execution requests at any scale, from a dozen events
a day to hundreds of per second. For more information, see [Automatically connecting a Lambda function and an Aurora DB cluster](lambda-rds-connect.md "lambda-rds-connect.md").
