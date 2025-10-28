# Insert an end time in an existing ad avail

You can insert an end time in the following situations:

- To add an end time to a message that has not yet started if an end time was
  not initially included.
- To cut short an ad avail that is in progress. The command can be used in
  this way if no end time was initially included or if it was included but you
  want to end early.
  **HTTP URL**

```
PUT <IP address of Live node>/live_events/<ID of event>/cue_point
```

**Body of HTTP**

The XML body contains one `cue_point` element containing the following
tags:

| Tag           | Sub-tag | Type    | Value                                                                                      |
| ------------- | ------- | ------- | ------------------------------------------------------------------------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| event_id      |         | integer | The event ID of the original POST cue_point (the request that did not include a duration). |
| return_offset | integer |         | The number of milliseconds to wait before inserting the ad avail.                          | ## Insert an End Time in an Existing Ad Avail Example Insert an end time immediately into the event with the ID 4. The original SCTE-35 ad avail has an ID of 38. `PUT 10.4.136.96/live_events/4/cue_point ---------------------------------------- <cue_point> <event_id>38</event_id> <return_offset>0</return_offset> </cue_point>` |
