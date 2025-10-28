# BatchContainerOverrides

The overrides that are sent to a container.

## Contents

**Command**

The command to send to the container that overrides the default command from the Docker
image or the task definition.

Type: Array of strings

Required: No

**Environment**

The environment variables to send to the container. You can add new environment
variables, which are added to the container at launch, or you can override the existing
environment variables from the Docker image or the task definition.

###### Note

Environment variables cannot start with "`AWS Batch` ". This
naming convention is reserved for variables that AWS Batch sets.

Type: Array of [BatchEnvironmentVariable](API_BatchEnvironmentVariable.md "API_BatchEnvironmentVariable.md") objects

Required: No

**InstanceType**

The instance type to use for a multi-node parallel job.

###### Note

This parameter isn't applicable to single-node container jobs or jobs that run on
Fargate resources, and shouldn't be provided.

Type: String

Required: No

**ResourceRequirements**

The type and amount of resources to assign to a container. This overrides the settings
in the job definition. The supported resources include `GPU`,
`MEMORY`, and `VCPU`.

Type: Array of [BatchResourceRequirement](API_BatchResourceRequirement.md "API_BatchResourceRequirement.md") objects

Required: No

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS SDK for C++](../../../goto/SdkForCpp/pipes-2015-10-07/BatchContainerOverrides.md "../../../goto/SdkForCpp/pipes-2015-10-07/BatchContainerOverrides.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/pipes-2015-10-07/BatchContainerOverrides.md "../../../goto/SdkForJavaV2/pipes-2015-10-07/BatchContainerOverrides.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/pipes-2015-10-07/BatchContainerOverrides.md "../../../goto/SdkForRubyV3/pipes-2015-10-07/BatchContainerOverrides.md")
