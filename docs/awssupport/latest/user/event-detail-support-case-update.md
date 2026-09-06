

# Support Case Update event
<a name="event-detail-support-case-update"></a>

Below are the detail fields for the `Support Case Update` event.

The `source` and `detail-type` fields are included below because they contain specific values for AWS Support events. For definitions of the other metadata fields that are included in all events, see [Event structure ](https://docs.aws.amazon.com/eventbridge/latest/ref/overiew-event-structure.html) in the *Amazon EventBridge Events Reference*.

```
{
  . . .,
  "detail-type": "Support Case Update",
  "source": "aws.support",
  . . .,
  "detail": {
    "case-id" : "{{string}}",
    "display-id" : "{{string}}",
    "communication-id" : "{{string}}",
    "event-name" : "{{string}}",
    "origin" : "{{string}}"
  }
}
```

`detail-type`  <a name="support-case-update-detail-type"></a>
Identifies the type of event.  
For this event, this value is `Support Case Update`.

`source`  <a name="support-case-update-source"></a>
Identifies the service that generated the event. For AWS Support events, this value is `aws.support`.

`detail`  <a name="support-case-update-detail"></a>
A JSON object that contains information about the event. The service generating the event determines the content of this field.  
For this event, this data includes:    
`case-id`  <a name="support-case-update-case-id"></a>
The support case ID. The case ID is an alphanumeric string in the following format: case-*12345678910-2013-c4c1d2bf33c5cf47*.  
`display-id`  <a name="support-case-update-display-id"></a>
The identifier for the case on pages in the AWS Support Center.  
`communication-id`  <a name="support-case-update-communication-id"></a>
The communication ID.  
`event-name`  <a name="support-case-update-event-name"></a>
*Valid values*: `CreateCase` \| `AddCommunicationToCase` \| `ResolveCase` \| `ReopenCase`  
Specifies the type of support case event.  
`origin`  <a name="support-case-update-origin"></a>
*Valid values*: `AWS` \| `CUSTOMER`  
Specifies whether you or an AWS Support agent added a case correspondence to a support case.  
Currently, only events with an `event-name` of `AddCommunicationToCase` will contain have this value.

**Example Support Case Update event example: Support case created**  <a name="event-detail-support-case-update.example-1"></a>

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

**Example Support Case Update event example: AWS Support replies to a support case**  <a name="event-detail-support-case-update.example-2"></a>

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

**Example Support Case Update event example: Support case resolved**  <a name="event-detail-support-case-update.example-3"></a>

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

**Example Support Case Update event example: Support case reopened**  <a name="event-detail-support-case-update.example-4"></a>

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