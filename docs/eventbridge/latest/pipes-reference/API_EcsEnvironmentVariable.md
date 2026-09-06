

# EcsEnvironmentVariable
<a name="API_EcsEnvironmentVariable"></a>

The environment variables to send to the container. You can add new environment variables, which are added to the container at launch, or you can override the existing environment variables from the Docker image or the task definition. You must also specify a container name.

## Contents
<a name="API_EcsEnvironmentVariable_Contents"></a>

 ** name **   <a name="eventbridge-Type-EcsEnvironmentVariable-name"></a>
The name of the key-value pair. For environment variables, this is the name of the environment variable.  
Type: String  
Required: No

 ** value **   <a name="eventbridge-Type-EcsEnvironmentVariable-value"></a>
The value of the key-value pair. For environment variables, this is the value of the environment variable.  
Type: String  
Required: No

## See Also
<a name="API_EcsEnvironmentVariable_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/pipes-2015-10-07/EcsEnvironmentVariable) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/pipes-2015-10-07/EcsEnvironmentVariable) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/pipes-2015-10-07/EcsEnvironmentVariable) 