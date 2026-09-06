

AWS Migration Hub is no longer open to new customers as of November 7, 2025. For capabilities similar to AWS Migration Hub, explore [AWS Transform](https://aws.amazon.com/transform).

# Migrate SAP NetWeaver based applications and SAP HANA databases to AWS
<a name="migrate-sap"></a>

With this template, you can automate the migration of your SAP NetWeaver based applications along with SAP HANA databases, or SAP HANA databases only to AWS.

**Topics**
+ [Migration types](#sap-migration-types)
+ [Prerequisites](#prerequisites-migrate-sap)
+ [Target environment setup](#target-env-setup-migrate-sap)
+ [Create a migration workflow](#create-workflow-migrate-sap)
+ [Details](#details-migrate-sap)
+ [Application](#applications-migrate-sap)
+ [Source environment configuration](#source-configurations-migrate-sap)
+ [Migration steps](#sap-migration-steps)

## Migration types
<a name="sap-migration-types"></a>

The template offers the following migration types.
+ SAP NetWeaver on SAP HANA – central system installation
+ SAP NetWeaver on SAP HANA – distributed system installation
+ SAP NetWeaver on SAP HANA – high availability installation
+ SAP NetWeaver on SAP HANA – scale-out
+ SAP HANA database – single node
+ SAP HANA database – high availability
+ SAP HANA database – scale-out

## Prerequisites
<a name="prerequisites-migrate-sap"></a>

You must meet the following requirements to create a migration workflow using this template.
+ Verify that your servers and applications are on a supported operating system. For more information, see [Version support for SAP deployments](https://docs.aws.amazon.com/launchwizard/latest/userguide/launch-wizard-sap-versions.html).
+ Enable network connectivity between the source and target servers by opening the required ports on both servers.
+ Provide credentials of SAP HANA database instance running on your source server. These credentials are used by the Migration Hub Orchestrator plugin to communicate with the source server.

  1. Sign in to [https://console.aws.amazon.com/secretsmanager/](https://console.aws.amazon.com/secretsmanager/).

  1. On the AWS Secrets Manager page, select **Store a new secret**.

  1. For Secret type, select **Other type of secret** and create the following key value pairs.    
[See the AWS documentation website for more details](http://docs.aws.amazon.com/migrationhub-orchestrator/latest/userguide/migrate-sap.html)
**Note**  
 The `hana_systemdb_username` and `hana_saptenantdb_username` must have admin permissions to enable the SAP HANA System Replication and perform database backups.

  1. Select **Next** and enter a name beginning with `migrationhub-orchestrator-{{secretname123}}` in Secret name.
**Important**  
The Secret ID must begin with the prefix `migrationhub-orchestrator-` and must only be followed by an alphanumeric value.

  1. Select **Next** and then, select **Store**.
+ The following parameters must be the same on the source and target environments.
  + SAP SID
  + SAP HANA SID
  + PAS instance number
  + ASCS instance number
  + SAP HANA instance number
  + SAP HANA database password
+ You must disable SAP HANA system replication before migrating SAP environments with high availability setup.

## Target environment setup
<a name="target-env-setup-migrate-sap"></a>

AWS Migration Hub Orchestrator guides you to create the target environment in AWS to host your SAP NetWeaver application using AWS Launch Wizard for SAP. For more information, see [Get started with AWS Launch Wizard for SAP](https://docs.aws.amazon.com/launchwizard/latest/userguide/launch-wizard-sap-getting-started.html).

Create an SAP deployment using AWS Launch Wizard for SAP. For more information, see [Deploy an SAP application with AWS Launch Wizard for SAP](https://docs.aws.amazon.com/launchwizard/latest/userguide/launch-wizard-sap-deploying.html#deploy-console-launch-wizard-sap).

**Note**  
Migration Hub Orchestrator supports single node or multi node SAP NetWeaver stack deployment for target. You must choose to deploy the SAP NetWeaver software as part of target environment setup with Launch Wizard.
+ Create a private key in the Amazon EC2 console and store it in the AWS Secrets Manager. The plugin uses this private key associated with the target instance to perform migration tasks.

  **See the following steps to create a private key.**

  1. Sign in to the Amazon EC2 console.

  1. In the left navigation pane, under Network & Security, select **Key Pairs**.

  1. Select **Create key pair**.

  1. Enter a name for the key pair beginning with `migrationhub-orchestrator-{{keyname123}}`.
**Important**  
The Key Pair must begin with the prefix `migrationhub-orchestrator-` and must only be followed by an alphanumeric value.

  1. Select **RSA** as the Key pair type.

  1. Select **.pem** as the Private key file format.

  1. Select **Create key pair** and save the file.

  **See the following steps to store the private key.**

  1. Sign in to [https://console.aws.amazon.com/secretsmanager/](https://console.aws.amazon.com/secretsmanager/).

  1. On the AWS Secrets Manager page, select **Store a new secret**.

  1. For Secret type, select **Other type of secret** and select **Plaintext** below.

  1. Copy and paste the Private key created in Amazon EC2 console and select Next.

  1. In Secret name, enter the same name (`migrationhub-orchestrator-{{keyname123}}`) that you used for creating the key pair.

  1. Select **Next** and then, **Store**.
+ To establish a connection between your source and target environments, we recommend creating a new security group with your source IP address while creating an SAP deployment with Launch Wizard.

  1. Under **Infrastructure - SAP landscape**, go to **Security groups**.

  1. Select **Create new security groups**.

  1. In Connection type, select **IP Address/CIDR**.

  1. In Value, enter your source IP address.
+ Launch Wizard attaches the `AmazonEC2RoleForLaunchWizard` instanceRole by default when creating the target environment. After creating the target instance with Launch Wizard, attach the `AWSMigrationHubOrchestratorInstanceRolePolicy` managed policy to `AmazonEC2RoleForLaunchWizard`. For more information, see [AWS managed policies for Migration Hub Orchestrator](https://docs.aws.amazon.com/migrationhub-orchestrator/latest/userguide/security-iam-awsmanpol.html#security-iam-awsmanpol-AWSMigrationHubOrchestratorInstanceRolePolicy).
+ Migration Hub Orchestrator uses the same secret to connect to databases on source and target servers for validation. For your target server, ensure that you provide the same SAP HANA database sign-in credentials that you stored in AWS Secrets Manager following the steps in [Prerequisites](#prerequisites-migrate-sap).

## Create a migration workflow
<a name="create-workflow-migrate-sap"></a>

1. Go to [https://console.aws.amazon.com/migrationhub/orchestrator/](https://console.aws.amazon.com/migrationhub/orchestrator/), and select **Create migration workflow**.

1. On Choose a workflow template page, select **Migrate SAP NetWeaver on HANA applications** template.

1. Configure and submit your workflow to begin migration.
   + [Details](#details-migrate-sap)
   + [Application](#applications-migrate-sap)
   + [Source environment configuration](#source-configurations-migrate-sap)

**Note**  
You can customize the migration workflow once it has been created. For more information, see [Migration workflows for Migration Hub Orchestrator](migration-workflows.md).

## Details
<a name="details-migrate-sap"></a>

Enter a name for your workflow. Optionally, you can enter a description and add tags. If you intend to run multiple migrations, we recommend adding tags to enhance searchability. For more information, see [Tagging AWS resources](https://docs.aws.amazon.com/general/latest/gr/aws_tagging.html).

## Application
<a name="applications-migrate-sap"></a>

Select the application you want to migrate. If you do not see the application in the list, you must define it in [AWS Application Discovery Service](https://console.aws.amazon.com/discovery/home).

### Define applications
<a name="define-applications"></a>

Define applications by adding a data source and grouping the servers as applications.

**Topics**
+ [Add data source](#add-data-source)
+ [Group servers](#group-servers)

#### Add data source
<a name="add-data-source"></a>

Get metadata about the source servers and applications that you want to migrate to AWS. You can use one of the following methods to collect the data.
+ **Migration Hub import** – Import information about your on-premises servers and applications into Migration Hub. For more information, see [Migration Hub Import](https://docs.aws.amazon.com/application-discovery/latest/userguide/discovery-import.html) in the *Application Discovery Service User Guide*. 
+ **AWS Agentless Discovery Connector** – The Discovery Connector is a VMware appliance that collects information about VMware virtual machines (VMs). For more information, see [AWS Agentless Discovery Connector](https://docs.aws.amazon.com/application-discovery/latest/userguide/discovery-connector.html) in the *Application Discovery Service User Guide*.
+ **AWS Application Discovery Agent** – The Discovery Agent is AWS software that you install on your on-premises servers and VMs to capture system information, as well as information about the network connections between systems. For more information, see [AWS Application Discovery Agent](https://docs.aws.amazon.com/application-discovery/latest/userguide/discovery-agent.html) in the *Application Discovery Service User Guide*.

#### Group servers
<a name="group-servers"></a>

To use Migration Hub Orchestrator, you must group servers as applications.

1. In AWS Migration Hub console, select **Discover**, **Servers**.

1. In the servers list, select each server that you want to group into a new or existing application.

1. To create your application, or add to an existing one, choose **Group as application**.

1. In the **Group as application** dialog box, choose **Group as a new application** or **Add to an existing application**.

1. Select **Group**.

To view and edit your applications in the AWS Migration Hub console, go to **Discover** > **Servers**.

## Source environment configuration
<a name="source-configurations-migrate-sap"></a>

Enter the details of the SAP source environment that you want to migrate with the Migration Hub Orchestrator.

**SAP application server configuration**
+ SAPSID: Enter the system ID of the SAP application that you want to migrate.
+ SAP application hostname: Enter the hostname of the source SAP application. 
+ AWS Application Discovery Service server ID for SAP application server: Select the server ID where the central instance of your source SAP application is running. The IDs in the list are available based on the application configurations made in AWS Application Discovery Service. For more information, see [Define applications](https://docs.aws.amazon.com/migrationhub-orchestrator/latest/userguide/orchestrate-migrations.html#define-applications).

**SAP HANA database configuration**
+ SAP HANA replication mode: Select from *synchronous* or *asynchronous* mode for database replication.
+ HANASID: Enter the system ID of your source SAP HANA database.
+ Instance number: Enter the instance number of your source SAP HANA database.
+ Database hostname: Enter the hostname of your source SAP HANA database. To find the hostname, run the `hostname` command on your database.
+ AWS Application Discovery Service server ID for SAP HANA database: Select the server ID where your SAP HANA database is running. The IDs in the list are available based on the application configurations made in Directory Service. For more information, see [Define applications](https://docs.aws.amazon.com/migrationhub-orchestrator/latest/userguide/orchestrate-migrations.html#define-applications).
+ Credentials: Select the credentials you created for your source HANA database in [Prerequisites](#prerequisites-migrate-sap).
+ Version: Migration Hub Orchestrator only supports migrations for SAP HANA database 2.0 versions. Verify that the version of your SAP HANA database is 2.0 or higher with `HDB version` command.
+ Backup location: Enter the backup location of your SAP HANA database.

**SSL encryption**
+ If you do not want to use SSL encryption for database replication, select the box next to *I want to disable SSL encryption for database replication*.
+ If you want to use SSL encryption for database replication or leave the box unchecked, a manual step – * Enable SSL on source for replication* in step group 4, must be completed to proceed with your migration workflow.

  1. Open the `global.ini` file on your source SAP HANA system.

  1. Set the replication property as follows.

     ```
            [system_replication_communication]
            enable_ssl=on
     ```

  1. Restart the database.
+ 
**Note**  
SSL encryption is required for SAP NetWeaver on SAP HANA – scale-out and SAP HANA database – scale-out migration types.

For more information, see SAP help portal – [Configure Secure Communication (TLS/SSL) Between Primary and Secondary Sites](https://help.sap.com/docs/SAP_HANA_PLATFORM/6b94445c94ae495c83a19646e7c3fd56/ec50b815f5b740d7a9777d80f7104a2c.html).

## Migration steps
<a name="sap-migration-steps"></a>

Migration Hub Orchestrator automates the migration process after you create the migration workflow. Some tasks require additional inputs and user interactions.
+ By default, Launch Wizard deploys the target SAP HANA database with baseline HANA components. If the source application that is being migrated has components that have been deployed after the initial installation, check and deploy those components on the target instance.
+ An SAP HANA system has several configuration `(*.ini )` files that contain properties for configuring the system as a whole and individual tenant databases, hosts, and services. SAP HANA's configuration files contain parameters for global system configuration `(global.ini)` and for each service in the system. For instance, `indexserver.ini`. Based on your application requirement, if any of these configuration files have been adjusted on the source, you need to update them on the newly deployed target system before cutover.
+ Before beginning cutover, verify that your source application has been migrated properly. Step group 7 of the **Migrate SAP NetWeaver to AWS** template guides you through the necessary steps.
  + **Stop source SAP production system**: Ensure that there are no end users logged in or accessing the application before stopping the source application.
  + **Stop source HANA production system**: Verify that the HANA System Replication has completed copying data to target and gracefully stopped the source HANA database.
  + **Cutover & Start SAP application**: Start the migrated SAP application servers on the target.
  + **Verify database records**: Verify database records to validate that the application has been migrated properly.
  + **Manual post processing**: Perform any manual post-migration tasks, such as attaching interface file systems or updating end user `SAPGUI`configuration to connect to the newly migrated applications on AWS.