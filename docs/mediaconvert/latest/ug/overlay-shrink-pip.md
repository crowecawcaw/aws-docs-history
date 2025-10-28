# How to shrink content during ad playback

(picture-in-picture)

The following procedure describes how to reduce the size of your primary content (to
20 percent) while displaying an advertisement in full screen. In steps 3 through 7, you
specify a full screen ad. In steps 8 through 12, you temporarily shrink your base input
video.

###### To add a video overlay by using the MediaConvert console:

1. Open the [Create job](https://console.aws.amazon.com/mediaconvert/home#/jobs/create "https://console.aws.amazon.com/mediaconvert/home#/jobs/create") page in the MediaConvert console.
2. Specify an input video. For more information, see _Step 1: Input files_ in [Configuring jobs](setting-up-a-job.md#specify-input-settings "setting-up-a-job.md#specify-input-settings").
3. In the settings for your input, next to **Video
   overlays**, choose **Add overlay**.
4. Specify an Input file URL for your ad file.
5. Specify a **Start timecode**.
6. Specify an **End timecode**.
7. Optionally add any **Input clips** for your video
   overlay.
8. Add a separate overlay by choosing **Add overlay**.
   This overlay provides the animated resizing transitions for your base
   input video.
9. Choose **Add transition**.
10. In the **Transition**, specify the following:
    **Height**: 20, **Width**: 20,
    **X position**: 75, **Y
    position**: 75, specify a **Start timecode**,
    and specify an **End timecode**.
11. Choose **Add transition**.
12. In the **Transition**, specify the following:
    **Height**: 100, **Width**: 100,
    **X position**: 0, **Y position**:
    0, specify a **Start timecode** some time after the
    previous transition, and specify an **End
    timecode**.
    To specify a video overlay using the API, SDK, or AWS Command Line Interface (AWS CLI), include
    `VideoOverlays` in your job settings JSON.

The following is an excerpt of a job settings JSON that specifies a full
screen ad and temporarily reduces the size of your base input video:

```
{
  "Settings": {
    "Inputs": [
      {
        "VideoOverlays": [
          {
            "EndTimecode": "00:00:18:00",
            "InitialPosition": {
              "Height": 100,
              "Unit": "PERCENTAGE",
              "Width": 100,
              "XPosition": 0,
              "YPosition": 0
            },
            "Input": {
              "FileInput": "s3://amzn-s3-demo-bucket/advertisement.mp4",
              "InputClippings": [
                {
                  "EndTimecode": "00:01:15:02",
                  "StartTimecode": "00:00:45:00"
                }
              ],
              "TimecodeSource": "ZEROBASED"
            },
            "StartTimecode": "00:00:13:00"
          },
          {
            "Transitions": [
              {
                "EndPosition": {
                  "Height": 20,
                  "Unit": "PERCENTAGE",
                  "Width": 20,
                  "XPosition": 75,
                  "YPosition": 75
                },
                "EndTimecode": "00:00:13:40",
                "StartTimecode": "00:00:13:00"
              },
              {
                "EndPosition": {
                  "Height": 100,
                  "Unit": "PERCENTAGE",
                  "Width": 100,
                  "XPosition": 0,
                  "YPosition": 0
                },
                "EndTimecode": "00:00:18:00",
                "StartTimecode": "00:00:17:40"
              }
            ]
          }
        ]
      }
    ]
  }
}

```
