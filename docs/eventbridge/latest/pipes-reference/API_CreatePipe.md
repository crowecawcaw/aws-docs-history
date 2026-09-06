

# CreatePipe
<a name="API_CreatePipe"></a>

Create a pipe. Amazon EventBridge Pipes connect event sources to targets and reduces the need for specialized knowledge and integration code.

## Request Syntax
<a name="API_CreatePipe_RequestSyntax"></a>

```
POST /v1/pipes/{{Name}} HTTP/1.1
Content-type: application/json

{
   "Description": "{{string}}",
   "DesiredState": "{{string}}",
   "Enrichment": "{{string}}",
   "EnrichmentParameters": { 
      "HttpParameters": { 
         "HeaderParameters": { 
            "{{string}}" : "{{string}}" 
         },
         "PathParameterValues": [ "{{string}}" ],
         "QueryStringParameters": { 
            "{{string}}" : "{{string}}" 
         }
      },
      "InputTemplate": "{{string}}"
   },
   "KmsKeyIdentifier": "{{string}}",
   "LogConfiguration": { 
      "CloudwatchLogsLogDestination": { 
         "LogGroupArn": "{{string}}"
      },
      "FirehoseLogDestination": { 
         "DeliveryStreamArn": "{{string}}"
      },
      "IncludeExecutionData": [ "{{string}}" ],
      "Level": "{{string}}",
      "S3LogDestination": { 
         "BucketName": "{{string}}",
         "BucketOwner": "{{string}}",
         "OutputFormat": "{{string}}",
         "Prefix": "{{string}}"
      }
   },
   "RoleArn": "{{string}}",
   "Source": "{{string}}",
   "SourceParameters": { 
      "ActiveMQBrokerParameters": { 
         "BatchSize": {{number}},
         "Credentials": { ... },
         "MaximumBatchingWindowInSeconds": {{number}},
         "QueueName": "{{string}}"
      },
      "DynamoDBStreamParameters": { 
         "BatchSize": {{number}},
         "DeadLetterConfig": { 
            "Arn": "{{string}}"
         },
         "MaximumBatchingWindowInSeconds": {{number}},
         "MaximumRecordAgeInSeconds": {{number}},
         "MaximumRetryAttempts": {{number}},
         "OnPartialBatchItemFailure": "{{string}}",
         "ParallelizationFactor": {{number}},
         "StartingPosition": "{{string}}"
      },
      "FilterCriteria": { 
         "Filters": [ 
            { 
               "Pattern": "{{string}}"
            }
         ]
      },
      "KinesisStreamParameters": { 
         "BatchSize": {{number}},
         "DeadLetterConfig": { 
            "Arn": "{{string}}"
         },
         "MaximumBatchingWindowInSeconds": {{number}},
         "MaximumRecordAgeInSeconds": {{number}},
         "MaximumRetryAttempts": {{number}},
         "OnPartialBatchItemFailure": "{{string}}",
         "ParallelizationFactor": {{number}},
         "StartingPosition": "{{string}}",
         "StartingPositionTimestamp": {{number}}
      },
      "ManagedStreamingKafkaParameters": { 
         "BatchSize": {{number}},
         "ConsumerGroupID": "{{string}}",
         "Credentials": { ... },
         "MaximumBatchingWindowInSeconds": {{number}},
         "StartingPosition": "{{string}}",
         "TopicName": "{{string}}"
      },
      "RabbitMQBrokerParameters": { 
         "BatchSize": {{number}},
         "Credentials": { ... },
         "MaximumBatchingWindowInSeconds": {{number}},
         "QueueName": "{{string}}",
         "VirtualHost": "{{string}}"
      },
      "SelfManagedKafkaParameters": { 
         "AdditionalBootstrapServers": [ "{{string}}" ],
         "BatchSize": {{number}},
         "ConsumerGroupID": "{{string}}",
         "Credentials": { ... },
         "MaximumBatchingWindowInSeconds": {{number}},
         "ServerRootCaCertificate": "{{string}}",
         "StartingPosition": "{{string}}",
         "TopicName": "{{string}}",
         "Vpc": { 
            "SecurityGroup": [ "{{string}}" ],
            "Subnets": [ "{{string}}" ]
         }
      },
      "SqsQueueParameters": { 
         "BatchSize": {{number}},
         "MaximumBatchingWindowInSeconds": {{number}}
      }
   },
   "Tags": { 
      "{{string}}" : "{{string}}" 
   },
   "Target": "{{string}}",
   "TargetParameters": { 
      "BatchJobParameters": { 
         "ArrayProperties": { 
            "Size": {{number}}
         },
         "ContainerOverrides": { 
            "Command": [ "{{string}}" ],
            "Environment": [ 
               { 
                  "Name": "{{string}}",
                  "Value": "{{string}}"
               }
            ],
            "InstanceType": "{{string}}",
            "ResourceRequirements": [ 
               { 
                  "Type": "{{string}}",
                  "Value": "{{string}}"
               }
            ]
         },
         "DependsOn": [ 
            { 
               "JobId": "{{string}}",
               "Type": "{{string}}"
            }
         ],
         "JobDefinition": "{{string}}",
         "JobName": "{{string}}",
         "Parameters": { 
            "{{string}}" : "{{string}}" 
         },
         "RetryStrategy": { 
            "Attempts": {{number}}
         }
      },
      "CloudWatchLogsParameters": { 
         "LogStreamName": "{{string}}",
         "Timestamp": "{{string}}"
      },
      "EcsTaskParameters": { 
         "CapacityProviderStrategy": [ 
            { 
               "base": {{number}},
               "capacityProvider": "{{string}}",
               "weight": {{number}}
            }
         ],
         "EnableECSManagedTags": {{boolean}},
         "EnableExecuteCommand": {{boolean}},
         "Group": "{{string}}",
         "LaunchType": "{{string}}",
         "NetworkConfiguration": { 
            "awsvpcConfiguration": { 
               "AssignPublicIp": "{{string}}",
               "SecurityGroups": [ "{{string}}" ],
               "Subnets": [ "{{string}}" ]
            }
         },
         "Overrides": { 
            "ContainerOverrides": [ 
               { 
                  "Command": [ "{{string}}" ],
                  "Cpu": {{number}},
                  "Environment": [ 
                     { 
                        "name": "{{string}}",
                        "value": "{{string}}"
                     }
                  ],
                  "EnvironmentFiles": [ 
                     { 
                        "type": "{{string}}",
                        "value": "{{string}}"
                     }
                  ],
                  "Memory": {{number}},
                  "MemoryReservation": {{number}},
                  "Name": "{{string}}",
                  "ResourceRequirements": [ 
                     { 
                        "type": "{{string}}",
                        "value": "{{string}}"
                     }
                  ]
               }
            ],
            "Cpu": "{{string}}",
            "EphemeralStorage": { 
               "sizeInGiB": {{number}}
            },
            "ExecutionRoleArn": "{{string}}",
            "InferenceAcceleratorOverrides": [ 
               { 
                  "deviceName": "{{string}}",
                  "deviceType": "{{string}}"
               }
            ],
            "Memory": "{{string}}",
            "TaskRoleArn": "{{string}}"
         },
         "PlacementConstraints": [ 
            { 
               "expression": "{{string}}",
               "type": "{{string}}"
            }
         ],
         "PlacementStrategy": [ 
            { 
               "field": "{{string}}",
               "type": "{{string}}"
            }
         ],
         "PlatformVersion": "{{string}}",
         "PropagateTags": "{{string}}",
         "ReferenceId": "{{string}}",
         "Tags": [ 
            { 
               "Key": "{{string}}",
               "Value": "{{string}}"
            }
         ],
         "TaskCount": {{number}},
         "TaskDefinitionArn": "{{string}}"
      },
      "EventBridgeEventBusParameters": { 
         "DetailType": "{{string}}",
         "EndpointId": "{{string}}",
         "Resources": [ "{{string}}" ],
         "Source": "{{string}}",
         "Time": "{{string}}"
      },
      "HttpParameters": { 
         "HeaderParameters": { 
            "{{string}}" : "{{string}}" 
         },
         "PathParameterValues": [ "{{string}}" ],
         "QueryStringParameters": { 
            "{{string}}" : "{{string}}" 
         }
      },
      "InputTemplate": "{{string}}",
      "KinesisStreamParameters": { 
         "PartitionKey": "{{string}}"
      },
      "LambdaFunctionParameters": { 
         "InvocationType": "{{string}}"
      },
      "RedshiftDataParameters": { 
         "Database": "{{string}}",
         "DbUser": "{{string}}",
         "SecretManagerArn": "{{string}}",
         "Sqls": [ "{{string}}" ],
         "StatementName": "{{string}}",
         "WithEvent": {{boolean}}
      },
      "SageMakerPipelineParameters": { 
         "PipelineParameterList": [ 
            { 
               "Name": "{{string}}",
               "Value": "{{string}}"
            }
         ]
      },
      "SqsQueueParameters": { 
         "MessageDeduplicationId": "{{string}}",
         "MessageGroupId": "{{string}}"
      },
      "StepFunctionStateMachineParameters": { 
         "InvocationType": "{{string}}"
      },
      "TimestreamParameters": { 
         "DimensionMappings": [ 
            { 
               "DimensionName": "{{string}}",
               "DimensionValue": "{{string}}",
               "DimensionValueType": "{{string}}"
            }
         ],
         "EpochTimeUnit": "{{string}}",
         "MultiMeasureMappings": [ 
            { 
               "MultiMeasureAttributeMappings": [ 
                  { 
                     "MeasureValue": "{{string}}",
                     "MeasureValueType": "{{string}}",
                     "MultiMeasureAttributeName": "{{string}}"
                  }
               ],
               "MultiMeasureName": "{{string}}"
            }
         ],
         "SingleMeasureMappings": [ 
            { 
               "MeasureName": "{{string}}",
               "MeasureValue": "{{string}}",
               "MeasureValueType": "{{string}}"
            }
         ],
         "TimeFieldType": "{{string}}",
         "TimestampFormat": "{{string}}",
         "TimeValue": "{{string}}",
         "VersionValue": "{{string}}"
      }
   }
}
```

