# UpdatePipe

Update an existing pipe. When you call `UpdatePipe`, EventBridge only the
updates fields you have specified in the request; the rest remain unchanged. The exception
to this is if you modify any AWS-service specific fields in the
`SourceParameters`, `EnrichmentParameters`, or
`TargetParameters` objects. For example,
`DynamoDBStreamParameters` or `EventBridgeEventBusParameters`.
EventBridge updates the fields in these objects atomically as one and overrides existing
values. This is by design, and means that if you don't specify an optional field in one of
these `Parameters` objects, EventBridge sets that field to its system-default
value during the update.

For more information about pipes, see [Amazon EventBridge Pipes](../userguide/eb-pipes.md "../userguide/eb-pipes.md") in the Amazon EventBridge User Guide.

## Request Syntax

```
PUT /v1/pipes/`Name` HTTP/1.1
Content-type: application/json

{
   "Description": "`string`",
   "DesiredState": "`string`",
   "Enrichment": "`string`",
   "EnrichmentParameters": {
      "HttpParameters": {
         "HeaderParameters": {
            "`string`" : "`string`"
         },
         "PathParameterValues": [ "`string`" ],
         "QueryStringParameters": {
            "`string`" : "`string`"
         }
      },
      "InputTemplate": "`string`"
   },
   "KmsKeyIdentifier": "`string`",
   "LogConfiguration": {
      "CloudwatchLogsLogDestination": {
         "LogGroupArn": "`string`"
      },
      "FirehoseLogDestination": {
         "DeliveryStreamArn": "`string`"
      },
      "IncludeExecutionData": [ "`string`" ],
      "Level": "`string`",
      "S3LogDestination": {
         "BucketName": "`string`",
         "BucketOwner": "`string`",
         "OutputFormat": "`string`",
         "Prefix": "`string`"
      }
   },
   "RoleArn": "`string`",
   "SourceParameters": {
      "ActiveMQBrokerParameters": {
         "BatchSize": `number`,
         "Credentials": { ... },
         "MaximumBatchingWindowInSeconds": `number`
      },
      "DynamoDBStreamParameters": {
         "BatchSize": `number`,
         "DeadLetterConfig": {
            "Arn": "`string`"
         },
         "MaximumBatchingWindowInSeconds": `number`,
         "MaximumRecordAgeInSeconds": `number`,
         "MaximumRetryAttempts": `number`,
         "OnPartialBatchItemFailure": "`string`",
         "ParallelizationFactor": `number`
      },
      "FilterCriteria": {
         "Filters": [
            {
               "Pattern": "`string`"
            }
         ]
      },
      "KinesisStreamParameters": {
         "BatchSize": `number`,
         "DeadLetterConfig": {
            "Arn": "`string`"
         },
         "MaximumBatchingWindowInSeconds": `number`,
         "MaximumRecordAgeInSeconds": `number`,
         "MaximumRetryAttempts": `number`,
         "OnPartialBatchItemFailure": "`string`",
         "ParallelizationFactor": `number`
      },
      "ManagedStreamingKafkaParameters": {
         "BatchSize": `number`,
         "Credentials": { ... },
         "MaximumBatchingWindowInSeconds": `number`
      },
      "RabbitMQBrokerParameters": {
         "BatchSize": `number`,
         "Credentials": { ... },
         "MaximumBatchingWindowInSeconds": `number`
      },
      "SelfManagedKafkaParameters": {
         "BatchSize": `number`,
         "Credentials": { ... },
         "MaximumBatchingWindowInSeconds": `number`,
         "ServerRootCaCertificate": "`string`",
         "Vpc": {
            "SecurityGroup": [ "`string`" ],
            "Subnets": [ "`string`" ]
         }
      },
      "SqsQueueParameters": {
         "BatchSize": `number`,
         "MaximumBatchingWindowInSeconds": `number`
      }
   },
   "Target": "`string`",
   "TargetParameters": {
      "BatchJobParameters": {
         "ArrayProperties": {
            "Size": `number`
         },
         "ContainerOverrides": {
            "Command": [ "`string`" ],
            "Environment": [
               {
                  "Name": "`string`",
                  "Value": "`string`"
               }
            ],
            "InstanceType": "`string`",
            "ResourceRequirements": [
               {
                  "Type": "`string`",
                  "Value": "`string`"
               }
            ]
         },
         "DependsOn": [
            {
               "JobId": "`string`",
               "Type": "`string`"
            }
         ],
         "JobDefinition": "`string`",
         "JobName": "`string`",
         "Parameters": {
            "`string`" : "`string`"
         },
         "RetryStrategy": {
            "Attempts": `number`
         }
      },
      "CloudWatchLogsParameters": {
         "LogStreamName": "`string`",
         "Timestamp": "`string`"
      },
      "EcsTaskParameters": {
         "CapacityProviderStrategy": [
            {
               "base": `number`,
               "capacityProvider": "`string`",
               "weight": `number`
            }
         ],
         "EnableECSManagedTags": `boolean`,
         "EnableExecuteCommand": `boolean`,
         "Group": "`string`",
         "LaunchType": "`string`",
         "NetworkConfiguration": {
            "awsvpcConfiguration": {
               "AssignPublicIp": "`string`",
               "SecurityGroups": [ "`string`" ],
               "Subnets": [ "`string`" ]
            }
         },
         "Overrides": {
            "ContainerOverrides": [
               {
                  "Command": [ "`string`" ],
                  "Cpu": `number`,
                  "Environment": [
                     {
                        "name": "`string`",
                        "value": "`string`"
                     }
                  ],
                  "EnvironmentFiles": [
                     {
                        "type": "`string`",
                        "value": "`string`"
                     }
                  ],
                  "Memory": `number`,
                  "MemoryReservation": `number`,
                  "Name": "`string`",
                  "ResourceRequirements": [
                     {
                        "type": "`string`",
                        "value": "`string`"
                     }
                  ]
               }
            ],
            "Cpu": "`string`",
            "EphemeralStorage": {
               "sizeInGiB": `number`
            },
            "ExecutionRoleArn": "`string`",
            "InferenceAcceleratorOverrides": [
               {
                  "deviceName": "`string`",
                  "deviceType": "`string`"
               }
            ],
            "Memory": "`string`",
            "TaskRoleArn": "`string`"
         },
         "PlacementConstraints": [
            {
               "expression": "`string`",
               "type": "`string`"
            }
         ],
         "PlacementStrategy": [
            {
               "field": "`string`",
               "type": "`string`"
            }
         ],
         "PlatformVersion": "`string`",
         "PropagateTags": "`string`",
         "ReferenceId": "`string`",
         "Tags": [
            {
               "Key": "`string`",
               "Value": "`string`"
            }
         ],
         "TaskCount": `number`,
         "TaskDefinitionArn": "`string`"
      },
      "EventBridgeEventBusParameters": {
         "DetailType": "`string`",
         "EndpointId": "`string`",
         "Resources": [ "`string`" ],
         "Source": "`string`",
         "Time": "`string`"
      },
      "HttpParameters": {
         "HeaderParameters": {
            "`string`" : "`string`"
         },
         "PathParameterValues": [ "`string`" ],
         "QueryStringParameters": {
            "`string`" : "`string`"
         }
      },
      "InputTemplate": "`string`",
      "KinesisStreamParameters": {
         "PartitionKey": "`string`"
      },
      "LambdaFunctionParameters": {
         "InvocationType": "`string`"
      },
      "RedshiftDataParameters": {
         "Database": "`string`",
         "DbUser": "`string`",
         "SecretManagerArn": "`string`",
         "Sqls": [ "`string`" ],
         "StatementName": "`string`",
         "WithEvent": `boolean`
      },
      "SageMakerPipelineParameters": {
         "PipelineParameterList": [
            {
               "Name": "`string`",
               "Value": "`string`"
            }
         ]
      },
      "SqsQueueParameters": {
         "MessageDeduplicationId": "`string`",
         "MessageGroupId": "`string`"
      },
      "StepFunctionStateMachineParameters": {
         "InvocationType": "`string`"
      },
      "TimestreamParameters": {
         "DimensionMappings": [
            {
               "DimensionName": "`string`",
               "DimensionValue": "`string`",
               "DimensionValueType": "`string`"
            }
         ],
         "EpochTimeUnit": "`string`",
         "MultiMeasureMappings": [
            {
               "MultiMeasureAttributeMappings": [
                  {
                     "MeasureValue": "`string`",
                     "MeasureValueType": "`string`",
                     "MultiMeasureAttributeName": "`string`"
                  }
               ],
               "MultiMeasureName": "`string`"
            }
         ],
         "SingleMeasureMappings": [
            {
               "MeasureName": "`string`",
               "MeasureValue": "`string`",
               "MeasureValueType": "`string`"
            }
         ],
         "TimeFieldType": "`string`",
         "TimestampFormat": "`string`",
         "TimeValue": "`string`",
         "VersionValue": "`string`"
      }
   }
}
```

