# Monitoring IAM Roles Anywhere events in Amazon EventBridge

You can monitor IAM Roles Anywhere events in [Amazon EventBridge](../../../eventbridge/latest/userguide.md "../../../eventbridge/latest/userguide.md"). Events from IAM Roles Anywhere are delivered to EventBridge in near-real time. You can write simple rules to indicate which events are of interest to you and the automated actions to take when an event matches a rule. With EventBridge, you can use events to trigger targets including AWS Lambda functions, AWS Batch jobs, Amazon SNS topics, and many others. For more information, see [Creating Amazon EventBridge rules that react to events](../../../eventbridge/latest/userguide/eb-create-rule.md "../../../eventbridge/latest/userguide/eb-create-rule.md").

The following examples show events for IAM Roles Anywhere.

###### Topics

- [Trust anchor certificate expiration event](#trust_anchor_cert_expiry_event "#trust_anchor_cert_expiry_event")
- [Intermediate or end-entity certificate expiration event](#cert_expiry_event "#cert_expiry_event")
- [Responding to an event](#event-sns-response "#event-sns-response")

## Trust anchor certificate expiration event

IAM Roles Anywhere sends daily expiration event for each trust anchor certificate that satisfies [notification evaluation criteria](customize-notification-settings.md#notification-evaluation "customize-notification-settings.md#notification-evaluation"). You can use expiration events to configure Amazon SNS to send a text notification whenever IAM Roles Anywhere generates this event.

Expiration events have the following structure.

```
{
  "version": "0",
  "id": "9c95e8e4-96a4-ef3f-b739-b6aa5b193afb",
  "detail-type": "Roles Anywhere Certificate Expiration State Change",
  "source": "aws.rolesanywhere",
  "account": "123456789012",
  "time": "2022-06-10T06:51:08Z",
  "region": "us-west-1",
  "resources": [
    "arn:aws:rolesanywhere:us-west-1:123456789012:trust-anchor/61f50cd4-45b9-4259-b049-d0a53682fa4b"
  ],
  "detail": {
    "certificate-serial-number": "00936EACBE07F201DF",
    "days-to-expiry": 3,
    "issuer": "L=Seattle,CN=CA Root v1,ST=Washington,C=US"
  }
}
```

## Intermediate or end-entity certificate expiration event

IAM Roles Anywhere sends an expiration event for intermediate or end-entity certificates when the certificate satisfies [notification evaluation criteria](customize-notification-settings.md#notification-evaluation "customize-notification-settings.md#notification-evaluation") and used in createSession API. You can use expiration events to configure Amazon SNS to send a text notification whenever IAM Roles Anywhere generates this event.

Expiration events have the following structure.

```
{
  "version": "0",
  "id": "9c95e8e4-96a4-ef3f-b739-b6aa5b193afb",
  "detail-type": "Roles Anywhere Certificate Expiration State Change",
  "source": "aws.rolesanywhere",
  "account": "123456789012",
  "time": "2022-06-10T06:51:08Z",
  "region": "us-west-1",
  "detail": {
    "certificate-serial-number": "00936EACBE07F201DF",
    "days-to-expiry": 3,
    "issuer": "L=Seattle,CN=CA Root v1,ST=Washington,C=US"
  }
}
```

## Responding to an event

You can configure Amazon Simple Notification Service to send a text notification whenever IAM Roles Anywhere generates an
EventBridge event.

###### To create an Amazon EventBridge rule that reacts to events

1. Open the Amazon EventBridge console at [https://console.aws.amazon.com/events/](https://console.aws.amazon.com/events/ "https://console.aws.amazon.com/events/").
2. In the navigation pane, choose **Rules**.
3. Choose **Create rule**.
4. Enter a name and description for the rule.

A rule can't have the same name as another rule in the same Region and on the
same event bus. 5. For **Event bus**, choose the event bus that you want
to associate with this rule. If you want this rule to match events that come
from your account, select **AWS default event bus**. When an
AWS service in your account emits an event, it always goes to your account’s
default event bus. 6. For **Rule type**, choose **Rule with an event
pattern**. 7. Choose **Next**. 8. For **Event source**, choose
**AWS services**. 9. For **Sample events**, choose an event under
**IAM Roles Anywhere**. 10. For **Event pattern**, do the following:

    1. For **Event source**, choose **AWS
     services**.
    2. For **AWS service**, choose
     **IAM Roles Anywhere.**
    3. For **Event Type**, choose an **IAM Roles Anywhere**
     event.
    4. Choose **Next**

11. In the **Targets** section, choose a service that can consume your
    event such as Amazon SNS, or choose **Lambda function** to pass the event to
    customized executable code.
