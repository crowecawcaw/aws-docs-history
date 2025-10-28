# Sending events with `PutEvents` in Amazon EventBridge

The `PutEvents` action sends multiple [events](eb-events.md "eb-events.md") to EventBridge in a single request. For
more information, see [PutEvents](../APIReference/API_PutEvents.md "../APIReference/API_PutEvents.md") in the _Amazon EventBridge API Reference_ and [put-events](../../../cli/latest/reference/events/put-events.md "../../../cli/latest/reference/events/put-events.md") in the
_AWS CLI Command Reference_.

Each `PutEvents` request can support a limited number of entries. For more
information, see [Amazon EventBridge quotas](eb-quota.md "eb-quota.md"). The
`PutEvents` operation attempts to process all entries in the natural order of
the request. After you call `PutEvents`, EventBridge assigns each event a unique
ID.

The following example Java code sends two identical events to
EventBridge.

AWS SDK for Java Version
2.x

```
EventBridgeClient eventBridgeClient =
    EventBridgeClient.builder().build();

PutEventsRequestEntry requestEntry = PutEventsRequestEntry.builder()
    .resources("resource1", "resource2")
    .source("com.mycompany.myapp")
    .detailType("myDetailType")
    .detail("{ \"key1\": \"value1\", \"key2\": \"value2\" }")
    .build();

List <
PutEventsRequestEntry > requestEntries = new ArrayList <
PutEventsRequestEntry > ();
requestEntries.add(requestEntry);

PutEventsRequest eventsRequest = PutEventsRequest.builder()
    .entries(requestEntries)
    .build();

PutEventsResponse result = eventBridgeClient.putEvents(eventsRequest);

for (PutEventsResultEntry resultEntry: result.entries()) {
    if (resultEntry.eventId() != null) {
        System.out.println("Event Id: " + resultEntry.eventId());
    } else {
        System.out.println("PutEvents failed with Error Code: " + resultEntry.errorCode());
    }
}

```

AWS SDK for Java Version
1.0

```
EventBridgeClient eventBridgeClient =
    EventBridgeClient.builder().build();

PutEventsRequestEntry requestEntry = new PutEventsRequestEntry()
        .withTime(new Date())
        .withSource("com.mycompany.myapp")
        .withDetailType("myDetailType")
        .withResources("resource1", "resource2")
        .withDetail("{ \"key1\": \"value1\", \"key2\": \"value2\" }");

PutEventsRequest request = new PutEventsRequest()
        .withEntries(requestEntry, requestEntry);

PutEventsResult result = awsEventsClient.putEvents(request);

for (PutEventsResultEntry resultEntry : result.getEntries()) {
    if (resultEntry.getEventId() != null) {
        System.out.println("Event Id: " + resultEntry.getEventId());
    } else {
        System.out.println("Injection failed with Error Code: " + resultEntry.getErrorCode());
    }
}
```

After you run this code, the `PutEvents` result includes an array of response
entries. Each entry in the response array corresponds to an entry in the request array in
order from the beginning to the end of the request and response. The response
`Entries` array always includes the same number of entries as the request
array.

## Handling failures with

`PutEvents`

By default, if an individual entry within a request fails, EventBridge continues processing
the rest of the entries in the request. A response `Entries` array can
include both successful and unsuccessful entries. You must detect unsuccessful entries
and include them in a subsequent call.

Successful result entries include an `Id` value, and unsuccessful result
entries include `ErrorCode` and `ErrorMessage` values.
`ErrorCode` describes the type of error. `ErrorMessage`
provides more information about the error. The following example has three result
entries for a `PutEvents` request. The second entry is unsuccessful.

```
{
    "FailedEntryCount": 1,
    "Entries": [
        {
            "EventId": "11710aed-b79e-4468-a20b-bb3c0c3b4860"
        },
        {   "ErrorCode": "InternalFailure",
            "ErrorMessage": "Internal Service Failure"
        },
        {
            "EventId": "d804d26a-88db-4b66-9eaf-9a11c708ae82"
        }
    ]
}
```

###### Note

If you use `PutEvents` to publish an event to an event bus that does not exist,
EventBridge event matching will not find a corresponding rule and will drop the event.
Although EventBridge will send a `200` response, it will not fail the request or include the event
in the `FailedEntryCount` value of the request response.

You can include entries that are unsuccessful in subsequent `PutEvents`
requests. First, to find out if there are failed entries in the request, check the
`FailedRecordCount` parameter in `PutEventsResult`. If it
isn't zero, then you can add each `Entry` that has an `ErrorCode`
that is not null to a subsequent request. The following example shows a failure
handler.

