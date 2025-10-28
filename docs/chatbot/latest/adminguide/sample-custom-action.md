AWS Chatbot is now Amazon Q Developer. [Learn more](service-rename.md "service-rename.md")

# Sample use cases

This page includes examples of functional use cases for custom actions that you can leverage for your specific needs.

## Custom notifications metadata

You can use custom notifications to specify metadata for your custom actions. Custom actions display this information as variables that you define in the payload. Before you run a custom
action, you're shown a complete summary of that action and its payload. In the following example, a custom notification for allow listing an IP address contains an IP address as metadata:

```
{
    "version": "1.0",
    "source": "custom",
    "content": {
        "title": "IP Address Allowlist Request",
        "description": "We have received a request to allows list an IP address from 'sample@sample.com'."
    },
    "metadata": {
        "additionalContext": {
            "IPAddress": "192.168.0.1"
        }
    }
}
```

If you create a custom action based on this notification, `{"message": "I'ved allow listed IP address: $IPAddress"}` is shown as an available notification variable that you can use in your payload.
For example, the following Lambda action payload displays the message and the IP address variable.

```
{"message": "I'ved allow listed IP address: $IPAddress"}
```

## Recent Amazon CloudWatch Logs errors

The following example shows how you can use custom actions to display recent errors from an Amazon CloudWatch Logs group in your channel from an Amazon CloudWatch Logs notification.

The following Lambda function returns a list of the most common Amazon CloudWatch Logs errors:

```
import boto3
from collections import Counter
import json
import datetime

def extract_message(value):
  if value.startswith('{'):
    try:
      structured_message = json.loads(value)

      return structured_message.get('message', value)
    except Exception:
      pass

  return value

def take_ellipsis(value, length):
  if len(value) <= length:
    return value
  else:
    return value[:length - 1] + '…'

def lambda_handler(event, context):
  log_group_name = event['logGroup']
  lookback_minutes = int(event.get('minutes', 60))
  filter = event.get('filter', 'ERROR')
  limit = int(event.get('limit', 10))

  logs_client = boto3.client('logs')

  now = datetime.datetime.now()
  offset = now - datetime.timedelta(minutes=lookback_minutes)
  print(offset)
  start_time = int(offset.timestamp() * 1000)
  end_time = int(now.timestamp() * 1000)

  response = logs_client.filter_log_events(
    logGroupName=log_group_name,
    startTime=start_time,
    endTime=end_time,
    filterPattern=filter
  )

  messages = [extract_message(event['message']) for event in response['events']]

  message_counts = Counter(messages)

  top_messages = message_counts.most_common(limit)

  if top_messages:
    formatted_messages = [
      f'{index + 1}. `{take_ellipsis(message[0], 100)}` ({message[1]} occurrences)' for index, error in enumerate(top_messages)
    ]
    message_summary = '\n'.join(formatted_messages)

    return f'*Most common errors in `{log_group_name}` within the last hour*\n\n' + message_summary
  else:
    return f'Found no errors matching filter within the last {lookback_minutes} minutes in {log_group_name}'

```

You can create a Lambda action that invokes this Lambda function and view errors for specific log groups by choosing this function while creating your action and entering the following as the payload:

```
{
    "logGroup": "$LogGroup"
}
```
