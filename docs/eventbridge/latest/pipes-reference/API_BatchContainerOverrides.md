

# BatchContainerOverrides
<a name="API_BatchContainerOverrides"></a>

The overrides that are sent to a container.

## Contents
<a name="API_BatchContainerOverrides_Contents"></a>

 ** Command **   <a name="eventbridge-Type-BatchContainerOverrides-Command"></a>
The command to send to the container that overrides the default command from the Docker image or the task definition.  
Type: Array of strings  
Required: No

 ** Environment **   <a name="eventbridge-Type-BatchContainerOverrides-Environment"></a>
The environment variables to send to the container. You can add new environment variables, which are added to the container at launch, or you can override the existing environment variables from the Docker image or the task definition.  
Environment variables cannot start with "` AWS Batch `". This naming convention is reserved for variables that AWS Batch sets.
Type: Array of [BatchEnvironmentVariable](API_BatchEnvironmentVariable.md) objects  
Required: No

 ** InstanceType **   <a name="eventbridge-Type-BatchContainerOverrides-InstanceType"></a>
The instance type to use for a multi-node parallel job.  
This parameter isn't applicable to single-node container jobs or jobs that run on Fargate resources, and shouldn't be provided.
Type: String  
Required: No

 ** ResourceRequirements **   <a name="eventbridge-Type-BatchContainerOverrides-ResourceRequirements"></a>
The type and amount of resources to assign to a container. This overrides the settings in the job definition. The supported resources include `GPU`, `MEMORY`, and `VCPU`.  
Type: Array of [BatchResourceRequirement](API_BatchResourceRequirement.md) objects  
Required: No

## See Also
<a name="API_BatchContainerOverrides_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/pipes-2015-10-07/BatchContainerOverrides) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/pipes-2015-10-07/BatchContainerOverrides) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/pipes-2015-10-07/BatchContainerOverrides) 