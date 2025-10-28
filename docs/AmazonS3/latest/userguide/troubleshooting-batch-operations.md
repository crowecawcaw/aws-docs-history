# Troubleshooting S3 Batch Operations

Amazon S3 Batch Operations allows you to perform large-scale operations on Amazon S3 objects. This guide helps you troubleshoot common issues you might encounter.

To troubleshoot issues with S3 Batch Replication, see [Troubleshooting replication](replication-troubleshoot.md "replication-troubleshoot.md").

There are two primary types of failures that result in Batch operation errors:

1. **API Failure** – The requested API (such as `CreateJob`) has failed to execute.
2. **Job Failure** – The initial API request succeeded but the job failed, for example, due to issues with the manifest or permissions to objects specified in the manifest.

## NoSuchJobException

**Type**: API failure

The `NoSuchJobException` occurs when S3 Batch Operations cannot locate the specified job. This error can happen in several scenarios beyond simple job expiration. Common causes include the following.

1. **Job expiration** – Jobs are automatically deleted 90 days after reaching a terminal state (`Complete`, `Cancelled`, or `Failed`).
2. **Incorrect job ID** – The job ID used in `DescribeJob` or `UpdateJobStatus` doesn't match the ID returned by `CreateJob`.
3. **Wrong region** – Attempting to access a job in a different region than where it was created.
4. **Wrong account** – Using a job ID from a different AWS account.
5. **Job ID format errors** – Typos, extra characters, or incorrect formatting in the job ID.
6. **Timing issues** – Checking job status immediately after creation before the job is fully registered.

Related error messages include the following.

1. `No such job`
2. `The specified job does not exist`

### Best practices to prevent `NoSuchJobException` API failures

1. **Store job IDs immediately** – Save the job ID from the `CreateJob` response before making subsequent API calls.
2. **Implement retry logic** – Add exponential backoff when checking job status immediately after creation.
3. **Set up monitoring** – Create CloudWatch alarms to track job completion before the 90-day expiration. For details, see [Using CloudWatch alarms](../../../AmazonCloudWatch/latest/monitoring/AlarmThatSendsEmail.md "../../../AmazonCloudWatch/latest/monitoring/AlarmThatSendsEmail.md") in the Amazon CloudWatch User Guide.
4. **Use consistent regions** – Ensure all job operations use the same region as job creation.
5. **Validate input** – Check job ID format before making API calls.

### When jobs expire

Jobs in terminal states are automatically deleted after 90 days. To avoid losing job information, consider the following.

1. **Download completion reports before expiration** – For instructions on retrieving and storing job results, see .
2. **Archive job metadata in your own systems** – Store critical job information in your databases or monitoring systems.
3. **Set up automated notifications before the 90-day deadline** – Use Amazon EventBridge to create rules that trigger notifications when jobs complete. For more information, see [Amazon S3 Event Notifications](EventNotifications.md "EventNotifications.md").

### `NoSuchJobException` troubleshooting

1. Use the following command to verify the job exists in your account and region.

```

aws s3control list-jobs --account-id `111122223333` --region `us-east-1`

```

2. Use the following comamand to search across all job statuses. Possible job statuses include `Active`, `Cancelled`, `Cancelling`, `Complete`, `Completing`, `Failed`, `Failing`, `New`, `Paused`, `Pausing`, `Preparing`, `Ready`, and `Suspended`.

```

aws s3control list-jobs --account-id `111122223333` --job-statuses `your-job-status`

```

3. Use the following command to check if the job exists in other regions where you commonly create jobs.

```

aws s3control list-jobs --account-id `111122223333` --region `job-region-1` aws s3control list-jobs --account-id `111122223333` --region `job-region-2`

```

4. Validate the job ID format. Job IDs typically contain 36 character, such as `12345678-1234-1234-1234-123456789012`. Check for extra spaces, missing characters, or case sensitivity issues and verify you're using the complete job ID returned by the `CreateJob` command.
5. Use the following command to check CloudTrail logs for job creation events.

```

    aws logs filter-log-events --log-group-name CloudTrail/S3BatchOperations \ --filter-pattern "{ $.eventName = CreateJob }" \ --start-time `timestamp`

```

### AccessDeniedException

**Type**: API failure

The `AccessDeniedException` occurs when an S3 Batch Operations request is blocked due to insufficient permissions, unsupported operations, or policy restrictions. This is one of the most common errors in Batch Operations. It has the following common causes:

