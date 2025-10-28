# Alerting Notification

Channels API

Use the Alerting Notification Channels API to create, update, delete, and retrieve
notification channels.

The identifier (id) of a notification channel is an auto-incrementing numeric value
and is only unique per workspace. The unique identifier (uid) of a notification channel
can be used to uniquely identify a folder between multiple workspaces. It’s
automatically generated if you don't provide one when you create a notification channel.
The uid allows having consistent URLs for accessing notification channels and when
synchronizing notification channels between multiple Amazon Managed Grafana workspaces.

###### Note

To use a Grafana API with your Amazon Managed Grafana workspace, you must have a valid Grafana
API token. You include this in the `Authorization` field in the API
request. For information about how to create a token to authenticate your API calls,
see [Authenticate with tokens](authenticating-grafana-apis.md "authenticating-grafana-apis.md").

## Get all notification

channels

Returns all notification channels that the authenticated user has permission to
view.

```
GET /api/alert-notifications
```

**Example request**

```
GET /api/alert-notifications HTTP/1.1
Accept: application/json
Content-Type: application/json
Authorization: Bearer 1234abcd567exampleToken890
```

**Example response**

```
HTTP/1.1 200
Content-Type: application/json

[
  {
    "id": 1,
    "uid": "sns-uid",
    "name": "test",
    "type": "sns",
    "isDefault": false,
    "sendReminder": false,
    "disableResolveMessage": false,
    "frequency": "",
    "created": "2023-09-08T19:57:56Z",
    "updated": "2023-09-08T19:57:56Z",
    "settings": {
      "authProvider": "default",
      "autoResolve": true,
      "httpMethod": "POST",
      "messageFormat": "json",
      "severity": "critical",
      "topic": "<SNS-TOPIC-ARN>",
      "uploadImage": false
    },
    "secureFields": {}
  }
]
```

## Get all

notification channels (lookup)

Returns all notification channels, but with less detailed information. Accessible
by any authenticated user and is mainly used to provide alert notification channels
in the Grafana workspace console UI when configuring alert rules.

```
GET /api/alert-notifications/lookup
```

**Example request**

```
GET /api/alert-notifications/lookup HTTP/1.1
Accept: application/json
Content-Type: application/json
Authorization: Bearer 1234abcd567exampleToken890
```

**Example response**

```
HTTP/1.1 200
Content-Type: application/json

[
  {
    "id": 1,
    "uid": "sns-uid",
    "name": "test",
    "type": "sns",
    "isDefault": false
  },
  {
    "id": 2,
    "uid": "slack-uid",
    "name": "Slack",
    "type": "slack",
    "isDefault": false
  }
]
```

## Get all

notification channels by UID

```
GET /api/alert-notifications/uid/:uid
```

**Example request**

```
GET /api/alert-notifications/uid/sns-uid HTTP/1.1
Accept: application/json
Content-Type: application/json
Authorization: Bearer 1234abcd567exampleToken890
```

**Example response**

```
HTTP/1.1 200
Content-Type: application/json

{
  "id": 1,
  "uid": "sns-uid",
  "name": "test",
  "type": "sns",
  "isDefault": false,
  "sendReminder": false,
  "disableResolveMessage": false,
  "frequency": "",
  "created": "2023-09-08T19:57:56Z",
  "updated": "2023-09-08T19:57:56Z",
  "settings": {
    "authProvider": "default",
    "autoResolve": true,
    "httpMethod": "POST",
    "messageFormat": "json",
    "severity": "critical",
    "topic": "<SNS-TOPIC-ARN>",
    "uploadImage": false
  },
  "secureFields": {}
}
```

## Get all notification

channels by Id

```
GET /api/alert-notifications/:id
```

**Example request**

```
GET /api/alert-notifications/1 HTTP/1.1
Accept: application/json
Content-Type: application/json
Authorization: Bearer 1234abcd567exampleToken890
```

**Example response**

```
HTTP/1.1 200
Content-Type: application/json

{
  "id": 1,
  "uid": "sns-uid",
  "name": "test",
  "type": "sns",
  "isDefault": false,
  "sendReminder": false,
  "disableResolveMessage": false,
  "frequency": "",
  "created": "2023-09-08T19:57:56Z",
  "updated": "2023-09-08T19:57:56Z",
  "settings": {
    "authProvider": "default",
    "autoResolve": true,
    "httpMethod": "POST",
    "messageFormat": "json",
    "severity": "critical",
    "topic": "<SNS-TOPIC-ARN>",
    "uploadImage": false
  },
  "secureFields": {}
}
```

## Create notification

channel

To see what notification channels are supported by Amazon Managed Grafana, see the list of
supported notifiers in [Working with contact points](alert-contact-points.md "alert-contact-points.md").

```
POST /api/alert-notifications
```

**Example request**

```
POST /api/alert-notifications HTTP/1.1
Accept: application/json
Content-Type: application/json
Authorization: Bearer 1234abcd567exampleToken890

{
  "uid": "new-sns-uid", // optional
  "name": "sns alert notification",  //Required
  "type":  "sns", //Required
  "isDefault": false,
  "sendReminder": false,
  "settings": {
    "authProvider": "default",
    "autoResolve": true,
    "httpMethod": "POST",
    "messageFormat": "json",
    "severity": "critical",
    "topic": "<SNS-TOPIC-ARN>",
    "uploadImage": false
  }
}
```

