# Input

prepare action – payload

The following sections show the payload for input switch
actions.

In this payload, the
`ScheduleActionStartSettings` contains only
one of `FixedModeScheduleActionStartSettings`,
`ImmediateModeScheduleActionStartSettings`,
or
`FollowModeScheduleActionStartSettings`.

See the examples that follow for samples of each of these
tags.

For information about the meaning and values for the fields in the following
JSON, see [Fields for an input switch](schedule-fields-for-ips.md "schedule-fields-for-ips.md").

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
    "FollowModeScheduleActionStartSettings": {
     "FollowPoint": "enum",
     "ReferenceActionName": "string"
    },
    "ImmediateModeScheduleActionStartSettings": {
    }
   },
   "ActionName": "string",
   "ScheduleActionSettings": {
    "InputPrepareSettings": {
     "InputAttachmentNameReference": "string",
     "InputClippingSettings": {
      "InputTimecodeSource": "enum",
      "StartTimecode": {
       "Timecode": "string"
      },
      "StopTimecode": {
       "LastFrameClippingBehavior": "enum",
       "Timecode": "string"
      }
     },
     "UrlPath": ["string", ...]
     }
    }
   }
  ]
 }
}
```

## Example of an

input prepare with a fixed start time

This example of a request is to switch to a live input
at a fixed start time. The switch action is called
`studio-feed` and it switches to the
input that is connected to the input attachment called
`live-studio-feed`. It switches to this
input at the specified UTC time.

```
{
  "ChannelId": "999999",
  "Creates": {
    "ScheduleActions": [
      {
       "ScheduleActionStartSettings": {
          "FixedModeScheduleActionStartSettings": {
            "Time": "2018-05-21T20:42:19.000Z"
           }
          },
      "ActionName": "studio-feed",
      "ScheduleActionSettings": {
        "InputSwitchSettings": {
          "InputAttachmentNameReference": "live-studio-feed"
     }
    }
   }
  ]
 }
}
```

## Example of an

input prepare as a follow

This example of a request is to switch to a static
file input to follow the end of the previous input. The
switch action is called `action-ad-003` and
it switches to the input that is connected to the input
attachment called `zel-cafe`. It switches to
this input when the action called
`action-ad-002` ends. The file for this
action is clipped so that it ends after 30 seconds and
11 frames:

```
{
  "ChannelId": "999999",
  "Creates": {
      "ScheduleActions": [
          {
            "ScheduleActionStartSettings": {
              "FollowModeScheduleActionStartSettings": {
                "FollowPoint": "END",
                "ReferenceActionName": "action-ad-002"
              }
            },
            "ActionName": "action-ad-003",
              "ScheduleActionSettings": {
                 "InputSwitchSettings": {
                    "InputAttachmentNameReference": "zel-cafe",
                      "InputClippingSettings": {
                          "InputTimecodeSource": "ZEROBASED",
               "StopTimecode":{
                 "Timecode": "00:00:30:11",
                 "LastFrameClippingBehavior": "INCLUDE_LAST_FRAME"
              }
            }
          }
        }
      }
    ]
  }
}
```
