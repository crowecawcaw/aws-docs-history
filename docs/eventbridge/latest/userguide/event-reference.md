# Amazon EventBridge events detail reference

EventBridge itself emits the following events. These events are automatically sent to the default event bus as with any other AWS service.

For definitions of the metadata fields that are included in all events, see [AWS service event metadata](../ref/events-structure.md "../ref/events-structure.md") in the _Events Reference_.

| Event detail type                                                                                            | Description                                                                 |
| ------------------------------------------------------------------------------------------------------------ | --------------------------------------------------------------------------- |
| [Scheduled Event](#event-detail-scheduled-event "#event-detail-scheduled-event")                             | Represents a scheduled event.                                               |
| [Schema Created](#event-detail-schema-created "#event-detail-schema-created")                                | Represents the creation of a new event schema.                              |
| [Schema Version Created](#event-detail-schema-version-created "#event-detail-schema-version-created")        | Represents the creation of a new version of a new or existing event schema. |
| [Connection state<br>events](#event-detail-connection-state "#event-detail-connection-state")                | Represents a change in the state of a connection.                           |
| [API Destination state<br>events](#event-detail-api-destination-state "#event-detail-api-destination-state") | Represents a change in the state of an API destination.                     |

## Schedule events

EventBridge sends the following schedule events to the default event bus. For more information, see [Scheduler](using-eventbridge-scheduler.md "using-eventbridge-scheduler.md").

### Scheduled Event

Represents a scheduled event.

The `source` and `detail-type` fields are included because they contain specific values for EventBridge events.
For definitions of the other metadata fields that are included in all events, see [AWS service event metadata](../ref/events-structure.md "../ref/events-structure.md") in the _Events Reference_.

```
{
  . . .,
  "detail-type": "Scheduled Event",
  "source": "aws.events",
  . . .,
  "detail": {}
}
```

`detail-type`

Identifies the type of event.

For this event, this value is `Scheduled Event`.

Required: Yes

`source`

Identifies the service that generated the event. For EventBridge
events, this value is `aws.events`.

Required: Yes

`detail`

A JSON object that contains information about the event. The service
generating the event determines the content of this field.

Required: Yes

There are no required fields in this object for `Scheduled Event` events.

###### Example Scheduled Event

event

```
{
  "version": "0",
  "id": "89d1a02d-5ec7-412e-82f5-13505f849b41",
  "detail-type": "Scheduled Event",
  "source": "aws.events",
  "account": "123456789012",
  "time": "2016-12-30T18:44:49Z",
  "region": "us-east-1",
  "resources": ["arn:aws:events:us-east-1:123456789012:rule/SampleRule"],
  "detail": {}
}
```

## Schema registry events

EventBridge sends the following schema registry events to the default event bus. For more information, see .

### Schema Created

Represents the creation of a new schema.

When a schema is created, EventBridge sends both a `Schema Created` and a `Schema Version Created` event.

The `source` and `detail-type` fields are included because they contain specific values for EventBridge events.
For definitions of the other metadata fields that are included in all events, see [AWS service event metadata](../ref/events-structure.md "../ref/events-structure.md") in the _Events Reference_.

```
{
  . . .,
  "detail-type": "Schema Created",
  "source": "aws.schemas",
  . . .,
  "detail": {
    "SchemaName" : "String",
    "SchemaType" : "String",
    "RegistryName" : "String",
    "CreationDate" : "DateTime",
    "Version" : "Number"
  }
}
```

`detail-type`

Identifies the type of event.

For this event, this value is `Schema Created`.

Required: Yes

`source`

Identifies the service that generated the event. For EventBridge
events, this value is `aws.schemas`.

Required: Yes

`detail`

A JSON object that contains information about the event. The service
generating the event determines the content of this field.

Required: Yes

For this event, this data includes:

`SchemaName`

The name of the schema.

Required: Yes

`SchemaType`

The type of schema.

Valid values: `OpenApi3` | `JSONSchemaDraft4`

Required: Yes

`RegistryName`

The name of the registry that contains the schema.

Required: Yes

`CreationDate`

The date the schema was created.

Required: Yes

`Version`

The version of the schema.

For `Schema Created` events, this value will always be `1`.

Required: Yes

###### Example Schema Created

event

```
{
  "version": "0",
  "id": "01234567-0123-0123-0123-012345678901",
  "detail-type": "Schema Created",
  "source": "aws.schemas",
  "account": "123456789012",
  "time": "2019-05-31T21:49:54Z",
  "region": "us-east-1",
  "resources": ["arn:aws:schemas:us-east-1::schema/myRegistry/mySchema"],
  "detail": {
    "SchemaName": "mySchema",
    "SchemaType": "OpenApi3",
    "RegistryName": "myRegistry",
    "CreationDate": "2019-11-29T20:08:55Z",
    "Version": "1"
  }
}

```

### Schema Version Created

Represents the creation of a new version of a new or existing event schema.

When a schema is created, EventBridge sends both a `Schema Created` and a `Schema Version Created` event.

The `source` and `detail-type` fields are included because they contain specific values for EventBridge events.
For definitions of the other metadata fields that are included in all events, see [AWS service event metadata](../ref/events-structure.md "../ref/events-structure.md") in the _Events Reference_.

```
{
  . . .,
  "detail-type": "Schema Version Created",
  "source": "aws.schemas",
  . . .,
  "detail": {
    "SchemaName" : "String",
    "SchemaType" : "String",
    "RegistryName" : "String",
    "CreationDate" : "DateTime",
    "Version" : "Number"
  }
}
```

`detail-type`

Identifies the type of event.

For this event, this value is `Schema Version Created`.

Required: Yes

`source`

Identifies the service that generated the event. For EventBridge
events, this value is `aws.schemas`.

Required: Yes

`detail`

A JSON object that contains information about the event. The service
generating the event determines the content of this field.

Required: Yes

For this event, this data includes:

`SchemaName`

The name of the schema.

Required: Yes

`SchemaType`

The type of schema.

Valid values: `OpenApi3` | `JSONSchemaDraft4`

Required: Yes

`RegistryName`

The name of the registry that contains the schema.

Required: Yes

`CreationDate`

The date the schema version was created.

Required: Yes

`Version`

The version of the schema.

Required: Yes

###### Example Schema Version

Created event

```
{
  "version": "0",
  "id": "01234567-0123-0123-0123-012345678901",
  "detail-type": "Schema Version Created",
  "source": "aws.schemas",
  "account": "123456789012",
  "time": "2019-05-31T21:49:54Z",
  "region": "us-east-1",
  "resources": ["arn:aws:schemas:us-east-1::schema/myRegistry/mySchema"],
  "detail": {
    "SchemaName": "mySchema",
    "SchemaType": "OpenApi3",
    "RegistryName": "myRegistry",
    "CreationDate": "2019-11-29T20:08:55Z",
    "Version": "5"
  }
}
```

## Connection events

EventBridge sends the following connection events to the default event bus. For more information, see [Connections](eb-target-connection.md "eb-target-connection.md").

### Connection state

events

These events each represent a change in the state of a new or existing
connection.

The `source` and `detail-type` fields are included because they contain specific values for EventBridge events.
For definitions of the other metadata fields that are included in all events, see [AWS service event metadata](../ref/events-structure.md "../ref/events-structure.md") in the _Events Reference_.

```
{
  . . .,
  "detail-type": "Connection `status`",
  "source": "aws.events",
  . . .,
  "detail": {
    "ConnectionName" : "String",
    "StateReason" : "String",
    "Timestamp" : "DateTime"
  }
}
```

`detail-type`

Identifies the type of event.

For this event, this value is one of the following:

- `Connection Creation Started`
- `Connection Update Started`
- `Connection Deletion Started`
- `Connection Activated`
- `Connection Authorized`
- `Connection Authorization Started`
- `Connection Deauthorization Started`
- `Connection Deauthorized`
- `Connection Failed Connectivity`

Required: Yes

`source`

Identifies the service that generated the event. For EventBridge events, this value is `aws.events`.

Required: Yes

`detail`

A JSON object that contains information about the event. The service
generating the event determines the content of this field.

Required: Yes

For this event, this data includes:

`ConnectionName`

The name of the connection.

Required: Yes

`StateReason`

The reason the connection state has changed.

Required: No

`Timestamp`

The time and date the connection state changed.

Required: Yes

###### Example Connection state event

```
{
    "version": "0",
    "id": "1d7a4ac6-a50a-745f-a331-a0d802f7badb",
    "detail-type": "Connection Creation Started",
    "source": "aws.events",
    "account": "123456789012",
    "time": "2024-10-28T09:08:20Z",
    "region": "us-east-1",
    "resources": [
        "arn:aws:events:us-east-1:123456789012:connection/sample-connection/ee7e4d52-8df0-4bed-a0d5-fa7dea43fcf8"
    ],
    "detail": {
        "ConnectionName": "sample-connection",
        "Timestamp": "2024-10-24 09:26:35 +0000 UTC"
    }
}
```

## API Destination events

EventBridge sends the following API destination events to the default event bus. For more information, see [API destinations](eb-api-destinations.md "eb-api-destinations.md").

### API Destination state

events

These events each represents a change in the state of an API destination.

The `source` and `detail-type` fields are included because they contain specific values for EventBridge events.
For definitions of the other metadata fields that are included in all events, see [AWS service event metadata](../ref/events-structure.md "../ref/events-structure.md") in the _Events Reference_.

```
{
  . . .,
  "detail-type": "API Destination `status`",
  "source": "aws.events",
  . . .,
  "detail": {
    "ApiDestinationName" : "String",
    "Timestamp" : "DateTime"
  }
}
```

`detail-type`

Identifies the type of event.

For this event, this value is one of the following:

- `API Destination Activated`
- `API Destination Deactivated`

Required: Yes

`source`

Identifies the service that generated the event. For EventBridge events, this value is `aws.events`.

Required: Yes

`detail`

A JSON object that contains information about the event. The service
generating the event determines the content of this field.

Required: Yes

For this event, this data includes:

`ApiDestinationName`

The name of the API destination.

Required: Yes

`Timestamp`

The time and date the API destination state
changed.

Required: Yes

###### Example API destination state event

```
{
    "version": "0",
    "id": "1d7a4ac6-a50a-745f-a331-a0d802f7badb",
    "detail-type": "API Destination Deactivated",
    "source": "aws.events",
    "account": "123456789012",
    "time": "2024-10-28T09:08:20Z",
    "region": "us-east-1",
    "resources": [
        "arn:aws:events:us-east-1:123456789012:api-destination/sample-api-destination/ee7e4d52-8df0-4bed-a0d5-fa7dea43fcf8"
    ],
    "detail": {
        "ApiDestinationName": "sample-api-destination",
        "Timestamp": "2024-10-24 09:26:35 +0000 UTC"
    }
}
```
