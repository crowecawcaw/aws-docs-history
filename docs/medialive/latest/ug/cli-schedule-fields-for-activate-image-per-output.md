# Activate per-outputs image action – payload

For information about the meaning and values for the fields in the following
JSON, see [Fields for
activating a per-outputs image overlay](schedule-fields-activate-image-per-output.md "schedule-fields-activate-image-per-output.md").

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
    "StaticImageOutputActivateSettings": {
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
     "OutputNames": [
       {}
      ],
     "Width": integer
     }
    }
   }
  ]
 }
}
```

## Example

This example of a request creates an image overlay to be inserted in
specific outputs in the channel. The overlay uses a file that is stored in
an Amazon S3 bucket. The request inserts the image in the outputs
`hls-high-res` and `mss-high-res`.
The image is sized appropriately for the video resolution in these outputs.

The request is intended to be always present. Therefore, it is set up to
start immediately (as soon as the channel starts). All the times are in
milliseconds, and all the positioning values are in pixels:

```
{
  "ChannelId": "999999",
  "Creates": {
  "ScheduleActions": [
    {
        "ScheduleActionStartSettings":
          {
          "ImmediateModeScheduleActionStartSettings": {
          }
         },
      },
      "ActionName": "logo-1280",
      "ScheduleActionSettings": {
        "StaticImageOutputActivateSettings": {
          "Image": {
          "PasswordParam": "corplogo!2312",
          "Uri": "s3ssl://amzn-s3-demo-bucket/logos/corporate/10percent-1280.bmp",
          "Username": "medialiveoperator"
          },
          "Layer": 0,
          "outputNames": [
            hls-high-res,mss-high-res
           ],
          "ImageX": 200,
          "ImageY": 300,
          "FadeIn": 1500,
          "Opacity": 60
          }
        }
      }
    ]
  }
}

```