1. **Missing IAM permissions** – The IAM identity lacks required permissions for Batch Operations APIs.
2. **Insufficient S3 permissions** – Missing permissions to access source or destination buckets and objects.
3. **Job execution role issues** – The job execution role lacks permissions to perform the specified operation.
4. **Unsupported operations** – Attempting to use operations not supported in the current region or bucket type.
5. **Cross-account access issues** – Missing permissions for cross-account bucket or object access.
6. **Resource-based policy restrictions** – Bucket policies or object ACLs blocking the operation.
7. **Service Control Policy (SCP) restrictions** – Organization-level policies preventing the operation.

Related error messages:

1. `Access Denied`
2. `User: arn:aws:iam::account:user/username is not authorized to perform: s3:operation`
3. `Cross-account pass role is not allowed`
4. `The bucket policy does not allow the specified operation`

#### Best practices to prevent AccessDeniedException API failures

1. **Use least privilege principle** – Grant only the minimum permissions required for your specific operations.
2. **Test permissions before large jobs** – Run small test jobs to validate permissions before processing thousands of objects.
3. **Use IAM policy simulator** – Test policies before deployment using the IAM policy simulator. For more information, see [IAM policy testing with the IAM policy simulator](../../../IAM/latest/UserGuide/access_policies_testing-policies.md "../../../IAM/latest/UserGuide/access_policies_testing-policies.md") in the IAM User Guide.
4. **Implement proper cross-account setup** – Check your cross-account access configuration for cross-account job configurations. For more information, see [IAM tutorial: Delegate access across AWS accounts using IAM roles](../../../IAM/latest/UserGuide/tutorial_cross-account-with-roles.md "../../../IAM/latest/UserGuide/tutorial_cross-account-with-roles.md") in the IAM User Guide.
5. **Monitor permission changes** – Set up CloudTrail alerts for IAM policy modifications that might affect Batch Operations.
6. **Document role requirements** – Maintain clear documentation of required permissions for each job type.
7. **Use common permission templates** - Use the permission examples and polcy templates:
   1. [Granting permissions for Batch Operations](batch-ops-iam-role-policies.md "batch-ops-iam-role-policies.md")
   2. [Cross account resources in IAM](../../../IAM/latest/UserGuide/access_policies-cross-account-resource-access.md "../../../IAM/latest/UserGuide/access_policies-cross-account-resource-access.md") in the IAM User Guide.
   3. [Control access to VPC endpoints using endpoint policies](../../../vpc/latest/privatelink/vpc-endpoints-access.md "../../../vpc/latest/privatelink/vpc-endpoints-access.md") in the AWS PrivateLink Guide.

#### AccessDeniedException troubleshooting

Follow these steps systematically to identify and resolve permission issues.

1. Check [Operations supported by S3 Batch Operations](batch-ops-operations.md "batch-ops-operations.md") for supported operations by region. Confirm directory bucket operations are only available at Regional and Zonal endpoints. Verify the operation is supported for your bucket's storage class.
2. Use the following command to determine if you can list jobs.

```

 aws s3control list-jobs --account-id `111122223333`

```

3. Use the following command to check IAM permissions for the requesting identity. The account running the job needs the following permissions: `s3:CreateJob`, `s3:DescribeJob`, `s3:ListJobs-s3:UpdateJobPriority`, `s3:UpdateJobStatus-iam:PassRole`.

```

aws sts get-caller-identity `111122223333`

```

4. Use the following command to check if the role exists and is assumable.

```

aws iam get-role --role-name `role-name`

```

5. Use the following command to review the role's trust policy. The role running the job must have the following:
   1. A trust relationship allowing `batchoperations.s3.amazonaws.com` to assume the role.
   2. The operations the batch operation is performing (such as `s3:PutObjectTagging` for tagging operations).
   3. Access to the source and destination buckets.
   4. Permission to read the manifest file.
   5. Permission to write completion reports.

```

aws iam get-role --role-name `role-name` --query 'Role.AssumeRolePolicyDocument'

```

6. Use the following command to rest access to the manifest and source buckets.

```

aws s3 ls s3://`bucket-name`

```

7. Test the operation being performed by the batch operation. For example, if the batch operation performs tagging, tag a sample object in the source bucket.
8. Review bucket policies for polcies that might deny the operation.
   1. Check object ACLs if working with legacy access controls.
   2. Verify no Service Control Policies (SCPs) are blocking the operation.
   3. Confirm VPC endpoint policies allow Batch Operations if using VPC endpoints.

