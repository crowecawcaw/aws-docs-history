# Cancel a pending ad

avail

If you inserted an ad avail the start time has not yet passed, you can cancel the
insertion. No SCTE-35 message will be inserted.

**HTTP URL**

```
POST <IP address of Live node>/live_events/<ID of event>/cue_point
```

**Body of HTTP**

The XML body contains one `cue_point` element containing the following
tag:

| Tag             | Sub-tag | Type    | Value                                         |
| --------------- | ------- | ------- | --------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| cancel_event_id |         | integer | The event ID of the original SCTE-35 request. | **Response** The response includes a message that identifies the event ID of the original request. ## Cancel a Pending Ad Avail Example The following shows a request to cancel the insertion of a pending ad avail in the event with the ID 4. The original SCTE-35 ad avail has an ID of 38: `POST 10.4.136.96/live_events/4/cue_point ---------------------------------------- <cue_point> <cancel_event_id>38</cancel_event_id> </cue_point>` The following shows an example response for the request: `<response> <tag>13</tag> <event_id>5</event_id> <message>Canceled eventID [5]</message> <value>cue_point</value> </response>` |
