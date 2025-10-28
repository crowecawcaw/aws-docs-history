# Sending a message

The AWS End User Messaging Push API can send transactional push notifications to specific device identifiers.
This section contains complete code examples that you can use to send push notifications
through the AWS End User Messaging Push API by using an AWS SDK.

You can use these examples to send push notifications through any push notification
service that AWS End User Messaging Push supports. Currently, AWS End User Messaging Push supports the following channels: Firebase
Cloud Messaging (FCM), Apple Push Notification Service (APNs), Baidu Cloud Push, and Amazon
Device Messaging (ADM).

For more code examples on endpoints, segments, and channels see [Code examples](../../../pinpoint/latest/developerguide/service_code_examples.md "../../../pinpoint/latest/developerguide/service_code_examples.md").

###### Note

When you send push notifications through the Firebase Cloud Messaging (FCM) service,
use the service name `GCM` in your call to the AWS End User Messaging Push API. The Google Cloud
Messaging (GCM) service was discontinued by Google on April 10, 2018. However, the AWS End User Messaging Push
API uses the `GCM` service name for messages that it sends through the FCM
service in order to maintain compatibility with API code that was written prior to the
discontinuation of the GCM service.

GCM (AWS CLI)The following example uses [send-messages](../../../cli/latest/reference/pinpoint/send-messages.md "../../../cli/latest/reference/pinpoint/send-messages.md") to send a GCM Push notification with the AWS CLI. Replace
`token` with the unique token of the device and `611e3e3cdd47474c9c1399a50example` with your application identifier.

```
aws pinpoint send-messages \
--application-id `611e3e3cdd47474c9c1399a50example` \
--message-request file://myfile.json \
--region us-west-2

Contents of myfile.json:
{
  "Addresses": {
    "`token`": {
      "ChannelType" : 'GCM'
    }
  },
  "MessageConfiguration": {
    "GCMMessage": {
      "Action": "URL",
      "Body": "This is a sample message",
      "Priority": "normal",
      "SilentPush": True,
      "Title": "My sample message",
      "TimeToLive": 30,
      "Url": "https://www.example.com"
      }
  }
}
```

The following example uses [send-messages](../../../cli/latest/reference/pinpoint/send-messages.md "../../../cli/latest/reference/pinpoint/send-messages.md") to send a GCM Push notification, using all legacy keys, with the AWS CLI. Replace
`token` with the unique token of the device and `611e3e3cdd47474c9c1399a50example` with your application identifier.

```
aws pinpoint send-messages \
--application-id `611e3e3cdd47474c9c1399a50example` \
--message-request
'{
  "MessageConfiguration": {
    "GCMMessage":{
      "RawContent": "{\"notification\": {\n \"title\": \"string\",\n \"body\": \"string\",\n \"android_channel_id\": \"string\",\n \"body_loc_args\": [\n \"string\"\n ],\n \"body_loc_key\": \"string\",\n \"click_action\": \"string\",\n \"color\": \"string\",\n \"icon\": \"string\",\n \"sound\": \"string\",\n \"tag\": \"string\",\n \"title_loc_args\": [\n \"string\"\n ],\n \"title_loc_key\": \"string\"\n },\"data\":{\"message\":\"hello in data\"} }",
      "TimeToLive" : 309744
     }
   },
  "Addresses": {
    "`token`": {
      "ChannelType":"GCM"
      }
   }
}'
\ --region us-east-1
```

The following example uses [send-messages](../../../cli/latest/reference/pinpoint/send-messages.md "../../../cli/latest/reference/pinpoint/send-messages.md") to send a GCM Push notification with FCMv1 message payload using
the AWS CLI. Replace `token` with the unique token of the device
and `611e3e3cdd47474c9c1399a50example` with your application
identifier.

