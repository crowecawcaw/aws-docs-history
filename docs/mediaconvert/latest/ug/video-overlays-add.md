# How to overlay a full screen video

The following procedure describes how to display a full screen video overlay for a
duration that you specify.

###### To add a video overlay by using the MediaConvert console:

1. Open the [Create
   job](https://console.aws.amazon.com/mediaconvert/home#/jobs/create "https://console.aws.amazon.com/mediaconvert/home#/jobs/create") page in the MediaConvert console.
2. Specify an input video. For more information, see _Step 1: Input files_ in [Configuring jobs](setting-up-a-job.md#specify-input-settings "setting-up-a-job.md#specify-input-settings").
3. In the settings for your input, next to **Video overlays**,
   choose **Add overlay**.
4. Specify an Input file URL.
5. Specify a **Start timecode**.
6. Specify an **End timecode**.
7. Optionally add any **Input clips** for your video
   overlay.
   To specify a video overlay using the API, SDK, or AWS Command Line Interface (AWS CLI), include
   `VideoOverlays` in your job settings JSON.

The following is an excerpt of a job settings JSON that specifies a full
screen video overlay at timecode `00:10:00:00` for one minute from a
clipped input:

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
