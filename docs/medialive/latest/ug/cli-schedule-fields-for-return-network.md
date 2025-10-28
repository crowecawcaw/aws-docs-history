# Return-to-network message – payload

For information about the meaning and values for the fields in the following
JSON, see [Fields for a
return-to-network message](schedule-fields-for-return-to-network.md "schedule-fields-for-return-to-network.md").

```
{
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
    "Scte35ReturnToNetworkSettings": {
     "SpliceEventId": integer
    }
   }
  }
 ]
}

```

## Example

This example of a request creates a return-to-network
with a UTC start time of 20:42:19.

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
      "ActionName": "end-adavail-3708",
      "ScheduleActionSettings": {
        "Scte35ReturnToNetworkSettings": {
          }
        }
      }
    ]
  }
}

```
