# Deactivate per-outputs overlay action – payload

For information about the meaning and values for the fields in the following
JSON, see [Fields for
deactivating a per-outputs image overlay](schedule-fields-deactivate-image-per-output.md "schedule-fields-deactivate-image-per-output.md").

```
{
 "ChannelId": "string",
 "Creates": {
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
    "StaticImageOutputDeactivateSettings": {
     "FadeOut": integer,
     "Layer": integer,
     "OutputNames"
    }
   }
  }
 ]
}

```

## Example

The deactivate action deactivates the image in the specified per-output
layer, in the specified output or outputs.

In this example, which follows on from the activate example, the action
removes all image overlays that are in per-outputs layer 4 in the output
hls-high-res.

```
{
  "ChannelId": "999999",
  "Creates": {
  "ScheduleActions": [
    {
      "ScheduleActionStartSettings": {
        "FixedModeScheduleActionStartSettings": {
          "Time": "2018-05-21T20:42:04.000Z"
        }
      },
      "ActionName": "stop-layer4-all-outputs",
      "ScheduleActionSettings": {
        "StaticImageOutputDeactivateSettings": {
          "outputNames": [
            hls-high-res
           ],
          "FadeOut": 500,
          "Layer": 4
          }
        }
      }
    ]
  }
}

```
