# Event metrics and attribution reports

To monitor the type and number of events sent to Amazon Personalize, use
Amazon CloudWatch metrics. For more information, see [Monitoring Amazon Personalize with Amazon CloudWatch](personalize-monitoring.md "personalize-monitoring.md").

To generate CloudWatch reports that show the impact of recommendations,
create a metric attribution and record user interactions with real-time recommendations. For information on
creating a metric attribution, see [Measuring the impact of Amazon Personalize recommendations](measuring-recommendation-impact.md "measuring-recommendation-impact.md").

For each event, include recommendation ID of the recommendations you showed the user. Or include
the event source, such as a third party. Import this data to compare different campaigns, recommenders, and third parties.
You can import at most 100 event attribution sources.

- If you provide a `recommendationId`, Amazon Personalize automatically determines the source campaign or recommender and identifies it in reports
  in an EVENT_ATTRIBUTION_SOURCE column.
- If you provide both attributes,
  Amazon Personalize uses only the `eventAttributionSource`.
- If you don't provide a source, Amazon Personalize labels the source `SOURCE_NAME_UNDEFINED` in reports.

The following code shows how to provide an `eventAttributionSource` for an event in a PutEvents operation.

```
response = personalize_events.put_events(
    trackingId = '`eventTrackerId`',
    userId= '`userId`',
    sessionId = '`sessionId123`',
    eventList = [{
        'eventId': '`event1`',
        'eventType': '`watch`',
        'sentAt': '`1667260945`',
        'itemId': '`123`',
        'metricAttribution': {
            'eventAttributionSource': '`thirdPartyServiceXYZ`'
        }
    }]
)
statusCode = response['ResponseMetadata']['HTTPStatusCode']
print(statusCode)
```

The following code shows how to provide a `recommendationId` for an event in a PutEvents operation.

```
response = personalize_events.put_events(
    trackingId = '`eventTrackerId`',
    userId= '`userId`',
    sessionId = '`sessionId123`',
    eventList = [{
        'eventId': '`event1`',
        'eventType': '`watch`',
        'sentAt': '`1667260945`',
        'itemId': '`123`',
        'recommendationId': '`RID-12345678-1234-1234-1234-abcdefghijkl`'
    }]
)
statusCode = response['ResponseMetadata']['HTTPStatusCode']
print(statusCode)
```
