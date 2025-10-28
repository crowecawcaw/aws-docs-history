# Create and manage Amazon SageMaker AI jobs with Step Functions

Learn how to use Step Functions to create and manage jobs on SageMaker AI. This page lists the supported SageMaker AI API actions and provides example
`Task` states to create SageMaker AI transform, training, labeling, and processing jobs.

To learn about integrating with AWS services in Step Functions, see [Integrating services](integrate-services.md "integrate-services.md") and [Passing parameters to a service API in Step Functions](connect-parameters.md "connect-parameters.md").

###### Key features of Optimized SageMaker AI integration

- The [Run a Job (.sync)](connect-to-resource.md#connect-sync "connect-to-resource.md#connect-sync") integration
  pattern is supported.
- There are no specific optimizations for the [Request Response](connect-to-resource.md#connect-default "connect-to-resource.md#connect-default") integration pattern.
- The [Wait for a Callback with Task Token](connect-to-resource.md#connect-wait-token "connect-to-resource.md#connect-wait-token")
  integration pattern is not supported.

## Optimized SageMaker AI APIs

- [`CreateEndpoint`](../../../sagemaker/latest/dg/API_CreateEndpoint.md "../../../sagemaker/latest/dg/API_CreateEndpoint.md")
- [`CreateEndpointConfig`](../../../sagemaker/latest/dg/API_CreateEndpointConfig.md "../../../sagemaker/latest/dg/API_CreateEndpointConfig.md")
- [`CreateHyperParameterTuningJob`](../../../sagemaker/latest/dg/API_CreateHyperParameterTuningJob.md "../../../sagemaker/latest/dg/API_CreateHyperParameterTuningJob.md") - Supports the `.sync` integration pattern.
- [`CreateLabelingJob`](../../../sagemaker/latest/dg/API_CreateLabelingJob.md "../../../sagemaker/latest/dg/API_CreateLabelingJob.md") - Supports the `.sync` integration pattern.
- [`CreateModel`](../../../sagemaker/latest/dg/API_CreateModel.md "../../../sagemaker/latest/dg/API_CreateModel.md")
- [`CreateProcessingJob`](../../../sagemaker/latest/dg/API_CreateProcessingJob.md "../../../sagemaker/latest/dg/API_CreateProcessingJob.md") - Supports the `.sync` integration pattern.
- [`CreateTrainingJob`](../../../sagemaker/latest/dg/API_CreateTrainingJob.md "../../../sagemaker/latest/dg/API_CreateTrainingJob.md") - Supports the `.sync` integration pattern.
- [`CreateTransformJob`](../../../sagemaker/latest/dg/API_CreateTransformJob.md "../../../sagemaker/latest/dg/API_CreateTransformJob.md") - Supports the `.sync` integration pattern.
- [`UpdateEndpoint`](../../../sagemaker/latest/dg/API_UpdateEndpoint.md "../../../sagemaker/latest/dg/API_UpdateEndpoint.md")

###### Note

AWS Step Functions will not automatically create a policy for
`CreateTransformJob`. You must attach an inline policy to the
created role. For more information, see this example IAM policy: [CreateTrainingJob](#sagemaker-iam-createtrainingjob "#sagemaker-iam-createtrainingjob").

## SageMaker AI Transform Job Example

The following includes a `Task` state that creates an Amazon SageMaker AI transform
job, specifying the Amazon S3 location for `DataSource` and
`TransformOutput`.

```
{
"SageMaker CreateTransformJob": {
  "Type": "Task",
  "Resource": "arn:aws:states:::sagemaker:createTransformJob.sync",
  "Arguments": {
    "ModelName": "SageMakerCreateTransformJobModel-9iFBKsYti9vr",
    "TransformInput": {
      "CompressionType": "None",
      "ContentType": "text/csv",
      "DataSource": {
        "S3DataSource": {
          "S3DataType": "S3Prefix",
          "S3Uri": "s3://amzn-s3-demo-source-bucket1/TransformJobDataInput.txt"
        }
      }
    },
    "TransformOutput": {
      "S3OutputPath": "s3://amzn-s3-demo-source-bucket1/TransformJobOutputPath"
    },
    "TransformResources": {
      "InstanceCount": 1,
      "InstanceType": "ml.m4.xlarge"
    },
    "TransformJobName": "sfn-binary-classification-prediction"
  },
  "Next": "ValidateOutput"
},
```

## SageMaker AI Training Job Example

The following includes a `Task` state that creates an Amazon SageMaker AI training
job.

```
{
   "SageMaker CreateTrainingJob":{
      "Type":"Task",
      "Resource":"arn:aws:states:::sagemaker:createTrainingJob.sync",
      "Arguments":{
         "TrainingJobName":"search-model",
         "ResourceConfig":{
            "InstanceCount":4,
            "InstanceType":"ml.c4.8xlarge",
            "VolumeSizeInGB":20
         },
         "HyperParameters":{
            "mode":"batch_skipgram",
            "epochs":"5",
            "min_count":"5",
            "sampling_threshold":"0.0001",
            "learning_rate":"0.025",
            "window_size":"5",
            "vector_dim":"300",
            "negative_samples":"5",
            "batch_size":"11"
         },
         "AlgorithmSpecification":{
            "TrainingImage":"...",
            "TrainingInputMode":"File"
         },
         "OutputDataConfig":{
            "S3OutputPath":"s3://amzn-s3-demo-destination-bucket1/doc-search/model"
         },
         "StoppingCondition":{
            "MaxRuntimeInSeconds":100000
         },
         "RoleArn":"arn:aws:iam::`account-id`:role/docsearch-stepfunction-iam-role",
         "InputDataConfig":[
            {
               "ChannelName":"train",
               "DataSource":{
                  "S3DataSource":{
                     "S3DataType":"S3Prefix",
                     "S3Uri":"s3://amzn-s3-demo-destination-bucket1/doc-search/interim-data/training-data/",
                     "S3DataDistributionType":"FullyReplicated"
                  }
               }
            }
         ]
      },
      "Retry":[
         {
            "ErrorEquals":[
               "SageMaker.AmazonSageMakerException"
            ],
            "IntervalSeconds":1,
            "MaxAttempts":100,
            "BackoffRate":1.1
         },
         {
            "ErrorEquals":[
               "SageMaker.ResourceLimitExceededException"
            ],
            "IntervalSeconds":60,
            "MaxAttempts":5000,
            "BackoffRate":1
         },
         {
            "ErrorEquals":[
               "States.Timeout"
            ],
            "IntervalSeconds":1,
            "MaxAttempts":5,
            "BackoffRate":1
         }
      ],
      "Catch":[
         {
            "ErrorEquals":[
               "States.ALL"
            ],
            "Next":"Sagemaker Training Job Error"
         }
      ],
      "Next":"Delete Interim Data Job"
   }
}



```

## SageMaker AI Labeling Job Example

The following includes a `Task` state that creates an Amazon SageMaker AI labeling
job.

```
{
  "StartAt": "SageMaker CreateLabelingJob",
  "TimeoutSeconds": 3600,
  "States": {
    "SageMaker CreateLabelingJob": {
      "Type": "Task",
      "Resource": "arn:aws:states:::sagemaker:createLabelingJob.sync",
      "Arguments": {
        "HumanTaskConfig": {
          "AnnotationConsolidationConfig": {
            "AnnotationConsolidationLambdaArn": "arn:aws:lambda:`region`:123456789012:function:ACS-TextMultiClass"
          },
          "NumberOfHumanWorkersPerDataObject": 1,
          "PreHumanTaskLambdaArn": "arn:aws:lambda:`region`:123456789012:function:PRE-TextMultiClass",
          "TaskDescription": "Classify the following text",
          "TaskKeywords": [
            "tc",
            "Labeling"
          ],
          "TaskTimeLimitInSeconds": 300,
          "TaskTitle": "Classify short bits of text",
          "UiConfig": {
            "UiTemplateS3Uri": "s3://amzn-s3-demo-bucket/TextClassification.template"
          },
          "WorkteamArn": "arn:aws:sagemaker:`region`:123456789012:workteam/private-crowd/ExampleTesting"
        },
        "InputConfig": {
          "DataAttributes": {
            "ContentClassifiers": [
              "FreeOfPersonallyIdentifiableInformation",
              "FreeOfAdultContent"
            ]
          },
          "DataSource": {
            "S3DataSource": {
              "ManifestS3Uri": "s3://amzn-s3-demo-bucket/manifest.json"
            }
          }
        },
        "LabelAttributeName": "Categories",
        "LabelCategoryConfigS3Uri": "s3://amzn-s3-demo-bucket/labelcategories.json",
        "LabelingJobName": "example-job-name",
        "OutputConfig": {
          "S3OutputPath": "s3://amzn-s3-demo-bucket/output"
        },
        "RoleArn": "arn:aws:iam::123456789012:role/service-role/AmazonSageMaker-ExecutionRole",
        "StoppingConditions": {
          "MaxHumanLabeledObjectCount": 10000,
          "MaxPercentageOfInputDatasetLabeled": 100
        }
      },
      "Next": "ValidateOutput"
    },
    "ValidateOutput": {
        "Type": "Choice",
        "Choices": [
            {
                "Next": "Success",
                "Condition": "{% $states.input.LabelingJobArn != '' %}"
            }
        ],
        "Default": "Fail"
        },
        "Success": {
            "Type": "Succeed"
        },
        "Fail": {
            "Type": "Fail",
            "Error": "InvalidOutput",
            "Cause": "Output is not what was expected. This could be due to a service outage or a misconfigured service integration."
        }
    }
}

```

## SageMaker AI Processing Job Example

The following includes a `Task` state that creates an Amazon SageMaker AI processing
job.

```
{
  "StartAt": "SageMaker CreateProcessingJob Sync",
  "TimeoutSeconds": 3600,
  "States": {
    "SageMaker CreateProcessingJob Sync": {
      "Type": "Task",
      "Resource": "arn:aws:states:::sagemaker:createProcessingJob.sync",
      "Arguments": {
        "AppSpecification": {
          "ImageUri": "737474898029.dkr.ecr.sa-east-1.amazonaws.com/sagemaker-scikit-learn:0.20.0-cpu-py3"
        },
        "ProcessingResources": {
          "ClusterConfig": {
            "InstanceCount": 1,
            "InstanceType": "ml.t3.medium",
            "VolumeSizeInGB": 10
          }
        },
        "RoleArn": "arn:aws:iam::`account-id`:role/SM-003-CreateProcessingJobAPIExecutionRole",
        "ProcessingJobName.$": "$.id"
      },
      "Next": "ValidateOutput"
    },
    "ValidateOutput": {
      "Type": "Choice",
      "Choices": [
        {
          "Not": {
            "Variable": "$.ProcessingJobArn",
            "StringEquals": ""
          },
          "Next": "Succeed"
        }
      ],
      "Default": "Fail"
    },
    "Succeed": {
      "Type": "Succeed"
    },
    "Fail": {
      "Type": "Fail",
      "Error": "InvalidConnectorOutput",
      "Cause": "Connector output is not what was expected. This could be due to a service outage or a misconfigured connector."
    }
  }
}

```

## IAM policies for calling Amazon SageMaker AI

The following example templates show how AWS Step Functions generates IAM policies based on the resources in your state machine definition. For more information, see [How Step Functions generates IAM policies for integrated
services](service-integration-iam-templates.md "service-integration-iam-templates.md") and [Discover service integration patterns in Step Functions](connect-to-resource.md "connect-to-resource.md").

###### Note

For these examples, `roleArn` refers to the
Amazon Resource Name (ARN) of the IAM role that SageMaker AI uses to access model artifacts and docker images
for deployment on ML compute instances, or for batch transform jobs. For more information, see
[Amazon SageMaker Roles](../../../sagemaker/latest/dg/sagemaker-roles.md "../../../sagemaker/latest/dg/sagemaker-roles.md").

### `CreateTrainingJob`

_Static resources_

Run a Job (.sync)

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "sagemaker:CreateTrainingJob",
 "sagemaker:DescribeTrainingJob",
 "sagemaker:StopTrainingJob"
 ],
 "Resource": [
 "arn:aws:sagemaker:`us-east-1`:`123456789012`:training-job/myJobName*"
 ]
 },
 {
 "Effect": "Allow",
 "Action": [
 "sagemaker:ListTags",
 "sagemaker:AddTags"
 ],
 "Resource": [
 "*"
 ]
 },
 {
 "Effect": "Allow",
 "Action": [
 "iam:PassRole"
 ],
 "Resource": [
 "arn:aws:iam::123456789012:role/`MyExampleRole`"
 ],
 "Condition": {
 "StringEquals": {
 "iam:PassedToService": "sagemaker.amazonaws.com"
 }
 }
 },
 {
 "Effect": "Allow",
 "Action": [
 "events:PutTargets",
 "events:PutRule",
 "events:DescribeRule"
 ],
 "Resource": [
 "arn:aws:events:`us-east-1`:`123456789012`:rule/StepFunctionsGetEventsForSageMakerTrainingJobsRule"
 ]
 }
 ]
}`

```

