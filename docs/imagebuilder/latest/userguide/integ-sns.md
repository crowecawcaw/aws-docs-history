

# Amazon SNS integration in Image Builder
<a name="integ-sns"></a>

Amazon Simple Notification Service (Amazon SNS) is a managed service that provides asynchronous message delivery from publishers to subscribers (also known as producers and consumers).

**Note**  
You can also receive `AVAILABLE` and `FAILED` state changes through the EventBridge `EC2 Image Builder Image State Change` event. The native Amazon SNS notification that's described here delivers detailed image information, whereas the event `detail` contains only the previous and new image state. For more information, see [Amazon EventBridge integration in Image Builder](integ-eventbridge.md).

You can specify an SNS topic in your infrastructure configuration. When you create an image or run a pipeline, Image Builder can publish detailed messages about your image status to this topic. When the image status reaches one of the following states, Image Builder publishes a message:
+ `AVAILABLE`
+ `FAILED`

Image Builder publishes an image status notification only for the `AVAILABLE` and `FAILED` states. Other states, including the intermediate build states and the `CANCELLED` terminal state, don't generate a status notification. To track those states, use an EventBridge rule for the `EC2 Image Builder Image State Change` event. For more information, see [EC2 Image Builder Image State Change](integ-eventbridge.md#eb-event-state-change).

**Note**  
Image Builder sends the image status notification on a best-effort basis. If Image Builder can't publish to your topic, the image build still completes and reaches its final state. A missing notification doesn't indicate a failed build. Image Builder can also drop the `FAILED` notification, so don't treat the notification as the source of truth for image status. To confirm the state of an image, call **GetImage**. Image Builder doesn't add a failure to publish the image status notification to your image build log.

**Note**  
When a `CreateInfrastructureConfiguration` or `UpdateInfrastructureConfiguration` request includes an `snsTopicArn` value, Image Builder validates the topic by publishing a test message with your credentials. If Amazon SNS rejects the test message, the request fails with an `InvalidParameterValueException` error for the `snsTopicArn` parameter, and the error message comes from Amazon SNS. If Amazon SNS returns a server error instead, the request fails with a `ServiceException` error.  
The test message body is a JSON object with a single `name` field, whose value is `EC2 Image Builder: {{operation}} - Validating caller SNS Topic publish permissions.`, where {{operation}} is `CreateInfrastructureConfiguration` or `UpdateInfrastructureConfiguration`. The test message also has a `String` message attribute named `EC2ImageBuilder`.

**Note**  
The topic name in `snsTopicArn` can contain only letters, numbers, hyphens, and underscores.

Image Builder validates the topic by calling Amazon SNS in the Region of the `CreateInfrastructureConfiguration` or `UpdateInfrastructureConfiguration` request. Image Builder publishes the status notification from the Region where the image build runs.

