

# Troubleshooting
<a name="model-customize-mtrl-troubleshooting"></a>

If your training job fails or behaves unexpectedly, the following sections can help you identify and resolve the issue. Checking your job status can help narrow down whether the issue is in your configuration or your agent, and the agent-specific sections below cover logs and common issues for each deployment path.

## Job level debugging
<a name="model-customize-mtrl-troubleshooting-job"></a>

Use the `DescribeJob` API to check your job's current status and see why it failed. The response includes the job's status, a failure reason if the job has failed, and a timeline of status transitions that shows how far the job progressed before the issue occurred.

```
aws sagemaker describe-job \
  --job-name "my-agent-rft-job" \
  --job-category AgentRFT \
  --region us-west-2
```

Key fields to check:
+ **JobStatus:** Current state (`InProgress`, `Completed`, `Failed`, `Stopping`, `Stopped`)
+ **SecondaryStatus:** More granular phase (`Starting`, `Downloading`, `Training`, `Uploading`)
+ **FailureReason:** If the job failed, a description of why
+ **SecondaryStatusTransitions:** Full timeline of status changes with timestamps

**Job CloudWatch logs**

Training progress and rollout-level information is logged to the following log group in your account:

```
/aws/sagemaker/Job/AgentRFT
```

The log stream name is `<job-name>/`.

These logs capture training step progress, rollout invocation events, and high-level errors. They can be helpful for understanding how far your job progressed and whether rollouts are being invoked successfully.

If your job fails, check the `FailureReason` field for details. If it fails during the `Training` phase, the issue could likely be in your agent. In this case, check your agent logs for more information.

## Agent level debugging
<a name="model-customize-mtrl-troubleshooting-agent"></a>

### Amazon Bedrock AgentCore debugging
<a name="model-customize-mtrl-troubleshooting-agent-agentcore"></a>

If you have deployed your agent to Amazon Bedrock AgentCore, the following can be helpful for investigating agent-side issues.

**Agent logs**

Your agent container's stdout and stderr output are captured in Amazon CloudWatch Logs in your account. You can find them at the following log group:

```
/aws/bedrock-agentcore/runtimes/<runtime-name>-<id>-<qualifier>
```

These logs capture output from your agent code, including errors, stack traces, and SDK messages. These logs can be used for investigating issues related to your agent code, dependencies, or connectivity to the RFT Runtime.

**Check agent health**

Verify your agent runtime is healthy:

```
aws bedrock-agentcore-control list-agent-runtimes --region us-west-2
```

For details on a specific runtime:

```
aws bedrock-agentcore-control get-agent-runtime \
  --agent-runtime-id <runtime-id> \
  --region us-west-2
```

### Custom agent debugging
<a name="model-customize-mtrl-troubleshooting-agent-custom"></a>

If you are using the Lambda forwarder path, issues can occur in the Lambda function itself or in your external agent. The following can be helpful for investigating both.

**Lambda forwarder logs**

Your Lambda function's execution logs are captured in Amazon CloudWatch Logs. You can find them at the following log group:

```
/aws/lambda/<function-name>
```

