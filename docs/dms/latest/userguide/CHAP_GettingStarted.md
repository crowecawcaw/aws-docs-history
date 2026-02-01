# Complete prerequisites to set up AWS Database Migration Service

In this section, you can learn the prerequisite tasks for AWS DMS, such as setting up
your source and target databases. As part of these tasks, you also set up a virtual private
cloud (VPC) based on the Amazon VPC service to contain your resources. In addition, you set up an
Amazon EC2 instance that you use to populate your source database and verify replication on your
target database.

###### Note

Populating the source database takes up to 45 minutes.

For this tutorial, you create a MariaDB database as your source, and a PostgreSQL database
as your target. This scenario uses commonly used, low-cost database engines to demonstrate
replication. Using different database engines demonstrates AWS DMS features for migrating data
between heterogeneous platforms.

The resources in this tutorial use the US West (Oregon) Region. If you want to use a
different AWS Region, specify your chosen Region instead wherever US West (Oregon)
appears.

###### Note

For the sake of simplicity, the databases that you create for this tutorial don't use
encryption or other advanced security features. You must use security features to keep
your production databases secure. For more information, see [Security in Amazon
RDS](../../../AmazonRDS/latest/UserGuide/UsingWithRDS.md "../../../AmazonRDS/latest/UserGuide/UsingWithRDS.md").

For prerequisite steps, see the following topics.

###### Topics

