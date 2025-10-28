# SAP HANA backup on Amazon EC2

###### Note

[Supported services by AWS Region](backup-feature-availability.md#supported-services-by-region "backup-feature-availability.md#supported-services-by-region") contains the currently supported Regions
where SAP HANA database backups on Amazon EC2 instances are available.

AWS Backup supports backups and restores of SAP HANA databases on Amazon EC2 instances.

###### Topics

- [Overview of SAP HANA databases with AWS Backup](#saphanaoverview "#saphanaoverview")
- [Prerequisites for backing up SAP HANA databases
  through AWS Backup](#saphanaprerequisites "#saphanaprerequisites")
- [SAP HANA backup operations in the AWS Backup
  console](#saphanabackupconsole "#saphanabackupconsole")
- [View SAP HANA database backups](#saphanaviewbackup "#saphanaviewbackup")
- [Use AWS CLI for SAP HANA databases with AWS Backup](#saphanaapicli "#saphanaapicli")
- [Troubleshooting backups of SAP HANA
  databases](#saphanatroubleshooting "#saphanatroubleshooting")
- [Glossary of SAP HANA terms when using AWS Backup](#saphanaglossary "#saphanaglossary")
- [AWS Backup support of SAP HANA databases on EC2 instances
  release notes](#saphanareleasenotes "#saphanareleasenotes")

## Overview of SAP HANA databases with AWS Backup

In addition to the ability to create backups and to restore databases, AWS Backup
integration with Amazon EC2 Systems Manager for SAP allows customers to identify and tag SAP HANA
databases.

AWS Backup is integrated with AWS Backint Agent to perform SAP HANA backups and restores.
For more information, see [AWS Backint](../../../sap/latest/sap-hana/aws-backint-agent-sap-hana.md "../../../sap/latest/sap-hana/aws-backint-agent-sap-hana.md").

## Prerequisites for backing up SAP HANA databases

through AWS Backup

Several prerequisites must be completed before backup and restore activities can be
performed. Note you will need administrative access to your SAP HANA database and
permissions to create new IAM roles and policies in your AWS account to perform these
steps.

Complete [these prerequisites at Amazon EC2 Systems Manager](../../../ssm-sap/latest/userguide/get-started.md "../../../ssm-sap/latest/userguide/get-started.md").

1. [Set up required
   permissions for Amazon EC2 instance running SAP HANA database](../../../ssm-sap/latest/userguide/get-started.md#ec2-permissions "../../../ssm-sap/latest/userguide/get-started.md#ec2-permissions")
2. [Register
   credentials in AWS Secrets Manager](../../../ssm-sap/latest/userguide/get-started.md#register-secrets "../../../ssm-sap/latest/userguide/get-started.md#register-secrets")
3. [Install
   AWS Backint and AWS Systems Manager for SAP Agents](../../../sap/latest/sap-hana/aws-backint-agent-installing-configuring.md "../../../sap/latest/sap-hana/aws-backint-agent-installing-configuring.md")
4. [Verify SSM
   Agent](../../../ssm-sap/latest/userguide/get-started.md#verify-ssm-agent "../../../ssm-sap/latest/userguide/get-started.md#verify-ssm-agent")
5. [Verify
   parameters](../../../ssm-sap/latest/userguide/get-started.md#verification "../../../ssm-sap/latest/userguide/get-started.md#verification")
6. [Register SAP HANA
   database](../../../ssm-sap/latest/userguide/get-started.md#register-database "../../../ssm-sap/latest/userguide/get-started.md#register-database")

It is best practice to register each HANA instance only once. Multiple registrations
can result in multiple ARNs for the same database. Maintaining a single ARN and
registration simplifies backup plan creation and maintenance and can also help reduce
unplanned duplication of backups.

## SAP HANA backup operations in the AWS Backup

console

Once the prerequisites and SSM for SAP setups are complete, you can back up and
restore your SAP HANA on EC2 databases.

### Opt in to protect SAP HANA resources

To use AWS Backup to protect your SAP HANA databases, SAP HANA must be toggled on as one
of the protected resources. To opt in:

1. Open the AWS Backup console at [https://console.aws.amazon.com/backup](https://console.aws.amazon.com/backup "https://console.aws.amazon.com/backup").
2. In the left navigation pane, choose **Settings**.
3. Under **Service opt-in**, select **Configure
   resources**.
4. Opt in to **SAP HANA on Amazon EC2.**.
5. Click **Confirm**.

Service opt-in for SAP HANA on Amazon EC2 will now be enabled.

### Create a scheduled backup of SAP HANA

databases

You can [edit an existing backup
plan](updating-a-backup-plan.md "updating-a-backup-plan.md") and add SAP HANA resources to it, or you can [create a new backup
plan](creating-a-backup-plan.md "creating-a-backup-plan.md") just for SAP HANA resources.

If you choose to create a new backup plan, you will have three options:

1.  **Option 1: Start with a template**
    1. Choose a backup plan template.
    2. Specify a backup plan name.
    3. Click **Create plan**.

2.  **Option 2: Build a new plan**
    1. Specify a backup plan name.
    2. Optionally specify tags to add to backup plan.
    3. Specify the backup rule configuration.
       1. Specify a backup rule name.
       2. Select an existing vault or create a new backup vault. This is where
          your backups are stored.
       3. Specify a backup frequency.
       4. Specify a backup window.

       _Note transition to cold storage is currently
       unsupported_. 5. Specify the retention period.

       _Copy to destination is currently unsupported_ 6. (_Optional_) Specify tags to add to recovery
       points.

    4. Click **Create plan**.

3.  **Option 3: Define a plan using JSON**

        1. Specify the JSON for your backup plan by either modifying the JSON
         expression of an existing backup plan or creating a new expression.
        2. Specify a backup plan name.
        3. Click **Validate JSON**.

    Once the backup plan is created successfully, you can assign resources to the
    backup plan in the next step.

Whichever plan you use, ensure you [assign resources](assigning-resources.md "assigning-resources.md").
You can choose which SAP HANA databases to assign, including system and tenant
databases. You also have the option to exclude specific resource IDs.

### Create an on-demand backup of SAP HANA

databases

You can [create a
full on-demand backup](recov-point-create-on-demand-backup.md "recov-point-create-on-demand-backup.md") that runs immediately after creation. Note that
on-demand backups of SAP HANA databases on Amazon EC2 instances are full backups; incremental
backups are not supported.

Your on-demand backup is now created. It will begin backing up your specified
resources. The console will transition you to the **Backup jobs** page
where you can view the job progress. Take note of the backup job ID from the blue banner
at the top of your screen, as you will need it to easily find the status of your backup
job. When the backup is completed, the status will progress to `Completed`.
Backups can take up to several hours.

Refresh the **Backup jobs list** to see the status change. You can
also search for and click on your **backup job ID** to view detailed
job status.

### Continuous backups of SAP HANA databases

You can make [continuous
backups](point-in-time-recovery.md "point-in-time-recovery.md") , which can be used with point-in-time restore (PITR) (note that
on-demand backups preserve resources in the state in which they are taken; whereas PITR
uses continuous backups which record changes over a period of time).

With continuous backups, you can restore your SAP HANA database on an EC2 instance
by rewinding it back to a specific time that you choose, within 1 second of precision
(going back a maximum of 35 days). Continuous backup works by first creating a full
backup of your resource, and then constantly backing up your resource’s transaction
logs. PITR restore works by accessing your full backup and replaying the transaction log
to the time that you tell AWS Backup to recover.

You can opt in to continuous backups when you create a backup plan in AWS Backup using
the AWS Backup console or the API.

###### To enable continuous backups using the console

1. Sign in to the AWS Management Console, and open the AWS Backup console at [https://console.aws.amazon.com/backup](https://console.aws.amazon.com/backup "https://console.aws.amazon.com/backup").
2. In the navigation pane, choose **Backup plans**, and then
   choose **Create Backup plan**.
3. Under **Backup rules**, choose **Add Backup
   rule**.
4. In the **Backup rule configuration** section, select
   **Enable continuous backups for supported resources**.

After you disable [PITR (point-in-time
restore)](point-in-time-recovery.md "point-in-time-recovery.md") for SAP HANA database backups, logs will continue to be sent to AWS Backup
until the recovery point expires (status equals `EXPIRED)`. You can change to
an alternative log backup location in SAP HANA to stop the transmission of logs to
AWS Backup.

A continuous recovery point with a status of `STOPPED` indicates that a
continuous recovery point has been interrupted; that is, the logs transmitted from SAP
HANA to AWS Backup that show the incremental changes to a database have a gap. The recovery
points that occur within this timeframe gap have a status of
`STOPPED.`.

For issues you may encounter during restore jobs of continuous backups (recovery
points), see the [SAP HANA Restore troubleshooting](saphana-restore.md#saphanarestoretroubleshooting "saphana-restore.md#saphanarestoretroubleshooting") section of this guide.

## View SAP HANA database backups

**View the status of backup and restore jobs:**

1. Open the AWS Backup console at [https://console.aws.amazon.com/backup](https://console.aws.amazon.com/backup "https://console.aws.amazon.com/backup").
2. In the navigation pane, choose **Jobs**.
3. Choose backup jobs, restore jobs or copy jobs to see the list of your jobs.
4. Search for and click on your job ID to view detailed job statuses.

**View all recovery points in a vault:**

1. Open the AWS Backup console at [https://console.aws.amazon.com/backup](https://console.aws.amazon.com/backup "https://console.aws.amazon.com/backup").
2. In the navigation pane, choose **Backup vaults**.
3. Search for and click on a backup vault to view all the recovery points within the
   vault.

**View details of protected resources:**

1. Open the AWS Backup console at [https://console.aws.amazon.com/backup](https://console.aws.amazon.com/backup "https://console.aws.amazon.com/backup").
2. In the navigation pane, choose **Protected resources**.
3. You may also filter by resource type to view all backups of that resource
   type.

## Use AWS CLI for SAP HANA databases with AWS Backup

Each action within the Backup console has a corresponding API call.

To programmatically configure and manage AWS Backup and its resources, use the API call
[`StartBackupJob`](API_StartBackupJob.md "API_StartBackupJob.md") to backup an SAP HANA database on an EC2
instance.

Use `start-backup-job` as the CLI command.

## Troubleshooting backups of SAP HANA

databases

If you encounter errors during your workflow, consult the following example errors and
suggested resolutions:

**Python prerequisites**

- **Error: Zypper error related to Python version** since SSM for
  SAP and AWS Backup require Python 3.6 but SUSE 12 SP5 by default supports Python
  3.4.

**Resolution:** Install multiple versions of Python on SUSE12 SP5
by doing the following steps:

    1. Run an update-alternatives command to create a symlink for Python 3 in
     '/usr/local/bin/' instead of directly using '/usr/bin/python3'. This commands will
     set Python 3.4 as the default version. The command is: `# sudo
     update-alternatives —install /usr/local/bin/python3 python3 /usr/bin/python3.4
     5`
    2. Add Python 3.6 to alternatives configuration by running the following command:
     `# sudo update-alternatives —install /usr/local/bin/python3 python3
     /usr/bin/python3.6 2`
    3. Change the alternative configuration to Python 3.6 by running the following
     command: `# sudo update-alternatives —config python3`


    The following output should be displayed:



    ```
    There are 2 choices for the alternative python3 (providing /usr/local/bin/python3).
     Selection Path Priority Status
    * 0 /usr/bin/python3.4 5 auto mode
     1 /usr/bin/python3.4 5 manual mode
     2 /usr/bin/python3.6 2 manual mode
    Press enter to keep the current choice[*], or type selection number:
    ```
    4. Enter the number corresponding to Python 3.6.
    5. Check the Python version and confirm Python 3.6 is being used.
    6. (*Optional, but recommended*) Verify Zypper commands work
     as expected.

**Amazon EC2 Systems Manager for SAP discovery and registration**

- **Error: SSM for SAP failed to discover workload** due to
  blocked access to public endpoint for AWS Secrets Manager and SSM.

**Resolution:** Test if endpoints are reachable from your SAP
HANA database. If they cannot be reached, you can create Amazon VPC endpoints for AWS Secrets Manager
and SSM for SAP.

    1. Test access to Secrets Manager from Amazon EC2 host for HANA DB by running the following the
     command: `aws secretsmanager get-secret-value —secret-id
     hanaeccsbx_hbx_database_awsbkp` . If the command fails to return a value,
     the firewall is blocking access to Secrets Manager service endpoint. The log will stop at
     the step “Retrieving secrets from Secrets Manager”.
    2. Test connectivity to SSM for SAP endpoint by running the command `aws
     ssm-sap list-registration` . If the command fails to return a value, the
     firewall is blocking access to the SSM for SAP endpoint.


    Example error: `Connection was closed before we received a valid response
     from endpoint URL:
     “https://ssm-sap.us-west-2.amazonaws.com/register-application"`.

There are two options to proceed if the endpoints are not reachable.

    + Open firewall ports to allow access to public service endpoint for Secrets Manager and
     SSM for SAP; or,
    + Create VPC endpoints for Secrets Manager and SSM for SAP, then:




    	- Ensure Amazon VPC is enabled for DNSSupport and DNSHostname.
    	- Ensure your VPC endpoint has enabled Allow Private DNS Name.
    	- If the SSM for SAP discovery completed successfully, the log will show
    	 the host is discovered.

- **Error: AWS Backup and Backint connection fails due to blocked access to AWS Backup
  service public endpoints.**
  `aws-backint-agent.log` can show errors similar to this:
  `time="2024-01-03T11:39:15-08:00" level=error msg="Storage configuration
 validation failed: missing backup data plane Id"` or `level=fatal
 msg="Error performing backup missing backup data plane Id`. Also, the AWS Backup
  console can show `Fatal Error: An internal error occured.`

**Resolution:** Open firewall ports to allow access to public service endpoints (HTTPS). After
this option is used, DNS will resolve requests to AWS services through public IP
addresses.

- **Error: SSM for SAP registration fails due to HANA password containing
  special characters.** Example errors can include `Error connecting to
database HBX/HBX when validating its credentials.` or `Discovery failed
because credentials for HBX/SYSTEMDB either not provided or cannot be
validated.` after testing a connection using `hdbsql` for
  `systemdb` and `tenantdb` that was tested from HANA database
  Amazon EC2 instance.

In the AWS Backupconsole on the Jobs page, the backup job details can show a status of
`FAILED` with the error `Miscellaneous: b’* 10: authentication
 failed SQLSTATE: 28000\n’`.

**Resolution:** Ensure your password does not have special
characters, such as $.

- **Error: `b’* 447: backup could not be completed: [110507] Backint
exited with exit code 1 instead of 0. console output:
time...`**

**Resolution:** The AWS BackInt Agent for SAP HANA installation
might not have completed successfully. Retry the process to deploy the [AWS
Backint Agent](../../../sap/latest/sap-hana/aws-backint-agent-sap-hana.md "../../../sap/latest/sap-hana/aws-backint-agent-sap-hana.md") and [Amazon EC2 Systems Manager Agent](../../../systems-manager/latest/userguide/ssm-agent.md "../../../systems-manager/latest/userguide/ssm-agent.md") on
your SAP application server.

- **Error: Console does not match log files after
  registration.**

The discovery log shows failed registration when trying to connect to HANA DB due
to the password containing special characters, though the SSM for SAP Application
Manager for SAP console displays successful registration. it does not confirm that
registration was successful. If the console shows successful registration but the logs
do not, backups will fail.

**Confirm the registration status:**

    1. Log into the [SSM
     console](https://console.aws.amazon.com/systems-manager "https://console.aws.amazon.com/systems-manager")
    2. Select **Run Command** from the left side navigation.
    3. Under text field **Command history**, input `Instance
     ID:Equal:`, with the value equal to the instance you used for
     registration. This will filter command history.
    4. Use the command id column to find commands with status `Failed`.
     Then, find the document name of
     **AWSSystemsManagerSAP-Discovery**.
    5. In the AWS CLI, run the command `aws ssm-sap register-application
     status`. If returned value shows `Error`, the registration was
     unsuccessful.

**Resolution:** Ensure your HANA password does not have special
characters (such as ‘$’).

**Creating a backup of an SAP HANA database**

- **Error: AWS Backup console displays message “Fatal Error” when an on-demand
  backup for SystemDB or TenantDB is created.** This occurs because the
  public endpoint cannot be accessed. This is
  caused by a client side firewall that blocks access to this endpoint.

`aws-backint-agent.log` can show errors such as `level=error
 msg="Storage configuration validation failed: missing backup data plane Id"`
or `level=fatal msg="Error performing backup missing backup data plane
 Id."`

**Resolution:** Open firewall access to public endpoint .

- **Error:**
  `Database cannot be backed up while it is stopped`.

**Resolution:** Ensure the database to be backed up is active.
Database data and logs can be backed up only while the database is online.

- **Error:**
  `Getting backup metadata failed. Check the SSM document execution for more
 details.`

**Resolution:** Ensure the database to be backed up is active.
Database data and logs can be backed up only while the database is online.

**Monitoring backup logs**

- **Error:**
  `Encountered an issue with log backups, please check SAP HANA for
 details.`

**Resolution:** Check SAP HANA to ensure log backups are being
sent to AWS Backup from SAP HANA.

- **Error:**
  `One or more log backup attempts failed for recovery point.`

**Resolution:** Check SAP HANA for details. Ensure log backups
are being sent to AWS Backup from SAP HANA.

- **Error:**
  `Unable to determine the status of log backups for recovery point.`

**Resolution:** Check SAP HANA for details. Ensure log backups
are being sent to AWS Backup from SAP HANA.

- **Error:**
  `Log backups for recovery point %s were interrupted due to a restore operation on
 the database.`

**Resolution:** Wait for the restore job to complete. The log
backups should resume.

## Glossary of SAP HANA terms when using AWS Backup

**Data Backup Types:** SAP HANA supports two types of data backups:
Full and INC (incremental). AWS Backup optimizes which type is used during each backup
operation.

**Catalog Backups:** SAP HANA maintains its own manifest called a
_catalog_. AWS Backup interacts with this catalog. Each new backup will
create an entry in the catalog.

**Continuous Log Backup (Transaction Logs)**: For Point in Time
Recovery (PITR) functions, SAP HANA tracks all transactions since the most recent backup.

**System Copy:** A restore job in which the restore target database
is different from the source database from which the recovery point was created.

**Destructive Restore:** A destructive restore is a type of restore
job during which a restored database deletes or overwrites the source or existing
database.

**FULL:** A full backup is a backup of a complete database.

**INC:** An incremental backup is a backup of all changes to an SAP
HANA database since the previous backup.

## AWS Backup support of SAP HANA databases on EC2 instances

release notes

Certain functionalities are not supported at this time:

- Continuous backups (which use transaction logs) cannot
  be copied to other Regions or accounts. Snapshot backups can be copied
  to supported Regions and accounts from full backups.
- Backup Audit Manager and reporting are not currently supported.
- [Supported services by AWS Region](backup-feature-availability.md#supported-services-by-region "backup-feature-availability.md#supported-services-by-region") contains the currently supported
  Regions for SAP HANA database backups on Amazon EC2 instances.
