# General troubleshooting

###### Topics

- [Why is my export unhealthy?](#dataexports-unhealthy-export "#dataexports-unhealthy-export")
- [Why is my SQL statement not being accepted by
  Data Exports?](#dataexports-sql-statement "#dataexports-sql-statement")
- [Why can't I locate a predefined SQL script for
  configuring Athena within Data Exports?](#dataexports-sql-script "#dataexports-sql-script")
- [Why is one of my export partitions empty?](#dataexports-empty-partition "#dataexports-empty-partition")
- [Why are there no report files in the Amazon S3 bucket?](#cur-no-report-files "#cur-no-report-files")

## Why is my export unhealthy?

An “unhealthy” export is one that encountered an error when it last tried to deliver a
refresh to your Amazon S3 bucket. You may see one of the following error messages when hovering
your cursor over the “unhealthy” message or by calling the `GetExport` API.

- **Data Exports issues**
  - **Insufficient permission:** This means Data Exports was unable to
    deliver the export files to your S3 bucket. This can be fixed by updating your S3 bucket
    policy with the permission listed in [Setting up an
    Amazon S3 bucket for data exports](dataexports-s3-bucket.md "dataexports-s3-bucket.md").
  - **Bill owner changed:** This error can occur when your
    AWS account moves to a new organization or leaves an organization in AWS Organizations.
    It can also happen when you're in an organization and your management account changes
    whether you belong to a billing group in AWS Billing Conductor. The best way to solve this
    problem is to create a new CUR and delete your old CUR. If you believe your account should
    not have changed organizations or billing groups, contact your account admin.
  - **Internal failure:** This error is due to an issue with
    the Data Exports internal infrastructure. Review the AWS Service Health Dashboard for updates on
    any service-wide issues that may be affecting Data Exports, or contact AWS Support for more
    information or help.

- **QuickSight integration issues**
  - **Insufficient SPICE capacity:** This error means that
    QuickSight does not have enough processing capacity provisioned to ingest your cost and
    usage data. For information on how to increase your SPICE capacity, see [Managing
    SPICE memory capacity](../../../quicksight/latest/user/managing-spice-capacity.md "../../../quicksight/latest/user/managing-spice-capacity.md").
  - **Insufficient permission to access the manifest file:**
    The service role you assigned to QuickSight to access your S3 bucket is no longer working.
    Review your service policy to make sure it's giving read permissions to the S3 bucket
    storing your cost and usage data.
  - **Access denied when trying to access manifest file:**
    Your IAM role does not have access to the S3 bucket storing your export files to check
    whether a QuickSight dashboard exists for this export. The dashboard may or may not be
    working. You need `s3:GetObject` permissions on the S3 bucket storing the export
    data in order to be able to check for a QuickSight dashboard.
  - **QuickSight CreateBundle failed:** This error means your
    dashboard failed to be created in QuickSight. This may have happened due to a delay in IAM
    role propagation if you created a new service role, or if you selected an existing service
    role that did not have the right permissions. Use the retry action if you created a new
    service role. If you selected an existing service role, you should delete your export and
    create a new one with a new service role.
  - **Dashboard does not exist:** This error means your
    dashboard was deleted in QuickSight. You should delete your existing cost and usage
    dashboard export in Data Exports and recreate it.
  - **QuickSight account does not exist:** This error means
    your QuickSight account was deleted. You will need to recreate your QuickSight account to
    use a dashboard again. After recreating your QuickSight account, you should delete your
    existing cost and usage dashboard export in Data Exports and recreate it.

## Why is my SQL statement not being accepted by

Data Exports?

Data Exports supports a limited set of SQL syntax that is mainly focused on column selections and
row filters. Make sure your SQL statement is using only the relevant keywords and operators. For
full details, see [Data query](dataexports-data-query.md "dataexports-data-query.md").

## Why can't I locate a predefined SQL script for

configuring Athena within Data Exports?

Unlike Cost and Usage Reports (CUR), Data Exports doesn't offer an SQL file for setting up Athena to query
your exports. You'll need to either use a CloudFormation template for Data Exports or manually configure
Athena. For more information, see [Configuring Amazon Athena](dataexports-processing.md "dataexports-processing.md").

## Why is one of my export partitions empty?

If an export is larger than most applications can handle, AWS splits the report into
multiple files. If an export update is smaller than the previous export and you're using
“overwrite” mode, AWS overwrites the unneeded partitions with empty data. The export manifest
only lists the partitions that have data. Review the report’s manifest file to find any empty
files that you don’t need to ingest.

## Why are there no report files in the Amazon S3 bucket?

Confirm that the Amazon S3 bucket policy grants the
**billingreports.amazonaws.com** service permission to put files in the
bucket. For more information on the required bucket policy, see [Setting up an Amazon
S3 bucket for data exports](dataexports-s3-bucket.md "dataexports-s3-bucket.md") or [Setting up an Amazon S3 bucket for Cost and Usage Reports](cur-s3.md "cur-s3.md").
