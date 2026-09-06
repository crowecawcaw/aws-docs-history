

# GetCentralizationRuleForOrganization
<a name="API_GetCentralizationRuleForOrganization"></a>

Retrieves the details of a specific organization centralization rule. This operation can only be called by the organization's management account or a delegated administrator account.

## Request Syntax
<a name="API_GetCentralizationRuleForOrganization_RequestSyntax"></a>

```
POST /GetCentralizationRuleForOrganization HTTP/1.1
Content-type: application/json

{
   "RuleIdentifier": "{{string}}"
}
```

## URI Request Parameters
<a name="API_GetCentralizationRuleForOrganization_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_GetCentralizationRuleForOrganization_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [RuleIdentifier](#API_GetCentralizationRuleForOrganization_RequestSyntax) **   <a name="cwoa-GetCentralizationRuleForOrganization-request-RuleIdentifier"></a>
The identifier (name or ARN) of the organization centralization rule to retrieve.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 1011.  
Required: Yes

## Response Syntax
<a name="API_GetCentralizationRuleForOrganization_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "CentralizationRule": { 
      "Destination": { 
         "Account": "string",
         "DestinationLogsConfiguration": { 
            "BackupConfiguration": { 
               "KmsKeyArn": "string",
               "Region": "string"
            },
            "LogGroupNameConfiguration": { 
               "LogGroupNamePattern": "string"
            },
            "LogsEncryptionConfiguration": { 
               "EncryptionConflictResolutionStrategy": "string",
               "EncryptionScope": "string",
               "EncryptionStrategy": "string",
               "KmsKeyArn": "string"
            },
            "TagPropagationConfiguration": { 
               "DestinationRoleArn": "string",
               "TagConflictResolutionStrategy": "string"
            }
         },
         "DestinationMetricsConfiguration": { 
            "BackupConfiguration": { 
               "Region": "string"
            }
         },
         "Region": "string"
      },
      "Source": { 
         "Regions": [ "string" ],
         "Scope": "string",
         "SourceLogsConfiguration": { 
            "DataSourceSelectionCriteria": "string",
            "EncryptedLogGroupStrategy": "string",
            "LogGroupSelectionCriteria": "string"
         },
         "SourceMetricsConfiguration": { 
            "MetricsSelectionCriteria": "string"
         }
      }
   },
   "CreatedRegion": "string",
   "CreatedTimeStamp": number,
   "CreatorAccountId": "string",
   "FailureReason": "string",
   "LastUpdateTimeStamp": number,
   "RuleArn": "string",
   "RuleHealth": "string",
   "RuleName": "string",
   "TagPropagationFailureReason": "string",
   "TagPropagationStatus": "string"
}
```

## Response Elements
<a name="API_GetCentralizationRuleForOrganization_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [CentralizationRule](#API_GetCentralizationRuleForOrganization_ResponseSyntax) **   <a name="cwoa-GetCentralizationRuleForOrganization-response-CentralizationRule"></a>
The configuration details for the organization centralization rule.  
Type: [CentralizationRule](API_CentralizationRule.md) object

 ** [CreatedRegion](#API_GetCentralizationRuleForOrganization_ResponseSyntax) **   <a name="cwoa-GetCentralizationRuleForOrganization-response-CreatedRegion"></a>
The AWS region where the organization centralization rule was created.  
Type: String  
Length Constraints: Minimum length of 1.

 ** [CreatedTimeStamp](#API_GetCentralizationRuleForOrganization_ResponseSyntax) **   <a name="cwoa-GetCentralizationRuleForOrganization-response-CreatedTimeStamp"></a>
The timestamp when the organization centralization rule was created.  
Type: Long

 ** [CreatorAccountId](#API_GetCentralizationRuleForOrganization_ResponseSyntax) **   <a name="cwoa-GetCentralizationRuleForOrganization-response-CreatorAccountId"></a>
The AWS Account that created the organization centralization rule.  
Type: String

 ** [FailureReason](#API_GetCentralizationRuleForOrganization_ResponseSyntax) **   <a name="cwoa-GetCentralizationRuleForOrganization-response-FailureReason"></a>
The reason why an organization centralization rule is marked UNHEALTHY.  
Type: String  
Valid Values: `TRUSTED_ACCESS_NOT_ENABLED | DESTINATION_ACCOUNT_NOT_IN_ORGANIZATION | INTERNAL_SERVER_ERROR` 

 ** [LastUpdateTimeStamp](#API_GetCentralizationRuleForOrganization_ResponseSyntax) **   <a name="cwoa-GetCentralizationRuleForOrganization-response-LastUpdateTimeStamp"></a>
The timestamp when the organization centralization rule was last updated.  
Type: Long

 ** [RuleArn](#API_GetCentralizationRuleForOrganization_ResponseSyntax) **   <a name="cwoa-GetCentralizationRuleForOrganization-response-RuleArn"></a>
The Amazon Resource Name (ARN) of the organization centralization rule.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 1011.  
Pattern: `arn:aws([a-z0-9\-]+)?:([a-zA-Z0-9\-]+):([a-z0-9\-]+)?:([0-9]{12})?:(.+)` 

 ** [RuleHealth](#API_GetCentralizationRuleForOrganization_ResponseSyntax) **   <a name="cwoa-GetCentralizationRuleForOrganization-response-RuleHealth"></a>
The health status of the organization centralization rule.  
Type: String  
Valid Values: `Healthy | Unhealthy | Provisioning` 

 ** [RuleName](#API_GetCentralizationRuleForOrganization_ResponseSyntax) **   <a name="cwoa-GetCentralizationRuleForOrganization-response-RuleName"></a>
The name of the organization centralization rule.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 100.  
Pattern: `[0-9A-Za-z-_.#/]+` 

 ** [TagPropagationFailureReason](#API_GetCentralizationRuleForOrganization_ResponseSyntax) **   <a name="cwoa-GetCentralizationRuleForOrganization-response-TagPropagationFailureReason"></a>
The reason tag propagation is unhealthy for this rule. Only present when `TagPropagationStatus` is `Unhealthy`.  
Type: String  
Valid Values: `RoleNotAssumable | RoleLacksPermissions` 

 ** [TagPropagationStatus](#API_GetCentralizationRuleForOrganization_ResponseSyntax) **   <a name="cwoa-GetCentralizationRuleForOrganization-response-TagPropagationStatus"></a>
The health status of tag propagation for this rule. This status is independent of the overall `RuleHealth` for log delivery. Returns `Healthy` when the most recent tag-propagation attempt succeeded, or `Unhealthy` when the most recent attempt failed.  
Type: String  
Valid Values: `Healthy | Unhealthy` 

## Errors
<a name="API_GetCentralizationRuleForOrganization_Errors"></a>

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
<a name="API_GetCentralizationRuleForOrganization_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/observabilityadmin-2018-05-10/GetCentralizationRuleForOrganization) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/observabilityadmin-2018-05-10/GetCentralizationRuleForOrganization) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/observabilityadmin-2018-05-10/GetCentralizationRuleForOrganization) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/observabilityadmin-2018-05-10/GetCentralizationRuleForOrganization) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/observabilityadmin-2018-05-10/GetCentralizationRuleForOrganization) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/observabilityadmin-2018-05-10/GetCentralizationRuleForOrganization) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/observabilityadmin-2018-05-10/GetCentralizationRuleForOrganization) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/observabilityadmin-2018-05-10/GetCentralizationRuleForOrganization) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/observabilityadmin-2018-05-10/GetCentralizationRuleForOrganization) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/observabilityadmin-2018-05-10/GetCentralizationRuleForOrganization) 