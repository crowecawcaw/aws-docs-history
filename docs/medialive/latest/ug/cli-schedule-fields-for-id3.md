# ID3 metadata item –

payload

For information about the meaning and values for the fields in the following
JSON, see [Fields for ID3
metadata](schedule-fields-for-id3-userdata.md "schedule-fields-for-id3-userdata.md").

**Payload for the HlsTimedMetadataSettings
action**

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
     "HlsTimedMetadataSettings": {
     "Id3": "string"
    }
   }
  }
 ]
}

```

**Payload for the TimedMetadataSettings
action**

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
     "TimedMetadataSettings": {
     "Id3": "string"
    }
   }
  }
 ]
}

```

## Example

This example of a request
uses the
`HlsTimedMetadataSettings` action. It
creates ID3 metadata to be inserted
in a
appropriate output groups at 13:35:59 UTC.

```
{
  "ChannelId": "999999",
  "Creates": {
  "ScheduleActions": [
    {
      "ScheduleActionStartSettings": {
        "FixedModeScheduleActionStartSettings": {
          "Time": "2019-01-02T13:35:59Z"
        }
      },
      "ActionName": "id3-metadata.2019-01-02T13:35:59Z",
      "ScheduleActionSettings": {
        "HlsTimedMetadataSettings": {
          "Id3": "SUQzBAAAAAAAF1RJVDIAAAANAAADSGVsbG8gV29ybGQA"
          }
        }
      }
    ]
  }
}

```
