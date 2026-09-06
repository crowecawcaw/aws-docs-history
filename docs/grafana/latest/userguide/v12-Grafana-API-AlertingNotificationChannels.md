

# Alerting Notification Channels API
<a name="v12-Grafana-API-AlertingNotificationChannels"></a>

Use the Alerting Notification Channels API to create, update, delete, and retrieve notification channels.

The identifier (id) of a notification channel is an auto-incrementing numeric value and is only unique per workspace. The unique identifier (uid) of a notification channel can be used to uniquely identify a folder between multiple workspaces. It’s automatically generated if you don't provide one when you create a notification channel. The uid allows having consistent URLs for accessing notification channels and when synchronizing notification channels between multiple Amazon Managed Grafana workspaces. 

**Note**  
To use a Grafana API with your Amazon Managed Grafana workspace, you must have a valid service account token. You include this in the `Authorization` field in the API request.

## Get all notification channels
<a name="v12-Grafana-API-AlertNotificationChannels-getall"></a>

Returns all notification channels that the authenticated user has permission to view.

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

## Get all notification channels (lookup)
<a name="v12-Grafana-API-AlertNotificationChannels-getlookup"></a>

Returns all notification channels, but with less detailed information. Accessible by any authenticated user and is mainly used to provide alert notification channels in the Grafana workspace console UI when configuring alert rules.

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

## Get all notification channels by UID
<a name="v12-Grafana-API-AlertNotificationChannels-getbyUID"></a>

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

## Get all notification channels by Id
<a name="v12-Grafana-API-AlertNotificationChannels-getbyId"></a>

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

## Create notification channel
<a name="v12-Grafana-API-AlertNotificationChannels-Create"></a>

To see what notification channels are supported by Amazon Managed Grafana, see the list of supported notifiers in [Working with contact points](alert-contact-points.md).

In Grafana version 12, use the Alerting Provisioning API to create contact points. The legacy `/api/alert-notifications` endpoint is no longer available.

**Example request**

```
POST /api/v1/provisioning/contact-points HTTP/1.1
Accept: application/json
Content-Type: application/json
Authorization: Bearer 1234abcd567exampleToken890

{
  "uid": "new-sns-uid",
  "name": "sns alert notification",
  "type": "sns",
  "isDefault": false,
  "sendReminder": false,
  "settings": {
    "topic_arn": "<SNS-TOPIC-ARN>",
    "subject": "<SUBJECT>"
  }
}
```

## Update notification channel by UID
<a name="v12-Grafana-API-AlertNotificationChannels-UpdatebyUID"></a>

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

## Update notification channel by Id
<a name="v12-Grafana-API-AlertNotificationChannels-UpdatebyId"></a>

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

## Delete notification channel by UID
<a name="v12-Grafana-API-AlertNotificationChannels-DeletebyUID"></a>

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

## Delete notification channel by Id
<a name="v12-Grafana-API-AlertNotificationChannels-DeletebyId"></a>

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

## Test notification channel
<a name="v12-Grafana-API-AlertNotificationChannels-Test"></a>

Sends a test notification message for the given notification channel type and settings.

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