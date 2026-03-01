# AWS AppSync JavaScript resolver function reference for EventBridge data source

The AWS AppSync resolver function request and response used with the EventBridge data source allows you to send
custom events to the Amazon EventBridge bus.

## Request

The request handler allows you to send multiple custom events to an EventBridge event bus:

```
export function request(ctx) {
  return {
    "operation" : "PutEvents",
    "events" : [{}]
  }
}
```

An EventBridge `PutEvents` request has the following type definition:

```
type PutEventsRequest = {
  operation: 'PutEvents'
  events: {
    source: string
    detail: { [key: string]: any }
    detailType: string
    resources?: string[]
    time?: string // RFC3339 Timestamp format
  }[]
}
```

## Response

If the `PutEvents` operation is successful, the response from EventBridge is included in the
`ctx.result`:

```
export function response(ctx) {
  if(ctx.error)
    util.error(ctx.error.message, ctx.error.type, ctx.result)
  else
    return ctx.result
}
```

Errors that occur while performing `PutEvents` operations such as
`InternalExceptions` or `Timeouts` will appear in `ctx.error`. For a
list of EventBridge's common errors, see the [EventBridge common error reference](../../../eventbridge/latest/APIReference/CommonErrors.md "../../../eventbridge/latest/APIReference/CommonErrors.md").

The `result` will have the following type definition:

```
type PutEventsResult = {
  Entries: {
    ErrorCode: string
    ErrorMessage: string
    EventId: string
  }[]
  FailedEntryCount: number
}
```

- **Entries**

The ingested event results, both successful and unsuccessful. If the ingestion was successful, the
entry has the `EventID` in it. Otherwise, you can use the `ErrorCode` and
`ErrorMessage` to identify the problem with the entry.

For each record, the index of the response element is the same as the index in the request
array.

- **FailedEntryCount**

The number of failed entries. This value is represented as an integer.

For more information about the response of `PutEvents`, see [PutEvents](../../../eventbridge/latest/APIReference/API_PutEvents.md#API_PutEvents_ResponseElements "../../../eventbridge/latest/APIReference/API_PutEvents.md#API_PutEvents_ResponseElements").

**Example sample response 1**

The following example is a `PutEvents` operation with two successful events:

```
{
    "Entries" : [
        {
            "EventId": "11710aed-b79e-4468-a20b-bb3c0c3b4860"
        },
        {
            "EventId": "d804d26a-88db-4b66-9eaf-9a11c708ae82"
        }
    ],
    "FailedEntryCount" : 0
}
```

**Example sample response 2**

The following example is a `PutEvents` operation with three events, two successes and one
fail:

```
{
    "Entries" : [
        {
            "EventId": "11710aed-b79e-4468-a20b-bb3c0c3b4860"
        },
        {
            "EventId": "d804d26a-88db-4b66-9eaf-9a11c708ae82"
        },
        {
            "ErrorCode" : "SampleErrorCode",
            "ErrorMessage" : "Sample Error Message"
        }
    ],
    "FailedEntryCount" : 1
}
```

## `PutEvents` fields

`PutEvents` contains the following mapping template fields:

- **Version**

Common to all request mapping templates, the `version` field defines the version
that the template uses. This field is required. The value `2018-05-29` is the only
version supported for the EventBridge mapping templates.

- **Operation**

The only supported operation is `PutEvents`. This operation allows you to add
custom events to your event bus.

- **Events**

An array of events that will be added to the event bus. This array should have an allocation
of 1 - 10 items.

The `Event` object has the following fields:

    + `"source"`: A string that defines the source of the event.
    + `"detail"`: A JSON object that you can use to attach information about the
     event. This field can be an empty map ( `{ }` ).
    + `"detailType`: A string that identifies the type of event.
    + `"resources"`: A JSON array of strings that identifies resources involved in
     the event. This field can be an empty array.
    + `"time"`: The event timestamp provided as a string. This should follow the
     [RFC3339](https://www.rfc-editor.org/rfc/rfc3339.txt "https://www.rfc-editor.org/rfc/rfc3339.txt") timestamp
     format.

The snippets below are some examples of valid `Event` objects:

**Example 1**

```
{
    "source" : "source1",
    "detail" : {
        "key1" : [1,2,3,4],
        "key2" : "strval"
    },
    "detailType" : "sampleDetailType",
    "resources" : ["Resouce1", "Resource2"],
    "time" : "2022-01-10T05:00:10Z"
}
```

**Example 2**

```
{
    "source" : "source1",
    "detail" : {},
    "detailType" : "sampleDetailType"
}
```

**Example 3**

```
{
    "source" : "source1",
    "detail" : {
        "key1" : 1200
    },
    "detailType" : "sampleDetailType",
    "resources" : []
}
```
