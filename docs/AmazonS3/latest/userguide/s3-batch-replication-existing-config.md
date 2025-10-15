# Create a Batch Replication job for
 existing replication rules

In Amazon S3, live replication doesn't replicate any objects that already existed in your
 source bucket before you created a replication configuration. Live replication automatically
 replicates only new and updated objects that are written to the bucket after the replication
 configuration is created. To replicate already existing objects, you can use
 S3 Batch Replication to replicate these objects on demand. 

You can configure S3 Batch Replication for an existing replication configuration by
 using the AWS SDKs, AWS Command Line Interface (AWS CLI), or the Amazon S3 console. For an overview of
 Batch Replication, see [Replicating existing objects with
 Batch Replication](s3-batch-replication-batch.md "s3-batch-replication-batch.md").

When the Batch Replication job finishes, you receive a completion report. For more
 information about how to use the report to examine the job, see [Tracking job status and completion reports](batch-ops-job-status.md "batch-ops-job-status.md").


###### Prerequisites


Before creating your Batch Replication job, you must create a Batch Operations AWS Identity and Access Management
 (IAM) role to grant Amazon S3 permissions to perform actions on your behalf. For more
 information, see [Configuring an IAM role for
 S3 Batch Replication](s3-batch-replication-policies.md "s3-batch-replication-policies.md").


