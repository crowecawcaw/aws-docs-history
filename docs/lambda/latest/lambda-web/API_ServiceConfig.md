

# ServiceConfig
<a name="API_ServiceConfig"></a>

The service configuration for a web function revision, including execution role, timeout, VPC network access, concurrency, and telemetry settings.

## Contents
<a name="API_ServiceConfig_Contents"></a>

 ** executionRoleArn **   <a name="lambdaweb-Type-ServiceConfig-executionRoleArn"></a>
The ARN of the IAM role that the web function assumes when it runs. This role provides permissions to access AWS services and resources.  
Type: String  
Length Constraints: Minimum length of 20. Maximum length of 2048.  
Pattern: `arn:(aws[a-z-]*):iam::[0-9]{12}:role/[a-zA-Z0-9+=,.@_/-]+`   
Required: Yes

 ** egressNetworkConnectorArn **   <a name="lambdaweb-Type-ServiceConfig-egressNetworkConnectorArn"></a>
The Amazon Resource Name (ARN) of the Lambda network connector that gives the web function access to resources in your VPC. You must specify the fully qualified ARN, including the connector version, which pins the revision to that version. If the network connector is deleted, invocations of revisions that reference it fail. Revisions that specify a network connector support only `HomeRegion` endpoints, not `MultiRegion` or `PerRegion`.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 2048.  
Pattern: `arn:(aws[a-z-]*):lambda:[a-z0-9-]+:[0-9]{12}:network-connector:[a-zA-Z0-9_-]+:[0-9]+`   
Required: No

 ** environmentVariables **   <a name="lambdaweb-Type-ServiceConfig-environmentVariables"></a>
A map of environment variable key-value pairs available to the web function at runtime. Environment variable values are sensitive.  
Type: String to string map  
Key Length Constraints: Minimum length of 1.  
Key Pattern: `[a-zA-Z]([a-zA-Z0-9_])*`   
Value Length Constraints: Minimum length of 1.  
Required: No

 ** maxConcurrencyPerEnvironment **   <a name="lambdaweb-Type-ServiceConfig-maxConcurrencyPerEnvironment"></a>
The maximum number of concurrent requests handled per execution environment. Minimum value of 1, maximum value of 128. If you don't specify a value, the default is 64, and this default is returned in the response.  
Type: Integer  
Valid Range: Minimum value of 1. Maximum value of 128.  
Required: No

 ** telemetryConfig **   <a name="lambdaweb-Type-ServiceConfig-telemetryConfig"></a>
The telemetry configuration for the web function, including logging settings.  
Type: [TelemetryConfig](API_TelemetryConfig.md) object  
Required: No

 ** timeoutSeconds **   <a name="lambdaweb-Type-ServiceConfig-timeoutSeconds"></a>
The amount of time (in seconds) that Lambda allows the web function to run before stopping it. Minimum value of 3, maximum value of 900. If you don't specify a value, the default is 30, and this default is returned in the response.  
Type: Integer  
Valid Range: Minimum value of 3. Maximum value of 900.  
Required: No

## See Also
<a name="API_ServiceConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/lambda-web-2025-03-07/ServiceConfig) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/lambda-web-2025-03-07/ServiceConfig) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/lambda-web-2025-03-07/ServiceConfig) 