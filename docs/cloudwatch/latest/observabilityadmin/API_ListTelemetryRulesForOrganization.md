

# ListTelemetryRulesForOrganization
<a name="API_ListTelemetryRulesForOrganization"></a>

 Lists all telemetry rules in your organization. This operation can only be called by the organization's management account or a delegated administrator account. 

## Request Syntax
<a name="API_ListTelemetryRulesForOrganization_RequestSyntax"></a>

```
POST /ListTelemetryRulesForOrganization HTTP/1.1
Content-type: application/json

{
   "MaxResults": {{number}},
   "NextToken": "{{string}}",
   "RuleNamePrefix": "{{string}}",
   "SourceAccountIds": [ "{{string}}" ],
   "SourceOrganizationUnitIds": [ "{{string}}" ]
}
```

## URI Request Parameters
<a name="API_ListTelemetryRulesForOrganization_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_ListTelemetryRulesForOrganization_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [MaxResults](#API_ListTelemetryRulesForOrganization_RequestSyntax) **   <a name="cwoa-ListTelemetryRulesForOrganization-request-MaxResults"></a>
 The maximum number of organization telemetry rules to return in a single call.   
Type: Integer  
Valid Range: Minimum value of 1. Maximum value of 100.  
Required: No

 ** [NextToken](#API_ListTelemetryRulesForOrganization_RequestSyntax) **   <a name="cwoa-ListTelemetryRulesForOrganization-request-NextToken"></a>
 The token for the next set of results. A previous call generates this token.   
Type: String  
Required: No

 ** [RuleNamePrefix](#API_ListTelemetryRulesForOrganization_RequestSyntax) **   <a name="cwoa-ListTelemetryRulesForOrganization-request-RuleNamePrefix"></a>
 A string to filter organization telemetry rules whose names begin with the specified prefix.   
Type: String  
Required: No

 ** [SourceAccountIds](#API_ListTelemetryRulesForOrganization_RequestSyntax) **   <a name="cwoa-ListTelemetryRulesForOrganization-request-SourceAccountIds"></a>
 The list of account IDs to filter organization telemetry rules by their source accounts.   
Type: Array of strings  
Array Members: Minimum number of 1 item. Maximum number of 10 items.  
Length Constraints: Fixed length of 12.  
Pattern: `[0-9]{12}`   
Required: No

 ** [SourceOrganizationUnitIds](#API_ListTelemetryRulesForOrganization_RequestSyntax) **   <a name="cwoa-ListTelemetryRulesForOrganization-request-SourceOrganizationUnitIds"></a>
 The list of organizational unit IDs to filter organization telemetry rules by their source organizational units.   
Type: Array of strings  
Array Members: Minimum number of 1 item.  
Pattern: `ou-[0-9a-z]{4,32}-[a-z0-9]{8,32}`   
Required: No

## Response Syntax
<a name="API_ListTelemetryRulesForOrganization_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "NextToken": "string",
   "TelemetryRuleSummaries": [ 
      { 
         "CreatedTimeStamp": number,
         "LastUpdateTimeStamp": number,
         "ResourceType": "string",
         "RuleArn": "string",
         "RuleName": "string",
         "TelemetrySourceTypes": [ "string" ],
         "TelemetryType": "string"
      }
   ]
}
```

## Response Elements
<a name="API_ListTelemetryRulesForOrganization_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [NextToken](#API_ListTelemetryRulesForOrganization_ResponseSyntax) **   <a name="cwoa-ListTelemetryRulesForOrganization-response-NextToken"></a>
 A token to resume pagination of results.   
Type: String

 ** [TelemetryRuleSummaries](#API_ListTelemetryRulesForOrganization_ResponseSyntax) **   <a name="cwoa-ListTelemetryRulesForOrganization-response-TelemetryRuleSummaries"></a>
 A list of organization telemetry rule summaries.   
Type: Array of [TelemetryRuleSummary](API_TelemetryRuleSummary.md) objects

## Errors
<a name="API_ListTelemetryRulesForOrganization_Errors"></a>

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

 ** TooManyRequestsException **   
 The request throughput limit was exceeded.   
HTTP Status Code: 429

 ** ValidationException **   
 Indicates input validation failed. Check your request parameters and retry the request.     
 ** Errors **   
 The errors in the input which caused the exception. 
HTTP Status Code: 400

## See Also
<a name="API_ListTelemetryRulesForOrganization_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/observabilityadmin-2018-05-10/ListTelemetryRulesForOrganization) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/observabilityadmin-2018-05-10/ListTelemetryRulesForOrganization) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/observabilityadmin-2018-05-10/ListTelemetryRulesForOrganization) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/observabilityadmin-2018-05-10/ListTelemetryRulesForOrganization) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/observabilityadmin-2018-05-10/ListTelemetryRulesForOrganization) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/observabilityadmin-2018-05-10/ListTelemetryRulesForOrganization) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/observabilityadmin-2018-05-10/ListTelemetryRulesForOrganization) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/observabilityadmin-2018-05-10/ListTelemetryRulesForOrganization) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/observabilityadmin-2018-05-10/ListTelemetryRulesForOrganization) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/observabilityadmin-2018-05-10/ListTelemetryRulesForOrganization) 