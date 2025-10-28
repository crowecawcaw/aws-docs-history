# Troubleshooting Amazon SageMaker Pipelines

When using Amazon SageMaker Pipelines, you might run into issues for various reasons. This topic provides
information about common errors and how to resolve them.

**Pipeline Definition Issues**

Your pipeline definition might not be formatted correctly. This can result in your
execution
failing or your job being inaccurate. These errors can be caught when the pipeline is created or
when an execution occurs. If your definition doesn’t validate, Pipelines returns an error message
identifying the character where the JSON file is malformed. To fix this problem, review the
steps created using the SageMaker AI Python SDK for accuracy.

You can only include steps in a pipeline definition once. Because of this, steps cannot exist
as part of a condition step _and_ a pipeline in the same
pipeline.

**Examining Pipeline Logs**

You can view the status of your steps using the following command:

```
execution.list_steps()
```

Each step includes the following information:

- The ARN of the entity launched by the pipeline, such as SageMaker AI job ARN, model ARN, or model
  package ARN.
- The failure reason includes a brief explanation of the step failure.
- If the step is a condition step, it includes whether the condition is evaluated to true or
  false.
- If the execution reuses a previous job execution, the `CacheHit` lists the
  source execution.
  You can also view the error messages and logs in the Amazon SageMaker Studio interface. For information
  about how to see the logs in Studio, see [View the details of a pipeline run](pipelines-studio-view-execution.md "pipelines-studio-view-execution.md").

**Missing Permissions**

Correct permissions are required for the role that creates the pipeline execution, and the
steps that create each of the jobs in your pipeline execution. Without these permissions, you
may not be able to submit your pipeline execution or run your SageMaker AI jobs as expected. To ensure
that your permissions are properly set up, see [IAM Access Management](build-and-manage-access.md "build-and-manage-access.md").

**Job Execution Errors**

You may run into issues when executing your steps because of issues in the scripts that define
the functionality of your SageMaker AI jobs. Each job has a set of CloudWatch logs. To view these logs from
Studio, see [View the details of a pipeline run](pipelines-studio-view-execution.md "pipelines-studio-view-execution.md"). For information about using CloudWatch logs with
SageMaker AI, see [CloudWatch Logs for Amazon SageMaker AI](logging-cloudwatch.md "logging-cloudwatch.md").

**Property File Errors**

You may have issues when incorrectly implementing property files with
your pipeline. To ensure that your implementation of property files
works as expected, see [Pass Data Between Steps](build-and-manage-propertyfile.md "build-and-manage-propertyfile.md").

**Issues copying the script to the container in the Dockerfile**

You can either copy the script to the container or pass it via the `entry_point`
argument (of your estimator entity) or `code` argument (of your processor entity),
as demonstrated in the following code sample.

```
step_process = ProcessingStep(
    name="PreprocessAbaloneData",
    processor=sklearn_processor,
    inputs = [
        ProcessingInput(
            input_name='dataset',
            source=...,
            destination="/opt/ml/processing/code",
        )
    ],
    outputs=[
        ProcessingOutput(output_name="train", source="/opt/ml/processing/train", destination = processed_data_path),
        ProcessingOutput(output_name="validation", source="/opt/ml/processing/validation", destination = processed_data_path),
        ProcessingOutput(output_name="test", source="/opt/ml/processing/test", destination = processed_data_path),
    ],
    code=os.path.join(BASE_DIR, "process.py"), ## Code is passed through an argument
    cache_config = cache_config,
    job_arguments = ['--input', 'arg1']
)

sklearn_estimator = SKLearn(
    entry_point=os.path.join(BASE_DIR, "train.py"), ## Code is passed through the entry_point
    framework_version="0.23-1",
    instance_type=training_instance_type,
    role=role,
    output_path=model_path, # New
    sagemaker_session=sagemaker_session, # New
    instance_count=1, # New
    base_job_name=f"{base_job_prefix}/pilot-train",
    metric_definitions=[
        {'Name': 'train:accuracy', 'Regex': 'accuracy_train=(.*?);'},
        {'Name': 'validation:accuracy', 'Regex': 'accuracy_validation=(.*?);'}
    ],
)
```
