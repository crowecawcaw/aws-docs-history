# Configuring a job with 3D LUTs

MediaConvert only applies color space conversions with your 3D LUTs to sets of inputs and
outputs that match the settings that you specify. You can apply custom color mapping to some
of your outputs, and apply default color mapping to others.

For example, you might include a 3D LUT that specifies a **Rec.
601** input color space and a **Rec. 709** output
color space. When your job settings meet the requirements listed in the previous section, MediaConvert applies your custom color mapping for all **Rec. 601** inputs that result in **Rec. 709**
outputs.

Specify a separate 3D LUT for each combination of input and output color space conversion
that you need. In a single job, you can include up to 8 different 3D LUT settings. MediaConvert
uses default color mapping for inputs or outputs with color spaces not included in your
3D LUT or job settings.

To specify a 3D LUT by using the MediaConvert console:

1. Open the [Create
   job](https://console.aws.amazon.com/mediaconvert/home#/jobs/create "https://console.aws.amazon.com/mediaconvert/home#/jobs/create") page in the MediaConvert console.
2. On the **Create job** page, provide transcode instructions and job
   settings. For more information, see [Tutorial: Configuring job settings](setting-up-a-job.md "setting-up-a-job.md").
3. Turn on the **Color corrector** preprocessor under the **Encoding settings** of your video output.
4. Specify an output color space under **Color space conversion**.
5. Choose **Global processing** under **Job
   settings**.
6. Turn on **3D LUTs**.
7. Under **Input color space**, enter the color space for your input
   or inputs that you want to apply this 3D LUT to.
8. (Optional) If you entered **HDR10** or **P3D65 (HDR)** for **Input color space**,
   optionally enter a value for **Input mastering luminance**. Use to
   select inputs with a specific luminance. Enter the same value that you enter for
   **Maximum luminance**, which is under the input's **Video
   selector**, **Video correction**, settings.

If you enter `0` for **Input mastering luminance**, or
keep blank, your 3D LUT will apply to all of your **HDR10** or **P3D65 (HDR)** inputs. 9. Under **Output color space**, enter the color space for your output
or outputs that you want to apply this 3D LUT to. 10. (Optional) If you entered **HDR10** or **P3D65 (HDR)** for **Output color space**,
optionally enter a value for **Output mastering luminance**. Use to
select outputs with a specific luminance. Enter the same value that you enter for
**Maximum luminance**, which is under the output's **Video** settings.

If you enter `0` for **Output mastering luminance**, or
keep blank, your 3D LUT will apply to all of your **HDR10** or **P3D65 (HDR)** outputs. 11. Under **3D LUT file input**, enter the URL for your 3D LUT .cube
file.
To specify a 3D LUT by using the API, SDK, or AWS Command Line Interface (AWS CLI),
include `ColorConversion3DLUTSettings` in your job settings JSON.

The following is an excerpt of a job settings JSON that specifies a 3D LUT for an
**HDR 10** to **P3D65 (HDR)**
workflow:

```
{
  "Settings": {
    "Inputs": [...],
    "OutputGroups": [
      {
        "Name": "File Group",
        "OutputGroupSettings": {...},
        "Outputs": [
          {
            "VideoDescription": {
              "CodecSettings": {... },
              "VideoPreprocessors": {
                "ColorCorrector": {
                  "ColorSpaceConversion": "FORCE_P3D65_HDR",
                  "MaxLuminance": 3000
                }
              }
            },
            "AudioDescriptions": [...],
            "ContainerSettings": {...}
          }
        ]
      }
    ],
    "ColorConversion3DLUTSettings": [
      {
        "InputColorSpace":"HDR10",
        "InputMasteringLuminance": 0,
        "OutputColorSpace": "P3D65HDR",
        "OutputMasteringLuminance": 3000,
        "FileInput": "s3://amzn-s3-demo-bucket/HDR10_to_P3D65HDR.cube"
      }
    ]
  }
}
```
