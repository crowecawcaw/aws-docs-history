

AWS Migration Hub is no longer open to new customers as of November 7, 2025. For capabilities similar to AWS Migration Hub, explore [AWS Transform](https://aws.amazon.com/transform).

# CreateProgressUpdateStream
<a name="API_CreateProgressUpdateStream"></a>

Creates a progress update stream which is an AWS resource used for access control as well as a namespace for migration task names that is implicitly linked to your AWS account. It must uniquely identify the migration tool as it is used for all updates made by the tool; however, it does not need to be unique for each AWS account because it is scoped to the AWS account.

## Request Syntax
<a name="API_CreateProgressUpdateStream_RequestSyntax"></a>

```
{
   "DryRun": {{boolean}},
   "ProgressUpdateStreamName": "{{string}}"
}
```

## Request Parameters
<a name="API_CreateProgressUpdateStream_RequestParameters"></a>

The request accepts the following data in JSON format.

 ** [DryRun](#API_CreateProgressUpdateStream_RequestSyntax) **   <a name="migrationhub-CreateProgressUpdateStream-request-DryRun"></a>
Optional boolean flag to indicate whether any effect should take place. Used to test if the caller has permission to make the call.  
Type: Boolean  
Required: No

 ** [ProgressUpdateStreamName](#API_CreateProgressUpdateStream_RequestSyntax) **   <a name="migrationhub-CreateProgressUpdateStream-request-ProgressUpdateStreamName"></a>
The name of the ProgressUpdateStream. *Do not store personal data in this field.*   
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 50.  
Pattern: `[^/:|\000-\037]+`   
Required: Yes

## Response Elements
<a name="API_CreateProgressUpdateStream_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_CreateProgressUpdateStream_Errors"></a>

 ** AccessDeniedException **   
You do not have sufficient access to perform this action.  
HTTP Status Code: 400

 ** DryRunOperation **   
Exception raised to indicate a successfully authorized action when the `DryRun` flag is set to "true".  
HTTP Status Code: 400

 ** HomeRegionNotSetException **   
The home region is not set. Set the home region to continue.  
HTTP Status Code: 400

 ** InternalServerError **   
Exception raised when an internal, configuration, or dependency error is encountered.  
HTTP Status Code: 500

 ** InvalidInputException **   
Exception raised when the provided input violates a policy constraint or is entered in the wrong format or data type.  
HTTP Status Code: 400

 ** ServiceUnavailableException **   
Exception raised when there is an internal, configuration, or dependency error encountered.  
HTTP Status Code: 500

 ** ThrottlingException **   
The request was denied due to request throttling.    
 ** Message **   
A message that provides information about the exception.  
 ** RetryAfterSeconds **   
The number of seconds the caller should wait before retrying.
HTTP Status Code: 400

 ** UnauthorizedOperation **   
Exception raised to indicate a request was not authorized when the `DryRun` flag is set to "true".  
HTTP Status Code: 400

## Examples
<a name="API_CreateProgressUpdateStream_Examples"></a>

### Create a progress update stream
<a name="API_CreateProgressUpdateStream_Example_1"></a>

The following example creates a progress update stream identified by the values passed to the required parameter `ProgressUpdateStreamName` in the request.

#### Sample Request
<a name="API_CreateProgressUpdateStream_Example_1_Request"></a>

```
{
    "ProgressUpdateStreamName": "SMS", 
    "DryRun": false
}
```

## See Also
<a name="API_CreateProgressUpdateStream_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/AWSMigrationHub-2017-05-31/CreateProgressUpdateStream) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/AWSMigrationHub-2017-05-31/CreateProgressUpdateStream) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/AWSMigrationHub-2017-05-31/CreateProgressUpdateStream) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/AWSMigrationHub-2017-05-31/CreateProgressUpdateStream) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/AWSMigrationHub-2017-05-31/CreateProgressUpdateStream) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/AWSMigrationHub-2017-05-31/CreateProgressUpdateStream) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/AWSMigrationHub-2017-05-31/CreateProgressUpdateStream) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/AWSMigrationHub-2017-05-31/CreateProgressUpdateStream) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/AWSMigrationHub-2017-05-31/CreateProgressUpdateStream) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/AWSMigrationHub-2017-05-31/CreateProgressUpdateStream) 