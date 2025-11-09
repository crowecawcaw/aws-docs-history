**End of support notice:** On October
30, 2026, AWS will end support for Amazon Pinpoint. After October 30, 2026, you will no
longer be able to access the Amazon Pinpoint console or Amazon Pinpoint resources (endpoints,
segments, campaigns, journeys, and analytics). For more information, see [Amazon Pinpoint end of
support](../../../console/pinpoint/migration-guide.md "../../../console/pinpoint/migration-guide.md"). **Note:** APIs related to SMS, voice,
mobile push, OTP, and phone number validate are not impacted by this change and are
supported by AWS End User Messaging.

# App event data stream from Amazon Pinpoint

After you integrate your application (app) with Amazon Pinpoint and set up event streaming, Amazon Pinpoint
retrieves your app's user activity, custom events, and message delivery data from the
destination that you specified during setup for you to view. For information about how
to set up event streaming so you can view your event data, see [Set up Amazon Pinpoint to stream app event data through Amazon Kinesis or Amazon Data Firehose](event-streams-setup.md "event-streams-setup.md") .

## App event example

The JSON object for an app event contains the data shown in the following
example.

```
{
  "event_type": "_session.stop",
  "event_timestamp": 1487973802507,
  "arrival_timestamp": 1487973803515,
  "event_version": "3.0",
  "application": {
    "app_id": "a1b2c3d4e5f6g7h8i9j0k1l2m3n4o5p6",
    "cognito_identity_pool_id": "us-east-1:a1b2c3d4-e5f6-g7h8-i9j0-k1l2m3n4o5p6",
    "package_name": "main.page",
    "sdk": {
      "name": "aws-sdk-mobile-analytics-js",
      "version": "0.9.1:2.4.8"
    },
    "title": "title",
    "version_name": "1.0",
    "version_code": "1"
  },
  "client": {
    "client_id": "m3n4o5p6-a1b2-c3d4-e5f6-g7h8i9j0k1l2",
    "cognito_id": "us-east-1:i9j0k1l2-m3n4-o5p6-a1b2-c3d4e5f6g7h8"
  },
  "device": {
    "locale": {
      "code": "en_US",
      "country": "US",
      "language": "en"
    },
    "make": "generic web browser",
    "model": "Unknown",
    "platform": {
      "name": "android",
      "version": "10.10"
    }
  },
  "session": {
    "session_id": "f549dea9-1090-945d-c3d1-e4967example",
    "start_timestamp": 1487973202531,
    "stop_timestamp": 1487973802507
  },
  "attributes": {},
  "metrics": {}
}
```

## App event attributes

This section defines the attributes that are included in the previous example of
the app event stream.

| Attribute           | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| ------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `event_type`        | The type of event. Possible values are:<br>• **\_session.start** –<br>The endpoint began a new session.<br>• **\_session.stop** – The<br>endpoint ended a session.<br>• **\_userauth.sign_in** –<br>The endpoint logged in to your app.<br>• **\_userauth.sign_up** –<br>A new endpoint completed the registration process in your<br>app.<br>• **\_userauth.auth_fail**<br>– The endpoint attempted to sign in to your app, but<br>wasn't able to complete the process.<br>• **\_monetization.purchase**<br>– The endpoint made a purchase in your app.<br>• **\_session.pause** –<br>The endpoint paused a session. Paused sessions can be<br>resumed so that you can continue to collect metrics without<br>starting an entirely new session.<br>• **\_session.resume** –<br>The endpoint resumed a session. |
| `event_timestamp`   | The time when the event was reported, shown as Unix time in<br>milliseconds.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| `arrival_timestamp` | The time when the event was received by Amazon Pinpoint, shown as Unix<br>time in milliseconds.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| `event_version`     | The version of the event JSON schema.<br>TipCheck this version in your event-processing application so<br>that you know when to update the application in response to a<br>schema update.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| `application`       | Information about the Amazon Pinpoint project that's associated with the event. For more information,<br>see the [Application](#event-streams-data-app-attributes-application "#event-streams-data-app-attributes-application") table.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| `client`            | Information about the endpoint that reported the event. For more information, see the [Client](#event-streams-data-app-attributes-client "#event-streams-data-app-attributes-client")<br>table.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| `device`            | Information about the device that reported the event. For more information, see the [Device](#event-streams-data-app-attributes-device "#event-streams-data-app-attributes-device")<br>table.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| `session`           | Information about the session that generated the event. For more information, see the [Session](#event-streams-data-app-attributes-session "#event-streams-data-app-attributes-session") table.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| `attributes`        | Attributes that are associated with the event. For events that are<br>reported by your apps, this object includes custom attributes that<br>you define.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| `metrics`           | Metrics that are related to the event. You can optionally configure<br>your apps to send custom metrics to Amazon Pinpoint.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |

