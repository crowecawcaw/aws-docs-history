

# Create an outbound campaign using the API or CLI
<a name="create-campaigns-api-cli"></a>

You can create and manage outbound campaigns programmatically using the AWS CLI or the [Amazon Connect Outbound Campaigns API](https://docs.aws.amazon.com/connect/latest/APIReference/API_Operations_Amazon_Connect_Outbound_Campaigns_V2.html). This topic explains how to create a Connect Customer outbound campaign, define campaign flows, and reference lifecycle commands using the CLI.

## Prerequisites
<a name="create-campaigns-api-cli-prereqs"></a>

Before you create a campaign using the API or CLI, make sure you have the following:
+ An Connect Customer instance with [outbound calling enabled](enable-outbound-calls.md).
+ An AWS KMS key configured for outbound campaigns. See [Create an AWS KMS key](enable-outbound-campaigns.md#create-kms-key-campaigns).
+ Outbound campaigns enabled on your instance. See [Configure outbound campaigns](enable-outbound-campaigns.md#configure-outbound-campaigns).
+ A [Customer Profiles segment](segmentation-admin-website.md) ARN for your campaign recipients.
+ Message templates created in your agent assist knowledge base. For more information, see [Create message templates](https://docs.aws.amazon.com/connect/latest/adminguide/create-message-templates.html).
+ The AWS CLI version 2 installed and configured. For more information, see [Installing the AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html).

## Create a campaign flow
<a name="create-campaigns-api-cli-flows"></a>

Campaign flows define the sequence of actions that run for each recipient. You create flows using the [CreateContactFlow](https://docs.aws.amazon.com/connect/latest/APIReference/API_CreateContactFlow.html) API with the flow type set to `CAMPAIGN`. For detailed information about each action type, see [Journey flow block definitions](journey-flow-block-definitions.md).

### Simple flow (no retries)
<a name="create-campaigns-api-cli-flows-simple"></a>

A simple flow sends a single communication to each recipient without checking delivery status. This is the simplest flow structure:

```
{
  "Version": "2019-10-30",
  "StartAction": "SendSMS",
  "Actions": [
    {
      "Identifier": "SendSMS",
      "Type": "SendSMS",
      "Parameters": {
        "Message": {
          "MessageSourceType": "TEMPLATE",
          "TemplatedMessage": {
            "WisdomKnowledgeBaseArn": "arn:aws:wisdom:us-east-1:123456789012:knowledge-base/your-kb-id",
            "WisdomMessageTemplateArn": "arn:aws:wisdom:us-east-1:123456789012:message-template/your-kb-id/your-template-id"
          }
        },
        "SourceEndpoint": {
          "Address": "arn:aws:connect:us-east-1:123456789012:phone-number/your-phone-number-id",
          "Type": "CONNECT_PHONENUMBER_ARN"
        }
      },
      "Transitions": {
        "NextAction": "EndFlow",
        "Conditions": [],
        "Errors": [
          {
            "NextAction": "EndFlow",
            "ErrorType": "NoMatchingError"
          }
        ]
      }
    },
    {
      "Identifier": "EndFlow",
      "Type": "EndFlowExecution",
      "Parameters": {}
    }
  ]
}
```

### Flow with delivery status check and retries
<a name="create-campaigns-api-cli-flows-retry"></a>

For flows that check delivery status and retry on failure, use the following structure. The flow sends a communication, waits for a delivery receipt, retrieves the communication status, and then branches based on the result.

The key actions in a retry flow are:

1. **SendSMS**, **SendOutboundEmail**, or **PutDialRequest**—Sends the outbound communication.

1. **Wait**—Waits for the delivery receipt.

1. **GetOutboundCommunicationStatus**—Retrieves the delivery status of the most recent communication.

1. **Compare**—Evaluates the delivery receipt and branches based on the result (for example, retry on bounce, end on success).

1. **EndFlowExecution**—Terminates the flow. All flow paths must end with this action.

The following example shows a flow for a `MANAGED` campaign that sends an SMS, waits for a delivery receipt, checks the status, and retries with an email if the message bounced:

```
{
  "Version": "2019-10-30",
  "StartAction": "SendSMS",
  "Actions": [
    {
      "Identifier": "SendSMS",
      "Type": "SendSMS",
      "Parameters": {
        "Message": {
          "MessageSourceType": "TEMPLATE",
          "TemplatedMessage": {
            "WisdomKnowledgeBaseArn": "arn:aws:wisdom:us-east-1:123456789012:knowledge-base/your-kb-id",
            "WisdomMessageTemplateArn": "arn:aws:wisdom:us-east-1:123456789012:message-template/your-kb-id/your-sms-template-id"
          }
        },
        "SourceEndpoint": {
          "Address": "arn:aws:connect:us-east-1:123456789012:phone-number/your-phone-number-id",
          "Type": "CONNECT_PHONENUMBER_ARN"
        }
      },
      "Transitions": {
        "NextAction": "Wait",
        "Conditions": [],
        "Errors": [
          {
            "NextAction": "EndFlow",
            "ErrorType": "NoMatchingError"
          }
        ]
      }
    },
    {
      "Identifier": "Wait",
      "Type": "Wait",
      "Parameters": {
        "TimeLimitSeconds": "900"
      },
      "Transitions": {
        "NextAction": "GetOutboundCommunicationStatus",
        "Conditions": [
          {
            "NextAction": "GetOutboundCommunicationStatus",
            "Condition": {
              "Operator": "Equals",
              "Operands": ["WaitCompleted"]
            }
          }
        ],
        "Errors": [
          {
            "NextAction": "EndFlow",
            "ErrorType": "NoMatchingError"
          }
        ]
      }
    },
    {
      "Identifier": "GetOutboundCommunicationStatus",
      "Type": "GetOutboundCommunicationStatus",
      "Parameters": {
        "OutboundCommunicationIds": ["$.OutboundCommunication.Latest.Id"]
      },
      "Transitions": {
        "NextAction": "Compare",
        "Conditions": [],
        "Errors": [
          {
            "NextAction": "EndFlow",
            "ErrorType": "NoMatchingError"
          }
        ]
      }
    },
    {
      "Identifier": "Compare",
      "Type": "Compare",
      "Parameters": {
        "ComparisonValue": "$.DeliveryReceipts['`$.OutboundCommunication.Latest.Id`'].Bounce"
      },
      "Transitions": {
        "NextAction": "EndFlow",
        "Conditions": [
          {
            "NextAction": "SendEmail",
            "Condition": {
              "Operator": "Exists",
              "Operands": []
            }
          }
        ],
        "Errors": [
          {
            "NextAction": "EndFlow",
            "ErrorType": "NoMatchingCondition"
          }
        ]
      }
    },
    {
      "Identifier": "SendEmail",
      "Type": "SendOutboundEmail",
      "Parameters": {
        "EmailMessage": {
          "MessageSourceType": "TEMPLATE",
          "TemplatedMessage": {
            "WisdomKnowledgeBaseArn": "arn:aws:wisdom:us-east-1:123456789012:knowledge-base/your-kb-id",
            "WisdomMessageTemplateArn": "arn:aws:wisdom:us-east-1:123456789012:message-template/your-kb-id/your-email-template-id"
          }
        },
        "FromEmailAddress": {
          "EmailAddress": "noreply@example.com"
        }
      },
      "Transitions": {
        "NextAction": "EndFlow",
        "Conditions": [],
        "Errors": [
          {
            "NextAction": "EndFlow",
            "ErrorType": "NoMatchingError"
          }
        ]
      }
    },
    {
      "Identifier": "EndFlow",
      "Type": "EndFlowExecution",
      "Parameters": {}
    }
  ]
}
```

**Important**  
If your flow uses multiple channel types (for example, SMS and email), include all channels in the `--channel-subtype-config` parameter when creating the campaign.
For flows used in campaigns with type `MANAGED` that check delivery status, the required action sequence is: **Wait** → **GetOutboundCommunicationStatus** → **Compare**. The `Wait` action pauses the flow for a specified duration to allow time for the delivery receipt to arrive. The `GetOutboundCommunicationStatus` action retrieves the delivery status. The `Compare` action branches based on the result.
The `OutboundCommunicationIds` parameter in `GetOutboundCommunicationStatus` must reference `$.OutboundCommunication.Latest.Id`. Delivery receipt references in `Compare` actions must use the same key. For example: `$.DeliveryReceipts['`$.OutboundCommunication.Latest.Id`'].Bounce`.
`MANAGED` campaigns that use voice channels require `dialCriteriaRules` in the `PutDialRequest` action:  

  ```
  {
    "Identifier": "PutDialRequest",
    "Type": "PutDialRequest",
    "Parameters": {
      "dialCriteriaRules": [
        {
          "type": "CheckSegmentMembershipForCustomerProfile",
          "segmentArn": "arn:aws:profile:us-east-1:123456789012:domains/your-domain/segments/your-segment"
        }
      ]
    },
    ...
  }
  ```

## Create a campaign flow version
<a name="create-campaigns-api-cli-version"></a>

After you create a campaign flow, you must create a version of the flow. The versioned flow ARN is required when creating a campaign. Use the [CreateContactFlowVersion](https://docs.aws.amazon.com/connect/latest/APIReference/API_CreateContactFlowVersion.html) API to create a version.

The versioned flow ARN includes a version suffix. For example: `arn:aws:connect:us-east-1:123456789012:instance/your-instance-id/contact-flow/your-flow-id:1`

For more information, see the [create-contact-flow-version CLI reference](https://docs.aws.amazon.com/cli/latest/reference/connect/create-contact-flow-version.html).

## Create an outbound campaign
<a name="create-campaigns-api-cli-create"></a>

Use the `create-campaign` command to create a campaign. The following example creates an SMS campaign with agentless outbound mode:

```
aws connectcampaignsv2 create-campaign \
  --name "My SMS Campaign" \
  --connect-instance-id "your-instance-id" \
  --type MANAGED \
  --connect-campaign-flow-arn "arn:aws:connect:us-east-1:123456789012:instance/your-instance-id/contact-flow/your-flow-id:1" \
  --source '{"customerProfilesSegmentArn": "arn:aws:profile:us-east-1:123456789012:domains/your-domain/segments/your-segment"}' \
  --channel-subtype-config '{
    "sms": {
      "outboundMode": {"agentless": {}},
      "defaultOutboundConfig": {
        "connectSourcePhoneNumberArn": "arn:aws:connect:us-east-1:123456789012:phone-number/your-phone-number-id",
        "wisdomTemplateArn": "arn:aws:wisdom:us-east-1:123456789012:message-template/your-kb-id/your-template-id"
      }
    }
  }' \
  --schedule '{"startTime": "2026-07-01T09:00:00", "endTime": "2026-07-01T17:00:00", "refreshFrequency": "PT30M"}' \
  --communication-time-config '{
    "localTimeZoneConfig": {"defaultTimeZone": "America/New_York"},
    "sms": {
      "openHours": {
        "dailyHours": {
          "MONDAY": [{"startTime": "T09:00", "endTime": "T17:00"}],
          "TUESDAY": [{"startTime": "T09:00", "endTime": "T17:00"}],
          "WEDNESDAY": [{"startTime": "T09:00", "endTime": "T17:00"}],
          "THURSDAY": [{"startTime": "T09:00", "endTime": "T17:00"}],
          "FRIDAY": [{"startTime": "T09:00", "endTime": "T17:00"}]
        }
      }
    }
  }' \
  --region us-east-1
```

On success, the command returns the campaign ID and ARN:

```
{
  "id": "campaign-id",
  "arn": "arn:aws:connect-campaigns:us-east-1:123456789012:campaign/campaign-id"
}
```

**Note**  
The `--type` parameter specifies the campaign type. Use `MANAGED` for outbound campaigns. Use `JOURNEY` for multi-step, multi-channel journeys—see [Visual Journey Builder](create-a-multi-step-and-multi-channel-journey.md).

**Note**  
You can also specify `--communication-limits-override` to control how many times a recipient can be contacted. For the full list of parameters, see the [create-campaign CLI reference](https://docs.aws.amazon.com/cli/latest/reference/connectcampaignsv2/create-campaign.html).

To manage campaign lifecycle operations (start, stop, pause, resume, delete), see the [AWS CLI reference for connectcampaignsv2](https://docs.aws.amazon.com/cli/latest/reference/connectcampaignsv2/index.html).