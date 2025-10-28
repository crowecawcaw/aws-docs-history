# JSON

for a state change event

Events that are based on a change of state in a [channel or
multiplex](monitor-activity-types-channel.md "monitor-activity-types-channel.md") are identified by their `detail-type`
property:

- `MediaLive Channel State Change` for a
  channel

- `MediaLive Multiplex State Change` for a
  multiplex.
  **Example**

Following is an example of the JSON payload for a state
change event. Note the `detail-type` in line 3.

```
{
    "version": "0",
    "id": "fbcbbbe3-2541-d4a3-d819-x39f522a8ce",
    "detail-type": "MediaLive Channel State Change",
    "source": "aws.medialive",
    "account": "111122223333",
    "time": "2023-03-08T18:40:59Z",
    "region": "us-west-2",
    "resources": [
        "arn:aws:medialive:us-west-2:111122223333:channel:283886"
    ],
    "detail": {
        "channel_arn": "arn:aws:medialive:us-west-2:111122223333:channel:123456",
        "state": "DELETED",
        "message": "Deleted channel",
        "pipelines_running_count": 0
    }
}
```