9. Use the following command to use CloudTrail to identify permission failures.

```

aws logs filter-log-events --log-group-name CloudTrail/S3BatchOperations \
    --filter-pattern "{ $.errorCode = AccessDenied }" \
    --start-time `timestamp`

```

#### SlowDownError

**Type**: API failure

The `SlowDownError` exception occurs when your account has exceeded the request rate limit for S3 Batch Operations APIs. This is a throttling mechanism to protect the service from being overwhelmed by too many requests. It has the following common causes:

1. **High API request frequency** – Making too many API calls in a short time period.
2. **Concurrent job operations** – Multiple applications or users creating/managing jobs simultaneously.
3. **Automated scripts without rate limiting** – Scripts that don't implement proper backoff strategies.
4. **Polling job status too frequently** – Checking job status more often than necessary.
5. **Burst traffic patterns** – Sudden spikes in API usage during peak processing times.
6. **Regional capacity limits** – Exceeding the allocated request capacity for your region.

Related error messages:

1. `SlowDown`
2. `Please reduce your request rate`
3. `Request rate exceeded`

#### Best practices to prevent SlowDownError API failures

1. **Implement client-side rate limiting** – Add delays between API calls in your applications.
2. **Use exponential backoff with jitter** – Randomize retry delays to avoid thundering herd problems.
3. **Set up proper retry logic** – Implement automatic retries with increasing delays for transient errors.
4. **Use event-driven architectures** – Replace polling with EventBridge notifications for job status changes.
5. **Distribute load across time** – Stagger job creation and status checks across different time periods.
6. **Monitor and alert on rate limits** – Set up CloudWatch alarms to detect when you're approaching limits.

Most AWS SDKs include built-in retry logic for rate limiting errors. Configure them as follows:

1. **AWS CLI** – Use `cli-read-timeout` and `cli-connect-timeout` parameters.
2. **AWS SDK for Python (Boto3)** – Configure retry modes and max attempts in your client configuration.
3. **AWS SDK for Java** – Use `RetryPolicy` and `ClientConfiguration` settings.
4. **AWS SDK for JavaScript** – Configure `maxRetries` and `retryDelayOptions`.

For more information about retry patterns and best practices, see [Retry with backoff pattern](../../../prescriptive-guidance/latest/cloud-design-patterns/retry-backoff.md "../../../prescriptive-guidance/latest/cloud-design-patterns/retry-backoff.md") in the AWS Prescriptive Guidance guide.

#### SlowDownError troubleshooting

1. In your code, implement exponential backoff immediately.

###### Example of exponential backoff in bash

```

for attempt in {1..5}; do
    if aws s3control describe-job --account-id `111122223333` --job-id `job-id`; then
        break
    else
        wait_time=$((2**attempt)) echo "Rate limited, waiting ${wait_time} seconds..." sleep $wait_time
        fi
done

```

2. Use CloudTrail to identify the source of high request volume.

```

aws logs filter-log-events \
    --log-group-name CloudTrail/S3BatchOperations \
    --filter-pattern "{ $.eventName = CreateJob || $.eventName = DescribeJob }" \
    --start-time `timestamp` \
    --query 'events[*].[eventTime,sourceIPAddress,userIdentity.type,eventName]'

```

3. Review polling frequency.
   1. Avoid checking job status more than once every 30 seconds for active jobs.
   2. Use job completion notifications instead of polling when possible.
   3. Implement jitter in your polling intervals to avoid synchronized requests.

4. Optimize your API usage patterns.
   1. Batch multiple operations when possible.
   2. Use `ListJobs` to get status of multiple jobs in one call.
   3. Cache job information to reduce redundant API calls.
   4. Spread job creation across time rather than creating many jobs simultaneously.

5. Use CloudWatch metrics for API calls to monitor your request patterns.

```

   aws logs put-metric-filter \
       --log-group-name CloudTrail/S3BatchOperations \
       --filter-name S3BatchOpsAPICallCount \
       --filter-pattern "{ $.eventSource = s3.amazonaws.com && $.eventName = CreateJob }" \
       --metric-transformations \
       metricName=S3BatchOpsAPICalls,metricNamespace=Custom/S3BatchOps,metricValue=1

```

## InvalidManifestContent

**Type**: Job failure

