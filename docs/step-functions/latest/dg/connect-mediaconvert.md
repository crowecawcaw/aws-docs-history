# Create an AWS Elemental MediaConvert job with Step Functions

Learn how to use Step Functions to create an AWS Elemental MediaConvert job using the [`CreateJob`](../../../mediaconvert/latest/apireference/jobs.md#jobspost "../../../mediaconvert/latest/apireference/jobs.md#jobspost") API.

###### Experiment with Step Functions and MediaConvert

Learn how to use the MediaConvert optimized integration in a workflow that detects and removes SMTPE color bars of unknown length from the beginning of a video clip. Read the blog post from Apr, 12, 2024: [_Low code workflows with AWS Elemental MediaConvert_](https://aws.amazon.com/blogs/media/low-code-workflows-with-aws-elemental-mediaconvert/ "https://aws.amazon.com/blogs/media/low-code-workflows-with-aws-elemental-mediaconvert/")

To learn about integrating with AWS services in Step Functions, see [Integrating services](integrate-services.md "integrate-services.md") and [Passing parameters to a service API in Step Functions](connect-parameters.md "connect-parameters.md").

###### Key features of Optimized MediaConvert integration

- The [Run a Job (.sync)](connect-to-resource.md#connect-sync "connect-to-resource.md#connect-sync") and [Request Response](connect-to-resource.md#connect-default "connect-to-resource.md#connect-default") integration patterns are supported.
- Step Functions will add the following custom tag to MediaConvert jobs: `ManagedByService: AWSStepFunctions`
- There is no specific optimization for [Wait for a Callback with Task Token](connect-to-resource.md#connect-wait-token "connect-to-resource.md#connect-wait-token") integration patterns.
  The following includes a `Task` state that submits a MediaConvert job and waits
  for it to complete.

```
{
    "StartAt": "MediaConvert_CreateJob",
    "States": {
        "MediaConvert_CreateJob": {
        "Type": "Task",
        "Resource": "arn:aws:states:::mediaconvert:createJob.sync",
        "Arguments": {
            "Role": "arn:aws:iam::111122223333:role/Admin",
            "Settings": {
            "OutputGroups": [
                {
                "Outputs": [
                    {
                    "ContainerSettings": {
                        "Container": "MP4"
                    },
                    "VideoDescription": {
                        "CodecSettings": {
                        "Codec": "H_264",
                        "H264Settings": {
                            "MaxBitrate": 1000,
                            "RateControlMode": "QVBR",
                            "SceneChangeDetect": "TRANSITION_DETECTION"
                        }
                        }
                    },
                    "AudioDescriptions": [
                        {
                        "CodecSettings": {
                            "Codec": "AAC",
                            "AacSettings": {
                            "Bitrate": 96000,
                            "CodingMode": "CODING_MODE_2_0",
                            "SampleRate": 48000
                            }
                        }
                        }
                    ]
                    }
                ],
                "OutputGroupSettings": {
                    "Type": "FILE_GROUP_SETTINGS",
                    "FileGroupSettings": {
                    "Destination": "s3://amzn-s3-demo-destination-bucket/"
                    }
                }
                }
            ],
            "Inputs": [
                {
                "AudioSelectors": {
                    "Audio Selector 1": {
                    "DefaultSelection": "DEFAULT"
                    }
                },
                "FileInput": "s3://amzn-s3-demo-bucket/DOC-EXAMPLE-SOURCE_FILE"
                }
            ]
            }
        },
        "End": true
        }
    }
}
```

###### Parameters in Step Functions are expressed in PascalCase

Even if the native service API is in camelCase, for example the API action `startSyncExecution`, you specify parameters in PascalCase, such as: `StateMachineArn`.

## Optimized MediaConvert APIs

- [`CreateJob`](../../../mediaconvert/latest/apireference/jobs.md#jobspost "../../../mediaconvert/latest/apireference/jobs.md#jobspost")
  - [Request syntax](../../../mediaconvert/latest/apireference/jobs.md#jobs-request-body-post-example "../../../mediaconvert/latest/apireference/jobs.md#jobs-request-body-post-example")
  - Supported parameters:
    - [`Role`](../../../mediaconvert/latest/apireference/jobs.md#jobs-prop-createjobrequest-role "../../../mediaconvert/latest/apireference/jobs.md#jobs-prop-createjobrequest-role") (Required)
    - [`Settings`](../../../mediaconvert/latest/apireference/jobs.md#jobs-prop-createjobrequest-settings "../../../mediaconvert/latest/apireference/jobs.md#jobs-prop-createjobrequest-settings") (Required)
    - [`CreateJobRequest`](../../../mediaconvert/latest/apireference/jobs.md#jobs-model-createjobrequest "../../../mediaconvert/latest/apireference/jobs.md#jobs-model-createjobrequest") (Optional)

  - [Response syntax](../../../mediaconvert/latest/apireference/jobs.md#jobs-response-examples "../../../mediaconvert/latest/apireference/jobs.md#jobs-response-examples") – see **CreateJobResponse schema**

## IAM policies for calling AWS Elemental MediaConvert

The following example templates show how AWS Step Functions generates IAM policies based on the resources in your state machine definition. For more information, see [How Step Functions generates IAM policies for integrated
services](service-integration-iam-templates.md "service-integration-iam-templates.md") and [Discover service integration patterns in Step Functions](connect-to-resource.md "connect-to-resource.md").

The IAM policy for `GetJob` and `CancelJob` actions are scoped to only permit access to jobs with the `ManagedByService: AWSStepFunctions` tag.

###### Tag-based policy

Modifying the autogenerated `ManagedByService: AWSStepFunctions` tag will cause state machine executions to fail.

Run a Job (.sync)

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "MediaConvertCreateJob",
 "Effect": "Allow",
 "Action": [
 "mediaconvert:CreateJob"
 ],
 "Resource": [
 "arn:aws:mediaconvert:`us-east-1`:`123456789012`:queues/*",
 "arn:aws:mediaconvert:`us-east-1`:`123456789012`:jobTemplates/*",
 "arn:aws:mediaconvert:`us-east-1`:`123456789012`:presets/*"
 ]
 },
 {
 "Sid": "MediaConvertManageJob",
 "Effect": "Allow",
 "Action": [
 "mediaconvert:GetJob",
 "mediaconvert:CancelJob"
 ],
 "Resource": "arn:aws:mediaconvert:`us-east-1`:`123456789012`:jobs/*",
 "Condition": {
 "StringEquals": {
 "aws:ResourceTag/ManagedByService": "AWSStepFunctions"
 }
 }
 },
 {
 "Sid": "IamPassRole",
 "Effect": "Allow",
 "Action": [
 "iam:PassRole"
 ],
 "Resource": [
 "arn:aws:iam::`123456789012`:role/myRoleName"
 ],
 "Condition": {
 "StringEquals": {
 "iam:PassedToService": [
 "mediaconvert.amazonaws.com"
 ]
 }
 }
 },
 {
 "Sid": "EventBridgeManageRule",
 "Effect": "Allow",
 "Action": [
 "events:PutTargets",
 "events:PutRule",
 "events:DescribeRule"
 ],
 "Resource": [
 "arn:aws:events:`us-east-1`:`123456789012`:rule/StepFunctionsGetEventsForMediaConvertJobRule"
 ]
 }
 ]
}`

```

Request Response

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "MediaConvertCreateJob",
 "Effect": "Allow",
 "Action": [
 "mediaconvert:CreateJob"
 ],
 "Resource": [
 "arn:aws:mediaconvert:`us-east-1`:`123456789012`:queues/*",
 "arn:aws:mediaconvert:`us-east-1`:`123456789012`:jobTemplates/*",
 "arn:aws:mediaconvert:`us-east-1`:`123456789012`:presets/*"
 ]
 },
 {
 "Sid": "IamPassRole",
 "Effect": "Allow",
 "Action": [
 "iam:PassRole"
 ],
 "Resource": [
 "arn:aws:iam::`123456789012`:role/myRoleName"
 ],
 "Condition": {
 "StringEquals": {
 "iam:PassedToService": [
 "mediaconvert.amazonaws.com"
 ]
 }
 }
 }
 ]
}`

```
