

# CreateConnector

Creates a connector to a third-party cloud provider. With a connector, you can discover resources in the provider and collect their telemetry. Currently, Microsoft Azure is the only supported provider.

## Request Syntax
<a name="API_CreateConnector_RequestSyntax"></a>

```
POST /CreateConnector HTTP/1.1
Content-type: application/json

{
   "ClientToken": "{{string}}",
   "ConnectorConfiguration": { ... },
   "Name": "{{string}}",
   "RoleArn": "{{string}}",
   "Tags": { 
      "{{string}}" : "{{string}}" 
   }
}
```

## URI Request Parameters
<a name="API_CreateConnector_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_CreateConnector_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [ClientToken](#API_CreateConnector_RequestSyntax) **   <a name="cwoa-CreateConnector-request-ClientToken"></a>
A unique, case-sensitive identifier that you provide to ensure the operation completes no more than one time. If you use an AWS SDK, the SDK generates this value and reuses it on retries. If this token matches a previous request with the same parameters, the service returns the connector from the first request without an error. If you use the same token with different parameters, including different tags, the service returns a `ValidationException`. This operation is idempotent when you use the same token and parameters.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 64.  
Pattern: `[!-~]+`   
Required: No

 ** [ConnectorConfiguration](#API_CreateConnector_RequestSyntax) **   <a name="cwoa-CreateConnector-request-ConnectorConfiguration"></a>
The configuration for connecting to the third-party cloud provider.  
Type: [ConnectorConfiguration](API_ConnectorConfiguration.md) object  
 **Note: **This object is a Union. Only one member of this object can be specified or returned.  
Required: Yes

 ** [Name](#API_CreateConnector_RequestSyntax) **   <a name="cwoa-CreateConnector-request-Name"></a>
The name of the connector. The name must be unique in the account and Region (case-sensitive). If another connector already uses the name, the request fails with a `ConflictException`.  
The name can contain letters, digits, hyphens (-), underscores (\_) and periods (.), and must start with a letter.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 256.  
Pattern: `[a-zA-Z][a-zA-Z0-9\-_.]*`   
Required: Yes

 ** [RoleArn](#API_CreateConnector_RequestSyntax) **   <a name="cwoa-CreateConnector-request-RoleArn"></a>
The Amazon Resource Name (ARN) of the AWS Identity and Access Management (IAM) role that CloudWatch assumes to get credentials for the third-party cloud provider. The role must trust the Amazon CloudWatch Observability Admin service principal, `observabilityadmin.amazonaws.com`. The role must also allow `sts:GetWebIdentityToken` for the provider's token exchange audience.  
Type: String  
Length Constraints: Minimum length of 20. Maximum length of 1011.  
Pattern: `arn:aws([a-z0-9\-]+)?:([a-zA-Z0-9\-]+):([a-z0-9\-]+)?:([0-9]{12})?:(.+)`   
Required: Yes

 ** [Tags](#API_CreateConnector_RequestSyntax) **   <a name="cwoa-CreateConnector-request-Tags"></a>
The tags that you want to apply to the connector.  
Type: String to string map  
Map Entries: Maximum number of 50 items.  
Key Length Constraints: Minimum length of 1. Maximum length of 128.  
Key Pattern: `([\p{L}\p{Z}\p{N}_.:/=+\-@]*)`   
Value Length Constraints: Minimum length of 0. Maximum length of 256.  
Value Pattern: `([\p{L}\p{Z}\p{N}_.:/=+\-@]*)`   
Required: No

## Response Syntax
<a name="API_CreateConnector_ResponseSyntax"></a>

```
HTTP/1.1 201
Content-type: application/json

{
   "Connector": { 
      "Arn": "string",
      "ConnectorConfiguration": { ... },
      "CreatedTimeStamp": number,
      "Name": "string",
      "Provider": "string",
      "RoleArn": "string"
   }
}
```

## Response Elements
<a name="API_CreateConnector_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 201 response.

The following data is returned in JSON format by the service.

 ** [Connector](#API_CreateConnector_ResponseSyntax) **   <a name="cwoa-CreateConnector-response-Connector"></a>
The connector that this request created.  
Type: [Connector](API_Connector.md) object

## Errors
<a name="API_CreateConnector_Errors"></a>

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

 ** ServiceQuotaExceededException **   
 The requested operation would exceed the allowed quota for the specified resource type.     
 ** amznErrorType **   
 The name of the exception.   
 ** QuotaCode **   
 The code for the exceeded service quota.   
 ** ResourceId **   
 The identifier of the resource which exceeds the service quota.   
 ** ResourceType **   
 The type of the resource which exceeds the service quota.   
 ** ServiceCode **   
 The code for the service of the exceeded quota. 
HTTP Status Code: 402

 ** TooManyRequestsException **   
 The request throughput limit was exceeded.   
HTTP Status Code: 429

 ** ValidationException **   
 Indicates input validation failed. Check your request parameters and retry the request.     
 ** Errors **   
 The errors in the input which caused the exception. 
HTTP Status Code: 400

## See Also
<a name="API_CreateConnector_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/observabilityadmin-2018-05-10/CreateConnector) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/observabilityadmin-2018-05-10/CreateConnector) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/observabilityadmin-2018-05-10/CreateConnector) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/observabilityadmin-2018-05-10/CreateConnector) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/observabilityadmin-2018-05-10/CreateConnector) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/observabilityadmin-2018-05-10/CreateConnector) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/observabilityadmin-2018-05-10/CreateConnector) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/observabilityadmin-2018-05-10/CreateConnector) 
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/observabilityadmin-2018-05-10/CreateConnector) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/observabilityadmin-2018-05-10/CreateConnector) 