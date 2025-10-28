# Recording

item interaction events with impressions data

If you use the [User-Personalization](native-recipe-new-item-USER_PERSONALIZATION.md "native-recipe-new-item-USER_PERSONALIZATION.md")
recipe or add the IMPRESSIONS field to your schema for a dataset in a
Domain dataset group, you can record impressions data in your PutEvents
operation. Impressions are lists of items that were visible to a user when
they interacted with (for example, clicked or watched) a particular item.
Amazon Personalize uses impressions data to guide exploration, where recommendations
include items with less interactions data or relevance. For information on
the _implicit_ and _explicit_
impressions Amazon Personalize can model, see [Impressions data](interactions-datasets.md#interactions-impressions-data "interactions-datasets.md#interactions-impressions-data").

###### Important

If you provide conflicting implicit and explicit impression data in
your `PutEvents` requests, Amazon Personalize uses the explicit
impressions by default.

To record the Amazon Personalize recommendations you show your user as impressions
data, include the `recommendationId` in your
[PutEvents](API_UBS_PutEvents.md "API_UBS_PutEvents.md") request
and Amazon Personalize derives the implicit impressions based on your recommendation
data.

To manually record impressions data for an event, list the impressions
in the [PutEvents](API_UBS_PutEvents.md "API_UBS_PutEvents.md") command's `impression` input parameter. The following code
sample shows how to include a `recommendationId` and an
`impression` in a PutEvents operation with either the
SDK for Python (Boto3) or the SDK for Java 2.x. If you include both, Amazon Personalize uses the explicit
impressions by default.

SDK for Python (Boto3)

```
import boto3

personalize_events = boto3.client(service_name='personalize-events')

personalize_events.put_events(
    trackingId = '`tracking_id`',
    userId= '`userId`',
    sessionId = '`sessionId`',
    eventList = [{
        'eventId': '`event1`',
        'eventType': '`rating`',
        'sentAt': `1553631760`,
        'itemId': '`item id`',
        'recommendationId': '`recommendation id`',
        'impression'`: ['`itemId1`', '`itemId2`', '`itemId3`'`]
        }]
)
```

SDK for Java 2.x
Use the following `putEvents` method to record an
event with impressions data and a recommendationId. For the
impressions parameter, pass the list of itemIds as an
ArrayList.

```
public static void putEvents(PersonalizeEventsClient personalizeEventsClient,
                                String trackingId,
                                String sessionId,
                                String userId,
                                String eventType,
                                Float eventValue,
                                String itemId,
                                ArrayList<String> impressions,
                                String recommendationId) {

    try {
        Event event = Event.builder()
            .eventType(eventType)
            .sentAt(Instant.ofEpochMilli(System.currentTimeMillis() + 10 * 60 * 1000))
            .itemId(itemId)
            .eventValue(eventValue)
            .impression(impressions)
            .recommendationId(recommendationId)
            .build();

        PutEventsRequest putEventsRequest = PutEventsRequest.builder()
            .trackingId(trackingId)
            .userId(userId)
            .sessionId(sessionId)
            .eventList(event)
            .build();

        int responseCode = personalizeEventsClient.putEvents(putEventsRequest)
            .sdkHttpResponse()
            .statusCode();
        System.out.println("Response code: " + responseCode);

    } catch (PersonalizeEventsException e) {
        System.out.println(e.awsErrorDetails().errorMessage());
    }
}
```
