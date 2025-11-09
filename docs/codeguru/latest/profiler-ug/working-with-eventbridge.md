# Working with Amazon EventBridge

This section helps you get started using Amazon EventBridge with Amazon CodeGuru Profiler.

CodeGuru Profiler sends events to EventBridge. An event indicates a change in a recommendation that CodeGuru Profiler
identified. CodeGuru Profiler sends a heartbeat event every 24 hours to show the continuity of the event.
Events carry CodeGuru Profiler recommendation information as well as metadata for your compute resources.
For information on an event lifecycle, see [Amazon EventBridge Events](../../../eventbridge/latest/userguide/eb-events.md "../../../eventbridge/latest/userguide/eb-events.md").

Events are only sent to EventBridge for Lambda compute platforms. For compute types that are
not Lambda, use the `GetRecommendations` API to see changes to recommendations that CodeGuru Profiler identifies.

###### Note

CodeGuru Profiler doesn't yet support localization. The default locale is `en_US`.

An event bus receives events from a source such as CodeGuru Profiler and routes them to rules
associated with that event bus. For more information on event buses, see [Event
buses](../../../eventbridge/latest/userguide/eb-event-bus.md "../../../eventbridge/latest/userguide/eb-event-bus.md").

The following table explains some of the parameters you might find in the
`detail` object. For more information, see [Amazon EventBridge events](../../../eventbridge/latest/userguide/eb-events.md "../../../eventbridge/latest/userguide/eb-events.md").

| Parameter             | Description                                                                                                                                                                                              |
| --------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `schema`              | The schema version.                                                                                                                                                                                      |
| `expiresOn`           | The ISO 8601 timestamp, after which the event expires.                                                                                                                                                   |
| `sourceUrl`           | The CodeGuru Profiler console URL where you can see more details about your<br>recommendations.                                                                                                          |
| `deduplicationId`     | This is used to elimate duplicated copies of events related to the current event.<br>In a typical event, you should see an `ONGOING` event every day, followed<br>by a `CLOSED` event when event closes. |
| `severity`            | The severity of the event. Only `MEDIUM` severity events are<br>sent.                                                                                                                                    |
| `status`              | Shows the status of an event. Possible statuses are `ONGOING` and<br>`CLOSED`.                                                                                                                           |
| `computeInstanceArns` | Information about the compute instances that are used for the profiled<br>applications.                                                                                                                  |
| `recommendation`      | Shows information such as the recommendation name, details, and a resolution<br>path.                                                                                                                    |

The following sample event shows a CodeGuru Profiler recommendations state change. The
`detail-type` shows a brief description of the event. The `account`
shows the user's account number.

```
{
    "version": "0",
    "id": "315c1398-40ff-a850-213b-158f73e60175",
    "detail-type": "CodeGuru Profiler Recommendations State Change",
    "source": "aws.codeguru-profiler",
    "account": "012345678912",
    "time": "2019-02-26T19:42:21Z",
    "region": "us-east-1",
    "resources": [
        "arn:aws:codeguru-profiler:us-east-1:012345678912:profilingGroup:profiling-group-name"
    ],
    "detail": {
        "schema": "2021-08-30",
        "expiresOn": "2019-02-27T19:42:21Z",
        "sourceUrl": "/codeguru/profiler/recommendations-report?endTime=2019-02-27T00%3A00%3A00.000Z&profilingGroupName=profiling-group-name&region=us-east-1&startTime=2019-02-26T00%3A00%3A00.000Z",
        "deduplicationId": "ada4cvf74uyrponkgk7tpxeo5idgqcrt",
        "title": {"value": "Issue name"},
        "eventStartTime": "2019-02-26T19:42:21Z",
        "eventEndTime": "2019-02-29T19:50:34Z", //Could be null until event closes
        "severity": "MEDIUM",
        "status": "ONGOING",
        "computeInstanceArns": ["arn:aws:lambda:us-east-1:012345678912:function:lambda-function"],
        "recommendation" : {
            "name": {
                "value": "Fix issue"
            },
            "description": {
                "value": "Description of the issue"
            },
            "resolutionSteps": {
                "value": "Fix the issue by following step 1, step 2 and step 3"
            },
            "reason": {
                "value": "Observed the issue because it used more CPU than ideal"
            },
        }
    }
}
```
