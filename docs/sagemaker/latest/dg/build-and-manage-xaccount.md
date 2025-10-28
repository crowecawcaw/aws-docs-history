# Set up cross-account support for Pipelines

Cross-account support for Amazon SageMaker Pipelines enables you to collaborate on machine learning
pipelines with other teams or organizations that operate in different AWS accounts. By
setting up cross-account pipeline sharing, you can grant controlled access to pipelines, allow
other accounts to view pipeline details, trigger executions, and monitor runs. The following
topic covers how to set up cross-account pipeline sharing, the different permission policies
available for shared resources, and how to access and interact with shared pipeline entities
through direct API calls to SageMaker AI.

## Set up cross-account pipeline

sharing

SageMaker AI uses [AWS
Resource Access Manager](../../../ram/latest/userguide/what-is.md "../../../ram/latest/userguide/what-is.md") (AWS RAM) to help you securely share your pipeline
entities across accounts.

### Create a resource share

1. Select **Create a resource share** through the [AWS RAM console](https://console.aws.amazon.com/ram/home "https://console.aws.amazon.com/ram/home").
2. When specifying resource share details, choose the Pipelines resource type and select
   one or more pipelines that you want to share. When you share a pipeline with any other
   account, all of its executions are also shared implicitly.
3. Associate permissions with your resource share. Choose either the default
   read-only permission policy or the extended pipeline execution permission policy. For
   more detailed information, see [Permission policies for Pipelines
   resources](#build-and-manage-xaccount-permissions "#build-and-manage-xaccount-permissions").

###### Note

If you select the extended pipeline execution policy, note that any start, stop,
and retry commands called by shared accounts use resources in the AWS account that
shared the pipeline. 4. Use AWS account IDs to specify the accounts to which you want to grant access to
your shared resources. 5. Review your resource share configuration and select **Create resource
share**. It may take a few minutes for the resource share and principal
associations to complete.

For more information, see [Sharing your AWS
resources](../../../ram/latest/userguide/getting-started-sharing.md "../../../ram/latest/userguide/getting-started-sharing.md") in the _AWS Resource Access Manager User
Guide_.

### Get responses to your

resource share invitation

Once the resource share and principal associations are set, the specified AWS
accounts receive an invitation to join the resource share. The AWS accounts must accept
the invite to gain access to any shared resources.

For more information on accepting a resource share invite through AWS RAM, see [Using shared
AWS resources](../../../ram/latest/userguide/getting-started-shared.md "../../../ram/latest/userguide/getting-started-shared.md") in the _AWS Resource Access Manager
User Guide_.

## Permission policies for Pipelines

resources

When creating your resource share, choose one of two supported permission policies to
associate with the SageMaker AI pipeline resource type. Both policies grant access to any selected
pipeline and all of its executions.

### Default read-only

permissions

The `AWSRAMDefaultPermissionSageMakerPipeline` policy allows the following
read-only actions:

```
"sagemaker:DescribePipeline"
"sagemaker:DescribePipelineDefinitionForExecution"
"sagemaker:DescribePipelineExecution"
"sagemaker:ListPipelineExecutions"
"sagemaker:ListPipelineExecutionSteps"
"sagemaker:ListPipelineParametersForExecution"
"sagemaker:Search"
```

### Extended pipeline

execution permissions

The `AWSRAMPermissionSageMakerPipelineAllowExecution` policy includes all
of the read-only permissions from the default policy and also allows shared accounts to
start, stop, and retry pipeline executions.

###### Note

Be mindful of AWS resource usage when using the extended pipeline execution
permission policy. With this policy, shared accounts are allowed to start, stop, and
retry pipeline executions. Any resources used for shared pipeline executions are
consumed by the owner account.

The extended pipeline execution permission policy allows the following actions:

```
"sagemaker:DescribePipeline"
"sagemaker:DescribePipelineDefinitionForExecution"
"sagemaker:DescribePipelineExecution"
"sagemaker:ListPipelineExecutions"
"sagemaker:ListPipelineExecutionSteps"
"sagemaker:ListPipelineParametersForExecution"
"sagemaker:StartPipelineExecution"
"sagemaker:StopPipelineExecution"
"sagemaker:RetryPipelineExecution"
"sagemaker:Search"
```

## Access shared pipeline entities

through direct API calls

Once cross-account pipeline sharing is set up, you can call the following SageMaker API
actions using a pipeline ARN:

###### Note

You can only call API commands if they are included in the permissions associated with
your resource share. If you select the
`AWSRAMPermissionSageMakerPipelineAllowExecution` policy, then the start,
stop, and retry commands use resources in the AWS account that shared the
pipeline.

- [DescribePipeline](../APIReference/API_DescribePipeline.md "../APIReference/API_DescribePipeline.md")
- [DescribePipelineDefinitionForExecution](../APIReference/API_DescribePipelineDefinitionForExecution.md "../APIReference/API_DescribePipelineDefinitionForExecution.md")
- [DescribePipelineExecution](../APIReference/API_DescribePipelineExecution.md "../APIReference/API_DescribePipelineExecution.md")
- [ListPipelineExecutions](../APIReference/API_ListPipelineExecutions.md "../APIReference/API_ListPipelineExecutions.md")
- [ListPipelineExecutionSteps](../APIReference/API_ListPipelineExecutionSteps.md "../APIReference/API_ListPipelineExecutionSteps.md")
- [ListPipelineParametersForExecution](../APIReference/API_ListPipelineParametersForExecution.md "../APIReference/API_ListPipelineParametersForExecution.md")
- [StartPipelineExecution](../APIReference/API_StartPipelineExecution.md "../APIReference/API_StartPipelineExecution.md")
- [StopPipelineExecution](../APIReference/API_StopPipelineExecution.md "../APIReference/API_StopPipelineExecution.md")
- [RetryPipelineExecution](../APIReference/API_RetryPipelineExecution.md "../APIReference/API_RetryPipelineExecution.md")
