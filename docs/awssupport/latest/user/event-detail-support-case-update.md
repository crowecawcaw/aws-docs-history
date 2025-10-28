# Support Case Update event

Below are the detail fields for the `Support Case Update` event.

The `source` and `detail-type` fields are included below because they contain specific values for AWS Support events. For
definitions of the other metadata fields that are included in all events, see [Event structure](../../../eventbridge/latest/ref/overiew-event-structure.md "../../../eventbridge/latest/ref/overiew-event-structure.md") in the _Amazon EventBridge Events Reference_.

```
{
  . . .,
  "detail-type": "Support Case Update",
  "source": "aws.support",
  . . .,
  "detail": {
    "case-id" : "`string`",
    "display-id" : "`string`",
    "communication-id" : "`string`",
    "event-name" : "`string`",
    "origin" : "`string`"
  }
}
```

`detail-type`

Identifies the type of event.

For this event, this value is `Support Case Update`.

`source`

Identifies the service that generated the event. For AWS Support events,
this value is `aws.support`.

`detail`

A JSON object that contains information about the event. The service
generating the event determines the content of this field.

For this event, this data includes:

`case-id`

The support case ID.
The case ID is an alphanumeric string in the following format: case-_12345678910-2013-c4c1d2bf33c5cf47_.

`display-id`

The identifier for the case on pages in the AWS Support Center.

`communication-id`

The communication ID.

`event-name`

_Valid values_: `CreateCase` | `AddCommunicationToCase` | `ResolveCase` | `ReopenCase`

Specifies the type of support case event.

`origin`

_Valid values_: `AWS` | `CUSTOMER`

Specifies whether you or an AWS Support agent added a case
correspondence to a support case.

Currently, only events with an `event-name` of `AddCommunicationToCase` will contain have this value.

###### Example Support Case Update event

example: Support case created

```
{
    "version": "0",
    "id": "3433df007-9285-55a3-f6d1-536944be45d7",
    "detail-type": "Support Case Update",
    "source": "aws.support",
    "account": "111122223333",
    "time": "2022-02-21T15:51:19Z",
    "region": "us-east-1",
    "resources": [],
    "detail": {
        "case-id": "case-111122223333-muen-2022-7118885805350839",
        "display-id": "1234563851",
        "communication-id": "",
        "event-name": "CreateCase",
        "origin": ""
    }
}
```

###### Example Support Case Update event

example: AWS Support replies to a support case

```
{
    "version": "0",
    "id": "f90cb8cb-32be-1c91-c0ba-d50b4ca5e51b",
    "detail-type": "Support Case Update",
    "source": "aws.support",
    "account": "111122223333",
    "time": "2022-02-21T15:51:31Z",
    "region": "us-east-1",
    "resources": [],
    "detail": {
        "case-id": "case-111122223333-muen-2022-7118885805350839",
        "display-id": "1234563851",
        "communication-id": "ekko:us-east-1:12345678-268a-424b-be08-54613cab84d2",
        "event-name": "AddCommunicationToCase",
        "origin": "AWS"
    }
}
```

###### Example Support Case Update event

example: Support case resolved

```
{
    "version": "0",
    "id": "1aa4458d-556f-732e-ddc1-4a5b2fbd14a5",
    "detail-type": "Support Case Update",
    "source": "aws.support",
    "account": "111122223333",
    "time": "2022-02-21T15:51:31Z",
    "region": "us-east-1",
    "resources": [],
    "detail": {
        "case-id": "case-111122223333-muen-2022-7118885805350839",
        "display-id": "1234563851",
        "communication-id": "",
        "event-name": "ResolveCase",
        "origin": ""
    }
}
```

###### Example Support Case Update event

example: Support case reopened

```
{
    "version": "0",
    "id": "3bb9d8fe-6089-ad27-9508-804209b233ad",
    "detail-type": "Support Case Update",
    "source": "aws.support",
    "account": "111122223333",
    "time": "2022-02-21T15:47:19Z",
    "region": "us-east-1",
    "resources": [],
    "detail": {
        "case-id": "case-111122223333-muen-2021-27f40618fe0303ea",
        "display-id": "1234563851",
        "communication-id": "",
        "event-name": "ReopenCase",
        "origin": ""
    }
}
```
