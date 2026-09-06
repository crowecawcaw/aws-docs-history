

# How to shrink content during ad playback (merge squeeze)
<a name="overlay-shrink"></a>

The following procedure describes how to reduce the size of your primary content (to 75 percent) while displaying an advertisement beneath it. In steps 3 through 12, you specify a full screen ad. In steps 12 through 17, you temporarily shrink your base input video.

## MediaConvert console
<a name="collapsible-section-1"></a>

**To add a video overlay by using the MediaConvert console:**

1. Open the [Create job](https://console.aws.amazon.com/mediaconvert/home#/jobs/create) page in the MediaConvert console.

1. Specify an input video. For more information, see *Step 1: Input files* in [ Configuring jobs](setting-up-a-job.md#specify-input-settings).

1. In the settings for your input, next to **Video overlays**, choose **Add overlay**. 

1. Specify an Input file URL for your ad file.

1. Specify a **Start timecode**.

1. Specify an **End timecode**.

1. For **Initial position**, specify the following: **Height**: 125, **Width**: 125, **X position**: -25, **Y position**: 0, **Unit**: Percentage, specify a **Start timecode**, and specify an **End timecode**.

1. Choose **Add transition**. 

1. In the **Transition**, specify the following: **Height**: 100, **Width**: 100, **X position**: 0, **Y position**: 0, **Unit**: Percentage, specify a **Start timecode**, and specify an **End timecode**.

1. Choose **Add transition**. 

1. In the **Transition**, specify the following: **Height**: 125, **Width**: 125, **X position**: -25, **Y position**: 0, **Unit**: Percentage, specify a **Start timecode**, and specify an **End timecode**.

1. Optionally add any **Input clips** for your video overlay.

1. Add a separate overlay by choosing **Add overlay**. This overlay provides the animated resizing transitions for your base input video.

1. Choose **Add transition**. 

1. In the **Transition**, specify the following: **Height**: 75, **Width**: 75, **X position**: 25, **Y position**: 0, **Unit**: Percentage, specify a **Start timecode**, and specify an **End timecode**.

1. Choose **Add transition**.

1. In the **Transition**, specify the following: **Height**: 100, **Width**: 100, **X position**: 0, **Y position**: 0, **Unit**: Percentage, specify a **Start timecode** some time after the previous transition, and specify an **End timecode**.

## API, SDK, or AWS Command Line Interface (AWS CLI)
<a name="collapsible-section-2"></a>

To specify a video overlay using the API, SDK, or AWS Command Line Interface (AWS CLI), include `VideoOverlays` in your job settings JSON.

The following is an excerpt of a job settings JSON that specifies a full screen ad and temporarily reduces the size of your base input video:

```
{
  "Settings": {
    "Inputs": [
      {
        "VideoOverlays": [
          {
            "InitialPosition": {
              "Height": 125,
              "Unit": "PERCENTAGE",
              "Width": 125,
              "XPosition": -25,
              "YPosition": 0
            },
            "Input": {
              "FileInput": "s3://amzn-s3-demo-bucket/advertisement.mov"
            },
            "Transitions": [
              {
                "EndPosition": {
                  "Height": 100,
                  "Unit": "PERCENTAGE",
                  "Width": 100,
                  "XPosition": 0,
                  "YPosition": 0
                },
                "EndTimecode": "00:00:14:00",
                "StartTimecode": "00:00:13:00"
              },
              {
                "EndPosition": {
                  "Height": 125,
                  "Unit": "PERCENTAGE",
                  "Width": 125,
                  "XPosition": -25,
                  "YPosition": 0
                },
                "EndTimecode": "00:00:19:30",
                "StartTimecode": "00:00:18:30"
              }
            ]
          },
          {
            "Transitions": [
              {
                "EndPosition": {
                  "Height": 75,
                  "Unit": "PERCENTAGE",
                  "Width": 75,
                  "XPosition": 25,
                  "YPosition": 0
                },
                "EndTimecode": "00:00:14:00",
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
                "EndTimecode": "00:00:19:30",
                "StartTimecode": "00:00:18:30"
              }
            ]
          }
        ]
      }
    ]
  }
}
```