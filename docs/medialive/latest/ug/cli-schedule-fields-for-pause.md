

# Pause pipeline action – payload
<a name="cli-schedule-fields-for-pause"></a>

For information about the meaning and values for the fields in the following JSON, see [Fields for pause](schedule-fields-for-pause.md).

```
{
 "ScheduleActions": [
  {
   "ScheduleActionStartSettings": {
    "FixedModeScheduleActionStartSettings": {
     "Time": "string"
    },
    "ImmediateModeScheduleActionStartSettings": {
    }
   },
   "ActionName": "string",
   "ScheduleActionSettings": {
    "PauseStateSettings": {
     "Pipelines": [
      {
       "PipelineId": "enum"
      }
     ]
    }
   }
  }
 ]
}
```

## Example: Pausing one pipeline
<a name="json-pause-example"></a>

This example of a request pauses pipeline 0 at 20:42:19 UTC. MediaLive always reads the command as:*set the specified pipeline or pipelines to pause and set all other pipelines to unpaused.*

```
{
  "ChannelId": "999999",
  "Creates": {
    "ScheduleActions": [
      {
        "ScheduleActionStartSettings": {
          "FixedModeScheduleActionStartSettings": {
            "Time": "2018-05-21T20:42:19Z"
          }
        },
        "ActionName": "pause-pipeline-0-now",
        "ScheduleActionSettings": {
          "PauseStateSettings": {
            "Pipelines": [
              {
                "PipelineId": "PIPELINE_0"
              }
            ]
          }
        }
      }
    ]
  }
}
```

## Example: Unpausing both pipelines
<a name="json-unpause-example"></a>

This example of a request unpauses all pipelines that are currently paused. 

**Note**  
MediaLive always reads the command as:*set the specified pipeline or pipelines to pause and set all other pipelines to unpaused.* In this example, the `Pipelines` array is empty. MediaLive interprets this empty array as: *set all pipelines to unpaused*.

```
{
 "ChannelId": "999999",
 "Creates": {
     "ScheduleActions": [
      {
       "ScheduleActionStartSettings": {
         "ImmediateModeScheduleActionStartSettings": {}
      },
     "ActionName": "unpause-pipeline-0",
     "ScheduleActionSettings": {
       "PauseStateSettings": {
         "Pipelines": [
       {}
      ]
     }
    }
   }
  ]
 }
}
```