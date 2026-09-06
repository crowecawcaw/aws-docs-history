

# ListCentralizationRulesForOrganization
<a name="API_ListCentralizationRulesForOrganization"></a>

Lists all centralization rules in your organization. This operation can only be called by the organization's management account or a delegated administrator account.

## Request Syntax
<a name="API_ListCentralizationRulesForOrganization_RequestSyntax"></a>

```
POST /ListCentralizationRulesForOrganization HTTP/1.1
Content-type: application/json

{
   "AllRegions": {{boolean}},
   "MaxResults": {{number}},
   "NextToken": "{{string}}",
   "RuleNamePrefix": "{{string}}"
}
```

## URI Request Parameters
<a name="API_ListCentralizationRulesForOrganization_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_ListCentralizationRulesForOrganization_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [AllRegions](#API_ListCentralizationRulesForOrganization_RequestSyntax) **   <a name="cwoa-ListCentralizationRulesForOrganization-request-AllRegions"></a>
A flag determining whether to return organization centralization rules from all regions or only the current region.  
Type: Boolean  
Required: No

 ** [MaxResults](#API_ListCentralizationRulesForOrganization_RequestSyntax) **   <a name="cwoa-ListCentralizationRulesForOrganization-request-MaxResults"></a>
The maximum number of organization centralization rules to return in a single call.  
Type: Integer  
Valid Range: Minimum value of 1. Maximum value of 100.  
Required: No

 ** [NextToken](#API_ListCentralizationRulesForOrganization_RequestSyntax) **   <a name="cwoa-ListCentralizationRulesForOrganization-request-NextToken"></a>
The token for the next set of results. A previous call generates this token.  
Type: String  
Required: No

 ** [RuleNamePrefix](#API_ListCentralizationRulesForOrganization_RequestSyntax) **   <a name="cwoa-ListCentralizationRulesForOrganization-request-RuleNamePrefix"></a>
A string to filter organization centralization rules whose names begin with the specified prefix.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 100.  
Required: No

## Response Syntax
<a name="API_ListCentralizationRulesForOrganization_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "CentralizationRuleSummaries": [ 
      { 
         "CreatedRegion": "string",
         "CreatedTimeStamp": number,
         "CreatorAccountId": "string",
         "DestinationAccountId": "string",
         "DestinationRegion": "string",
         "FailureReason": "string",
         "LastUpdateTimeStamp": number,
         "RuleArn": "string",
         "RuleHealth": "string",
         "RuleName": "string",
         "TagPropagationFailureReason": "string",
         "TagPropagationStatus": "string"
      }
   ],
   "NextToken": "string"
}
```

## Response Elements
<a name="API_ListCentralizationRulesForOrganization_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [CentralizationRuleSummaries](#API_ListCentralizationRulesForOrganization_ResponseSyntax) **   <a name="cwoa-ListCentralizationRulesForOrganization-response-CentralizationRuleSummaries"></a>
A list of centralization rule summaries.  
Type: Array of [CentralizationRuleSummary](API_CentralizationRuleSummary.md) objects

 ** [NextToken](#API_ListCentralizationRulesForOrganization_ResponseSyntax) **   <a name="cwoa-ListCentralizationRulesForOrganization-response-NextToken"></a>
A token to resume pagination of results.  
Type: String

## Errors
<a name="API_ListCentralizationRulesForOrganization_Errors"></a>

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
<a name="API_ListCentralizationRulesForOrganization_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/observabilityadmin-2018-05-10/ListCentralizationRulesForOrganization) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/observabilityadmin-2018-05-10/ListCentralizationRulesForOrganization) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/observabilityadmin-2018-05-10/ListCentralizationRulesForOrganization) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/observabilityadmin-2018-05-10/ListCentralizationRulesForOrganization) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/observabilityadmin-2018-05-10/ListCentralizationRulesForOrganization) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/observabilityadmin-2018-05-10/ListCentralizationRulesForOrganization) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/observabilityadmin-2018-05-10/ListCentralizationRulesForOrganization) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/observabilityadmin-2018-05-10/ListCentralizationRulesForOrganization) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/observabilityadmin-2018-05-10/ListCentralizationRulesForOrganization) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/observabilityadmin-2018-05-10/ListCentralizationRulesForOrganization) 