Request Response and Callback (.waitForTaskToken)

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "sagemaker:CreateTrainingJob"
 ],
 "Resource": [
 "arn:aws:sagemaker:`us-east-1`:`123456789012`:training-job/myJobName*"
 ]
 },
 {
 "Effect": "Allow",
 "Action": [
 "sagemaker:ListTags",
 "sagemaker:AddTags"
 ],
 "Resource": [
 "*"
 ]
 },
 {
 "Effect": "Allow",
 "Action": [
 "iam:PassRole"
 ],
 "Resource": [
 "arn:aws:iam::123456789012:role/`MyExampleRole`"
 ],
 "Condition": {
 "StringEquals": {
 "iam:PassedToService": "sagemaker.amazonaws.com"
 }
 }
 }
 ]
}`

```

_Dynamic resources_

.sync or .waitForTaskToken

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "sagemaker:CreateTrainingJob",
 "sagemaker:DescribeTrainingJob",
 "sagemaker:StopTrainingJob"
 ],
 "Resource": [
 "arn:aws:sagemaker:`us-east-1`:`123456789012`:training-job/*"
 ]
 },
 {
 "Effect": "Allow",
 "Action": [
 "sagemaker:ListTags",
 "sagemaker:AddTags"
 ],
 "Resource": [
 "*"
 ]
 },
 {
 "Effect": "Allow",
 "Action": [
 "iam:PassRole"
 ],
 "Resource": [
 "arn:aws:iam::123456789012:role/`MyExampleRole`"
 ],
 "Condition": {
 "StringEquals": {
 "iam:PassedToService": "sagemaker.amazonaws.com"
 }
 }
 },
 {
 "Effect": "Allow",
 "Action": [
 "events:PutTargets",
 "events:PutRule",
 "events:DescribeRule"
 ],
 "Resource": [
 "arn:aws:events:`us-east-1`:`123456789012`:rule/StepFunctionsGetEventsForSageMakerTrainingJobsRule"
 ]
 }
 ]
}`

```

