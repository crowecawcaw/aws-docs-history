# Creating a Batch Operations job to update object encryption

To update the server-side encryption type of more than one Amazon S3 object with a single request, you
can use S3 Batch Operations. You can use S3 Batch Operations through the Amazon S3 console, AWS Command Line Interface (AWS CLI) AWS SDKs, or the Amazon S3 REST API.

To run the following commands, you must have the AWS CLI installed and configured. If you don’t
have the AWS CLI installed, see [Install or update to the latest version
of the AWS CLI](../../../cli/latest/userguide/getting-started-install.md "../../../cli/latest/userguide/getting-started-install.md") in the _AWS Command Line Interface User Guide_.

Alternatively, you can run AWS CLI commands from the console by using AWS CloudShell. AWS CloudShell is a
browser-based, pre-authenticated shell that you can launch directly from the AWS Management Console. For more
information, see [What is
CloudShell?](../../../cloudshell/latest/userguide/welcome.md "../../../cloudshell/latest/userguide/welcome.md") and [Getting started with AWS CloudShell](../../../cloudshell/latest/userguide/getting-started.md "../../../cloudshell/latest/userguide/getting-started.md") in
the _AWS CloudShell User Guide_.

###### Example 1 – Create a Batch Operations job that updates encrypted objects from one AWS KMS key to another KMS key

The following example shows how to create an S3 Batch Operations job that updates the
encryption settings for multiple objects in your general purpose bucket. This command creates a
job that changes objects encrypted with one AWS Key Management Service (AWS KMS) key to use a different KMS key.
This job also generates and saves a manifest of the affected objects and creates a report of the
results. To use this command, replace the `user input
 placeholders` with your own information.

```
aws s3control create-job --account-id `account-id` \
--no-confirmation-required \
--operation '{"S3UpdateObjectEncryption": {  "ObjectEncryption": { "SSEKMS": { "KMSKeyArn": "`KMS-key-ARN-to-apply`", "BucketKeyEnabled": false  }  }  } }' \
--report '{ "Enabled": true, "Bucket": "`report-bucket-ARN`",  "Format": "Report_CSV_20180820", "Prefix": "report", "ReportScope": "AllTasks" }' \
--manifest-generator '{ "S3JobManifestGenerator": { "ExpectedBucketOwner": "`account-id`", "SourceBucket": "`source-bucket-ARN`", "EnableManifestOutput": true, "ManifestOutputLocation": { "Bucket": "`manifest-bucket-ARN`", "ManifestFormat": "S3InventoryReport_CSV_20211130", "ManifestPrefix": "`manifest-prefix`" }, "Filter": {   "MatchAnyObjectEncryption": [{ "SSEKMS": { "KmsKeyArn": "`kms-key-ARN-to-match`" } }] } } }' \
--priority 1 \
--role-arn `batch-operations-role-ARN`
```

For best performance, we recommend using the `KmsKeyArn` filter in
conjunction with other object metadata filters, such as `MatchAnyPrefix`,
`CreatedAfter`, or `MatchAnyStorageClass`.

###### Example 2 – Create a Batch Operations job that updates SSE-S3 encrypted objects to SSE-KMS

The following example shows how to create an S3 Batch Operations job that updates the
encryption settings for multiple objects in your general purpose bucket. This command creates a
job that changes objects encrypted by using server-side encryption with Amazon S3 managed keys (SSE-S3)
to use server-side encryption with AWS Key Management Service (AWS KMS) keys (SSE-KMS) instead. This job also
generates and saves a manifest of the affected objects and creates a report of the results. To use
this command, replace the `user input placeholders` with
your own information.

```
aws s3control create-job --account-id `account-id` \
--no-confirmation-required \
--operation '{"S3UpdateObjectEncryption": {  "ObjectEncryption": { "SSEKMS": { "KMSKeyArn": "`KMS-key-ARN-to-apply`", "BucketKeyEnabled": false  }  }  } }' \
--report '{ "Enabled": true, "Bucket": "`report-bucket-ARN`",  "Format": "Report_CSV_20180820", "Prefix": "report", "ReportScope": "AllTasks" }' \
--manifest-generator '{ "S3JobManifestGenerator": { "ExpectedBucketOwner": "`account-id`", "SourceBucket": "`source-bucket-ARN`", "EnableManifestOutput": true, "ManifestOutputLocation": { "Bucket": "`manifest-bucket-ARN`", "ManifestFormat": "S3InventoryReport_CSV_20211130", "ManifestPrefix": "`manifest-prefix`" }, "Filter": {   "MatchAnyObjectEncryption": [{ "SSES3": {} }] } } }' \
--priority 1 \
--role-arn `batch-operations-role-ARN`
```

For best performance, we recommend using the `KmsKeyArn` filter in
conjunction with other object metadata filters, such as `MatchAnyPrefix`,
`CreatedAfter`, or `MatchAnyStorageClass`.
