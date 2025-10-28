# Monitoring with Amazon EventBridge

AWS End User Messaging Social sends events to EventBridge for WhatsApp events. You can use EventBridge to write rules that take actions, such as notifying you, when specific event types
are received. For more information, see the following topics in the Amazon EventBridge User Guide:

- [What is Amazon EventBridge?](../../../eventbridge/latest/userguide/eb-what-is.md "../../../eventbridge/latest/userguide/eb-what-is.md")
- [Amazon EventBridge events](../../../eventbridge/latest/userguide/eb-events.md "../../../eventbridge/latest/userguide/eb-events.md")
- [Amazon EventBridge event patterns](../../../eventbridge/latest/userguide/eb-event-patterns.md "../../../eventbridge/latest/userguide/eb-event-patterns.md")
- [Amazon EventBridge rules](../../../eventbridge/latest/userguide/eb-rules.md "../../../eventbridge/latest/userguide/eb-rules.md")
  AWS End User Messaging Social sends the following events to Amazon EventBridge:

- WhatsApp Message Delivered
- WhatsApp Message Failed
- WhatsApp Message Handover Failed
- WhatsApp Message Handover Succeeded
- WhatsApp Message Read
- WhatsApp Message Received
- WhatsApp Message Sent
- WhatsApp Message Undeliverable
- WhatsApp Unknown Notification Received

## Event for a delivered WhatsApp message

```
{
    "version": "0",
    "id": "76a454c4-26df-6e2c-bc50-2137de2a0fe7",
    "detail-type": "WhatsApp Message Delivered",
    "source": "aws.social-messaging",
    "account": "111122223333",
    "time": "2025-10-03T04:34:24Z",
    "region": "ca-central-1",
    "resources": [],
    "detail": {
        "wabaId": "1163793972139053",
        "originationPhoneNumber": "15815555555",
        "originationPhoneNumberId": "574086085794038",
        "messageId": "4bee7d29-70f5-4a49-b84e-facf4424fe58",
        "status": "delivered",
        "eventTimestamp": "1759466063"
    }
}
```

## Event for a read WhatsApp message

```
{
    "version": "0",
    "id": "c730142c-96d6-28f6-00d4-1a8a12e509da",
    "detail-type": "WhatsApp Message Read",
    "source": "aws.social-messaging",
    "account": "111122223333",
    "time": "2025-10-03T04:53:07Z",
    "region": "ca-central-1",
    "resources": [],
    "detail": {
        "wabaId": "1163793972139053",
        "originationPhoneNumber": "15815555555",
        "originationPhoneNumberId": "574086085794038",
        "messageId": "e16d4108-fe93-471f-a057-4c6473e68430",
        "status": "read",
        "eventTimestamp": "1759467185"
    }
}
```

## Event for a sent WhatsApp message

```
{
    "version": "0",
    "id": "09b261c5-5c4b-b912-afa8-845214926b2f",
    "detail-type": "WhatsApp Message Sent",
    "source": "aws.social-messaging",
    "account": "111122223333",
    "time": "2025-10-03T04:26:16Z",
    "region": "ca-central-1",
    "resources": [],
    "detail": {
        "wabaId": "1163793972139053",
        "originationPhoneNumber": "15815555555",
        "originationPhoneNumberId": "574086085794038",
        "messageId": "a8dec257-b52e-4acc-8654-3dfb96468a43",
        "status": "sent",
        "eventTimestamp": "1759465574"
    }
}
```

## Event for a failed WhatsApp message

```
{
    "version": "0",
    "id": "281b8c6b-f39f-f768-4229-d66e893592c1",
    "detail-type": "WhatsApp Message Failed",
    "source": "aws.social-messaging",
    "account": "111122223333",
    "time": "2025-10-03T04:49:25Z",
    "region": "ca-central-1",
    "resources": [],
    "detail": {
        "wabaId": "1163793972139053",
        "originationPhoneNumber": "15815555555",
        "originationPhoneNumberId": "574086085794038",
        "messageId": "7bd36188-6123-4ded-a1dd-f017f0814405",
        "status": "failed",
        "eventTimestamp": "1759466965",
        "errors": [
            {
                "code": 131026,
                "title": "Message undeliverable",
                "message": "Message undeliverable"
            }
        ]
    }
}
```
