

# Troubleshooting
<a name="troubleshooting"></a>

The following topics can help you troubleshoot issues that you encounter when using HealthOmics workflows and data stores.

**Topics**
+ [Troubleshooting workflows](#error-workflows)
+ [Troubleshooting call caching issues](#workflow-cache-troubleshooting)
+ [Troubleshooting data stores](#error-datastores)
+ [Troubleshooting with Kiro CLI](#kiro-cli-troubleshooting)

## Troubleshooting workflows
<a name="error-workflows"></a>

**Topics**
+ [How do I troubleshoot a failed run?](#troubleshooting-run-fail)
+ [How do I troubleshoot a failed task?](#troubleshooting-task-fail)
+ [Where do I find the engine logs?](#troubleshooting-engine-logs)
+ [How can I reduce the input parameter size for a workflow?](#troubleshooting-input-file-size)
+ [Why is my run not completing?](#troubleshooting-unresponsive-runs)

### How do I troubleshoot a failed run?
<a name="troubleshooting-run-fail"></a>

Use the **GetRun** API operation to retrieve the failure reason. For more information, see [Run failure reasons](workflows-run-errors.md).

### How do I troubleshoot a failed task?
<a name="troubleshooting-task-fail"></a>

Review the error code from the task failure message to understand the failure. Review the task logs in CloudWatch to see detailed logging messages for the task. If you aren’t getting detailed log messages, you can revise your workflow to output additional log statements. For more information, see [Monitoring HealthOmics with CloudWatch Logs](monitoring-cloudwatch-logs.md).

### Where do I find the engine logs?
<a name="troubleshooting-engine-logs"></a>

HealthOmics publishes engine logs to CloudWatch in near real-time for all runs (successful and failed). Engine logs are also delivered to your Amazon S3 bucket after the run completes. For more information, see [Monitoring HealthOmics with CloudWatch Logs](monitoring-cloudwatch-logs.md) and [Logs in Amazon S3](monitoring-cloudwatch-logs.md#s3-logs).

### How can I reduce the input parameter size for a workflow?
<a name="troubleshooting-input-file-size"></a>

You can specify up to 50 KB of input parameters for a workflow. You can use directory imports or sample sheets to remain within this size constraint. For more information, see [Managing run parameters size](workflows-run-inputs.md#run-input-file-options).

### Why is my run not completing?
<a name="troubleshooting-unresponsive-runs"></a>

If there are issues with your code and the processes have not exited properly, your run could become unresponsive or “stuck”. For more information on how to prevent and catch unresponsive runs, see [Guidance for unresponsive runs](workflows-run-errors.md#workflows-guidance-unresponsive-runs).

## Troubleshooting call caching issues
<a name="workflow-cache-troubleshooting"></a>

The following topics can help you troubleshoot issues that you encounter with call caching.

**Topics**
+ [Why isn’t my run saving to the cache?](#troubleshooting-did-run-cache)
+ [Why isn’t a task using the cache entry?](#troubleshooting-did-run-cache)
+ [Why is the call caching for a task disabled?](#troubleshooting-task-cache-disabled)

### Why isn’t my run saving to the cache?
<a name="troubleshooting-did-run-cache"></a>

1. Verify that the run is configured to use a cache by checking the cacheId field in the GetRun API operation response. Using the CLI, run this command: `aws omics get-run —id <run_id>`.

1. If the run was successful, verify the cache behavior returned in the GetRun response is CACHE\_ALWAYS. If the cache behavior is set to CACHE\_ON\_FAILURE, runs will only save to the cache when they fail.

### Why isn’t a task using the cache entry?
<a name="troubleshooting-did-run-cache"></a>

In the `/aws/omics/WorkflowLog` CloudWatch log group, open the log stream for the run cache: **runCache/<cache\_id>/<cache\_uuid>**.

1. Verify that a previous run created a cache entry for the task that you expected to be cached. Runs that have saved to the cache will be recorded with a log message of CACHE\_ENTRY\_CREATED. 

1. Locate the CACHE\_MISS log for the task and run that completed. If there is no log entry, check that the run was configured to use the cache.

1. If a cache entry was created, verify that the CPUs, memory, GPUs and container digest are identical for both tasks. The task ARN for the task that created the cache entry is in the log message.

1. If the compute requirements for both tasks match, verify that the inputs have not changed between the tasks. To do this, open the engine logs. Engine logs are available in CloudWatch Log Group /aws/omics/WorkflowLog for all runs. They are also available in the output directory of the run after completion.

### Why is the call caching for a task disabled?
<a name="troubleshooting-task-cache-disabled"></a>

Check if the task is configured to opt out of caching using workflow engine features:
+ For WDL workflows: Check if the task has volatile set to `true` in the meta section
+ For Nextflow workflows: Check if the task has cache directive set to `false`
+ For CWL workflows: Check if the task has enableReuse set to `false` for the WorkReuse feature

## Troubleshooting data stores
<a name="error-datastores"></a>

**Topics**
+ [Why is S3 GetObject failing on my read set?](#sequence-store-s3-getobject-failing)
+ [Why can't I see my annotation store or variant store in Athena?](#athena-troubleshooting)
+ [Why can't I access my data store in Athena?](#athena-engine-troubleshooting)

### Why is S3 GetObject failing on my read set?
<a name="sequence-store-s3-getobject-failing"></a>

Most commonly, the failure is due to a missing permission. Sequence store S3 reading permission is a bi-directional configuration requiring both the sequence store S3 access policy to allow access and the IAM principal to have a policy attached allowing access. For more detail on the policy requirements see [Permissions for data access using Amazon S3 URIs](s3-sharing.md). Check that the following configurations are in place:
+ The sequence store S3 access policy has explicitly allowed access to the IAM principal or the root of the principal’s account.
+ Check that the IAM principal has a policy explicitly providing permission to the resource being accessed. Note that the IAM principal policy must use the Access Point ARN and not the Access point Alias based path when defining permissions and that the ARN is in the condition and not used to specify a resource. 
+ If your store uses a customer managed key (CMK-KMS), ensure that the IAM principal has kms:decrypt permissions on the key. See the KMS [cross-account access guide](https://docs.aws.amazon.com/kms/latest/developerguide/key-policy-modifying-external-accounts.html) for configuring usage across accounts. 

If you have a policy that's using tag based access controls, ensure the following:
+ Ensure that the sequence store has finished synchronizing the tags. For this, the store’s status needs to be **active** and not **updating**. 
+ Ensure that there are no typos in the tag key or key value on the read set and the policy. 

### Why can't I see my annotation store or variant store in Athena?
<a name="athena-troubleshooting"></a>

In Lake Formation, be sure to create a resource link based on the store that was shared with you. Once you create a resource link that you have permission to access, the store should be visible in Athena. For more information, see [Configuring Lake Formation to use HealthOmics](setting-up-lf.md). 

### Why can't I access my data store in Athena?
<a name="athena-engine-troubleshooting"></a>

If your annotation or variant store is visible but you are receiving an error message saying that access is denied, check which query engine version you're using. Only queries run using engine version 3 are supported. To read more about Athena query engine versions, see the [Amazon Athena documentation](https://docs.aws.amazon.com/athena/latest/ug/engine-versions-changing.html). 

## Troubleshooting with Kiro CLI
<a name="kiro-cli-troubleshooting"></a>

[Kiro CLI](https://docs.aws.amazon.com/kiro/latest/userguide/what-is.html) can help streamline your troubleshooting process by:
+ Analyzing workflow runs and debug task failures
+ Collecting relevant logs and error messages
+ Creating AWS Support cases with all necessary debugging logs attached
+ Redacts personal identifiable information (PII) from information submitted to AWS Support

For more information about using Kiro CLI with AWS HealthOmics for troubleshooting and creating support cases, see the [HealthOmics Agentic generative AI tutorial](https://github.com/aws-samples/aws-healthomics-tutorials/tree/main/generative-ai) on GitHub.

**Warning**  
When working with Kiro CLI, review all generated content and proposed actions before proceeding. Provide feedback to improve response quality and to match your workflow’s requirements. For more information, see [ Security considerations and best practices](https://docs.aws.amazon.com/kiro/latest/userguide/command-line-chat-security.html) for Kiro.