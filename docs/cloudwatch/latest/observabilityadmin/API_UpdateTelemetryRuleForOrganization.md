

# UpdateTelemetryRuleForOrganization
<a name="API_UpdateTelemetryRuleForOrganization"></a>

 Updates an existing telemetry rule that applies across an AWS Organization. This operation can only be called by the organization's management account or a delegated administrator account. 

## Request Syntax
<a name="API_UpdateTelemetryRuleForOrganization_RequestSyntax"></a>

```
POST /UpdateTelemetryRuleForOrganization HTTP/1.1
Content-type: application/json

{
   "Rule": { 
      "AllowFieldUpdates": {{boolean}},
      "AllRegions": {{boolean}},
      "DestinationConfiguration": { 
         "CloudtrailParameters": { 
            "AdvancedEventSelectors": [ 
               { 
                  "FieldSelectors": [ 
                     { 
                        "EndsWith": [ "{{string}}" ],
                        "Equals": [ "{{string}}" ],
                        "Field": "{{string}}",
                        "NotEndsWith": [ "{{string}}" ],
                        "NotEquals": [ "{{string}}" ],
                        "NotStartsWith": [ "{{string}}" ],
                        "StartsWith": [ "{{string}}" ]
                     }
                  ],
                  "Name": "{{string}}"
               }
            ]
         },
         "DestinationPattern": "{{string}}",
         "DestinationType": "{{string}}",
         "ELBLoadBalancerLoggingParameters": { 
            "FieldDelimiter": "{{string}}",
            "OutputFormat": "{{string}}"
         },
         "KmsKeyArn": "{{string}}",
         "LogDeliveryParameters": { 
            "LogTypes": [ "{{string}}" ]
         },
         "MskMonitoringParameters": { 
            "EnhancedMonitoring": "{{string}}"
         },
         "RetentionInDays": {{number}},
         "VPCFlowLogParameters": { 
            "LogFormat": "{{string}}",
            "MaxAggregationInterval": {{number}},
            "TrafficType": "{{string}}"
         },
         "WAFLoggingParameters": { 
            "LoggingFilter": { 
               "DefaultBehavior": "{{string}}",
               "Filters": [ 
                  { 
                     "Behavior": "{{string}}",
                     "Conditions": [ 
                        { 
                           "ActionCondition": { 
                              "Action": "{{string}}"
                           },
                           "LabelNameCondition": { 
                              "LabelName": "{{string}}"
                           }
                        }
                     ],
                     "Requirement": "{{string}}"
                  }
               ]
            },
            "LogType": "{{string}}",
            "RedactedFields": [ 
               { 
                  "Method": "{{string}}",
                  "QueryString": "{{string}}",
                  "SingleHeader": { 
                     "Name": "{{string}}"
                  },
                  "UriPath": "{{string}}"
               }
            ]
         }
      },
      "Regions": [ "{{string}}" ],
      "ResourceType": "{{string}}",
      "Scope": "{{string}}",
      "SelectionCriteria": "{{string}}",
      "TelemetrySourceTypes": [ "{{string}}" ],
      "TelemetryType": "{{string}}"
   },
   "RuleIdentifier": "{{string}}"
}
```

## URI Request Parameters
<a name="API_UpdateTelemetryRuleForOrganization_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_UpdateTelemetryRuleForOrganization_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [Rule](#API_UpdateTelemetryRuleForOrganization_RequestSyntax) **   <a name="cwoa-UpdateTelemetryRuleForOrganization-request-Rule"></a>
 The new configuration details for the organization telemetry rule, including resource type, telemetry type, and destination configuration.   
Type: [TelemetryRule](API_TelemetryRule.md) object  
Required: Yes

 ** [RuleIdentifier](#API_UpdateTelemetryRuleForOrganization_RequestSyntax) **   <a name="cwoa-UpdateTelemetryRuleForOrganization-request-RuleIdentifier"></a>
 The identifier (name or ARN) of the organization telemetry rule to update.   
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 1011.  
Required: Yes

## Response Syntax
<a name="API_UpdateTelemetryRuleForOrganization_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "RuleArn": "string"
}
```

## Response Elements
<a name="API_UpdateTelemetryRuleForOrganization_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [RuleArn](#API_UpdateTelemetryRuleForOrganization_ResponseSyntax) **   <a name="cwoa-UpdateTelemetryRuleForOrganization-response-RuleArn"></a>
 The Amazon Resource Name (ARN) of the updated organization telemetry rule.   
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 1011.  
Pattern: `arn:aws([a-z0-9\-]+)?:([a-zA-Z0-9\-]+):([a-z0-9\-]+)?:([0-9]{12})?:(.+)` 

## Errors
<a name="API_UpdateTelemetryRuleForOrganization_Errors"></a>

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
<a name="API_UpdateTelemetryRuleForOrganization_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/observabilityadmin-2018-05-10/UpdateTelemetryRuleForOrganization) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/observabilityadmin-2018-05-10/UpdateTelemetryRuleForOrganization) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/observabilityadmin-2018-05-10/UpdateTelemetryRuleForOrganization) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/observabilityadmin-2018-05-10/UpdateTelemetryRuleForOrganization) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/observabilityadmin-2018-05-10/UpdateTelemetryRuleForOrganization) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/observabilityadmin-2018-05-10/UpdateTelemetryRuleForOrganization) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/observabilityadmin-2018-05-10/UpdateTelemetryRuleForOrganization) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/observabilityadmin-2018-05-10/UpdateTelemetryRuleForOrganization) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/observabilityadmin-2018-05-10/UpdateTelemetryRuleForOrganization) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/observabilityadmin-2018-05-10/UpdateTelemetryRuleForOrganization) 