```
PutEventsRequestEntry requestEntry = new PutEventsRequestEntry()
        .withTime(new Date())
        .withSource("com.mycompany.myapp")
        .withDetailType("myDetailType")
        .withResources("resource1", "resource2")
        .withDetail("{ \"key1\": \"value1\", \"key2\": \"value2\" }");

List<PutEventsRequestEntry> putEventsRequestEntryList = new ArrayList<>();
for (int i = 0; i < 3; i++) {
    putEventsRequestEntryList.add(requestEntry);
}

PutEventsRequest putEventsRequest = new PutEventsRequest();
putEventsRequest.withEntries(putEventsRequestEntryList);
PutEventsResult putEventsResult = awsEventsClient.putEvents(putEventsRequest);

while (putEventsResult.getFailedEntryCount() > 0) {
    final List<PutEventsRequestEntry> failedEntriesList = new ArrayList<>();
    final List<PutEventsResultEntry> PutEventsResultEntryList = putEventsResult.getEntries();
    for (int i = 0; i < PutEventsResultEntryList.size(); i++) {
        final PutEventsRequestEntry putEventsRequestEntry = putEventsRequestEntryList.get(i);
        final PutEventsResultEntry putEventsResultEntry = PutEventsResultEntryList.get(i);
        if (putEventsResultEntry.getErrorCode() != null) {
            failedEntriesList.add(putEventsRequestEntry);
        }
    }
    putEventsRequestEntryList = failedEntriesList;
    putEventsRequest.setEntries(putEventsRequestEntryList);
    putEventsResult = awsEventsClient.putEvents(putEventsRequest);
    }
```

## Sending events using the AWS CLI

You can use the AWS CLI to send custom events to EventBridge so they can be processed. The following example puts one custom
event into EventBridge:

```
aws events put-events \
--entries '[{"Time": "2016-01-14T01:02:03Z", "Source": "com.mycompany.myapp", "Resources": ["resource1", "resource2"], "DetailType": "myDetailType", "Detail": "{ \"key1\": \"value1\", \"key2\": \"value2\" }"}]'
```

You can also create a JSON file that contains custom events.

```
[
  {
    "Time": "2016-01-14T01:02:03Z",
    "Source": "com.mycompany.myapp",
    "Resources": [
      "resource1",
      "resource2"
    ],
    "DetailType": "myDetailType",
    "Detail": "{ \"key1\": \"value1\", \"key2\": \"value2\" }"
  }
]
```

Then, to use the AWS CLI to read the entries from this file and send events, at a
command prompt, type:

```
aws events put-events --entries file://`entries.json`
```

## Calculating PutEvents event entry size

When you send custom events to EventBridge using the `PutEvents` action, you can batch
multiple event entries into one request for efficiency. However, the total entry size--that
is, the sum of all events in the request--must be less than 256KB. You can calculate the
entry size before you send the events.

###### Note

The size limit is imposed on the _entry_. Even if the entry is less
than the size limit, the _event_ in EventBridge is always larger than the
entry size due to the necessary characters and keys of the JSON representation of the
event. For more information, see [Events in Amazon EventBridge](eb-events.md "eb-events.md").

EventBridge calculates the `PutEventsRequestEntry` size as follows:

- If specified, the `Time` parameter is 14 bytes.
- The `Source` and `DetailType` parameters are the number of
  bytes for their UTF-8 encoded forms.
- If specified, the `Detail` parameter is the number of bytes for its
  UTF-8 encoded form.
- If specified, each entry of the `Resources` parameter is the number of
  bytes for its UTF-8 encoded forms.

The following example Java code calculates the size of a given
`PutEventsRequestEntry` object. In order to verify the 256KB limit is not violated, you need to perform the calculation for all events in a request.

```
int getSize(PutEventsRequestEntry entry) {
    int size = 0;
    if (entry.getTime() != null) {
        size += 14;
    }
    size += entry.getSource().getBytes(StandardCharsets.UTF_8).length;
    size += entry.getDetailType().getBytes(StandardCharsets.UTF_8).length;
    if (entry.getDetail() != null) {
        size += entry.getDetail().getBytes(StandardCharsets.UTF_8).length;
    }
    if (entry.getResources() != null) {
        for (String resource : entry.getResources()) {
            if (resource != null) {
                size += resource.getBytes(StandardCharsets.UTF_8).length;
            }
        }
    }
    return size;
}
```

###### Note

If the entry size is larger than 256KB, we recommend uploading the event to an Amazon S3 bucket and including the `Object URL` in the `PutEvents` entry.
