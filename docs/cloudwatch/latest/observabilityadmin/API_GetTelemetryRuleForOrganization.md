

# GetTelemetryRuleForOrganization
<a name="API_GetTelemetryRuleForOrganization"></a>

 Retrieves the details of a specific organization telemetry rule. This operation can only be called by the organization's management account or a delegated administrator account. 

## Request Syntax
<a name="API_GetTelemetryRuleForOrganization_RequestSyntax"></a>

```
POST /GetTelemetryRuleForOrganization HTTP/1.1
Content-type: application/json

{
   "RuleIdentifier": "{{string}}"
}
```

## URI Request Parameters
<a name="API_GetTelemetryRuleForOrganization_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_GetTelemetryRuleForOrganization_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [RuleIdentifier](#API_GetTelemetryRuleForOrganization_RequestSyntax) **   <a name="cwoa-GetTelemetryRuleForOrganization-request-RuleIdentifier"></a>
 The identifier (name or ARN) of the organization telemetry rule to retrieve.   
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 1011.  
Required: Yes

## Response Syntax
<a name="API_GetTelemetryRuleForOrganization_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "CreatedTimeStamp": number,
   "HomeRegion": "string",
   "IsReplicated": boolean,
   "LastUpdateTimeStamp": number,
   "RegionStatuses": [ 
      { 
         "FailureReason": "string",
         "Region": "string",
         "RuleArn": "string",
         "Status": "string"
      }
   ],
   "RuleArn": "string",
   "RuleName": "string",
   "TelemetryRule": { 
      "AllowFieldUpdates": boolean,
      "AllRegions": boolean,
      "DestinationConfiguration": { 
         "CloudtrailParameters": { 
            "AdvancedEventSelectors": [ 
               { 
                  "FieldSelectors": [ 
                     { 
                        "EndsWith": [ "string" ],
                        "Equals": [ "string" ],
                        "Field": "string",
                        "NotEndsWith": [ "string" ],
                        "NotEquals": [ "string" ],
                        "NotStartsWith": [ "string" ],
                        "StartsWith": [ "string" ]
                     }
                  ],
                  "Name": "string"
               }
            ]
         },
         "DestinationPattern": "string",
         "DestinationType": "string",
         "ELBLoadBalancerLoggingParameters": { 
            "FieldDelimiter": "string",
            "OutputFormat": "string"
         },
         "KmsKeyArn": "string",
         "LogDeliveryParameters": { 
            "LogTypes": [ "string" ]
         },
         "MskMonitoringParameters": { 
            "EnhancedMonitoring": "string"
         },
         "RetentionInDays": number,
         "VPCFlowLogParameters": { 
            "LogFormat": "string",
            "MaxAggregationInterval": number,
            "TrafficType": "string"
         },
         "WAFLoggingParameters": { 
            "LoggingFilter": { 
               "DefaultBehavior": "string",
               "Filters": [ 
                  { 
                     "Behavior": "string",
                     "Conditions": [ 
                        { 
                           "ActionCondition": { 
                              "Action": "string"
                           },
                           "LabelNameCondition": { 
                              "LabelName": "string"
                           }
                        }
                     ],
                     "Requirement": "string"
                  }
               ]
            },
            "LogType": "string",
            "RedactedFields": [ 
               { 
                  "Method": "string",
                  "QueryString": "string",
                  "SingleHeader": { 
                     "Name": "string"
                  },
                  "UriPath": "string"
               }
            ]
         }
      },
      "Regions": [ "string" ],
      "ResourceType": "string",
      "Scope": "string",
      "SelectionCriteria": "string",
      "TelemetrySourceTypes": [ "string" ],
      "TelemetryType": "string"
   }
}
```

## Response Elements
<a name="API_GetTelemetryRuleForOrganization_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [CreatedTimeStamp](#API_GetTelemetryRuleForOrganization_ResponseSyntax) **   <a name="cwoa-GetTelemetryRuleForOrganization-response-CreatedTimeStamp"></a>
 The timestamp when the organization telemetry rule was created.   
Type: Long

 ** [HomeRegion](#API_GetTelemetryRuleForOrganization_ResponseSyntax) **   <a name="cwoa-GetTelemetryRuleForOrganization-response-HomeRegion"></a>
 The AWS Region where the organization telemetry rule was originally created. For replicated rules in spoke regions, this indicates the region that manages the rule. For rules created without multi-region scope, this field is not present.   
Type: String  
Length Constraints: Minimum length of 1.

 ** [IsReplicated](#API_GetTelemetryRuleForOrganization_ResponseSyntax) **   <a name="cwoa-GetTelemetryRuleForOrganization-response-IsReplicated"></a>
 Indicates whether this organization telemetry rule is a replica that was created in this region through multi-region fan-out from the home region. Replicated rules cannot be directly updated or deleted in the spoke region. To modify a replicated rule, make changes in the home region.   
Type: Boolean

 ** [LastUpdateTimeStamp](#API_GetTelemetryRuleForOrganization_ResponseSyntax) **   <a name="cwoa-GetTelemetryRuleForOrganization-response-LastUpdateTimeStamp"></a>
 The timestamp when the organization telemetry rule was last updated.   
Type: Long

 ** [RegionStatuses](#API_GetTelemetryRuleForOrganization_ResponseSyntax) **   <a name="cwoa-GetTelemetryRuleForOrganization-response-RegionStatuses"></a>
 A list of per-region replication statuses for the organization telemetry rule. Each entry indicates the replication status of the rule in a specific spoke region. This field is only present for rules created with multi-region scope.   
Type: Array of [RegionStatus](API_RegionStatus.md) objects

 ** [RuleArn](#API_GetTelemetryRuleForOrganization_ResponseSyntax) **   <a name="cwoa-GetTelemetryRuleForOrganization-response-RuleArn"></a>
 The Amazon Resource Name (ARN) of the organization telemetry rule.   
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 1011.  
Pattern: `arn:aws([a-z0-9\-]+)?:([a-zA-Z0-9\-]+):([a-z0-9\-]+)?:([0-9]{12})?:(.+)` 

 ** [RuleName](#API_GetTelemetryRuleForOrganization_ResponseSyntax) **   <a name="cwoa-GetTelemetryRuleForOrganization-response-RuleName"></a>
 The name of the organization telemetry rule.   
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 100.  
Pattern: `[0-9A-Za-z-_.#/]+` 

 ** [TelemetryRule](#API_GetTelemetryRuleForOrganization_ResponseSyntax) **   <a name="cwoa-GetTelemetryRuleForOrganization-response-TelemetryRule"></a>
 The configuration details of the organization telemetry rule.   
Type: [TelemetryRule](API_TelemetryRule.md) object

## Errors
<a name="API_GetTelemetryRuleForOrganization_Errors"></a>

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
<a name="API_GetTelemetryRuleForOrganization_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/observabilityadmin-2018-05-10/GetTelemetryRuleForOrganization) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/observabilityadmin-2018-05-10/GetTelemetryRuleForOrganization) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/observabilityadmin-2018-05-10/GetTelemetryRuleForOrganization) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/observabilityadmin-2018-05-10/GetTelemetryRuleForOrganization) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/observabilityadmin-2018-05-10/GetTelemetryRuleForOrganization) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/observabilityadmin-2018-05-10/GetTelemetryRuleForOrganization) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/observabilityadmin-2018-05-10/GetTelemetryRuleForOrganization) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/observabilityadmin-2018-05-10/GetTelemetryRuleForOrganization) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/observabilityadmin-2018-05-10/GetTelemetryRuleForOrganization) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/observabilityadmin-2018-05-10/GetTelemetryRuleForOrganization) 