```
aws pinpoint send-messages \
--application-id 6a2dafd84bec449ea75fb773f4c41fa1 \
--message-request
'{
  "MessageConfiguration": {
    "GCMMessage":{
      "RawContent": "{\n \"fcmV1Message\": \n {\n \"message\" :{\n  \"notification\": {\n \"title\": \"string\",\n \"body\": \"string\"\n },\n \"android\": {\n \"priority\": \"high\",\n \"notification\": {\n \"title\": \"string\",\n \"body\": \"string\",\n \"icon\": \"string\",\n \"color\": \"string\",\n \"sound\": \"string\",\n \"tag\": \"string\",\n \"click_action\": \"string\",\n \"body_loc_key\": \"string\",\n \"body_loc_args\": [\n \"string\"\n ],\n \"title_loc_key\": \"string\",\n \"title_loc_args\": [\n \"string\"\n ],\n \"channel_id\": \"string\",\n \"ticker\": \"string\",\n \"sticky\": true,\n \"event_time\": \"2024-02-06T22:11:55Z\",\n \"local_only\": true,\n \"notification_priority\": \"PRIORITY_UNSPECIFIED\",\n \"default_sound\": false,\n \"default_vibrate_timings\": true,\n \"default_light_settings\": false,\n \"vibrate_timings\": [\n \"22s\"\n ],\n \"visibility\": \"VISIBILITY_UNSPECIFIED\",\n \"notification_count\": 5,\n \"light_settings\": {\n \"color\": {\n \"red\": 1,\n \"green\": 2,\n \"blue\": 3,\n \"alpha\": 6\n },\n \"light_on_duration\": \"112s\",\n \"light_off_duration\": \"1123s\"\n },\n \"image\": \"string\"\n },\n \"data\": {\n \"dataKey1\": \"priority message\",\n \"data_key_3\": \"priority message\",\n \"dataKey2\": \"priority message\",\n \"data_key_5\": \"priority message\"\n },\n \"ttl\": \"10023.32s\"\n },\n \"apns\": {\n \"payload\": {\n \"aps\": {\n \"alert\": {\n \"subtitle\": \"string\",\n \"title-loc-args\": [\n \"string\"\n ],\n \"title-loc-key\": \"string\",\n \"launch-image\": \"string\",\n \"subtitle-loc-key\": \"string\",\n \"subtitle-loc-args\": [\n \"string\"\n ],\n \"loc-args\": [\n \"string\"\n ],\n \"loc-key\": \"string\",\n \"title\": \"string\",\n \"body\": \"string\"\n },\n \"thread-id\": \"string\",\n \"category\": \"string\",\n \"content-available\": 1,\n \"mutable-content\": 1,\n \"target-content-id\": \"string\",\n \"interruption-level\": \"string\",\n \"relevance-score\": 25,\n \"filter-criteria\": \"string\",\n \"stale-date\": 6483,\n \"content-state\": {},\n \"timestamp\": 673634,\n \"dismissal-date\": 4,\n \"attributes-type\": \"string\",\n \"attributes\": {},\n \"sound\": \"string\",\n \"badge\": 5\n }\n }\n },\n \"webpush\": {\n \"notification\": {\n \"permission\": \"granted\",\n \"maxActions\": 2,\n \"actions\": [\n \"title\"\n ],\n \"badge\": \"URL\",\n \"body\": \"Hello\",\n \"data\": {\n \"hello\": \"hey\"\n },\n \"dir\": \"auto\",\n \"icon\": \"icon\",\n \"image\": \"image\",\n \"lang\": \"string\",\n \"renotify\": false,\n \"requireInteraction\": true,\n \"silent\": false,\n \"tag\": \"tag\",\n \"timestamp\": 1707259524964,\n \"title\": \"hello\",\n \"vibrate\": [\n 100,\n 200,\n 300\n ]\n },\n \"data\": {\n \"data1\": \"priority message\",\n \"data2\": \"priority message\",\n \"data12\": \"priority message\",\n \"data3\": \"priority message\"\n }\n },\n \"data\": {\n \"data7\": \"priority message\",\n \"data5\": \"priority message\",\n \"data8\": \"priority message\",\n \"data9\": \"priority message\"\n }\n }\n \n}\n}",
      "TimeToLive" : 309744
    }
  },
  "Addresses": {
    `token`: {
      "ChannelType":"GCM"
    }
   }
}'
\ --region us-east-1
```

if using `ImageUrl` field for GCM , pinpoint sends the field as data notification, with
the key being `pinpoint.notification.imageUrl`, which can prevent the image from being
rendered out of the box. Please use RawContent or add handling of the data keys such as
integrating your app with AWS Amplify.