### Application

Includes information about the Amazon Pinpoint project that the event is associated
with.

| Attribute                  | Description                                                                                                                                                                                                         |
| -------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `app_id`                   | The unique ID of the Amazon Pinpoint project that reported the<br>event.                                                                                                                                            |
| `cognito_identity_pool_id` | The ID of the Amazon Cognito Identity Pool that the endpoint is<br>associated with.                                                                                                                                 |
| `package_name`             | The name of the app package, such as<br>`com.example.my_app`.                                                                                                                                                       |
| `sdk`                      | Information about the SDK that was used to report the event.<br>For more information, see the [SDK](#event-streams-data-app-attributes-application-sdk "#event-streams-data-app-attributes-application-sdk") table. |
| `title`                    | The name of the app.                                                                                                                                                                                                |
| `version_name`             | The name of the version of the app, such as<br>`V2.5`.                                                                                                                                                              |
| `version_code`             | The version number of the app, such as `3`.                                                                                                                                                                         |

#### SDK

Includes information about the SDK that was used to report the event.

| Attribute | Description                                               |
| --------- | --------------------------------------------------------- |
| `name`    | The name of the SDK that was used to report the<br>event. |
| `version` | The version of the SDK.                                   |

### Client

Includes information about the endpoint that generated the event.

| Attribute    | Description                                                      |
| ------------ | ---------------------------------------------------------------- |
| `client_id`  | The ID of the endpoint.                                          |
| `cognito_id` | The Amazon Cognito ID token that's associated with the endpoint. |

### Device

Includes information about the device of the endpoint that generated the
event.

| Attribute  | Description                                                                                                                                                                                                                         |
| ---------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `locale`   | Information about the language and region settings for the<br>endpoint's device. For more information, see the [Locale](#event-streams-data-app-attributes-device-locale "#event-streams-data-app-attributes-device-locale") table. |
| `make`     | The manufacturer of the endpoint's device.                                                                                                                                                                                          |
| `model`    | The model identifier of the endpoint's device.                                                                                                                                                                                      |
| `platform` | Information about the operating system on the endpoint's<br>device. For more information, see the [Platform](#event-streams-data-app-attributes-device-platform "#event-streams-data-app-attributes-device-platform") table.        |

#### Locale

Includes information about the language and region settings for the endpoint's
device.

| Attribute  | Description                                                          |
| ---------- | -------------------------------------------------------------------- |
| `code`     | The locale identifier that's associated with the<br>device.          |
| `country`  | The country or region that's associated with the device's<br>locale. |
| `language` | The language that's associated with the device's<br>locale.          |

#### Platform

Includes information about the operating system on the endpoint's
device.

| Attribute | Description                                        |
| --------- | -------------------------------------------------- |
| `name`    | The name of the operating system on the device.    |
| `version` | The version of the operating system on the device. |

### Session

Includes information about the session that generated the event.

| Attribute         | Description                                                                      |
| ----------------- | -------------------------------------------------------------------------------- |
| `session_id`      | A unique ID that identifies the session.                                         |
| `start_timestamp` | The date and time when the session began, shown as Unix<br>time in milliseconds. |
| `stop_timestamp`  | The date and time when the session ended, shown as Unix<br>time in milliseconds. |
