# Using Google Firebase Cloud Messaging v1 payloads in

Amazon SNS

Amazon SNS supports using FCM HTTP v1 API to send notifications to Android, iOS, and Webpush
destinations. This topic provides examples of the payload structure when publishing mobile push
notifications using the CLI, or the Amazon SNS API.

You can include the following message types in your payload when sending an FCM
notification:

- **Data message** – A data message is handled by your
  client app and contains custom key-value pairs. When constructing a data message, you must
  include the `data` key with a JSON object as the value, and then enter your
  custom key-value pairs.
- **Notification message** or **display
  message** – A notification message contains a predefined set of keys
  handled by the FCM SDK. These keys vary depending on the device type to which you are
  delivering. For more information on platform-specific notification keys, see the
  following:

      + [Android
       notification keys](https://firebase.google.com/docs/reference/fcm/rest/v1/projects.messages "https://firebase.google.com/docs/reference/fcm/rest/v1/projects.messages")
      + [APNS notification keys](https://developer.apple.com/documentation/usernotifications/generating-a-remote-notification "https://developer.apple.com/documentation/usernotifications/generating-a-remote-notification")
      + [Webpush
       notification keys](https://developer.mozilla.org/en-US/docs/Web/API/Notification "https://developer.mozilla.org/en-US/docs/Web/API/Notification")

  For more information about FCM message types, see [Message types](https://firebase.google.com/docs/cloud-messaging/concept-options#notifications_and_data_messages "https://firebase.google.com/docs/cloud-messaging/concept-options#notifications_and_data_messages") in the in Google's _Firebase_
  documentation.

## Using the FCM v1 payload structure to send

messages

If you are creating an FCM application for the first time, or wish to take advantage of
FCM v1 features, you can opt-in to send an FCM v1 formatted payload. To do this, you must
include the top-level key `fcmV1Message`. For more information about constructing
FCM v1 payloads, see [Migrate from legacy FCM
APIs to HTTP v1](https://firebase.google.com/docs/cloud-messaging/migrate-v1 "https://firebase.google.com/docs/cloud-messaging/migrate-v1") and [Customizing a message across platforms](https://firebase.google.com/docs/cloud-messaging/concept-options#customizing-a-message-across-platforms "https://firebase.google.com/docs/cloud-messaging/concept-options#customizing-a-message-across-platforms") in Google's _Firebase_ documentation.

**FCM v1 example payload sent to Amazon SNS:**

###### Note

The `GCM` key value used in the following example must be encoded as a String
when publishing a notification using Amazon SNS.

```
{
  "GCM": "{
    \"fcmV1Message\": {
      \"validate_only\": false,
      \"message\": {
        \"notification\": {
          \"title\": \"string\",
          \"body\": \"string\"
        },
        \"data\": {
          \"dataGen\": \"priority message\"
        },
        \"android\": {
          \"priority\": \"high\",
          \"notification\": {
            \"body_loc_args\": [\"string\"],
            \"title_loc_args\": [\"string\"],
            \"sound\": \"string\",
            \"title_loc_key\": \"string\",
            \"title\": \"string\",
            \"body\": \"string\",
            \"click_action\": \"clicky_clacky\",
            \"body_loc_key\": \"string\"
          },
          \"data\": {
            \"dataAndroid\": \"priority message\"
          },
          \"ttl\": \"10023.32s\"
        },
        \"apns\": {
          \"payload\": {
            \"aps\": {
              \"alert\": {
                \"subtitle\": \"string\",
                \"title-loc-args\": [\"string\"],
                \"title-loc-key\": \"string\",
                \"loc-args\": [\"string\"],
                \"loc-key\": \"string\",
                \"title\": \"string\",
                \"body\": \"string\"
              },
              \"category\": \"Click\",
              \"content-available\": 0,
              \"sound\": \"string\",
              \"badge\": 5
            }
          }
        },
        \"webpush\": {
          \"notification\": {
            \"badge\": \"5\",
            \"title\": \"string\",
            \"body\": \"string\"
          },
          \"data\": {
            \"dataWeb\": \"priority message\"
          }
        }
      }
    }
  }"
}
```

When sending a JSON payload, be sure to include the `message-structure`
attribute in your request, and set it to `json`.

**CLI example:**

```
aws sns publish --topic $TOPIC_ARN --message '{"GCM": "{\"fcmV1Message\": {\"message\":{\"notification\":{\"title\":\"string\",\"body\":\"string\"},\"android\":{\"priority\":\"high\",\"notification\":{\"title\":\"string\",\"body\":\"string\"},\"data\":{\"customAndroidDataKey\":\"custom key value\"},\"ttl\":\"0s\"},\"apns\":{\"payload\":{\"aps\":{\"alert\":{\"title\":\"string\", \"body\":\"string\"},\"content-available\":1,\"badge\":5}}},\"webpush\":{\"notification\":{\"badge\":\"URL\",\"body\":\"Test\"},\"data\":{\"customWebpushDataKey\":\"priority message\"}},\"data\":{\"customGeneralDataKey\":\"priority message\"}}}}", "default": "{\"notification\": {\"title\": \"test\"}"}' --region $REGION --message-structure json
```

For more information on sending FCM v1 formatted payloads, see the following in Google's
_Firebase_ documentation:

- [Migrate from
  legacy FCM APIs to HTTP v1](https://firebase.google.com/docs/cloud-messaging/migrate-v1 "https://firebase.google.com/docs/cloud-messaging/migrate-v1")
- [About FCM messages](https://firebase.google.com/docs/cloud-messaging/concept-options#customizing_a_message_across_platforms "https://firebase.google.com/docs/cloud-messaging/concept-options#customizing_a_message_across_platforms")
- [REST Resource: projects.messages](https://firebase.google.com/docs/reference/fcm/rest/v1/projects.messages "https://firebase.google.com/docs/reference/fcm/rest/v1/projects.messages")

## Using the legacy payload structure to

send messages to the FCM v1 API

When migrating to FCM v1, you don't have to change the payload structure that you were
using for your legacy credentials. Amazon SNS transforms your payload into the new FCM v1 payload
structure, and sends to Google.

Input message payload format:

```
{
  "GCM": "{\"notification\": {\"title\": \"string\", \"body\": \"string\", \"android_channel_id\": \"string\", \"body_loc_args\": [\"string\"], \"body_loc_key\": \"string\", \"click_action\": \"string\", \"color\": \"string\", \"icon\": \"string\", \"sound\": \"string\", \"tag\": \"string\", \"title_loc_args\": [\"string\"], \"title_loc_key\": \"string\"}, \"data\": {\"message\": \"priority message\"}}"
}
```

Message sent to Google:

```
{
  "message": {
    "token": "***",
    "notification": {
      "title": "string",
      "body": "string"
    },
    "android": {
      "priority": "high",
      "notification": {
        "body_loc_args": [
          "string"
        ],
        "title_loc_args": [
          "string"
        ],
        "color": "string",
        "sound": "string",
        "icon": "string",
        "tag": "string",
        "title_loc_key": "string",
        "title": "string",
        "body": "string",
        "click_action": "string",
        "channel_id": "string",
        "body_loc_key": "string"
      },
      "data": {
        "message": "priority message"
      }
    },
    "apns": {
      "payload": {
        "aps": {
          "alert": {
            "title-loc-args": [
              "string"
            ],
            "title-loc-key": "string",
            "loc-args": [
              "string"
            ],
            "loc-key": "string",
            "title": "string",
            "body": "string"
          },
          "category": "string",
          "sound": "string"
        }
      }
    },
    "webpush": {
      "notification": {
        "icon": "string",
        "tag": "string",
        "body": "string",
        "title": "string"
      },
      "data": {
        "message": "priority message"
      }
    },
    "data": {
      "message": "priority message"
    }
  }
}
```

**Potential risks**

- Legacy to v1 mapping doesn't support the Apple Push Notification Service (APNS)
  `headers` or the `fcm_options` keys. If you'd like to use these
  fields, send an FCM v1 payload.
- In some cases, message headers are required by FCM v1 to send silent notifications to
  your APNs devices. If you are currently sending silent notifications to your APNs devices,
  they will not work with the legacy approach. Instead, we recommend using the FCM v1
  payload to avoid unexpected issues. To find a list of APNs headers and what they are used
  for, see [Communicating with APNs](https://developer.apple.com/library/archive/documentation/NetworkingInternet/Conceptual/RemoteNotificationsPG/CommunicatingwithAPNs.html "https://developer.apple.com/library/archive/documentation/NetworkingInternet/Conceptual/RemoteNotificationsPG/CommunicatingwithAPNs.html") in the _Apple Developer
  Guide_.
- If you are using the `TTL` Amazon SNS attribute when sending your notification,
  it will only be updated in the `android` field. If you'd like to set the
  `TTL` APNS attribute, use the FCM v1 payload.
- The `android`, `apns`, and `webpush` keys will be
  mapped and populated with all relevant keys provided. For example, if you provide
  `title`, which is a key shared among all three platforms, the FCM v1
  mapping will populate all three platforms with the title you provided.
- Some shared keys among platforms expect different value types. For example, the
  `badge` key passed to `apns` expects an integer value, while the
  `badge` key passed to `webpush` expects a String value. In cases
  where you provide the `badge` key, the FCM v1 mapping will only populate the
  key for which you provided a valid value.

## FCM delivery failure events

The following table provides the Amazon SNS failure type that corresponds to the error/status
codes received from Google for FCM v1 notification requests. All observed error codes
received from the FCM v1 API are available to you in CloudWatch when you set-up [delivery status logging](topics-attrib.md "topics-attrib.md") for your application.

| FCM error/status code    | Amazon SNS failure type | Failure message                                                             | Cause and mitigation                                                                                                                                                                                                                                                                                                                            |
| ------------------------ | ----------------------- | --------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `UNREGISTERED`           | `InvalidPlatformToken`  | Platform token associated with the endpoint is not valid.                   | The device token attached to your endpoint is stale or invalid. Amazon SNS disabled your endpoint. Update the Amazon SNS endpoint to the newest device token.                                                                                                                                                                                   |
| `INVALID_ARGUMENT`       | `InvalidNotification`   | Notification body is invalid.                                               | The device token or message payload may be invalid. Verify that your message payload is valid. If the message payload is valid, update the Amazon SNS endpoint to the newest device token.                                                                                                                                                      |
| `SENDER_ID_MISMATCH`     | `InvalidPlatformToken`  | Platform token associated with the endpoint is not valid.                   | The platform application associated with the device token doesn't have permission to send to the device token. Verify that you are using the correct FCM credentials in your Amazon SNS platform application.                                                                                                                                   |
| `UNAVAILABLE`            | `DependencyUnavailable` | Dependency is not available.                                                | FCM couldn't process the request in time. All the retries executed by Amazon SNS have failed. You can store these messages in a dead-letter queue (DLQ) and redrive them later.                                                                                                                                                                 |
| `INTERNAL`               | `UnexpectedFailure`     | Unexpected failure; please contact Amazon. Failure phrase [Internal Error]. | The FCM server encountered an error while trying to process your request. All the retries executed by Amazon SNS have failed. You can store these messages in a dead-letter queue (DLQ) and redrive them later.                                                                                                                                 |
| `THIRD_PARTY_AUTH_ERROR` | `InvalidCredentials`    | Platform application credentials are not valid.                             | A message targeted to an iOS device or a Webpush device could not be sent. Verify that your development and production credentials are valid.                                                                                                                                                                                                   |
| `QUOTA_EXCEEDED`         | `Throttled`             | Request throttled by [gcm].                                                 | A message rate quota, device message rate quota, or topic message rate quota has been exceeded. For information on how to resolve this issue, see [ErrorCode](https://firebase.google.com/docs/reference/fcm/rest/v1/ErrorCode "https://firebase.google.com/docs/reference/fcm/rest/v1/ErrorCode") in the in Google's _Firebase_ documentation. |
| `PERMISSION_DENIED`      | `InvalidNotification`   | Notification body is invalid.                                               | In the case of a `PERMISSION_DENIED` exception, the caller (your FCM application) doesn't have permission to execute the specified operation in the payload. Navigate to your FCM console, and verify your credentials have the required API actions enabled.                                                                                   |
