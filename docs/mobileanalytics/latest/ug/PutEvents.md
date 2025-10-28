# PutEvents

###### Note

Amazon Mobile Analytics was discontinued on April 30, 2018. The features that were
previously provided by Mobile Analytics are now provided by Amazon Pinpoint. If you're new to
Mobile Analytics, you should use Amazon Pinpoint instead. If you currently use Mobile Analytics, see
[Migrating from Amazon Mobile Analytics to Amazon Pinpoint](migrate.md "migrate.md").

The PutEvents operation records one or more events. You
can have up to 1,500 unique custom events per app, any combination of up to 40
attributes and metrics per custom event, and an infinite number of attribute or metrics
values.

###### Topics

- [Requests](#putEvents-requests "#putEvents-requests")
- [Responses](#putEvents-preset-responses "#putEvents-preset-responses")

## Requests

### Client Context

Header

#### Syntax

```
x-amz-Client-Context: {
                        "client": {
                                    "client_id":"`<client_id>`",
                                    "app_title":"`<app_title>`",
                                    "app_version_name":"`<app_version_name>`",
                                    "app_version_code":"`<app_version_code>`",
                                    "app_package_name":"`<app_package_name>`"
                                  },

                        "custom": {},

                        "env":{
                                "platform":"`<platform>`",
                                "model":"`<model>`",
                                "make":"`<make>`",
                                "platform_version":"`<platform_version>`",
                                "locale":"`<locale>`”
                              },

                        "services": {
                                      "mobile_analytics": {
                                                            "app_id":"`<mobile_analytics_app_id>`"
                                                          }
                                    }
                       }
```

#### Description

The operation takes the following request header.

**x-amz-client-context**

The request header.

**client**

Name-value pairs that describes the client
application.

**client_id**

A unique identifier representing this
installation instance of your app.

Type: String

Default: None

Required: Yes

**app_title**

The title of your app. For example,
`My App`.

Type: String

Default: None

Required: Yes

**app_version_name**

The version of your app. For example,
`V2.0`.

Type: String

Default: None

Required: No

**app_version_code**

The version code for your app. For example,
`3`.

Type: String

Default: None

Required: No

**app_package_name**

The name of your package. For example,
`com.example.my_app`.

Type: String

Default: None

Required: No

**custom**

User defined name-value pairs that describe this
installation of the application.

Type: Map

Default: None

Required: No

**env**

Name-value pair that describes the device that
runs the event.

**platform**

The operating system of the device. For
example, `iphoneos`.

Type: String

Valid values: `iphoneos`,
`android`, `windowsphone`,
`blackberry`, `macos`,
`windows`, `linux`

Default: None

Required: Yes

**model**

The model of the device. For example,
`Nexus`.

Type: String

Default: None

Required: No

**make**

The manufacturer of the device. For example,
`Samsung`.

Type: String

Default: None

Required: No

**platform_version**

The version of the operating system of the
device. For example, `4.0.4`.

Type: String

Default: None

Required: No

**locale**

The locale of the device. For example,
`en_US`.

Type: String

Default: None

Required: No

**services**

Name-value pair that contains service specific
sections.

**mobile_analytics**

Name-value pair that describes service
specific attributes.

**app_id**

The value obtained from the Mobile Analytics console to
record data to.

Type: String

Default: None

Required: Yes

### Request Body

#### Syntax

```
{
  "events": [
    {
      "eventType": "`<Event type>`",
      "timestamp": "`<ISO 8601 date>`",
      "version": "v2.0",
      "session": {
                  "id": "`<Session id>`",
                  "startTimestamp": "`<ISO 8601 date>`"
      },
      "attributes": {
                     "`<Optional string name>`": "`<Optional string value>`",
                     ...
                     "`<Optional string name>`": "`<Optional string value>`"
      },
      "metrics": {
                  "`<Optional string name>`": `<Optional numeric value>`,
                   ...
                  "`<Optional string name>`": `<Optional numeric value>`
      }
    },
    ...
  ]
}
```

#### Description

This operation takes the following request content.

**Events**

An array of JSON objects representing a batch of unique event
occurrences in your app. Each JSON object in the array consists
of the following:

**eventType**

A name signifying an event that occurred in your
app. This is used for grouping and aggregating like
events together for reporting purposes.

Type: String

Default: None

Required: Yes

**timestamp**

The time the event occurred in ISO 8601 standard
date time format. For example,
`2014-06-30T19:07:47.885Z`

Type: String

Constraints: Must follow ISO 8601 format

Default: None

Required: Yes

**attributes**

A collection of key-value pairs that give
additional context to the event. The key-value pairs
are specified by the developer.

This collection can be empty or the attribute
object can be omitted.

Type: JSON object of key-value pairs
(String:String)

Constraints: Key can be up to 50 characters or
less and the value can be up to 200 characters.

Default: None

Required: No

**metrics**

A collection of key-value pairs that gives
additional measurable context to the event. This key
has the following key-values pairs. The pairs
specified by the developer.

This collection can be empty or the attribute
object can be omitted.

Type: JSON object of key value pairs
(String:Number)

Constraints: Key can be up to 50 characters.

Default: None

Required: No

**session**

Describes the session. Session information is
required on events to be aggregated in console
reports. Events submitted without session
information are still exported to S3 or Redshift but
are not aggregated for inclusion in reports. This
key has the following key-value pairs.

**id**

A unique identifier for the session.

Type: String

Default: None

Required: Yes

**startTimestamp**

The time the event occurred in ISO 8601
standard date time format. For example,
`2014-06-30T19:07:47.885Z`

Type: String

Constraints: Must follow ISO 8601 format

Default: None

Required: Yes

**version**

Describes the version. This value must always be
`v2.0`.

Type: String

Constraints: Must always be
`v2.0`.

Default: None

Required: Yes

#### JSON Example

```
{"events":[
  {
    "metrics":{
                "Score":12345,
                "TimeInLevel":64
    },
    "session":{
                "id" : "`<session id>`",
                "startTimestamp" : "2014-06-30T19:07:47.885Z"
    },
    "attributes":{
                   "LevelName":"Level1",
                   "CharacterClass":"Warrior",
                   "Successful":"True"
    },
    "eventType":"LevelComplete",
    "version":"v2.0",
    "timestamp":"2014-06-30T19:07:47.885Z"
  }
]}
```

## Responses

### Syntax

```
HTTP/1.1 202
x-amzn-RequestId: `<A request id>`
Content-Type: application/json
```

### Response Headers

This operation has the following response codes.

**202 Accepted**

The request has been accepted for processing, however the events
have not been fully processed.

**400 Bad Request**

The x-amz-client-context header is missing or invalid.

OR

The event payload is missing or invalid.

**403 Forbidden**

The request is not authorized to perform this action.

**413 Request Entity Too Large**

The payload is too large. The payload cannot exceed 1024
KB.