The [EC2ImageBuilderExecutionPolicy](security-iam-awsmanpol.md#sec-iam-manpol-EC2ImageBuilderExecutionPolicy) AWS managed policy allows `sns:Publish` only for topics in the same account as the role.

For an example SNS message from Image Builder, see [SNS message format](#integ-sns-message). If you want to create a new SNS topic, see [Getting started with Amazon SNS](https://docs.aws.amazon.com/sns/latest/dg/sns-getting-started.html) in the *Amazon Simple Notification Service Developer Guide*.

## Encrypted SNS Topics
<a name="integ-sns-encrypted"></a>

If your SNS topic is encrypted, you must grant permission in the AWS KMS key policy to perform the following actions. Grant this permission to the role that Image Builder uses to publish notifications. That role is the Image Builder service-linked role `AWSServiceRoleForImageBuilder`, or the workflow execution role that you specified for the image or image pipeline.
+ `kms:Decrypt`
+ `kms:GenerateDataKey`
+ `kms:GenerateDataKeyWithoutPlaintext`

**Note**  
If your SNS topic is encrypted, the key that encrypts this topic must reside in the account where the Image Builder service runs. Image Builder can't send notifications to SNS topics that are encrypted with keys from other accounts.

**Example KMS key policy addition**  
The following example shows the additional section that you add to the KMS key policy. Use the Amazon Resource Name (ARN) for the IAM service-linked role that Image Builder created under your account when you first created an Image Builder image. To learn more about the Image Builder service-linked role, see [Use IAM service-linked roles for Image Builder](image-builder-service-linked-role.md).

```
{
  "Statement": [{
    "Effect": "Allow",
    "Principal": {
      "AWS": "arn:aws:iam::{{123456789012}}:role/aws-service-role/imagebuilder.amazonaws.com/AWSServiceRoleForImageBuilder"
    },
    "Action": [
      "kms:Decrypt",
      "kms:GenerateDataKey",
      "kms:GenerateDataKeyWithoutPlaintext"
    ],
    "Resource": "*"
  }]
}
```

**Note**  
Image Builder publishes the status notification with the role that it uses to run the workflows for the image build, not with the instance profile in your infrastructure configuration. By default, that role is the service-linked role. If you specify a workflow execution role for the image or image pipeline, Image Builder uses that role instead. You set this role in the `executionRole` parameter of **CreateImage**, **CreateImagePipeline**, **UpdateImagePipeline**, or **ImportDiskImage**. **UpdateImagePipeline** doesn't support selective updates, so include `executionRole` in every update request for a pipeline that uses one. Otherwise, Image Builder runs later pipeline builds with the service-linked role.  
Grant the same KMS key permissions to the role that you specify.

You can use one of the following methods to get the ARN.

------
#### [ Console ]

To get the ARN for the service-linked role that Image Builder created under your account from the AWS Management Console, follow these steps:

1. Open the IAM console at [https://console.aws.amazon.com/iam/](https://console.aws.amazon.com/iam/).

1. In the left navigation pane, choose **Roles**.

1. Search for `ImageBuilder`, and choose the following **Role name** from the results: `AWSServiceRoleForImageBuilder`. This displays the role detail page.

1. To copy the ARN to your clipboard, choose the icon next to the ARN name.

------
#### [ AWS CLI ]

To get the ARN for the service-linked role that Image Builder created under your account from the AWS CLI, use the IAM [get-role](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/get-role.html) command, as follows.

```
aws iam get-role --role-name AWSServiceRoleForImageBuilder
```

**Partial sample output:**

```
{
    "Role": {
        "Path": "/aws-service-role/imagebuilder.amazonaws.com/",
        "RoleName": "AWSServiceRoleForImageBuilder",
        ...
        "Arn": "arn:aws:iam::{{123456789012}}:role/aws-service-role/imagebuilder.amazonaws.com/AWSServiceRoleForImageBuilder",
        ...
}
```

------
#### [ PowerShell ]

To get the ARN for the service-linked role that Image Builder created under your account with PowerShell, use the IAM [Get-IAMRole](https://docs.aws.amazon.com/powershell/latest/reference/items/Get-IAMRole.html) cmdlet:

```
Get-IAMRole -RoleName AWSServiceRoleForImageBuilder
```

------

## SNS message format
<a name="integ-sns-message"></a>

After Image Builder publishes a message to your Amazon SNS topic, other services that subscribe to the topic can act on the message contents. For example, a success message might initiate a task to update an AWS Systems Manager parameter store, or to launch an external compliance testing workflow for the output AMI.

**Note**  
Image Builder sends the image status notification data in the message body and doesn't set any Amazon SNS message attributes on that notification. To filter image status notifications with an Amazon SNS subscription filter policy, set the `FilterPolicyScope` subscription attribute to `MessageBody`. For more information, see [Amazon SNS subscription filter policy scope](https://docs.aws.amazon.com/sns/latest/dg/sns-message-filtering-scope.html) in the *Amazon Simple Notification Service Developer Guide*.  
Image Builder publishes other messages to the topics that you configure: the test message that validates the topic when you create or update an infrastructure configuration, and, if you use the `WaitForAction` workflow step, that step's waiting notification. Those messages have a different body structure.

The following example shows the JSON payload for a typical message that Image Builder publishes when a pipeline build runs to completion, and creates a Linux image.

Image Builder uses the same message format for every image, but not every field appears in every message. Which fields appear depends on the image type, on the configurations that you attached to the image or pipeline, and on how far the build progressed before it reached its final state. For example, a message for a Windows image can include an `inventoryConfiguration` block, and a message for a failed build can omit `osVersion` and contain an empty output resource list. Treat every block as optional.

The `type` field tells you whether the message describes an AMI (`AMI`) or a container image (`DOCKER`). Branch on `type` before you read any of the blocks that depend on it. A message for a container image includes a `containerRecipe` block instead of `imageRecipe`, and `outputResources.containers` instead of `outputResources.amis`.

```
{
  "versionlessArn": "arn:aws:imagebuilder:us-west-1:123456789012:image/example-linux-image",
  "semver": 1237940039285380274899124227,
  "arn": "arn:aws:imagebuilder:us-west-1:123456789012:image/example-linux-image/1.0.0/3",
  "name": "example-linux-image",
  "version": "1.0.0",
  "type": "AMI",
  "buildVersion": 3,
  "state": {
    "status": "AVAILABLE"
  },
  "platform": "Linux",
  "imageRecipe": {
    "arn": "arn:aws:imagebuilder:us-west-1:123456789012:image-recipe/example-linux-image/1.0.0",
    "name": "amjule-barebones-linux",
    "version": "1.0.0",
    "components": [
      {
        "componentArn": "arn:aws:imagebuilder:us-west-1:123456789012:component/update-linux/1.0.2/1"
      }
    ],
    "platform": "Linux",
    "parentImage": "arn:aws:imagebuilder:us-west-1:987654321098:image/amazon-linux-2-x86/2022.6.14/1",
    "blockDeviceMappings": [
      {
        "deviceName": "/dev/xvda",
        "ebs": {
          "encrypted": false,
          "deleteOnTermination": true,
          "volumeSize": 8,
          "volumeType": "gp2"
        }
      }
    ],
    "dateCreated": "Feb 24, 2021 12:31:54 AM",
    "tags": {
      "internalId": "1a234567-8901-2345-bcd6-ef7890123456",
      "resourceArn": "arn:aws:imagebuilder:us-west-1:123456789012:image-recipe/example-linux-image/1.0.0"
    },
    "workingDirectory": "/tmp",
    "accountId": "462045008730"
  },
  "sourcePipelineArn": "arn:aws:imagebuilder:us-west-1:123456789012:image-pipeline/example-linux-pipeline",
  "infrastructureConfiguration": {
    "arn": "arn:aws:imagebuilder:us-west-1:123456789012:infrastructure-configuration/example-linux-infra-config-uswest1",
    "name": "example-linux-infra-config-uswest1",
    "instanceProfileName": "example-linux-ib-baseline-admin",
    "tags": {
      "internalId": "234abc56-d789-0123-a4e5-6b789d012c34",
      "resourceArn": "arn:aws:imagebuilder:us-west-1:123456789012:infrastructure-configuration/example-linux-infra-config-uswest1"
    },
    "logging": {
      "s3Logs": {
        "s3BucketName": "amzn-s3-demo-bucket"
      }
    },
    "keyPair": "example-linux-key-pair-uswest1",
    "terminateInstanceOnFailure": true,
    "snsTopicArn": "arn:aws:sns:us-west-1:123456789012:example-linux-ibnotices-uswest1",
    "dateCreated": "Feb 24, 2021 12:31:55 AM",
    "accountId": "123456789012"
  },
  "imageTestsConfigurationDocument": {
    "imageTestsEnabled": true,
    "timeoutMinutes": 720
  },
  "distributionConfiguration": {
    "arn": "arn:aws:imagebuilder:us-west-1:123456789012:distribution-configuration/example-linux-distribution",
    "name": "example-linux-distribution",
    "dateCreated": "Feb 24, 2021 12:31:56 AM",
    "distributions": [
      {
        "region": "us-west-1",
        "amiDistributionConfiguration": {}
      }
    ],
    "tags": {
      "internalId": "345abc67-8910-12d3-4ef5-67a8b90c12de",
      "resourceArn": "arn:aws:imagebuilder:us-west-1:123456789012:distribution-configuration/example-linux-distribution"
    },
    "accountId": "123456789012"
  },
  "dateCreated": "Jul 28, 2022 1:13:45 AM",
  "outputResources": {
    "amis": [
      {
        "region": "us-west-1",
        "image": "ami-01a23bc4def5a6789",
        "name": "example-linux-image 2022-07-28T01-14-17.416Z",
        "accountId": "123456789012"
      }
    ]
  },
  "buildExecutionId": "ab0cd12e-34fa-5678-b901-2c3456d789e0",
  "testExecutionId": "6a7b8901-cdef-234a-56b7-8cd89ef01234",
  "distributionJobId": "1f234567-8abc-9d0e-1234-fa56b7c890de",
  "integrationJobId": "432109b8-afe7-6dc5-4321-0ba98f7654e3",
  "accountId": "123456789012",
  "osVersion": "Amazon Linux 2",
  "enhancedImageMetadataEnabled": true,
  "buildType": "USER_INITIATED",
  "tags": {
    "internalId": "901e234f-a567-89bc-0123-d4e567f89a01",
    "resourceArn": "arn:aws:imagebuilder:us-west-1:123456789012:image/example-linux-image/1.0.0/3"
  }
}
```

The following example shows the JSON payload for a typical message that Image Builder publishes for a pipeline build failure for a Linux image.

```
{
  "versionlessArn": "arn:aws:imagebuilder:us-west-2:123456789012:image/my-example-image",
  "semver": 1237940039285380274899124231,
  "arn": "arn:aws:imagebuilder:us-west-2:123456789012:image/my-example-image/1.0.0/7",
  "name": "My Example Image",
  "version": "1.0.0",
  "type": "AMI",
  "buildVersion": 7,
  "state": {
    "status": "FAILED",
    "reason": "Image Failure reason."
  },
  "platform": "Linux",
  "imageRecipe": {
    "arn": "arn:aws:imagebuilder:us-west-2:123456789012:image-recipe/my-example-image/1.0.0",
    "name": "My Example Image",
    "version": "1.0.0",
    "description": "Testing Image recipe",
    "components": [
      {
        "componentArn": "arn:aws:imagebuilder:us-west-2:123456789012:component/my-example-image-component/1.0.0/1"
      }
    ],
    "platform": "Linux",
    "parentImage": "ami-0cd12345db678d90f",
    "dateCreated": "Jun 21, 2022 11:36:14 PM",
    "tags": {
      "internalId": "1a234567-8901-2345-bcd6-ef7890123456",
      "resourceArn": "arn:aws:imagebuilder:us-west-2:123456789012:image-recipe/my-example-image/1.0.0"
    },
    "accountId": "123456789012"
  },
  "sourcePipelineArn": "arn:aws:imagebuilder:us-west-2:123456789012:image-pipeline/my-example-image-pipeline",
  "infrastructureConfiguration": {
    "arn": "arn:aws:imagebuilder:us-west-2:123456789012:infrastructure-configuration/my-example-infra-config",
    "name": "SNS topic Infra config",
    "description": "An example that will retain instances of failed builds",
    "instanceTypes": [
      "t2.micro"
    ],
    "instanceProfileName": "EC2InstanceProfileForImageBuilder",
    "tags": {
      "internalId": "234abc56-d789-0123-a4e5-6b789d012c34",
      "resourceArn": "arn:aws:imagebuilder:us-west-2:123456789012:infrastructure-configuration/my-example-infra-config"
    },
    "terminateInstanceOnFailure": true,
    "snsTopicArn": "arn:aws:sns:us-west-2:123456789012:example-pipeline-notification-topic",
    "dateCreated": "Jul 5, 2022 7:31:53 PM",
    "accountId": "123456789012"
  },
  "imageTestsConfigurationDocument": {
    "imageTestsEnabled": true,
    "timeoutMinutes": 720
  },
  "distributionConfiguration": {
    "arn": "arn:aws:imagebuilder:us-west-2:123456789012:distribution-configuration/my-example-distribution-config",
    "name": "New distribution config",
    "dateCreated": "Dec 3, 2021 9:24:22 PM",
    "distributions": [
      {
        "region": "us-west-2",
        "amiDistributionConfiguration": {},
        "fastLaunchConfigurations": [
          {
            "enabled": true,
            "snapshotConfiguration": {
              "targetResourceCount": 2
            },
            "maxParallelLaunches": 2,
            "launchTemplate": {
              "launchTemplateId": "lt-01234567890"
            },
            "accountId": "123456789012"
          }
        ]
      }
    ],
    "tags": {
      "internalId": "1fecd23a-4f56-7f89-01e2-345678abbe90",
      "resourceArn": "arn:aws:imagebuilder:us-west-2:123456789012:distribution-configuration/my-example-distribution-config"
    },
    "accountId": "123456789012"
  },
  "dateCreated": "Jul 5, 2022 7:40:15 PM",
  "outputResources": {
    "amis": []
  },
  "buildExecutionId": "cd12ef34-56ab-7890-c123-4e5678f90ab1",
  "testExecutionId": "7b8c9012-def3-456b-67c8-9de01fa12345",
  "distributionJobId": "2f345678-9bcd-0e1f-2345-ab67c8d901ef",
  "integrationJobId": "543210c9-bfa8-7ed6-5432-1cb09f8765f4",
  "accountId": "123456789012",
  "enhancedImageMetadataEnabled": true,
  "buildType": "SCHEDULED",
  "tags": {
    "internalId": "456c78b9-0e12-3f45-afb6-7e89b0f1a23b",
    "resourceArn": "arn:aws:imagebuilder:us-west-2:123456789012:image/my-example-image/1.0.0/7"
  }
}
```

**Note**  
Image Builder includes the `buildExecutionId`, `testExecutionId`, `distributionJobId`, and `integrationJobId` fields only for backward compatibility, and sets each one to a randomly generated value in every message. No Image Builder API returns these four fields for an image. Image Builder also replaces every `internalId` value with a randomly generated value, so the value in a message changes from message to message and doesn't match the value that Image Builder stores for the resource. Don't use any of these values as stable or queryable identifiers.  
For backward compatibility, Image Builder also reports every `dateCreated` and `dateUpdated` value in the message in the format `Mon D, YYYY H:MM:SS AM`, instead of the ISO 8601 format that **GetImage** returns. The message carries no time zone offset for these values. Image Builder also reports the image's `imageTestsConfiguration` in a field named `imageTestsConfigurationDocument`. Parse the message body as its own schema, and call **GetImage** when you need the current state of the image.