

# Using the AWS AppConfig deployment events to Amazon SNS extension
<a name="working-with-appconfig-extensions-about-predefined-notification-sns"></a>

The `AWS AppConfig deployment events to Amazon SNS` extension is an AWS authored extension that helps you monitor and act on the AWS AppConfig configuration deployment workflow. The extension publishes messages to an Amazon SNS topic whenever a configuration is deployed. After you associate the extension to one of your AWS AppConfig applications, environments, or configuration profiles, AWS AppConfig publishes a message to the topic after every configuration deployment start, end, and rollback.

If you want more control over which action points send Amazon SNS notifications, you can create a custom extension and enter an Amazon SNS topic Amazon Resource Name (ARN) for the URI field. For information about creating an extension, see [Walkthrough: Creating custom AWS AppConfig extensions](working-with-appconfig-extensions-creating-custom.md).

## Using the extension
<a name="working-with-appconfig-extensions-about-predefined-notification-sns-using"></a>

This section describes how to use the `AWS AppConfig deployment events to Amazon SNS` extension.

**Step 1: Configure AWS AppConfig to publish messages to a topic**  
Add an access control policy to your Amazon SNS topic that gives AWS AppConfig (`appconfig.amazonaws.com`) permission to publish messages (`sns:Publish`). To make sure only your own account can send these messages, add an `aws:SourceAccount` condition to the policy and set it to your AWS account ID. This prevents someone in a different AWS account from using the extension to send messages to your topic. To scope access even more tightly, you can use an `aws:SourceArn` condition set to the ARN of the extension association instead. For more information, see [Example cases for Amazon SNS access control](https://docs.aws.amazon.com/sns/latest/dg/sns-access-policy-use-cases.html).

The following example policy lets AWS AppConfig publish to your topic only when the request comes from your own account. Replace `MySNSTopic` and the example account ID with your own values.

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "AllowAppConfigPublish",
            "Effect": "Allow",
            "Principal": {
                "Service": "appconfig.amazonaws.com"
            },
            "Action": "SNS:Publish",
            "Resource": "arn:aws:sns:us-east-1:111122223333:MySNSTopic",
            "Condition": {
                "StringEquals": {
                    "aws:SourceAccount": "111122223333"
                }
            }
        }
    ]
}
```

**Prevent cross-account access**  
You must include either the `aws:SourceAccount` or `aws:SourceArn` condition in your Amazon SNS topic policy to prevent cross-account access. Without these conditions, another AWS account could configure its `AWS AppConfig deployment events to Amazon SNS` extension to send deployment events to your topic. Always limit the policy to your own account.

**Step 2: Create an extension association**  
Attach the extension to one of your AWS AppConfig resources by creating an extension association. You create the association by using the AWS AppConfig console or the [CreateExtensionAssociation](https://docs.aws.amazon.com/appconfig/2019-10-09/APIReference/API_CreateExtensionAssociation.html) API action. When you create the association, you specify the ARN of an AWS AppConfig application, environment, or configuration profile. If you associate the extension to an application or an environment, a notification is sent for any configuration profile contained within the specified application or environment. When you create the association, you must enter a value for the `topicArn` parameter that contains the ARN of the Amazon SNS topic you want to use.

After you create the association, when a configuration for the specified AWS AppConfig resource is deployed, AWS AppConfig invokes the extension and sends notifications according to the action points specified in the extension.

**Note**  
This extension is invoked by the following action points:  
`ON_DEPLOYMENT_START`
`ON_DEPLOYMENT_COMPLETE`
`ON_DEPLOYMENT_ROLLED_BACK`
You can't customize the actions points for this extension. To invoke different action points, you can create your own extension. For more information, see [Walkthrough: Creating custom AWS AppConfig extensions](working-with-appconfig-extensions-creating-custom.md).

Use the following procedures to create an AWS AppConfig extension association by using either the AWS Systems Manager console or the AWS CLI.

**To create an extension association (console)**

1. Open the AWS Systems Manager console at [https://console.aws.amazon.com/systems-manager/appconfig/](https://console.aws.amazon.com/systems-manager/appconfig/).

1. In the navigation pane, choose **AWS AppConfig**.

1. On the **Extensions** tab, choose **Add to resource**.

1. In the **Extension resource details** section, for **Resource type**, choose an AWS AppConfig resource type. Depending on the resource you choose, AWS AppConfig prompts you to choose other resources.

1. Choose **Create association to resource**.

Here's a sample of the message sent to the Amazon SNS topic when the extension is invoked.

```
{
    "Type": "Notification",
    "MessageId": "ae9d702f-9a66-51b3-8586-2b17932a9f28",
    "TopicArn": "arn:aws:sns:us-east-1:111122223333:MySNSTopic",
    "Message": {
        "InvocationId": "7itcaxp",
        "Parameters": {
            "topicArn": "arn:aws:sns:us-east-1:111122223333:MySNSTopic"
        },
        "Application": {
            "Id": "1a2b3c4d",
            "Name": MyApp
        },
        "Environment": {
            "Id": "1a2b3c4d",
            "Name": MyEnv
        },
        "ConfigurationProfile": {
            "Id": "1a2b3c4d",
            "Name": "MyConfigProfile"
        },
        "Description": null,
        "DeploymentNumber": "3",
        "ConfigurationVersion": "1",
        "Type": "OnDeploymentComplete"
    },
    "Timestamp": "2022-06-30T20:26:52.067Z",
    "SignatureVersion": "1",
    "Signature": "<...>",
    "SigningCertURL": "<...>",
    "UnsubscribeURL": "<...>",
    "MessageAttributes": {
        "MessageType": {
            "Type": "String",
            "Value": "OnDeploymentStart"
        }
    }
}
```