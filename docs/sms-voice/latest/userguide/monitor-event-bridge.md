# Monitoring with EventBridge

AWS End User Messaging SMS sends events to EventBridge for Registration, SMS, MMS, and voice events. You can use EventBridge to write rules that take actions, such as notifying you, when specific event types
are received. For more information, see the following topics in the Amazon EventBridge User Guide:

- [What is Amazon EventBridge?](../../../eventbridge/latest/userguide/eb-what-is.md "../../../eventbridge/latest/userguide/eb-what-is.md")
- [Amazon EventBridge events](../../../eventbridge/latest/userguide/eb-events.md "../../../eventbridge/latest/userguide/eb-events.md")
- [Amazon EventBridge event patterns](../../../eventbridge/latest/userguide/eb-event-patterns.md "../../../eventbridge/latest/userguide/eb-event-patterns.md")
- [Amazon EventBridge rules](../../../eventbridge/latest/userguide/eb-rules.md "../../../eventbridge/latest/userguide/eb-rules.md")
  AWS End User Messaging SMS sends the following events directly to EventBridge:

- Text Message Delivery Status Updated
- Media Message Delivery Status Updated
- Voice Message Delivery Status Updated
- Registration Status Change
  For text, media, and voice message events, the `detail` section in the following examples resembles the
  [Example event
  data](configuration-sets-event-format.md "configuration-sets-event-format.md").

## Event for a delivered SMS message

```
{
    "version": "0",
    "id": "5c0fa4f8-e4ba-ed02-6101-c795472fccd0",
    "detail-type": "Text Message Delivery Status Updated",
    "source": "aws.sms-voice",
    "account": "111122223333",
    "time": "2025-10-01T18:20:41Z",
    "region": "us-east-1",
    "resources": [],
    "detail": {
        "eventType": "TEXT_SUCCESSFUL",
        "eventVersion": "1.0",
        "eventTimestamp": 1759342841377,
        "isFinal": true,
        "originationPhoneNumber": "VAJZNBLLDX",
        "isoCountryCode": "ES",
        "isInternationalSend": false,
        "mcc": "214",
        "mnc": "05",
        "carrierName": "Movistar",
        "messageId": "ed23196c-75ce-4727-93ee-7bf72b64998f",
        "messageRequestTimestamp": 1759342840978,
        "messageEncoding": "GSM",
        "messageType": "TRANSACTIONAL",
        "messageStatus": "SUCCESSFUL",
        "messageStatusDescription": "Message has been accepted by phone carrier",
        "totalMessageParts": 1,
        "totalMessagePrice": 0.06087,
        "totalCarrierFee": 0.0,
        "protectConfiguration": {
            "protectConfigurationId": "protect-e06e5d722c31455286262a108e7d863d",
            "protectStatus": "ALLOW"
        }
    }
}
```

## Event for a sent SMS message

```
{
    "version": "0",
    "id": "4111946b-816c-e73a-9ea0-a8367b9d57e4",
    "detail-type": "Text Message Delivery Status Updated",
    "source": "aws.sms-voice",
    "account": "555555555555",
    "time": "2024-10-16T17:20:24Z",
    "region": "eu-west-2",
    "resources": [],
    "detail": {
        "eventType": "TEXT_SUCCESSFUL",
        "eventVersion": "1.0",
        "eventTimestamp": 1729099224788,
        "isFinal": true,
        "originationPhoneNumber": "+18445550123",
        "isoCountryCode": "US",
        "isInternationalSend": false,
        "messageId": "9539975a-e71f-45f3-b496-8d98dc098a77",
        "messageRequestTimestamp": 1729099224438,
        "messageEncoding": "GSM",
        "messageType": "PROMOTIONAL",
        "messageStatus": "SUCCESSFUL",
        "messageStatusDescription": "Message has been accepted by phone carrier",
        "totalMessageParts": 1,
        "totalMessagePrice": 0.00581,
        "totalCarrierFee": 0.00302,
        "protectConfiguration": {
            "protectConfigurationId": "protect-e06e5d722c31455286262a108e7d863d",
            "protectStatus": "ALLOW"
        }
    }
}
```

## Event for a sent voice message

```
{
    "version": "0",
    "id": "3bd18839-b5b4-79c5-1b18-bd6545f40566",
    "detail-type": "Voice Message Delivery Status Updated",
    "source": "aws.sms-voice",
    "account": "444455556666",
    "time": "2024-10-16T17:18:50Z",
    "region": "eu-west-2",
    "resources": [],
    "detail": {
        "eventType": "VOICE_INITIATED",
        "eventVersion": "1.0",
        "eventTimestamp": 1729099130226,
        "isFinal": false,
        "originationPhoneNumber": "+18445550123",
        "isoCountryCode": "US",
        "messageId": "1d2295bd-ac9b-4517-821f-7c6d95d789a1",
        "messageRequestTimestamp": 1729099129845,
        "messageStatus": "INITIATED"
    }
}
```

## Event for a registration status change

AWS End User Messaging SMS sends the following registration status changes to Amazon EventBridge:

`CLOSED`, `CREATED`, `COMPLETE`, `DELETED`, `PROVISIONING`, `REQUIRES_AUTHENTICATION`, `REQUIRES_UPDATES`, `REVIEWING`, `SUBMITTED`

For definitions of these status values, see
[RegistrationInformation](../../../pinpoint/latest/apireference_smsvoicev2/API_RegistrationInformation.md "../../../pinpoint/latest/apireference_smsvoicev2/API_RegistrationInformation.md") in the AWS End User Messaging SMS API Reference.

```
{
    "version": "0",
    "id": "d2e8812b-d34c-90f9-a8a9-3f18e15d1db9",
    "detail-type": "Registration Status Change",
    "source": "aws.sms-voice",
    "account": "111122223333",
    "time": "2025-09-26T17:42:25Z",
    "region": "us-east-1",
    "resources": ["arn:aws:sms-voice:us-east-1:111122223333:registration/registration-30a16a8b7cec478a8e37febbb9005348"],
    "detail": {
        "registrationDetails": {
            "registrationId": "registration-30a16a8b7cec478a8e37febbb9005348",
            "registrationVersionNumber": 1,
            "registrationType": "ZZ_LONG_CODE_REGISTRATION",
            "registrationStatusChangeTimestamp": 1758908543000,
            "currentStatus": "SUBMITTED"
        },
        "registrationArn": "arn:aws:sms-voice:us-east-1:111122223333:registration/registration-30a16a8b7cec478a8e37febbb9005348"
    }
}
```
