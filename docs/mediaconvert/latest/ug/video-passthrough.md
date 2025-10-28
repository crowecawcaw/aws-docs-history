# Video passthrough

MediaConvert supports video passthrough for **AVC (H.264)**, **HEVC (H.265)**, and
**I-frame only** inputs. For AVC and HEVC inputs, you can create
an output with any supported container type. For I-frame only inputs, you can
create MXF or QuickTime outputs. Use video passthrough to repackage one or more inputs
without any video encoding.

When you use video passthrough, you can repackage your input video but you cannot re-encode or otherwise modify the video
essence.

## Using video passthrough

The following sections describe how to configure your job settings with Video
passthrough.

To specify Video passthrough using the MediaConvert console:

1. Open the [Create
   job](https://console.aws.amazon.com/mediaconvert/home#/jobs/create "https://console.aws.amazon.com/mediaconvert/home#/jobs/create") page in the MediaConvert console.
2. On the **Create job** page, provide transcode instructions and job
   settings. For more information, see [Tutorial: Configuring job settings](setting-up-a-job.md "setting-up-a-job.md").
3. Specify one or more supported inputs. If you specify multiple
   inputs, each of your input's encoding attributes must exactly match,
   including video codec, frame size, profile, frame rate, and color
   space.
4. Next to **Output groups**, select
   **Add** .
5. Keep **File group** selected and
   choose **Select**.
6. In the **Output settings**, choose a
   **Container**. Note: If your input
   has an I-frame only video codec, you must choose **QuickTime** or **MXF**.
7. In **Encoding** settings, under
   **Video codec**, choose **Passthrough**.
   The following is an excerpt of a job settings JSON that specifies Video
   passthrough for an Apple ProRes workflow with two inputs:

```
{
  "Settings": {
    "Inputs": [
      {
        "FileInput": "s3://amzn-s3-demo-bucket/prores.mov"
      },
      {
        "FileInput": "s3://amzn-s3-demo-bucket/prores-2.mov"
      }
    ],
    "OutputGroups": [
      {
        "Name": "File Group",
        "OutputGroupSettings": {
          "Type": "FILE_GROUP_SETTINGS",
          "FileGroupSettings": {
            "Destination": "s3://amzn-s3-demo-bucket/passthrough-output.mov"
          }
        },
        "Outputs": [
          {
            "VideoDescription": {
              "CodecSettings": {
                "Codec": "PASSTHROUGH"
              }
            },
            "ContainerSettings": {
              "Container": "MOV",
              "MovSettings": {}
            }
          }
        ]
      }
    ]
  }
}
```
