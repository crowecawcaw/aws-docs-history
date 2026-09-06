

# Amazon EventBridge events detail reference
<a name="event-reference"></a>

EventBridge itself emits the following events. These events are automatically sent to the default event bus as with any other AWS service.

For definitions of the metadata fields that are included in all events, see [AWS service event metadata](https://docs.aws.amazon.com/eventbridge/latest/ref/events-structure.html) in the *Events Reference*.


| Event detail type | Description | 
| --- | --- | 
|  [Scheduled Event](#event-detail-scheduled-event)  | Represents a scheduled event. | 
|  [Schema Created](#event-detail-schema-created)  | Represents the creation of a new event schema. | 
|  [Schema Version Created](#event-detail-schema-version-created)  | Represents the creation of a new version of a new or existing event schema. | 
|  [Connection state events](#event-detail-connection-state)  | Represents a change in the state of a connection. | 
|  [API Destination state events](#event-detail-api-destination-state)  | Represents a change in the state of an API destination. | 

## Schedule events
<a name="event-reference-schedules"></a>

EventBridge sends the following schedule events to the default event bus. For more information, see [Scheduler](using-eventbridge-scheduler.md).

### Scheduled Event
<a name="event-detail-scheduled-event"></a>

Represents a scheduled event.

The `source` and `detail-type` fields are included because they contain specific values for EventBridge events. For definitions of the other metadata fields that are included in all events, see [AWS service event metadata](https://docs.aws.amazon.com/eventbridge/latest/ref/events-structure.html) in the *Events Reference*.

```
{
  . . .,
  "detail-type": "Scheduled Event",
  "source": "aws.events",
  . . .,
  "detail": {}
}
```

`detail-type`  <a name="scheduled-event-detail-type"></a>
Identifies the type of event.  
For this event, this value is `Scheduled Event`.  
Required: Yes

`source`  <a name="scheduled-event-source"></a>
Identifies the service that generated the event. For EventBridge events, this value is `aws.events`.  
Required: Yes

`detail`  <a name="scheduled-event-detail"></a>
A JSON object that contains information about the event. The service generating the event determines the content of this field.  
Required: Yes  
There are no required fields in this object for `Scheduled Event` events.

**Example Scheduled Event event**  <a name="event-detail-scheduled-event.example"></a>

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
<a name="event-reference-schemas"></a>

EventBridge sends the following schema registry events to the default event bus. For more information, see [](eb-schema.md).

### Schema Created
<a name="event-detail-schema-created"></a>

Represents the creation of a new schema.

When a schema is created, EventBridge sends both a `Schema Created` and a `Schema Version Created` event.

The `source` and `detail-type` fields are included because they contain specific values for EventBridge events. For definitions of the other metadata fields that are included in all events, see [AWS service event metadata](https://docs.aws.amazon.com/eventbridge/latest/ref/events-structure.html) in the *Events Reference*.

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

`detail-type`  <a name="schema-created-detail-type"></a>
Identifies the type of event.  
For this event, this value is `Schema Created`.  
Required: Yes

`source`  <a name="schema-created-source"></a>
Identifies the service that generated the event. For EventBridge events, this value is `aws.schemas`.  
Required: Yes

`detail`  <a name="schema-created-detail"></a>
A JSON object that contains information about the event. The service generating the event determines the content of this field.  
Required: Yes  
For this event, this data includes:    
`SchemaName`  <a name="schema-created-schema-name"></a>
The name of the schema.  
Required: Yes  
`SchemaType`  <a name="schema-created-schema-type"></a>
The type of schema.  
Valid values: `OpenApi3` \| `JSONSchemaDraft4`  
Required: Yes  
`RegistryName`  <a name="schema-created-registry-name"></a>
The name of the registry that contains the schema.  
Required: Yes  
`CreationDate`  <a name="schema-created-creation-date"></a>
The date the schema was created.  
Required: Yes  
`Version`  <a name="schema-created-version"></a>
The version of the schema.  
For `Schema Created` events, this value will always be `1`.  
Required: Yes

**Example Schema Created event**  <a name="event-detail-schema-created.example"></a>

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
<a name="event-detail-schema-version-created"></a>

Represents the creation of a new version of a new or existing event schema.

When a schema is created, EventBridge sends both a `Schema Created` and a `Schema Version Created` event.

The `source` and `detail-type` fields are included because they contain specific values for EventBridge events. For definitions of the other metadata fields that are included in all events, see [AWS service event metadata](https://docs.aws.amazon.com/eventbridge/latest/ref/events-structure.html) in the *Events Reference*.

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

`detail-type`  <a name="schema-version-created-detail-type"></a>
Identifies the type of event.  
For this event, this value is `Schema Version Created`.  
Required: Yes

`source`  <a name="schema-version-created-source"></a>
Identifies the service that generated the event. For EventBridge events, this value is `aws.schemas`.  
Required: Yes

`detail`  <a name="schema-version-created-detail"></a>
A JSON object that contains information about the event. The service generating the event determines the content of this field.  
Required: Yes  
For this event, this data includes:    
`SchemaName`  <a name="schema-version-created-schema-name"></a>
The name of the schema.  
Required: Yes  
`SchemaType`  <a name="schema-version-created-schema-type"></a>
The type of schema.  
Valid values: `OpenApi3` \| `JSONSchemaDraft4`  
Required: Yes  
`RegistryName`  <a name="schema-version-created-registry-name"></a>
The name of the registry that contains the schema.  
Required: Yes  
`CreationDate`  <a name="schema-version-created-creation-date"></a>
The date the schema version was created.  
Required: Yes  
`Version`  <a name="schema-version-created-version"></a>
The version of the schema.  
Required: Yes

**Example Schema Version Created event**  <a name="event-detail-schema-version-created.example"></a>

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
<a name="event-reference-connections"></a>

EventBridge sends the following connection events to the default event bus. For more information, see [Connections](eb-target-connection.md).

### Connection state events
<a name="event-detail-connection-state"></a>

These events each represent a change in the state of a new or existing connection.

The `source` and `detail-type` fields are included because they contain specific values for EventBridge events. For definitions of the other metadata fields that are included in all events, see [AWS service event metadata](https://docs.aws.amazon.com/eventbridge/latest/ref/events-structure.html) in the *Events Reference*.

```
{
  . . .,
  "detail-type": "Connection {{status}}",
  "source": "aws.events",
  . . .,
  "detail": {
    "ConnectionName" : "String",
    "StateReason" : "String",
    "Timestamp" : "DateTime"
  }
}
```

`detail-type`  <a name="connection-state-detail-type"></a>
Identifies the type of event.  
For this event, this value is one of the following:   
+ `Connection Creation Started`
+ `Connection Update Started`
+ `Connection Deletion Started`
+ `Connection Activated`
+ `Connection Authorized`
+ `Connection Authorization Started`
+ `Connection Deauthorization Started`
+ `Connection Deauthorized`
+ `Connection Failed Connectivity`
Required: Yes

`source`  <a name="connection-state-source"></a>
Identifies the service that generated the event. For EventBridge events, this value is `aws.events`.  
Required: Yes

`detail`  <a name="connection-state-detail"></a>
A JSON object that contains information about the event. The service generating the event determines the content of this field.  
Required: Yes  
For this event, this data includes:    
`ConnectionName`  <a name="connection-state-connection-name"></a>
The name of the connection.  
Required: Yes  
`StateReason`  <a name="connection-state-state-reason"></a>
The reason the connection state has changed.  
Required: No  
`Timestamp`  <a name="connection-state-timestamp"></a>
The time and date the connection state changed.  
Required: Yes

**Example Connection state event**  <a name="event-detail-connection-state.example"></a>

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
<a name="event-reference-api-destinations"></a>

EventBridge sends the following API destination events to the default event bus. For more information, see [API destinations](eb-api-destinations.md).

### API Destination state events
<a name="event-detail-api-destination-state"></a>

These events each represents a change in the state of an API destination.

The `source` and `detail-type` fields are included because they contain specific values for EventBridge events. For definitions of the other metadata fields that are included in all events, see [AWS service event metadata](https://docs.aws.amazon.com/eventbridge/latest/ref/events-structure.html) in the *Events Reference*.

```
{
  . . .,
  "detail-type": "API Destination {{status}}",
  "source": "aws.events",
  . . .,
  "detail": {
    "ApiDestinationName" : "String",
    "Timestamp" : "DateTime"
  }
}
```

`detail-type`  <a name="api-destination-state-detail-type"></a>
Identifies the type of event.  
For this event, this value is one of the following:   
+ `API Destination Activated`
+ `API Destination Deactivated`
Required: Yes

`source`  <a name="api-destination-state-source"></a>
Identifies the service that generated the event. For EventBridge events, this value is `aws.events`.  
Required: Yes

`detail`  <a name="api-destination-state-detail"></a>
A JSON object that contains information about the event. The service generating the event determines the content of this field.  
Required: Yes  
For this event, this data includes:    
`ApiDestinationName`  <a name="api-destination-state-connection-name"></a>
The name of the API destination.  
Required: Yes  
`Timestamp`  <a name="api-destination-state-timestamp"></a>
The time and date the API destination state changed.  
Required: Yes

**Example API destination state event**  <a name="event-detail-api-destination-state.example"></a>

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