Request Response and Callback (.waitForTaskToken)

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "sagemaker:CreateTrainingJob"
 ],
 "Resource": [
 "arn:aws:sagemaker:`us-east-1`:`123456789012`:training-job/*"
 ]
 },
 {
 "Effect": "Allow",
 "Action": [
 "sagemaker:ListTags",
 "sagemaker:AddTags"
 ],
 "Resource": [
 "*"
 ]
 },
 {
 "Effect": "Allow",
 "Action": [
 "iam:PassRole"
 ],
 "Resource": [
 "arn:aws:iam::123456789012:role/`MyExampleRole`"
 ],
 "Condition": {
 "StringEquals": {
 "iam:PassedToService": "sagemaker.amazonaws.com"
 }
 }
 }
 ]
}`

```

### `CreateTransformJob`

###### Note

AWS Step Functions will not automatically create a policy for `CreateTransformJob`
when you create a state machine that integrates with SageMaker AI. You must attach an inline policy
to the created role based on one of the following IAM examples.

_Static resources_

Run a Job (.sync)

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "sagemaker:CreateTransformJob",
 "sagemaker:DescribeTransformJob",
 "sagemaker:StopTransformJob"
 ],
 "Resource": [
 "arn:aws:sagemaker:`us-east-1`:`123456789012`:transform-job/myJobName*"
 ]
 },
 {
 "Effect": "Allow",
 "Action": [
 "sagemaker:ListTags",
 "sagemaker:AddTags"
 ],
 "Resource": [
 "*"
 ]
 },
 {
 "Effect": "Allow",
 "Action": [
 "iam:PassRole"
 ],
 "Resource": [
 "arn:aws:iam::123456789012:role/`MyExampleRole`"
 ],
 "Condition": {
 "StringEquals": {
 "iam:PassedToService": "sagemaker.amazonaws.com"
 }
 }
 },
 {
 "Effect": "Allow",
 "Action": [
 "events:PutTargets",
 "events:PutRule",
 "events:DescribeRule"
 ],
 "Resource": [
 "arn:aws:events:`us-east-1`:`123456789012`:rule/StepFunctionsGetEventsForSageMakerTransformJobsRule"
 ]
 }
 ]
}`

```

