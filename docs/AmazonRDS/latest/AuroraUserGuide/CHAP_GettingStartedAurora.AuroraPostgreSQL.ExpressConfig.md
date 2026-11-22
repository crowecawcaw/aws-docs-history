

# Create with express configuration

You can create and connect to an Aurora PostgreSQL serverless database in seconds using express configuration which provides a streamlined database creation experience with preconfigured defaults to help you get started easily and quickly.

In two clicks, you can have an Aurora cluster with a serverless instance ready to use in seconds. You can also use the AWS Command Line Interface (AWS CLI) or [AWS SDKs](https://docs.aws.amazon.com/sdkref/latest/guide/overview.html) with the parameter `--with-express-configuration` to create both a cluster and an instance within the cluster with single API call which makes it ready for running queries in seconds. You have the flexibility to modify most of the settings during, and most other settings after the database creation. For more information about these settings, see [Express configuration settings](#CHAP_GettingStartedAurora.AuroraPostgreSQL.ExpressConfig.Settings). Once created, you have access to most of the features and benefits of Aurora such as the ability to add readers for high availability and scalability, and automatic failover capabilities. Some options, such as specifying a customer managed encryption key or selecting specific engine versions, are only available when using the [Create with full configuration](CHAP_GettingStartedAurora.AuroraPostgreSQL.FullConfig.md) option. This creation experience for Aurora PostgreSQL is also available with the [AWS Free Tier](https://aws.amazon.com/rds/free/). 

By default, a cluster created with express configuration isn't associated with a virtual private cloud (VPC). You connect to it through the internet access gateway. If you want the cluster to be in your VPC, you can create it in a VPC, or move it into a VPC later without changing its endpoint. For more information, see [Creating a cluster with express configuration in a VPC](#CHAP_GettingStartedAurora.AuroraPostgreSQL.ExpressConfig.CreateInVPC) and [Moving a cluster with express configuration into a VPC](#CHAP_GettingStartedAurora.AuroraPostgreSQL.ExpressConfig.MoveIntoVPC).

**Topics**
+ [Prerequisites](#CHAP_GettingStartedAurora.AuroraPostgreSQL.ExpressConfig.Prerequisites)
+ [Supported Regions](#CHAP_GettingStartedAurora.AuroraPostgreSQL.ExpressConfig.SupportedRegions)
+ [Internet access gateway](#CHAP_GettingStartedAurora.AuroraPostgreSQL.ExpressConfig.InternetAccessGateway)
+ [Creating a DB cluster with express configuration](#CHAP_GettingStartedAurora.AuroraPostgreSQL.ExpressConfig.CreatingDBCluster)
+ [Express configuration settings](#CHAP_GettingStartedAurora.AuroraPostgreSQL.ExpressConfig.Settings)
+ [Connecting to clusters with express configuration](#CHAP_GettingStartedAurora.AuroraPostgreSQL.ExpressConfig.Connecting)
+ [Moving a cluster with express configuration into a VPC](#CHAP_GettingStartedAurora.AuroraPostgreSQL.ExpressConfig.MoveIntoVPC)
+ [Restoring a cluster created through express configuration](#CHAP_GettingStartedAurora.AuroraPostgreSQL.ExpressConfig.Restoring)
+ [Limitations](#CHAP_GettingStartedAurora.AuroraPostgreSQL.ExpressConfig.Limitations)

## Prerequisites
<a name="CHAP_GettingStartedAurora.AuroraPostgreSQL.ExpressConfig.Prerequisites"></a>

Before you can create an Aurora PostgreSQL DB cluster with express configuration, you must at minimum have the following permissions:
+ `ec2:DescribeAvailabilityZones`
+ `iam:CreateServiceLinkedRole`
+ `rds:CreateDBCluster`
+ `rds:CreateDBInstance`
+ `rds:EnableInternetAccessGateway`

To create the cluster in a VPC, you also need the following permission:
+ `rds:EnableVpcNetworking`

For the permissions needed to move an existing cluster into a VPC, see [Moving a cluster with express configuration into a VPC](#CHAP_GettingStartedAurora.AuroraPostgreSQL.ExpressConfig.MoveIntoVPC).

## Supported Regions
<a name="CHAP_GettingStartedAurora.AuroraPostgreSQL.ExpressConfig.SupportedRegions"></a>

You can create an Aurora PostgreSQL serverless cluster with express configuration in all AWS Regions except the AWS GovCloud (US), Middle East (UAE), and Middle East (Bahrain) Regions.

## Internet access gateway
<a name="CHAP_GettingStartedAurora.AuroraPostgreSQL.ExpressConfig.InternetAccessGateway"></a>

Aurora also provides an internet access gateway enabled by default to connect securely with the clusters created through express configuration. The internet access gateway is supported for Aurora PostgreSQL DB clusters that don't use VPC networking. It supports the PostgreSQL wire protocol and enables you to connect through the internet from a wide range of tools and development platforms that might be running outside of your AWS infrastructure - no VPN or AWS Direct Connect required. The gateway is distributed across multiple Availability Zones, offering the same level of high availability as your Aurora cluster. It is a managed component of Aurora, so there are no software updates or patches that need to be applied by you.

The internet access gateway is integrated with AWS Identity and Access Management (IAM), allowing you to enforce identity-based permissions for authorized access and safeguard your data with ephemeral token-based access. When using the gateway, the required setup for the database administrator user, including granting the rds\_iam role, is automatically managed for you.

A DB cluster uses either VPC networking or the internet access gateway. It can't use both at the same time, and it can't have both turned off. You can switch a DB cluster between the two by modifying the cluster. The cluster endpoint stays the same. For more information, see [Moving a cluster with express configuration into a VPC](#CHAP_GettingStartedAurora.AuroraPostgreSQL.ExpressConfig.MoveIntoVPC) and [Moving a DB cluster out of a VPC](USER_VPC.WorkingWithRDSInstanceinaVPC.md#USER_VPC.WorkingWithRDSInstanceinaVPC.MoveOutOfVPC).

## Creating a DB cluster with express configuration
<a name="CHAP_GettingStartedAurora.AuroraPostgreSQL.ExpressConfig.CreatingDBCluster"></a>

You can create an Aurora PostgreSQL DB cluster with express configuration using the AWS Management Console, the AWS CLI, or the RDS API.

### Console
<a name="CHAP_GettingStartedAurora.AuroraPostgreSQL.ExpressConfig.CreatingDBCluster.Console"></a>

To create with express configuration using the console:

**To create with express configuration using the console**

1. Sign in to the AWS Management Console and open the Amazon RDS console at [https://console.aws.amazon.com/rds/](https://console.aws.amazon.com/rds/).

1. In the AWS Management Console, choose the AWS Region in which you want to create the DB cluster.

1. In the navigation pane, choose Databases.

1. On the Welcome to Aurora and RDS page, locate the Create with express configuration in seconds section, and choose Create.  
![The Welcome to Aurora and RDS page showing the Create with express configuration section.](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/images/aurora-express-config-image1.png)

1. Review pre-configured settings in the Create with express configuration dialog.  
![The Create with express configuration dialog showing pre-configured settings.](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/images/aurora-express-config-image2.png)

1. (Optional) Modify the DB cluster identifier or the capacity range as per your need.

1. (Optional) To create the cluster in a VPC, in the **Configuration details** table, for **Network access type**, choose **VPC**, and then choose the **Virtual private cloud (VPC)**, **DB subnet group**, and **VPC security group**. Before you choose, see [Creating a cluster with express configuration in a VPC](#CHAP_GettingStartedAurora.AuroraPostgreSQL.ExpressConfig.CreateInVPC).

1. Choose Create database.

1. Your Aurora PostgreSQL Serverless database should be ready in seconds. If you created the cluster in a VPC, it takes longer to become available, but it's still faster than creating a cluster with full configuration. A success banner confirms the creation, and the database status changes to "Available".  
![The database status showing Available after successful creation.](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/images/aurora-express-config-image3.png)

### CLI
<a name="CHAP_GettingStartedAurora.AuroraPostgreSQL.ExpressConfig.CreatingDBCluster.CLI"></a>

You can use the AWS CLI to create an Aurora PostgreSQL clusters with express configuration.

For Linux or MacOS.

```
aws rds create-db-cluster --db-cluster-identifier sample-express-cluster \
    --engine aurora-postgresql \
    --with-express-configuration
```

For Windows:

```
aws rds create-db-cluster --db-cluster-identifier sample-express-cluster ^
    --engine aurora-postgresql ^
    --with-express-configuration
```

The express configuration parameter takes care of creating a database cluster, an Aurora serverless instance, setting up the internet access gateway, and IAM authentication for the admin database user (default = postgres).

To create the cluster in a VPC, see [Creating a cluster with express configuration in a VPC](#CHAP_GettingStartedAurora.AuroraPostgreSQL.ExpressConfig.CreateInVPC).

### API
<a name="CHAP_GettingStartedAurora.AuroraPostgreSQL.ExpressConfig.CreatingDBCluster.API"></a>

You can use the relevant AWS SDK and call the CreateDBCluster operation to create a DB cluster and database instance with the express configuration.

### Creating a cluster with express configuration in a VPC
<a name="CHAP_GettingStartedAurora.AuroraPostgreSQL.ExpressConfig.CreateInVPC"></a>

By default, express configuration creates a DB cluster without VPC networking, and you connect to it through the internet access gateway. To create the cluster in your VPC instead, turn on VPC networking and turn off the internet access gateway in the same request. You can choose the DB subnet group (and so the VPC), the VPC security groups, and the network type. All other express configuration defaults are the same as for a cluster without VPC networking.

Aurora creates the cluster with the internet access gateway turned on, and then moves the cluster into your VPC right away. Because of this extra step, the cluster takes longer to become available than a cluster without VPC networking. It's still faster than creating a cluster with full configuration.

**Important**  
Until the move into the VPC is complete, any IAM principal that has `rds-db:connect` permission for the cluster can connect to it through the internet access gateway. Before you create the cluster, make sure that only the principals that need it have this permission.

#### Before you begin
<a name="CHAP_GettingStartedAurora.AuroraPostgreSQL.ExpressConfig.CreateInVPC.BeforeYouBegin"></a>
+ **Choose a DB subnet group that has a subnet in every Availability Zone in the AWS Region.** Aurora chooses the Availability Zone for the cluster's DB instance before it moves the cluster into the VPC. If the DB subnet group doesn't have a subnet in that Availability Zone, the cluster isn't moved into the VPC. For more information, see [Working with DB subnet groups](USER_VPC.WorkingWithRDSInstanceinaVPC.md#USER_VPC.Subnets).
+ **If you don't specify a DB subnet group,** Aurora uses the default DB subnet group. It exists only if your account has a default VPC in the AWS Region. Otherwise, you must specify a DB subnet group.
+ **If you don't specify VPC security groups,** Aurora uses the default security group of the VPC. If the DB subnet group is in a shared VPC, you must specify the security groups.
+ **If you don't specify a network type,** the cluster uses IPv4.
+ **Check your IAM permissions.** See [Prerequisites](#CHAP_GettingStartedAurora.AuroraPostgreSQL.ExpressConfig.Prerequisites).

#### AWS CLI
<a name="CHAP_GettingStartedAurora.AuroraPostgreSQL.ExpressConfig.CreateInVPC.CLI"></a>

Specify `--with-express-configuration`, `--enable-vpc-networking`, and `--no-enable-internet-access-gateway`. If you leave out either networking option, the request fails with `InvalidParameterCombination`.

For Linux, macOS, or Unix:

```
aws rds create-db-cluster \
    --db-cluster-identifier sample-express-cluster \
    --engine aurora-postgresql \
    --with-express-configuration \
    --enable-vpc-networking \
    --no-enable-internet-access-gateway \
    --db-subnet-group-name mysubnetgroup \
    --vpc-security-group-ids sg-0abcd1234efgh5678 \
    --network-type IPV4
```

For Windows:

```
aws rds create-db-cluster ^
    --db-cluster-identifier sample-express-cluster ^
    --engine aurora-postgresql ^
    --with-express-configuration ^
    --enable-vpc-networking ^
    --no-enable-internet-access-gateway ^
    --db-subnet-group-name mysubnetgroup ^
    --vpc-security-group-ids sg-0abcd1234efgh5678 ^
    --network-type IPV4
```

The output shows the cluster before it moves into the VPC: `VPCNetworkingEnabled` is `false` and `InternetAccessGatewayEnabled` is `true`. `PendingModifiedValues` shows the move into the VPC.

#### RDS API
<a name="CHAP_GettingStartedAurora.AuroraPostgreSQL.ExpressConfig.CreateInVPC.API"></a>

Call the CreateDBCluster operation. Set `WithExpressConfiguration` to `true`, `EnableVPCNetworking` to `true`, and `EnableInternetAccessGateway` to `false`. Optionally, specify `DBSubnetGroupName`, `VpcSecurityGroupIds`, and `NetworkType`.

#### Verifying that the cluster is in the VPC
<a name="CHAP_GettingStartedAurora.AuroraPostgreSQL.ExpressConfig.CreateInVPC.Verifying"></a>

When the cluster status is `available`, run [describe-db-clusters](https://docs.aws.amazon.com/cli/latest/reference/rds/describe-db-clusters.html) and check that `VPCNetworkingEnabled` is `true` and `InternetAccessGatewayEnabled` is `false`. Don't treat the cluster as private until you see these values.

#### If the cluster isn't moved into the VPC
<a name="CHAP_GettingStartedAurora.AuroraPostgreSQL.ExpressConfig.CreateInVPC.NotMoved"></a>

If Aurora can't move the new cluster into the VPC, the create request still succeeds. Aurora keeps the cluster available on the internet access gateway and publishes an RDS event. Check the event for the cause, for example a DB subnet group that doesn't cover the cluster's Availability Zone. Then move the cluster into the VPC. For more information, see [Moving a cluster with express configuration into a VPC](#CHAP_GettingStartedAurora.AuroraPostgreSQL.ExpressConfig.MoveIntoVPC). If the cluster status doesn't return to `available`, contact AWS Support.

## Express configuration settings
<a name="CHAP_GettingStartedAurora.AuroraPostgreSQL.ExpressConfig.Settings"></a>

The following table describes the settings for express configuration and indicates whether they can be modified after creation.


| Setting | Setting description | Default Setting and Limitations | 
| --- | --- | --- | 
| Auto minor version upgrade | This setting enables your Aurora DB cluster to receive preferred minor version upgrades to the DB engine automatically when they become available. For more information about engine updates for Aurora PostgreSQL, see [Database engine updates for Amazon Aurora PostgreSQL](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/AuroraPostgreSQL.Updates.html). | Enabled by default. Can be changed after the create operation completes. | 
| AWS KMS key | [Clusters with express configuration are encrypted with AWS/RDS Service owned keys.](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/Overview.Encryption.html) | Enabled with AWS/RDS service owned key. Cannot be modified. | 
| Certificate authority | Clusters with express configuration are enabled with internet access gateway, which uses the AWS root certificates. For more information, see [ACM root CAs](https://docs.aws.amazon.com/acm/latest/userguide/acm-concepts.html) | Not applicable for connecting through internet access gateway | 
| Cluster storage configuration | The storage type for the DB cluster: Aurora Standard or Aurora I/O-Optimized. For more information, see [Storage Configurations for Amazon Aurora DB clusters](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/Aurora.Overview.StorageReliability.html). | Aurora Standard by default. Can be changed after the create operation completes. | 
| Copy tags to snapshots | Choose this option to copy any DB instance tags to a DB snapshot when you create a snapshot. For more information, see [Tagging Amazon Aurora and Amazon RDS resources](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/USER_Tagging.html). | Disabled by default. Can be changed during creation or after the creation. | 
| Database authentication | Clusters with express configuration and internet access gateway only support IAM authentication. For more information, see [IAM database authentication](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/UsingWithRDS.IAMDBAuth.html). | Enabled with IAM Authentication by default. Cannot be modified. | 
| Database port | Clusters with express configuration and internet access gateway only support the default PostgreSQL port | Default value = 5432. Cannot be modified. | 
| DB cluster identifier | Enter a name for your DB cluster that is unique for your account in the AWS Region that you chose. This identifier is used in the cluster endpoint address for your DB cluster. For information on the cluster endpoint, see [Amazon Aurora endpoint connections](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/Aurora.Overview.Endpoints.html). The DB cluster identifier has the following constraints: It must contain from 1 to 63 alphanumeric characters or hyphens. Its first character must be a letter. It cannot end with a hyphen or contain two consecutive hyphens. It must be unique for all DB clusters per AWS account, per AWS Region. | Required parameter. Can be changed during creation or after the creation. | 
| DB cluster parameter group | Clusters with express configuration use the Aurora default DB cluster parameter group. | Default parameter group. Can be changed after the create operation completes. | 
| DB instance class | Clusters with express configuration start with an Aurora serverless instance. | Aurora serverless instance. Can be changed after the create operation completes. | 
| DB subnet group | By default, clusters with express configuration are not created within your VPC, and access is through the Aurora internet access gateway. If you create the cluster in a VPC, the DB subnet group determines the VPC and subnets for the cluster. | No VPC associated by default. Can be set during creation, or after creation when you move the cluster into a VPC. If you don't specify one, Aurora uses the default DB subnet group, if your account has a default VPC in the AWS Region. | 
| Enable deletion protection | Choose Enable deletion protection to prevent your DB cluster from being deleted. If you create a production DB cluster with the console, deletion protection is enabled by default. | Disabled by default. Can be changed during or after the creation completes. | 
| Enable encryption | [Clusters with express configuration are encrypted with AWS/RDS Service owned keys.](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/Overview.Encryption.html) | Enabled with AWS/RDS service owned key. Cannot be modified. | 
| Enable Enhanced Monitoring | Choose Enable enhanced monitoring to enable gathering metrics in real time for the operating system that your DB cluster runs on. For more information, see [Monitoring OS metrics with Enhanced Monitoring](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/USER_Monitoring.OS.html). | Disabled by default. Can be changed after the create operation completes. | 
| Enable the RDS Data API | Choose Enable the RDS Data API to enable RDS Data API (Data API). Data API provides a secure HTTP endpoint for running SQL statements without managing connections. For more information, see [Using the Amazon RDS Data API](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/data-api.html). | Disabled by default. Can be changed after the create operation completes. | 
| Engine type | Clusters with express configuration clusters are only supported with Aurora PostgreSQL | Required paramater. Supported value: "aurora-postgresql". Cannot be modified. | 
| Engine version | Clusters with express configuration use the default major and minor version. See [Aurora versions](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/Aurora.VersionPolicy.Versioning.html), for details on default versions. | Default major and minor version. Engine version can be upgraded later. | 
| Failover priority | Choose a failover priority for the instance. If you don't choose a value, the default is tier-1. This priority determines the order in which Aurora Replicas are promoted when recovering from a primary instance failure. For more information, see [Fault tolerance for an Aurora DB cluster](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/Concepts.AuroraHighAvailability.html). | Default value = 1. Can be changed after the create operation completes. | 
| Initial database name | The name for your default database. If you don't provide a name for an Aurora PostgreSQL DB cluster, Amazon RDS creates a database named postgres. For Aurora PostgreSQL, the default database name has these constraints: It must contain 1–63 alphanumeric characters. It must begin with a letter. Subsequent characters can be letters, underscores, or digits (0–9). It can't be a word reserved by the database engine. To create additional databases, connect to the DB cluster and use the SQL command CREATE DATABASE. For more information about connecting to the DB cluster, see Connecting to an Amazon Aurora DB cluster with internet access gateway. | Default value = postgres. Can be changed during or after the creation completes. | 
| Log exports | In the Log exports section, choose the logs that you want to start publishing to Amazon CloudWatch Logs. For more information about publishing Aurora MySQL logs to CloudWatch Logs, see Publishing Aurora MySQL logs to Amazon CloudWatch Logs. For more information about publishing Aurora PostgreSQL logs to CloudWatch Logs, see Publishing Aurora PostgreSQL logs to Amazon CloudWatch Logs. | Disabled by default. Can be changed during or after the creation. | 
| Maintenance window | Choose Select window and specify the weekly time range during which system maintenance can occur. Or choose No preference for Amazon RDS to assign a period randomly. | Default maintenance window varies by [Region](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/USER_UpgradeDBInstance.Maintenance.html). Can be changed during or after the creation. | 
| Manage master credentials in AWS Secrets Manager | Clusters with express configuration and internet access gateway support IAM authentication only. This setting does not apply. | N/A | 
| Master password | Clusters with express configuration and internet access gateway support IAM authentication only. This setting does not apply. | N/A | 
| Master user authentication type | Clusters with express configuration automatically sets authentication type to IAM authentication. | Supported Value = iam-db-auth. Cannot be modified. | 
| Master username | Enter a name to use as the master username to log on to your DB cluster. For Aurora PostgreSQL, it must contain 1–63 alphanumeric characters. The first character must be a letter. The name can't be a word reserved by the database engine. You can't change the master username after the DB cluster is created. | Default value = postgres. Can be changed during or after the creation. | 
| Multi-AZ deployment | Clusters with express configuration have their Availability Zones automatically chosen for you. This includes the first DB instance of a cluster that you create in a VPC. DB instances that you add after the cluster is in a VPC are placed in the Availability Zones of the DB subnet group. You can add read replicas after the database is created. | Availability zones are automatically chosen. The writer and reader instances are placed in different availability zones. | 
| Network type | The IP addressing protocols supported by a cluster in a VPC. Clusters without VPC networking support IPv4 only. | Not applicable without VPC networking. In a VPC, IPv4 by default. Can be changed to Dual-stack mode after the cluster is in a VPC. | 
| Public access | Clusters with express configuration are created with the internet access gateway, which offers secure internet access with built-in integration with AWS Identity and Access Management and AWS Shield. | Not applicable when the internet access gateway is turned on. For a cluster in a VPC, you can make DB instances publicly accessible after creation by modifying them. For more information, see [Hiding a DB cluster in a VPC from the internet](USER_VPC.WorkingWithRDSInstanceinaVPC.md#USER_VPC.Hiding). | 
| RDS Extended Support | Select Enable RDS Extended Support to allow supported major engine versions to continue running past the Aurora end of standard support date. When you create a DB cluster, Amazon Aurora defaults to RDS Extended Support. To prevent the creation of a new DB cluster after the Aurora end of standard support date and to avoid charges for RDS Extended Support, disable this setting. Your existing DB clusters won't incur charges until the RDS Extended Support pricing start date. For more information, see [Amazon RDS Extended Support with Amazon Aurora](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/extended-support.html). | Not supported | 
| RDS Proxy | RDS Proxy is not supported with clusters that are not associated with a VPC. For more information, see [Amazon RDS Proxy for Aurora](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/rds-proxy.html). | Not supported | 
| Retention period | Choose the length of time, from 1 to 35 days, that Aurora retains backup copies of the database. Backup copies can be used for point-in-time restores (PITR) of your database down to the second. | Default value = 1. Can be changed after the create operation completes. | 
| Backup window | A 30-minute window selected at random from an 8-hour block of time to take automatic backup of your database. | Uses the default parameter group. Can be changed later using parameter groups. | 
| Turn on DevOps Guru | DevOps Guru for RDS provides detailed analysis of performance anomalies, Performance Insights must be turned on. For more information, see [Setting up DevOps Guru for RDS](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/devops-guru-for-rds.html). | Disabled by default. Can be changed after the create operation completes. | 
| Turn on Performance Insights | Amazon RDS Performance Insights provides monitoring information for your database. For more information, see [Monitoring DB load with Performance Insights on Amazon Aurora](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/USER_PerfInsights.html). | Disabled by default. Can be changed after the create operation completes. | 
| Virtual Private Cloud (VPC) | Clusters with express configuration are not associated with a VPC by default. | No VPC by default. Can be set during creation, or after creation by moving the cluster into a VPC. | 
| VPC security group (firewall) | Clusters with express configuration without VPC networking don't use VPC security groups. Access is controlled by IAM database authentication. | Not applicable without VPC networking. In a VPC, can be set during or after creation. The VPC's default security group is used if you don't specify one (not allowed for a shared VPC). | 
| Write forwarding | Enables you to forward writes sent on the reader endpoint to the writer node for processing. Enables achieving read-after-write consistency. For more information see, [Local write forwarding in Aurora PostgreSQL](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/aurora-postgresql-write-forwarding.html). | Disabled by default. Can be changed after the create operation completes. | 

## Connecting to clusters with express configuration
<a name="CHAP_GettingStartedAurora.AuroraPostgreSQL.ExpressConfig.Connecting"></a>

Clusters created with express configuration are automatically set up with an internet access gateway, which provides public access to your database with IAM authentication. Ensure that the IAM identity you use to connect to the database has permissions to rds-db:connect to generate the authentication token needed to access the database. To learn more, see [IAM database authentication](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/UsingWithRDS.IAMDBAuth.html).

The connection options in this section apply to clusters that use the internet access gateway. If your cluster is in a VPC, connect to it the same way as to any Aurora DB cluster in a VPC: from a client that can reach the VPC and is allowed by the cluster's VPC security groups. For more information, see [Scenarios for accessing a DB cluster in a VPC](USER_VPC.Scenarios.md) and [Connecting to an Amazon Aurora DB cluster](Aurora.Connecting.md).

The following guide demonstrates how to use the various options in the "Connectivity & Security" tab in the AWS Management Console to connect to your database.

The RDS Console surfaces relevant information such as code snippets, endpoint details, and other connection details to help you connect to the database. It also offers a utility to generate a token and direct access through AWS CloudShell. Both the generate token utility and CloudShell connect using the master username you set up at the time of database creation.

### Using the Connectivity & security tab
<a name="CHAP_GettingStartedAurora.AuroraPostgreSQL.ExpressConfig.Connecting.ConnectivityTab"></a>

After your database is created, navigate to the Connectivity & security tab to access connection options. The Connect to database section provides three methods for connecting:

#### Code snippets
<a name="CHAP_GettingStartedAurora.AuroraPostgreSQL.ExpressConfig.Connecting.CodeSnippets"></a>

Use when connecting through SDK, APIs, or third-party tools. The console provides ready-to-use code snippets for your selected programming language. The snippets also dynamically reflect the authentication configuration for your database.

The following steps show connecting to your database cluster using the psql command line utility code snippet.

**Prerequisites**
+ You can connect to Aurora PostgreSQL DB clusters by using tools like psql, the PostgreSQL interactive terminal. To install psql and learn more about using the PostgreSQL interactive terminal, see psql in the PostgreSQL documentation.
+ You must have the latest version of the AWS CLI installed. To install or update the AWS CLI, see [Installing or updating to the latest version of the AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html).

**Connecting with psql**

**To connect with psql**

1. Sign in to the AWS Management Console and open the Amazon RDS console at [https://console.aws.amazon.com/rds/](https://console.aws.amazon.com/rds/).

1. Navigate to your database cluster from the Databases list tab.

1. Under the connectivity & Security tab, select the PSQL code snippet for your respective operating system (macOS, linux, or Windows).

1. Copy the code shown in connection steps modal.  
![The connection steps modal showing the PSQL code snippet.](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/images/aurora-express-config-image4.png)

1. Open a terminal on your local development environment / machine.

1. (optional) If you have already configured the AWS CLI and credentials, you can skip this step. Otherwise, use the following command for a temporary login session.

   ```
   aws login
   ```

1. Paste the command you copied in step 4. You should see psql login and the “postgres =>” prompt, enabling you to run SQL commands.

#### CloudShell
<a name="CHAP_GettingStartedAurora.AuroraPostgreSQL.ExpressConfig.Connecting.CloudShell"></a>

The console provides an automated way to connect to your cluster using AWS CloudShell. The following guide shows the steps to connect using psql and CloudShell.

**Prerequisites**

None

**Using CloudShell and PSQL**

**To connect using CloudShell and PSQL**

1. Sign in to the AWS Management Console and open the Amazon RDS console at [https://console.aws.amazon.com/rds/](https://console.aws.amazon.com/rds/).

1. Navigate to your database cluster from the Databases list tab.

1. Under the connectivity & Security tab, select CloudShell.

1. Choose **Launch Cloudshell**  
![The CloudShell launch button in the connectivity and security tab.](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/images/aurora-express-config-image5.png)

1. Choose **Run** on the prompt window. The command is prepopulated with relevant information to connect to your specific cluster.  
![The CloudShell prompt window with pre-populated connection command.](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/images/aurora-express-config-image6.png)

1. You should see psql login and the “postgres =>” prompt, enabling you to run SQL commands.  
![The psql login prompt in CloudShell showing successful connection.](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/images/aurora-express-config-image7.png)

Use for quick access to AWS CLI that launches directly from the AWS Management Console. CloudShell provides a browser-based shell environment with pre-authenticated AWS CLI access.

#### Endpoints with Get token utility
<a name="CHAP_GettingStartedAurora.AuroraPostgreSQL.ExpressConfig.Connecting.GetToken"></a>

If you are using tools that only support using username and password credentials, you can use the Get token utility to connect. In this case, you use the token generated by the utility in the password field. The token is generated for the master username that you setup at the time of creating the database. The token is valid for 15 minutes at a time. If the tool you are using terminates the connection, you would need to generate the token again.

The following steps show, how to use the Get token utility to connect to your database cluster using pgAdmin.

**Prerequisites**
+ You can use the pgAdmin utility to connect to Aurora PostgreSQL DB clusters by using a UI interface. For more information, see the [Download](https://www.pgadmin.org/download/) page from the pgAdmin website.

**Connecting to pgAdmin**

**To connect using pgAdmin**

1. Sign in to the AWS Management Console and open the Amazon RDS console at [https://console.aws.amazon.com/rds/](https://console.aws.amazon.com/rds/).

1. Navigate to your database cluster from the Databases list tab.

1. Under the connectivity & Security tab, select the “Endpoints” tab.  
![The Endpoints tab showing writer endpoint, port, and database details.](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/images/aurora-express-config-image8.png)

1. Copy the relevant information, including the writer endpoint, port, master username, and database name.

1. Generate and copy a new token (short lived password) from the Get token utility.  
![The Get token utility for generating an authentication token.](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/images/aurora-express-config-image9.png)

1. Open pgAdmin on your machine, and “Add a new server”. Enter the details in the Connection tab. Use the token in the password field.  
![The pgAdmin connection dialog with server details.](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/images/aurora-express-config-image10.png)

The connection panel displays: internet access gateway status (Enabled), IAM Authentication status (Enabled), and IAM authentication token option. Select your programming language from the dropdown and follow the connection steps to paste the code and run the commands.

## Moving a cluster with express configuration into a VPC
<a name="CHAP_GettingStartedAurora.AuroraPostgreSQL.ExpressConfig.MoveIntoVPC"></a>

You can move an Aurora PostgreSQL DB cluster that uses the internet access gateway into a virtual private cloud (VPC). For example, you might start with a cluster with express configuration for prototyping, and then move it into your VPC when you prepare for production. In a VPC, you can control network access with VPC security groups and private subnets, and you can use features that require a VPC, such as Aurora global databases, RDS Proxy, and blue/green deployments.

When you move a cluster into a VPC, Aurora turns on VPC networking and turns off the internet access gateway in a single operation. The cluster endpoint doesn't change, so clients in the VPC keep using the same endpoint. You don't need to take a snapshot and restore it into a new cluster.

This procedure also applies to an Aurora PostgreSQL DB cluster that you previously moved out of a VPC. For more information, see [Moving a DB cluster out of a VPC](USER_VPC.WorkingWithRDSInstanceinaVPC.md#USER_VPC.WorkingWithRDSInstanceinaVPC.MoveOutOfVPC).

**Important**  
Connectivity to the cluster is briefly interrupted while Aurora moves it into the VPC. After the move, clients outside the VPC can no longer connect to the cluster through the internet access gateway. Make sure that your applications can reach the VPC before you move the cluster, and schedule the move for a time when a brief interruption is acceptable.

### Before you begin
<a name="CHAP_GettingStartedAurora.AuroraPostgreSQL.ExpressConfig.MoveIntoVPC.BeforeYouBegin"></a>
+ **Choose a VPC and DB subnet group.** The DB subnet group must have a subnet with available IP addresses in each Availability Zone where the cluster has a DB instance. To find these Availability Zones, run `aws rds describe-db-instances --filters Name=db-cluster-id,Values={{cluster}} --query "DBInstances[].AvailabilityZone"`. If you plan to add DB instances in other Availability Zones later, include subnets in those zones too. For more information, see [Working with DB subnet groups](USER_VPC.WorkingWithRDSInstanceinaVPC.md#USER_VPC.Subnets).
+ **Choose VPC security groups.** The security groups must belong to the VPC of the DB subnet group, and must allow your clients to connect on the database port.
+ **Defaults.** If you don't specify a DB subnet group, VPC security groups, or a network type, Aurora uses the same defaults as when you create a cluster in a VPC. For more information, see [Creating a cluster with express configuration in a VPC](#CHAP_GettingStartedAurora.AuroraPostgreSQL.ExpressConfig.CreateInVPC).
+ **Make sure that all DB instances in the DB cluster are available.** If a DB instance is in the incompatible-network state when the move starts, the move fails and the whole DB cluster can enter that state.
+ **Plan client connectivity.** Clients must be able to reach the VPC, for example from Amazon EC2 instances or AWS Lambda functions in the VPC, or through VPC peering, AWS Transit Gateway, AWS Site-to-Site VPN, or Direct Connect. Clients that connect over the internet through the internet access gateway lose access after the move.
+ **Check your IAM permissions.** See [IAM permissions](#CHAP_GettingStartedAurora.AuroraPostgreSQL.ExpressConfig.MoveIntoVPC.IAM).

### IAM permissions
<a name="CHAP_GettingStartedAurora.AuroraPostgreSQL.ExpressConfig.MoveIntoVPC.IAM"></a>

To move a DB cluster into a VPC, you need permission for the following actions on the DB cluster:
+ `rds:ModifyDBCluster`
+ `rds:EnableVpcNetworking`
+ `rds:DisableInternetAccessGateway`

If you specify a DB subnet group, you also need permission for `rds:ModifyDBCluster` on the DB subnet group.

These additional permissions help prevent a DB cluster from being moved into or out of a VPC by mistake. `rds:ModifyDBCluster` permission alone isn't enough.

### Console
<a name="CHAP_GettingStartedAurora.AuroraPostgreSQL.ExpressConfig.MoveIntoVPC.Console"></a>

**To move a cluster with express configuration into a VPC**

1. Sign in to the AWS Management Console and open the [Amazon RDS console](https://console.aws.amazon.com/rds/).

1. In the navigation pane, choose **Databases**, and then choose the DB cluster that you want to move.

1. Choose **Modify**.

1. In the **Connectivity** section, for **Network access type**, choose **VPC**.  
![Connectivity section with Network access type options VPC and Internet access gateway, VPC selected, and the Virtual private cloud, DB subnet group, VPC security group, Network type, and Database port fields.](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/images/aurora-express-modify-connectivity-vpc.png)  
   The Connectivity section of the Modify DB cluster page, with Network access type set to VPC.

1. Choose the **Virtual private cloud (VPC)**, **DB subnet group**, and **VPC security group (firewall)** for the cluster. Optionally, choose the **Network type**.

1. Choose **Continue** and review the summary of modifications.

1. To move the cluster now, choose **Apply immediately**. Otherwise, Aurora moves the cluster during the next maintenance window.

1. Choose **Modify cluster**.

When the move starts, the cluster status changes to `modifying`. When the status returns to `available`, the cluster is in the VPC. On the cluster's **Configuration** tab, **Network access type** shows **VPC**.

### AWS CLI
<a name="CHAP_GettingStartedAurora.AuroraPostgreSQL.ExpressConfig.MoveIntoVPC.CLI"></a>

Call the [modify-db-cluster](https://docs.aws.amazon.com/cli/latest/reference/rds/modify-db-cluster.html) command and specify both `--enable-vpc-networking` and `--no-enable-internet-access-gateway`. Optionally, specify `--db-subnet-group-name`, `--vpc-security-group-ids`, and `--network-type`. To move the cluster now, specify `--apply-immediately`. If you specify `--no-apply-immediately` or omit the option, Aurora moves the cluster during the next maintenance window.

Example:

For Linux, macOS, or Unix:

```
aws rds modify-db-cluster \
    --db-cluster-identifier sample-express-cluster \
    --enable-vpc-networking \
    --no-enable-internet-access-gateway \
    --db-subnet-group-name mysubnetgroup \
    --vpc-security-group-ids sg-0abcd1234efgh5678 \
    --network-type IPV4 \
    --apply-immediately
```

For Windows:

```
aws rds modify-db-cluster ^
    --db-cluster-identifier sample-express-cluster ^
    --enable-vpc-networking ^
    --no-enable-internet-access-gateway ^
    --db-subnet-group-name mysubnetgroup ^
    --vpc-security-group-ids sg-0abcd1234efgh5678 ^
    --network-type IPV4 ^
    --apply-immediately
```

### RDS API
<a name="CHAP_GettingStartedAurora.AuroraPostgreSQL.ExpressConfig.MoveIntoVPC.API"></a>

Call the ModifyDBCluster operation. Set `EnableVPCNetworking` to `true` and `EnableInternetAccessGateway` to `false`. Optionally, specify `DBSubnetGroupName`, `VpcSecurityGroupIds`, and `NetworkType`. Set `ApplyImmediately` to `true` to move the cluster now, or to `false` to move it during the next maintenance window.

### Verifying the move
<a name="CHAP_GettingStartedAurora.AuroraPostgreSQL.ExpressConfig.MoveIntoVPC.Verifying"></a>

The change is applied asynchronously. To check whether it's complete, run the [describe-db-clusters](https://docs.aws.amazon.com/cli/latest/reference/rds/describe-db-clusters.html) command:

For Linux, macOS, or Unix:

```
aws rds describe-db-clusters \
    --db-cluster-identifier sample-express-cluster \
    --query "DBClusters[0].[Status,VPCNetworkingEnabled,InternetAccessGatewayEnabled,DBSubnetGroup]"
```

For Windows:

```
aws rds describe-db-clusters ^
    --db-cluster-identifier sample-express-cluster ^
    --query "DBClusters[0].[Status,VPCNetworkingEnabled,InternetAccessGatewayEnabled,DBSubnetGroup]"
```

When the move is complete, `Status` is `available`, `VPCNetworkingEnabled` is `true`, `InternetAccessGatewayEnabled` is `false`, and `DBSubnetGroup` shows the DB subnet group that you chose.

If you scheduled the move for the next maintenance window, it appears in `PendingModifiedValues` as `VPCNetworkingEnabled: true` and `InternetAccessGatewayEnabled: false`. `PendingModifiedValues` doesn't show the DB subnet group or security groups that you chose.

### If the move doesn't complete
<a name="CHAP_GettingStartedAurora.AuroraPostgreSQL.ExpressConfig.MoveIntoVPC.NotComplete"></a>

If Aurora can't move the cluster into the VPC, it returns the cluster to the internet access gateway and publishes an RDS event. The cluster endpoint doesn't change. Check the event for the cause, correct it, and try again. If the cluster status doesn't return to `available`, contact AWS Support. For more information, see [Working with Amazon RDS event notification](USER_Events.md).

Aurora publishes RDS-EVENT-0673 when the move starts, RDS-EVENT-0674 when it completes, and RDS-EVENT-0675 if it fails. If Aurora rejects the change before the move starts, it publishes RDS-EVENT-0675 without RDS-EVENT-0673. For more information, see [Amazon RDS event categories and event messages for Aurora](USER_Events.Messages.md).

## Restoring a cluster created through express configuration
<a name="CHAP_GettingStartedAurora.AuroraPostgreSQL.ExpressConfig.Restoring"></a>

The restore process for express configuration clusters follows the same workflow as standard clusters. You can restore from a manual snapshot using the [restore-db-cluster-from-snapshot](https://docs.aws.amazon.com/cli/latest/reference/rds/restore-db-cluster-from-snapshot.html) operation or restore to a specific point in time using the [restore-db-cluster-to-point-in-time](https://docs.aws.amazon.com/cli/latest/reference/rds/restore-db-cluster-to-point-in-time.html) operation. You can restore a cluster with express configuration to either a cluster with full configuration or a cluster with express configuration. You don't need to take a snapshot and restore it to move a cluster with express configuration into a VPC. You can modify the cluster in place and keep its endpoint. For more information, see [Moving a cluster with express configuration into a VPC](#CHAP_GettingStartedAurora.AuroraPostgreSQL.ExpressConfig.MoveIntoVPC). If you want to restore to a cluster with express configuration, both restore operations require two additional parameters—EnableVPCNetworking must be set to false and EnableInternetAccessGateway must be set to true (in the AWS CLI, `--no-enable-vpc-networking` and `--enable-internet-access-gateway`). If you're restoring a regular cluster that used master username and password authentication to an express configuration cluster, you'll need to modify the restored DB cluster to update MasterUserAuthenticationType to iam-db-auth.

## Limitations
<a name="CHAP_GettingStartedAurora.AuroraPostgreSQL.ExpressConfig.Limitations"></a>

The following limitations apply to clusters created with express configuration and the internet access gateway that is enabled by default.
+ You can use express configuration only with Aurora PostgreSQL.
+ Cluster created with express configuration are encrypted with AWS/RDS service managed key. You cannot use a custom AWS KMS key to encrypt the database.
+ When connecting from a machine that is inside a VPC to the database with the express cluster with internet access gateway enabled, ensure that the machine allows inbound and outbound traffic from the internet.
+ A DB cluster uses either VPC networking or the internet access gateway. You can't turn off the internet access gateway unless you turn on VPC networking in the same request, and you can't turn off both.
+ You can only use RDS IAM authentication with the internet access gateway. See, [IAM database authentication](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/UsingWithRDS.IAMDBAuth.html) for list of limitations and recommendation. Features related to other forms of authentication such as managed credentials in AWS Secrets Manager, and Kerberos authentication cannot be used with clusters that have internet access gateway enabled. You also cannot disable IAM authentication.
**Warning**  
If you disable the `rds_iam` role for the master username, you will lose access to new connections to the database. You can restore access by modifying the cluster and setting the `--master-user-authentication-type` to `iam-db-auth`. See, [modify-db-cluster](https://docs.aws.amazon.com/cli/latest/reference/rds/modify-db-cluster.html).
+ You cannot select a specific engine version with express configuration. Engine version can be upgraded but not downgraded.
+ Clusters with express configuration only support creating an Aurora serverless instance. You can modify the instance type or add instances after the database is created.
+ Clusters with express configuration only support the default parameter group. The parameter group can be updated after the database is created.
+ The following features are not supported with clusters that don't use VPC networking. To use them, move the cluster into a VPC first. For more information, see [Moving a cluster with express configuration into a VPC](#CHAP_GettingStartedAurora.AuroraPostgreSQL.ExpressConfig.MoveIntoVPC).
  + Aurora limitless database
  + Aurora global database
  + RDS Proxy
  + Aurora Zero-ETL integration
  + RDS Query Editor
  + Blue/Green Deployments
  + Database Activity Streams
  + Zero Downtime Patching
  + Babelfish
+ Data API can be enabled for a cluster with express configuration after creation using the [EnableHttpEndpoint](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_EnableHttpEndpoint.html) operation. However, it doesn't support authentication with master username/password. You must create new user credentials to access Data API.
+ Database Insights Advanced mode can be enabled on a cluster with express configuration after creation using the ModifyDBCluster operation.
+ Clusters with express configuration that don't use VPC networking support IPv4 addresses only. IPv6 is not supported.
+ Clusters with express configuration does not support changing all settings at the time of create operations. For example, you can only choose Aurora Standard storage when creating with express configuration. You can change the storage type after the cluster is created. See, Express configuration settings for a list of all other settings and default values that apply with express configuration.
+ Clusters created through express configuration with internet access gateway enabled do not support configurable cipher suites. Although Amazon RDS for PostgreSQL allows you to configure the ssl\_ciphers parameter to restrict allowed SSL cipher suites, this parameter is ignored on clusters with internet access gateway enabled, which use the default cipher suite configuration instead.

After a cluster with express configuration is in a VPC, most of these limitations no longer apply. For example, you can change the DB cluster parameter group, and you can use password authentication or Secrets Manager for the master user. The following still apply:
+ The cluster stays encrypted with the AWS/RDS service owned key. You can't change it to a customer managed AWS KMS key.
+ You can't use Aurora Limitless Database. It can be chosen only when you create a cluster.
+ You can't use Babelfish for Aurora PostgreSQL.