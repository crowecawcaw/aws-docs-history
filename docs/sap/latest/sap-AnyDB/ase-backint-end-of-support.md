

# AWS Backint Agent for SAP ASE end of support
<a name="ase-backint-end-of-support"></a>

After careful consideration, we have decided to end support for AWS Backint Agent for SAP ASE, effective September 29, 2027. Beginning October 29, 2026, AWS Backint Agent for SAP ASE will no longer be available to download for new customers. As an existing customer, you can continue to use AWS Backint Agent for SAP ASE until September 29, 2027. After September 29, 2027, AWS Backint Agent for SAP ASE will no longer be available to download, existing installations will no longer be supported, and backup and restore operations that use the agent will no longer be supported and might not function as expected.

 AWS Backint Agent for SAP HANA is not affected by this change and continues to be supported until further notice.

## Key dates
<a name="ase-backint-eos-key-dates"></a>


| Milestone | Date | 
| --- | --- | 
| Public announcement of end of support | September 29, 2026 | 
| Downloads unavailable for new customers | October 29, 2026 | 
| End of support for new and existing customers | September 29, 2027 | 

## What continues before the end of support date
<a name="ase-backint-eos-what-continues"></a>

Between September 29, 2026 and September 29, 2027, AWS continues to provide the following for AWS Backint Agent for SAP ASE:
+  **Security patches** – Critical security updates continue to be released.
+  **Bug fixes** – Critical bug fixes that affect backup and restore reliability are delivered.
+  **Technical support** – AWS Support continues to assist you with issues through standard support channels.
+  **Documentation** – Existing documentation remains available.

No new features or enhancements are delivered during this period. We encourage you to begin migration planning promptly.

**Important**  
Backups created in Amazon S3 using the AWS Backint Agent for SAP ASE are not compatible with the recommended alternative solutions. The backup format used by the Backint agent is specific to its implementation of the SAP ASE Backup Server Archive API and cannot be restored using the alternatives including native ASE S3 commands or third-party backup tools.

During the migration period (October 29, 2026 to September 29, 2027), fully migrate your backup strategy to one of the recommended alternatives and create new full backups with your chosen alternative. Do not rely on backups that were created with the agent for recovery after the end of support date. We strongly recommend that you complete your migration well before September 29, 2027, to avoid any risk of business disruption.

## Alternatives and migration guidance
<a name="ase-backint-eos-alternatives"></a>

Consider migrating to one of the following alternatives well ahead of the end of support date.

### Option 1: SAP ASE native Amazon S3 backup (recommended)
<a name="ase-backint-eos-native-s3"></a>

SAP ASE 16.1 natively supports `syb_aws` as an external API endpoint name with backup and recovery commands (`dump` and `load`). This allows you to use SAP ASE native commands and tools to control the flow of backups to Amazon S3, without requiring a separate agent.

Benefits:
+ No additional agent to install, configure, or maintain
+ Full end-to-end control of backup and recovery operations within SAP ASE
+ Native SAP support and documentation
+ No additional cost beyond standard Amazon S3 storage fees
+ Eliminates a third-party agent from the backup chain

#### Migration steps
<a name="ase-backint-eos-native-s3-migration"></a>

SAP ASE 16.1 includes a native Amazon S3 backup capability that eliminates the need for the AWS Backint Agent.