Request Response and Callback (.waitForTaskToken)

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "sagemaker:CreateTransformJob"
 ],
 "Resource": [
 "arn:aws:sagemaker:`us-east-1`:`123456789012`:transform-job/myJobName*"
 ]
 },
 {
 "Effect": "Allow",
 "Action": [
 "sagemaker:ListTags",
 "sagemaker:AddTags"
 ],
 "Resource": [
 "*"
 ]
 },
 {
 "Effect": "Allow",
 "Action": [
 "iam:PassRole"
 ],
 "Resource": [
 "arn:aws:iam::123456789012:role/`MyExampleRole`"
 ],
 "Condition": {
 "StringEquals": {
 "iam:PassedToService": "sagemaker.amazonaws.com"
 }
 }
 }
 ]
}`

```

_Dynamic resources_

Run a Job (.sync)

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "sagemaker:CreateTransformJob",
 "sagemaker:DescribeTransformJob",
 "sagemaker:StopTransformJob"
 ],
 "Resource": [
 "arn:aws:sagemaker:`us-east-1`:`123456789012`:transform-job/*"
 ]
 },
 {
 "Effect": "Allow",
 "Action": [
 "sagemaker:ListTags",
 "sagemaker:AddTags"
 ],
 "Resource": [
 "*"
 ]
 },
 {
 "Effect": "Allow",
 "Action": [
 "iam:PassRole"
 ],
 "Resource": [
 "arn:aws:iam::123456789012:role/`MyExampleRole`"
 ],
 "Condition": {
 "StringEquals": {
 "iam:PassedToService": "sagemaker.amazonaws.com"
 }
 }
 },
 {
 "Effect": "Allow",
 "Action": [
 "events:PutTargets",
 "events:PutRule",
 "events:DescribeRule"
 ],
 "Resource": [
 "arn:aws:events:`us-east-1`:`123456789012`:rule/StepFunctionsGetEventsForSageMakerTransformJobsRule"
 ]
 }
 ]
}`

```

Request Response and Callback (.waitForTaskToken)

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "sagemaker:CreateTransformJob"
 ],
 "Resource": [
 "arn:aws:sagemaker:`us-east-1`:`123456789012`:transform-job/*"
 ]
 },
 {
 "Effect": "Allow",
 "Action": [
 "sagemaker:ListTags",
 "sagemaker:AddTags"
 ],
 "Resource": [
 "*"
 ]
 },
 {
 "Effect": "Allow",
 "Action": [
 "iam:PassRole"
 ],
 "Resource": [
 "arn:aws:iam::123456789012:role/`MyExampleRole`"
 ],
 "Condition": {
 "StringEquals": {
 "iam:PassedToService": "sagemaker.amazonaws.com"
 }
 }
 }
 ]
}`

```