The `InvalidManifestContent` exception occurs when there are issues with the manifest file format, content, or structure that prevent S3 Batch Operations from processing the job. It has the following common causes:

1. **Format violations** – Missing required columns, incorrect delimiters, or malformed CSV structure.
2. **Content encoding issues** – Incorrect character encoding, BOM markers, or non-UTF-8 characters.
3. **Object key problems** – Invalid characters, improper URL encoding, or keys exceeding length limits.
4. **Size limitations** – Manifest contains more objects than the operation supports.
5. **Version ID format errors** – Malformed or invalid version IDs for versioned objects.
6. **ETag format issues** – Incorrect ETag format or missing quotes for operations that require ETags.
7. **Inconsistent data** – Mixed formats within the same manifest or inconsistent column counts.

Related error messages:

1. `Required fields are missing in the schema: + missingFields`
2. `Invalid Manifest Content`
3. `The S3 Batch Operations job failed because it contains more keys than the maximum allowed in a single job`
4. `Invalid object key format`
5. `Manifest file is not properly formatted`
6. `Invalid version ID format`
7. `ETag format is invalid`

### Best practices to prevent InvalidManifestContent job failures

1. **Validate before upload** – Test manifest format with small jobs before processing large datasets.
2. **Use consistent encoding** – Always use UTF-8 encoding without BOM for manifest files.
3. **Implement manifest generation standards** – Create templates and validation procedures for manifest creation.
4. **Handle special characters properly** – URL encode object keys that contain special characters.
5. **Monitor object counts** – Track manifest size and split large jobs proactively.
6. **Validate object existence** – Verify objects exist before including them in manifests.
7. **Use AWS tools for manifest generation** – Leverage AWS CLI `s3api list-objects-v2` to generate properly formatted object lists.

Common manifest issues and solutions:

1. **Missing required columns** – Ensure your manifest includes all required columns for your operation type. The most common missing columns are Bucket and Key.
2. **Incorrect CSV format** – Use comma delimiters, ensure consistent column counts across all rows, and avoid embedded line breaks within fields.
3. **Special characters in object keys** – URL encode object keys that contain spaces, Unicode characters, or XML special characters (<, >, &, ", ').
4. **Large manifest files** – Split manifests with more than the operation limit into multiple smaller manifests and create separate jobs.
5. **Invalid version IDs** – Ensure version IDs are properly formatted alphanumeric strings. Remove version ID column if not needed.
6. **Encoding issues** – Save manifest files as UTF-8 without BOM. Avoid copying manifests through systems that might alter encoding.

For detailed manifest format specifications and examples, see the following:

1. [Specifying a manifest](batch-ops-create-job.md#specify-batchjob-manifest "batch-ops-create-job.md#specify-batchjob-manifest")
2. [Operations supported by S3 Batch Operations](batch-ops-operations.md "batch-ops-operations.md")
3. [Naming Amazon S3 objects](object-keys.md "object-keys.md")

### InvalidManifestContent troubleshooting

1.  Download and inspect the manifest file. Manually verify the manifest meets format requirements:

        1. CSV format with comma delimiters.
        2. UTF-8 encoding without BOM.
        3. Consistent number of columns across all rows.
        4. No empty lines or trailing spaces.
        5. Object keys properly URL encoded if they contain special characters.

    Use the following command to download the manifest file.

```

aws s3 cp s3://`amzn-s3-demo-bucket1`/`manifest-key` `./manifest.csv`

```

2. Check required columns for your operation:
   1. All operations: `Bucket`, `Key`
   2. Copy operations: `VersionId` (optional)
   3. Restore operations: `VersionId` (optional)
   4. Replace tag operations: No additional columns required.
   5. Replace ACL operations: No additional columns required.
   6. Initiate restore: `VersionId` (optional)

3. Check object count limits:
   1. Copy: 1 billion objects maximum.
   2. Delete: 1 billion objects maximum.
   3. Restore: 1 billion objects maximum.
   4. Tagging: 1 billion objects maximum.
   5. ACL: 1 billion objects maximum.

4. Create a test manifest with a few objects from your orginial manifest.
5. Use the following command to cehck if a sample of objects from the manifest exist.

```

aws s3 ls s3://`amzn-s3-demo-bucket1`/`object-key`

```

6. Check job failure details and review the failure reason and any specific error details in the job description.

```

aws s3control describe-job --account-id `111122223333` --job-id `job-id`

```
