# Creating and connecting to an Oracle DB instance

This tutorial creates an EC2 instance and an RDS for Oracle DB instance. The tutorial shows you how to
access the DB instance from the EC2 instance using a standard Oracle client. As a best
practice, this tutorial creates a private DB instance in a virtual private cloud (VPC). In most
cases, other resources in the same VPC, such as EC2 instances, can access the DB instance, but
resources outside of the VPC can't access it.

After you complete the tutorial, there is a public and private subnet in each Availability
Zone in your VPC. In one Availability Zone, the EC2 instance is in the public subnet, and
the DB instance is in the private subnet.

###### Important

There's no charge for creating an AWS account. However, by completing this tutorial, you might incur
costs for the AWS resources you use. You can delete these resources after you complete the tutorial
if they are no longer needed.

The following diagram shows the configuration when the tutorial is complete.

![EC2 instance and Oracle DB instance.](images/getting-started-oracle.png)
This tutorial allows you to create your resources by using one of the following methods:

1. Use the AWS Management Console ‐
   [Step 2: Create an Oracle DB instance](#CHAP_GettingStarted.Creating.Oracle "#CHAP_GettingStarted.Creating.Oracle") and
   [Step 1: Create an EC2 instance](#CHAP_GettingStarted.Creating.Oracle.EC2 "#CHAP_GettingStarted.Creating.Oracle.EC2")
2. Use CloudFormation to create the database instance and EC2 instance ‐
   [(Optional) Create VPC, EC2 instance, and Oracle DB instance using CloudFormation](#CHAP_GettingStarted.CFN.Oracle "#CHAP_GettingStarted.CFN.Oracle")
   The first method uses **Easy create** to create a private Oracle DB instance with the AWS Management Console.
   Here, you specify only the DB engine type, DB instance size, and DB instance identifier.
   **Easy create** uses the default settings for the other configuration options.

When you use **Standard create** instead, you can specify more configuration options when you create a DB instance.
These options include settings for availability, security, backups, and maintenance.
To create a public DB instance, you must use **Standard create**.
For information, see [Creating an Amazon RDS DB instance](USER_CreateDBInstance.md "USER_CreateDBInstance.md").

###### Topics

- [Prerequisites](#CHAP_GettingStarted.Prerequisites.Oracle "#CHAP_GettingStarted.Prerequisites.Oracle")
- [Step 1: Create an EC2 instance](#CHAP_GettingStarted.Creating.Oracle.EC2 "#CHAP_GettingStarted.Creating.Oracle.EC2")
- [Step 2: Create an Oracle DB instance](#CHAP_GettingStarted.Creating.Oracle "#CHAP_GettingStarted.Creating.Oracle")
- [(Optional) Create VPC, EC2 instance, and Oracle DB instance using CloudFormation](#CHAP_GettingStarted.CFN.Oracle "#CHAP_GettingStarted.CFN.Oracle")
- [Step 3: Connect your SQL client to an
  Oracle DB instance](#CHAP_GettingStarted.Connecting.Oracle "#CHAP_GettingStarted.Connecting.Oracle")
- [Step 4: Delete the EC2 instance and
  DB instance](#CHAP_GettingStarted.Deleting.Oracle "#CHAP_GettingStarted.Deleting.Oracle")
- [(Optional) Delete the EC2 instance and DB
  instance created with CloudFormation](#CHAP_GettingStarted.DeletingCFN.Oracle "#CHAP_GettingStarted.DeletingCFN.Oracle")
- [(Optional) Connect your DB instance to a Lambda function](#CHAP_GettingStarted.ComputeConnect.Oracle "#CHAP_GettingStarted.ComputeConnect.Oracle")

## Prerequisites

Before you begin, complete the steps in the following sections:

- [Sign up for an AWS account](CHAP_SettingUp.md#sign-up-for-aws "CHAP_SettingUp.md#sign-up-for-aws")
- [Create a user with administrative access](CHAP_SettingUp.md#create-an-admin "CHAP_SettingUp.md#create-an-admin")

## Step 1: Create an EC2 instance

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

## Step 2: Create an Oracle DB instance

The basic building block of Amazon RDS is the DB instance. This environment is where you run your
Oracle databases.

In this example, you use **Easy create** to create a DB instance running the
Oracle database engine with a db.m5.large DB instance class.

###### To create an Oracle DB instance with Easy create

1. Sign in to the AWS Management Console and open the Amazon RDS console at
   [https://console.aws.amazon.com/rds/](https://console.aws.amazon.com/rds/ "https://console.aws.amazon.com/rds/").
2. In the upper-right corner of the Amazon RDS console, choose the AWS Region in which
   you want to create the DB instance.
3. In the navigation pane, choose **Databases**.
4. Choose **Create database** and make sure that **Easy
   create** is chosen.

![Easy create option.](images/easy-create-option.png) 5. In **Configuration**, choose **Oracle**. 6. For **DB instance size**, choose **Dev/Test**. 7. For **DB instance identifier**, enter
`database-test1`. 8. For **Master username**, enter a name for the master user, or
keep the default name.

The **Create database** page should look similar to the following
image.

![Create database page.](images/easy-create-oracle2.png) 9. To use an automatically generated master password for the DB instance, select
**Auto generate a password**.

To enter your master password, make sure **Auto generate a
password** is cleared, and then enter the same password in
**Master password** and **Confirm
password**. 10. To set up a connection with the EC2 instance you created previously, open
**Set up EC2 connection -
_optional_**.

Select **Connect to an EC2 compute resource**. Choose the EC2
instance you created previously.

![Set up EC2 connection option.](images/EC2_RDS_Setup_Conn-EasyCreate.png) 11. Open **View default settings for Easy create**.

![Easy create default settings.](images/easy-create-view-default-Oracle.png)

You can examine the default settings used with **Easy create**.
The **Editable after database is created** column shows which
options you can change after you create the database.

    * If a setting has **No** in that column, and you want a
     different setting, you can use **Standard create** to
     create the DB instance.
    * If a setting has **Yes** in that column, and you want a
     different setting, you can either use **Standard create**
     to create the DB instance, or modify the DB instance after you create it to change the
     setting.

12. Choose **Create database**.

To view the master username and password for the DB instance, choose **View credential
details**.

You can use the username and password that appears to connect to the DB instance as the
master user.

###### Important

You can't view the master user password again. If you don't record it, you
might have to change it.

If you need to change the master user password after the DB instance is available,
you can modify the DB instance to do so. For more information about modifying a DB instance,
see [Modifying an Amazon RDS DB instance](Overview.DBInstance.md "Overview.DBInstance.md"). 13. In the **Databases** list, choose the name of the new Oracle
DB instance to show its details.

The DB instance has a status of **Creating** until it is ready to
use.

![DB instance details.](images/Oracle-Launch05.png)

When the status changes to **Available**, you can connect to the
DB instance. Depending on the DB instance class and the amount of storage, it can take up to 20
minutes before the new instance is available. While the DB instance is being created, you
can move on to the next step and create an EC2 instance.

## (Optional) Create VPC, EC2 instance, and Oracle DB instance using CloudFormation

Instead of using the console to create your VPC, EC2 instance, and Oracle DB instance, you can use CloudFormation to provision AWS resources by treating infrastructure as code.
To help you organize your AWS resources into smaller and more manageable units, you can use the CloudFormation nested stack functionality.
For more information, see [Creating a stack on the CloudFormation console](../../../AWSCloudFormation/latest/UserGuide/cfn-console-create-stack.md "../../../AWSCloudFormation/latest/UserGuide/cfn-console-create-stack.md") and
[Working with nested stacks](../../../AWSCloudFormation/latest/UserGuide/using-cfn-nested-stacks.md "../../../AWSCloudFormation/latest/UserGuide/using-cfn-nested-stacks.md").

###### Important

CloudFormation is free, but the resources that CloudFormation creates are live. You incur the standard
usage fees for these resources until you terminate them. For more information, see
[RDS for Oracle pricing](https://aws.amazon.com//rds/oracle/pricing "https://aws.amazon.com//rds/oracle/pricing").

To create your resources using the CloudFormation console, complete the following steps:

- Step 1: Download the CloudFormation template
- Step 2: Configure your resources using CloudFormation

### Download the CloudFormation template

A CloudFormation template is a JSON or YAML text file that contains the configuration information about the resources you want to create in the stack.
This template also creates a VPC and a bastion host for you along with the RDS instance.

To download the template file, open the following link, [Oracle CloudFormation template](https://github.com/aws-ia/cfn-ps-amazon-rds/blob/main/templates/rds-oracle-main.template.yaml "https://github.com/aws-ia/cfn-ps-amazon-rds/blob/main/templates/rds-oracle-main.template.yaml").

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
   1. Set **Stack name** to **OracleTestStack**.
   2. Under **Parameters**, set **Availability Zones** by selecting three availability zones.
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
   SSH. 5. Under **Database General configuration**, set **Database instance class** to **db.t3.micro**. 6. Set **Database name** to `database-test1`. 7. For **Database master username**, enter a name for the master user. 8. Set **Manage DB master user password with Secrets Manager** to `false` for this tutorial. 9. For **Database password**, set a password of your choice. Remember this password for further steps in the tutorial. 10. Under **Database Storage configuration**, set **Database storage type** to **gp2**. 11. Under **Database Monitoring configuration**, set **Enable RDS Performance Insights** to false. 12. Leave all other settings as the default values. Click **Next** to continue.

5. In the **Configure stack options** page, leave all the default options. Click **Next** to continue.
6. In the **Review stack** page, select **Submit** after checking the database and Linux bastion host options.

After the stack creation process completes, view the stacks with names _BastionStack_ and _RDSNS_
to note the information you need to connect to the database. For more information, see
[Viewing CloudFormation stack data and resources on the AWS Management Console](../../../AWSCloudFormation/latest/UserGuide/cfn-console-view-stack-data-resources.md "../../../AWSCloudFormation/latest/UserGuide/cfn-console-view-stack-data-resources.md").

## Step 3: Connect your SQL client to an

Oracle DB instance

You can use any standard SQL client application to connect to your DB instance. In this example,
you connect to an Oracle DB instance using the Oracle command-line client.

###### To connect to an Oracle DB instance

1. Find the endpoint (DNS name) and port number for your DB instance.
   1. Sign in to the AWS Management Console and open the Amazon RDS console at
      [https://console.aws.amazon.com/rds/](https://console.aws.amazon.com/rds/ "https://console.aws.amazon.com/rds/").
   2. In the upper-right corner of the Amazon RDS console, choose the AWS Region
      for the DB instance.
   3. In the navigation pane, choose **Databases**.
   4. Choose the Oracle DB instance name to display its details.
   5. On the **Connectivity & security** tab, copy the
      endpoint. Also, note the port number. You need both the endpoint and the
      port number to connect to the DB instance.

   ![Connect to an Oracle DB instance.](images/OracleConnect1.png)

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

3. Get the latest bug fixes and security updates by updating the software on your EC2
   instance. To do so, use the following command.

###### Note

The `-y` option installs the updates without asking for
confirmation. To examine updates before installing, omit this option.

```
sudo dnf update -y
```

4. In a web browser, go to [https://www.oracle.com/database/technologies/instant-client/linux-x86-64-downloads.html](https://www.oracle.com/database/technologies/instant-client/linux-x86-64-downloads.html "https://www.oracle.com/database/technologies/instant-client/linux-x86-64-downloads.html").
5. For the latest database version that appears on the web page, copy the .rpm links (not the
   .zip links) for the Instant Client Basic Package and SQL\*Plus Package. For example,
   the following links are for Oracle Database version 21.9:
   - https://download.oracle.com/otn\_software/linux/instantclient/219000/oracle-instantclient-basic-21.9.0.0.0-1.el8.x86\_64.rpm
   - https://download.oracle.com/otn\_software/linux/instantclient/219000/oracle-instantclient-sqlplus-21.9.0.0.0-1.el8.x86\_64.rpm

6. In your SSH session, run the `wget` command to the download the .rpm files from
   the links that you obtained in the previous step. The following example downloads
   the .rpm files for Oracle Database version 21.9:

```
wget https://download.oracle.com/otn_software/linux/instantclient/219000/oracle-instantclient-basic-21.9.0.0.0-1.el8.x86_64.rpm
wget https://download.oracle.com/otn_software/linux/instantclient/219000/oracle-instantclient-sqlplus-21.9.0.0.0-1.el8.x86_64.rpm
```

7. Install the packages by running the `dnf` command as follows:

```
sudo dnf install oracle-instantclient-*.rpm
```

8. Start SQL\*Plus and connect to the Oracle DB instance. For example, enter the following
   command.

Substitute the DB instance endpoint (DNS name) for
`oracle-db-instance-endpoint` and
substitute the master user name that you used for
`admin`. When you use **Easy
create** for Oracle, the database name is `DATABASE`.
Provide the master password that you used when prompted for a password.

```
sqlplus `admin`@`oracle-db-instance-endpoint`:1521/DATABASE
```

After you enter the password for the user, you should see output similar to the
following.

```
SQL*Plus: Release 21.0.0.0.0 - Production on Wed Mar 1 16:41:28 2023
Version 21.9.0.0.0

Copyright (c) 1982, 2022, Oracle.  All rights reserved.

Enter password:
Last Successful login time: Wed Mar 01 2023 16:30:52 +00:00

Connected to:
Oracle Database 19c Standard Edition 2 Release 19.0.0.0.0 - Production
Version 19.18.0.0.0

SQL>
```

For more information about connecting to an RDS for Oracle DB instance, see [Connecting to your Oracle DB instance](USER_ConnectToOracleInstance.md "USER_ConnectToOracleInstance.md"). If you can't connect to
your DB instance, see [Can't connect to Amazon RDS DB instance](CHAP_Troubleshooting.md#CHAP_Troubleshooting.Connecting "CHAP_Troubleshooting.md#CHAP_Troubleshooting.Connecting").

For security, it is a best practice to use encrypted connections. Only use an unencrypted
Oracle connection when the client and server are in the same VPC and the network is
trusted. For information about using encrypted connections, see [Securing Oracle DB instance connections](Oracle.Concepts.md "Oracle.Concepts.md"). 9. Run SQL commands.

For example, the following SQL command shows the current date:

```
SELECT SYSDATE FROM DUAL;
```

## Step 4: Delete the EC2 instance and

DB instance

After you connect to and explore the sample EC2 instance and DB instance that you created,
delete them so you're no longer charged for them.

If you used CloudFormation to create resources, skip this step and go to the next step.

###### To delete the EC2 instance

1. Sign in to the AWS Management Console and open the Amazon EC2 console at
   [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/ "https://console.aws.amazon.com/ec2/").
2. In the navigation pane, choose **Instances**.
3. Select the EC2 instance, and choose **Instance state, Terminate
   instance**.
4. Choose **Terminate** when prompted for confirmation.

For more information about deleting an EC2 instance, see [Terminate your instance](../../../AWSEC2/latest/UserGuide/terminating-instances.md "../../../AWSEC2/latest/UserGuide/terminating-instances.md")
in the _Amazon EC2 User Guide_.

###### To delete the DB instance with no final DB snapshot

1. Sign in to the AWS Management Console and open the Amazon RDS console at
   [https://console.aws.amazon.com/rds/](https://console.aws.amazon.com/rds/ "https://console.aws.amazon.com/rds/").
2. In the navigation pane, choose **Databases**.
3. Choose the DB instance that you want to delete.
4. For **Actions**, choose **Delete**.
5. Clear **Create final snapshot?** and **Retain automated
   backups**.
6. Complete the acknowledgement and choose **Delete**.

## (Optional) Delete the EC2 instance and DB

instance created with CloudFormation

If you used CloudFormation to create resources, delete the CloudFormation stack after you connect to and explore the sample EC2 instance and DB instance, so you're no longer charged for them.

###### To delete the CloudFormation resources

1. Open the CloudFormation console.
2. On the **Stacks** page in the CloudFormationconsole,
   select the root stack (the stack without the name VPCStack, BastionStack or RDSNS).
3. Choose **Delete**.
4. Select **Delete stack** when prompted for confirmation.

For more information about deleting a stack in CloudFormation, see [Deleting a stack on the CloudFormation console](../../../AWSCloudFormation/latest/UserGuide/cfn-console-delete-stack.md "../../../AWSCloudFormation/latest/UserGuide/cfn-console-delete-stack.md")
in the _AWS CloudFormation User Guide_.

## (Optional) Connect your DB instance to a Lambda function

You can also connect your RDS for Oracle DB instance to a Lambda serverless compute resource.
Lambda functions allow you to run code without provisioning or managing infrastructure. A Lambda function
also allows you to automatically respond to code execution requests at any scale, from a dozen events
a day to hundreds of per second. For more information, see [Automatically connecting a Lambda function and a
DB instance](lambda-rds-connect.md "lambda-rds-connect.md").
