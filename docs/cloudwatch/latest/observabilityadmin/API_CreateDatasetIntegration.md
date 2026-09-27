

# CreateDatasetIntegration
<a name="API_CreateDatasetIntegration"></a>

Creates a dataset integration for the caller's account in the current region and returns its ARN.

To use this operation, you must have permission to access the dataset integration resources through the IAM role specified in the `RoleArn` parameter.

If a dataset integration already exists for the account, this operation fails with a `ConflictException`.

## Request Syntax
<a name="API_CreateDatasetIntegration_RequestSyntax"></a>

```
POST /CreateDatasetIntegration HTTP/1.1
Content-type: application/json

{
   "RoleArn": "{{string}}",
   "Tags": { 
      "{{string}}" : "{{string}}" 
   }
}
```

## URI Request Parameters
<a name="API_CreateDatasetIntegration_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_CreateDatasetIntegration_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [RoleArn](#API_CreateDatasetIntegration_RequestSyntax) **   <a name="cwoa-CreateDatasetIntegration-request-RoleArn"></a>
The Amazon Resource Name (ARN) of the IAM role that grants Amazon CloudWatch permission to access the resources needed for the dataset integration.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 1011.  
Pattern: `arn:aws([a-z0-9\-]+)?:([a-zA-Z0-9\-]+):([a-z0-9\-]+)?:([0-9]{12})?:(.+)`   
Required: Yes

 ** [Tags](#API_CreateDatasetIntegration_RequestSyntax) **   <a name="cwoa-CreateDatasetIntegration-request-Tags"></a>
The key-value pairs to associate with the dataset integration resource for categorization and management purposes.  
Type: String to string map  
Map Entries: Maximum number of 50 items.  
Key Length Constraints: Minimum length of 1. Maximum length of 128.  
Key Pattern: `([\p{L}\p{Z}\p{N}_.:/=+\-@]*)`   
Value Length Constraints: Minimum length of 0. Maximum length of 256.  
Value Pattern: `([\p{L}\p{Z}\p{N}_.:/=+\-@]*)`   
Required: No

## Response Syntax
<a name="API_CreateDatasetIntegration_ResponseSyntax"></a>

```
HTTP/1.1 201
Content-type: application/json

{
   "Arn": "string",
   "CreatedAt": number,
   "RoleArn": "string",
   "UpdatedAt": number
}
```

## Response Elements
<a name="API_CreateDatasetIntegration_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 201 response.

The following data is returned in JSON format by the service.

 ** [Arn](#API_CreateDatasetIntegration_ResponseSyntax) **   <a name="cwoa-CreateDatasetIntegration-response-Arn"></a>
The Amazon Resource Name (ARN) of the created dataset integration.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 1011.  
Pattern: `arn:aws([a-z0-9\-]+)?:([a-zA-Z0-9\-]+):([a-z0-9\-]+)?:([0-9]{12})?:(.+)` 

 ** [CreatedAt](#API_CreateDatasetIntegration_ResponseSyntax) **   <a name="cwoa-CreateDatasetIntegration-response-CreatedAt"></a>
The timestamp when the dataset integration was created.  
Type: Timestamp

 ** [RoleArn](#API_CreateDatasetIntegration_ResponseSyntax) **   <a name="cwoa-CreateDatasetIntegration-response-RoleArn"></a>
The Amazon Resource Name (ARN) of the IAM role associated with the dataset integration.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 1011.  
Pattern: `arn:aws([a-z0-9\-]+)?:([a-zA-Z0-9\-]+):([a-z0-9\-]+)?:([0-9]{12})?:(.+)` 

 ** [UpdatedAt](#API_CreateDatasetIntegration_ResponseSyntax) **   <a name="cwoa-CreateDatasetIntegration-response-UpdatedAt"></a>
The timestamp when the dataset integration was last updated.  
Type: Timestamp

## Errors
<a name="API_CreateDatasetIntegration_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **   
 Indicates you don't have permissions to perform the requested operation. The user or role that is making the request must have at least one IAM permissions policy attached that grants the required permissions. For more information, see [Access management for AWS resources](https://docs.aws.amazon.com/IAM/latest/UserGuide/access.html) in the IAM user guide.     
 ** amznErrorType **   
 The name of the exception. 
HTTP Status Code: 400

 ** ConflictException **   
 The requested operation conflicts with the current state of the specified resource or with another request.     
 ** ResourceId **   
 The identifier of the resource which is in conflict with the requested operation.   
 ** ResourceType **   
 The type of the resource which is in conflict with the requested operation. 
HTTP Status Code: 409

 ** InternalServerException **   
 Indicates the request has failed to process because of an unknown server error, exception, or failure.     
 ** amznErrorType **   
 The name of the exception.   
 ** retryAfterSeconds **   
The number of seconds to wait before retrying the request.
HTTP Status Code: 500

 ** TooManyRequestsException **   
 The request throughput limit was exceeded.   
HTTP Status Code: 429

 ** ValidationException **   
 Indicates input validation failed. Check your request parameters and retry the request.     
 ** Errors **   
 The errors in the input which caused the exception. 
HTTP Status Code: 400

## See Also
<a name="API_CreateDatasetIntegration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/observabilityadmin-2018-05-10/CreateDatasetIntegration) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/observabilityadmin-2018-05-10/CreateDatasetIntegration) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/observabilityadmin-2018-05-10/CreateDatasetIntegration) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/observabilityadmin-2018-05-10/CreateDatasetIntegration) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/observabilityadmin-2018-05-10/CreateDatasetIntegration) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/observabilityadmin-2018-05-10/CreateDatasetIntegration) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/observabilityadmin-2018-05-10/CreateDatasetIntegration) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/observabilityadmin-2018-05-10/CreateDatasetIntegration) 
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/observabilityadmin-2018-05-10/CreateDatasetIntegration) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/observabilityadmin-2018-05-10/CreateDatasetIntegration) 