**Example response**

```
HTTP/1.1 200
Content-Type: application/json

{
  "id": 1,
  "uid": "new-sns-uid",
  "name": "sns alert notification",
  "type": "sns",
  "isDefault": false,
  "sendReminder": false,
  "settings": {
    "authProvider": "default",
    "autoResolve": true,
    "httpMethod": "POST",
    "messageFormat": "json",
    "severity": "critical",
    "topic": "<SNS-TOPIC-ARN>",
    "uploadImage": false
  },
  "created": "2018-04-23T14:44:09+02:00",
  "updated": "2018-08-20T15:47:49+02:00"
}
```

## Update

notification channel by UID

```
PUT /api/alert-notifications/uid/:uid
```

**Example request**

```
PUT /api/alert-notifications/uid/sns-uid HTTP/1.1
Accept: application/json
Content-Type: application/json
Authorization: Bearer 1234abcd567exampleToken890

{
  "uid": "sns-uid", // optional
  "name": "sns alert notification",  //Required
  "type":  "sns", //Required
  "isDefault": false,
  "sendReminder": true,
  "frequency": "15m",
  "settings": {
    "authProvider": "default",
    "autoResolve": true,
    "httpMethod": "POST",
    "messageFormat": "json",
    "severity": "critical",
    "topic": "<SNS-TOPIC-ARN>",
    "uploadImage": false
  }
}
```

**Example response**

```
HTTP/1.1 200
Content-Type: application/json

{
  "id": 1,
  "uid": "sns-uid",
  "name": "sns alert notification",
  "type": "sns",
  "isDefault": false,
  "sendReminder": true,
  "frequency": "15m",
  "settings": {
    "authProvider": "default",
    "autoResolve": true,
    "httpMethod": "POST",
    "messageFormat": "json",
    "severity": "critical",
    "topic": "<SNS-TOPIC-ARN>",
    "uploadImage": false
  },
  "created": "2017-01-01 12:34",
  "updated": "2017-01-01 12:34"
}
```

## Update

notification channel by Id

```
PUT /api/alert-notifications/:id
```

**Example request**

```
PUT /api/alert-notifications/1 HTTP/1.1
Accept: application/json
Content-Type: application/json
Authorization: Bearer 1234abcd567exampleToken890

{
  "id": 1,
  "uid": "sns-uid", // optional
  "name": "sns alert notification",  //Required
  "type":  "sns", //Required
  "isDefault": false,
  "sendReminder": true,
  "frequency": "15m",
  "settings": {
    "authProvider": "default",
    "autoResolve": true,
    "httpMethod": "POST",
    "messageFormat": "json",
    "severity": "critical",
    "topic": "<SNS-TOPIC-ARN>",
    "uploadImage": false
  }
}
```

**Example response**

```
HTTP/1.1 200
Content-Type: application/json

{
  "id": 1,
  "uid": "sns-uid",
  "name": "sns alert notification",
  "type": "sns",
  "isDefault": false,
  "sendReminder": true,
  "frequency": "15m",
  "settings": {
    "authProvider": "default",
    "autoResolve": true,
    "httpMethod": "POST",
    "messageFormat": "json",
    "severity": "critical",
    "topic": "<SNS-TOPIC-ARN>",
    "uploadImage": false
  },
  "created": "2017-01-01 12:34",
  "updated": "2017-01-01 12:34"
}
```

## Delete

notification channel by UID

```
DELETE /api/alert-notifications/uid/:uid
```

**Example request**

```
DELETE /api/alert-notifications/uid/sns-uid HTTP/1.1
Accept: application/json
Content-Type: application/json
Authorization: Bearer 1234abcd567exampleToken890
```

**Example response**

```
HTTP/1.1 200
Content-Type: application/json

{
  "message": "Notification deleted"
}
```

## Delete

notification channel by Id

```
DELETE /api/alert-notifications/:id
```

**Example request**

```
DELETE /api/alert-notifications/1 HTTP/1.1
Accept: application/json
Content-Type: application/json
Authorization: Bearer 1234abcd567exampleToken890
```

**Example response**

```
HTTP/1.1 200
Content-Type: application/json

{
  "message": "Notification deleted"
}
```

## Test notification

channel

Sends a test notification message for the given notification channel type and
settings.

```
POST /api/alert-notifications/test
```

**Example request**

```
POST /api/alert-notifications/test HTTP/1.1
Accept: application/json
Content-Type: application/json
Authorization: Bearer 1234abcd567exampleToken890

{
  "type":  "sns",
  "settings": {
    "authProvider": "default",
    "autoResolve": true,
    "httpMethod": "POST",
    "messageFormat": "json",
    "severity": "critical",
    "topic": "<SNS-TOPIC-ARN>",
    "uploadImage": false
  }
}
```

**Example response**

```
HTTP/1.1 200
Content-Type: application/json

{
  "message": "Test notification sent"
}
```