Prerequisites:
+ SAP ASE 16.1 or later
+ An Amazon S3 bucket outside of `us-east-1` (see [Known limitations](#ase-backint-eos-native-s3-limitations))
+ An IAM identity with at least `s3:PutObject`, `s3:GetObject`, `s3:ListBucket`, and `s3:GetBucketLocation` permissions on the target bucket
+ Access to the SAP ASE host OS with `root` or `sybase` user privileges

 **Step 1 – Create an Amazon S3 bucket** 

Create the target bucket in any Region other than `us-east-1`. For example, with the AWS CLI:

```
aws s3api create-bucket --bucket my-ase-backup-bucket --region us-west-2 --create-bucket-configuration LocationConstraint=us-west-2
```

For bucket naming rules and best practices, see [Bucket naming rules](https://docs.aws.amazon.com/AmazonS3/latest/userguide/bucketnamingrules.html) in the *Amazon S3 User Guide*.

 **Step 2 – Set up IAM credentials** 

Create an IAM user or role with a policy that grants access to the backup bucket. The following is a minimal policy example.

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": [
                "s3:PutObject",
                "s3:GetObject",
                "s3:ListBucket",
                "s3:GetBucketLocation"
            ],
            "Resource": [
                "arn:aws:s3:::my-ase-backup-bucket",
                "arn:aws:s3:::my-ase-backup-bucket/*"
            ]
        }
    ]
}
```

Generate an access key for the IAM user. The credentials are passed inline in the `dump database` command in Step 3. For more information about protecting credentials, see [Security best practices in IAM](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html).

**Note**  
Do not store credentials in plaintext files. See [Known limitations](#ase-backint-eos-native-s3-limitations) for the current status of `sp_config_dump` encrypted storage.

 **Step 3 – Run a backup** 

Connect to the SAP ASE instance.

```
source /opt/sap/SYBASE.sh
isql -Usa -P<sa_password> -S<server_name>:<port> -w1024
```

Run the `dump` command.

```
dump database <database_name> to "syb_aws::<backup_object_name>"
with extlib_login_name='<ACCESS_KEY_ID>',
extlib_login_pwd='<SECRET_ACCESS_KEY>',
extlib_container_name='my-ase-backup-bucket'
go
```

Replace the placeholders: `<database_name>` (the SAP ASE database to back up), `<backup_object_name>` (the Amazon S3 object key), `<ACCESS_KEY_ID>` and `<SECRET_ACCESS_KEY>` (the IAM credentials), and `my-ase-backup-bucket` (the target S3 bucket name).

A successful backup prints the following.

```
Backup Server: 3.42.1.1: DUMP is complete (database <database_name>).
```

 **Step 4 – Restore a backup** 

```
load database <database_name> from "syb_aws::<backup_object_name>"
with extlib_login_name='<ACCESS_KEY_ID>',
extlib_login_pwd='<SECRET_ACCESS_KEY>',
extlib_container_name='my-ase-backup-bucket'
go
```

 **Step 5 – Update automation and validate** 
+ Update cron jobs, scripts, or backup scheduling tools to use the new native `dump` and `load` commands.
+ Validate retention policies and ensure that S3 Lifecycle rules are correctly applied to the new backup paths.
+ Create new full backups with the native method during the migration period.
+ After you validate the migration, decommission AWS Backint Agent for SAP ASE from the Amazon EC2 instance.

#### Known limitations
<a name="ase-backint-eos-native-s3-limitations"></a>

Amazon S3 buckets in the `us-east-1` Region are not supported with the native SAP ASE Amazon S3 backup feature. Backup operations that target a bucket in `us-east-1` fail with `curlCode: 6, Could not resolve hostname`. There is no parameter that bypasses this behavior.

Use an Amazon S3 bucket in any Region other than `us-east-1`, such as `us-west-2`, `eu-west-1`, or `ap-southeast-1`. To open a support case with SAP for this issue, reference ASE 16.1 EBF 31284.

 **Troubleshooting** 


| Symptom | Likely cause | Resolution | 
| --- | --- | --- | 
|  `Could not resolve hostname` / `curlCode: 6`  | The bucket is in `us-east-1`, or `libaws-cpp-sdk-s3.so` is not on the library path. | Use a bucket outside of `us-east-1`, and verify that `ldconfig` includes `/opt/sap/ASE-16_1/lib/`. | 
| The backup server starts, but Amazon S3 operations silently fail. |  `libaws-cpp-sdk-s3.so` is not found at startup. | Run `ldconfig` and restart the backup server. | 
| Permission denied or HTTP 403 from Amazon S3 | The IAM policy is missing required actions. | Verify that the IAM policy includes `s3:PutObject`, `s3:GetObject`, `s3:ListBucket`, and `s3:GetBucketLocation`. | 

For issues with the native Amazon S3 backup feature, raise an incident through the [SAP support portal](https://me.sap.com).

### Option 2: AWS Storage Gateway (Amazon S3 File Gateway)
<a name="ase-backint-eos-storage-gateway"></a>

As an alternative, you can use AWS Storage Gateway (Amazon S3 File Gateway) to present an NFS file share that is backed by Amazon S3.

Benefits:
+ The NFS file share works as a standard SAP ASE backup and restore target.
+ Integrates with existing SAP ASE backup scripts without modification.

#### Migration steps
<a name="ase-backint-eos-storage-gateway-migration"></a>

1. Create an Amazon S3 File Gateway. Deploy the Storage Gateway VM (on premises through VMware, Hyper-V, or KVM, or on Amazon EC2). Activate and configure the gateway.

1. Create an NFS file share. Connect the NFS file share to the target S3 bucket, and restrict access to the SAP ASE database host.

1. Mount the NFS file share. On the SAP ASE database host, mount the NFS share to a local directory, such as `/mnt/s3-gateway`.

1. (Optional) Configure backup parameters. Use `sp_config_dump` to create an SAP ASE database dump configuration with the backup file directory (`@stripe_dir`) set to the NFS share path.

   ```
   sp_config_dump @config_name='db_bkp',
   @stripe_dir='/mnt/s3-gateway', @compression='101',
   @verify='header'
   go
   dump database <database_name> using config = db_bkp
   go
   ```

1. Run a backup. Run the `dump database` command either directly to the NFS mount, for example `/mnt/s3-gateway`:

   ```
   dump database <database_name> to /mnt/s3-gateway
   go
   ```

   Or by using the stored configuration:

   ```
   dump database <database_name> using config = db_bkp
   go
   ```

1. Restore from backup. Use the `load database` command with the backup file path on the NFS share.

   ```
   load database <database_name> from '/mnt/s3-gateway/<backup_file>'
   go
   ```

1. Test and validate. Perform end-to-end backup and restore testing.

1. Decommission the agent. After you validate the migration, remove AWS Backint Agent for SAP ASE.

Considerations:
+  AWS Storage Gateway pricing applies (gateway instance and storage).
+ The local cache size should be greater than the largest full backup size.
+ Data transfer from cache to Amazon S3 is asynchronous. Allow sufficient time before you verify backup availability in Amazon S3.

For a step-by-step walkthrough, see [Integrate an SAP ASE database to Amazon S3 using AWS Storage Gateway](https://aws.amazon.com/blogs/storage/integrate-an-sap-ase-database-to-amazon-s3-using-aws-storage-gateway/).

### Option 3: Third-party enterprise backup solutions
<a name="ase-backint-eos-third-party"></a>

SAP-certified enterprise backup solutions can target Amazon S3 as a storage destination.

Benefits:
+ Enterprise-grade backup management features
+ Centralized backup administration across heterogeneous environments
+ SAP certification and vendor support
+ Advanced features such as deduplication, compression, and catalog management

Considerations:
+ Additional licensing costs might apply.
+ Requires installation and configuration of third-party software.

#### Migration steps
<a name="ase-backint-eos-third-party-migration"></a>

1. Select an SAP-certified backup solution that supports SAP ASE and Amazon S3 as a storage target.

1. Install and configure the backup software, and configure Amazon S3 as the backup destination, by following the vendor documentation.

1. Configure the third-party solution to integrate with the SAP ASE Backup Server API.

1. Perform end-to-end backup and restore testing.

1. After you validate the migration, remove AWS Backint Agent for SAP ASE.

## Agent downloads for existing customers
<a name="ase-backint-eos-existing-downloads"></a>

On October 29, 2026, access to the AWS Backint Agent for SAP ASE download changes from publicly available to restricted to existing customers only. After that date, downloads require an authenticated request from an allowlisted AWS account. This access allows existing customers to obtain the critical security patches and bug fixes that AWS continues to publish until September 29, 2027. Existing installations are not affected, and an agent that is already installed continues to operate without any changes. If you have already migrated to one of the alternatives on this page, you do not need to take any action.

### Allowlisting
<a name="ase-backint-eos-allowlisting"></a>

Existing customer accounts are allowlisted automatically. No request is needed. If a download fails with an access denied error after October 29, 2026, open a support case through the [AWS Support Center](https://console.aws.amazon.com/support/home) and provide the AWS account ID that you use to download the agent.

### Grant read access within the AWS account
<a name="ase-backint-eos-grant-access"></a>

Allowlisting permits an AWS account to read the download bucket. It does not by itself grant that permission to a user or role inside the account. An additional IAM policy is required. Attach a policy such as the following to the IAM principal that performs the download. In most cases, this is the IAM role that is attached to the Amazon EC2 instance that runs SAP ASE.

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": "s3:GetObject",
            "Resource": "arn:aws:s3:::awssap-backint-agent-ase/binary/*"
        }
    ]
}
```

