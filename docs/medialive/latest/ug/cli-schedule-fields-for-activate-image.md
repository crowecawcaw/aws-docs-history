# Activate global image

action – payload

For information about the meaning and values for the fields in the following
JSON, see [Fields for activating a
global image overlay](schedule-fields-for-activate-image.md "schedule-fields-for-activate-image.md").

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
    "StaticImageActivateSettings": {
     "Duration": integer,
     "FadeIn": integer,
     "FadeOut": integer,
     "Height": integer,
     "Image": {
      "PasswordParam": "string",
      "Uri": "string",
      "Username": "string"
     },
     "ImageX": integer,
     "ImageY": integer,
     "Layer": integer,
     "Opacity": integer,
     "Width": integer
     }
    }
   }
  ]
 }
}
```

## Example

This example of a request creates an image overlay to be inserted in every
video output in every output group in the channel. The overlay uses a file
that is stored in an Amazon S3 bucket. The request doesn't include a duration and
therefore doesn't include a fadeout. Instead, the intention is to send a
separate deactivate request at the appropriate time. All the times are in
milliseconds, and all the positioning values are in pixels:

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
      "ActionName": "corporate-logo-030",
      "ScheduleActionSettings": {
        "StaticImageActivateSettings": {
          "Image": {
          "PasswordParam": "corplogo!2312",
          "Uri": "s3ssl://amzn-s3-demo-bucket/logos/corporate/high-res.bmp",
          "Username": "medialiveoperator"
          },
          "Layer": 1,
          "FadeIn": 1500,
          "Height": 900
          "Width": 800,
          "ImageX": 200,
          "ImageY": 300,
          "Opacity": 60,
          }
        }
      }
    ]
  }
}

```
