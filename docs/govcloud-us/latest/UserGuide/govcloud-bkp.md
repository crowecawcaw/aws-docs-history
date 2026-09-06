

# AWS Backup in AWS GovCloud (US)
<a name="govcloud-bkp"></a>

AWS Backup is a fully managed backup service that makes it easy to centralize and automate the backup of data across AWS services in the cloud and on premises. Using AWS Backup, you can configure backup policies and monitor backup activity for your AWS resources in one place. AWS Backup automates and consolidates backup tasks that were previously performed service-by-service, and removes the need to create custom scripts and manual processes. With just a few clicks on the AWS Backup console, you can create backup policies that automate backup schedules and retention management.

## Region availability
<a name="_region_availability"></a>

This service is available in the following AWS GovCloud (US) Regions:
+  AWS GovCloud (US-West) 
+  AWS GovCloud (US-East) 

## How AWS Backup differs
<a name="govcloud-bkp-diffs"></a>

The following differences apply to AWS Backup:
+ Restore testing is not available.
+ Backup Audit Manager multi-account, multi-Region reporting is not available.

## Documentation
<a name="govcloud-bkp-docs"></a>
+  [AWS Backup documentation](https://docs.aws.amazon.com/aws-backup/latest/devguide/whatisbackup.html) 

## Export-controlled content
<a name="govcloud-bkp-itar"></a>

For AWS Services architected within the AWS GovCloud (US) Regions, the following list explains how certain components of data may leave the AWS GovCloud (US) Regions in the normal course of the service offerings. The list can be used as a guide to help meet applicable customer compliance obligations. Data not included in the following list remains within the AWS GovCloud (US) Regions.
+ Do not enter export-controlled data in the following AWS Backup fields:
  + Resource tag
  + Plan name
  + Rule name
  + Selection name
  + Vault name