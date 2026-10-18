

# LoggingConfig
<a name="API_LoggingConfig"></a>

The logging configuration for a web function revision.

## Contents
<a name="API_LoggingConfig_Contents"></a>

 ** applicationLogLevel **   <a name="lambdaweb-Type-LoggingConfig-applicationLogLevel"></a>
The log level for application logs emitted by the web function. If you don't specify a value, the default is `INFO`, and this default is returned in the response.  
Type: String  
Valid Values: `TRACE | DEBUG | INFO | WARN | ERROR | FATAL`   
Required: No

 ** logGroup **   <a name="lambdaweb-Type-LoggingConfig-logGroup"></a>
The name of the Amazon CloudWatch Logs log group the web function sends logs to. If you don't specify a value, the default is `/aws/lambda/web/{functionName}`, and this default is returned in the response.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 500.  
Pattern: `[a-zA-Z0-9\.\-_/#]+`   
Required: No

 ** systemLogLevel **   <a name="lambdaweb-Type-LoggingConfig-systemLogLevel"></a>
The log level for system logs emitted by the Lambda runtime. If you don't specify a value, the default is `INFO`, and this default is returned in the response.  
Type: String  
Valid Values: `DEBUG | INFO | WARN`   
Required: No

## See Also
<a name="API_LoggingConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/lambda-web-2025-03-07/LoggingConfig) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/lambda-web-2025-03-07/LoggingConfig) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/lambda-web-2025-03-07/LoggingConfig) 