# PipeTargetBatchJobParameters

The parameters for using an AWS Batch job as a target.

## Contents

**JobDefinition**

The job definition used by this job. This value can be one of `name`,
`name:revision`, or the Amazon Resource Name (ARN) for the job definition. If
name is specified without a revision then the latest active revision is used.

Type: String

Required: Yes

**JobName**

The name of the job. It can be up to 128 letters long. The first character must be
alphanumeric, can contain uppercase and lowercase letters, numbers, hyphens (-), and
underscores (\_).

Type: String

Required: Yes

**ArrayProperties**

The array properties for the submitted job, such as the size of the array. The array size can be between 2 and 10,000.
If you specify array properties for a job, it becomes an array job. This parameter is used only if the target is an AWS Batch job.

Type: [BatchArrayProperties](API_BatchArrayProperties.md "API_BatchArrayProperties.md") object

Required: No

**ContainerOverrides**

The overrides that are sent to a container.

Type: [BatchContainerOverrides](API_BatchContainerOverrides.md "API_BatchContainerOverrides.md") object

Required: No

**DependsOn**

A list of dependencies for the job. A job can depend upon a maximum of 20 jobs. You can
specify a `SEQUENTIAL` type dependency without specifying a job ID for array
jobs so that each child array job completes sequentially, starting at index 0. You can also
specify an `N_TO_N` type dependency with a job ID for array jobs. In that case,
each index child of this job must wait for the corresponding index child of each dependency
to complete before it can begin.

Type: Array of [BatchJobDependency](API_BatchJobDependency.md "API_BatchJobDependency.md") objects

Array Members: Minimum number of 0 items. Maximum number of 20 items.

Required: No

**Parameters**

Additional parameters passed to the job that replace parameter substitution placeholders
that are set in the job definition. Parameters are specified as a key and value pair
mapping. Parameters included here override any corresponding parameter defaults from the
job definition.

Type: String to string map

Required: No

**RetryStrategy**

The retry strategy to use for failed jobs. When a retry strategy is specified here, it
overrides the retry strategy defined in the job definition.

Type: [BatchRetryStrategy](API_BatchRetryStrategy.md "API_BatchRetryStrategy.md") object

Required: No

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS SDK for C++](../../../goto/SdkForCpp/pipes-2015-10-07/PipeTargetBatchJobParameters.md "../../../goto/SdkForCpp/pipes-2015-10-07/PipeTargetBatchJobParameters.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/pipes-2015-10-07/PipeTargetBatchJobParameters.md "../../../goto/SdkForJavaV2/pipes-2015-10-07/PipeTargetBatchJobParameters.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/pipes-2015-10-07/PipeTargetBatchJobParameters.md "../../../goto/SdkForRubyV3/pipes-2015-10-07/PipeTargetBatchJobParameters.md")
