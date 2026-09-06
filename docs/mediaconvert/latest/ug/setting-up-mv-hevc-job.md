

# Job settings to create an MV-HEVC output
<a name="setting-up-mv-hevc-job"></a>

To set up a job with an MV-HEVC output, you create the output in the File group output group. Then you specify MP4 or MOV as the output container, choose H.265 as the video codec, and configure `multiViewSettings` on your inputs to provide the right eye enhancement layer.

1. Use the **File group** output group to add your MV-HEVC outputs. For general job setup information, see [Tutorial: Configuring job settings](setting-up-a-job.md).

1. On the **Create job** page, in the **Job** pane on the left, choose your input.

1. For **Input file URL**, specify the S3, HTTP, or HTTPS path to your left eye (base layer) video file.

1. Toggle the **Multi View - Enhancement Layers** button for that input.

1. For the multi-view input **File URL**, specify the S3, HTTP, or HTTPS path to your right eye (enhancement layer) video file.
**Note**  
Both input files must have the same resolution, frame rate, and number of frames. The left eye file is the primary input and serves as the base layer. The right eye file is the enhancement layer.

1. If your job has multiple inputs, repeat steps 2–5 for each input. All inputs in the job must have `multiViewSettings` configured.

1. In the **Job** pane on the left, choose your output.

1. In the **Output settings** section, for **Container**, choose **MPEG-4 container (MP4)** or **QuickTime container (MOV)**.

1. In the **Encoding settings** section, for **Video codec**, choose **H.265 (HEVC)**.

1. Configure your H.265 encoding settings as needed. For information about supported encoding configurations, see [Supported encoding settings](mv-hevc-supported-encoding.md).

If you use the API, CLI, or an SDK, specify the relevant settings in your JSON job specification and then submit it programmatically. We recommend using the MediaConvert console to generate your JSON job specification, because the console functions as an interactive validator against the MediaConvert job schema.

The following example shows the key parts of a JSON job specification for an MV-HEVC output. The left eye video is specified as the primary `FileInput`, and the right eye video is specified in `MultiViewSettings`.

```
{
  "Inputs": [
    {
      "FileInput": "s3://DOC-EXAMPLE-BUCKET/left_eye.mp4",
      "AudioSelectors": {
        "Audio Selector 1": {
          "ProgramSelection": 1,
          "Offset": 0
        }
      },
      "MultiViewSettings": [
        {
          "Input": {
            "FileInput": "s3://DOC-EXAMPLE-BUCKET/right_eye.mp4"
          }
        }
      ]
    }
  ],
  "OutputGroups": [
    {
      "OutputGroupSettings": {
        "Type": "FILE_GROUP_SETTINGS",
        "FileGroupSettings": {
          "Destination": "s3://DOC-EXAMPLE-BUCKET/output/"
        }
      },
      "Outputs": [
        {
          "NameModifier": "_mv",
          "VideoDescription": {
            "CodecSettings": {
              "Codec": "H_265",
              "H265Settings": {
                "RateControlMode": "CBR",
                "Bitrate": 5000000,
                "CodecProfile": "MAIN10_MAIN"
              }
            }
          },
          "ContainerSettings": {
            "Container": "MP4"
          }
        }
      ]
    }
  ],
  "TimecodeConfig": {
    "Source": "ZEROBASED"
  }
}
```