Add `s3:ListBucket` on `arn:aws:s3:::awssap-backint-agent-ase` to list the available agent versions. No AWS KMS permissions are required. The access that is granted is read-only and limited to the `binary/` prefix of the download bucket.

### Use an authenticated download
<a name="ase-backint-eos-authenticated-download"></a>

Unauthenticated access to the download bucket ends on October 29, 2026. Downloads over a plain HTTPS URL, for example with a web browser, `curl`, or `wget` without credentials, fail with an access denied error. Use the AWS CLI or an AWS SDK instead.

```
aws s3 cp s3://awssap-backint-agent-ase/binary/<version>/<file> .
```

The download bucket for commercial Regions is `s3://awssap-backint-agent-ase` (`us-east-1`).

**Important**  
Update any installation scripts, runbooks, or automation that currently retrieve the agent from a public URL. Scripts that rely on an unauthenticated download stop working on October 29, 2026, even for allowlisted accounts.

After September 29, 2027, download access to the agent is removed entirely. You will no longer be able to download AWS Backint Agent for SAP ASE.

## Frequently asked questions
<a name="ase-backint-eos-faq"></a>

 **Does this affect AWS Backint Agent for SAP HANA?**   
No. AWS Backint Agent for SAP HANA is not affected and continues to be fully supported.

 **What happens to existing backups that are stored in Amazon S3?**   
