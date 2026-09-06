

# CreateCustomPlugin
<a name="API_CreateCustomPlugin"></a>

Creates a custom plugin using the specified properties.

## Request Syntax
<a name="API_CreateCustomPlugin_RequestSyntax"></a>

```
POST /v1/custom-plugins HTTP/1.1
Content-type: application/json

{
   "contentType": "{{string}}",
   "description": "{{string}}",
   "location": { 
      "s3Location": { 
         "bucketArn": "{{string}}",
         "fileKey": "{{string}}",
         "objectVersion": "{{string}}"
      }
   },
   "name": "{{string}}",
   "tags": { 
      "{{string}}" : "{{string}}" 
   }
}
```

## URI Request Parameters
<a name="API_CreateCustomPlugin_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_CreateCustomPlugin_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [contentType](#API_CreateCustomPlugin_RequestSyntax) **   <a name="MSKC-CreateCustomPlugin-request-contentType"></a>
The type of the plugin file.  
Type: String  
Valid Values: `JAR | ZIP`   
Required: Yes

 ** [description](#API_CreateCustomPlugin_RequestSyntax) **   <a name="MSKC-CreateCustomPlugin-request-description"></a>
A summary description of the custom plugin.  
Type: String  
Length Constraints: Minimum length of 0. Maximum length of 1024.  
Required: No

 ** [location](#API_CreateCustomPlugin_RequestSyntax) **   <a name="MSKC-CreateCustomPlugin-request-location"></a>
Information about the location of a custom plugin.  
Type: [CustomPluginLocation](API_CustomPluginLocation.md) object  
Required: Yes

 ** [name](#API_CreateCustomPlugin_RequestSyntax) **   <a name="MSKC-CreateCustomPlugin-request-name"></a>
The name of the custom plugin.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 128.  
Required: Yes

 ** [tags](#API_CreateCustomPlugin_RequestSyntax) **   <a name="MSKC-CreateCustomPlugin-request-tags"></a>
The tags you want to attach to the custom plugin.  
Type: String to string map  
Map Entries: Minimum number of 0 items. Maximum number of 200 items.  
Key Length Constraints: Minimum length of 1. Maximum length of 128.  
Value Length Constraints: Minimum length of 0. Maximum length of 256.  
Required: No

## Response Syntax
<a name="API_CreateCustomPlugin_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "customPluginArn": "string",
   "customPluginState": "string",
   "name": "string",
   "revision": number
}
```

## Response Elements
<a name="API_CreateCustomPlugin_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [customPluginArn](#API_CreateCustomPlugin_ResponseSyntax) **   <a name="MSKC-CreateCustomPlugin-response-customPluginArn"></a>
The Amazon Resource Name (ARN) that Amazon assigned to the custom plugin.  
Type: String

 ** [customPluginState](#API_CreateCustomPlugin_ResponseSyntax) **   <a name="MSKC-CreateCustomPlugin-response-customPluginState"></a>
The state of the custom plugin.  
Type: String  
Valid Values: `CREATING | CREATE_FAILED | ACTIVE | UPDATING | UPDATE_FAILED | DELETING` 

 ** [name](#API_CreateCustomPlugin_ResponseSyntax) **   <a name="MSKC-CreateCustomPlugin-response-name"></a>
The name of the custom plugin.  
Type: String

 ** [revision](#API_CreateCustomPlugin_ResponseSyntax) **   <a name="MSKC-CreateCustomPlugin-response-revision"></a>
The revision of the custom plugin.  
Type: Long

## Errors
<a name="API_CreateCustomPlugin_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** BadRequestException **   
HTTP Status Code 400: Bad request due to incorrect input. Correct your request and then retry it.  
HTTP Status Code: 400

 ** ConflictException **   
HTTP Status Code 409: Conflict. A resource with this name already exists. Retry your request with another name.  
HTTP Status Code: 409

 ** ForbiddenException **   
HTTP Status Code 403: Access forbidden. Correct your credentials and then retry your request.  
HTTP Status Code: 403

 ** InternalServerErrorException **   
HTTP Status Code 500: Unexpected internal server error. Retrying your request might resolve the issue.  
HTTP Status Code: 500

 ** NotFoundException **   
HTTP Status Code 404: Resource not found due to incorrect input. Correct your request and then retry it.  
HTTP Status Code: 404

 ** ServiceUnavailableException **   
HTTP Status Code 503: Service Unavailable. Retrying your request in some time might resolve the issue.  
HTTP Status Code: 503

 ** TooManyRequestsException **   
HTTP Status Code 429: Limit exceeded. Resource limit reached.  
HTTP Status Code: 429

 ** UnauthorizedException **   
HTTP Status Code 401: Unauthorized request. The provided credentials couldn't be validated.  
HTTP Status Code: 401

## See Also
<a name="API_CreateCustomPlugin_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/kafkaconnect-2021-09-14/CreateCustomPlugin) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/kafkaconnect-2021-09-14/CreateCustomPlugin) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/kafkaconnect-2021-09-14/CreateCustomPlugin) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/kafkaconnect-2021-09-14/CreateCustomPlugin) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/kafkaconnect-2021-09-14/CreateCustomPlugin) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/kafkaconnect-2021-09-14/CreateCustomPlugin) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/kafkaconnect-2021-09-14/CreateCustomPlugin) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/kafkaconnect-2021-09-14/CreateCustomPlugin) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/kafkaconnect-2021-09-14/CreateCustomPlugin) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/kafkaconnect-2021-09-14/CreateCustomPlugin) 