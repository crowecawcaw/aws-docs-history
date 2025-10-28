# Recording a single item interaction event

After you create an _Item interactions dataset_ and an [event tracker](event-get-tracker.md "event-get-tracker.md") for your dataset group,
you are ready to record item interaction events. The following example shows a `PutEvents` operation that passes one item interaction event. The
corresponding schema is shown, along with an example row from the Item interactions dataset.

Your application generates a unique `sessionId` when a user first visits your website or uses your
application. You must use the same `sessionId` in all events throughout the session. Amazon Personalize uses the
`sessionId` to associate events with the user before they log in (is anonymous). For more information, see
[Recording events for
anonymous users](recording-events.md#recording-anonymous-user-events "recording-events.md#recording-anonymous-user-events").

The event list is an array of [Event](API_UBS_Event.md "API_UBS_Event.md") objects. An
`eventType` is required for each event. If you don't have event type data, you can provide a placeholder value to satisfy the requirement.

The `trackingId` comes from the event tracker you created in [Creating an item interaction event tracker](event-get-tracker.md "event-get-tracker.md"). The `userId`, `itemId`, and `sentAt` parameters
map to the USER_ID, ITEM_ID, and TIMESTAMP fields of a corresponding historical `Interactions` dataset. For
more information, see [Creating schema JSON files for Amazon Personalize schemas](how-it-works-dataset-schema.md "how-it-works-dataset-schema.md").

**Corresponding dataset columns**

```
Dataset columns: USER_ID, ITEM_ID, TIMESTAMP, EVENT_TYPE
Example data: user123, item-xyz, 1543631760, click
```

**Code example**

SDK for Python (Boto3)

```
import boto3

personalize_events = boto3.client(service_name='personalize-events')

personalize_events.put_events(
    trackingId = '`tracking_id`',
    userId= '`USER_ID`',
    sessionId = '`session_id`',
    eventList = [{
        'sentAt': `1719511760`,
        'eventType': '`click`',
        'itemId': '`ITEM_ID`'
        }]
)
```

SDK for JavaScript v3

```
// Get service clients module and commands using ES6 syntax.
import { PutEventsCommand } from "@aws-sdk/client-personalize-events";
import { personalizeEventsClient } from "./libs/personalizeClients.js";
// Or, create the client here.
// const personalizeEventsClient = new PersonalizeEventsClient({ region: "REGION"});

// Convert your UNIX timestamp to a Date.
const sentAtDate = new Date(1613443801 * 1000); // 1613443801 is a testing value. Replace it with your sentAt timestamp in UNIX format.

// Set put events parameters.
const putEventsParam = {
  eventList: [
    /* required */
    {
      eventType: "EVENT_TYPE" /* required */,
      sentAt: sentAtDate /* required, must be a Date with js */,
      eventId: "EVENT_ID" /* optional */,
      itemId: "ITEM_ID" /* optional */,
    },
  ],
  sessionId: "SESSION_ID" /* required */,
  trackingId: "TRACKING_ID" /* required */,
  userId: "USER_ID" /* required */,
};
export const run = async () => {
  try {
    const response = await personalizeEventsClient.send(
      new PutEventsCommand(putEventsParam),
    );
    console.log("Success!", response);
    return response; // For unit tests.
  } catch (err) {
    console.log("Error", err);
  }
};
run();

```

AWS CLI

```
aws personalize-events put-events \
    --tracking-id tracking_id \
    --user-id `USER_ID` \
    --session-id session_id \
    --event-list '[{
        "sentAt": `1719511760`,
        "eventType": "`click`",
        "itemId": "`ITEM_ID`"
      }]'
```

SDK for Java 2.x

```
public static void putEvents(PersonalizeEventsClient personalizeEventsClient,
                            String trackingId,
                            String sessionId,
                            String userId,
                            String itemId,
                            String eventType) {

    try {
        Event event = Event.builder()
            .sentAt(Instant.ofEpochMilli(System.currentTimeMillis() + 10 * 60 * 1000))
            .itemId(itemId)
            .eventType(eventType)
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