Safari (AWS CLI)
You can use AWS End User Messaging Push to send messages to macOS computers that use Apple's Safari web browser.
To send a message to the Safari browser, you must specify the raw message content, and you
must include a specific attribute in the message payload. You can do this by [creating a push notification template with
a raw message payload](../../../pinpoint/latest/userguide/message-templates-creating-push.md#message-templates-creating-push-raw "../../../pinpoint/latest/userguide/message-templates-creating-push.md#message-templates-creating-push-raw"), or by specifying the raw message content directly in a
[campaign](../../../pinpoint/latest/userguide/campaigns-message.md#campaigns-message-push "../../../pinpoint/latest/userguide/campaigns-message.md#campaigns-message-push") message, in the _Amazon Pinpoint User Guide_.

###### Note

This special attribute is required for sending to macOS laptop and desktop computers
that use the Safari web browser. It isn't required for sending to iOS devices such as
iPhones and iPads.

To send a message to Safari web browsers, you must specify the raw message payload. The
raw message payload must include a `url-args` array within the `aps`
object. The `url-args` array is required in order to send push notifications to
the Safari web browser. However, it is acceptable for the array to contain a single, empty
element.

The following example uses [send-messages](../../../cli/latest/reference/pinpoint/send-messages.md "../../../cli/latest/reference/pinpoint/send-messages.md") to send a notification to the Safari web browser with the AWS CLI. Replace
`token` with the unique token of the device and `611e3e3cdd47474c9c1399a50example` with your application identifier.

```
aws pinpoint send-messages \
--application-id `611e3e3cdd47474c9c1399a50example` \
--message-request
'{
  "Addresses": {
    "`token`":
    {
      "ChannelType":"APNS"
    }
  },
  "MessageConfiguration": {
    "APNSMessage": {
        "RawContent":
          "{\"aps\": {\"alert\": { \"title\": \"Title of my message\", \"body\": \"This is a push notification for the Safari web browser.\"},\"content-available\": 1,\"url-args\": [\"\"]}}"
     }
  }
}'
\ --region us-east-1
```

For more information about Safari push notifications, see [Configuring Safari Push Notifications](https://developer.apple.com/library/archive/documentation/NetworkingInternet/Conceptual/NotificationProgrammingGuideForWebsites/PushNotifications/PushNotifications.html "https://developer.apple.com/library/archive/documentation/NetworkingInternet/Conceptual/NotificationProgrammingGuideForWebsites/PushNotifications/PushNotifications.html") on the Apple Developer website.

APNS (AWS CLI)The following example uses [send-messages](../../../cli/latest/reference/pinpoint/send-messages.md "../../../cli/latest/reference/pinpoint/send-messages.md") to send a APNS Push notification with the
AWS CLI. Replace
`token` with the unique token of the device, `611e3e3cdd47474c9c1399a50example` with your application identifier, and `GAME_INVITATION` with a unique identifier.

```
aws pinpoint send-messages \
--application-id `611e3e3cdd47474c9c1399a50example` \
--message-request
'{
    "Addresses": {
     "`token`":
    {
      "ChannelType":"APNS"
    }
  },
  "MessageConfiguration": {
    "APNSMessage": {
      "RawContent": "{\"aps\" : {\"alert\" : {\"title\" : \"Game Request\",\"subtitle\" : \"Five Card Draw\",\"body\" : \"Bob wants to play poker\"},\"category\" : \"`GAME_INVITATION`\"},\"gameID\" : \"12345678\"}"
      }
    }
}'
\ --region us-east-1
```

JavaScript (Node.js)
Use this example to send push notifications by using the AWS SDK for JavaScript in Node.js. This
example assumes that you've already installed and configured the SDK for JavaScript in Node.js.

This example also assumes that you're using a shared credentials file to
specify the Access Key and Secret Access Key for an existing user. For more
information, see [Setting
credentials](../../../sdk-for-javascript/v3/developer-guide/setting-credentials.md "../../../sdk-for-javascript/v3/developer-guide/setting-credentials.md") in the _AWS SDK for JavaScript in Node.js Developer
Guide_.

```
'use strict';

const AWS = require('aws-sdk');

// The AWS Region that you want to use to send the message. For a list of
// AWS Regions where the API is available
const region = 'us-east-1';

// The title that appears at the top of the push notification.
var title = 'Test message sent from End User Messaging Push.';

// The content of the push notification.
var message = 'This is a sample message sent from End User Messaging Push by using the '
            + 'AWS SDK for JavaScript in Node.js';

// The application ID that you want to use when you send this
// message. Make sure that the push channel is enabled for the project that
// you choose.
var applicationId = 'ce796be37f32f178af652b26eexample';

// An object that contains the unique token of the device that you want to send
// the message to, and the push service that you want to use to send the message.
var recipient = {
  'token': 'a0b1c2d3e4f5g6h7i8j9k0l1m2n3o4p5q6r7s8t9u0v1w2x3y4z5a6b7c8d8e9f0',
  'service': 'GCM'
  };

// The action that should occur when the recipient taps the message. Possible
// values are OPEN_APP (opens the app or brings it to the foreground),
// DEEP_LINK (opens the app to a specific page or interface), or URL (opens a
// specific URL in the device's web browser.)
var action = 'URL';

// This value is only required if you use the URL action. This variable contains
// the URL that opens in the recipient's web browser.
var url = 'https://www.example.com';

// The priority of the push notification. If the value is 'normal', then the
// delivery of the message is optimized for battery usage on the recipient's
// device, and could be delayed. If the value is 'high', then the notification is
// sent immediately, and might wake a sleeping device.
var priority = 'normal';

// The amount of time, in seconds, that the push notification service provider
// (such as FCM or APNS) should attempt to deliver the message before dropping
// it. Not all providers allow you specify a TTL value.
var ttl = 30;

// Boolean that specifies whether the notification is sent as a silent
// notification (a notification that doesn't display on the recipient's device).
var silent = false;

function CreateMessageRequest() {
  var token = recipient['token'];
  var service = recipient['service'];
  if (service == 'GCM') {
    var messageRequest = {
      'Addresses': {
        [token]: {
          'ChannelType' : 'GCM'
        }
      },
      'MessageConfiguration': {
        'GCMMessage': {
          'Action': action,
          'Body': message,
          'Priority': priority,
          'SilentPush': silent,
          'Title': title,
          'TimeToLive': ttl,
          'Url': url
        }
      }
    };
  } else if (service == 'APNS') {
    var messageRequest = {
      'Addresses': {
        [token]: {
          'ChannelType' : 'APNS'
        }
      },
      'MessageConfiguration': {
        'APNSMessage': {
          'Action': action,
          'Body': message,
          'Priority': priority,
          'SilentPush': silent,
          'Title': title,
          'TimeToLive': ttl,
          'Url': url
        }
      }
    };
  } else if (service == 'BAIDU') {
    var messageRequest = {
      'Addresses': {
        [token]: {
          'ChannelType' : 'BAIDU'
        }
      },
      'MessageConfiguration': {
        'BaiduMessage': {
          'Action': action,
          'Body': message,
          'SilentPush': silent,
          'Title': title,
          'TimeToLive': ttl,
          'Url': url
        }
      }
    };
  } else if (service == 'ADM') {
    var messageRequest = {
      'Addresses': {
        [token]: {
          'ChannelType' : 'ADM'
        }
      },
      'MessageConfiguration': {
        'ADMMessage': {
          'Action': action,
          'Body': message,
          'SilentPush': silent,
          'Title': title,
          'Url': url
        }
      }
    };
  }

  return messageRequest
}

function ShowOutput(data){
  if (data["MessageResponse"]["Result"][recipient["token"]]["DeliveryStatus"]
      == "SUCCESSFUL") {
    var status = "Message sent! Response information: ";
  } else {
    var status = "The message wasn't sent. Response information: ";
  }
  console.log(status);
  console.dir(data, { depth: null });
}

function SendMessage() {
  var token = recipient['token'];
  var service = recipient['service'];
  var messageRequest = CreateMessageRequest();

  // Specify that you're using a shared credentials file, and specify the
  // IAM profile to use.
  var credentials = new AWS.SharedIniFileCredentials({ profile: 'default' });
  AWS.config.credentials = credentials;

  // Specify the AWS Region to use.
  AWS.config.update({ region: region });

  //Create a new Pinpoint object.
  var pinpoint = new AWS.Pinpoint();
  var params = {
    "ApplicationId": applicationId,
    "MessageRequest": messageRequest
  };

  // Try to send the message.
  pinpoint.sendMessages(params, function(err, data) {
    if (err) console.log(err);
    else     ShowOutput(data);
  });
}

SendMessage()
```

Python
Use this example to send push notifications by using the AWS SDK for Python (Boto3). This
example assumes that you've already installed and configured the
SDK for Python (Boto3).

This example also assumes that you're using a shared credentials file to
specify the Access Key and Secret Access Key for an existing user. For
more information, see [Credentials](../../../sdk-for-javascript/v3/developer-guide/setting-credentials.md "../../../sdk-for-javascript/v3/developer-guide/setting-credentials.md") in the _AWS SDK for Python (Boto3) API Reference_.

```
import json
import boto3
from botocore.exceptions import ClientError

# The AWS Region that you want to use to send the message. For a list of
# AWS Regions where the API is available
region = "us-east-1"

# The title that appears at the top of the push notification.
title = "Test message sent from End User Messaging Push."

# The content of the push notification.
message = ("This is a sample message sent from End User Messaging Push by using the "
           "AWS SDK for Python (Boto3).")

# The application ID to use when you send this message.
# Make sure that the push channel is enabled for the project or application
# that you choose.
application_id = "ce796be37f32f178af652b26eexample"

# A dictionary that contains the unique token of the device that you want to send the
# message to, and the push service that you want to use to send the message.
recipient = {
    "token": "a0b1c2d3e4f5g6h7i8j9k0l1m2n3o4p5q6r7s8t9u0v1w2x3y4z5a6b7c8d8e9f0",
    "service": "GCM"
    }

# The action that should occur when the recipient taps the message. Possible
# values are OPEN_APP (opens the app or brings it to the foreground),
# DEEP_LINK (opens the app to a specific page or interface), or URL (opens a
# specific URL in the device's web browser.)
action = "URL"

# This value is only required if you use the URL action. This variable contains
# the URL that opens in the recipient's web browser.
url = "https://www.example.com"

# The priority of the push notification. If the value is 'normal', then the
# delivery of the message is optimized for battery usage on the recipient's
# device, and could be delayed. If the value is 'high', then the notification is
# sent immediately, and might wake a sleeping device.
priority = "normal"

# The amount of time, in seconds, that the push notification service provider
# (such as FCM or APNS) should attempt to deliver the message before dropping
# it. Not all providers allow you specify a TTL value.
ttl = 30

# Boolean that specifies whether the notification is sent as a silent
# notification (a notification that doesn't display on the recipient's device).
silent = False

# Set the MessageType based on the values in the recipient variable.
def create_message_request():

    token = recipient["token"]
    service = recipient["service"]

    if service == "GCM":
        message_request = {
            'Addresses': {
                token: {
                    'ChannelType': 'GCM'
                }
            },
            'MessageConfiguration': {
                'GCMMessage': {
                    'Action': action,
                    'Body': message,
                    'Priority' : priority,
                    'SilentPush': silent,
                    'Title': title,
                    'TimeToLive': ttl,
                    'Url': url
                }
            }
        }
    elif service == "APNS":
        message_request = {
            'Addresses': {
                token: {
                    'ChannelType': 'APNS'
                }
            },
            'MessageConfiguration': {
                'APNSMessage': {
                    'Action': action,
                    'Body': message,
                    'Priority' : priority,
                    'SilentPush': silent,
                    'Title': title,
                    'TimeToLive': ttl,
                    'Url': url
                }
            }
        }
    elif service == "BAIDU":
        message_request = {
            'Addresses': {
                token: {
                    'ChannelType': 'BAIDU'
                }
            },
            'MessageConfiguration': {
                'BaiduMessage': {
                    'Action': action,
                    'Body': message,
                    'SilentPush': silent,
                    'Title': title,
                    'TimeToLive': ttl,
                'Url': url
                }
            }
        }
    elif service == "ADM":
        message_request = {
            'Addresses': {
                token: {
                    'ChannelType': 'ADM'
                }
            },
            'MessageConfiguration': {
                'ADMMessage': {
                    'Action': action,
                    'Body': message,
                    'SilentPush': silent,
                    'Title': title,
                    'Url': url
                }
            }
        }
    else:
        message_request = None

    return message_request

# Show a success or failure message, and provide the response from the API.
def show_output(response):
    if response['MessageResponse']['Result'][recipient["token"]]['DeliveryStatus'] == "SUCCESSFUL":
        status = "Message sent! Response information:\n"
    else:
        status = "The message wasn't sent. Response information:\n"
    print(status, json.dumps(response,indent=4))

# Send the message through the appropriate channel.
def send_message():

    token = recipient["token"]
    service = recipient["service"]
    message_request = create_message_request()

    client = boto3.client('pinpoint',region_name=region)

    try:
        response = client.send_messages(
            ApplicationId=application_id,
            MessageRequest=message_request
        )
    except ClientError as e:
        print(e.response['Error']['Message'])
    else:
        show_output(response)

send_message()
```

## Additional resources

- For more information on Push channel templates, see [Creating push notification templates](../../../pinpoint/latest/userguide/message-templates-creating-push.md "../../../pinpoint/latest/userguide/message-templates-creating-push.md") in the _Amazon Pinpoint User Guide_.
