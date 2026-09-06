

# DeleteTelemetryRuleForOrganization
<a name="API_DeleteTelemetryRuleForOrganization"></a>

 Deletes an organization-wide telemetry rule. This operation can only be called by the organization's management account or a delegated administrator account. 

## Request Syntax
<a name="API_DeleteTelemetryRuleForOrganization_RequestSyntax"></a>

```
POST /DeleteTelemetryRuleForOrganization HTTP/1.1
Content-type: application/json

{
   "RuleIdentifier": "{{string}}"
}
```

## URI Request Parameters
<a name="API_DeleteTelemetryRuleForOrganization_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_DeleteTelemetryRuleForOrganization_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [RuleIdentifier](#API_DeleteTelemetryRuleForOrganization_RequestSyntax) **   <a name="cwoa-DeleteTelemetryRuleForOrganization-request-RuleIdentifier"></a>
 The identifier (name or ARN) of the organization telemetry rule to delete.   
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 1011.  
Required: Yes

## Response Syntax
<a name="API_DeleteTelemetryRuleForOrganization_ResponseSyntax"></a>

```
HTTP/1.1 200
```

## Response Elements
<a name="API_DeleteTelemetryRuleForOrganization_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_DeleteTelemetryRuleForOrganization_Errors"></a>

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
<a name="API_DeleteTelemetryRuleForOrganization_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/observabilityadmin-2018-05-10/DeleteTelemetryRuleForOrganization) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/observabilityadmin-2018-05-10/DeleteTelemetryRuleForOrganization) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/observabilityadmin-2018-05-10/DeleteTelemetryRuleForOrganization) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/observabilityadmin-2018-05-10/DeleteTelemetryRuleForOrganization) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/observabilityadmin-2018-05-10/DeleteTelemetryRuleForOrganization) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/observabilityadmin-2018-05-10/DeleteTelemetryRuleForOrganization) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/observabilityadmin-2018-05-10/DeleteTelemetryRuleForOrganization) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/observabilityadmin-2018-05-10/DeleteTelemetryRuleForOrganization) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/observabilityadmin-2018-05-10/DeleteTelemetryRuleForOrganization) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/observabilityadmin-2018-05-10/DeleteTelemetryRuleForOrganization) 