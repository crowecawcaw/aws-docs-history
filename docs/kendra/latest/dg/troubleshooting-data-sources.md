# Troubleshooting data sources

This section can help you solve common issues when configuring and using Amazon Kendra data source connectors.

## My documents were not

indexed

When you synchronize your Amazon Kendra index with a data source, you may run
into issues that prevent the documents from being indexed. Indexing is a two-step
process. First, the data source is checked for new and updated documents to index,
and to find documents to remove from the index. Second, at the document level, each
document is accessed and indexed.

An error can occur in either of these steps. Data source level errors are reported
in the console in the **Sync run history** section of the data
source details page. The status of the synchronization job can be
**Succeeded**, **Incomplete**, or
**Failed**. You can also see the number of documents indexed
and deleted during the job. If the status is **Failed**, a message
is shown in the **Details** column.

Document level errors are reported in Amazon CloudWatch Logs. You can see the
errors using the CloudWatch console.

To generate a document sync status report, see [I want to generate a sync status report for my documents](troubleshooting-data-sources.md#troubleshooting-data-sources-sync-status-manifest "troubleshooting-data-sources.md#troubleshooting-data-sources-sync-status-manifest").

## My synchronization job

failed

A synchronization job typically fails when there is a configuration error in the
index or the data source. In the console, you can find the error message in the
**Sync run history** section of the data source details page,
under the **Details** column. Document level errors are reported in
Amazon CloudWatch Logs. The error message gives information about what went
wrong. The problem is usually that the index or the data source does not have the
proper IAM permissions. The error message describes the missing
permissions. Here are some of the error messages that you can receive:

`Failed to create log group for job. Please make sure that the IAM role provided has sufficient permissions.`

If your index role does not have permission to use CloudWatch, the data
source will not be able to create a CloudWatch log. If you get this error,
you must add CloudWatch permissions to the index role.

`Failed to access Amazon S3 file prefix (`bucket
name`) while trying to crawl your metadata files. Please make
 sure the IAM role (`ARN`) provided has
 sufficient permissions.`

When you are using an Amazon S3 data source, Amazon Kendra must have
permission to access the bucket that contains the documents. You need to add
permission for Amazon Kendra to read the bucket to the data source IAM role.

`The provided IAM role (`ARN`) could
 not be assumed. Please make sure Amazon Kendra is a trusted entity that is
 allowed to assume the role.`

Amazon Kendra needs permission to assume the index and data source IAM roles. You need to add a trust policy to the roles with permission
for the `sts:AssumeRole` action.

For the IAM policies that Amazon Kendra needs to index a data
source, see [IAM roles](iam-roles.md "iam-roles.md").

To generate a document sync status report, see [I want to generate a sync status report for my documents](troubleshooting-data-sources.md#troubleshooting-data-sources-sync-status-manifest "troubleshooting-data-sources.md#troubleshooting-data-sources-sync-status-manifest").

## My

synchronization job is incomplete

Jobs are generally incomplete when they have completed the data source level
process but have some error during the document level process. When a job is
incomplete, some of the documents might not have successfully indexed. For an
Amazon S3 data source, an incomplete job is typically caused by:

- The metadata for one or more documents was invalid.
- When documents are submitted for indexing but at least one document was
  not submitted.
- When documents are submitted for deleting from the index but at least one
  document was not submitted.

To troubleshoot an incomplete synchronization job, look first to your CloudWatch logs.

1. From the details column, choose **View details in CloudWatch**.
2. Review the error messages to see what caused the document to fail.

To generate a document sync status report, see [I want to generate a sync status report for my documents](troubleshooting-data-sources.md#troubleshooting-data-sources-sync-status-manifest "troubleshooting-data-sources.md#troubleshooting-data-sources-sync-status-manifest").

## My

synchronization job succeeded but there are no indexed documents

Occasionally, an index synchronization job run will be marked as
**Succeeded** but there are no new or updated documents indexed
when you expect them. Possible reasons include:

- Check CloudWatch
  `DocumentsSubmittedForIndexingFailed` metric to see if any
  documents failed to synchronize. Check your CloudWatch logs for
  details.
- For an Amazon S3 data source, you may have given Amazon Kendra the wrong bucket name or prefix. Make sure that the bucket that Amazon Kendra is using is the one that contains the documents to
  index.
- When re-indexing a document that failed to be indexed in an earlier job,
  Amazon Kendra won't index it unless you've changed the document or
  its associated metadata file.

To generate a document sync status report, see [I want to generate a sync status report for my documents](troubleshooting-data-sources.md#troubleshooting-data-sources-sync-status-manifest "troubleshooting-data-sources.md#troubleshooting-data-sources-sync-status-manifest").

## I am running into

file format issues while syncing my data source

If you run into file format issues while adding files to your data source or
syncing your data source, make sure that your document types are Amazon Kendra
supported. For a list of document types supported by Amazon Kendra see [Document
types or formats](index-document-types.md "index-document-types.md").

If you are using the `BatchPutDocument` API with plain text files,
specify `PLAIN_TEXT` as content type.

## I want to

generate a sync history report for my documents

You can view a document-level sync run history report in CloudWatch for your data source
sync job by selecting **View Report**. A sync run history report
will have details about the progress and status of each document in the sync job. It
shows if a document succeeded, failed, or was skipped during the crawl, sync, and
index stages. You'll also find any error messages related to failed or skipped
documents. If the report doesn't show results for an in-progress sync job, the logs
may not be available yet. Check back later as data is emitted to the report as
events occur during the sync process.

To access your sync run history report, take the following steps:

1. Open the Amazon Kendra console at [https://console.aws.amazon.com/kendra/](https://console.aws.amazon.com/kendra/ "https://console.aws.amazon.com/kendra/").
2. From the left navigation menu, under **Data management**,
   choose **Data sources**, and then choose your data
   source.
3. From your data source summary page, scroll down and select the
   **Sync history** tab.
4. From **Sync run history**, select
   **Actions**.
5. From **Actions**, select **View
   report**. You will be redirected to the CloudWatch console where you will
   be able to access your report.

###### Note

A sync run history records if a document was successfully indexed during
ingestion, including attached ACLs and metadata, for all Amazon Kendra supported
connectors.

**If you're using the Amazon S3 connector:**

In addition to the vieing the document-level sync run history report in CloudWatch, you
can generate sync history reports for each document in your Amazon S3 data source and
copy it to an Amazon S3 bucket. During this process, your data is encrypted
using AWS KMS keys and can only be viewed by you. Reported document
status can be one of the following: **Failed**,
**Completed**, or **Succeeded with errors**.
Before you can generate sync status reports for Amazon S3, you must do the
following:

- Add the following Amazon Kendra service principal to your Amazon S3 access policy
- Create an Amazon S3 bucket with access permissions to Amazon Kendra

If you use the console, to generate a sync history report for Amazon S3, choose to
activate the **Generate reports** option from **Sync
history reports – _optional_** section on the
**Data source details** page. Then, enter the Amazon S3
bucket location and choose from the configuration options available. Reports will be
generated from the next sync after you have activated generate report.

If you delete the Amazon S3 bucket, you will lose your log data and will
have to set up a new bucket to store new sync reports.

###### Note

A sync history report provides information only about whether an Amazon S3
connector successfully crawled and ingested data.

## How much time does syncing

a data source take?

If there are no updates to documents, sync time for a Amazon Kendra index
increases in linear proportion to the number of documents. For example, 1,000
documents without any updates would take about five minutes to sync and 2,000
documents without any updates will take about 10 minutes. If there are any updates
to the documents, then the sync time will increase based on the number of documents
updated.

## What is the charge for

syncing a data source?

When you sync your index, it takes two minutes to warm up and activate Amazon EC2 to establish the necessary connections. You are not charged during
this process. Your usage meter begins only after the sync job starts. For more
information on Amazon Kendra pricing, see [_Amazon Kendra
pricing_](https://aws.amazon.com/kendra/pricing/ "https://aws.amazon.com/kendra/pricing/").

## I am getting an Amazon EC2 authorization error

If an Amazon EC2 unauthorized operation error occurs during a sync for a
virtual private cloud (VPC) data source, it's likely that your VPC IAM role lacks required permissions. Please check that the IAM role
you use for your data source has the attached permissions. For more information, see
[Virtual private cloud IAM role](iam-roles.md#iam-roles-vpc "iam-roles.md#iam-roles-vpc").

## I am unable to use search

index links to open my Amazon S3 objects

Your Amazon Kendra index can only access files that an Amazon S3 data
source grants it permissions to access. For example, Amazon Kendra cannot
modify the Amazon S3 permissions that determine if an object is meant to be
public or encrypted. Amazon Kendra also doesn't have the default permissions to
create or return a signed link for Amazon S3 objects. If you want to
activate signed linking for Amazon S3 objects in a Amazon Kendra index,
you have two options:

- You can use sign your index query results with the source uri object
  before returning the result to the search page. For a step-by-step
  walkthrough of this process, see [_Sharing objects using presigned
  URLs_](../../../AmazonS3/latest/userguide/ShareObjectPreSignedURL.md "../../../AmazonS3/latest/userguide/ShareObjectPreSignedURL.md").
- You can override the Amazon S3 object metadata source uri and make
  your service available through an CloudFront content delivery network
  (CDN) connected to an Amazon S3 bucket. Or, you can use an API Gateway proxy endpoint that returns a presigned URL and redirect to
  it.

## I am

getting an **`AccessDenied When Using SSL Certificate File`**
error message

If you are getting an access denied error when using an SSL certificate with your
data source, make sure that your IAM role has the permission to
access the SSL certificate file in its specified location. If the certificate is
encrypted with an AWS KMS key, your IAM role should also
have permission to decrypt using the AWS KMS key. For more information,
see [_Authentication and access control for AWS KMS_](../../../kms/latest/developerguide/control-access.md "../../../kms/latest/developerguide/control-access.md").

## I am

getting an authorization error when using a SharePoint data source

If you are getting an authorization error while syncing your index with a
SharePoint data source, confirm that you have a Site Admin role assigned to you in
SharePoint.

## My index

does not crawl documents from my Confluence data source

If your Amazon Kendra index is not crawling documents from your Confluence
data source during the syncing process, confirm that you are part of Administrator
Groups in Confluence.
