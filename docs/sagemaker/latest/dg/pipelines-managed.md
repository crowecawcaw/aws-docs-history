

# AWS managed pipelines

An AWS managed pipeline is a pipeline that AWS creates and maintains for a common ML workflow. You can run it from your account without writing a pipeline definition. AWS owns the pipeline, so its ARN uses `aws` in place of an account ID:

```
arn:aws:sagemaker:{{region}}:aws:pipeline/{{pipeline-name}}
```

When you run a managed pipeline, the execution runs in your account and uses an IAM role that you provide. The jobs that the execution creates, such as training jobs, and the data they write are in your account.

## Find managed pipelines
<a name="pipelines-managed-find"></a>

To list managed pipelines, call `ListPipelines` with `ManagedBy` set to `AWS`. To list only the pipelines that you created, set it to `CUSTOMER`.

```python
import boto3

sm = boto3.client("sagemaker")
response = sm.list_pipelines(ManagedBy="AWS")
for summary in response["PipelineSummaries"]:
    print(summary["PipelineArn"], summary.get("PipelineDescription"))
```

To see a managed pipeline's definition and parameters, call `DescribePipeline` with its ARN. To see its versions and their aliases, call `ListPipelineVersions`.

```python
pipeline_arn = "arn:aws:sagemaker:us-west-2:aws:pipeline/{{pipeline-name}}"

pipeline = sm.describe_pipeline(PipelineName=pipeline_arn)
versions = sm.list_pipeline_versions(PipelineName=pipeline_arn)
```

Managed pipelines aren't available in every AWS Region. If a managed pipeline isn't available to your account, requests for it fail with a `ResourceNotFound` error.

## Run a managed pipeline
<a name="pipelines-managed-run"></a>

Call `StartPipelineExecution` with the pipeline ARN and a `RoleArn`. The execution uses this role to create and access resources in your account, so the role needs the permissions that the pipeline's steps require. `RoleArn` is required for a managed pipeline. You can't specify it for a pipeline that you created, because those executions use the pipeline's role.

```python
response = sm.start_pipeline_execution(
    PipelineName=pipeline_arn,
    RoleArn="arn:aws:iam::{{111122223333}}:role/{{MySageMakerExecutionRole}}",
    PipelineParameters=[
        {"Name": "{{ParameterName}}", "Value": "{{value}}"},
    ],
)
execution_arn = response["PipelineExecutionArn"]
```

The execution ARN contains your account ID. You monitor the execution the same way as an execution of your own pipeline, with `DescribePipelineExecution` and `ListPipelineExecutionSteps`. `DescribePipelineExecution` also returns the `RoleArn` that the execution uses.

AWS can release new versions of a managed pipeline. If you don't specify a version, the execution uses the latest version that's available to you. To get the same behavior on every run, specify `PipelineVersionId` or `PipelineVersionAlias`. For more information about aliases, see [Pipeline version aliases](pipelines-version-aliases.md).

## Customize a managed pipeline
<a name="pipelines-managed-copy"></a>

You can't update or delete a managed pipeline, or change the aliases of its versions. These requests fail with an `AccessDenied` error. To change a managed pipeline, copy its definition into a pipeline in your account and edit the copy. Your copy doesn't receive the updates that AWS makes to the managed pipeline.

```python
definition = sm.describe_pipeline(PipelineName=pipeline_arn)["PipelineDefinition"]

sm.create_pipeline(
    PipelineName="{{my-pipeline}}",
    PipelineDefinition=definition,
    RoleArn="arn:aws:iam::{{111122223333}}:role/{{MySageMakerExecutionRole}}",
)
```