Existing backup data in Amazon S3 is not deleted and remains accessible with standard Amazon S3 tools. However, backups that were created with the agent might not be fully compatible with the recommended alternative backup solutions. Create new full backups with your chosen alternative during the migration period (October 29, 2026 to September 29, 2027), and do not rely on agent-created backups for recovery after the end of support date.

 **Is there a cost difference with the alternatives?**   
The SAP ASE native Amazon S3 backup approach has no additional cost from AWS beyond standard Amazon S3 storage fees, as of the date of this publication. AWS Storage Gateway pricing applies separately. Third-party solutions (such as Commvault or Veritas) might have additional licensing fees.

 **Can the agent continue to be used after the announcement but before the end of support date?**   
Existing installations remain functional during the 12-month notice period. We encourage you to begin migration planning promptly.

 **Will automated migration scripts be provided?**   
Because of the unique nature of each customer’s environment, automated migration scripts are not available. The migration guidance in this topic provides detailed step-by-step instructions for each recommended alternative.

 **When will new customers be blocked from accessing the agent?**   
After October 29, 2026 (30 days after the public announcement), the agent is no longer available to new customers.

 **What happens to existing backups in Amazon S3 that were created by the agent after the end of support date?**   
Existing backup data that is stored in Amazon S3 remains in your account, and you continue to incur standard Amazon S3 storage charges. These backups are in an agent-specific format and are not compatible with the recommended alternatives. Review your retention requirements and delete backups that are no longer needed to avoid unnecessary storage costs.

 **Will the agent continue to function after September 29, 2027? Can I restore an existing agent-created backup after the end of support date?**   
 AWS does not guarantee continued functionality of AWS Backint Agent for SAP ASE beyond the end of support date. After September 29, 2027, the agent no longer receives updates or support from AWS. Backup and restore operations that use the agent might not function as expected, and changes to underlying AWS services or other dependencies might cause the agent to stop working without notice. Complete your migration, and restore and re-create backups of any critical data with your chosen alternative before September 29, 2027.

 **Do I need to take any action regarding my existing Amazon S3 backups during the transition period?**   
Yes. You should do the following:  
+ Identify any historical backups that are needed for compliance or audit purposes, and restore them with the agent while it is still supported.
+ Re-create backups of any critical data with your chosen alternative (native SAP ASE Amazon S3 backup or AWS Storage Gateway).
+ After you validate the new backup strategy, delete old agent-format backups from Amazon S3 to avoid ongoing storage charges.

## Additional resources and support
<a name="ase-backint-eos-resources"></a>

For additional questions about this end of support announcement or assistance with migration planning:
+ Open a support case through the [AWS Support Center](https://console.aws.amazon.com/support/home).
+ Contact your AWS account team for guidance on migration planning and execution.

Related documentation:
+  [AWS Backint Agent for SAP ASE](ase-backint.md) 
+  [SAP ASE documentation – Backup and Recovery](https://help.sap.com/docs/SAP_ASE?locale=en-US) 
+  [Amazon S3 documentation](https://docs.aws.amazon.com/s3/) 
+  [AWS Support Center](https://console.aws.amazon.com/support/home) 
+  [IAM best practices](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html) 
+  [SAP ASE 16.1 Cloud Storage documentation](https://help.sap.com/docs/SAP_ASE/3bdda6b0ffad441aab4fe51e4e876a19/0ea25d91f623469a9a0fd3652825876b.html?version=16.1.0.0&locale=en-US) 
+  [Integrate an SAP ASE database to Amazon S3 using AWS Storage Gateway (blog)](https://aws.amazon.com/blogs/storage/integrate-an-sap-ase-database-to-amazon-s3-using-aws-storage-gateway/) 