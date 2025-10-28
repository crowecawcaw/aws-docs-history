# Activate motion graphic

overlay – payload

For information about the meaning and values for the fields in the following
JSON, see [Fields for activating a motion graphics
overlay](schedule-fields-for-mg.md "schedule-fields-for-mg.md").

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
    "MotionGraphicsImageActivateSettings": {
     "Duration": integer
     "Url": "string"
     "Username": "string",
     "PasswordParam": "string"
    }
   }
  ]
 }
}
```

## Example

This example of a request creates a motion graphics
overlay action called mg_ticker_tape. The motion graphic
asset is stored at http://example.com/ticker\_tape.html.
This server requires user credentials. The request
doesn't include a duration. Instead, the intention is to
send a separate deactivate request at the appropriate
time.

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
   "ActionName": "mg_ticker_tape",
   "ScheduleActionSettings": {
    "MotionGraphicsImageActivateSettings": {
     "Url": "https://example.com/ticker_tape.html"
     "Username": "medialiveoperator",
     "PasswordParam": "/medialive/12345"
    }
   }
  ]
 }
}
```
