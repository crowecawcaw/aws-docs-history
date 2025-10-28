# Installing SAP BusinessObjects BI Platform in the DR Region

When you have selected the DR region, follow the steps in the [Preparing the OS](bobj-ha-dr-installing-for-ha.md#bobj-ha-dr-ha-preparing-os "bobj-ha-dr-installing-for-ha.md#bobj-ha-dr-ha-preparing-os") section earlier in this guide to build SAP BusinessObjects BI Platform EC2 instances in that region.

## Installing and Configuring the CMS Database for the DR Region

The CMS database in the DR region must be a copy of the CMS database in the primary region. The method for copying this database depends on the database type and your RTO and RPO requirements. This guide describes two options for an Amazon RDS MySQL database.

- Option 1: Create a cross-region Read Replica of the primary Amazon RDS MySQL database.

Amazon RDS uses the MySQL DB engine’s built-in replication functionality to create a special type of DB instance called a Read Replica from a source DB instance. Updates made to the source DB instance are asynchronously copied to the Read Replica. Create a Read Replica of the primary CMS database by following the instructions in the [Amazon RDS documentation](../../../AmazonRDS/latest/UserGuide/USER_ReadRepl.md#USER_ReadRepl.Create "../../../AmazonRDS/latest/UserGuide/USER_ReadRepl.md#USER_ReadRepl.Create"). The documentation also provides instructions for promoting a Read Replica to a primary DB instance. This option will provide a lower RPO and RTO than Option 2.

- Option 2: Copy primary database snapshots to the DR region and use them to build a DR CMS database.

Create a snapshot of the Amazon RDS MySQL DB and copy the snapshot to the DR region. Use this snapshot to create a new instance of the Amazon RDS MySQL DB, and use this instance to configure the SAP BusinessObjects BI Platform DR database. See the [Amazon RDS documentation](../../../AmazonRDS/latest/UserGuide/USER_CopySnapshot.md "../../../AmazonRDS/latest/UserGuide/USER_CopySnapshot.md") for instructions, features, and limitations of this option. For a continuous copy of the database content, you can create and schedule scripts to perform the snapshot and copy them to the DR region. You can also use open-source tools to deploy such solutions, but make sure to test any tools thoroughly before using them for your DR deployment. When your testing is complete and the primary region is active, you can delete the RDS instance. Create a new instance by using the latest snapshot when the DR system is required again.

## Installing a CMS Node

The steps to install the SAP BusinessObjects BI Platform application in the DR region are described in [SAP Note 2603573](https://launchpad.support.sap.com/#/notes/2603573 "https://launchpad.support.sap.com/#/notes/2603573"). This procedure uses SQL Anywhere to temporarily create Server Intelligence Agents (SIAs) on all instances with a local CMS database. In the next section, we’ll reconfigure all nodes to form a single SAP BusinessObjects BI Platform cluster.

1. Log in to all CMS servers for your SAP BusinessObjects BI Platform DR nodes, based on your design.
2. Install the CMS servers by following the instructions in the SAP Note and using the same SIA names as in the production cluster.

## Starting SAP BusinessObjects BI Platform in the DR Region

Create the SIA nodes for the CMS servers by following the procedure described in [SAP Note 2603573](https://launchpad.support.sap.com/#/notes/2603573 "https://launchpad.support.sap.com/#/notes/2603573"). When prompted for the CMS database details, use the connection information and credentials of the database created in the previous section. The CMS servers should now start correctly. You can now install the remaining tiers, such as the processing tier or web tier, as required by your design. The installation instructions for the primary region also apply to the DR region.

## Creating an Amazon EFS Filestore for the DR Region

The filestore for the DR region in the Amazon EFS file system must be a copy of the filestore in the primary region. You can use AWS DataSync for copying this data. See [Transfer Files to Amazon EFS Using AWS DataSync](../../../efs/latest/ug/gs-step-four-sync-files.md "../../../efs/latest/ug/gs-step-four-sync-files.md") for detailed steps.

1. Set up correct permissions for the Amazon EFS file system for the filestore.
2. Restart the input and output file servers in the DR region. You should now be able to verify that the SAP BusinessObjects BI Platform system in the DR region has all the data of the primary region, as of the time the database and filestore were last copied.

## Performing the Failover

When you complete all the steps described in the previous sections, the SAP BusinessObjects BI Platform system will be up and running in the DR region with primary region data. You can shut down the EC2 instances in the DR region when you don’t need them. Monitor the copy of the database and Amazon EFS file system to make sure that they’re active according to your configuration. In the event of a disaster or DR drill, follow these steps:

1. Start the CMS database in the DR region using one of these options:
   - If you’re using a Read Replica, open the [Amazon RDS console](https://console.aws.amazon.com/rds/ "https://console.aws.amazon.com/rds/") in the DR region, and then choose **Instances**. Select the DB instance that is the Read Replica of the production database, and then choose **Instance Actions**, **Promote Read Replica** to start the CMS database in the DR region.
   - If you’re using snapshots, open the [Amazon RDS console](https://console.aws.amazon.com/rds/ "https://console.aws.amazon.com/rds/") in the DR region, and then choose **Snapshots**. Select the latest snapshot and restore that snapshot to create a CMS database in the DR region.

2. If you’re using snapshots, update the data source settings for SAP BusinessObjects BI Platform in the DR region by following the instructions in the section _To select a new or existing CMS database on UNIX_ in the [SAP BusinessObjects BI Platform Administration Guide](https://help.sap.com/viewer/product/SAP_BUSINESSOBJECTS_BUSINESS_INTELLIGENCE_PLATFORM/4.2/en-US "https://help.sap.com/viewer/product/SAP_BUSINESSOBJECTS_BUSINESS_INTELLIGENCE_PLATFORM/4.2/en-US"). Use the RDS instance created with the latest CMS database snapshot in the primary region.
3. Copy the contents of the S3 bucket that has the latest Amazon EFS content (from the primary region) to the Amazon EFS file system for the input and output filestore, and set up correct permissions.
4. Start SAP BusinessObjects BI Platform in the DR region and perform validation.
5. Redirect your users by changing the value of the CNAME used for SAP BusinessObjects BI Platform from the Application Load Balancer for the primary region to the load balancer for the DR region.
