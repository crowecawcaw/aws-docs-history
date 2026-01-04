# Subscribing to Amazon RDS event notification

The simplest way to create a subscription is with the RDS console. If you choose to create event notification
subscriptions using the CLI or API, you must create an Amazon Simple Notification Service topic and subscribe to that topic with the Amazon SNS
console or Amazon SNS API. You will also need to retain the Amazon Resource Name (ARN) of the topic because it is used
when submitting CLI commands or API operations. For information on creating an SNS topic and subscribing to it,
see [Getting started with Amazon SNS](../../../sns/latest/dg/GettingStarted.md "../../../sns/latest/dg/GettingStarted.md") in the _Amazon Simple Notification Service
Developer Guide_.

You can specify the type of source you want to be notified of and the Amazon RDS source that triggers the event:

**Source type**

The type of source. For example, **Source type** might be **Instances**. You must choose a
source type.

**`Resources` to include**

The Amazon RDS resources that are generating the events. For example, you might choose **Select specific instances**
and then **myDBInstance1**.

The following table explains the result when you specify or don't specify **`Resources` to
include**.

| Resources to include | Description                                                                                        | Example                                                                                                                                                 |
| -------------------- | -------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Specified            | RDS notifies you about all events for the specified resource only.                                 | If your **Source type\*<br>• is **Instances\*<br>• and your resource is<br>**myDBInstance1**, RDS notifies you about all events for myDBInstance1 only. |
| Not specified        | RDS notifies you about the events for the specified source type for all your Amazon RDS resources. | If your **Source type\*<br>• is **Instances\*\*, RDS notifies you about all instance-related<br>events in your account.                                 |

An Amazon SNS topic subscriber receives every message published to the topic by default.
To receive only a subset of the messages, the subscriber must assign a filter policy to
the topic subscription. For more information about SNS message filtering, see
[Amazon SNS message filtering](../../../sns/latest/dg/sns-message-filtering.md "../../../sns/latest/dg/sns-message-filtering.md") in the
_Amazon Simple Notification Service Developer Guide_

###### To subscribe to RDS event notification

1.  Sign in to the AWS Management Console and open the Amazon RDS console at
    [https://console.aws.amazon.com/rds/](https://console.aws.amazon.com/rds/ "https://console.aws.amazon.com/rds/").
2.  In navigation pane, choose **Event subscriptions**.
3.  In the **Event subscriptions** pane, choose **Create event
    subscription**.
4.  Enter your subscription details as follows:

        1. For **Name**, enter a name for the event notification
         subscription.
        2. For **Send notifications to**, do one of the following:




        	* Choose **New email topic**. Enter a name
        	 for your email topic and a list of recipients. We recommend
        	 that you configure the events subscriptions to the same
        	 email address as your primary account contact. The
        	 recommendations, service events, and personal health
        	 messages are sent using different channels. The
        	 subscriptions to the same email address ensures that all the
        	 messages are consolidated in one location.
        	* Choose **Amazon Resource Name (ARN)**. Then choose existing Amazon SNS ARN for an Amazon SNS
        	 topic.


        	If you want to use a topic that has been enabled for server-side encryption (SSE), grant Amazon RDS the necessary
        	 permissions to access the AWS KMS key. For more information, see  [Enable compatibility between
        	 event sources from AWS services and encrypted topics](../../../sns/latest/dg/sns-key-management.md#compatibility-with-aws-services "../../../sns/latest/dg/sns-key-management.md#compatibility-with-aws-services") in the
        	 *Amazon Simple Notification Service Developer Guide*.
        3. For **Source type**, choose a source type. For example, choose **Instances** or **Parameter groups**.
        4. Choose the event categories and resources that you want to receive event notifications for.


        The following example configures event notifications for the DB instance named `testinst`.



        ![Enter source type](images/event-source.png)
        5. Choose **Create**.

    The Amazon RDS console indicates that the subscription is being created.

![List DB event notification subscriptions](images/EventNotification-Create2.png)
To subscribe to RDS event notification, use the AWS CLI [`create-event-subscription`](../../../cli/latest/reference/rds/create-event-subscription.md "../../../cli/latest/reference/rds/create-event-subscription.md")
command. Include the following required parameters:

- `--subscription-name`
- `--sns-topic-arn`

###### Example

For Linux, macOS, or Unix:

```
aws rds create-event-subscription \
    --subscription-name `myeventsubscription` \
    --sns-topic-arn `arn:aws:sns:us-east-1:123456789012:myawsuser-RDS` \
    `--enabled`
```

For Windows:

```
aws rds create-event-subscription ^
    --subscription-name `myeventsubscription` ^
    --sns-topic-arn `arn:aws:sns:us-east-1:123456789012:myawsuser-RDS` ^
    `--enabled`
```

To subscribe to Amazon RDS event notification, call the Amazon RDS API function [`CreateEventSubscription`](../APIReference/API_CreateEventSubscription.md "../APIReference/API_CreateEventSubscription.md"). Include the following required parameters:

- `SubscriptionName`
- `SnsTopicArn`
