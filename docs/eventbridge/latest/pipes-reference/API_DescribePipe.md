

# DescribePipe
<a name="API_DescribePipe"></a>

Get the information about an existing pipe. For more information about pipes, see [Amazon EventBridge Pipes](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-pipes.html) in the Amazon EventBridge User Guide.

## Request Syntax
<a name="API_DescribePipe_RequestSyntax"></a>

```
GET /v1/pipes/{{Name}} HTTP/1.1
```

## URI Request Parameters
<a name="API_DescribePipe_RequestParameters"></a>

The request uses the following URI parameters.

 ** [Name](#API_DescribePipe_RequestSyntax) **   <a name="eventbridge-DescribePipe-request-uri-Name"></a>
The name of the pipe.  
Length Constraints: Minimum length of 1. Maximum length of 64.  
Pattern: `[\.\-_A-Za-z0-9]+`   
Required: Yes

## Request Body
<a name="API_DescribePipe_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_DescribePipe_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "Arn": "string",
   "CreationTime": number,
   "CurrentState": "string",
   "Description": "string",
   "DesiredState": "string",
   "Enrichment": "string",
   "EnrichmentParameters": { 
      "HttpParameters": { 
         "HeaderParameters": { 
            "string" : "string" 
         },
         "PathParameterValues": [ "string" ],
         "QueryStringParameters": { 
            "string" : "string" 
         }
      },
      "InputTemplate": "string"
   },
   "KmsKeyIdentifier": "string",
   "LastModifiedTime": number,
   "LogConfiguration": { 
      "CloudwatchLogsLogDestination": { 
         "LogGroupArn": "string"
      },
      "FirehoseLogDestination": { 
         "DeliveryStreamArn": "string"
      },
      "IncludeExecutionData": [ "string" ],
      "Level": "string",
      "S3LogDestination": { 
         "BucketName": "string",
         "BucketOwner": "string",
         "OutputFormat": "string",
         "Prefix": "string"
      }
   },
   "Name": "string",
   "RoleArn": "string",
   "Source": "string",
   "SourceParameters": { 
      "ActiveMQBrokerParameters": { 
         "BatchSize": number,
         "Credentials": { ... },
         "MaximumBatchingWindowInSeconds": number,
         "QueueName": "string"
      },
      "DynamoDBStreamParameters": { 
         "BatchSize": number,
         "DeadLetterConfig": { 
            "Arn": "string"
         },
         "MaximumBatchingWindowInSeconds": number,
         "MaximumRecordAgeInSeconds": number,
         "MaximumRetryAttempts": number,
         "OnPartialBatchItemFailure": "string",
         "ParallelizationFactor": number,
         "StartingPosition": "string"
      },
      "FilterCriteria": { 
         "Filters": [ 
            { 
               "Pattern": "string"
            }
         ]
      },
      "KinesisStreamParameters": { 
         "BatchSize": number,
         "DeadLetterConfig": { 
            "Arn": "string"
         },
         "MaximumBatchingWindowInSeconds": number,
         "MaximumRecordAgeInSeconds": number,
         "MaximumRetryAttempts": number,
         "OnPartialBatchItemFailure": "string",
         "ParallelizationFactor": number,
         "StartingPosition": "string",
         "StartingPositionTimestamp": number
      },
      "ManagedStreamingKafkaParameters": { 
         "BatchSize": number,
         "ConsumerGroupID": "string",
         "Credentials": { ... },
         "MaximumBatchingWindowInSeconds": number,
         "StartingPosition": "string",
         "TopicName": "string"
      },
      "RabbitMQBrokerParameters": { 
         "BatchSize": number,
         "Credentials": { ... },
         "MaximumBatchingWindowInSeconds": number,
         "QueueName": "string",
         "VirtualHost": "string"
      },
      "SelfManagedKafkaParameters": { 
         "AdditionalBootstrapServers": [ "string" ],
         "BatchSize": number,
         "ConsumerGroupID": "string",
         "Credentials": { ... },
         "MaximumBatchingWindowInSeconds": number,
         "ServerRootCaCertificate": "string",
         "StartingPosition": "string",
         "TopicName": "string",
         "Vpc": { 
            "SecurityGroup": [ "string" ],
            "Subnets": [ "string" ]
         }
      },
      "SqsQueueParameters": { 
         "BatchSize": number,
         "MaximumBatchingWindowInSeconds": number
      }
   },
   "StateReason": "string",
   "Tags": { 
      "string" : "string" 
   },
   "Target": "string",
   "TargetParameters": { 
      "BatchJobParameters": { 
         "ArrayProperties": { 
            "Size": number
         },
         "ContainerOverrides": { 
            "Command": [ "string" ],
            "Environment": [ 
               { 
                  "Name": "string",
                  "Value": "string"
               }
            ],
            "InstanceType": "string",
            "ResourceRequirements": [ 
               { 
                  "Type": "string",
                  "Value": "string"
               }
            ]
         },
         "DependsOn": [ 
            { 
               "JobId": "string",
               "Type": "string"
            }
         ],
         "JobDefinition": "string",
         "JobName": "string",
         "Parameters": { 
            "string" : "string" 
         },
         "RetryStrategy": { 
            "Attempts": number
         }
      },
      "CloudWatchLogsParameters": { 
         "LogStreamName": "string",
         "Timestamp": "string"
      },
      "EcsTaskParameters": { 
         "CapacityProviderStrategy": [ 
            { 
               "base": number,
               "capacityProvider": "string",
               "weight": number
            }
         ],
         "EnableECSManagedTags": boolean,
         "EnableExecuteCommand": boolean,
         "Group": "string",
         "LaunchType": "string",
         "NetworkConfiguration": { 
            "awsvpcConfiguration": { 
               "AssignPublicIp": "string",
               "SecurityGroups": [ "string" ],
               "Subnets": [ "string" ]
            }
         },
         "Overrides": { 
            "ContainerOverrides": [ 
               { 
                  "Command": [ "string" ],
                  "Cpu": number,
                  "Environment": [ 
                     { 
                        "name": "string",
                        "value": "string"
                     }
                  ],
                  "EnvironmentFiles": [ 
                     { 
                        "type": "string",
                        "value": "string"
                     }
                  ],
                  "Memory": number,
                  "MemoryReservation": number,
                  "Name": "string",
                  "ResourceRequirements": [ 
                     { 
                        "type": "string",
                        "value": "string"
                     }
                  ]
               }
            ],
            "Cpu": "string",
            "EphemeralStorage": { 
               "sizeInGiB": number
            },
            "ExecutionRoleArn": "string",
            "InferenceAcceleratorOverrides": [ 
               { 
                  "deviceName": "string",
                  "deviceType": "string"
               }
            ],
            "Memory": "string",
            "TaskRoleArn": "string"
         },
         "PlacementConstraints": [ 
            { 
               "expression": "string",
               "type": "string"
            }
         ],
         "PlacementStrategy": [ 
            { 
               "field": "string",
               "type": "string"
            }
         ],
         "PlatformVersion": "string",
         "PropagateTags": "string",
         "ReferenceId": "string",
         "Tags": [ 
            { 
               "Key": "string",
               "Value": "string"
            }
         ],
         "TaskCount": number,
         "TaskDefinitionArn": "string"
      },
      "EventBridgeEventBusParameters": { 
         "DetailType": "string",
         "EndpointId": "string",
         "Resources": [ "string" ],
         "Source": "string",
         "Time": "string"
      },
      "HttpParameters": { 
         "HeaderParameters": { 
            "string" : "string" 
         },
         "PathParameterValues": [ "string" ],
         "QueryStringParameters": { 
            "string" : "string" 
         }
      },
      "InputTemplate": "string",
      "KinesisStreamParameters": { 
         "PartitionKey": "string"
      },
      "LambdaFunctionParameters": { 
         "InvocationType": "string"
      },
      "RedshiftDataParameters": { 
         "Database": "string",
         "DbUser": "string",
         "SecretManagerArn": "string",
         "Sqls": [ "string" ],
         "StatementName": "string",
         "WithEvent": boolean
      },
      "SageMakerPipelineParameters": { 
         "PipelineParameterList": [ 
            { 
               "Name": "string",
               "Value": "string"
            }
         ]
      },
      "SqsQueueParameters": { 
         "MessageDeduplicationId": "string",
         "MessageGroupId": "string"
      },
      "StepFunctionStateMachineParameters": { 
         "InvocationType": "string"
      },
      "TimestreamParameters": { 
         "DimensionMappings": [ 
            { 
               "DimensionName": "string",
               "DimensionValue": "string",
               "DimensionValueType": "string"
            }
         ],
         "EpochTimeUnit": "string",
         "MultiMeasureMappings": [ 
            { 
               "MultiMeasureAttributeMappings": [ 
                  { 
                     "MeasureValue": "string",
                     "MeasureValueType": "string",
                     "MultiMeasureAttributeName": "string"
                  }
               ],
               "MultiMeasureName": "string"
            }
         ],
         "SingleMeasureMappings": [ 
            { 
               "MeasureName": "string",
               "MeasureValue": "string",
               "MeasureValueType": "string"
            }
         ],
         "TimeFieldType": "string",
         "TimestampFormat": "string",
         "TimeValue": "string",
         "VersionValue": "string"
      }
   }
}
```

## Response Elements
<a name="API_DescribePipe_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Arn](#API_DescribePipe_ResponseSyntax) **   <a name="eventbridge-DescribePipe-response-Arn"></a>
The ARN of the pipe.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 1600.  
Pattern: `arn:aws([a-z]|\-)*:([a-zA-Z0-9\-]+):([a-z]|\d|\-)*:([0-9]{12})?:(.+)` 

 ** [CreationTime](#API_DescribePipe_ResponseSyntax) **   <a name="eventbridge-DescribePipe-response-CreationTime"></a>
The time the pipe was created.  
Type: Timestamp

 ** [CurrentState](#API_DescribePipe_ResponseSyntax) **   <a name="eventbridge-DescribePipe-response-CurrentState"></a>
The state the pipe is in.  
Type: String  
Valid Values: `RUNNING | STOPPED | CREATING | UPDATING | DELETING | STARTING | STOPPING | CREATE_FAILED | UPDATE_FAILED | START_FAILED | STOP_FAILED | DELETE_FAILED | CREATE_ROLLBACK_FAILED | DELETE_ROLLBACK_FAILED | UPDATE_ROLLBACK_FAILED` 

 ** [Description](#API_DescribePipe_ResponseSyntax) **   <a name="eventbridge-DescribePipe-response-Description"></a>
A description of the pipe.  
Type: String  
Length Constraints: Minimum length of 0. Maximum length of 512.  
Pattern: `.*` 

 ** [DesiredState](#API_DescribePipe_ResponseSyntax) **   <a name="eventbridge-DescribePipe-response-DesiredState"></a>
The state the pipe should be in.  
Type: String  
Valid Values: `RUNNING | STOPPED | DELETED` 

 ** [Enrichment](#API_DescribePipe_ResponseSyntax) **   <a name="eventbridge-DescribePipe-response-Enrichment"></a>
The ARN of the enrichment resource.  
Type: String  
Length Constraints: Minimum length of 0. Maximum length of 1600.  
Pattern: `$|arn:(aws[a-zA-Z0-9-]*):([a-zA-Z0-9\-]+):([a-z]{2,4}((-gov)|(-de)|(-iso([a-z]?)))?-[a-z]+(-\d{1})?)?:(\d{12})?:(.+)` 

 ** [EnrichmentParameters](#API_DescribePipe_ResponseSyntax) **   <a name="eventbridge-DescribePipe-response-EnrichmentParameters"></a>
The parameters required to set up enrichment on your pipe.  
Type: [PipeEnrichmentParameters](API_PipeEnrichmentParameters.md) object

 ** [KmsKeyIdentifier](#API_DescribePipe_ResponseSyntax) **   <a name="eventbridge-DescribePipe-response-KmsKeyIdentifier"></a>
The identifier of the AWS KMS customer managed key for EventBridge to use to encrypt pipe data, if one has been specified.  
For more information, see [Data encryption in EventBridge](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-encryption.html) in the *Amazon EventBridge User Guide*.  
Type: String  
Length Constraints: Minimum length of 0. Maximum length of 2048.  
Pattern: `[a-zA-Z0-9_\-/:]*` 

 ** [LastModifiedTime](#API_DescribePipe_ResponseSyntax) **   <a name="eventbridge-DescribePipe-response-LastModifiedTime"></a>
When the pipe was last updated, in [ISO-8601 format](https://www.w3.org/TR/NOTE-datetime) (YYYY-MM-DDThh:mm:ss.sTZD).  
Type: Timestamp

 ** [LogConfiguration](#API_DescribePipe_ResponseSyntax) **   <a name="eventbridge-DescribePipe-response-LogConfiguration"></a>
The logging configuration settings for the pipe.  
Type: [PipeLogConfiguration](API_PipeLogConfiguration.md) object

 ** [Name](#API_DescribePipe_ResponseSyntax) **   <a name="eventbridge-DescribePipe-response-Name"></a>
The name of the pipe.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 64.  
Pattern: `[\.\-_A-Za-z0-9]+` 

 ** [RoleArn](#API_DescribePipe_ResponseSyntax) **   <a name="eventbridge-DescribePipe-response-RoleArn"></a>
The ARN of the role that allows the pipe to send data to the target.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 1600.  
Pattern: `arn:(aws[a-zA-Z-]*)?:iam::\d{12}:role/?[a-zA-Z0-9+=,.@\-_/]+` 

 ** [Source](#API_DescribePipe_ResponseSyntax) **   <a name="eventbridge-DescribePipe-response-Source"></a>
The ARN of the source resource.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 1600.  
Pattern: `smk://(([a-zA-Z0-9]|[a-zA-Z0-9][a-zA-Z0-9\-]*[a-zA-Z0-9])\.)*([A-Za-z0-9]|[A-Za-z0-9][A-Za-z0-9\-]*[A-Za-z0-9]):[0-9]{1,5}|arn:(aws[a-zA-Z0-9-]*):([a-zA-Z0-9\-]+):([a-z]{2,4}((-gov)|(-de)|(-iso([a-z]?)))?-[a-z]+(-\d{1})?)?:(\d{12})?:(.+)` 

 ** [SourceParameters](#API_DescribePipe_ResponseSyntax) **   <a name="eventbridge-DescribePipe-response-SourceParameters"></a>
The parameters required to set up a source for your pipe.  
Type: [PipeSourceParameters](API_PipeSourceParameters.md) object

 ** [StateReason](#API_DescribePipe_ResponseSyntax) **   <a name="eventbridge-DescribePipe-response-StateReason"></a>
The reason the pipe is in its current state.  
Type: String  
Length Constraints: Minimum length of 0. Maximum length of 512.  
Pattern: `.*` 

 ** [Tags](#API_DescribePipe_ResponseSyntax) **   <a name="eventbridge-DescribePipe-response-Tags"></a>
The list of key-value pairs to associate with the pipe.  
Type: String to string map  
Map Entries: Maximum number of 50 items.  
Key Length Constraints: Minimum length of 1. Maximum length of 128.  
Value Length Constraints: Minimum length of 0. Maximum length of 256.

 ** [Target](#API_DescribePipe_ResponseSyntax) **   <a name="eventbridge-DescribePipe-response-Target"></a>
The ARN of the target resource.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 1600.  
Pattern: `arn:(aws[a-zA-Z0-9-]*):([a-zA-Z0-9\-]+):([a-z]{2,4}((-gov)|(-de)|(-iso([a-z]?)))?-[a-z]+(-\d{1})?)?:(\d{12})?:(.+)` 

 ** [TargetParameters](#API_DescribePipe_ResponseSyntax) **   <a name="eventbridge-DescribePipe-response-TargetParameters"></a>
The parameters required to set up a target for your pipe.  
For more information about pipe target parameters, including how to use dynamic path parameters, see [Target parameters](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-pipes-event-target.html) in the *Amazon EventBridge User Guide*.  
Type: [PipeTargetParameters](API_PipeTargetParameters.md) object

## Errors
<a name="API_DescribePipe_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalException **   
This exception occurs due to unexpected causes.    
 ** retryAfterSeconds **   
The number of seconds to wait before retrying the action that caused the exception.
HTTP Status Code: 500

 ** NotFoundException **   
An entity that you specified does not exist.  
HTTP Status Code: 404

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
<a name="API_DescribePipe_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/pipes-2015-10-07/DescribePipe) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/pipes-2015-10-07/DescribePipe) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/pipes-2015-10-07/DescribePipe) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/pipes-2015-10-07/DescribePipe) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/pipes-2015-10-07/DescribePipe) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/pipes-2015-10-07/DescribePipe) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/pipes-2015-10-07/DescribePipe) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/pipes-2015-10-07/DescribePipe) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/pipes-2015-10-07/DescribePipe) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/pipes-2015-10-07/DescribePipe) 