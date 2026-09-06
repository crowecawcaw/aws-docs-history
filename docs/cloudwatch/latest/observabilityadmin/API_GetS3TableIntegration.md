

# GetS3TableIntegration
<a name="API_GetS3TableIntegration"></a>

Retrieves information about a specific S3 Table integration, including its configuration, status, and metadata.

## Request Syntax
<a name="API_GetS3TableIntegration_RequestSyntax"></a>

```
POST /GetS3TableIntegration HTTP/1.1
Content-type: application/json

{
   "Arn": "{{string}}"
}
```

## URI Request Parameters
<a name="API_GetS3TableIntegration_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_GetS3TableIntegration_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [Arn](#API_GetS3TableIntegration_RequestSyntax) **   <a name="cwoa-GetS3TableIntegration-request-Arn"></a>
The Amazon Resource Name (ARN) of the S3 Table integration to retrieve.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 1011.  
Pattern: `arn:aws([a-z0-9\-]+)?:([a-zA-Z0-9\-]+):([a-z0-9\-]+)?:([0-9]{12})?:(.+)`   
Required: Yes

## Response Syntax
<a name="API_GetS3TableIntegration_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "Arn": "string",
   "CreatedTimeStamp": number,
   "DestinationTableBucketArn": "string",
   "Encryption": { 
      "KmsKeyArn": "string",
      "SseAlgorithm": "string"
   },
   "RoleArn": "string",
   "Status": "string"
}
```

## Response Elements
<a name="API_GetS3TableIntegration_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Arn](#API_GetS3TableIntegration_ResponseSyntax) **   <a name="cwoa-GetS3TableIntegration-response-Arn"></a>
The Amazon Resource Name (ARN) of the S3 Table integration.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 1011.  
Pattern: `arn:aws([a-z0-9\-]+)?:([a-zA-Z0-9\-]+):([a-z0-9\-]+)?:([0-9]{12})?:(.+)` 

 ** [CreatedTimeStamp](#API_GetS3TableIntegration_ResponseSyntax) **   <a name="cwoa-GetS3TableIntegration-response-CreatedTimeStamp"></a>
The timestamp when the S3 Table integration was created.  
Type: Long

 ** [DestinationTableBucketArn](#API_GetS3TableIntegration_ResponseSyntax) **   <a name="cwoa-GetS3TableIntegration-response-DestinationTableBucketArn"></a>
The Amazon Resource Name (ARN) of the S3 bucket used as the destination for the table data.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 1011.  
Pattern: `arn:aws([a-z0-9\-]+)?:([a-zA-Z0-9\-]+):([a-z0-9\-]+)?:([0-9]{12})?:(.+)` 

 ** [Encryption](#API_GetS3TableIntegration_ResponseSyntax) **   <a name="cwoa-GetS3TableIntegration-response-Encryption"></a>
The encryption configuration for the S3 Table integration.  
Type: [Encryption](API_Encryption.md) object

 ** [RoleArn](#API_GetS3TableIntegration_ResponseSyntax) **   <a name="cwoa-GetS3TableIntegration-response-RoleArn"></a>
The Amazon Resource Name (ARN) of the IAM role used by the S3 Table integration.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 1011.  
Pattern: `arn:aws([a-z0-9\-]+)?:([a-zA-Z0-9\-]+):([a-z0-9\-]+)?:([0-9]{12})?:(.+)` 

 ** [Status](#API_GetS3TableIntegration_ResponseSyntax) **   <a name="cwoa-GetS3TableIntegration-response-Status"></a>
The current status of the S3 Table integration.  
Type: String  
Valid Values: `ACTIVE | DELETING` 

## Errors
<a name="API_GetS3TableIntegration_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **   
 Indicates you don't have permissions to perform the requested operation. The user or role that is making the request must have at least one IAM permissions policy attached that grants the required permissions. For more information, see [Access management for AWS resources](https://docs.aws.amazon.com/IAM/latest/UserGuide/access.html) in the IAM user guide.     
 ** amznErrorType **   
 The name of the exception. 
HTTP Status Code: 400

 ** InternalServerException **   
 Indicates the request has failed to process because of an unknown server error, exception, or failure.     
 ** amznErrorType **   
 The name of the exception.   
 ** retryAfterSeconds **   
The number of seconds to wait before retrying the request.
HTTP Status Code: 500

 ** ResourceNotFoundException **   
 The specified resource (such as a telemetry rule) could not be found.     
 ** ResourceId **   
 The identifier of the resource which could not be found.   
 ** ResourceType **   
 The type of the resource which could not be found. 
HTTP Status Code: 404

 ** TooManyRequestsException **   
 The request throughput limit was exceeded.   
HTTP Status Code: 429

 ** ValidationException **   
 Indicates input validation failed. Check your request parameters and retry the request.     
 ** Errors **   
 The errors in the input which caused the exception. 
HTTP Status Code: 400

## See Also
<a name="API_GetS3TableIntegration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/observabilityadmin-2018-05-10/GetS3TableIntegration) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/observabilityadmin-2018-05-10/GetS3TableIntegration) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/observabilityadmin-2018-05-10/GetS3TableIntegration) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/observabilityadmin-2018-05-10/GetS3TableIntegration) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/observabilityadmin-2018-05-10/GetS3TableIntegration) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/observabilityadmin-2018-05-10/GetS3TableIntegration) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/observabilityadmin-2018-05-10/GetS3TableIntegration) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/observabilityadmin-2018-05-10/GetS3TableIntegration) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/observabilityadmin-2018-05-10/GetS3TableIntegration) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/observabilityadmin-2018-05-10/GetS3TableIntegration) 