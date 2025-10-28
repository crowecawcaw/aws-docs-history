# Events that Amazon SageMaker AI sends to

Amazon EventBridge

Amazon EventBridge monitors status change events in Amazon SageMaker AI. EventBridge enables you to automate SageMaker AI and
respond automatically to events such as a training job status change or endpoint status
change. Events from SageMaker AI are delivered to EventBridge in near real time. You can write simple rules
to indicate which events are of interest to you, and what automated actions to take when an
event matches a rule. To create a rule, see [Creating rules that react to events
in EventBridge](../../../eventbridge/latest/userguide/eb-create-rule.md "../../../eventbridge/latest/userguide/eb-create-rule.md"). If you use AWS CLI, see [put-rule](../../../cli/latest/reference/events/put-rule.md "../../../cli/latest/reference/events/put-rule.md") from the _AWS CLI Command Reference_.

The following sections describe the events that SageMaker AI sends to EventBridge, along with examples.
You can use the examples to help you write automation rules.

###### Note

SageMaker AI may send multiple events to EventBridge for each state change. This behavior is expected
and does not necessarily indicate an error.

Some examples of the actions that can be automatically triggered include the
following:

- Invoking an AWS Lambda function
- Invoking Amazon EC2 Run Command
- Relaying the event to Amazon Kinesis Data Streams
- Activating an AWS Step Functions state machine
- Notifying an Amazon SNS topic or an AWS SMS queue

###### SageMaker AI events monitored by EventBridge

