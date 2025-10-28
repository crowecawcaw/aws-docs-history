# Resolve errors when

creating a model evaluation job in Amazon SageMaker AI

###### Important

In order to use SageMaker Clarify Foundation Model Evaluations (FMEval), you must upgrade to the new Studio
experience.

As of November 30, 2023, the previous Amazon SageMaker Studio experience is now named
Amazon SageMaker Studio Classic. FMEval isn't available in Amazon SageMaker Studio Classic.

For information about how to upgrade to the new Studio experience, see [Migration from Amazon SageMaker Studio Classic](studio-updated-migrate.md "studio-updated-migrate.md"). For
information about using the Studio Classic application, see [Amazon SageMaker Studio Classic](studio.md "studio.md").

If you run into an error while creating a model evaluation job, use the following list to troubleshoot your evaluation. If you need further assistance, contact [Support](https://console.aws.amazon.com/support/ "https://console.aws.amazon.com/support/") or [AWS Developer Forums for Amazon SageMaker AI](https://forums.aws.amazon.com/forum.jspa?forumID=285 "https://forums.aws.amazon.com/forum.jspa?forumID=285").

###### Topics

- [Error
  uploading your data from an Amazon S3 bucket](#clarify-foundation-model-evaluate-troubleshooting-cors "#clarify-foundation-model-evaluate-troubleshooting-cors")
- [The
  processing job failed to complete](#clarify-foundation-model-evaluate-troubleshooting-failure "#clarify-foundation-model-evaluate-troubleshooting-failure")
- [You
  can't find foundation model evaluations in the SageMaker AI console](#clarify-foundation-model-evaluate-troubleshooting-upgrade "#clarify-foundation-model-evaluate-troubleshooting-upgrade")
- [Your model does not support prompt stereotyping](#clarify-foundation-model-evaluate-troubleshooting-ps "#clarify-foundation-model-evaluate-troubleshooting-ps")
- [Dataset validation errors (Human)](#clarify-foundation-model-evaluate-troubleshooting-valid "#clarify-foundation-model-evaluate-troubleshooting-valid")

## Error

uploading your data from an Amazon S3 bucket

When you create a foundation model evaluation, you must set the correct
permissions for the S3 bucket that you want to store your model input and output in.
If the Cross-origin resource sharing (CORS) permissions are not set correctly, SageMaker AI
generates the following error:

**`Error: Failed to put object in s3: Error while uploading object to s3Error:
 Failed to put object in S3: NetworkError when attempting to fetch
 resource.`**

To set the correct bucket permissions, follow the instructions under **Set up your environment** in [Create an automatic model evaluation job in Studio](clarify-foundation-model-evaluate-auto-ui.md "clarify-foundation-model-evaluate-auto-ui.md").

## The

processing job failed to complete

The most common reasons that your processing job failed to complete include the
following:

- [Insufficient quota](#clarify-foundation-model-evaluate-troubleshooting-failure-quota "#clarify-foundation-model-evaluate-troubleshooting-failure-quota")
- [Insufficient memory](#clarify-foundation-model-evaluate-troubleshooting-failure-memory "#clarify-foundation-model-evaluate-troubleshooting-failure-memory")
- [Did not pass ping check](#clarify-foundation-model-evaluate-troubleshooting-failure-ping "#clarify-foundation-model-evaluate-troubleshooting-failure-ping")

See the following sections to help you mitigate each issue.

### Insufficient quota

When you run a foundation model evaluation for a non-deployed JumpStart
model, SageMaker Clarify deploys your large language model (LLM) to a SageMaker AI endpoint in your
account. If your account does not have sufficient quota to run the selected
JumpStart model, the job fails with a `ClientError`. To increase
your quota, follow these steps:

###### Request an AWS Service Quotas increase

1.  Retrieve the instance name, current quota and necessary quota from the
    on screen error message. For example, in the following error:

        * The instance name is `ml.g5.12xlarge`.
        * The current quota from the number following `current
         utilization`is `0 instances`
        * The additional required quota from the number following
         `request delta` is `1
         instances`.

    The sample error follows:

`ClientError: An error occurred (ResourceLimitExceeded) when
 calling the CreateEndpoint operation: The account-level service
 limit 'ml.g5.12xlarge for endpoint usage' is 0 Instances, with
 current utilization of 0 Instances and a request delta of 1
 Instances. Please use AWS Service Quotas to request an increase for
 this quota. If AWS Service Quotas is not available, contact AWS
 support to request an increase for this quota` 2. Sign into the AWS Management Console and open the [Service Quotas
console](https://console.aws.amazon.com/servicequotas/home "https://console.aws.amazon.com/servicequotas/home"). 3. In the navigation pane, under **Manage quotas**,
input `Amazon SageMaker AI`. 4. Choose **View quotas**. 5. In the search bar under **Service quotas**, input the
name of the instance from Step 1. For example, using the information
contained in the error message from Step 1, input
`ml.g5.12xlarge`. 6. Choose the **Quota name** that appears next to your
instance name and ends with **for endpoint usage**. For
example, using the information contained in the error message from Step
1, choose **ml.g5.12xlarge for endpoint usage**. 7. Choose **Request increase at account-level**. 8. Under **Increase quota value**, input the necessary
required quota from the information given in the error message from Step

1. Input the **total** of `current
utilization` and `request delta`. In the previous
   example error, the `current utilization` is `0
Instances`, and the `request delta` is `1
Instances`. In this example, request a quota of `1`
   to supply the required quota.
2. Choose **Request**.
3. Choose **Quota request history** from the navigation
   pane.
4. When the **Status** changes from
   **Pending** to **Approved**, rerun
   your job. You may need to refresh your browser to see the change.

For more information about requesting an increase in your quota, see [Requesting
a quota increase](../../../servicequotas/latest/userguide/request-quota-increase.md "../../../servicequotas/latest/userguide/request-quota-increase.md").

### Insufficient memory

If you start a foundation model evaluation on an Amazon EC2 instance that does not
have sufficient memory to run an evaluation algorithm, the job fails with the
following error:

`The actor is dead because its worker process has died. Worker exit type:
 SYSTEM_ERROR Worker exit detail: Worker unexpectedly exits with a connection
 error code 2. End of file. There are some potential root causes. (1) The
 process is killed by SIGKILL by OOM killer due to high memory usage. (2) ray
 stop --force is called. (3) The worker is crashed unexpectedly due to
 SIGSEGV or other unexpected errors. The actor never ran - it was cancelled
 before it started running.`

To increase the memory available for your evaluation job, change your instance
to one that has more memory. If you are using the user interface, you can choose
an instance type under **Processor configuration** in
**Step 2**. If you are running your job inside the SageMaker AI
console, launch a new space using an instance with increased memory
capacity.

For a list of Amazon EC2 instances, see [Instance types](../../../AWSEC2/latest/UserGuide/instance-types.md#AvailableInstanceTypes "../../../AWSEC2/latest/UserGuide/instance-types.md#AvailableInstanceTypes").

For more information, about instances with larger memory capacity, see [Memory
optimized instances](../../../AWSEC2/latest/UserGuide/memory-optimized-instances.md "../../../AWSEC2/latest/UserGuide/memory-optimized-instances.md").

### Did not pass ping check

In some instances, your foundation model evaluation job will fail because it
did not pass a ping check when SageMaker AI was deploying your endpoint. If it does not
pass a ping test, the following error appears:

`ClientError: Error hosting endpoint
 `your_endpoint_name`: Failed. Reason: The
 primary container for production variant AllTraffic did not pass the ping
 health check. Please check CloudWatch logs for this endpoint..., Job exited
 for model: `your_model_name`of model_type:
 `your_model_type``

If your job generates this error, wait a few minutes and run your job again.
If the error persists, contact [AWS Support](https://console.aws.amazon.com/support/ "https://console.aws.amazon.com/support/") or
[AWS
Developer Forums for Amazon SageMaker AI](https://forums.aws.amazon.com/forum.jspa?forumID=285 "https://forums.aws.amazon.com/forum.jspa?forumID=285").

## You

can't find foundation model evaluations in the SageMaker AI console

In order to use SageMaker Clarify Foundation Model Evaluations, you must upgrade to the new Studio experience.
As of November 30, 2023, the previous Amazon SageMaker Studio experience is now named
Amazon SageMaker Studio Classic. The foundation evaluation feature can only be used in the updated experience. For information about how to update Studio, see [Migration from Amazon SageMaker Studio Classic](studio-updated-migrate.md "studio-updated-migrate.md").

## Your model does not support prompt stereotyping

Only some JumpStart models support prompt stereotyping. If you select a
JumpStart model that is not supported, the following error appears:

`{"evaluationMetrics":"This model does not support Prompt stereotyping
 evaluation. Please remove that evaluation metric or select another model that
 supports it."}`

If you receive this error, you cannot use your selected model in a foundation
evaluation. SageMaker Clarify is currently working to update all JumpStart models for prompt
stereotyping tasks so that they can be used in a foundation model evaluation.

## Dataset validation errors (Human)

The custom prompt dataset in a model evaluation job that uses human workers must be formatted using the JSON lines format using the `.jsonl` extension.

When you start a job each JSON object in the prompt dataset is interdependently validated. If one of the JSON objects is not valid you get the following error.

```
Customer Error: Your input dataset could not be validated. Your dataset can have up to 1000 prompts. The dataset must be a valid jsonl file, and each prompt valid json object.To learn more about troubleshooting dataset validations errors, see Troubleshooting guide. Job executed for models: meta-textgeneration-llama-2-7b-f, pytorch-textgeneration1-alexa20b.
```

For a custom prompt dataset to pass all validations the following must be _true_ for all JSON objects in the JSON lines file.

- Each line in the prompt dataset file must be a valid JSON object.
- Special characters such as quotation marks (`"`) must be escaped properly. For example, if your prompt was the following `"Claire said to the crowd, "Bananas are the best!""` the quotes would need to be escaped using a `\`, `"Claire said to the crowd, \"Bananas are the best!\""`.
- A valid JSON objects must contain at least the `prompt`key/value pair.
- A prompt dataset file cannot contain more than 1,000 JSON objects in a single file.
- If you specify the `responses` key in _any_ JSON object, it must be present in*all* JSON objects.
- The maximum number of objects in the `responses` key is 1. If you have responses from multiple models you want to compare, each require a separate BYOI dataset.
- If you specify the `responses` key in _any_ JSON object, it must also contain the `modelIdentifier` and `text` keys in all _all_ `responses` objects.
