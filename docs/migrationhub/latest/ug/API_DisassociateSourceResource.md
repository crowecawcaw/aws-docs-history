

AWS Migration Hub is no longer open to new customers as of November 7, 2025. For capabilities similar to AWS Migration Hub, explore [AWS Transform](https://aws.amazon.com/transform).

# DisassociateSourceResource
<a name="API_DisassociateSourceResource"></a>

Removes the association between a source resource and a migration task.

## Request Syntax
<a name="API_DisassociateSourceResource_RequestSyntax"></a>

```
{
   "DryRun": {{boolean}},
   "MigrationTaskName": "{{string}}",
   "ProgressUpdateStream": "{{string}}",
   "SourceResourceName": "{{string}}"
}
```

## Request Parameters
<a name="API_DisassociateSourceResource_RequestParameters"></a>

The request accepts the following data in JSON format.

 ** [DryRun](#API_DisassociateSourceResource_RequestSyntax) **   <a name="migrationhub-DisassociateSourceResource-request-DryRun"></a>
This is an optional parameter that you can use to test whether the call will succeed. Set this parameter to `true` to verify that you have the permissions that are required to make the call, and that you have specified the other parameters in the call correctly.  
Type: Boolean  
Required: No

 ** [MigrationTaskName](#API_DisassociateSourceResource_RequestSyntax) **   <a name="migrationhub-DisassociateSourceResource-request-MigrationTaskName"></a>
A unique identifier that references the migration task. *Do not include sensitive data in this field.*   
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 256.  
Pattern: `[^:|]+`   
Required: Yes

 ** [ProgressUpdateStream](#API_DisassociateSourceResource_RequestSyntax) **   <a name="migrationhub-DisassociateSourceResource-request-ProgressUpdateStream"></a>
The name of the progress-update stream, which is used for access control as well as a namespace for migration-task names that is implicitly linked to your AWS account. The progress-update stream must uniquely identify the migration tool as it is used for all updates made by the tool; however, it does not need to be unique for each AWS account because it is scoped to the AWS account.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 50.  
Pattern: `[^/:|\000-\037]+`   
Required: Yes

 ** [SourceResourceName](#API_DisassociateSourceResource_RequestSyntax) **   <a name="migrationhub-DisassociateSourceResource-request-SourceResourceName"></a>
The name that was specified for the source resource.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 1600.  
Required: Yes

## Response Elements
<a name="API_DisassociateSourceResource_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_DisassociateSourceResource_Errors"></a>

 ** AccessDeniedException **   
You do not have sufficient access to perform this action.  
HTTP Status Code: 400

 ** DryRunOperation **   
Exception raised to indicate a successfully authorized action when the `DryRun` flag is set to "true".  
HTTP Status Code: 400

 ** InternalServerError **   
Exception raised when an internal, configuration, or dependency error is encountered.  
HTTP Status Code: 500

 ** InvalidInputException **   
Exception raised when the provided input violates a policy constraint or is entered in the wrong format or data type.  
HTTP Status Code: 400

 ** ResourceNotFoundException **   
Exception raised when the request references a resource (Application Discovery Service configuration, update stream, migration task, etc.) that does not exist in Application Discovery Service (Application Discovery Service) or in Migration Hub's repository.  
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

## See Also
<a name="API_DisassociateSourceResource_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/AWSMigrationHub-2017-05-31/DisassociateSourceResource) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/AWSMigrationHub-2017-05-31/DisassociateSourceResource) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/AWSMigrationHub-2017-05-31/DisassociateSourceResource) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/AWSMigrationHub-2017-05-31/DisassociateSourceResource) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/AWSMigrationHub-2017-05-31/DisassociateSourceResource) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/AWSMigrationHub-2017-05-31/DisassociateSourceResource) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/AWSMigrationHub-2017-05-31/DisassociateSourceResource) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/AWSMigrationHub-2017-05-31/DisassociateSourceResource) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/AWSMigrationHub-2017-05-31/DisassociateSourceResource) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/AWSMigrationHub-2017-05-31/DisassociateSourceResource) 