1. Sign in to the AWS Management Console and open the Amazon S3 console at
 [https://console.aws.amazon.com/s3/](https://console.aws.amazon.com/s3/ "https://console.aws.amazon.com/s3/").
2. In the left navigation pane, choose
 **Batch Operations**.
3. Choose **Create job**.
4. Verify that the **AWS Region** section shows the Region
 where you want to create your job.
5. In the **Manifest** section, specify the manifest format
 that you want to use. The manifest is a list of all of the objects that you
 want to run the specified action on. To learn more about Batch Operations
 manifests, see [Specifying a manifest](batch-ops-create-job.md#specify-batchjob-manifest "batch-ops-create-job.md#specify-batchjob-manifest").




	* If you have a manifest prepared, choose **S3 inventory
	 report (manifest.json)** or **CSV**.
	 If your manifest is in a versioned bucket, you can specify the
	 version ID for the manifest. If you don't specify a version ID,
	 Batch Operations uses the current version of your manifest. For more
	 information about creating a manifest, see [Specifying a manifest](batch-ops-create-job.md#specify-batchjob-manifest "batch-ops-create-job.md#specify-batchjob-manifest").
	
	
	###### Note
	
	If the objects in your manifest are in a versioned bucket, you
	 must specify the version IDs for the objects. For more
	 information, see [Specifying a manifest](batch-ops-create-job.md#specify-batchjob-manifest "batch-ops-create-job.md#specify-batchjob-manifest").
	* To create a manifest based on your replication configuration,
	 choose **Create manifest using S3 Replication
	 configuration**. Then choose the source bucket of your
	 replication configuration.
6. (Optional) If you chose **Create manifest using S3 Replication
 configuration**, you can include additional filters, such as
 the object creation date and replication status. For examples of how to
 filter by replication status, see [Specifying a manifest for a
 Batch Replication job](s3-batch-replication-batch.md#batch-replication-manifest "s3-batch-replication-batch.md#batch-replication-manifest").
7. (Optional) If you chose **Create manifest using S3 Replication
 configuration**, you can save the generated manifest. To save
 this manifest, select **Save Batch Operations manifest**. Then
 specify the destination bucket for the manifest and choose whether to
 encrypt the manifest. 


###### Note

The generated manifest must be stored in the same AWS Region as the
 source bucket.
8. Choose **Next**.
9. On the **Operations** page, choose
 **Replicate**, then choose **Next**.
10. (Optional) Provide a **Description**.
11. Adjust the **Priority** of the job if needed. Higher
 numbers indicate higher priority. Amazon S3 attempts to run higher priority jobs
 before lower priority jobs. For more information about job priority, see
 [Assigning job priority](batch-ops-job-priority.md "batch-ops-job-priority.md").
12. (Optional) Generate a completion report. To generate this report, select
 **Generate completion report**.


If you choose to generate a completion report, you must choose either to
 report **Failed tasks only** or **All
 tasks**, and provide a destination bucket for the
 report.
13. In the **Permissions** section, make sure that you choose
 an IAM role that has the required permissions for Batch Replication. One
 of the most common causes of replication failures is insufficient
 permissions in the provided IAM role. For information about creating this
 role, see [Configuring an IAM role for
 S3 Batch Replication](s3-batch-replication-policies.md "s3-batch-replication-policies.md").
14. (Optional) Add job tags to the Batch Replication job.
15. Choose **Next**.
16. Review your job configuration, and then choose **Create
 job**.
The following example `create-job` command creates an
 S3 Batch Replication job by using an S3 generated manifest for the AWS account
 ``111122223333``. This example
 replicates existing objects and objects that previously failed to replicate. For
 information about filtering by replication status, see [Specifying a manifest for a
 Batch Replication job](s3-batch-replication-batch.md#batch-replication-manifest "s3-batch-replication-batch.md#batch-replication-manifest"). 

To use this command, replace the ``user input
 placeholders`` with your own information. Replace the IAM
 role `role/`batch-Replication-IAM-policy`` with
 the IAM role that you previously created. For more information, see [Configuring an IAM role for
 S3 Batch Replication](s3-batch-replication-policies.md "s3-batch-replication-policies.md").


```
aws s3control create-job --account-id `111122223333` \ 
--operation '{"S3ReplicateObject":{}}' \ 
--report '{"Bucket":"arn:aws:s3:::`amzn-s3-demo-completion-report-bucket`",\ 
"Prefix":"`batch-replication-report`", \ 
"Format":"Report_CSV_20180820","Enabled":true,"ReportScope":"AllTasks"}' \ 
--manifest-generator '{"S3JobManifestGenerator": {"ExpectedBucketOwner": "`111122223333`", \ 
"SourceBucket": "arn:aws:s3:::``amzn-s3-demo-source-bucket``", \ 
"EnableManifestOutput": false, "Filter": {"EligibleForReplication": true, \ 
"ObjectReplicationStatuses": ["`NONE`","`FAILED`"]}}}' \ 
--priority `1` \ 
--role-arn arn:aws:iam::`111122223333`:role/`batch-Replication-IAM-policy` \ 
--no-confirmation-required \ 
--region `source-bucket-region`
```
###### Note

You must initiate the job from the same AWS Region as the replication source
 bucket. 

After you have successfully initiated a Batch Replication job, you receive the
 job ID as the response. You can monitor this job by using the following
 `describe-job` command. To use this command, replace the
 ``user input placeholders`` with your
 own information. 


```
aws s3control describe-job --account-id `111122223333` --job-id `job-id` --region `source-bucket-region`
```
The following example creates an S3 Batch Replication job by using a
 user-defined manifest for AWS account
 ``111122223333``. If the
 objects in your manifest are in a versioned bucket, you must specify the version IDs
 for the objects. Only the object with the version ID specified in the manifest will
 be replicated. For more information about creating a manifest, see [Specifying a manifest](batch-ops-create-job.md#specify-batchjob-manifest "batch-ops-create-job.md#specify-batchjob-manifest"). 

To use this command, replace the ``user input
 placeholders`` with your own information. Replace the IAM
 role `role/`batch-Replication-IAM-policy`` with
 the IAM role that you previously created. For more information, see [Configuring an IAM role for
 S3 Batch Replication](s3-batch-replication-policies.md "s3-batch-replication-policies.md").


```
aws s3control create-job --account-id `111122223333` \ 
--operation '{"S3ReplicateObject":{}}' \
--report '{"Bucket":"arn:aws:s3:::`amzn-s3-demo-completion-report-bucket`",\
"Prefix":"`batch-replication-report`", \
"Format":"Report_CSV_20180820","Enabled":true,"ReportScope":"AllTasks"}' \
--manifest '{"Spec":{"Format":"S3BatchOperations_CSV_20180820",\
"Fields":["Bucket","Key","VersionId"]},\
"Location":{"ObjectArn":"arn:aws:s3:::``amzn-s3-demo-manifest-bucket`/manifest.csv`",\
"ETag":"`Manifest Etag`"}}' \
--priority `1` \
--role-arn arn:aws:iam::`111122223333`:role/`batch-Replication-IAM-policy` \
--no-confirmation-required \
--region `source-bucket-region`
```
###### Note

You must initiate the job from the same AWS Region as the replication source
 bucket. 

After you have successfully initiated a Batch Replication job, you receive the
 job ID as the response. You can monitor this job by using the following
 `describe-job` command.


```
aws s3control describe-job --account-id `111122223333` --job-id `job-id` --region `source-bucket-region`
```
