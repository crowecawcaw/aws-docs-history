# Troubleshooting data source connectors

This section can help you fix issues with Amazon Q Business data source
connectors.

###### Topics

- [My documents were not
  indexed](#troubleshooting-data-sources-not-indexed "#troubleshooting-data-sources-not-indexed")
- [My synchronization job
  failed](#troubleshooting-data-sources-failed "#troubleshooting-data-sources-failed")
- [My
  synchronization job is incomplete](#troubleshooting-data-sources-sync-job-incomplete "#troubleshooting-data-sources-sync-job-incomplete")
- [My
  synchronization job succeeded but there are no indexed documents](#troubleshooting-data-sources-succeeded-no-indexed-docs "#troubleshooting-data-sources-succeeded-no-indexed-docs")
- [I am running into
  file format issues while syncing my data source](#troubleshooting-data-sources-file-format-issues "#troubleshooting-data-sources-file-format-issues")
- [I am
  getting an AccessDenied When Using SSL Certificate File
  error message](#troubleshooting-data-sources-ssl-certificate-access-denied "#troubleshooting-data-sources-ssl-certificate-access-denied")
- [No CloudWatch Logs for Application Using New Connector](#troubleshooting-data-sources-no-cloudwatch-logs "#troubleshooting-data-sources-no-cloudwatch-logs")

## My documents were not

indexed

When you synchronize your Amazon Q Business index with a data source, you
may run into issues that prevent the documents from being indexed. Indexing is a
two-step process. First, the data source is checked for new and updated documents to
index, and to find documents to remove from the index. Second, at the document
level, each document is accessed and indexed.

An error can occur in either of these steps. Data source level errors are reported
in the console in the **Sync run history** section of the data
source details page. The status of the synchronization job can be
**Succeeded**, **Incomplete**, or
**Failed**. You can also see the number of documents indexed
and deleted during the job. If the status is **Failed**, a message
is shown in the **Details** column.

Document level errors are reported in Amazon CloudWatch Logs. You can see the
errors using the CloudWatch console.

You can view a document-level sync run history report in CloudWatch for your data source
sync job by selecting **View Report**. A sync run history report
will have details about the progress and status of each document in the sync job. It
shows if a document succeeded, failed, or was skipped during the crawl, sync, and
index stages. You'll also find any error messages related to failed or skipped
documents. If the report doesn't show results for an in-progress sync job, the logs
may not be available yet. Check back later as data is emitted to the report as
events occur during the sync process.

To access your sync run history report, take the following steps:

1. Open the Amazon Q Business console.
2. From the left navigation menu, under **Enhancements**,
   choose **Data sources**, and then choose your data
   source.
3. From your data source summary page, scroll down and select the
   **Sync history** tab.
4. From **Sync run history**, select
   **Actions**.
5. From **Actions**, select **View
   report**. You will be redirected to the CloudWatch console where you will
   be able to access your report.

A sync run history records if a document was successfully indexed during
ingestion, including attached ACLs and metadata, for all Amazon Q Business supported
connectors.

###### Note

To learn more about generating and understanding a sync run history report,
see [Introducing document-level sync reports: Enhanced data sync visibility in
Amazon Q Business](https://aws.amazon.com/blogs/machine-learning/introducing-document-level-sync-reports-enhanced-data-sync-visibility-in-amazon-q-business/ "https://aws.amazon.com/blogs/machine-learning/introducing-document-level-sync-reports-enhanced-data-sync-visibility-in-amazon-q-business/") in the _AWS Machine Learning
Blog_. To learn more about analyzing data using Amazon CloudWatch, see
[Analyzing log data with CloudWatch Logs Insights](../../../AmazonCloudWatch/latest/logs/AnalyzingLogData.md "../../../AmazonCloudWatch/latest/logs/AnalyzingLogData.md") in
the _Amazon CloudWatch User Guide_.

## My synchronization job

failed

A synchronization job typically fails when there is a configuration error in the
index or the data source. In the console, you can find the error message in the
**Sync run history** section of the data source details page,
under the **Details** column. Document level errors are reported in
Amazon CloudWatch Logs. The error message gives information about what went
wrong. The problem is usually that the index or the data source doesn't have the
correct IAM permissions. The error message describes the missing
permissions. Following are some of the error messages that you can receive:

`Failed to create log group for job. Please make sure that the IAM role provided has sufficient permissions.`

If your index role doesn't have permissions to use CloudWatch, the data
source can't create a CloudWatch log. If you get this error, you must add
CloudWatch permissions to the index role.

`Failed to access Amazon S3 file prefix (`bucket
name`) while trying to crawl your metadata files. Please make
 sure the IAM role (`ARN`) provided has
 sufficient permissions.`

When you're using an Amazon S3 data source, Amazon Q Business must
have permissions to access the bucket that contains the documents. You need to add
permissions for Amazon Q Business to read the bucket to the data source
IAM role.

`The provided IAM role (`ARN`) could
 not be assumed. Please make sure Amazon Q Business is a trusted entity
 that is allowed to assume the role.`

Amazon Q Business needs permissions to assume the index and data source
IAM roles. You need to add a trust policy to the roles with
permissions for the `sts:AssumeRole` action.

For the IAM policies that Amazon Q Business needs to index a
data source, see [IAM
roles for Amazon Q Business connectors](iam-roles.md#iam-roles-ds "iam-roles.md#iam-roles-ds").

## My

synchronization job is incomplete

Jobs are generally incomplete when they have completed the data source level
process but have some error during the document level process. When a job is
incomplete, some of the documents might not have indexed successfully . For an
Amazon S3 data source, an incomplete job is typically caused by one of
the following issues:

- The metadata for one or more documents was not valid.
- When documents are submitted for indexing but at least one document was
  not submitted.
- When documents are submitted for deleting from the index but at least one
  document was not submitted.

To troubleshoot an incomplete synchronization job, look first to your CloudWatch logs.

1. From the details column, choose **View details in CloudWatch**.
2. Review the error messages to see what caused the document to fail.

## My

synchronization job succeeded but there are no indexed documents

Occasionally, an index synchronization job run is marked as
**Succeeded**, but there are no new or updated documents
indexed when you expect them. Possible reasons include the following:

- Check CloudWatch
  `DocumentsSubmittedForIndexingFailed` metric to see if any
  documents failed to synchronize. Check your CloudWatch logs for
  details.
- For an Amazon S3 data source, you might have given Amazon Q Business the wrong bucket name or prefix. Make sure that the S3
  bucket that Amazon Q Business is using is the bucket that contains the
  documents to index.
- When re-indexing a document that failed to be indexed in an earlier job,
  Amazon Q Business won't index it unless you've changed the
  document or its associated metadata file.

## I am running into

file format issues while syncing my data source

If you run into file format issues while adding files to your data source or
syncing your data source, make sure that your document types are supported by
Amazon Q Business. For a list of document types supported by Amazon Q see [Supported document
types](doc-types.md "doc-types.md").

If you're using the `BatchPutDocument` API operation with plaintext
files, specify `PLAIN_TEXT` as the content type.

## I am

getting an **`AccessDenied When Using SSL Certificate File`**
error message

If you're getting an access denied error when using an SSL certificate with your
data source, make sure that your IAM role has the permissions to
access the SSL certificate file in its specified location. If the certificate is
encrypted with an AWS KMS key, your IAM role should also
have permissions to decrypt using the AWS KMS key. For more information,
see [Authentication and access control for AWS KMS](../../../kms/latest/developerguide/control-access.md "../../../kms/latest/developerguide/control-access.md") in the
_AWS Key Management Service Developer Guide_.

## No CloudWatch Logs for Application Using New Connector

I'm not seeing any CloudWatch logs for an application using a new connector.

To get the logs to display, you must call four operations before creating the connector:

1. `CreateLogGroup`: Create a log group with the name `/aws/qbusiness/${applicationId}` to be consistent with the sync run report link in the sync run history table.
2. `PutDeliverySource`: Create a delivery source with log-type set to `SYNC_JOB_LOGS`.
3. `PutDeliveryDestination`: Create a delivery destination using the log group ARN from step 1.
4. `CreateDelivery`: Create the delivery configuration linking the source and destination.

**CLI Example**

Replace `YOUR_APPLICATION_ID` with your actual application ID:

**Step 1: Create the log group**

```
aws logs create-log-group \
    --log-group-name "/aws/qbusiness/YOUR_APPLICATION_ID"
```

**Step 2: Create delivery source**

```
aws logs put-delivery-source \
    --name "qbusiness-sync-logs-source" \
    --log-type "`SYNC_JOB_LOGS`"
    --resource-arn "arn:aws:qbusiness:`REGION`:`012345678910`:application/$`{APP_ID}`"
```

**Step 3: Create delivery destination**

```
aws logs put-delivery-destination \
    --name "`qbusiness-sync-logs-destination`" \
    --delivery-destination-configuration '{"destinationResourceArn":"arn:aws:logs:`REGION`:`ACCOUNT_ID`:log-group:/aws/qbusiness/`01a2c3d4-a1b2-a1b2-a1b2-01a2c3b4d5`}'
    --region "`region-name`"
```

**Step 4: Create delivery**

```
aws logs create-delivery \
    --delivery-source-name "qbusiness-sync-logs-source" \
    "arn:aws:logs:`region-name`:`012345678910`:`delivery-destination`:`qbusiness-sync-logs-destination`"
    --region "`region-name`"
```

**Note:** Update `REGION` and `ACCOUNT_ID` with your AWS region and account ID.

**Verification**

After completing these steps, create your connector, and run the sync job. The CloudWatch logs should now appear in the specified log group.
