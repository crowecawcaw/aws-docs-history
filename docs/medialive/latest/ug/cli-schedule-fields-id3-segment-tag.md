# ID3 segment tag item

– payload

For information about the meaning and values for the fields in the following
JSON, see [Fields for ID3 segment
tags](schedule-fields-for-id3-segment-tags.md "schedule-fields-for-id3-segment-tags.md").

**Payload for the HlsId3SegmentTaggingSettings
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
	"HlsId3SegmentTaggingSettings": {
         "Tag": "string"
         "Id3": "string"
    }
   }
  }
 ]
}

```

**Payload for the Id3SegmentTaggingSettings
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
	"Id3SegmentTaggingSettings": {
         "Tag": "string"
         "Id3": "string"
    }
   }
  }
 ]
}

```

## Example using the tag

property

This example of a request
uses the
`HlsId3SegmentTaggingSettings` action. It
creates an ID3 segment tag to be inserted starting at
13:35:59 UTC. This example uses the `Tag` property
,
which means that you specify only the content of the `value` for
the `TXXX` field. In this example, the content is the date, time,
and number of the segment.

```
{
  "ChannelId": "999999",
  "Creates": {
  "ScheduleActions": [
    {
      "ScheduleActionStartSettings": {
        "FixedModeScheduleActionStartSettings": {
          "Time": "2020-01-02T13:35:59Z"
        }
      },
      "ActionName": "id3-datetime-and-segment",
      "ScheduleActionSettings": {
        "HlsId3SegmentTaggingSettings": {
          "Tag": "$dt$-$sn$"
          }
        }
      }
    ]
  }
}

```

## Example using the Id3

property

This example of a request creates an ID3 segment tag to be inserted
immediately. This example uses the `Id3`
property,
which means that the content is encoded as base64.

```
{
  "ChannelId": "999999",
  "Creates": {
  "ScheduleActions": [
    {
      "ScheduleActionStartSettings": {
        ImmediateModeScheduleActionStartSettings
       }
      },
      "ActionName": "id3-song309",
      "ScheduleActionSettings": {
        "HlsId3SegmentTaggingSettings": {
          "Id3": "SUQzBAAAAAAAF1RJVDIAAAANAAADSGVsbG8gV29ybGQA"
          }
        }
      }
    ]
  }
}

```
