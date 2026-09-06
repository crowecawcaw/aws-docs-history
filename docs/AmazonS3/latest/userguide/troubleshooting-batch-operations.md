

# Troubleshooting S3 Batch Operations
<a name="troubleshooting-batch-operations"></a>

Amazon S3 Batch Operations allows you to perform large-scale operations on Amazon S3 objects. This guide helps you troubleshoot common issues you might encounter.

To troubleshoot issues with S3 Batch Replication, see [Troubleshooting replication](replication-troubleshoot.md).

There are two primary types of failures that result in Batch operation errors:

1. **API Failure** – The requested API (such as `CreateJob`) has failed to execute.

1. **Job Failure** – The initial API request succeeded but the job failed, for example, due to issues with the manifest or permissions to objects specified in the manifest.

## NoSuchJobException
<a name="nosuchjobexception"></a>

**Type**: API failure

The `NoSuchJobException` occurs when S3 Batch Operations cannot locate the specified job. This error can happen in several scenarios beyond simple job expiration. Common causes include the following.

1. **Job expiration** – Jobs are automatically deleted 90 days after reaching a terminal state (`Complete`, `Cancelled`, or `Failed`).

1. **Incorrect job ID** – The job ID used in `DescribeJob` or `UpdateJobStatus` doesn't match the ID returned by `CreateJob`.

1. **Wrong region** – Attempting to access a job in a different region than where it was created.

1. **Wrong account** – Using a job ID from a different AWS account.

1. **Job ID format errors** – Typos, extra characters, or incorrect formatting in the job ID.

1. **Timing issues** – Checking job status immediately after creation before the job is fully registered.

Related error messages include the following.

1. `No such job`

1. `The specified job does not exist`

### Best practices to prevent `NoSuchJobException` API failures
<a name="nosuchjobexception-prevention"></a>

1. **Store job IDs immediately** – Save the job ID from the `CreateJob` response before making subsequent API calls.

1. **Implement retry logic** – Add exponential backoff when checking job status immediately after creation.

1. **Set up monitoring** – Create CloudWatch alarms to track job completion before the 90-day expiration. For details, see [Using CloudWatch alarms](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/AlarmThatSendsEmail.html) in the Amazon CloudWatch User Guide.

1. **Use consistent regions** – Ensure all job operations use the same region as job creation.

1. **Validate input** – Check job ID format before making API calls.

### When jobs expire
<a name="nosuchjobexception-jobs-expire"></a>

Jobs in terminal states are automatically deleted after 90 days. To avoid losing job information, consider the following.

