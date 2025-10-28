For similar capabilities to Amazon Timestream for LiveAnalytics, consider Amazon Timestream for InfluxDB. It offers simplified
data ingestion and single-digit millisecond query response times for real-time analytics. Learn more [here](timestream-for-influxdb.md "timestream-for-influxdb.md").

# Getting started with Timestream for

InfluxDB 3

## Setting up Amazon Timestream for

InfluxDB 3

Before you use Amazon Timestream for InfluxDB for the first time, complete the following tasks:

If you already have an AWS account, know your Timestream for InfluxDB requirements, and
prefer to use the defaults for IAM and Amazon VPC, skip to [Creating and
connecting to a Timestream for InfluxDB instance](#creating-and-connecting-to-a-timestream-for-influxdb-instance "#creating-and-connecting-to-a-timestream-for-influxdb-instance").

### Sign up for an AWS account

If you do not have an AWS account, complete the following steps to create one.

###### To sign up for an AWS account

1. Open [https://portal.aws.amazon.com/billing/signup](https://portal.aws.amazon.com/billing/signup "https://portal.aws.amazon.com/billing/signup").
2. Follow the online instructions.

Part of the sign-up procedure involves receiving a phone call or text message and entering
a verification code on the phone keypad.

When you sign up for an AWS account, an _AWS account root user_ is created. The root user has access to all AWS services
and resources in the account. As a security best practice, assign administrative access to a user, and use only the root user to perform [tasks that require root user access](../../../IAM/latest/UserGuide/id_root-user.md#root-user-tasks "../../../IAM/latest/UserGuide/id_root-user.md#root-user-tasks").

AWS sends you a confirmation email after the sign-up process is
complete. At any time, you can view your current account activity and manage your account by
going to [https://aws.amazon.com/](https://aws.amazon.com/ "https://aws.amazon.com/") and choosing **My
Account**.

### Create a user with administrative access

After you sign up for an AWS account, secure your AWS account root user, enable AWS IAM Identity Center, and create an administrative user so that you
don't use the root user for everyday tasks.

###### Secure your AWS account root user

1. Sign in to the [AWS Management Console](https://console.aws.amazon.com/ "https://console.aws.amazon.com/") as the account owner by choosing **Root user** and entering your AWS account email address. On the next page, enter your password.

For help signing in by using root user, see [Signing in as the root user](../../../signin/latest/userguide/console-sign-in-tutorials.md#introduction-to-root-user-sign-in-tutorial "../../../signin/latest/userguide/console-sign-in-tutorials.md#introduction-to-root-user-sign-in-tutorial") in the _AWS Sign-In User Guide_. 2. Turn on multi-factor authentication (MFA) for your root user.

For instructions, see [Enable a virtual MFA device for your AWS account root user (console)](../../../IAM/latest/UserGuide/enable-virt-mfa-for-root.md "../../../IAM/latest/UserGuide/enable-virt-mfa-for-root.md") in the _IAM User Guide_.

###### Create a user with administrative access

1. Enable IAM Identity Center.

For instructions, see [Enabling
AWS IAM Identity Center](../../../singlesignon/latest/userguide/get-set-up-for-idc.md "../../../singlesignon/latest/userguide/get-set-up-for-idc.md") in the
_AWS IAM Identity Center User Guide_. 2. In IAM Identity Center, grant administrative access to a user.

For a tutorial about using the IAM Identity Center directory as your identity source, see [Configure user access with the default IAM Identity Center directory](../../../singlesignon/latest/userguide/quick-start-default-idc.md "../../../singlesignon/latest/userguide/quick-start-default-idc.md") in the
_AWS IAM Identity Center User Guide_.

###### Sign in as the user with administrative access

- To sign in with your IAM Identity Center user, use the sign-in URL that was sent to your email address when you created the IAM Identity Center user.

For help signing in using an IAM Identity Center user, see [Signing in to the AWS access portal](../../../signin/latest/userguide/iam-id-center-sign-in-tutorial.md "../../../signin/latest/userguide/iam-id-center-sign-in-tutorial.md") in the _AWS Sign-In User Guide_.

###### Assign access to additional users

1. In IAM Identity Center, create a permission set that follows the best practice of applying least-privilege permissions.

For instructions, see [Create a permission set](../../../singlesignon/latest/userguide/get-started-create-a-permission-set.md "../../../singlesignon/latest/userguide/get-started-create-a-permission-set.md") in the _AWS IAM Identity Center User Guide_. 2. Assign users to a group, and then assign single sign-on access to the group.

For instructions, see [Add groups](../../../singlesignon/latest/userguide/addgroups.md "../../../singlesignon/latest/userguide/addgroups.md") in the _AWS IAM Identity Center User Guide_.

### Grant programmatic access

Users need programmatic access if they want to interact with AWS outside of the
AWS Management Console. The way to grant programmatic access depends on the type of user that's accessing
AWS:

- For workforce identity (Users managed in AWS IAM Identity Center): Use temporary credentials
- For IAM users: Use temporary credentials or long-term credentials (not
  recommended)

### Determine requirements

Before you create a DB instance and a security group, you must know your DB instance
and network needs. Here are some important things to consider:

- **Resource requirements** – What are the memory and
  processor requirements for your application or service?
- **VPC and security group** – Your DB instance will
  most likely be in a virtual private cloud (VPC). To connect to your DB instance, you
  need to set up security group rules.
- **High availability** – Do you need failover
  support?
- **IAM policies** – Does your AWS account have
  policies that grant the permissions needed to perform Amazon Timestream for InfluxDB
  operations?
- **Open ports** – What TCP/IP port does your database
  listen on? The default for Timestream for InfluxDB is 8086.
- **AWS Region** – What AWS Region do you want
  your database in?
- **DB disk subsystem** – What are your storage
  requirements?

### Provide access to your DB instance in your VPC by creating a security group

VPC security groups provide access to DB instances in a VPC. They act as a firewall for
the associated DB instance, controlling both inbound and outbound traffic at the DB instance
level. DB instances are created by default with a firewall and a default security group that
protect the DB instance.

To create a VPC security group:

1. In the AWS Management Console, choose **VPC**.
2. In the navigation pane, choose **Security Groups**.
3. Choose **Create security group**.
4. Enter a name, description, and select your VPC.
5. Add inbound rules for Custom TCP with appropriate source settings.
6. Create the security group.

## Creating and

connecting to a Timestream for InfluxDB instance

Connecting to a Amazon Timestream for InfluxDB DB instance uses token authentication.

The connection information includes endpoint, port, username, password, and a valid
access token. You can find this information using the AWS Management Console or AWS CLI.

You can create access tokens using:

- [The
  InfluxDB CLI](https://docs.influxdata.com/influxdb3/enterprise/reference/cli/influxdb3/ "https://docs.influxdata.com/influxdb3/enterprise/reference/cli/influxdb3/")
- [The InfluxDB 3
  Explorer](https://docs.influxdata.com/influxdb3/explorer/ "https://docs.influxdata.com/influxdb3/explorer/")
- [The InfluxDB
  API](https://docs.influxdata.com/influxdb3/enterprise/api/v3/ "https://docs.influxdata.com/influxdb3/enterprise/api/v3/")

The following procedure creates both an Amazon Elastic Compute Cloud instance and a Timestream for InfluxDB DB
cluster, and shows you how to write data to the DB instance from the Amazon EC2 instance using the
Telegraf client.

### Step 1: Create an Amazon EC2

instance

1. Sign in to the AWS Management Console and open the Amazon EC2 console.
2. Choose the AWS Region where you want to create the Amazon EC2 instance.
3. Choose Amazon EC2 Dashboard, then Launch instance.
4. Configure your Amazon EC2 instance with appropriate settings .

### Step 2: Create an InfluxDB 3

instance

1. Sign in to the AWS Management Console and open the Timestream for InfluxDB console.
2. In the navigation pane, choose **InfluxDB Databases**.
3. Choose **Create InfluxDB 3 database**.
4. After selecting InfluxDB 3, choose between the Core and Enterprise editions. For
   this tutorial, where you'll be ingesting data from a single Amazon EC2 instance and running
   test queries, the Core edition is sufficient for your needs.
5. Configure your DB instance with appropriate settings. For specific engine
   configurations, you can select from an existing parameter group or create a new one. If
   no custom configuration is needed, simply proceed and a default parameter group will be
   automatically created for your instance.
6. Configure your instance size and network settings. Pay special attention to the
   network configuration. If you choose a private instance, ensure it's accessible from
   your Amazon EC2 instance's VPC by selecting the appropriate VPC, subnets, and security groups
   that allow connectivity between your Amazon EC2 instance and the InfluxDB instance.
7. Choose **Create InfluxDB database**.
8. Wait for your DB instance to become available.

### Step 3: Access the InfluxDB Explorer

To access your InfluxDB instance through the InfluxDB Explorer:

1. Download the InfluxDB Explorer from [https://docs.influxdata.com/influxdb3/explorer/](https://docs.influxdata.com/influxdb3/explorer/ "https://docs.influxdata.com/influxdb3/explorer/")
2. For private DB instances, run the Explorer from within the same VPC (using an Amazon EC2
   instance or bastion host).
3. For publicly accessible DB instances, you can run the Explorer from any location
   with internet access.
4. Configure the Explorer with your cluster endpoint and credentials.

### Step 4: Send Telegraf

data to your InfluxDB instance

1. Connect to your InfluxDB instance using the InfluxDB Explorer and generate an API
   token.
2. Connect to your Amazon EC2 instance and install Telegraf.
3. Configure Telegraf to send data to your InfluxDB instance.
4. Enable and start the Telegraf service.

### Step 5:

Delete the Amazon EC2 instance and the InfluxDB DB instance

After you explore the Telegraf-generated data, delete both your Amazon EC2 and your InfluxDB
DB instances to avoid being charged for them.
