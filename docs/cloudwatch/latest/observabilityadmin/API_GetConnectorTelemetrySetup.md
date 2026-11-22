

# GetConnectorTelemetrySetup

Generates the artifacts that you use to create the infrastructure in your cloud provider that delivers the telemetry declared in the connector's telemetry manifest. This operation doesn't change any resources in your cloud provider or in AWS.

## Request Syntax
<a name="API_GetConnectorTelemetrySetup_RequestSyntax"></a>

```
POST /GetConnectorTelemetrySetup HTTP/1.1
Content-type: application/json

{
   "ConnectorIdentifier": "{{string}}",
   "Format": "{{string}}"
}
```

## URI Request Parameters
<a name="API_GetConnectorTelemetrySetup_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_GetConnectorTelemetrySetup_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [ConnectorIdentifier](#API_GetConnectorTelemetrySetup_RequestSyntax) **   <a name="cwoa-GetConnectorTelemetrySetup-request-ConnectorIdentifier"></a>
The connector whose telemetry manifest you want to generate the setup from. Specify one of the following:  
+ The Amazon Resource Name (ARN) of the connector
+ The ID of the connector
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 1011.  
Pattern: `([a-z0-9]+|arn:aws[a-z0-9\-]*:observabilityadmin:[a-z0-9-]+:[0-9]{12}:connector/(azure/)?[a-z0-9]+)`   
Required: Yes

 ** [Format](#API_GetConnectorTelemetrySetup_RequestSyntax) **   <a name="cwoa-GetConnectorTelemetrySetup-request-Format"></a>
The format of the setup artifacts. If you omit this value, the service uses the default format for the connector's provider (`BICEP` for an Azure connector). If the provider doesn't support the format, the service returns a `ValidationException`.  
Type: String  
Valid Values: `BICEP`   
Required: No

## Response Syntax
<a name="API_GetConnectorTelemetrySetup_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "Artifacts": [ 
      { 
         "Content": "string",
         "ContentType": "string",
         "FileName": "string",
         "Format": "string"
      }
   ],
   "Format": "string",
   "ManifestVersion": number,
   "Provider": "string",
   "RequiredPermissionsToApply": [ "string" ]
}
```

## Response Elements
<a name="API_GetConnectorTelemetrySetup_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Artifacts](#API_GetConnectorTelemetrySetup_ResponseSyntax) **   <a name="cwoa-GetConnectorTelemetrySetup-response-Artifacts"></a>
The setup artifacts to apply in your cloud provider.  
Type: Array of [SetupArtifact](API_SetupArtifact.md) objects  
Array Members: Minimum number of 0 items. Maximum number of 50 items.

 ** [Format](#API_GetConnectorTelemetrySetup_ResponseSyntax) **   <a name="cwoa-GetConnectorTelemetrySetup-response-Format"></a>
The format of the setup artifacts.  
Type: String  
Valid Values: `BICEP` 

 ** [ManifestVersion](#API_GetConnectorTelemetrySetup_ResponseSyntax) **   <a name="cwoa-GetConnectorTelemetrySetup-response-ManifestVersion"></a>
The version of the telemetry manifest that the service generated the setup artifacts from.  
Type: Long

 ** [Provider](#API_GetConnectorTelemetrySetup_ResponseSyntax) **   <a name="cwoa-GetConnectorTelemetrySetup-response-Provider"></a>
The cloud provider that the setup artifacts are for.  
Type: String  
Valid Values: `AZURE` 

 ** [RequiredPermissionsToApply](#API_GetConnectorTelemetrySetup_ResponseSyntax) **   <a name="cwoa-GetConnectorTelemetrySetup-response-RequiredPermissionsToApply"></a>
The permissions or roles in your cloud provider that you need to apply the artifacts, for example Azure Contributor and User Access Administrator.  
Type: Array of strings  
Array Members: Minimum number of 0 items. Maximum number of 50 items.  
Length Constraints: Minimum length of 1. Maximum length of 256.

## Errors
<a name="API_GetConnectorTelemetrySetup_Errors"></a>

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
<a name="API_GetConnectorTelemetrySetup_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/observabilityadmin-2018-05-10/GetConnectorTelemetrySetup) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/observabilityadmin-2018-05-10/GetConnectorTelemetrySetup) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/observabilityadmin-2018-05-10/GetConnectorTelemetrySetup) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/observabilityadmin-2018-05-10/GetConnectorTelemetrySetup) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/observabilityadmin-2018-05-10/GetConnectorTelemetrySetup) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/observabilityadmin-2018-05-10/GetConnectorTelemetrySetup) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/observabilityadmin-2018-05-10/GetConnectorTelemetrySetup) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/observabilityadmin-2018-05-10/GetConnectorTelemetrySetup) 
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/observabilityadmin-2018-05-10/GetConnectorTelemetrySetup) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/observabilityadmin-2018-05-10/GetConnectorTelemetrySetup) 