- [SageMaker endpoint deployment state change](#eventbridge-deployment-state "#eventbridge-deployment-state")
- [SageMaker endpoint state change](#eventbridge-endpoint "#eventbridge-endpoint")
- [SageMaker feature group state change](#eventbridge-feature-group "#eventbridge-feature-group")
- [SageMaker hyperparameter tuning job state change](#eventbridge-hpo "#eventbridge-hpo")
- [SageMaker HyperPod cluster event](#eventbridge-hyperpod-cluster-event "#eventbridge-hyperpod-cluster-event")
- [SageMaker HyperPod cluster node health](#eventbridge-hyperpod-node-health "#eventbridge-hyperpod-node-health")
- [SageMaker HyperPod cluster state
  change](#eventbridge-hyperpod-cluster-state "#eventbridge-hyperpod-cluster-state")
- [SageMaker image state change](#eventbridge-image-state "#eventbridge-image-state")
- [SageMaker image version state change](#eventbridge-image-version-state "#eventbridge-image-version-state")
- [SageMaker model card state change](#eventbridge-model-card-state "#eventbridge-model-card-state")
- [SageMaker model package state change](#eventbridge-model-package "#eventbridge-model-package")
- [SageMaker model state change](#eventbridge-model "#eventbridge-model")
- [SageMaker pipeline execution state change](#eventbridge-pipeline "#eventbridge-pipeline")
- [SageMaker pipeline step state change](#eventbridge-pipeline-step "#eventbridge-pipeline-step")
- [SageMaker processing job state change](#processing-job-state "#processing-job-state")
- [SageMaker training job state change](#eventbridge-training "#eventbridge-training")
- [SageMaker transform job state change](#eventbridge-transform "#eventbridge-transform")

## SageMaker endpoint deployment state change

###### Important

The following examples may not work for all endpoints. For a list of features that may
exclude your endpoint, see the [Exclusions](deployment-guardrails-exclusions.md "deployment-guardrails-exclusions.md") page.

Indicates a state change for an endpoint deployment. The following example shows an
endpoint updating with a blue/green canary deployment.

```
{
    "version": "0",
    "id": "0bd4a141-0a02-9d8a-f977-3924c3fb259c",
    "detail-type": "SageMaker Endpoint Deployment State Change",
    "source": "aws.sagemaker",
    "account": "111122223333",
    "time": "2021-10-25T01:52:12Z",
    "region": "us-west-2",
    "resources": [
        "arn:aws:sagemaker:us-west-2:111122223333:endpoint/sample-endpoint"
    ],
    "detail": {
        "EndpointName": "sample-endpoint",
        "EndpointArn": "arn:aws:sagemaker:us-west-2:111122223333:endpoint/sample-endpoint",
        "EndpointConfigName": "sample-endpoint-config-1",
        "ProductionVariants": [
            {
                "VariantName": "AllTraffic",
                "CurrentWeight": 1,
                "DesiredWeight": 1,
                "CurrentInstanceCount": 3,
                "DesiredInstanceCount": 3
            }
        ],
        "EndpointStatus": "UPDATING",
        "CreationTime": 1635195148181,
        "LastModifiedTime": 1635195148181,
        "Tags": {},
        "PendingDeploymentSummary": {
            "EndpointConfigName": "sample-endpoint-config-2",
            "StartTime": Timestamp,
            "ProductionVariants": [
                {
                    "VariantName": "AllTraffic",
                    "CurrentWeight": 1,
                    "DesiredWeight": 1,
                    "CurrentInstanceCount": 1,
                    "DesiredInstanceCount": 3,
                    "VariantStatus": [
                        {
                            "Status": "Baking",
                            "StatusMessage": "Baking for 600 seconds (TerminationWaitInSeconds) with traffic enabled on canary capacity of 1 instance(s).",
                            "StartTime": 1635195269181,
                        }
                    ]
                }
            ]
        }
    }
}
```

The following example indicates a state change for an endpoint deployment, which is
being updated with new capacity on an existing endpoint configuration.

```
{
    "version": "0",
    "id": "0bd4a141-0a02-9d8a-f977-3924c3fb259c",
    "detail-type": "SageMaker Endpoint Deployment State Change",
    "source": "aws.sagemaker",
    "account": "111122223333",
    "time": "2021-10-25T01:52:12Z",
    "region": "us-west-2",
    "resources": [
        "arn:aws:sagemaker:us-west-2:651393343886:endpoint/sample-endpoint"
    ],
    "detail": {
        "EndpointName": "sample-endpoint",
        "EndpointArn": "arn:aws:sagemaker:us-west-2:651393343886:endpoint/sample-endpoint",
        "EndpointConfigName": "sample-endpoint-config-1",
        "ProductionVariants": [
            {
                "VariantName": "AllTraffic",
                "CurrentWeight": 1,
                "DesiredWeight": 1,
                "CurrentInstanceCount": 3,
                "DesiredInstanceCount": 6,
                "VariantStatus": [
                    {
                        "Status": "Updating",
                        "StatusMessage": "Scaling out desired instance count to 6.",
                        "StartTime": 1635195269181,
                    }
                ]
            }
        ],
        "EndpointStatus": "UPDATING",
        "CreationTime": 1635195148181,
        "LastModifiedTime": 1635195148181,
        "Tags": {},
    }
```

The following secondary deployment statuses are also available for endpoints found in
the `VariantStatus` object.

- `Creating`: creating instances for the production variant.

Example message: `"Launching X instance(s)."`

- `Deleting`: terminating instances for the production variant.

Example message: `"Terminating X instance(s)."`

- `Updating`: updating capacity for the production variant.

Example messages: `"Launching X instance(s)."`, `"Scaling out
 desired instance count to X."`

- `ActivatingTraffic`: turning on traffic for the production
  variant.

Example message: `"Activating traffic on canary capacity of X
 instance(s)."`

- `Baking`: waiting period to monitor the CloudWatch alarms in the auto-rollback
  configuration.

Example message: `"Baking for X seconds (TerminationWaitInSeconds) with traffic
 enabled on full capacity of Y instance(s)."`

## SageMaker endpoint state change

Indicates a change in the status of a SageMaker AI hosted real-time inference endpoint.

The following shows an event with an endpoint in the `IN_SERVICE`
state.

```
{
  "version": "0",
  "id": "d2921b5a-b0ad-cace-a8e3-0f159d018e06",
  "detail-type": "SageMaker Endpoint State Change",
  "source": "aws.sagemaker",
  "account": "111122223333",
  "time": "1583831889050",
  "region": "us-west-2",
  "resources": [
      "arn:aws:sagemaker:us-west-2:111122223333:endpoint/myendpoint"
  ],
  "detail": {
      "EndpointName": "MyEndpoint",
      "EndpointArn": "arn:aws:sagemaker:us-west-2:111122223333:endpoint/myendpoint",
      "EndpointConfigName": "MyEndpointConfig",
      "ProductionVariants": [
          {
              "DesiredWeight": 1.0,
              "DesiredInstanceCount": 1.0
          }
      ],
      "EndpointStatus": "IN_SERVICE",
      "CreationTime": 1592411992203.0,
      "LastModifiedTime": 1592411994287.0,
      "Tags": {

      }
  }
}
```

## SageMaker feature group state change

Indicates a change either in the `FeatureGroupStatus` or the
`OfflineStoreStatus` of a SageMaker feature group.

```
{
  "version": "0",
  "id": "93201303-abdb-36a4-1b9b-4c1c3e3671c0",
  "detail-type": "SageMaker Feature Group State Change",
  "source": "aws.sagemaker",
  "account": "111122223333",
  "time": "2021-01-26T01:22:01Z",
  "region": "us-east-1",
  "resources": [
    "arn:aws:sagemaker:us-east-1:111122223333:feature-group/sample-feature-group"
  ],
  "detail": {
    "FeatureGroupArn": "arn:aws:sagemaker:us-east-1:111122223333:feature-group/sample-feature-group",
    "FeatureGroupName": "sample-feature-group",
    "RecordIdentifierFeatureName": "RecordIdentifier",
    "EventTimeFeatureName": "EventTime",
    "FeatureDefinitions": [
      {
        "FeatureName": "RecordIdentifier",
        "FeatureType": "Integral"
      },
      {
        "FeatureName": "EventTime",
        "FeatureType": "Fractional"
      }
    ],
    "CreationTime": 1611624059000,
    "OnlineStoreConfig": {
      "EnableOnlineStore": true
    },
    "OfflineStoreConfig": {
      "S3StorageConfig": {
        "S3Uri": "s3://offline/s3/uri"
      },
      "DisableGlueTableCreation": false,
      "DataCatalogConfig": {
        "TableName": "sample-feature-group-1611624059",
        "Catalog": "AwsDataCatalog",
        "Database": "sagemaker_featurestore"
      }
    },
    "RoleArn": "arn:aws:iam::111122223333:role/SageMakerRole",
    "FeatureGroupStatus": "Active",
    "Tags": {}
  }
}
```

## SageMaker hyperparameter tuning job state change

Indicates a change in the status of a SageMaker hyperparameter tuning job.

```
{
  "version": "0",
  "id": "844e2571-85d4-695f-b930-0153b71dcb42",
  "detail-type": "SageMaker HyperParameter Tuning Job State Change",
  "source": "aws.sagemaker",
  "account": "111122223333",
  "time": "2018-10-06T12:26:13Z",
  "region": "us-east-1",
  "resources": [
    "arn:aws:sagemaker:us-east-1:111122223333:tuningJob/x"
  ],
  "detail": {
    "HyperParameterTuningJobName": "016bffd3-6d71-4d3a-9710-0a332b2759fc",
    "HyperParameterTuningJobArn": "arn:aws:sagemaker:us-east-1:111122223333:tuningJob/x",
    "TrainingJobDefinition": {
      "StaticHyperParameters": {},
      "AlgorithmSpecification": {
        "TrainingImage": "trainingImageName",
        "TrainingInputMode": "inputModeFile",
        "MetricDefinitions": [
          {
            "Name": "metricName",
            "Regex": "regex"
          }
        ]
      },
      "RoleArn": "roleArn",
      "InputDataConfig": [
        {
          "ChannelName": "channelName",
          "DataSource": {
            "S3DataSource": {
              "S3DataType": "s3DataType",
              "S3Uri": "s3Uri",
              "S3DataDistributionType": "s3DistributionType"
            }
          },
          "ContentType": "contentType",
          "CompressionType": "gz",
          "RecordWrapperType": "RecordWrapper"
        }
      ],
      "VpcConfig": {
        "SecurityGroupIds": [
          "securityGroupIds"
        ],
        "Subnets": [
          "subnets"
        ]
      },
      "OutputDataConfig": {
        "KmsKeyId": "kmsKeyId",
        "S3OutputPath": "s3OutputPath"
      },
      "ResourceConfig": {
        "InstanceType": "instanceType",
        "InstanceCount": 10,
        "VolumeSizeInGB": 500,
        "VolumeKmsKeyId": "volumeKeyId"
      },
      "StoppingCondition": {
        "MaxRuntimeInSeconds": 3600
      }
    },
    "HyperParameterTuningJobStatus": "status",
    "CreationTime": "1583831889050",
    "LastModifiedTime": "1583831889050",
    "TrainingJobStatusCounters": {
      "Completed": 1,
      "InProgress": 0,
      "RetryableError": 0,
      "NonRetryableError": 0,
      "Stopped": 0
    },
    "ObjectiveStatusCounters": {
      "Succeeded": 1,
      "Pending": 0,
      "Failed": 0
    },
    "Tags": {}
  }
}
```

## SageMaker HyperPod cluster event

Indicates a new event in the state of a SageMaker HyperPod cluster. For more information, see
the [DescribeClusterEvent](../APIReference/API_DescribeClusterEvent.md "../APIReference/API_DescribeClusterEvent.md") operation.

```
{
    "version": "0",
    "id": "0bd4a141-0a02-9d8a-f977-3924c3fb259c",
    "detail-type": "SageMaker HyperPod Cluster Event",
    "source": "aws.sagemaker",
    "account": "[REDACTED:BANK_ACCOUNT_NUMBER]",
    "time": "2025-04-28T16:59:01Z",
    "region": "us-west-2",
    "resources": [
        "arn:aws:sagemaker:us-west-2:111122223333:cluster/sample-cluster"
    ],
    "detail": {
        "EventDetails": {
            "EventId": "a307fae0-6937-40f9-af2f-16eb873d340a",
            "ClusterArn": "arn:aws:sagemaker:us-west-2:111122223333:cluster/sample-cluster",
            "ClusterName": "sample-cluster",
            "InstanceGroupName": "sample-instance-group",
            "InstanceId": "i-0391f86fa0fe0d465",
            "ResourceType": "Instance",
            "EventTime": 1745858447412,
            "EventDetails": {
                "EventMetadata": {
                    "Instance": {
                        "LcsExecutionState": "Started"
                    }
                }
            },
            "Description": "Instance lifecycle script execution for EC2InstanceId i-0391f86fa0fe0d465 has Started"
        }
    }
}
```

## SageMaker HyperPod cluster node health

Indicates when HyperPod detects unhealthy nodes or when unhealthy nodes
transition to a healthy state.

```
{
    "version": "0",
    "id": "0bd4a141-0a02-9d8a-f977-3924c3fb259c",
    "detail-type": "SageMaker HyperPod Cluster Node Health Event",
    "source": "aws.sagemaker",
    "account": "111122223333",
    "time": "2021-10-25T01:52:12Z",
    "region": "us-west-2",
    "resources": [
        "arn:aws:sagemaker:us-west-2:111122223333:cluster/sample-cluster"
    ],
    "detail": {
        "ClusterName": "sample-cluster",
        "ClusterArn": "arn:aws:sagemaker:us-west-2:111122223333:cluster/sample-cluster",
        "InstanceId": "i-12345678abcdefghi",
        "Tags": {},
        "HealthSummary": {
            "HealthStatus": "Unhealthy",
            "HealthStatusReason": "HyperPod Health Monitoring Agent (HMA) has detected fault type NvidiaErrorTerminate on this node and is unhealthy.",
            "RepairAction": "None",
            "Recommendation": "Please Replace the Faulty Node."
        }
    }
}
```

## SageMaker HyperPod cluster state

change

Indicates a change in the state of a SageMaker HyperPod cluster. For more information, see the
[DescribeCluster](../APIReference/API_DescribeCluster.md#API_DescribeCluster_ResponseSyntax "../APIReference/API_DescribeCluster.md#API_DescribeCluster_ResponseSyntax") API reference.

```
{
   "version": "0",
   "id": "0bd4a141-0a02-9d8a-f977-3924c3fb259c",
   "detail-type": "SageMaker HyperPod Cluster State Change",
   "source": "aws.sagemaker",
   "account": "111122223333",
   "time": "2025-04-28T16:59:01Z",
   "region": "us-west-2",
   "resources": [
      "arn:aws:sagemaker:us-west-2:111122223333:cluster/sample-cluster"
   ],
   "detail": {
      "ClusterArn": "arn:aws:sagemaker:us-west-2:111122223333:cluster/sample-cluster",
      "ClusterName": "sample-cluster",
      "ClusterStatus": "InService",
      "CreationTime": 1745858447412,
      "FailureMessage": "",
      "InstanceGroups": [
         {
            "CurrentCount": 1,
            "ExecutionRole": "arn:aws:iam::111122223333:role/sagemaker-hyperpod-AmazonSagemakerClusterExecutionR-123OTacPcKk1",
            "InstanceGroupName": "example instance group name",
            "InstanceStorageConfigs": [
               {}
            ],
            "InstanceType": "ml.t3.medium",
            "LifeCycleConfig": {
               "OnCreate": "on_create.sh",
               "SourceS3Uri": "s3://sagemaker-hyperpod//LifeCycleScripts/base-config/provisioning_parameters.json"
            },
            "OnStartDeepHealthChecks": [
               "example health checks"
            ],
            "OverrideVpcConfig": {
               "SecurityGroupIds": [
                  "SecurityGroupId1"
               ],
               "Subnets": [
                  "Subnet1"
               ]
            },
            "Status": "Failed",
            "TargetCount": 2,
            "ThreadsPerCore": 2,
            "TrainingPlanArn": "arn:aws:sagemaker:us-west-2:111122223333:training-plan/large-models-fine-tuning",
            "TrainingPlanStatus": "NotApplicable"
         }
      ],
      "NodeRecovery": "Automatic",
      "Orchestrator": {
         "Eks": {
            "ClusterArn": "arn:aws:eks:us-west-2:111122223333:cluster/my-hyperPod-eks-cluster"
         }
      },
      "VpcConfig": {
         "SecurityGroupIds": [
            "SecurityGroupId2"
         ],
         "Subnets": [
            "Subnet2"
         ]
      }
   }
}
```

## SageMaker image state change

Indicates a change in the status of a SageMaker image.

```
{
  "version": "0",
  "id": "cee033a3-17d8-49f8-865f-b9ebf485d9ee",
  "detail-type": "SageMaker Image State Change",
  "source": "aws.sagemaker",
  "account": "111122223333",
  "time": "2021-04-29T01:29:59Z",
  "region": "us-east-1",
  "resources": ["arn:aws:sagemaker:us-west-2:111122223333:image/cee033a3-17d8-49f8-865f-b9ebf485d9ee"],
  "detail": {
    "ImageName": "cee033a3-17d8-49f8-865f-b9ebf485d9ee",
    "ImageArn": "arn:aws:sagemaker:us-west-2:111122223333:image/cee033a3-17d8-49f8-865f-b9ebf485d9ee",
    "ImageStatus": "Creating",
    "Version": 1.0,
    "Tags": {}
  }
}
```

## SageMaker image version state change

Indicates a change in the status of a SageMaker image version.

```
{
  "version": "0",
  "id": "07fc4615-ebd7-15fc-1746-243411f09f04",
  "detail-type": "SageMaker Image Version State Change",
  "source": "aws.sagemaker",
  "account": "111122223333",
  "time": "2021-04-29T01:29:59Z",
  "region": "us-east-1",
  "resources": ["arn:aws:sagemaker:us-west-2:111122223333:image-version/07800032-2d29-48b7-8f82-5129225b2a85"],
  "detail": {
    "ImageArn": "arn:aws:sagemaker:us-west-2:111122223333:image/a70ff896-c832-4fe8-add6-eba25a0f43e6",
    "ImageVersionArn": "arn:aws:sagemaker:us-west-2:111122223333:image-version/07800032-2d29-48b7-8f82-5129225b2a85",
    "ImageVersionStatus": "Creating",
    "Version": 1.0,
    "Tags": {}
  }
}
```

## SageMaker model card state change

Indicates a change in the status of an Amazon SageMaker model card. For more information about
model cards, see [Amazon SageMaker Model Cards](model-cards.md "model-cards.md").

```
{
    "version": "0",
    "id": "aa7a9c4f-2caa-4d04-a6de-e67227ba4302",
    "detail-type": "SageMaker Model Card State Change",
    "source": "aws.sagemaker",
    "account": "111122223333",
    "time": "2022-11-30T00:00:00Z",
    "region": "us-east-1",
    "resources": [
        "arn:aws:sagemaker:us-east-1:111122223333:model-card/example-card"
    ],
    "detail": {
        "ModelCardVersion": 2,
        "LastModifiedTime": "2022-12-03T00:09:44.893854735Z",
        "LastModifiedBy": {
            "DomainId": "us-east-1",
            "UserProfileArn": "arn:aws:sagemaker:us-east-1:111122223333:user-profile/user",
            "UserProfileName": "user"
        },
        "CreationTime": "2022-12-03T00:09:33.084Z",
        "CreatedBy": {
            "DomainId": "us-east-1",
            "UserProfileArn": "arn:aws:sagemaker:us-east-1:111122223333:user-profile/user",
            "UserProfileName": "user"
        },
        "ModelCardName": "example-card",
        "ModelId": "example-model",
        "ModelCardStatus": "Draft",
        "AccountId": "111122223333",
        "SecurityConfig": {}
    }
}
```

## SageMaker model package state change

Indicates a change in the status of a SageMaker model package.

```
{
  "version": "0",
  "id": "844e2571-85d4-695f-b930-0153b71dcb42",
  "detail-type": "SageMaker Model Package State Change",
  "source": "aws.sagemaker",
  "account": "111122223333",
  "time": "2021-02-24T17:00:14Z",
  "region": "us-east-2",
  "resources": [
    "arn:aws:sagemaker:us-east-2:111122223333:model-package/versionedmp-p-idy6c3e1fiqj/2"
  ],
  "source": [
    "aws.sagemaker"
  ],
  "detail": {
    "ModelPackageGroupName": "versionedmp-p-idy6c3e1fiqj",
    "ModelPackageVersion": 2,
    "ModelPackageArn": "arn:aws:sagemaker:us-east-2:111122223333:model-package/versionedmp-p-idy6c3e1fiqj/2",
    "CreationTime": "2021-02-24T17:00:14Z",
    "InferenceSpecification": {
      "Containers": [
        {
          "Image": "257758044811.dkr.ecr.us-east-2.amazonaws.com/sagemaker-xgboost:1.0-1-cpu-py3",
          "ImageDigest": "sha256:4dc8a7e4a010a19bb9e0a6b063f355393f6e623603361bd8b105f554d4f0c004",
          "ModelDataUrl": "s3://sagemaker-project-p-idy6c3e1fiqj/versionedmp-p-idy6c3e1fiqj/AbaloneTrain/pipelines-4r83jejmhorv-TrainAbaloneModel-xw869y8C4a/output/model.tar.gz"
        }
      ],
      "SupportedContentTypes": [
        "text/csv"
      ],
      "SupportedResponseMIMETypes": [
        "text/csv"
      ]
    },
    "ModelPackageStatus": "Completed",
    "ModelPackageStatusDetails": {
      "ValidationStatuses": [],
      "ImageScanStatuses": []
    },
    "CertifyForMarketplace": false,
    "ModelApprovalStatus": "Rejected",
    "MetadataProperties": {
      "GeneratedBy": "arn:aws:sagemaker:us-east-2:111122223333:pipeline/versionedmp-p-idy6c3e1fiqj/execution/4r83jejmhorv"
    },
    "ModelMetrics": {
      "ModelQuality": {
        "Statistics": {
          "ContentType": "application/json",
          "S3Uri": "s3://sagemaker-project-p-idy6c3e1fiqj/versionedmp-p-idy6c3e1fiqj/script-2021-02-24-10-55-15-413/output/evaluation/evaluation.json"
        }
      }
    },
    "ModelLifeCycle": {
      "Stage": "Development",
      "StageStatus": "Approved",
      "StageDescription": "StageDescription"
    },
    "UpdatedModelPackageFields": [
      "ModelLifeCycle"
      # Other possible values are
      # "ModelApprovalStatus","ApprovalDescription","sourceUri","CustomerMetadataProperties", "InferenceSpecification"
    ]
    "LastModifiedTime": "2021-02-24T17:00:14Z"
  }
}
```

## SageMaker model state change

Indicates a change in the state of a SageMaker AI model. The state changes when a SageMaker AI model is
either created or deleted.

```
{
  "source": ["aws.sagemaker"],
  "detail-type": ["SageMaker Model State Change"],
  "Resources" : ["arn:aws:sagemaker:us-east-1:111122223333:model/model-name"]
}
```

If a model is specified under `Resources`, an event will be generated and
sent to EventBridge when the state of this model changes. If you do not specify a value for
`Resources`, an event will generate when the status of any of the SageMaker AI models
associated with your account changes.

## SageMaker pipeline execution state change

Indicates a change in the status of a SageMaker pipeline execution.

`currentPipelineExecutionStatus` and
`previousPipelineExecutionStatus`can be one of the following values:

- Executing
- Succeeded
- Failed
- Stopping
- Stopped

```
{
  "version": "0",
  "id": "315c1398-40ff-a850-213b-158f73kd93ir",
  "detail-type": "SageMaker Model Building Pipeline Execution Status Change",
  "source": "aws.sagemaker",
  "account": "111122223333",
  "time": "2021-03-15T16:10:11Z",
  "region": "us-east-1",
  "resources": ["arn:aws:sagemaker:us-east-1:111122223333:pipeline/myPipeline-123", "arn:aws:sagemaker:us-east-1:111122223333:pipeline/myPipeline-123/execution/p4jn9xou8a8s"],
  "detail": {
    "pipelineExecutionDisplayName": "SomeDisplayName",
    "currentPipelineExecutionStatus": "Succeeded",
    "previousPipelineExecutionStatus": "Executing",
    "executionStartTime": "2021-03-15T16:03:13Z",
    "executionEndTime": "2021-03-15T16:10:10Z",
    "pipelineExecutionDescription": "SomeDescription",
    "pipelineArn": "arn:aws:sagemaker:us-east-1:111122223333:pipeline/myPipeline-123",
    "pipelineExecutionArn": "arn:aws:sagemaker:us-east-1:111122223333:pipeline/myPipeline-123/execution/p4jn9xou8a8s"
  }
}
```

## SageMaker pipeline step state change

Indicates a change in the status of a SageMaker pipeline step.

If there is a cache hit, the event contains the `cacheHitResult` field.
`currentStepStatus` and `previousStepStatus`can be one of the
following values:

- Starting
- Executing
- Succeeded
- Failed
- Stopping
- Stopped

If the value of `currentStepStatus` is `Failed`, the event
contains the `failureReason` field, which provides a description of why the step
failed.

```
{
  "version": "0",
  "id": "ea37ccbb-5e2b-05e9-4073-1daazc940304",
  "detail-type": "SageMaker Model Building Pipeline Execution Step Status Change",
  "source": "aws.sagemaker",
  "account": "111122223333",
  "time": "2021-03-15T16:10:10Z",
  "region": "us-east-1",
  "resources": ["arn:aws:sagemaker:us-east-1:111122223333:pipeline/myPipeline-123", "arn:aws:sagemaker:us-east-1:111122223333:pipeline/myPipeline-123/execution/p4jn9xou8a8s"],
  "detail": {
    "metadata": {
      "processingJob": {
        "arn": "arn:aws:sagemaker:us-east-1:111122223333:processing-job/pipelines-p4jn9xou8a8s-myprocessingstep1-tmgxry49ug"
      }
    },
    "stepStartTime": "2021-03-15T16:03:14Z",
    "stepEndTime": "2021-03-15T16:10:09Z",
    "stepName": "myprocessingstep1",
    "stepType": "Processing",
    "previousStepStatus": "Executing",
    "currentStepStatus": "Succeeded",
    "pipelineArn": "arn:aws:sagemaker:us-east-1:111122223333:pipeline/myPipeline-123",
    "pipelineExecutionArn": "arn:aws:sagemaker:us-east-1:111122223333:pipeline/myPipeline-123/execution/p4jn9xou8a8s"
  }
}
```

## SageMaker processing job state change

Indicates a change in the status of a SageMaker processing job.

The following example event is for a failed processing job, where the
`ProcessingJobStatus` value is `Failed`.

```
{
  "version": "0",
  "id": "0a15f67d-aa23-0123-0123-01a23w89r01t",
  "detail-type": "SageMaker Processing Job State Change",
  "source": "aws.sagemaker",
  "account": "111122223333",
  "time": "2019-05-31T21:49:54Z",
  "region": "us-east-1",
  "resources": ["arn:aws:sagemaker:us-west-2:037210630506:processing-job/integ-test-analytics-algo-54ee3282-5899-4aa3-afc2-7ce1d02"],
  "detail": {
    "ProcessingInputs": [{
      "InputName": "InputName",
      "S3Input": {
        "S3Uri": "s3://input/s3/uri",
        "LocalPath": "/opt/ml/processing/input/local/path",
        "S3DataType": "MANIFEST_FILE",
        "S3InputMode": "PIPE",
        "S3DataDistributionType": "FULLYREPLICATED"
      }
    }],
    "ProcessingOutputConfig": {
      "Outputs": [{
        "OutputName": "OutputName",
        "S3Output": {
          "S3Uri": "s3://output/s3/uri",
          "LocalPath": "/opt/ml/processing/output/local/path",
          "S3UploadMode": "CONTINUOUS"
        }
      }],
      "KmsKeyId": "KmsKeyId"
    },
    "ProcessingJobName": "integ-test-analytics-algo-54ee3282-5899-4aa3-afc2-7ce1d02",
    "ProcessingResources": {
      "ClusterConfig": {
        "InstanceCount": 3,
        "InstanceType": "ml.c5.xlarge",
        "VolumeSizeInGB": 5,
        "VolumeKmsKeyId": "VolumeKmsKeyId"
      }
    },
    "StoppingCondition": {
      "MaxRuntimeInSeconds": 2000
    },
    "AppSpecification": {
      "ImageUri": "012345678901.dkr.ecr.us-west-2.amazonaws.com/processing-uri:latest"
    },
    "NetworkConfig": {
      "EnableInterContainerTrafficEncryption": true,
      "EnableNetworkIsolation": false,
      "VpcConfig": {
        "SecurityGroupIds": ["SecurityGroupId1", "SecurityGroupId2", "SecurityGroupId3"],
        "Subnets": ["Subnet1", "Subnet2"]
      }
    },
    "RoleArn": "arn:aws:iam::037210630506:role/SageMakerPowerUser",
    "ExperimentConfig": {},
    "ProcessingJobArn": "arn:aws:sagemaker:us-west-2:037210630506:processing-job/integ-test-analytics-algo-54ee3282-5899-4aa3-afc2-7ce1d02",
    "ProcessingJobStatus":"Failed",
    "FailureReason":"InternalServerError: We encountered an internal error.  Please try again.",
    "ProcessingEndTime":1704320746000,
    "ProcessingStartTime":1704320734000,
    "LastModifiedTime":1704320746000,
    "CreationTime":1704320199000
  }
}
```

## SageMaker training job state change

Indicates a change in the status of a SageMaker training job.

If the value of `TrainingJobStatus` is `Failed`, the event
contains the `FailureReason` field, which provides a description of why the
training job failed.

```
{
    "version": "0",
    "id": "844e2571-85d4-695f-b930-0153b71dcb42",
    "detail-type": "SageMaker Training Job State Change",
    "source": "aws.sagemaker",
    "account": "111122223333",
    "time": "2018-10-06T12:26:13Z",
    "region": "us-east-1",
    "resources": [
        "arn:aws:sagemaker:us-east-1:111122223333:training-job/kmeans-1"
    ],
    "detail": {
        "TrainingJobName": "89c96cc8-dded-4739-afcc-6f1dc936701d",
        "TrainingJobArn": "arn:aws:sagemaker:us-east-1:111122223333:training-job/kmeans-1",
        "TrainingJobStatus": "Completed",
        "SecondaryStatus": "Completed",
        "HyperParameters": {
            "Hyper": "Parameters"
        },
        "AlgorithmSpecification": {
            "TrainingImage": "TrainingImage",
            "TrainingInputMode": "TrainingInputMode"
        },
        "RoleArn": "arn:aws:iam::111122223333:role/SMRole",
        "InputDataConfig": [
            {
                "ChannelName": "Train",
                "DataSource": {
                    "S3DataSource": {
                        "S3DataType": "S3DataType",
                        "S3Uri": "S3Uri",
                        "S3DataDistributionType": "S3DataDistributionType"
                    }
                },
                "ContentType": "ContentType",
                "CompressionType": "CompressionType",
                "RecordWrapperType": "RecordWrapperType"
            }
        ],
        "OutputDataConfig": {
            "KmsKeyId": "KmsKeyId",
            "S3OutputPath": "S3OutputPath"
        },
        "ResourceConfig": {
            "InstanceType": "InstanceType",
            "InstanceCount": 3,
            "VolumeSizeInGB": 20,
            "VolumeKmsKeyId": "VolumeKmsKeyId"
        },
        "VpcConfig": {

        },
        "StoppingCondition": {
            "MaxRuntimeInSeconds": 60
        },
        "CreationTime": "1583831889050",
        "TrainingStartTime": "1583831889050",
        "TrainingEndTime": "1583831889050",
        "LastModifiedTime": "1583831889050",
        "SecondaryStatusTransitions": [

        ],
        "Tags": {

        }
    }
}
```

## SageMaker transform job state change

Indicates a change in the status of a SageMaker batch transform job.

If the value of `TransformJobStatus` is `Failed`, the event
contains the `FailureReason` field, which provides a description of why the
training job failed.

```
{
  "version": "0",
  "id": "844e2571-85d4-695f-b930-0153b71dcb42",
  "detail-type": "SageMaker Transform Job State Change",
  "source": "aws.sagemaker",
  "account": "111122223333",
  "time": "2018-10-06T12:26:13Z",
  "region": "us-east-1",
  "resources": ["arn:aws:sagemaker:us-east-1:111122223333:transform-job/myjob"],
  "detail": {
    "TransformJobName": "4b52bd8f-e034-4345-818d-884bdd7c9724",
    "TransformJobArn": "arn:aws:sagemaker:us-east-1:111122223333:transform-job/myjob",
    "TransformJobStatus": "another status... GO",
    "FailureReason": "failed why 1",
    "ModelName": "i am a beautiful model",
    "MaxConcurrentTransforms": 5,
    "MaxPayloadInMB": 10,
    "BatchStrategy": "Strategizing...",
    "Environment": {
      "environment1": "environment2"
    },
    "TransformInput": {
      "DataSource": {
        "S3DataSource": {
          "S3DataType": "s3DataType",
          "S3Uri": "s3Uri"
        }
      },
      "ContentType": "content type",
      "CompressionType": "compression type",
      "SplitType": "split type"
    },
    "TransformOutput": {
      "S3OutputPath": "s3Uri",
      "Accept": "accept",
      "AssembleWith": "assemblyType",
      "KmsKeyId": "kmsKeyId"
    },
    "TransformResources": {
      "InstanceType": "instanceType",
      "InstanceCount": 3
    },
    "CreationTime": "2018-10-06T12:26:13Z",
    "TransformStartTime": "2018-10-06T12:26:13Z",
    "TransformEndTime": "2018-10-06T12:26:13Z",
    "Tags": {}
  }
}
```

For more information about the status values and their meanings for SageMaker AI jobs, endpoints,
and pipelines, see the following links:

- [`AlgorithmStatus`](../APIReference/API_DescribeAlgorithm.md#sagemaker-DescribeAlgorithm-response-AlgorithmStatus "../APIReference/API_DescribeAlgorithm.md#sagemaker-DescribeAlgorithm-response-AlgorithmStatus")
- [`EndpointStatus`](../APIReference/API_DescribeEndpoint.md#sagemaker-DescribeEndpoint-response-EndpointStatus "../APIReference/API_DescribeEndpoint.md#sagemaker-DescribeEndpoint-response-EndpointStatus")
- [`FeatureGroupStatus`](../APIReference/API_DescribeFeatureGroup.md#sagemaker-DescribeFeatureGroup-response-FeatureGroupStatus "../APIReference/API_DescribeFeatureGroup.md#sagemaker-DescribeFeatureGroup-response-FeatureGroupStatus")
- [`HyperParameterTuningJobStatus`](../APIReference/API_DescribeHyperParameterTuningJob.md#sagemaker-DescribeHyperParameterTuningJob-response-HyperParameterTuningJobStatus "../APIReference/API_DescribeHyperParameterTuningJob.md#sagemaker-DescribeHyperParameterTuningJob-response-HyperParameterTuningJobStatus")
- [`LabelingJobStatus`](../APIReference/API_DescribeLabelingJob.md#sagemaker-DescribeLabelingJob-response-LabelingJobStatus "../APIReference/API_DescribeLabelingJob.md#sagemaker-DescribeLabelingJob-response-LabelingJobStatus")
- [`ModelPackageStatus`](../APIReference/API_DescribeModelPackage.md#sagemaker-DescribeModelPackage-response-ModelPackageStatus "../APIReference/API_DescribeModelPackage.md#sagemaker-DescribeModelPackage-response-ModelPackageStatus")
- [`NotebookInstanceStatus`](../APIReference/API_DescribeNotebookInstance.md#sagemaker-DescribeNotebookInstance-response-NotebookInstanceStatus "../APIReference/API_DescribeNotebookInstance.md#sagemaker-DescribeNotebookInstance-response-NotebookInstanceStatus")
- [`PipelineExecutionStatus`](../APIReference/API_DescribePipelineExecution.md#sagemaker-DescribePipelineExecution-response-PipelineExecutionStatus "../APIReference/API_DescribePipelineExecution.md#sagemaker-DescribePipelineExecution-response-PipelineExecutionStatus")
- [`StepStatus`](../APIReference/API_PipelineExecutionStep.md#sagemaker-Type-PipelineExecutionStep-StepStatus "../APIReference/API_PipelineExecutionStep.md#sagemaker-Type-PipelineExecutionStep-StepStatus")
- [`ProcessingJobStatus`](../APIReference/API_DescribeProcessingJob.md#sagemaker-DescribeProcessingJob-response-ProcessingJobStatus "../APIReference/API_DescribeProcessingJob.md#sagemaker-DescribeProcessingJob-response-ProcessingJobStatus")
- [`TrainingJobStatus`](../APIReference/API_DescribeTrainingJob.md#sagemaker-DescribeTrainingJob-response-TrainingJobStatus "../APIReference/API_DescribeTrainingJob.md#sagemaker-DescribeTrainingJob-response-TrainingJobStatus")
- [`TransformJobStatus`](../APIReference/API_DescribeTransformJob.md#sagemaker-DescribeTransformJob-response-TransformJobStatus "../APIReference/API_DescribeTransformJob.md#sagemaker-DescribeTransformJob-response-TransformJobStatus")
  For more information, see the [Amazon EventBridge User
  Guide](../../../eventbridge/latest/userguide/what-is-amazon-eventbridge.md "../../../eventbridge/latest/userguide/what-is-amazon-eventbridge.md").