These logs can be used for investigating issues related to request forwarding, timeouts, or connectivity between the Lambda and your agent. Check for:
+ Invocation errors (Lambda couldn't reach your agent)
+ Timeout errors (agent took too long to respond)
+ Validation errors (malformed rollout request)

**Verify connectivity**

If your Lambda logs show invocation errors or timeouts, the issue may be that the Lambda cannot reach your agent. The following checks can help confirm whether the connection between your Lambda and agent is working.

Health check — confirm your agent is running:

```
curl -s "http://$AGENT_ENDPOINT/health"

# Expected: {"status": "ok"}
```

Lambda test invoke — confirm Lambda can reach your agent:

```
aws lambda invoke \
  --function-name rft-agent-forwarder \
  --cli-binary-format raw-in-base64-out \
  --payload '{"prompt": "test", "metadata": {"jobArn": "test", "rolloutId": "test-1"}}' \
  --region us-west-2 \
  /tmp/response.json && cat /tmp/response.json

# Note: This will return an InternalServerError because the jobArn "test"
# does not correspond to an active training job. This is expected.
# Success means the Lambda executed and reached your agent — check agent
# logs to confirm the request was received.
```

If your Lambda executes successfully but the job still fails, your agent logs may have more details. Check your agent logs for errors related to inference calls or reward reporting.

**Agent logs**

Your agent's own logs depend on where it's deployed. These logs can be used for investigating issues related to your agent code, inference calls to the RFT Runtime, or reward reporting.

For example, if you deployed your agent to Amazon EKS, you can check your agent's logs with:

```
kubectl logs -l app=external-agent --tail=50
```

## Using CloudTrail for debugging
<a name="model-customize-mtrl-troubleshooting-cloudtrail"></a>

CloudTrail data events can help confirm whether your agent's calls to the RFT Runtime are succeeding. Look for events with:
+ **eventName:** `Sample`, `SampleWithResponseStream`, `CompleteRollout`, `UpdateReward`
+ **resources.type:** `AWS::SageMaker::Job`

If you don't see these events, your agent is not successfully calling the RFT Runtime. Check agent logs and permissions.

## Logging API calls with AWS CloudTrail
<a name="model-customize-mtrl-cloudtrail"></a>

Amazon SageMaker AI is integrated with AWS CloudTrail, a service that provides a record of actions taken by a user, role, or an AWS service. CloudTrail captures all API calls for Amazon SageMaker AI as events. The calls captured include calls from the Amazon SageMaker AI console and code calls to the Amazon SageMaker AI API operations. Using the information collected by CloudTrail, you can determine the request that was made to Amazon SageMaker AI, the IP address from which the request was made, when it was made, and additional details.

Every event or log entry contains information about who generated the request. The identity information helps you determine the following:
+ Whether the request was made with root user or user credentials.
+ Whether the request was made on behalf of an IAM Identity Center user.
+ Whether the request was made with temporary security credentials for a role or federated user.
+ Whether the request was made by another AWS service.

CloudTrail is active in your AWS account when you create the account and you automatically have access to the CloudTrail **Event history**. The CloudTrail **Event history** provides a viewable, searchable, downloadable, and immutable record of the past 90 days of recorded management events in an AWS Region. For more information, see [Working with CloudTrail Event history](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/view-cloudtrail-events.html) in the *AWS CloudTrail User Guide*. There are no CloudTrail charges for viewing the **Event history**.

For an ongoing record of events in your AWS account past 90 days, create a trail or a [CloudTrail Lake](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-lake.html) event data store.

### CloudTrail trails
<a name="model-customize-mtrl-cloudtrail-trails"></a>

A *trail* enables CloudTrail to deliver log files to an Amazon S3 bucket. All trails created using the AWS Management Console are multi-Region. You can create a single-Region or a multi-Region trail by using the AWS CLI. Creating a multi-Region trail is recommended because you capture activity in all AWS Regions in your account. If you create a single-Region trail, you can view only the events logged in the trail's AWS Region. For more information about trails, see [Creating a trail for your AWS account](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-create-and-update-a-trail.html) and [Creating a trail for an organization](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/creating-trail-organization.html) in the *AWS CloudTrail User Guide*.

You can deliver one copy of your ongoing management events to your Amazon S3 bucket at no charge from CloudTrail by creating a trail, however, there are Amazon S3 storage charges. For more information about CloudTrail pricing, see [AWS CloudTrail Pricing](https://aws.amazon.com/cloudtrail/pricing/). For information about Amazon S3 pricing, see [Amazon S3 Pricing](https://aws.amazon.com/s3/pricing/).

### CloudTrail Lake event data stores
<a name="model-customize-mtrl-cloudtrail-lake"></a>

*CloudTrail Lake* lets you run SQL-based queries on your events. CloudTrail Lake converts existing events in row-based JSON format to [Apache ORC](https://orc.apache.org/) format. ORC is a columnar storage format that is optimized for fast retrieval of data. Events are aggregated into *event data stores*, which are immutable collections of events based on criteria that you select by applying [advanced event selectors](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-lake-concepts.html#adv-event-selectors). The selectors that you apply to an event data store control which events persist and are available for you to query. For more information about CloudTrail Lake, see [Working with AWS CloudTrail Lake](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-lake.html) in the *AWS CloudTrail User Guide*.

CloudTrail Lake event data stores and queries incur costs. When you create an event data store, you choose the [pricing option](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-lake-manage-costs.html#cloudtrail-lake-manage-costs-pricing-option) you want to use for the event data store. The pricing option determines the cost for ingesting and storing events, and the default and maximum retention period for the event data store. For more information about CloudTrail pricing, see [AWS CloudTrail Pricing](https://aws.amazon.com/cloudtrail/pricing/).

### SageMaker AI data events in CloudTrail
<a name="model-customize-mtrl-cloudtrail-data-events"></a>

[Data events](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/logging-data-events-with-cloudtrail.html#logging-data-events) provide information about the resource operations performed on or in a resource (for example, reading or writing to an Amazon S3 object). These are also known as data plane operations. Data events are often high-volume activities. By default, CloudTrail doesn't log data events. The CloudTrail **Event history** doesn't record data events.

Additional charges apply for data events. For more information about CloudTrail pricing, see [AWS CloudTrail Pricing](https://aws.amazon.com/cloudtrail/pricing/).

You can log data events for various Amazon SageMaker AI resource types by using the CloudTrail console, AWS CLI, or CloudTrail API operations. For more information about how to log data events, see [Logging data events with the AWS Management Console](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/logging-data-events-with-cloudtrail.html#logging-data-events-console) and [Logging data events with the AWS Command Line Interface](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/logging-data-events-with-cloudtrail.html#creating-data-event-selectors-with-the-AWS-CLI) in the *AWS CloudTrail User Guide*.

The following table lists the Amazon SageMaker AI resource types for which you can log data events:


| Resource type (console) | resources.type value | Data APIs logged to CloudTrail | API Reference | 
| --- | --- | --- | --- | 
| SageMaker endpoint | AWS::SageMaker::Endpoint | InvokeEndpoint, InvokeEndpointAsync, InvokeEndpointWithResponseStream |  [InvokeEndpoint](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_runtime_InvokeEndpoint.html), [InvokeEndpointAsync](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_runtime_InvokeEndpointAsync.html), [InvokeEndpointWithResponseStream](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_runtime_InvokeEndpointWithResponseStream.html)  | 
| SageMaker jobs | AWS::SageMaker::Job | CompleteRollout, Sample, SampleWithResponseStream |  [CompleteRollout](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_job_runtime_CompleteRollout.html), [Sample](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_job_runtime_Sample.html), [SampleWithResponseStream](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_job_runtime_SampleWithResponseStream.html)  | 

**Note**  
The `InvokeEndpoint`, `InvokeEndpointAsync`, `Sample`, and `SampleWithResponseStream` API calls don't log the request parameters.

You can configure advanced event selectors to filter on the `eventName`, `readOnly`, and `resources.ARN` fields to log only those events that are important to you. For more information about these fields, see [AdvancedFieldSelector](https://docs.aws.amazon.com/awscloudtrail/latest/APIReference/API_AdvancedFieldSelector.html) in the *AWS CloudTrail API Reference*.

**Example: Log data events for a SageMaker endpoint and job**

The following example shows how to use the [put-event-selectors](https://docs.aws.amazon.com/cli/latest/reference/cloudtrail/put-event-selectors.html) AWS CLI command to add advanced event selectors:

```
[
  {
    "FieldSelectors": [
      { "Field": "eventCategory", "Equals": ["Data"] },
      { "Field": "resources.ARN", "Equals": ["arn:aws:sagemaker:us-east-1:111122223333:endpoint/your-inference-endpoint-arn"] },
      { "Field": "resources.type", "Equals": ["AWS::SageMaker::Endpoint"] }
    ]
  },
  {
    "FieldSelectors": [
      { "Field": "eventCategory", "Equals": ["Data"] },
      { "Field": "resources.ARN", "Equals": ["arn:aws:sagemaker:us-east-1:111122223333:job/your-job-arn"] },
      { "Field": "resources.type", "Equals": ["AWS::SageMaker::Job"] }
    ]
  }
]
```

Then run:

```
aws cloudtrail put-event-selectors \
    --trail-name your-trail-name \
    --advanced-event-selectors=file://advanced-event-selectors.json
```

### SageMaker AI management events in CloudTrail
<a name="model-customize-mtrl-cloudtrail-management-events"></a>

[Management events](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/logging-management-events-with-cloudtrail.html#logging-management-events) provide information about management operations that are performed on resources in your AWS account. These are also known as control plane operations. By default, CloudTrail logs management events.

Amazon SageMaker AI logs all Amazon SageMaker AI control plane operations as management events. For a list of the Amazon SageMaker AI control plane operations that Amazon SageMaker AI logs to CloudTrail, see the [Amazon SageMaker AI API Reference](https://docs.aws.amazon.com/sagemaker/latest/APIReference).

### CloudTrail event examples
<a name="model-customize-mtrl-cloudtrail-event-examples"></a>

For information about CloudTrail record contents, see [CloudTrail record contents](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-event-reference-record-contents.html) in the *AWS CloudTrail User Guide*.

## Model packages and checkpoints
<a name="model-customize-mtrl-model-packages"></a>

### Overview
<a name="model-customize-mtrl-model-packages-overview"></a>

During multi-turn RL training, the platform periodically saves the model's learned parameters as **checkpoints**. These checkpoints are stored as **SageMaker Model Packages** within **Model Package Groups**, enabling versioning, lineage tracking, and cross-job continuity.

### Key concepts
<a name="model-customize-mtrl-model-packages-concepts"></a>

**Model Package**

A Model Package is a versioned, immutable artifact in SageMaker AI that contains trained model weights at a specific point in time. Each checkpoint produced during training is stored as a Model Package. A Model Package has:
+ An ARN (e.g., `arn:aws:sagemaker:us-west-2:123456789012:model-package/my-group/5`)
+ An S3 location containing the model files
+ Metadata about when it was created and from which training step

**Model Package Group**

A Model Package Group is a container that holds multiple Model Package versions. Multi-turn RL uses two separate groups:


| Group | Purpose | Contents | 
| --- | --- | --- | 
| Output Model Package Group | Final trained model checkpoints | HuggingFace-compatible LoRA adapter weights suitable for inference and continued training | 
| Intermediate Checkpoint Model Package Group | Resumable training state | Full optimizer state \+ adapter weights for resuming interrupted training | 

You specify both when creating a job:

```
{
  "ModelPackageConfig": {
    "OutputModelPackageGroupArn": "arn:aws:sagemaker:us-west-2:123456789012:model-package-group/my-final-models",
    "IntermediateCheckpointModelPackageGroupArn": "arn:aws:sagemaker:us-west-2:123456789012:model-package-group/my-intermediate-checkpoints"
  }
}
```

### Checkpoint types
<a name="model-customize-mtrl-model-packages-types"></a>

**Resumable Checkpoint (Full State)**
+ **Contents**: LoRA adapter weights \+ optimizer states \+ training step metadata (per GPU rank)
+ **Stored in**: Intermediate Checkpoint Model Package Group
+ **Purpose**: Resume training from the exact point it was interrupted
+ **Format**: Internal format (not directly usable for inference)
+ **When created**: Every step
+ **Use case**: Automatic resilience or explicit continued training

**Model Checkpoint (Weights Only)**
+ **Contents**: HuggingFace-compatible LoRA adapter weights in SafeTensors format
+ **Stored in**: Output Model Package Group
+ **Purpose**: Inference, deployment, or continued training
+ **Format**: Standard HuggingFace adapter format (`adapter_config.json` \+ `adapter_model.safetensors`)
+ **When created**: Every step, at job completion, and when a job is stopped
+ **Use case**: Deploy the fine-tuned model for inference, or use as input for a new training job

### Resuming interrupted training
<a name="model-customize-mtrl-model-packages-resume"></a>

If a training job fails or is stopped mid-training, you can start a new job that resumes from the exact point where the previous job left off. The platform loads the full training state (weights \+ optimizer \+ step counter) from a resumable checkpoint.

To resume, specify a resumable checkpoint (from the Intermediate Checkpoint Model Package Group) as `InputModelPackageArn`:

```
{
  "ModelPackageConfig": {
    "OutputModelPackageGroupArn": "arn:aws:sagemaker:us-west-2:123456789012:model-package-group/my-final-models",
    "IntermediateCheckpointModelPackageGroupArn": "arn:aws:sagemaker:us-west-2:123456789012:model-package-group/my-intermediate-checkpoints",
    "InputModelPackageArn": "arn:aws:sagemaker:us-west-2:123456789012:model-package/my-intermediate-checkpoints/5"
  }
}
```

**Requirements:**
+ The `InputModelPackageArn` must point to a resumable checkpoint (one with `IsCheckpoint=true` in its Model Package metadata)
+ The new job must use the same base model
+ The new job must use the same LoRA configuration (rank, alpha)
+ The new job must use the same hyperparameters (learning rate, batch size, etc.)
+ The new job must use the same dataset

### Iterative training (continued training)
<a name="model-customize-mtrl-model-packages-iterative"></a>

Iterative training lets you build on a previously trained model with new hyperparameters, a different dataset, or a different training configuration. Unlike resuming, this starts a fresh training run that initializes from the trained LoRA weights but with a fresh optimizer state.

To do iterative training, specify a model checkpoint (from the Output Model Package Group) as `InputModelPackageArn`:

```
{
  "ModelPackageConfig": {
    "OutputModelPackageGroupArn": "arn:aws:sagemaker:us-west-2:123456789012:model-package-group/my-final-models",
    "IntermediateCheckpointModelPackageGroupArn": "arn:aws:sagemaker:us-west-2:123456789012:model-package-group/my-intermediate-checkpoints",
    "InputModelPackageArn": "arn:aws:sagemaker:us-west-2:123456789012:model-package/my-final-models/3"
  }
}
```

**What you can change between iterations:**
+ Hyperparameters (learning rate, batch size, max\_steps, group\_size, etc.)
+ Dataset (different prompts, different data distribution)
+ Reward function (different reward lambda)
+ Agent configuration

**What must stay the same:**
+ The base model (the LoRA adapter is specific to the base model architecture)

**Typical use cases:**
+ Train on easy problems first, then continue on harder problems (curriculum learning)
+ Train with a simple reward function, then refine with a more nuanced one
+ Increase batch size or adjust learning rate after observing initial training dynamics

### Checkpoint lifecycle
<a name="model-customize-mtrl-model-packages-lifecycle"></a>

```
Training Step 1 → Intermediate Checkpoint (Resumable)
Training Step 1 → Intermediate Checkpoint (HFCompatible)
...
Training Step N-1 → Intermediate Checkpoint (Resumable)
Training Step N-1 → Intermediate Checkpoint (HFCompatible)
...
Training Step N (final) → Model Checkpoint (HuggingFace LoRA) → Output Model Package Group
```

When a job completes successfully: The final model weights are saved as a Model Package in the Output Model Package Group. The `OutputModelPackageArn` field on the job record contains the ARN of the final model.

When a job fails or is stopped: The last intermediate checkpoint is promoted to the Output Model Package Group (best-effort).

### Best practices for checkpoints
<a name="model-customize-mtrl-model-packages-best-practices"></a>
+ **Monitor checkpoint creation** — use `DescribeJob` to track `ResumableCheckpoint` and `ModelCheckpoint` fields during training
+ **For long jobs, use iterative training** — if a job with many steps might fail, plan to resume from checkpoints rather than restarting from scratch