

# How to overlay a full screen video
<a name="video-overlays-add"></a>

The following procedure describes how to display a full screen video overlay for a duration that you specify.

## MediaConvert console
<a name="collapsible-section-1"></a>

**To add a video overlay by using the MediaConvert console:**

1. Open the [Create job](https://console.aws.amazon.com/mediaconvert/home#/jobs/create) page in the MediaConvert console.

1. Specify an input video. For more information, see *Step 1: Input files* in [ Configuring jobs](setting-up-a-job.md#specify-input-settings).

1. In the settings for your input, next to **Video overlays**, choose **Add overlay**. 

1. Specify an Input file URL.

1. Specify a **Start timecode**.

1. Specify an **End timecode**.

1. Optionally add any **Input clips** for your video overlay.

## API, SDK, or AWS Command Line Interface (AWS CLI)
<a name="collapsible-section-2"></a>

To specify a video overlay using the API, SDK, or AWS Command Line Interface (AWS CLI), include `VideoOverlays` in your job settings JSON.

The following is an excerpt of a job settings JSON that specifies a full screen video overlay at timecode `00:10:00:00` for one minute from a clipped input:

```
{
  "Settings": {
    "Inputs": [
      {
        "VideoOverlays": [
          {
            "Input": {
              "FileInput": "s3://amzn-s3-demo-bucket/overlay.mp4",
              "InputClippings": [
                {
                  "StartTimecode": "00:10:00:00",
                  "EndTimecode": "00:11:00:00"
                }
              ],
              "TimecodeSource": "EMBEDDED"
            },
            "StartTimecode": "00:01:00:00",
            "EndTimecode": "00:02:00:00"
          }
        ]
      }
    ]
  }
}
```