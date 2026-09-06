

# Recording multiple item interaction events with event value data
<a name="recording-events-example-event-value"></a>

After you create an *Item interactions dataset* and an [event tracker](event-get-tracker.md) for your dataset group, you are ready to record item interaction events. The following example shows how to record multiple item interaction events with different event types and different event values.

 When you configure a solution, if your *Item interactions dataset* includes EVENT\_TYPE and EVENT\_VALUE fields, you can set a specific value as a threshold to exclude records from training. For more information, see [Choosing the item interaction data used for training](event-values-types.md). 

------
#### [ Python ]

```
import boto3
import json

personalize_events = boto3.client(service_name='personalize-events')

personalize_events.put_events(
    trackingId = '{{tracking_id}}',
    userId= 'user555',
    sessionId = 'session1',
    eventList = [{
        'eventId': 'event1',
        'sentAt': 1553631760,
        'eventType': 'like',
        'properties': json.dumps({
            'itemId': 'choc-panama',
            'eventValue': 4
            })
        }, {
        'eventId': 'event2',
        'sentAt': 1553631782,
        'eventType': 'rating',
        'properties': json.dumps({
            'itemId': 'movie_ten',
            'eventValue': 3
            })
        }]
)
```

------
#### [ AWS CLI ]

```
aws personalize-events put-events \
    --tracking-id {{tracking_id}} \
    --user-id user555 \
    --session-id session1 \
    --event-list '[{
        "eventId": "event1",
        "sentAt": 1553631760,
        "eventType": "like",
        "properties": "{\"itemId\": \"choc-panama\", \"eventValue\": \"true\"}"
      }, {
        "eventId": "event2",
        "sentAt": 1553631782,
        "eventType": "rating",
        "properties": "{\"itemId\": \"movie_ten\", \"eventValue\": \"4\", \"numRatings\": \"13\"}"
      }]'
```

------
#### [ SDK for Java 2.x ]

```
public static void putMultipleEvents(PersonalizeEventsClient personalizeEventsClient, 
                            String trackingId, 
                            String sessionId, 
                            String userId, 
                            String event1Type, 
                            Float event1Value, 
                            String event1ItemId,
                            int event1NumRatings,
                            String event2Type, 
                            Float event2Value, 
                            String event2ItemId,
                            int event2NumRatings) {  
                                                    
    ArrayList<Event> eventList = new ArrayList<Event>();
                        
    try {
        Event event1 = Event.builder()
            .eventType(event1Type)
            .sentAt(Instant.ofEpochMilli(System.currentTimeMillis() + 10 * 60 * 1000))
            .itemId(event1ItemId)
            .eventValue(event1Value)
            .properties("{\"numRatings\": "+ event1NumRatings +"}")
            .build(); 

        eventList.add(event1); 

        Event event2 = Event.builder()
            .eventType(event2Type)
            .sentAt(Instant.ofEpochMilli(System.currentTimeMillis() + 10 * 60 * 1000))
            .itemId(event2ItemId)
            .eventValue(event2Value)
            .properties("{\"numRatings\": "+ event2NumRatings +"}")
            .build();

        eventList.add(event2);

        PutEventsRequest putEventsRequest = PutEventsRequest.builder()
            .trackingId(trackingId)
            .userId(userId)
            .sessionId(sessionId)
            .eventList(eventList)
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

------

**Note**  
The properties keys use camel case names that match the fields in the Interactions schema. For example, if the field 'NUM\_RATINGS' is defined in the Interactions schema, the property key should be `numRatings`.