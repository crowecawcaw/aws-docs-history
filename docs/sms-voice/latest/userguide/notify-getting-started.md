# Getting started with Notify

This tutorial walks you through creating a Notify configuration and sending your first
OTP message. You can complete this tutorial in about 5 minutes.

## Prerequisites

- An AWS account.
- IAM permissions for AWS End User Messaging SMS operations. For more information, see
  [Identity and access management for AWS End User Messaging SMS](security-iam.md "security-iam.md").

The following IAM policy grants permissions to send messages and browse templates:

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": [
                "sms-voice:SendNotifyTextMessage",
                "sms-voice:SendNotifyVoiceMessage",
                "sms-voice:DescribeNotifyTemplates",
                "sms-voice:DescribeNotifyConfigurations",
                "sms-voice:ListNotifyCountries",
                "sms-voice:PutMessageFeedback"
            ],
            "Resource": "*"
        }
    ]
}
```

The following policy grants full Notify management permissions:

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": [
                "sms-voice:CreateNotifyConfiguration",
                "sms-voice:UpdateNotifyConfiguration",
                "sms-voice:DeleteNotifyConfiguration",
                "sms-voice:DescribeNotifyConfigurations",
                "sms-voice:DescribeNotifyTemplates",
                "sms-voice:ListNotifyCountries",
                "sms-voice:SendNotifyTextMessage",
                "sms-voice:SendNotifyVoiceMessage",
                "sms-voice:SetNotifyMessageSpendLimitOverride",
                "sms-voice:DeleteNotifyMessageSpendLimitOverride",
                "sms-voice:PutMessageFeedback"
            ],
            "Resource": "*"
        }
    ]
}
```

To restrict permissions to a specific Notify configuration, use the configuration ARN
for resource-level actions (such as `SendNotifyTextMessage`,
`SendNotifyVoiceMessage`, `DescribeNotifyConfigurations`,
`CreateNotifyConfiguration`, `UpdateNotifyConfiguration`, and
`DeleteNotifyConfiguration`). Actions that do not support resource-level
permissions (such as `DescribeNotifyTemplates`,
`ListNotifyCountries`, `SetNotifyMessageSpendLimitOverride`,
`DeleteNotifyMessageSpendLimitOverride`, and
`PutMessageFeedback`) require `"Resource": "*"`.

## Step 1: Create a Notify configuration

Console

1. Open the AWS End User Messaging SMS console at
   [https://console.aws.amazon.com/sms-voice/](https://console.aws.amazon.com/sms-voice/ "https://console.aws.amazon.com/sms-voice/").
2. In the navigation pane, under **Notify**, choose
   **Notify configurations**.
3. Choose **Create Notify configuration**.
4. For **Display name**, enter your brand name (for example,
   `AcmeCorp`).
5. For **Use case**, **Code verification** is
   automatically selected.
6. For **Channels**, select **SMS**,
   **VOICE**, or both.
7. (Optional) Expand **Advanced settings** to select countries,
   a default template, an associated pool, or enable deletion protection.
8. Choose **Create Notify configuration**.

Your configuration is created in **Pending** status while
the system validates your account. Once validated, the status changes to
**Active** and you can start sending messages.

###### Note

Configuration creation includes automated account validation and brand name
checks. Most configurations are activated within seconds. If your brand name requires
verification, the status will be **Requires
verification**.

AWS CLI

```
aws pinpoint-sms-voice-v2 create-notify-configuration \
    --display-name "AcmeCorp" \
    --use-case CODE_VERIFICATION \
    --enabled-channels SMS
```

Configuration statuses:

PENDING
Configuration is being validated.

ACTIVE
Ready to send messages.

REQUIRES_VERIFICATION
Brand name requires verification before activation.

REJECTED
Configuration was rejected. Check `RejectionReason` for
details.

## Step 2: Browse available templates

Before sending, check which templates are available for your tier and channel:

```
aws pinpoint-sms-voice-v2 describe-notify-templates \
    --filters '[{"Name":"channels","Values":["SMS"]},{"Name":"tier-access","Values":["BASIC"]}]'
```

## Step 3: Send a test message

Console

1. In the Notify configurations list, choose your configuration.
2. Choose the **Test** tab.
3. Select a template from the templates table.
4. For **Destination phone number**, enter a phone number in
   E.164 format (for example, `+12065550100`).
5. Fill in the template variables (for example, enter `123456` for
   the **code** variable).
6. Choose **Send**.

AWS CLI

```
aws pinpoint-sms-voice-v2 send-notify-text-message \
    --notify-configuration-id "`nc-1234567890abcdef0`" \
    --destination-phone-number "`+12065550100`" \
    --template-id "`notify-code-verification-english-001`" \
    --template-variables '{"code":"123456"}'
```

Python (boto3)

```
import boto3

client = boto3.client('pinpoint-sms-voice-v2')

response = client.send_notify_text_message(
    NotifyConfigurationId='nc-1234567890abcdef0',
    DestinationPhoneNumber='+12065550100',
    TemplateId='notify-code-verification-english-001',
    TemplateVariables={
        'code': '123456'
    }
)

print(f"Message ID: {response['MessageId']}")
print(f"Resolved body: {response['ResolvedMessageBody']}")
```

## Step 4: Check available countries

Use `ListNotifyCountries` to see which countries are available for your tier
and channel:

```
aws pinpoint-sms-voice-v2 list-notify-countries \
    --channels SMS \
    --tier BASIC
```

## Next steps

- [Managing Notify configurations](notify-configurations.md "notify-configurations.md") – Learn about all configuration options.
- [Working with Notify templates](notify-templates.md "notify-templates.md") – Browse and understand available templates.
- [Notify tiers](notify-tiers.md "notify-tiers.md") – Learn about tiers and how to upgrade to Advanced.
- [Notify spend limits](notify-spend-limits.md "notify-spend-limits.md") – Manage your Notify spend limits.