1. **Download completion reports before expiration** – For instructions on retrieving and storing job results, see [Completion reports](batch-ops-job-status.md#batch-ops-completion-report).

1. **Archive job metadata in your own systems** – Store critical job information in your databases or monitoring systems.

1. **Set up automated notifications before the 90-day deadline** – Use Amazon EventBridge to create rules that trigger notifications when jobs complete. For more information, see [Amazon S3 Event Notifications](EventNotifications.md).

### `NoSuchJobException` troubleshooting
<a name="nosuchjobexception-troubleshooting"></a>

1. Use the following command to verify the job exists in your account and region.

   ```
   aws s3control list-jobs --account-id {{111122223333}} --region {{us-east-1}}
   ```

1. Use the following command to search across all job statuses. Possible job statuses include `Active`, `Cancelled`, `Cancelling`, `Complete`, `Completing`, `Failed`, `Failing`, `New`, `Paused`, `Pausing`, `Preparing`, `Ready`, and `Suspended`.

   ```
   aws s3control list-jobs --account-id {{111122223333}} --job-statuses {{your-job-status}}
   ```

1. Use the following command to check if the job exists in other regions where you commonly create jobs.

   ```
   aws s3control list-jobs --account-id {{111122223333}} --region {{job-region-1}} aws s3control list-jobs --account-id {{111122223333}} --region {{job-region-2}}                    
   ```

1. Validate the job ID format. Job IDs typically contain 36 character, such as `12345678-1234-1234-1234-123456789012`. Check for extra spaces, missing characters, or case sensitivity issues and verify you're using the complete job ID returned by the `CreateJob` command.

1. Use the following command to check CloudTrail logs for job creation events.

   ```
       aws logs filter-log-events --log-group-name CloudTrail/S3BatchOperations \ --filter-pattern "{ $.eventName = CreateJob }" \ --start-time {{timestamp}}                    
   ```

### AccessDeniedException
<a name="accessdeniedexception"></a>

**Type**: API failure

The `AccessDeniedException` occurs when an S3 Batch Operations request is blocked due to insufficient permissions, unsupported operations, or policy restrictions. This is one of the most common errors in Batch Operations. It has the following common causes:

1. **Missing IAM permissions** – The IAM identity lacks required permissions for Batch Operations APIs.

1. **Insufficient S3 permissions** – Missing permissions to access source or destination buckets and objects.

1. **Job execution role issues** – The job execution role lacks permissions to perform the specified operation.

1. **Unsupported operations** – Attempting to use operations not supported in the current region or bucket type.

1. **Cross-account access issues** – Missing permissions for cross-account bucket or object access.

1. **Resource-based policy restrictions** – Bucket policies or object ACLs blocking the operation.

1. **Service Control Policy (SCP) restrictions** – Organization-level policies preventing the operation.

Related error messages:

1. `Access Denied`

1. `User: arn:aws:iam::account:user/username is not authorized to perform: s3:operation`

1. `Cross-account pass role is not allowed`

1. `The bucket policy does not allow the specified operation`

#### Best practices to prevent AccessDeniedException API failures
<a name="accessdeniedexception-prevention"></a>

1. **Use least privilege principle** – Grant only the minimum permissions required for your specific operations.

1. **Test permissions before large jobs** – Run small test jobs to validate permissions before processing thousands of objects.

1. **Use IAM policy simulator** – Test policies before deployment using the IAM policy simulator. For more information, see [IAM policy testing with the IAM policy simulator](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_testing-policies.html) in the IAM User Guide.

1. **Implement proper cross-account setup** – Check your cross-account access configuration for cross-account job configurations. For more information, see [IAM tutorial: Delegate access across AWS accounts using IAM roles](https://docs.aws.amazon.com/IAM/latest/UserGuide/tutorial_cross-account-with-roles.html) in the IAM User Guide.

1. **Monitor permission changes** – Set up CloudTrail alerts for IAM policy modifications that might affect Batch Operations.

1. **Document role requirements** – Maintain clear documentation of required permissions for each job type.

1. **Use common permission templates** - Use the permission examples and policy templates:

   1. [Granting permissions for Batch Operations](batch-ops-iam-role-policies.md)

   1. [Cross account resources in IAM](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies-cross-account-resource-access.html) in the IAM User Guide.

   1. [Control access to VPC endpoints using endpoint policies](https://docs.aws.amazon.com/vpc/latest/privatelink/vpc-endpoints-access.html) in the AWS PrivateLink Guide.

#### AccessDeniedException troubleshooting
<a name="accessdeniedexception-troubleshooting"></a>

Follow these steps systematically to identify and resolve permission issues.

1. Check [Operations supported by S3 Batch Operations](batch-ops-operations.md) for supported operations by region. Confirm directory bucket operations are only available at Regional and Zonal endpoints. Verify the operation is supported for your bucket's storage class.

1. Use the following command to determine if you can list jobs.

   ```
    aws s3control list-jobs --account-id {{111122223333}}
   ```

1. Use the following command to check IAM permissions for the requesting identity. The account running the job needs the following permissions: `s3:CreateJob`, `s3:DescribeJob`, `s3:ListJobs`, `s3:UpdateJobPriority`, `s3:UpdateJobStatus`, and `iam:PassRole`.

   ```
   aws sts get-caller-identity {{111122223333}}
   ```

1. Use the following command to check if the role exists and is assumable.

   ```
   aws iam get-role --role-name {{role-name}}
   ```

1. Use the following command to review the role's trust policy. The role running the job must have the following:

   1. A trust relationship allowing `batchoperations.s3.amazonaws.com` to assume the role.

   1. The operations the batch operation is performing (such as `s3:PutObjectTagging` for tagging operations).

   1. Access to the source and destination buckets.

   1. Permission to read the manifest file.

   1. Permission to write completion reports.

   ```
   aws iam get-role --role-name {{role-name}} --query 'Role.AssumeRolePolicyDocument'
   ```

1. Use the following command to test access to the manifest and source buckets.

   ```
   aws s3 ls s3://{{amzn-s3-demo-bucket}}                        
   ```

1. Test the operation being performed by the batch operation. For example, if the batch operation performs tagging, tag a sample object in the source bucket.

1. Review bucket policies for policies that might deny the operation.

   1. Check object ACLs if working with legacy access controls.

   1. Verify no Service Control Policies (SCPs) are blocking the operation.

   1.  Confirm VPC endpoint policies allow Batch Operations if using VPC endpoints.

1. Use the following command to use CloudTrail to identify permission failures.

   ```
   aws logs filter-log-events --log-group-name CloudTrail/S3BatchOperations \
       --filter-pattern "{ $.errorCode = AccessDenied }" \
       --start-time {{timestamp}}
   ```

#### SlowDownError
<a name="slowdownerror"></a>

**Type**: API failure

The `SlowDownError` exception occurs when your account has exceeded the request rate limit for S3 Batch Operations APIs. This is a throttling mechanism to protect the service from being overwhelmed by too many requests. It has the following common causes:

1. **High API request frequency** – Making too many API calls in a short time period.

1. **Concurrent job operations** – Multiple applications or users creating/managing jobs simultaneously.

1. **Automated scripts without rate limiting** – Scripts that don't implement proper backoff strategies.

1. **Polling job status too frequently** – Checking job status more often than necessary.

1. **Burst traffic patterns** – Sudden spikes in API usage during peak processing times.

1. **Regional capacity limits** – Exceeding the allocated request capacity for your region.

Related error messages:

1. `SlowDown`

1. `Please reduce your request rate`

1. `Request rate exceeded`

#### Best practices to prevent SlowDownError API failures
<a name="slowdownerror-prevention"></a>

1. **Implement client-side rate limiting** – Add delays between API calls in your applications.

1. **Use exponential backoff with jitter** – Randomize retry delays to avoid thundering herd problems.

1. **Set up proper retry logic** – Implement automatic retries with increasing delays for transient errors.

1. **Use event-driven architectures** – Replace polling with EventBridge notifications for job status changes.

1. **Distribute load across time** – Stagger job creation and status checks across different time periods.

1. **Monitor and alert on rate limits** – Set up CloudWatch alarms to detect when you're approaching limits.

Most AWS SDKs include built-in retry logic for rate limiting errors. Configure them as follows:

1. **AWS CLI** – Use `cli-read-timeout` and `cli-connect-timeout` parameters.

1. **AWS SDK for Python (Boto3)** – Configure retry modes and max attempts in your client configuration.

1. **AWS SDK for Java** – Use `RetryPolicy` and `ClientConfiguration` settings.

1. **AWS SDK for JavaScript** – Configure `maxRetries` and `retryDelayOptions`.

For more information about retry patterns and best practices, see [Retry with backoff pattern](https://docs.aws.amazon.com/prescriptive-guidance/latest/cloud-design-patterns/retry-backoff.html) in the AWS Prescriptive Guidance guide.

#### SlowDownError troubleshooting
<a name="slowdownerror-troubleshooting"></a>

1. In your code, implement exponential backoff immediately.  
**Example of exponential backoff in bash**  

   ```
   for attempt in {1..5}; do
       if aws s3control describe-job --account-id {{111122223333}} --job-id {{job-id}}; then 
           break
       else 
           wait_time=$((2**attempt)) echo "Rate limited, waiting ${wait_time} seconds..." sleep $wait_time
           fi
   done
   ```

1. Use CloudTrail to identify the source of high request volume.

   ```
   aws logs filter-log-events \
       --log-group-name CloudTrail/S3BatchOperations \
       --filter-pattern "{ $.eventName = CreateJob || $.eventName = DescribeJob }" \
       --start-time {{timestamp}} \
       --query 'events[*].[eventTime,sourceIPAddress,userIdentity.type,eventName]'
   ```

1. Review polling frequency.

   1. Avoid checking job status more than once every 30 seconds for active jobs.

   1. Use job completion notifications instead of polling when possible.

   1. Implement jitter in your polling intervals to avoid synchronized requests.

1. Optimize your API usage patterns.

   1. Batch multiple operations when possible.

   1. Use `ListJobs` to get status of multiple jobs in one call.

   1. Cache job information to reduce redundant API calls.

   1. Spread job creation across time rather than creating many jobs simultaneously.

1. Use CloudWatch metrics for API calls to monitor your request patterns.

   ```
      aws logs put-metric-filter \
          --log-group-name CloudTrail/S3BatchOperations \
          --filter-name S3BatchOpsAPICallCount \      
          --filter-pattern "{ $.eventSource = s3.amazonaws.com && $.eventName = CreateJob }" \
          --metric-transformations \        
          metricName=S3BatchOpsAPICalls,metricNamespace=Custom/S3BatchOps,metricValue=1
   ```

## InvalidManifestContent
<a name="invalidmanifestcontent"></a>

**Type**: Job failure

The `InvalidManifestContent` exception occurs when there are issues with the manifest file format, content, or structure that prevent S3 Batch Operations from processing the job. It has the following common causes:

1. **Format violations** – Missing required columns, incorrect delimiters, or malformed CSV structure.

1. **Content encoding issues** – Incorrect character encoding, BOM markers, or non-UTF-8 characters.

1. **Object key problems** – Invalid characters, improper URL encoding, or keys exceeding length limits.

1. **Size limitations** – Manifest contains more objects than the operation supports.

1. **Version ID format errors** – Malformed or invalid version IDs for versioned objects.

1. **ETag format issues** – Incorrect ETag format or missing quotes for operations that require ETags.

1. **Inconsistent data** – Mixed formats within the same manifest or inconsistent column counts.

Related error messages:

1. `Required fields are missing in the schema: + missingFields`

1. `Invalid Manifest Content`

1. `The S3 Batch Operations job failed because it contains more keys than the maximum allowed in a single job`

1. `Invalid object key format`

1. `Manifest file is not properly formatted`

1. `Invalid version ID format`

1. `ETag format is invalid`

### Best practices to prevent InvalidManifestContent job failures
<a name="invalidmanifestcontent-prevention"></a>

1. **Validate before upload** – Test manifest format with small jobs before processing large datasets.

1. **Use consistent encoding** – Always use UTF-8 encoding without BOM for manifest files.

1. **Implement manifest generation standards** – Create templates and validation procedures for manifest creation.

1. **Handle special characters properly** – URL encode object keys that contain special characters.

1. **Monitor object counts** – Track manifest size and split large jobs proactively.

1. **Validate object existence** – Verify objects exist before including them in manifests.

1. **Use AWS tools for manifest generation** – Leverage AWS CLI `s3api list-objects-v2` to generate properly formatted object lists.

Common manifest issues and solutions:

1. **Missing required columns** – Ensure your manifest includes all required columns for your operation type. The most common missing columns are Bucket and Key.

1. **Incorrect CSV format** – Use comma delimiters, ensure consistent column counts across all rows, and avoid embedded line breaks within fields.

1. **Special characters in object keys** – URL encode object keys that contain spaces, Unicode characters, or XML special characters (<, >, &, ", ').

1. **Large manifest files** – Split manifests with more than the operation limit into multiple smaller manifests and create separate jobs.

1. **Invalid version IDs** – Ensure version IDs are properly formatted alphanumeric strings. Remove version ID column if not needed.

1. **Encoding issues** – Save manifest files as UTF-8 without BOM. Avoid copying manifests through systems that might alter encoding.

For detailed manifest format specifications and examples, see the following:

1. [Specifying a manifest](batch-ops-create-job.md#specify-batchjob-manifest)

1. [Operations supported by S3 Batch Operations](batch-ops-operations.md)

1. [Naming Amazon S3 objects](object-keys.md)

### InvalidManifestContent troubleshooting
<a name="invalidmanifestcontent-troubleshooting"></a>

1. Download and inspect the manifest file. Manually verify the manifest meets format requirements:

   1. CSV format with comma delimiters.

   1. UTF-8 encoding without BOM.

   1. Consistent number of columns across all rows.

   1. No empty lines or trailing spaces.

   1. Object keys properly URL encoded if they contain special characters.

   Use the following command to download the manifest file.

   ```
   aws s3 cp s3://{{amzn-s3-demo-bucket1}}/{{manifest-key}} {{./manifest.csv}} 
   ```

1. Check required columns for your operation:

   1. All operations: `Bucket`, `Key`

   1. Copy operations: `VersionId` (optional)

   1. Restore operations: `VersionId` (optional)

   1. Replace tag operations: No additional columns required.

   1. Replace ACL operations: No additional columns required.

   1. Initiate restore: `VersionId` (optional)

1. Check object count limits:

   1. Copy: 1 billion objects maximum.

   1. Delete: 1 billion objects maximum.

   1. Restore: 1 billion objects maximum.

   1. Tagging: 1 billion objects maximum.

   1. ACL: 1 billion objects maximum.

1. Create a test manifest with a few objects from your original manifest.

1. Use the following command to check if a sample of objects from the manifest exist.

   ```
   aws s3 ls s3://{{amzn-s3-demo-bucket1}}/{{object-key}}
   ```

1. Check job failure details and review the failure reason and any specific error details in the job description.

   ```
   aws s3control describe-job --account-id {{111122223333}} --job-id {{job-id}}                        
   ```