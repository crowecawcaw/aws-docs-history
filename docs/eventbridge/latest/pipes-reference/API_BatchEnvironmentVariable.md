

# BatchEnvironmentVariable
<a name="API_BatchEnvironmentVariable"></a>

The environment variables to send to the container. You can add new environment variables, which are added to the container at launch, or you can override the existing environment variables from the Docker image or the task definition.

**Note**  
Environment variables cannot start with "` AWS Batch `". This naming convention is reserved for variables that AWS Batch sets.

## Contents
<a name="API_BatchEnvironmentVariable_Contents"></a>

 ** Name **   <a name="eventbridge-Type-BatchEnvironmentVariable-Name"></a>
The name of the key-value pair. For environment variables, this is the name of the environment variable.  
Type: String  
Required: No

 ** Value **   <a name="eventbridge-Type-BatchEnvironmentVariable-Value"></a>
The value of the key-value pair. For environment variables, this is the value of the environment variable.  
Type: String  
Required: No

## See Also
<a name="API_BatchEnvironmentVariable_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/pipes-2015-10-07/BatchEnvironmentVariable) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/pipes-2015-10-07/BatchEnvironmentVariable) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/pipes-2015-10-07/BatchEnvironmentVariable) 