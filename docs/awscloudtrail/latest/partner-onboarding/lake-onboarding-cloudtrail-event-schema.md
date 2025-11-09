# Understanding the CloudTrail Lake event schema

The tables in this section describe the required and optional schema elements that match
those in CloudTrail event records. The contents of `eventData` are provided by
customer events; other fields are provided by CloudTrail after customer events are
ingested.

- [Fields that are provided by CloudTrail after
  ingestion](#fields-cloudtrail "#fields-cloudtrail")
- [Fields that are provided by your
  events](#fields-event "#fields-event")
  The following fields are provided by CloudTrail after ingestion:

| Field name         | Input type | Requirement | Description                                                                                                                                                                                                 |
| ------------------ | ---------- | ----------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| eventVersion       | string     | Required    | The event version.                                                                                                                                                                                          |
| eventCategory      | string     | Required    | The event category. For non-AWS events, the value is<br>`ActivityAuditLog`.                                                                                                                                 |
| eventType          | string     | Required    | The event type. For non-AWS events, the valid value is<br>`ActivityLog`.                                                                                                                                    |
| eventID            | string     | Required    | A unique ID for an event.                                                                                                                                                                                   |
| eventTime          | string     | Required    | Event timestamp, in `yyyy-MM-DDTHH:mm:ss` format, in<br>Universal Coordinated Time (UTC).                                                                                                                   |
| awsRegion          | string     | Required    | The AWS Region where the `PutAuditEvents` call was<br>made.                                                                                                                                                 |
| recipientAccountId | string     | Required    | Represents the account ID that received this event. CloudTrail populates<br>this field by calculating it from event payload.                                                                                |
| addendum           | -          | Optional    | Shows information about why event processing was delayed. If information<br>was missing from an existing event, the addendum block includes the<br>missing information and a reason for why it was missing. |
| • reason           | string     | Optional    | The reason that the event or some of its contents were<br>missing.                                                                                                                                          |
| • updatedFields    | string     | Optional    | The event record fields that are updated by the addendum. This is<br>only provided if the reason is `UPDATED_DATA`.                                                                                         |
| • originalUID      | string     | Optional    | The original event UID from the source. This is only provided if<br>the reason is `UPDATED_DATA`.                                                                                                           |
| • originalEventID  | string     | Optional    | The original event ID. This is only provided if the reason is<br>`UPDATED_DATA`.                                                                                                                            |
| metadata           | -          | Required    | Information about the channel that the event used.                                                                                                                                                          |
| • ingestionTime    | string     | Required    | The timestamp when the event was processed, in `yyyy-MM-DDTHH:mm:ss`<br>format, in Universal Coordinated Time (UTC).                                                                                        |
| • channelARN       | string     | Required    | The ARN of the channel that the event used.                                                                                                                                                                 |

The following fields are provided by customer events:

| Field name            | Input type  | Requirement | Description                                                                                                                                                                         |
| --------------------- | ----------- | ----------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| eventData             | -           | Required    | The audit data sent to CloudTrail in a `PutAuditEvents` call.                                                                                                                       |
| • version             | string      | Required    | The version of the event from its source.<br>Length constraints: Maximum length of 256.                                                                                             |
| • userIdentity        | -           | Required    | Information about the user who made a request.                                                                                                                                      |
| • + type              | string      | Required    | The type of user identity.<br>Length constraints: Maximum length of 128.                                                                                                            |
| • + principalId       | string      | Required    | A unique identifier for the actor of the event.<br>Length constraints: Maximum length of 1024.                                                                                      |
| • + details           | JSON object | Optional    | Additional information about the identity.                                                                                                                                          |
| • userAgent           | string      | Optional    | The agent through which the request was made.<br>Length constraints: Maximum length of 1024.                                                                                        |
| • eventSource         | string      | Required    | This is the partner event source, or the custom<br>application about which events are logged.<br>Length constraints: Maximum length of 1024.                                        |
| • eventName           | string      | Required    | The requested action, one of the actions in the API for the source<br>service or application.<br>Length constraints: Maximum length of 1024.                                        |
| • eventTime           | string      | Required    | Event timestamp, in `yyyy-MM-DDTHH:mm:ss` format, in<br>Universal Coordinated Time (UTC).                                                                                           |
| • UID                 | string      | Required    | The UID value that identifies the request. The service or<br>application that is called generates this value.<br>Length constraints: Maximum length of 1024.                        |
| • requestParameters   | JSON object | Optional    | The parameters, if any, that were sent with the request. This<br>field has a maximum size of 100 kB, and content exceeding the limit<br>is rejected.                                |
| • responseElements    | JSON object | Optional    | The response element for actions that make changes (create,<br>update, or delete actions). This field has a maximum size of 100 kB, and content<br>exceeding the limit is rejected. |
| • errorCode           | string      | Optional    | A string representing an error for the event.<br>Length constraints: Maximum length of 256.                                                                                         |
| • errorMessage        | string      | Optional    | The description of the error.<br>Length constraints: Maximum length of 256.                                                                                                         |
| • sourceIPAddress     | string      | Optional    | The IP address from which the request was made. Both IPv4 and IPv6 addresses are accepted.                                                                                          |
| • recipientAccountId  | string      | Required    | Represents the account ID that received this event. The account ID must be the same as the AWS account ID that owns the channel.                                                    |
| • additionalEventData | JSON object | Optional    | Additional data about the event that was not part of the request<br>or response. This field has a maximum size of 28 kB, and content<br>exceeding that limit is rejected.           |

The following example shows the hierarchy of schema elements that match those in
CloudTrail event records.

```
{
    "eventVersion": String,
    "eventCategory": String,
    "eventType": String,
    "eventID": String,
    "eventTime": String,
    "awsRegion": String,
    "recipientAccountId": String,
    "addendum": {
       "reason": String,
       "updatedFields": String,
       "originalUID": String,
       "originalEventID": String
    },
    "metadata" : {
       "ingestionTime": String,
       "channelARN": String
    },
    "eventData": {
        "version": String,
        "userIdentity": {
          "type": String,
          "principalId": String,
          "details": {
             JSON
          }
        },
        "userAgent": String,
        "eventSource": String,
        "eventName": String,
        "eventTime": String,
        "UID": String,
        "requestParameters": {
           JSON
        },
        "responseElements": {
           JSON
        },
        "errorCode": String,
        "errorMessage": String,
        "sourceIPAddress": String,
        "recipientAccountId": String,
        "additionalEventData": {
           JSON
        }
    }
}
```
