# Recording multiple action interaction events

The following code shows how to record multiple action interaction events for the same user with the same sessionId.

**Corresponding Action interactions dataset**

```
USER_ID, ACTION_ID, EVENT_TYPE, TIMESTAMP
user123, action123, Taken, 1543531139
user123, action345, Not Taken, 1543531139
```

AWS CLI

```
aws personalize-events put-action-interactions \
--tracking-id 6ddfe6b7-cd83-4dd4-b09d-4c35ecbacfe1 \
--action-interactions '[{
  "userId": "`user123`",
  "sessionId": "`abcdefg`",
  "timestamp": `1543531139`,
  "eventType": "`Taken`",
  "actionId": "`action123`"
},
{
  "userId": "`user123`",
  "sessionId": "`abcdefg`",
  "timestamp": `1543531139`,
  "eventType": "`Not Taken`",
  "actionId": "`action345`"}]'
```

SDK for Python (Boto3)

```
import boto3

personalize_events = boto3.client(service_name='personalize-events')

response = personalize_events.put_action_interactions(
  trackingId='`12345678-xxxx-xxxx-xxxx-xxxxxxxxxxxx`',
  actionInteractions=[{
    'userId': '`user123`',
    'sessionId': '`abcdefg`',
    'timestamp': `1697848587`,
    'eventType': '`Taken`',
    'actionId': '`action123`'
  },
  {
    'userId': '`user123`',
    'sessionId': '`abcdefg`',
    'timestamp': `1697848622`,
    'eventType': '`Not Taken`',
    'actionId': '`action345`'
  }]
)
```