## URI Request Parameters

The request uses the following URI parameters.

**[Name](#API_UpdatePipe_RequestSyntax "#API_UpdatePipe_RequestSyntax")**

The name of the pipe.

Length Constraints: Minimum length of 1. Maximum length of 64.

Pattern: `[\.\-_A-Za-z0-9]+`

Required: Yes

## Request Body

The request accepts the following data in JSON format.

**[Description](#API_UpdatePipe_RequestSyntax "#API_UpdatePipe_RequestSyntax")**

A description of the pipe.

Type: String

Length Constraints: Minimum length of 0. Maximum length of 512.

Pattern: `.*`

Required: No

**[DesiredState](#API_UpdatePipe_RequestSyntax "#API_UpdatePipe_RequestSyntax")**

The state the pipe should be in.

Type: String

Valid Values: `RUNNING | STOPPED`

Required: No

**[Enrichment](#API_UpdatePipe_RequestSyntax "#API_UpdatePipe_RequestSyntax")**

The ARN of the enrichment resource.

Type: String

Length Constraints: Minimum length of 0. Maximum length of 1600.

Pattern: `$|arn:(aws[a-zA-Z0-9-]*):([a-zA-Z0-9\-]+):([a-z]{2,4}((-gov)|(-de)|(-iso([a-z]?)))?-[a-z]+(-\d{1})?)?:(\d{12})?:(.+)`

Required: No

**[EnrichmentParameters](#API_UpdatePipe_RequestSyntax "#API_UpdatePipe_RequestSyntax")**

The parameters required to set up enrichment on your pipe.

Type: [PipeEnrichmentParameters](API_PipeEnrichmentParameters.md "API_PipeEnrichmentParameters.md") object

Required: No

**[KmsKeyIdentifier](#API_UpdatePipe_RequestSyntax "#API_UpdatePipe_RequestSyntax")**

The identifier of the AWS KMS
customer managed key for EventBridge to use, if you choose to use a customer managed key to encrypt pipe data. The identifier can be the key
Amazon Resource Name (ARN), KeyId, key alias, or key alias ARN.

To update a pipe that is using the default AWS owned key to use a customer managed key instead, or update a pipe that is using a customer managed key to use a
different customer managed key, specify a customer managed key identifier.

To update a pipe that is using a customer managed key to use the default AWS owned key, specify an empty string.

For more information, see [Managing keys](../../../kms/latest/developerguide/getting-started.md "../../../kms/latest/developerguide/getting-started.md") in the _AWS Key Management Service
Developer Guide_.

Type: String

Length Constraints: Minimum length of 0. Maximum length of 2048.

Pattern: `[a-zA-Z0-9_\-/:]*`

Required: No

**[LogConfiguration](#API_UpdatePipe_RequestSyntax "#API_UpdatePipe_RequestSyntax")**

The logging configuration settings for the pipe.

Type: [PipeLogConfigurationParameters](API_PipeLogConfigurationParameters.md "API_PipeLogConfigurationParameters.md") object

Required: No

**[RoleArn](#API_UpdatePipe_RequestSyntax "#API_UpdatePipe_RequestSyntax")**

The ARN of the role that allows the pipe to send data to the target.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 1600.

Pattern: `arn:(aws[a-zA-Z-]*)?:iam::\d{12}:role/?[a-zA-Z0-9+=,.@\-_/]+`

Required: Yes

**[SourceParameters](#API_UpdatePipe_RequestSyntax "#API_UpdatePipe_RequestSyntax")**

The parameters required to set up a source for your pipe.

Type: [UpdatePipeSourceParameters](API_UpdatePipeSourceParameters.md "API_UpdatePipeSourceParameters.md") object

Required: No

**[Target](#API_UpdatePipe_RequestSyntax "#API_UpdatePipe_RequestSyntax")**

The ARN of the target resource.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 1600.

Pattern: `arn:(aws[a-zA-Z0-9-]*):([a-zA-Z0-9\-]+):([a-z]{2,4}((-gov)|(-de)|(-iso([a-z]?)))?-[a-z]+(-\d{1})?)?:(\d{12})?:(.+)`

Required: No

**[TargetParameters](#API_UpdatePipe_RequestSyntax "#API_UpdatePipe_RequestSyntax")**

The parameters required to set up a target for your pipe.

For more information about pipe target parameters, including how to use dynamic path parameters, see [Target parameters](../userguide/eb-pipes-event-target.md "../userguide/eb-pipes-event-target.md") in the _Amazon EventBridge User Guide_.

Type: [PipeTargetParameters](API_PipeTargetParameters.md "API_PipeTargetParameters.md") object

Required: No

## Response Syntax

```
HTTP/1.1 200
Content-type: application/json

{
   "Arn": "***string***",
   "CreationTime": ***number***,
   "CurrentState": "***string***",
   "DesiredState": "***string***",
   "LastModifiedTime": ***number***,
   "Name": "***string***"
}
```

## Response Elements

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

**[Arn](#API_UpdatePipe_ResponseSyntax "#API_UpdatePipe_ResponseSyntax")**

The ARN of the pipe.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 1600.

Pattern: `arn:aws([a-z]|\-)*:([a-zA-Z0-9\-]+):([a-z]|\d|\-)*:([0-9]{12})?:(.+)`

**[CreationTime](#API_UpdatePipe_ResponseSyntax "#API_UpdatePipe_ResponseSyntax")**

The time the pipe was created.

Type: Timestamp

**[CurrentState](#API_UpdatePipe_ResponseSyntax "#API_UpdatePipe_ResponseSyntax")**

The state the pipe is in.

Type: String

Valid Values: `RUNNING | STOPPED | CREATING | UPDATING | DELETING | STARTING | STOPPING | CREATE_FAILED | UPDATE_FAILED | START_FAILED | STOP_FAILED | DELETE_FAILED | CREATE_ROLLBACK_FAILED | DELETE_ROLLBACK_FAILED | UPDATE_ROLLBACK_FAILED`

**[DesiredState](#API_UpdatePipe_ResponseSyntax "#API_UpdatePipe_ResponseSyntax")**

The state the pipe should be in.

Type: String

Valid Values: `RUNNING | STOPPED`

**[LastModifiedTime](#API_UpdatePipe_ResponseSyntax "#API_UpdatePipe_ResponseSyntax")**

When the pipe was last updated, in [ISO-8601 format](https://www.w3.org/TR/NOTE-datetime "https://www.w3.org/TR/NOTE-datetime") (YYYY-MM-DDThh:mm:ss.sTZD).

Type: Timestamp

**[Name](#API_UpdatePipe_ResponseSyntax "#API_UpdatePipe_ResponseSyntax")**

The name of the pipe.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 64.

Pattern: `[\.\-_A-Za-z0-9]+`

## Errors

For information about the errors that are common to all actions, see [Common Errors](CommonErrors.md "CommonErrors.md").

**ConflictException**

An action you attempted resulted in an exception.

**resourceId**

The ID of the resource that caused the exception.

**resourceType**

The type of resource that caused the exception.

HTTP Status Code: 409

**InternalException**

This exception occurs due to unexpected causes.

**retryAfterSeconds**

The number of seconds to wait before retrying the action that caused the
exception.

HTTP Status Code: 500

**NotFoundException**

An entity that you specified does not exist.

HTTP Status Code: 404

**ThrottlingException**

An action was throttled.

**quotaCode**

The identifier of the quota that caused the exception.

**retryAfterSeconds**

The number of seconds to wait before retrying the action that caused the
exception.

**serviceCode**

The identifier of the service that caused the exception.

HTTP Status Code: 429

**ValidationException**

Indicates that an error has occurred while performing a validate operation.

**fieldList**

The list of fields for which validation failed and the corresponding failure
messages.

HTTP Status Code: 400

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS Command Line Interface V2](../../../goto/cli2/pipes-2015-10-07/UpdatePipe.md "../../../goto/cli2/pipes-2015-10-07/UpdatePipe.md")
- [AWS SDK for .NET V4](../../../goto/DotNetSDKV4/pipes-2015-10-07/UpdatePipe.md "../../../goto/DotNetSDKV4/pipes-2015-10-07/UpdatePipe.md")
- [AWS SDK for C++](../../../goto/SdkForCpp/pipes-2015-10-07/UpdatePipe.md "../../../goto/SdkForCpp/pipes-2015-10-07/UpdatePipe.md")
- [AWS SDK for Go v2](../../../goto/SdkForGoV2/pipes-2015-10-07/UpdatePipe.md "../../../goto/SdkForGoV2/pipes-2015-10-07/UpdatePipe.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/pipes-2015-10-07/UpdatePipe.md "../../../goto/SdkForJavaV2/pipes-2015-10-07/UpdatePipe.md")
- [AWS SDK for JavaScript V3](../../../goto/SdkForJavaScriptV3/pipes-2015-10-07/UpdatePipe.md "../../../goto/SdkForJavaScriptV3/pipes-2015-10-07/UpdatePipe.md")
- [AWS SDK for Kotlin](../../../goto/SdkForKotlin/pipes-2015-10-07/UpdatePipe.md "../../../goto/SdkForKotlin/pipes-2015-10-07/UpdatePipe.md")
- [AWS SDK for PHP V3](../../../goto/SdkForPHPV3/pipes-2015-10-07/UpdatePipe.md "../../../goto/SdkForPHPV3/pipes-2015-10-07/UpdatePipe.md")
- [AWS SDK for Python](../../../goto/boto3/pipes-2015-10-07/UpdatePipe.md "../../../goto/boto3/pipes-2015-10-07/UpdatePipe.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/pipes-2015-10-07/UpdatePipe.md "../../../goto/SdkForRubyV3/pipes-2015-10-07/UpdatePipe.md")
