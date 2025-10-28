# Creating and connecting to a Microsoft SQL Server DB instance

This tutorial creates an EC2 instance and an RDS for Microsoft SQL Server DB instance. The tutorial shows you how to access
the DB instance from the EC2 instance using the Microsoft SQL Server Management Studio client. As a best practice, this tutorial creates
a private DB instance in a virtual private cloud (VPC). In most cases, other resources in the same VPC, such
as EC2 instances, can access the DB instance, but resources outside of the VPC can't access it.

After you complete the tutorial, there is a public and private subnet in each Availability
Zone in your VPC. In one Availability Zone, the EC2 instance is in the public subnet, and
the DB instance is in the private subnet.

###### Important

There's no charge for creating an AWS account. However, by completing this tutorial, you might incur
costs for the AWS resources you use. You can delete these resources after you complete the tutorial
if they are no longer needed.

The following diagram shows the configuration when the tutorial is complete.

![EC2 instance and Microsoft SQL Server DB instance.](images/getting-started-sqlserver.png)
This tutorial allows you to create your resources by using one of the following methods:

1. Use the AWS Management Console ‐
   [Create a SQL Server DB
   instance](#CHAP_GettingStarted.Creating.SQLServer "#CHAP_GettingStarted.Creating.SQLServer") and
   [Create an EC2
   instance](#CHAP_GettingStarted.Creating.SQLServer.EC2 "#CHAP_GettingStarted.Creating.SQLServer.EC2")
2. Use AWS CloudFormation to create the database instance and EC2 instance ‐
   [(Optional) Create VPC, EC2 instance, and SQL Server instance using AWS CloudFormation](#CHAP_GettingStarted.CFN.SQLServer "#CHAP_GettingStarted.CFN.SQLServer")
   The first method uses **Easy create** to create a private SQL Server DB instance with the AWS Management Console.
   Here, you specify only the DB engine type, DB instance size, and DB instance identifier.
   **Easy create** uses the default settings for the other configuration options.

When you use **Standard create** instead, you can specify more configuration options when you create a DB instance.
These options include settings for availability, security, backups, and maintenance.
To create a public DB instance, you must use **Standard create**. For information, see [Creating an Amazon RDS DB instance](USER_CreateDBInstance.md "USER_CreateDBInstance.md").

###### Topics

- [Prerequisites](#CHAP_GettingStarted.Prerequisites.SQLServer "#CHAP_GettingStarted.Prerequisites.SQLServer")
- [Create an EC2
  instance](#CHAP_GettingStarted.Creating.SQLServer.EC2 "#CHAP_GettingStarted.Creating.SQLServer.EC2")
- [Create a SQL Server DB
  instance](#CHAP_GettingStarted.Creating.SQLServer "#CHAP_GettingStarted.Creating.SQLServer")
- [(Optional) Create VPC, EC2 instance, and SQL Server instance using AWS CloudFormation](#CHAP_GettingStarted.CFN.SQLServer "#CHAP_GettingStarted.CFN.SQLServer")
- [Connect to your SQL Server
  DB instance](#CHAP_GettingStarted.Connecting.SQLServer "#CHAP_GettingStarted.Connecting.SQLServer")
- [Explore your sample SQL Server
  DB instance](#CHAP_GettingStarted.SQLServer.Exploring "#CHAP_GettingStarted.SQLServer.Exploring")
- [Delete the EC2
  instance and DB instance](#CHAP_GettingStarted.Deleting.SQLServer "#CHAP_GettingStarted.Deleting.SQLServer")
- [(Optional) Delete the EC2 instance and DB
  instance created with CloudFormation](#CHAP_GettingStarted.DeletingCFN.SQLServer "#CHAP_GettingStarted.DeletingCFN.SQLServer")
- [(Optional) Connect your DB instance to a Lambda function](#CHAP_GettingStarted.ComputeConnect.SQLServer "#CHAP_GettingStarted.ComputeConnect.SQLServer")

## Prerequisites

Before you begin, complete the steps in the following sections:

- [Sign up for an AWS account](CHAP_SettingUp.md#sign-up-for-aws "CHAP_SettingUp.md#sign-up-for-aws")
- [Create a user with administrative access](CHAP_SettingUp.md#create-an-admin "CHAP_SettingUp.md#create-an-admin")

## Create an EC2

instance

Create an Amazon EC2 instance that you will use to connect to your database.

###### To create an EC2 instance

1. Sign in to the AWS Management Console and open the Amazon EC2 console at
   [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/ "https://console.aws.amazon.com/ec2/").
2. In the upper-right corner of the AWS Management Console, choose the AWS Region you used for the database
   previously.
3. Choose **EC2 Dashboard**, and then choose **Launch
   instance**, as shown in the following image.

![EC2 Dashboard.](images/Tutorial_WebServer_11.png)

The **Launch an instance** page opens. 4. Choose the following settings on the **Launch an instance**
page.

    1. Under **Name and tags**, for **Name**, enter
     `ec2-database-connect`.
    2. Under **Application and OS Images (Amazon Machine
     Image)**, choose **Windows**, and then choose the
     **Microsoft Windows Server 2022 Base**. Keep the default selections for the
     other choices.



    ![Choose an Amazon Machine Image.](images/tutorial_ec2_sqlserver_create1.png)
    3. Under **Instance type**, choose **t2.micro**.
    4. Under **Key pair (login)**, choose a **Key pair name** to use an existing key
     pair. To create a new key pair for the Amazon EC2 instance, choose **Create new key pair**
     and then use the **Create key pair** window to create it.


    For more information about creating a new key pair, see [Create a key pair](../../../AWSEC2/latest/WindowsGuide/ec2-key-pairs.md "../../../AWSEC2/latest/WindowsGuide/ec2-key-pairs.md")
     in the *Amazon EC2 User Guide for Windows Instances*.
    5. For **Firewall (security groups)** in **Network
     settings**, choose **Allow RDP traffic from**
     to connect to the EC2 instance.


    You can choose **My IP** if the displayed IP address is
     correct for RDP connections. Otherwise, you can determine the IP address to
     use to connect to EC2 instances in your VPC using RDP. To determine your
     public IP address, in a different browser window or tab, you can use the
     service at [https://checkip.amazonaws.com](https://checkip.amazonaws.com/ "https://checkip.amazonaws.com/"). An example of an IP address is
     192.0.2.1/32.


     In many cases, you might connect through an internet service provider
     (ISP) or from behind your firewall without a static IP address. If so, make
     sure to determine the range of IP addresses used by client computers.


    ###### Warning

    If you use `0.0.0.0/0` for RDP access, you make it possible
     for all IP addresses to access your public EC2 instances using RDP. This
     approach is acceptable for a short time in a test environment, but it's
     unsafe for production environments. In production, authorize only a
     specific IP address or range of addresses to access your EC2 instances
     using RDP.


    The following image shows an example of the **Network
     settings** section.



    ![Network settings for an EC2 instance.](images/EC2_RDS_Connect_NtwkSettingsRDSMS.png)
    6. Keep the default values for the remaining sections.
    7. Review a summary of your EC2 instance configuration in the **Summary** panel, and when you're ready,
     choose **Launch instance**.

5. On the **Launch Status** page, note the identifier for your new
   EC2 instance, for example: `i-1234567890abcdef0`.

![EC2 instance identifier on Launch Status page.](images/getting-started-ec2-id.png) 6. Choose the EC2 instance identifier to open the list of EC2 instances. 7. Wait until the **Instance state** for your EC2 instance has a status
of **Running** before continuing.

## Create a SQL Server DB

instance

The basic building block of Amazon RDS is the DB instance. This environment is where you
run your SQL Server databases.

In this example, you use **Easy create** to create a DB instance
running the SQL Server database engine with a db.t2.micro DB instance class.

###### To create a Microsoft SQL Server DB instance with Easy create

1. Sign in to the AWS Management Console and open the Amazon RDS console at
   [https://console.aws.amazon.com/rds/](https://console.aws.amazon.com/rds/ "https://console.aws.amazon.com/rds/").
2. In the upper-right corner of the Amazon RDS console, choose the AWS Region in
   which you want to create the DB instance.
3. In the navigation pane, choose **Databases**.
4. Choose **Create database** and make sure that **Easy
   create** is chosen.

![Easy create option.](images/easy-create-option.png) 5. In **Configuration**, choose **Microsoft SQL
Server**. 6. For **Edition**, choose **SQL Server Express
Edition**. 7. For **DB instance size**, choose **Free
tier**. **Free tier** appears for free
plan accounts. **Sandbox** appears for paid plan
accounts. 8. For **DB instance identifier**, enter
`database-test1`.

The **Create database** page should look similar to the
following image. For free plan accounts, **Free tier** appears. For paid plan accounts, **Sandbox** appears.

![Engine options](images/easy-create-sqlserver.png) 9. For **Master username**, enter a name for the master user, or
keep the default name. 10. To set up a connection with the EC2 instance you created previously, open
**Set up EC2 connection -
_optional_**.

Select **Connect to an EC2 compute resource**. Choose the EC2
instance you created previously.

![Set up EC2 connection option.](images/EC2_RDS_Setup_Conn-EasyCreate.png) 11. To use an automatically generated master password for the DB instance, select
the **Auto generate a password** box.

To enter your master password, clear the **Auto generate a
password** box, and then enter the same password in
**Master password** and **Confirm
password**. 12. Open **View default settings for Easy create**.

![Easy create default settings.](images/easy-create-sqlserver-confirm.png)

You can examine the default settings used with **Easy
create**. The **Editable after database is
created** column shows which options you can change after you
create the database.

    * If a setting has **No** in that column, and you want
     a different setting, you can use **Standard create** to
     create the DB instance.
    * If a setting has **Yes** in that column, and you want
     a different setting, you can either use **Standard
     create** to create the DB instance, or modify the DB
     instance after you create it to change the setting.

13. Choose **Create database**.

To view the master username and password for the DB instance, choose
**View credential details**.

You can use the username and password that appears to connect to the DB
instance as the master user.

###### Important

You can't view the master user password again. If you don't record it, you
might have to change it.

If you need to change the master user password after the DB instance is
available, you can modify the DB instance to do so. For more information
about modifying a DB instance, see [Modifying an Amazon RDS DB instance](Overview.DBInstance.md "Overview.DBInstance.md"). 14. In the **Databases** list, choose the name of the new SQL
Server DB instance to show its details.

The DB instance has a status of **Creating** until it is
ready to use.

![Screen capture of the DB instance details.](images/easy-create-sqlserver-launch.png)

When the status changes to **Available**, you can connect to
the DB instance. Depending on the DB instance class and the amount of storage,
it can take up to 20 minutes before the new instance is available.

## (Optional) Create VPC, EC2 instance, and SQL Server instance using AWS CloudFormation

Instead of using the console to create your VPC, EC2 instance, and SQL Server instance, you can use AWS CloudFormation to provision AWS resources by treating infrastructure as code.
To help you organize your AWS resources into smaller and more manageable units, you can use the AWS CloudFormation nested stack functionality.
For more information, see [Creating a stack on the AWS CloudFormation console](../../../AWSCloudFormation/latest/UserGuide/cfn-console-create-stack.md "../../../AWSCloudFormation/latest/UserGuide/cfn-console-create-stack.md") and
[Working with nested stacks](../../../AWSCloudFormation/latest/UserGuide/using-cfn-nested-stacks.md "../../../AWSCloudFormation/latest/UserGuide/using-cfn-nested-stacks.md")..

###### Important

AWS CloudFormation is free, but the resources that CloudFormation creates are live. You incur the standard
usage fees for these resources until you terminate them. For more information, see
[RDS for SQL Server
pricing](https://aws.amazon.com/rds/sqlserver/pricing "https://aws.amazon.com/rds/sqlserver/pricing").

To create your resources using the AWS CloudFormation console, complete the following steps:

- Download the CloudFormation template
- Configure your resources using CloudFormation

### Download the CloudFormation template

A CloudFormation template is a JSON or YAML text file that contains the configuration information about the resources you want to create in the stack.
This template also creates a VPC and a bastion host for you along with the RDS instance.

To download the template file, open the following link, [SQL Server CloudFormation template](https://github.com/aws-ia/cfn-ps-amazon-rds/blob/main/templates/rds-sqlserver-main.template.yaml "https://github.com/aws-ia/cfn-ps-amazon-rds/blob/main/templates/rds-sqlserver-main.template.yaml").

In the Github page, click the _Download raw file_ button to save the template YAML file.

### Configure your resources using CloudFormation

###### Note

Before starting this process, make sure you have a Key pair for an EC2 instance in your AWS account. For more information,
see [Amazon EC2 key pairs and Linux instances](../../../AWSEC2/latest/UserGuide/ec2-key-pairs.md "../../../AWSEC2/latest/UserGuide/ec2-key-pairs.md").

When you use the AWS CloudFormation template, you must select the correct parameters to make sure your resources are created properly.
Follow the steps below:

1. Sign in to the AWS Management Console and open the AWS CloudFormation console at [https://console.aws.amazon.com/cloudformation](https://console.aws.amazon.com/cloudformation/ "https://console.aws.amazon.com/cloudformation/").
2. Choose **Create Stack**.
3. In the Specify template section, select **Upload a template file from your computer**, and then choose **Next**.
4. In the **Specify stack details** page, set the following parameters:
   1. Set **Stack name** to **SQLServerTestStack**.
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
   SSH. 5. Under **Database General configuration**, set **Database instance class** to **db.t3.micro**. 6. Set **Database name** to `database-test1`. 7. For **Database master username**, enter a name for the master user. 8. Set **Manage DB master user password with Secrets Manager**
   to `false` for this tutorial. 9. For **Database password**, set a password of your choice. Remember this password for further steps in the tutorial. 10. Under **Database Storage configuration**, set **Database storage
   type** to **gp2**. 11. Under **Database Monitoring configuration**, set **Enable RDS Performance Insights** to false. 12. Leave all other settings as the default values. Click **Next** to continue.

5. In the **Configure stack options** page, leave all the default options. Click **Next** to continue.
6. In the **Review stack** page, select **Submit** after checking the database and Linux bastion host options.

After the stack creation process completes, view the stacks with names _BastionStack_ and _RDSNS_
to note the information you need to connect to the database. For more information, see
[Viewing AWS CloudFormation stack data and resources on the AWS Management Console](../../../AWSCloudFormation/latest/UserGuide/cfn-console-view-stack-data-resources.md "../../../AWSCloudFormation/latest/UserGuide/cfn-console-view-stack-data-resources.md").

## Connect to your SQL Server

DB instance

In the following procedure, you connect to your DB instance by using Microsoft SQL
Server Management Studio (SSMS).

###### To connect to an RDS for SQL Server DB instance using SSMS

1. Find the endpoint (DNS name) and port number for your DB instance.
   1. Sign in to the AWS Management Console and open the Amazon RDS console at
      [https://console.aws.amazon.com/rds/](https://console.aws.amazon.com/rds/ "https://console.aws.amazon.com/rds/").
   2. In the upper-right corner of the Amazon RDS console, choose the AWS Region for the DB instance.
   3. In the navigation pane, choose **Databases**.
   4. Choose the SQL Server DB instance name to display its details.
   5. On the **Connectivity** tab, copy the endpoint.
      Also, note the port number. You need both the endpoint and the port number to connect to the DB instance.

   ![Connect to a Microsoft SQL Server DB instance.](images/SQLServerConnect2.png)

2. Connect to the EC2 instance that you created earlier by following the steps in [Connect to your Microsoft Windows instance](../../../AWSEC2/latest/WindowsGuide/EC2_GetStarted.md#ec2-connect-to-instance-windows "../../../AWSEC2/latest/WindowsGuide/EC2_GetStarted.md#ec2-connect-to-instance-windows")
   in the _Amazon EC2 User Guide for Windows Instances_.
3. Install the SQL Server Management Studio (SSMS) client from Microsoft.

To download a standalone version of SSMS to your EC2 instance, see [Download SQL Server Management
Studio (SSMS)](https://docs.microsoft.com/en-us/sql/ssms/download-sql-server-management-studio-ssms "https://docs.microsoft.com/en-us/sql/ssms/download-sql-server-management-studio-ssms") in the Microsoft documentation.

    1. Use the Start menu to open Internet Explorer.
    2. Use Internet Explorer to download and install a standalone version of
     SSMS. If you are prompted that the site isn't trusted, add the site to
     the list of trusted sites.

4. Start SQL Server Management Studio (SSMS).

The **Connect to Server** dialog box appears. 5. Provide the following information for your sample DB instance:

    1. For **Server type**, choose **Database Engine**.
    2. For **Server name**, enter the DNS name, followed by a comma and the
     port number (the default port is 1433). For example, your server name
     should look as follows:



    ```
    database-test1.`0123456789012`.`us-west-2`.rds.amazonaws.com,1433
    ```
    3. For **Authentication**, choose **SQL Server Authentication**.
    4. For **Login**, enter the username that you chose to use for your
     sample DB instance. This is also known as the master username.
    5. For **Password**, enter the password that you chose earlier for your
     sample DB instance. This is also known as the master user password.

6. Choose **Connect**.

After a few moments, SSMS connects to your DB instance. For security, it is a best practice to use encrypted connections. Only use an unencrypted SQL Server connection when the client and server are in the same VPC and the network is trusted.
For information about using encrypted connections, see
[Using SSL with a Microsoft SQL Server DB instance](SQLServer.Concepts.General.SSL.md "SQLServer.Concepts.General.SSL.md")

For more information about connecting to a Microsoft SQL Server DB instance, see
[Connecting to your Microsoft SQL Server
DB instance](USER_ConnectToMicrosoftSQLServerInstance.md "USER_ConnectToMicrosoftSQLServerInstance.md").

For information about connection issues, see [Can't connect to Amazon RDS DB instance](CHAP_Troubleshooting.md#CHAP_Troubleshooting.Connecting "CHAP_Troubleshooting.md#CHAP_Troubleshooting.Connecting").

## Explore your sample SQL Server

DB instance

You can explore your sample DB instance by using Microsoft SQL Server Management Studio (SSMS).

###### To explore a DB instance using SSMS

1. Your SQL Server DB instance comes with SQL Server's standard built-in system databases (master, model, msdb, and tempdb).
   To explore the system databases, do the following:
   1. In SSMS, on the **View** menu, choose **Object Explorer**.
   2. Expand your DB instance, expand **Databases**, and then expand **System Databases** as shown.

   ![Object Explorer displaying the system databases.](images/SQL-SSMS-SystemDBs.png)Your SQL Server DB instance also comes with a database named `rdsadmin`. Amazon RDS
   uses this database to store the objects that it uses to manage your database. The
   `rdsadmin` database also includes stored procedures that you can run to
   perform advanced tasks.

2. Start creating your own databases and running queries against your DB instance and
   databases as usual. To run a test query against your sample DB instance, do the
   following:
   1. In SSMS, on the **File** menu, point to
      **New** and then choose **Query with
      Current Connection**.
   2. Enter the following SQL query:

   ```
   select @@VERSION
   ```

   3. Run the query.
      SSMS returns the SQL Server version of your Amazon RDS DB instance.

   ![SQL Query Window.](images/SQL-Connect-Query.png)

## Delete the EC2

instance and DB instance

After you connect to and explore the sample EC2 instance and DB instance that you created, delete them so
you're no longer charged for them.

If you used AWS CloudFormation to create resources, skip this step and go to the next step.

###### To delete the EC2 instance

1. Sign in to the AWS Management Console and open the Amazon EC2 console at
   [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/ "https://console.aws.amazon.com/ec2/").
2. In the navigation pane, choose **Instances**.
3. Select the EC2 instance, and choose **Instance state, Terminate instance**.
4. Choose **Terminate** when prompted for confirmation.

For more information about deleting an EC2 instance, see [Terminate your instance](../../../AWSEC2/latest/WindowsGuide/terminating-instances.md "../../../AWSEC2/latest/WindowsGuide/terminating-instances.md")
in the _User Guide for Windows Instances_.

###### To delete the DB instance with no final DB snapshot

1. Sign in to the AWS Management Console and open the Amazon RDS console at
   [https://console.aws.amazon.com/rds/](https://console.aws.amazon.com/rds/ "https://console.aws.amazon.com/rds/").
2. In the navigation pane, choose **Databases**.
3. Choose the DB instance that you want to delete.
4. For **Actions**, choose
   **Delete**.
5. Clear **Create final snapshot?** and **Retain automated backups**.
6. Complete the acknowledgement and choose **Delete**.

## (Optional) Delete the EC2 instance and DB

instance created with CloudFormation

If you used AWS CloudFormation to create resources, delete the CloudFormation
stack after you connect to and explore the sample EC2 instance
and DB instance, so you're no longer charged for them.

###### To delete the CloudFormation resources

1. Open the AWS CloudFormation console.
2. On the **Stacks** page in the CloudFormationconsole,
   select the root stack (the stack without the name VPCStack, BastionStack or RDSNS).
3. Choose **Delete**.
4. Select **Delete stack** when prompted for confirmation.

For more information about deleting a stack in CloudFormation, see [Deleting a stack on the AWS CloudFormation console](../../../AWSCloudFormation/latest/UserGuide/cfn-console-delete-stack.md "../../../AWSCloudFormation/latest/UserGuide/cfn-console-delete-stack.md")
in the _AWS CloudFormation User Guide_.

## (Optional) Connect your DB instance to a Lambda function

You can also connect your RDS for SQL Server DB instance to a Lambda serverless compute resource.
Lambda functions allow you to run code without provisioning or managing infrastructure. A Lambda function
also allows you to automatically respond to code execution requests at any scale, from a dozen events
a day to hundreds of per second. For more information, see [Automatically connecting a Lambda function and a
DB instance](lambda-rds-connect.md "lambda-rds-connect.md").
