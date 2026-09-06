

# Migrating an on-premises database to Amazon EC2
<a name="migrate-sql-from-on-premises"></a>

You can migrate your on-premises Microsoft SQL Server database to Amazon Elastic Compute Cloud (Amazon EC2). If you select a migration method and perform these steps, your on-premises database will reside on an Amazon EC2 instance running Windows Server.

**Topics**
+ [Automated SQL Server backup and restore](#migrate-sql-from-on-premises-automated)
+ [Manual SQL Server backup and restore](#migrate-sql-from-on-premises-manual)
+ [Server rehost](#migrate-sql-from-on-premises-rehost)

## Automated SQL Server backup and restore
<a name="migrate-sql-from-on-premises-automated"></a>

You can use AWS Migration Hub Orchestrator to orchestrate and automate the migration of SQL Server databases to Amazon EC2 using automated native backup and restore. This feature of AWS Migration Hub uses predefined workflow templates that are built based on best practices. Migration Hub Orchestrator automates error-prone manual tasks involved in the migration process, such as checking environment readiness and connections. For more information, see [Rehost SQL Server on Amazon EC2](https://docs.aws.amazon.com/migrationhub-orchestrator/latest/userguide/rehost-sql-ec2.html) in the *Migration Hub Orchestrator User Guide*.

## Manual SQL Server backup and restore
<a name="migrate-sql-from-on-premises-manual"></a>

You can use native backup files as a way to restore SQL Server databases without additional dependencies. You can back up and restore individual databases, or the entire database instance, from on premises to your EC2 instance.

**Topics**
+ [Prerequisites](#migrate-sql-from-on-premises-manual-prerequisites)
+ [Step 1: Backing up your database](#migrate-sql-from-on-premises-manual-backup)
+ [Step 2: Uploading your database backup files](#migrate-sql-from-on-premises-manual-upload)
+ [Step 3: Downloading your database backup files](#migrate-sql-from-on-premises-manual-download)
+ [Step 4: Restoring your database backup files](#migrate-sql-from-on-premises-manual-restore)

### Prerequisites
<a name="migrate-sql-from-on-premises-manual-prerequisites"></a>

You must meet the following prerequisites to migrate an on-premises database to Amazon EC2 using Amazon Simple Storage Service (Amazon S3):
+ An active AWS account. For more information, see [Set up Microsoft SQL Server on Amazon EC2](https://docs.aws.amazon.com/sql-server-ec2/latest/userguide/setting-up.html).
+ A source SQL Server database running on premises that you'd like to migrate.
+ A destination EC2 instance running Windows Server with SQL Server installed on it. It is preferred that the destination instance’s SQL Server version is the same or higher than the source SQL Server version running on premises. For more information on how to launch an instance, see [Launch your instance](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/LaunchingAndUsingInstances.html) in the *Amazon EC2 User Guide*.
+ An Amazon Simple Storage Service (Amazon S3) bucket. For more information, see [Creating, configuring, and working with Amazon S3 buckets](https://docs.aws.amazon.com/AmazonS3/latest/userguide/creating-buckets-s3.html) in the *Amazon S3 User Guide*.
+ Microsoft SQL Server Management Studio (SSMS) has been installed on the destination EC2 instance. For more information, see [Download SQL Server Management Studio (SSMS)](https://learn.microsoft.com/en-us/sql/ssms/download-sql-server-management-studio-ssms?view=sql-server-ver16#download-ssms) in the Microsoft documentation.

### Step 1: Backing up your database
<a name="migrate-sql-from-on-premises-manual-backup"></a>

You will need to create a full backup of the database as well as back up the Transaction Log for the on-premises SQL Server to capture all of the necessary data for restoration. This procedure generates the backup files can restore your database with in an EC2 instance.

**To back up an on-premises database**

1. Create a full backup of your database. For more information about how to create a full backup of your database, see [Create a Full Database Backup](https://learn.microsoft.com/en-us/sql/relational-databases/backup-restore/create-a-full-database-backup-sql-server?view=sql-server-ver16) in the Microsoft documentation.

1. Create a backup of the Transaction Log. For more information about how to back up the transaction log, see [Back up a Transaction Log](https://learn.microsoft.com/en-us/sql/relational-databases/backup-restore/back-up-a-transaction-log-sql-server?view=sql-server-ver16) in the Microsoft documentation.

1. Make a note of the backup file locations, because you will need to upload them to Amazon S3 in the next step.

### Step 2: Uploading your database backup files
<a name="migrate-sql-from-on-premises-manual-upload"></a>

With the backup files created, you can now upload them to Amazon S3.

**To upload your database backup files**

1. Determine size of your backup files to see which upload methods are supported.

1. Use the file locations you noted previously to upload your backup files. For more information about how you can upload your database backup files to Amazon S3, see [Uploading objects](https://docs.aws.amazon.com/AmazonS3/latest/userguide/upload-objects.html).

### Step 3: Downloading your database backup files
<a name="migrate-sql-from-on-premises-manual-download"></a>

Once the backup files have been uploaded to Amazon S3, you can restore them in an EC2 instance.

**To download your backup files from Amazon S3 in the EC2 instance**

1. Connect to your SQL Server instance and open SSMS. For more information, see [Connect to Microsoft SQL Server on Amazon EC2](connect-sql-server-on-ec2-instance.md).

1. Download the backup files in your Amazon EC2 instance running SQL Server. For more information about downloading your files from Amazon S3, see [Downloading an object](https://docs.aws.amazon.com/AmazonS3/latest/userguide/download-objects.html).

1. Make a note of the backup file locations, because you will need them to restore the database in the next step.

### Step 4: Restoring your database backup files
<a name="migrate-sql-from-on-premises-manual-restore"></a>

After you download the backup files, you can connect to your instance and restore them using SSMS.

**To restore your database**

1. Connect to your instance and open SSMS.

1. Restore the full database backup using the backup files noted previously. For more information about restoring your database from the backup files, see [Restore a Database Backup Using SSMS](https://learn.microsoft.com/en-us/sql/relational-databases/backup-restore/restore-a-database-backup-using-ssms?view=sql-server-ver16) in the Microsoft documentation.

1. In the EC2 instance, validate that your database has been restored as expected.

## Server rehost
<a name="migrate-sql-from-on-premises-rehost"></a>

You can choose to *rehost* (lift and shift) your entire SQL Server to Amazon EC2 instead of individual databases using AWS Transform MGN or AWS Migration Hub Orchestrator.

**MGN (MGN)**  
MGN (MGN) automates the migration of your servers and applications to the cloud during a cutover window. For more information on how you can rehost SQL Server using MGN, see [Quick start guide](https://docs.aws.amazon.com/mgn/latest/ug/quick-start-guide-gs.html) in the *MGN User Guide*.

**Migration Hub Orchestrator**  
Migration Hub Orchestrator orchestrates and further automates the rehost process for servers and applications. For more information on how you can rehost SQL Server using Migration Hub Orchestrator, see [Rehost applications on Amazon EC2](https://docs.aws.amazon.com/migrationhub-orchestrator/latest/userguide/rehost-on-ec2.html) in the *Migration Hub Orchestrator User Guide*.