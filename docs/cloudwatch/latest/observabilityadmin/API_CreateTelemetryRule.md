

# CreateTelemetryRule
<a name="API_CreateTelemetryRule"></a>

 Creates a telemetry rule that defines how telemetry should be configured for AWS resources in your account. The rule specifies which resources should have telemetry enabled and how that telemetry data should be collected based on resource type, telemetry type, and selection criteria. 

## Request Syntax
<a name="API_CreateTelemetryRule_RequestSyntax"></a>

```
POST /CreateTelemetryRule HTTP/1.1
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
   "RuleName": "{{string}}",
   "Tags": { 
      "{{string}}" : "{{string}}" 
   }
}
```

## URI Request Parameters
<a name="API_CreateTelemetryRule_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_CreateTelemetryRule_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [Rule](#API_CreateTelemetryRule_RequestSyntax) **   <a name="cwoa-CreateTelemetryRule-request-Rule"></a>
 The configuration details for the telemetry rule, including the resource type, telemetry type, destination configuration, and selection criteria for which resources the rule applies to.   
Type: [TelemetryRule](API_TelemetryRule.md) object  
Required: Yes

 ** [RuleName](#API_CreateTelemetryRule_RequestSyntax) **   <a name="cwoa-CreateTelemetryRule-request-RuleName"></a>
 A unique name for the telemetry rule being created.   
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 100.  
Pattern: `[0-9A-Za-z-_.#/]+`   
Required: Yes

 ** [Tags](#API_CreateTelemetryRule_RequestSyntax) **   <a name="cwoa-CreateTelemetryRule-request-Tags"></a>
 The key-value pairs to associate with the telemetry rule resource for categorization and management purposes.   
Type: String to string map  
Map Entries: Maximum number of 50 items.  
Key Length Constraints: Minimum length of 1. Maximum length of 128.  
Key Pattern: `([\p{L}\p{Z}\p{N}_.:/=+\-@]*)`   
Value Length Constraints: Minimum length of 0. Maximum length of 256.  
Value Pattern: `([\p{L}\p{Z}\p{N}_.:/=+\-@]*)`   
Required: No

## Response Syntax
<a name="API_CreateTelemetryRule_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "RuleArn": "string"
}
```

## Response Elements
<a name="API_CreateTelemetryRule_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [RuleArn](#API_CreateTelemetryRule_ResponseSyntax) **   <a name="cwoa-CreateTelemetryRule-response-RuleArn"></a>
 The Amazon Resource Name (ARN) of the created telemetry rule.   
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 1011.  
Pattern: `arn:aws([a-z0-9\-]+)?:([a-zA-Z0-9\-]+):([a-z0-9\-]+)?:([0-9]{12})?:(.+)` 

## Errors
<a name="API_CreateTelemetryRule_Errors"></a>

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
<a name="API_CreateTelemetryRule_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/observabilityadmin-2018-05-10/CreateTelemetryRule) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/observabilityadmin-2018-05-10/CreateTelemetryRule) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/observabilityadmin-2018-05-10/CreateTelemetryRule) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/observabilityadmin-2018-05-10/CreateTelemetryRule) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/observabilityadmin-2018-05-10/CreateTelemetryRule) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/observabilityadmin-2018-05-10/CreateTelemetryRule) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/observabilityadmin-2018-05-10/CreateTelemetryRule) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/observabilityadmin-2018-05-10/CreateTelemetryRule) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/observabilityadmin-2018-05-10/CreateTelemetryRule) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/observabilityadmin-2018-05-10/CreateTelemetryRule) 