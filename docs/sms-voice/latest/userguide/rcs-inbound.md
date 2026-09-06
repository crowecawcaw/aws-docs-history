

# Receiving inbound RCS messages
<a name="rcs-inbound"></a>

AWS End User Messaging supports two-way RCS messaging, allowing you to receive text messages from your customers. Inbound RCS messages follow the same pattern as SMS two-way messaging: incoming messages are delivered to an Amazon SNS topic that you configure, and you process them using Lambda functions or other SNS subscribers.

**Important**  
To consume inbound RCS messages, you must set up a two-way messaging SNS topic on your AWS RCS Agent. Two-way messaging is disabled by default when you create an agent. After you enable it and configure an SNS topic, inbound messages are delivered to that topic. Customers are charged for all inbound RCS messages at standard rates.

This section explains how two-way RCS messaging works, how to enable it for your AWS RCS Agent, the inbound message payload format, and how to manage keywords. For information about managing AWS RCS Agents, see [Managing RCS agents](rcs-agents.md). For information about sending RCS messages, see [Sending RCS messages](rcs-send-message.md).

**Topics**
+ [How two-way RCS messaging works](#rcs-inbound-how-it-works)
+ [Configuring your two-way messaging destination](#rcs-inbound-enable)
+ [Inbound message payload format](#rcs-inbound-payload)
+ [Supported message types](#rcs-inbound-text-only)
+ [Keyword management for RCS](#rcs-inbound-keywords)
+ [Processing inbound messages with Lambda](#rcs-inbound-lambda)
+ [Best practices for inbound RCS messaging](#rcs-inbound-best-practices)

## How two-way RCS messaging works
<a name="rcs-inbound-how-it-works"></a>

When a customer sends a text message to your AWS RCS Agent, AWS End User Messaging receives the message and publishes it to an Amazon SNS topic that you designate. From there, you can process the message using any SNS subscriber, such as a Lambda function, an Amazon SQS queue, or an HTTP/HTTPS endpoint.

The two-way RCS messaging flow works as follows:

1. A customer sends a text message to your AWS RCS Agent from their RCS-capable device.

1. AWS End User Messaging receives the inbound message and evaluates it against your configured keywords. If the message matches a keyword, the service sends the configured auto-response (if any).

1. AWS End User Messaging publishes the message payload as a JSON object to the Amazon SNS topic that you configured for two-way messaging on the AWS RCS Agent.

1. Your SNS subscribers (for example, a Lambda function) receive the message payload and process it according to your application logic.

In addition to text messages, customers can send media (images, videos, audio files, and documents) to your AWS RCS Agent. When you configure inbound media storage, AWS End User Messaging saves the media to your Amazon S3 bucket and publishes a notification to your SNS topic with the file location and metadata. For more information, see [Receiving inbound RCS media](rcs-inbound-media.md).

## Configuring your two-way messaging destination
<a name="rcs-inbound-enable"></a>

To receive and process inbound RCS messages in your application, you must enable two-way messaging and configure a destination on your AWS RCS Agent. Two-way messaging is disabled by default. When you enable it, you specify an Amazon SNS topic where AWS End User Messaging delivers inbound messages. You can configure the destination using the AWS End User Messaging console or the API.

------
#### [ Console ]

**To configure your two-way messaging destination using the console**

1. Open the AWS End User Messaging console.

1. In the navigation pane, choose **RCS agents**.

1. Choose the AWS RCS Agent that you want to configure.

1. Choose the **Two-way messaging** tab.

1. Choose **Edit settings**.

1. Toggle **Enable two-way messaging** to on.

1. For **SNS topic**, choose an existing Amazon SNS topic or create a new one. This is the topic where inbound messages are published.

1. Choose **Save**.

------
#### [ AWS CLI ]

To configure your two-way messaging destination using the API, call the `UpdateRcsAgent` API with the following parameters:
+ `two-way-enabled` — Set to `true` to enable two-way messaging.
+ `two-way-channel-arn` — The ARN of the Amazon SNS topic where inbound messages are published.
+ `two-way-channel-role` — The ARN of the IAM role that grants AWS End User Messaging permission to publish messages to the SNS topic.

The following example configures the two-way messaging destination using the AWS CLI:

```
aws pinpoint-sms-voice-v2 update-rcs-agent \
    --rcs-agent-id rcs-a1b2c3d4 \
    --two-way-enabled \
    --two-way-channel-arn arn:aws:sns:us-east-1:123456789012:MyRCSInboundTopic \
    --two-way-channel-role arn:aws:iam::123456789012:role/SMSVoiceSNSPublishRole
```

------

### SNS topic permissions
<a name="rcs-inbound-sns-permissions"></a>

The Amazon SNS topic that you configure for two-way RCS messaging must allow AWS End User Messaging to publish messages to it. You have two options for granting access.

#### Option 1: Use an IAM role
<a name="rcs-inbound-sns-permissions-iam-role"></a>

Create an IAM role that AWS End User Messaging can assume to publish messages to your SNS topic. The role needs both a trust policy and a permission policy.

The following is the **trust policy** for the IAM role. Replace {{accountId}} with the unique ID for your AWS account.

```
{
  "Version": "2012-10-17", 		 	 	 
  "Statement": [
    {
      "Sid": "SMSVoice",
      "Effect": "Allow",
      "Principal": {
        "Service": "sms-voice.amazonaws.com"
      },
      "Action": "sts:AssumeRole",
      "Condition": {
        "StringEquals": {
          "aws:SourceAccount": "{{accountId}}"
        }
      }
    }
  ]
}
```

The following is the **permission policy** for the IAM role. The `SMSVoiceAllowSNSPublish` Sid allows publishing to Amazon SNS topics and the `SMSVoiceAllowEncryptedSNSTopics` Sid is optional for encrypted Amazon SNS topics. Make the following changes:
+ Replace {{partition}} with the AWS partition that you use AWS End User Messaging in.
+ Replace {{region}} with the AWS Region that you use AWS End User Messaging in.
+ Replace {{accountId}} with the unique ID for your AWS account.
+ Replace {{snsTopicName}} with the name of the Amazon SNS topic that receives inbound messages.

```
{
  "Version": "2012-10-17", 		 	 	 
  "Statement": [
    {
      "Sid": "SMSVoiceAllowSNSPublish",
      "Effect": "Allow",
      "Action": "sns:Publish",
      "Resource": "arn:{{partition}}:sns:{{region}}:{{accountId}}:{{snsTopicName}}",
      "Condition": {
        "StringEquals": {
          "aws:ResourceAccount": "{{accountId}}"
        }
      }
    },
    {
      "Sid": "SMSVoiceAllowEncryptedSNSTopics",
      "Effect": "Allow",
      "Action": [
        "kms:Decrypt",
        "kms:GenerateDataKey*"
      ],
      "Resource": "*",
      "Condition": {
        "StringEquals": {
          "kms:EncryptionContext:aws:sns:topicArn": "arn:{{partition}}:sns:{{region}}:{{accountId}}:{{snsTopicName}}",
          "aws:CalledViaLast": "sns.amazonaws.com"
        }
      }
    }
  ]
}
```

#### Option 2: Use an SNS topic policy
<a name="rcs-inbound-sns-permissions-topic-policy"></a>

Alternatively, add a policy statement directly to the SNS topic that allows AWS End User Messaging to publish messages. Replace {{snsTopicArn}} with the ARN of your SNS topic.

```
{
  "Effect": "Allow",
  "Principal": {
    "Service": "sms-voice.amazonaws.com"
  },
  "Action": "sns:Publish",
  "Resource": "{{snsTopicArn}}"
}
```

## Inbound message payload format
<a name="rcs-inbound-payload"></a>

When your AWS RCS Agent receives an inbound text message, AWS End User Messaging publishes a JSON payload to the configured Amazon SNS topic. The RCS inbound message payload uses the same format as SMS two-way messaging:

```
{
  "originationNumber": "+14255550182",
  "destinationNumber": "+12125550101",
  "messageKeyword": "JOIN",
  "messageBody": "EXAMPLE",
  "inboundMessageId": "cae173d2-66b9-564c-8309-21f858e9fb84",
  "previousPublishedMessageId": "wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY"
}
```

The inbound message payload contains the following fields:


**Inbound RCS message payload fields**  

| Field | Description | 
| --- | --- | 
| `originationNumber` | The phone number that sent the inbound message (the customer's phone number). | 
| `destinationNumber` | The identifier of the AWS RCS Agent that received the message. | 
| `messageKeyword` | The registered keyword that matches the inbound message, if any. Keywords are evaluated against the beginning of the message body. | 
| `messageBody` | The text content of the inbound message. | 
| `inboundMessageId` | A unique identifier for the inbound message. | 
| `previousPublishedMessageId` | The unique identifier of the outbound message that the customer is responding to, if the inbound message is a reply to a previous outbound message. | 

## Supported message types
<a name="rcs-inbound-text-only"></a>

AWS End User Messaging supports the following inbound RCS message types. When a customer sends a message to your AWS RCS Agent, AWS End User Messaging delivers a notification to your configured Amazon SNS topic for processing.
+ **Text messages**. The message text is delivered in the SNS notification body.
+ **Media messages** (images, videos, audio files, and documents). When you configure inbound media storage, AWS End User Messaging saves the media file to your Amazon S3 bucket and includes the S3 location in the SNS notification. For more information, see [Receiving inbound RCS media](rcs-inbound-media.md).
+ **Location shares and suggestion responses**. When a customer shares a location or chooses a suggestion, the content is delivered directly in the SNS notification body.

## Keyword management for RCS
<a name="rcs-inbound-keywords"></a>

Keywords allow you to configure automatic responses when customers send specific words or phrases to your AWS RCS Agent. When an inbound message matches a configured keyword, AWS End User Messaging sends the associated auto-response message back to the customer.

For RCS, keywords are configured on the AWS RCS Agent and apply to all associated RCS for Business IDs (testing agent and country launch agents). You can configure up to 30 keywords per AWS RCS Agent.

To manage keywords for your AWS RCS Agent, use the AWS End User Messaging console or the API. For general information about keyword management, see [Keywords in AWS End User Messaging SMS](keywords.md).

**Note**  
Keywords configured on the AWS RCS Agent apply to all associated registrations. You cannot set different keywords for your testing agent and country launch agents independently.

## Processing inbound messages with Lambda
<a name="rcs-inbound-lambda"></a>

A common pattern for processing inbound RCS messages is to subscribe a Lambda function to the Amazon SNS topic configured for two-way messaging. The Lambda function receives the inbound message payload and can implement your application logic, such as responding to customer inquiries, processing commands, or routing messages to other systems.

The following Python example shows a Lambda function that processes inbound RCS messages and sends a response using the `SendTextMessage` API:

```
import json
import boto3

sms_client = boto3.client('pinpoint-sms-voice-v2')

def lambda_handler(event, context):
    # Parse the SNS message
    for record in event['Records']:
        sns_message = json.loads(record['Sns']['Message'])

        origination_number = sns_message['originationNumber']
        message_body = sns_message['messageBody']
        keyword = sns_message.get('messageKeyword', '')

        print(f"Received message from {origination_number}: {message_body}")

        # Process the message and determine a response
        if keyword.upper() == 'HELP':
            response_text = 'Available commands: HELP, STATUS, STOP'
        elif keyword.upper() == 'STATUS':
            response_text = 'Your account is active. No action needed.'
        else:
            response_text = (
                f'Thanks for your message. '
                f'Reply HELP for available commands.'
            )

        # Send a response back to the customer
        try:
            response = sms_client.send_text_message(
                DestinationPhoneNumber=origination_number,
                OriginationIdentity='pool-a1b2c3d4e5f6g7h8i',
                MessageBody=response_text,
                MessageType='TRANSACTIONAL'
            )
            print(f"Response sent. Message ID: {response['MessageId']}")
        except Exception as e:
            print(f"Failed to send response: {str(e)}")

    return {'statusCode': 200}
```

In this example, the Lambda function:

1. Parses the inbound message payload from the SNS event.

1. Checks the `messageKeyword` field to determine the customer's intent.

1. Sends a response using pool-based sending (recommended) through the `SendTextMessage` API. The pool handles channel selection automatically.

**Note**  
When sending responses to inbound messages, use pool-based sending to ensure automatic SMS fallback if the customer's device no longer supports RCS. For details on sending patterns, see [Sending RCS messages](rcs-send-message.md).

## Best practices for inbound RCS messaging
<a name="rcs-inbound-best-practices"></a>

Follow these best practices when implementing two-way RCS messaging:
+ **Implement error handling** — Your Lambda function or SNS subscriber should handle errors gracefully. If your function fails to process a message, configure a dead-letter queue (DLQ) on the SNS subscription to capture unprocessed messages for later retry.
+ **Send fallback responses** — When your application receives a message it cannot process, send a helpful fallback response rather than leaving the customer without a reply. For example, respond with available commands or direct the customer to an alternative support channel.
+ **Use pool-based sending for responses** — When sending responses to inbound messages, use pool-based sending to ensure automatic SMS fallback. This guarantees that your response reaches the customer even if their device no longer supports RCS.
+ **Monitor message processing** — Use Amazon CloudWatch metrics to monitor your inbound message volume and processing success rate. Set up alarms for unusual patterns, such as a sudden increase in inbound messages or a high rate of processing failures. For details on RCS metrics, see [RCS CloudWatch metrics and monitoring](rcs-monitoring.md).
+ **Handle keyword responses consistently** — Ensure that keyword auto-responses and your application's programmatic responses do not conflict. If you configure a keyword auto-response for a specific keyword, your Lambda function still receives the message. Design your function to avoid sending a duplicate response for keywords that already have auto-responses configured.