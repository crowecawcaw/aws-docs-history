

# EcsContainerOverride
<a name="API_EcsContainerOverride"></a>

The overrides that are sent to a container. An empty container override can be passed in. An example of an empty container override is `{"containerOverrides": [ ] }`. If a non-empty container override is specified, the `name` parameter must be included.

## Contents
<a name="API_EcsContainerOverride_Contents"></a>

 ** Command **   <a name="eventbridge-Type-EcsContainerOverride-Command"></a>
The command to send to the container that overrides the default command from the Docker image or the task definition. You must also specify a container name.  
Type: Array of strings  
Required: No

 ** Cpu **   <a name="eventbridge-Type-EcsContainerOverride-Cpu"></a>
The number of `cpu` units reserved for the container, instead of the default value from the task definition. You must also specify a container name.  
Type: Integer  
Required: No

 ** Environment **   <a name="eventbridge-Type-EcsContainerOverride-Environment"></a>
The environment variables to send to the container. You can add new environment variables, which are added to the container at launch, or you can override the existing environment variables from the Docker image or the task definition. You must also specify a container name.  
Type: Array of [EcsEnvironmentVariable](API_EcsEnvironmentVariable.md) objects  
Required: No

 ** EnvironmentFiles **   <a name="eventbridge-Type-EcsContainerOverride-EnvironmentFiles"></a>
A list of files containing the environment variables to pass to a container, instead of the value from the container definition.  
Type: Array of [EcsEnvironmentFile](API_EcsEnvironmentFile.md) objects  
Required: No

 ** Memory **   <a name="eventbridge-Type-EcsContainerOverride-Memory"></a>
The hard limit (in MiB) of memory to present to the container, instead of the default value from the task definition. If your container attempts to exceed the memory specified here, the container is killed. You must also specify a container name.  
Type: Integer  
Required: No

 ** MemoryReservation **   <a name="eventbridge-Type-EcsContainerOverride-MemoryReservation"></a>
The soft limit (in MiB) of memory to reserve for the container, instead of the default value from the task definition. You must also specify a container name.  
Type: Integer  
Required: No

 ** Name **   <a name="eventbridge-Type-EcsContainerOverride-Name"></a>
The name of the container that receives the override. This parameter is required if any override is specified.  
Type: String  
Required: No

 ** ResourceRequirements **   <a name="eventbridge-Type-EcsContainerOverride-ResourceRequirements"></a>
The type and amount of a resource to assign to a container, instead of the default value from the task definition. The only supported resource is a GPU.  
Type: Array of [EcsResourceRequirement](API_EcsResourceRequirement.md) objects  
Required: No

## See Also
<a name="API_EcsContainerOverride_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/pipes-2015-10-07/EcsContainerOverride) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/pipes-2015-10-07/EcsContainerOverride) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/pipes-2015-10-07/EcsContainerOverride) 