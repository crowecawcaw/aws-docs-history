# Deactivate motion graphic

overlay – payload

For information about the meaning and values for the fields in the following
JSON, see [Fields for deactivating a
motion graphics overlay](schedule-fields-for-mg-deactivate.md "schedule-fields-for-mg-deactivate.md").

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
    "MotionGraphicsImageDeactivateSettings": {
     }
    }
   }
  ]
 }
}

```

## Example

This example of a request creates an action to end a
motion graphic overlay at 23:59:00.000 (UTC). :

```
{
"ChannelId": "999999",
"Creates": {
 "ScheduleActions": [
  {
  "ScheduleActionStartSettings": {
   "FixedModeScheduleActionStartSettings": {
   "Time": "2018-05-21T23:59:00.000Z"
   },
   "ActionName": "deactivate-ticker-tape",
   "ScheduleActionSettings": {
    "MotionGraphicsImageDeactivateSettings": {
     }
    }
   }
  ]
 }
}

```
