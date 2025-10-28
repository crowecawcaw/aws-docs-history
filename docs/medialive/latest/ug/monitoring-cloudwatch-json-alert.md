# JSON for an

alert event

Events that are based on [alerts](monitor-activity-types-alerts-channels.md "monitor-activity-types-alerts-channels.md") are identified by their
`detail-type` property:

- `MediaLive Channel Alert` for a
  channel

- `MediaLive Multiplex Alert` for a
  multiplex.
  **Example**

Following is an example of the JSON payload for an alert
event. Note the `detail-type` in line 3.

```
{
    "version": "0",
    "id": "154769fb-9f7c-32a1-6822-26fppppe5a58",
    "detail-type": "MediaLive Channel Alert",
    "source": "aws.medialive",
    "account": "111122223333",
    "time": "2023-03-08T18:14:25Z",
    "region": "us-west-2",
    "resources": [
        "arn:aws:medialive:us-west-2:111122223333:channel:123456"
    ],
    "detail": {
        "alarm_state": "CLEARED",
        "alarm_id": "7ad616bd389832yue90aab1324bffab5b834a",
        "alert_type": "Failed to Create Output File or Socket",
        "pipeline": "0",
        "channel_arn": "arn:aws:medialive:us-west-2:111122223333:channel:123456",
        "message": "MPEGTS muxer for mediaID [1] unable to open output or stream [https://`<path>`]."
    }
}
```
