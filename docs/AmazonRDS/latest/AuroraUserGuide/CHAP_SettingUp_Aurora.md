# Setting up your environment for Amazon Aurora

Before you use Amazon Aurora for the first time, complete the following tasks.

###### Topics

- [Sign up for an AWS account](#sign-up-for-aws "#sign-up-for-aws")
- [Determine requirements](#CHAP_SettingUp_Aurora.Requirements "#CHAP_SettingUp_Aurora.Requirements")
- [Provide access to the DB cluster in the VPC by creating a security group](#CHAP_SettingUp_Aurora.SecurityGroup "#CHAP_SettingUp_Aurora.SecurityGroup")
  If you already have an AWS account, know your Aurora requirements, and prefer to use the defaults for IAM
  and VPC security groups, skip ahead to [Getting started with Amazon Aurora](CHAP_GettingStartedAurora.md "CHAP_GettingStartedAurora.md").

## Sign up for an AWS account

To get started with AWS, you need an AWS account. For information about creating an AWS account, see
[Getting started with an AWS account](../../../accounts/latest/reference/getting-started.md "../../../accounts/latest/reference/getting-started.md")
in the _AWS Account Management Reference Guide_.

## Determine requirements

The basic building block of Aurora is the DB cluster. One or more DB instances can belong to a DB cluster.
A DB cluster provides a network address called the _cluster endpoint_. Your applications connect to the cluster endpoint exposed
by the DB cluster whenever they need to access the databases created in that DB
cluster. The information you specify when you create the DB cluster controls
configuration elements such as memory, database engine and version, network
configuration, security, and maintenance periods.

Before you create a DB cluster and a security group, you must know your DB cluster and
network needs. Here are some important things to consider:

- **Resource requirements** – What are the memory and
  processor requirements for your application or service? You will use
  these settings when you determine what DB instance class you will use when you
  create your DB cluster. For specifications about DB instance classes, see [Amazon AuroraDB instance classes](Concepts.DBInstanceClass.md "Concepts.DBInstanceClass.md").
- **VPC, subnet, and security group –** Your DB cluster will be in
  a virtual private cloud (VPC). Security group rules must be configured
  to connect to a DB cluster. The following list describes the rules for each VPC
  option:

  - **Default VPC** — If your AWS account has a
    default VPC in the AWS Region, that VPC is configured to support DB
    clusters. If you specify the default VPC when you create the DB
    cluster:

    - Make sure to create a _VPC security group_ that authorizes
      connections from the application or service to the Aurora DB
      cluster. Use the **Security Group** option on the VPC
      console or the AWS CLI to create VPC security groups. For information, see
      [Step 3: Create a VPC security group](USER_VPC.WorkingWithRDSInstanceinaVPC.md#USER_VPC.CreateVPCSecurityGroup "USER_VPC.WorkingWithRDSInstanceinaVPC.md#USER_VPC.CreateVPCSecurityGroup").
    - You must specify the default DB subnet group. If this is the first DB cluster you
      have created in the AWS Region, Amazon RDS will create the default DB
      subnet group when it creates the DB cluster.

  - **User-defined VPC** — If you want to specify a
    user-defined VPC when you create a DB cluster:

    - Make sure to create a _VPC security group_ that authorizes
      connections from the application or service to the Aurora DB
      cluster. Use the **Security Group** option on the VPC
      console or the AWS CLI to create VPC security groups. For information, see
      [Step 3: Create a VPC security group](USER_VPC.WorkingWithRDSInstanceinaVPC.md#USER_VPC.CreateVPCSecurityGroup "USER_VPC.WorkingWithRDSInstanceinaVPC.md#USER_VPC.CreateVPCSecurityGroup").
    - The VPC must meet certain requirements in order to host DB clusters, such
      as having at least two subnets, each in a separate availability
      zone. For information, see [Amazon VPC and Amazon Aurora](USER_VPC.md "USER_VPC.md").
    - You must specify a DB subnet group that defines which subnets in that VPC can be used by
      the DB cluster. For information, see the DB Subnet Group section in
      [Working with a DB cluster in a VPC](USER_VPC.WorkingWithRDSInstanceinaVPC.md#Overview.RDSVPC.Create "USER_VPC.WorkingWithRDSInstanceinaVPC.md#Overview.RDSVPC.Create").

- **High availability:** Do you need failover support?
  On Aurora, a Multi-AZ deployment creates a primary instance and Aurora Replicas. You can
  configure the primary instance and Aurora Replicas to be in different Availability Zones for
  failover support. We recommend Multi-AZ deployments for production workloads to maintain high availability.
  For development and test purposes, you can use a non-Multi-AZ deployment.
  For more information, see
  [High availability for Amazon Aurora](Concepts.AuroraHighAvailability.md "Concepts.AuroraHighAvailability.md").
- **IAM policies:** Does your AWS account have policies that grant the permissions needed to perform Amazon RDS
  operations? If you are connecting to AWS using IAM credentials, your
  IAM account must have IAM policies that grant the permissions required to
  perform Amazon RDS operations. For more information, see [Identity and access management for Amazon Aurora](UsingWithRDS.IAM.md "UsingWithRDS.IAM.md").
- **Open ports:** What TCP/IP port will your database be listening on? The firewall at some companies might
  block connections to the default port for your database engine. If your company
  firewall blocks the default port, choose another port for the new DB cluster.
  Note that once you create a DB cluster that listens on a port you specify, you
  can change the port by modifying the DB cluster.
- **AWS Region:** What AWS Region do you want your database in? Having the database close in proximity to the
  application or web service could reduce network latency. For more information, see [Regions and Availability Zones](Concepts.RegionsAndAvailabilityZones.md "Concepts.RegionsAndAvailabilityZones.md").

Once you have the information you need to create the security group and the DB cluster,
continue to the next step.

## Provide access to the DB cluster in the VPC by creating a security group

Your DB cluster will be created in a VPC. Security groups provide access to the
DB cluster in the VPC. They act as a firewall for the associated DB cluster,
controlling both inbound and outbound traffic at the cluster level. DB clusters are
created by default with a firewall and a default security group that prevents access to
the DB cluster. You must therefore add rules to a security group that enable you to
connect to your DB cluster. Use the network and configuration information you
determined in the previous step to create rules to allow access to your DB
cluster.

For example, if you have an application that will access a database on your DB cluster in
a VPC, you must add a custom TCP rule that specifies the port range and IP addresses
that application will use to access the database. If you have an application on an
Amazon EC2 instance, you can use the VPC security group you set up for the Amazon EC2
instance.

You can configure connectivity between an Amazon EC2 instance a DB cluster when you create the
DB cluster. For more information, see [Configure automatic network connectivity with an EC2 instance](Aurora.CreateInstance.md#Aurora.CreateInstance.Prerequisites.VPC.Automatic "Aurora.CreateInstance.md#Aurora.CreateInstance.Prerequisites.VPC.Automatic").

###### Tip

You can set up network connectivity between an Amazon EC2 instance and a DB
cluster automatically when you create the DB cluster. For more information, see
[Configure automatic network connectivity with an EC2 instance](Aurora.CreateInstance.md#Aurora.CreateInstance.Prerequisites.VPC.Automatic "Aurora.CreateInstance.md#Aurora.CreateInstance.Prerequisites.VPC.Automatic").

For information about how to connect resources in Amazon Lightsail to your DB clusters, see [Connect Lightsail resources to AWS services using VPC peering](../../../lightsail/latest/userguide/using-lightsail-with-other-aws-services.md "../../../lightsail/latest/userguide/using-lightsail-with-other-aws-services.md").

For more information about creating a VPC for use with Aurora, see
[Tutorial: Create a VPC for use with a DB cluster (IPv4 only)](CHAP_Tutorials.WebServerDB.CreateVPC.md "CHAP_Tutorials.WebServerDB.CreateVPC.md").
For information about common scenarios for accessing a DB instance, see
[Scenarios for accessing a DB cluster in a VPC](USER_VPC.Scenarios.md "USER_VPC.Scenarios.md").

###### To create a VPC security group

1. Sign in to the AWS Management Console and open the Amazon VPC console at [https://console.aws.amazon.com/vpc](https://console.aws.amazon.com/vpc "https://console.aws.amazon.com/vpc").

###### Note

Make sure you are in the VPC console, not the RDS console. 2. In the AWS Management Console, choose the AWS Region where you want to create your
VPC security group and DB cluster. In the list of Amazon VPC resources for that AWS
Region, you should see at least one VPC and several subnets. If you don't,
you don't have a default VPC in that AWS Region. 3. In the navigation pane, choose **Security Groups**. 4. Choose **Create security group**.

The **Create security group** page appears. 5. In **Basic details**, enter the
**Security group name** and **Description**.
For **VPC**, choose the VPC that you
want to create your DB cluster in. 6. In **Inbound rules**, choose **Add rule**.

    1. For **Type**, choose **Custom TCP**.
    2. For **Port range**, enter the port value to use for your DB
     cluster.
    3. For **Source**, choose a security group name or type the IP address
     range (CIDR value) from where you access the DB cluster. If you choose
     **My IP**, this allows access to the DB cluster
     from the IP address detected in your browser.

7. If you need to add more IP addresses or different port ranges, choose **Add rule**
and enter the information for the rule. 8. (Optional) In **Outbound rules**, add rules for outbound traffic.
By default, all outbound traffic is allowed. 9. Choose **Create security group**.

You can use the VPC security group you just created as the security group for your DB
cluster when you create it.

###### Note

If you use a default VPC, a default subnet group spanning all of the VPC's subnets is created
for you. When you create a DB cluster, you can select the default VPC and use **default**
for **DB Subnet Group**.

Once you have completed the setup requirements, you can create a DB cluster using your
requirements and security group by following the instructions in [Creating an Amazon Aurora DB cluster](Aurora.CreateInstance.md "Aurora.CreateInstance.md"). For information about getting started by creating a DB
cluster that uses a specific DB engine, see [Getting started with Amazon Aurora](CHAP_GettingStartedAurora.md "CHAP_GettingStartedAurora.md").