- [Create a VPC](#CHAP_GettingStarted.Prerequisites.VPC "#CHAP_GettingStarted.Prerequisites.VPC")
- [Create Amazon RDS parameter groups](#CHAP_GettingStarted.Prerequisites.params "#CHAP_GettingStarted.Prerequisites.params")
- [Create your source Amazon RDS
  database](#CHAP_GettingStarted.Prerequisites.sdatabase "#CHAP_GettingStarted.Prerequisites.sdatabase")
- [Create your target Amazon RDS database](#CHAP_GettingStarted.Prerequisites.tdatabase "#CHAP_GettingStarted.Prerequisites.tdatabase")
- [Create an Amazon EC2 client](#CHAP_GettingStarted.Prerequisites.client "#CHAP_GettingStarted.Prerequisites.client")
- [Populate your source database](#CHAP_GettingStarted.Prerequisites.Populate "#CHAP_GettingStarted.Prerequisites.Populate")

## Create a VPC

In this section, you create a VPC to contain your AWS resources. Using a VPC is a
best practice when using AWS resources, so that your databases, Amazon EC2 instances,
security groups, and so on, are logically organized and secure.

Using a VPC for your tutorial resources also ensures that you delete all of the
resources you use when you are done with the tutorial. You must delete all of the
resources that a VPC contains before you can delete the VPC.

###### To create a VPC for use with AWS DMS

1.  Sign in to the AWS Management Console and open the Amazon VPC console at
    [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/ "https://console.aws.amazon.com/vpc/").
2.  On the navigation pane, choose **VPC Dashboard**, and then choose
    **Create VPC**.
3.  On the **Create VPC** page, enter the following
    options:

        * **Resources to create**: **VPC and more**
        * **Name tag auto generation**: Choose **Auto-generate**,
         and enter `DMSVPC`.
        * **IPv4 block**: `10.0.1.0/24`
        * **IPv6 CIDR block**: **No IPv6 CIDR block**
        * **Tenancy**: **Default**
        * **Number of availability zones**: 2
        * **Number of public subnets**: 2
        * **Number of private subnets**: 2
        * **NAT gateways ($)**: **None**
        * **VPC endpoints**: **None**

    Choose **Create VPC**.

4.  On the navigation pane, choose **Your VPCs**. Note the VPC ID for
    **DMSVPC**.
5.  On the navigation pane, choose **Security Groups**.
6.  Choose the group named **default** that has a **VPC ID**
    that matches the ID that you noted for **DMSVPC**.
7.  Choose the **Inbound rules** tab, and choose **Edit inbound
    rules**.
8.  Choose **Add rule**. Add a rule of type **MySQL/Aurora** and
    choose **Anywhere-IPv4** for **Source**.
9.  Choose **Add rule** again. Add a rule of type **PostgreSQL**
    and choose **Anywhere-IPv4** for **Source**.
10. Choose **Save rules**.

## Create Amazon RDS parameter groups

To specify settings for your source and target databases for AWS DMS, use Amazon RDS
parameter groups. To allow initial and ongoing replication between your databases, make
sure to configure the following:

- Your source database's binary log, so that AWS DMS can determine what incremental updates it
  needs to replicate.
- Your target database's replication role, so that AWS DMS ignores foreign key constraints during
  the initial data transfer. With this setting, AWS DMS can migrate data out of
  order.

###### To create parameter groups for use with AWS DMS

1. Open the Amazon RDS console at
   [https://console.aws.amazon.com/rds/](https://console.aws.amazon.com/rds/ "https://console.aws.amazon.com/rds/").
2. On the navigation pane, choose **Parameter groups**.
3. On the **Parameter groups** page, choose **Create parameter group**.
4. On the **Create parameter group** page, enter the following settings:
   - **Parameter group family**: **mariadb10.6**
   - **Group name**: `dms-mariadb-parameters`
   - **Description**: `Group for specifying binary log settings for replication`Choose **Create**.

5. On the **Parameter groups** page, choose
   **dms-mariadb-parameters**, and on the
   **dms-mariadb-parameters** page, choose **Edit**.
6. Set the following parameters to the following values:
   - **binlog_checksum**: **NONE**
   - **binlog_format**: **ROW**Choose **Save changes**.

7. On the **Parameter groups** page, choose **Create parameter group** again.
8. On the **Create parameter group** page, enter the following settings:
   - **Parameter group family**: **postgres16**
   - **Group name**: `dms-postgresql-parameters`
   - **Description**: `Group for specifying role setting for replication`Choose **Create**.

9. On the **Parameter groups** page, choose **dms-postgresql-parameters**.
10. On the **dms-postgresql-parameters** page, choose **Edit**,
    and set **session_replication_role
    parameter** to **replica**. Note that the **session_replication_role** parameter is not on the first page of parameters. Use the pagination controls or the search
    field to find the parameter.
11. Choose **Save changes**.

## Create your source Amazon RDS

database

Use the following procedure to create your source Amazon RDS database.

###### To create your source Amazon RDS for MariaDB database

1. Open the Amazon RDS console at
   [https://console.aws.amazon.com/rds/](https://console.aws.amazon.com/rds/ "https://console.aws.amazon.com/rds/").
2. On the **Dashboard** page, choose **Create Database** in the
   **Database** section. Don't choose **Create
   Database** in the **Try the new Amazon RDS Multi-AZ deployment option for MySQL and PostgreSQL** section at the
   top of the page.
3. On the **Create database** page, set the following options:
   - **Choose a database creation method**: Choose **Standard Create**.
   - **Engine options**: For **Engine type**, choose
     **MariaDB**. For **Version**, leave **MariaDB 10.6.14** selected.
   - **Templates**: Choose **Dev/Test**.
   - **Settings**:
     - **DB instance identifier**: Enter `dms-mariadb`.
     - In the **Credentials settings** section, enter the following:
       - **Master username**: Leave as `admin`.
       - Leave **Manage master credentials in AWS Secrets Manager** unchecked.
       - **Auto generate a password**: Leave unselected.
       - **Master password**: Enter `changeit`.
       - **Confirm password**: Enter `changeit` again.

   - **Instance configuration**:
     - **DB instance class**: Leave **Standard classes** chosen.
     - For **DB instance class**, choose **db.m5.large**.

   - **Storage**:
     - Clear the **Enable storage autoscaling** box.
     - Leave the rest of the settings as they are.

   - **Availability and Durability**: Leave
     **Do not create a standby instance** selected.
   - **Connectivity**:
     - **Compute resource** Leave **Don't connect to an EC2 compute resource**
     - **Network type**: Leave **IPv4** selected.
     - **Virtual private cloud**: **DMSVPC-vpc**
     - **Public access**: **Yes**. You must enable public access to use the
       AWS Schema Conversion Tool.
     - **Availability zone**: **us-west-2a**
     - Leave the rest of the settings as they are.

   - **Database authentication**: Leave **Password authentication** selected.
   - Under **Monitoring**, clear the **Turn on Performance Insights** box.
     Expand the **Additional configuration** section, and clear the **Enable Enhanced monitoring**
     box.
   - Expand **Additional configuration**:
     - Under **Database options**, enter `dms_sample` for **Initial database name**.
     - Under **DB parameter group**, choose **dms-mariadb-parameters**.
     - For **Option group**, leave **default:mariadb-10-6** selected.
     - Under **Backup**, do the following:
       - Leave **Enable automatic backups**
         selected. Your source database must have automatic backups
         enabled to support ongoing replication.
       - For **Backup retention period**, choose **1 day**.
       - For **Backup window**, leave **No preference** selected.
       - Clear the **Copy tags to snapshots** box.
       - Leave the **Enable replication in another AWS region** unchecked.

     - Under **Encryption**, clear the **Enable encryption**
       box.
     - Leave the **Log exports** section as it is.
     - Under **Maintenance**, clear the **Enable auto minor version
       upgrade** box, and leave the **Maintenance window** setting
       as **No preference**.
     - Leave **Enable deletion protection** unchecked.

4. Choose **Create database**.

## Create your target Amazon RDS database

Repeat the previous procedure to create your target Amazon RDS database, with the following
changes.

###### To create your target RDS for PostgreSQL database

1. Repeat steps 1 and 2 from the previous procedure.
2. On the **Create database** page, set the same options, except
   for these:
   1. For **Engine options**, choose **PostgreSQL**.
   2. For **Version**, choose an available **PostgreSQL 16**
      version
   3. For **DB instance identifier**, enter `dms-postgresql`.
   4. For **Master username**, leave `postgres` selected.
   5. For **DB parameter group**, choose **dms-postgresql-parameters**.
   6. Clear **Enable automatic backups**.

3. Choose **Create database**.

## Create an Amazon EC2 client

In this section, you create an Amazon EC2 client. You use this client to populate your
source database with data to replicate. You also use this client to verify replication
by running queries on the target database.

Using an Amazon EC2 client to access your databases provides the following advantages over
accessing your databases over the internet:

- You can restrict access to your databases to clients that are in the same VPC.
- We have confirmed that the tools you use in this tutorial work, and are easy to install, on
  Amazon Linux 2023, which we recommend for this tutorial.
- Data operations between components in a VPC generally perform better than those over the
  internet.

###### To create and configure an Amazon EC2 client to populate your source database

1.  Open the Amazon EC2 console at
    [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/ "https://console.aws.amazon.com/ec2/").
2.  On the **Dashboard**, choose **Launch instance**.
3.  On the **Launch an Instance** page, enter the following values:
    1.  In the **Name and tags** section, enter `DMSClient` for **Name**.
    2.  In the **Application and OS Images (Amazon Machine Image)** section, leave the settings as they are.
    3.  In the **Instance Type** section, choose **t2.xlarge**.
    4.  In the **Key pair (login)** section, choose **Create a new key pair**.
    5.  On the **Create key pair** page, enter the following:

            * **Key pair name**: `DMSKeyPair`
            * **Key pair type**: Leave as **RSA**.
            * **Private key file format**: Choose
             **pem** for OpenSSH on MacOS or Linux, or **ppk** for PuTTY on Windows.

        Save the key file when prompted.

    ###### Note

    You can also use an existing Amazon EC2 key pair rather than creating a new one. 6. In the **Network Settings** section, choose **Edit**. Choose the following settings:

        * **VPC - *required***: Choose the VPC with the ID that you recorded for the
         **DMSVPC-vpc** VPC.
        * **Subnet**: Choose the first public subnet.
        * **Auto-assign public IP**: Choose **Enable**.

    Leave the rest of the settings as they are, and choose **Launch instance**.

## Populate your source database

In this section, you find endpoints for your source and target databases for later
use and use the following tools to populate the source database:

- Git, to download the script that populates your source database.
- MariaDB client, to run this script.

### Get endpoints

Find and note the endpoints of your RDS for MariaDB and RDS for PostgreSQL DB instances for
later use.

###### To find your DB instance endpoints

1. Sign in to the AWS Management Console and open the Amazon RDS console at
   [https://console.aws.amazon.com/rds/](https://console.aws.amazon.com/rds/ "https://console.aws.amazon.com/rds/").
2. On the navigation pane, choose **Databases**.
3. Choose the **dms-mariadb** database, and note the **Endpoint**
   value for the database.
4. Repeat the previous steps for the **dms-postgresql** database.

### Populate your source

database

Next, connect to your client instance, install the necessary software,
download AWS sample database scripts from Git, and run the scripts to populate
your source database.

###### To populate your source database

1. Connect to the client instance using the host name and public key that you saved in previous
   steps.

For more information on connecting to an Amazon EC2 instance, see [Accessing
Instances](../../../AWSEC2/latest/UserGuide/AccessingInstances.md "../../../AWSEC2/latest/UserGuide/AccessingInstances.md") in the _Amazon EC2 User Guide_.

###### Note

If you are using PuTTY, enable TCP keepalives on the **Connection** settings
page so that your connection doesn't time out from inactivity. 2. Install Git, MariaDB, and PostgreSQL. Confirm installation as needed.

```
$ sudo yum install git
$ sudo dnf install mariadb105
$ sudo dnf install postgresql15
```

3. Run the following command to download the database creation scripts from GitHub.

```
git clone https://github.com/aws-samples/aws-database-migration-samples.git
```

4. Change to the `aws-database-migration-samples/mysql/sampledb/v1/` directory.
5. Run the following command. Provide the endpoint for your source RDS instance that you noted
   previously, for example
   `dms-mariadb.cdv5fbeyiy4e.us-east-1.rds.amazonaws.com`.

```
mysql -h dms-mariadb.`abcdefghij01`.us-east-1.rds.amazonaws.com -P 3306 -u admin -p dms_sample < ~/aws-database-migration-samples/mysql/sampledb/v1/install-rds.sql
```

6. Let the database creation script run. The script takes up to 45 minutes to create the schema and populate
   the data. You can safely ignore errors and warnings that the script displays.