## URI Request Parameters
<a name="API_CreatePipe_RequestParameters"></a>

The request uses the following URI parameters.

 ** [Name](#API_CreatePipe_RequestSyntax) **   <a name="eventbridge-CreatePipe-request-uri-Name"></a>
The name of the pipe.  
Length Constraints: Minimum length of 1. Maximum length of 64.  
Pattern: `[\.\-_A-Za-z0-9]+`   
Required: Yes

## Request Body
<a name="API_CreatePipe_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [Description](#API_CreatePipe_RequestSyntax) **   <a name="eventbridge-CreatePipe-request-Description"></a>
A description of the pipe.  
Type: String  
Length Constraints: Minimum length of 0. Maximum length of 512.  
Pattern: `.*`   
Required: No

 ** [DesiredState](#API_CreatePipe_RequestSyntax) **   <a name="eventbridge-CreatePipe-request-DesiredState"></a>
The state the pipe should be in.  
Type: String  
Valid Values: `RUNNING | STOPPED`   
Required: No

 ** [Enrichment](#API_CreatePipe_RequestSyntax) **   <a name="eventbridge-CreatePipe-request-Enrichment"></a>
The ARN of the enrichment resource.  
Type: String  
Length Constraints: Minimum length of 0. Maximum length of 1600.  
Pattern: `$|arn:(aws[a-zA-Z0-9-]*):([a-zA-Z0-9\-]+):([a-z]{2,4}((-gov)|(-de)|(-iso([a-z]?)))?-[a-z]+(-\d{1})?)?:(\d{12})?:(.+)`   
Required: No

 ** [EnrichmentParameters](#API_CreatePipe_RequestSyntax) **   <a name="eventbridge-CreatePipe-request-EnrichmentParameters"></a>
The parameters required to set up enrichment on your pipe.  
Type: [PipeEnrichmentParameters](API_PipeEnrichmentParameters.md) object  
Required: No

 ** [KmsKeyIdentifier](#API_CreatePipe_RequestSyntax) **   <a name="eventbridge-CreatePipe-request-KmsKeyIdentifier"></a>
The identifier of the AWS KMS customer managed key for EventBridge to use, if you choose to use a customer managed key to encrypt pipe data. The identifier can be the key Amazon Resource Name (ARN), KeyId, key alias, or key alias ARN.  
If you do not specify a customer managed key identifier, EventBridge uses an AWS owned key to encrypt pipe data.  
For more information, see [Managing keys](https://docs.aws.amazon.com/kms/latest/developerguide/getting-started.html) in the * AWS Key Management Service Developer Guide*.   
Type: String  
Length Constraints: Minimum length of 0. Maximum length of 2048.  
Pattern: `[a-zA-Z0-9_\-/:]*`   
Required: No

 ** [LogConfiguration](#API_CreatePipe_RequestSyntax) **   <a name="eventbridge-CreatePipe-request-LogConfiguration"></a>
The logging configuration settings for the pipe.  
Type: [PipeLogConfigurationParameters](API_PipeLogConfigurationParameters.md) object  
Required: No

 ** [RoleArn](#API_CreatePipe_RequestSyntax) **   <a name="eventbridge-CreatePipe-request-RoleArn"></a>
The ARN of the role that allows the pipe to send data to the target.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 1600.  
Pattern: `arn:(aws[a-zA-Z-]*)?:iam::\d{12}:role/?[a-zA-Z0-9+=,.@\-_/]+`   
Required: Yes

 ** [Source](#API_CreatePipe_RequestSyntax) **   <a name="eventbridge-CreatePipe-request-Source"></a>
The ARN of the source resource.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 1600.  
Pattern: `smk://(([a-zA-Z0-9]|[a-zA-Z0-9][a-zA-Z0-9\-]*[a-zA-Z0-9])\.)*([A-Za-z0-9]|[A-Za-z0-9][A-Za-z0-9\-]*[A-Za-z0-9]):[0-9]{1,5}|arn:(aws[a-zA-Z0-9-]*):([a-zA-Z0-9\-]+):([a-z]{2,4}((-gov)|(-de)|(-iso([a-z]?)))?-[a-z]+(-\d{1})?)?:(\d{12})?:(.+)`   
Required: Yes

 ** [SourceParameters](#API_CreatePipe_RequestSyntax) **   <a name="eventbridge-CreatePipe-request-SourceParameters"></a>
The parameters required to set up a source for your pipe.  
Type: [PipeSourceParameters](API_PipeSourceParameters.md) object  
Required: No

 ** [Tags](#API_CreatePipe_RequestSyntax) **   <a name="eventbridge-CreatePipe-request-Tags"></a>
The list of key-value pairs to associate with the pipe.  
Type: String to string map  
Map Entries: Maximum number of 50 items.  
Key Length Constraints: Minimum length of 1. Maximum length of 128.  
Value Length Constraints: Minimum length of 0. Maximum length of 256.  
Required: No

 ** [Target](#API_CreatePipe_RequestSyntax) **   <a name="eventbridge-CreatePipe-request-Target"></a>
The ARN of the target resource.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 1600.  
Pattern: `arn:(aws[a-zA-Z0-9-]*):([a-zA-Z0-9\-]+):([a-z]{2,4}((-gov)|(-de)|(-iso([a-z]?)))?-[a-z]+(-\d{1})?)?:(\d{12})?:(.+)`   
Required: Yes

 ** [TargetParameters](#API_CreatePipe_RequestSyntax) **   <a name="eventbridge-CreatePipe-request-TargetParameters"></a>
The parameters required to set up a target for your pipe.  
For more information about pipe target parameters, including how to use dynamic path parameters, see [Target parameters](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-pipes-event-target.html) in the *Amazon EventBridge User Guide*.  
Type: [PipeTargetParameters](API_PipeTargetParameters.md) object  
Required: No

## Response Syntax
<a name="API_CreatePipe_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "Arn": "string",
   "CreationTime": number,
   "CurrentState": "string",
   "DesiredState": "string",
   "LastModifiedTime": number,
   "Name": "string"
}
```

## Response Elements
<a name="API_CreatePipe_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Arn](#API_CreatePipe_ResponseSyntax) **   <a name="eventbridge-CreatePipe-response-Arn"></a>
The ARN of the pipe.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 1600.  
Pattern: `arn:aws([a-z]|\-)*:([a-zA-Z0-9\-]+):([a-z]|\d|\-)*:([0-9]{12})?:(.+)` 

 ** [CreationTime](#API_CreatePipe_ResponseSyntax) **   <a name="eventbridge-CreatePipe-response-CreationTime"></a>
The time the pipe was created.  
Type: Timestamp

 ** [CurrentState](#API_CreatePipe_ResponseSyntax) **   <a name="eventbridge-CreatePipe-response-CurrentState"></a>
The state the pipe is in.  
Type: String  
Valid Values: `RUNNING | STOPPED | CREATING | UPDATING | DELETING | STARTING | STOPPING | CREATE_FAILED | UPDATE_FAILED | START_FAILED | STOP_FAILED | DELETE_FAILED | CREATE_ROLLBACK_FAILED | DELETE_ROLLBACK_FAILED | UPDATE_ROLLBACK_FAILED` 

 ** [DesiredState](#API_CreatePipe_ResponseSyntax) **   <a name="eventbridge-CreatePipe-response-DesiredState"></a>
The state the pipe should be in.  
Type: String  
Valid Values: `RUNNING | STOPPED` 

 ** [LastModifiedTime](#API_CreatePipe_ResponseSyntax) **   <a name="eventbridge-CreatePipe-response-LastModifiedTime"></a>
When the pipe was last updated, in [ISO-8601 format](https://www.w3.org/TR/NOTE-datetime) (YYYY-MM-DDThh:mm:ss.sTZD).  
Type: Timestamp

 ** [Name](#API_CreatePipe_ResponseSyntax) **   <a name="eventbridge-CreatePipe-response-Name"></a>
The name of the pipe.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 64.  
Pattern: `[\.\-_A-Za-z0-9]+` 

## Errors
<a name="API_CreatePipe_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ConflictException **   
An action you attempted resulted in an exception.    
 ** resourceId **   
The ID of the resource that caused the exception.  
 ** resourceType **   
The type of resource that caused the exception.
HTTP Status Code: 409

 ** InternalException **   
This exception occurs due to unexpected causes.    
 ** retryAfterSeconds **   
The number of seconds to wait before retrying the action that caused the exception.
HTTP Status Code: 500

 ** NotFoundException **   
An entity that you specified does not exist.  
HTTP Status Code: 404

 ** ServiceQuotaExceededException **   
A quota has been exceeded.    
 ** quotaCode **   
The identifier of the quota that caused the exception.  
 ** resourceId **   
The ID of the resource that caused the exception.  
 ** resourceType **   
The type of resource that caused the exception.  
 ** serviceCode **   
The identifier of the service that caused the exception.
HTTP Status Code: 402

 ** ThrottlingException **   
An action was throttled.    
 ** quotaCode **   
The identifier of the quota that caused the exception.  
 ** retryAfterSeconds **   
The number of seconds to wait before retrying the action that caused the exception.  
 ** serviceCode **   
The identifier of the service that caused the exception.
HTTP Status Code: 429

 ** ValidationException **   
Indicates that an error has occurred while performing a validate operation.    
 ** fieldList **   
The list of fields for which validation failed and the corresponding failure messages.
HTTP Status Code: 400

## See Also
<a name="API_CreatePipe_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/pipes-2015-10-07/CreatePipe) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/pipes-2015-10-07/CreatePipe) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/pipes-2015-10-07/CreatePipe) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/pipes-2015-10-07/CreatePipe) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/pipes-2015-10-07/CreatePipe) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/pipes-2015-10-07/CreatePipe) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/pipes-2015-10-07/CreatePipe) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/pipes-2015-10-07/CreatePipe) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/pipes-2015-10-07/CreatePipe) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/pipes-2015-10-07/CreatePipe) 