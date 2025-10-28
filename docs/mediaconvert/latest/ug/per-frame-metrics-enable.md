# Generating per-frame metric reports

Configure per-frame metric reports at either the output group level or the individual
output level.

To enable per-frame metrics for an output group by using the MediaConvert console:

1. Select an **Output group**.
2. In the **Output group settings** section, enable
   **Per-frame metrics**.
3. Under **Per-frame metrics**, select one or more metrics.
   To enable per-frame metrics for an individual output by using the MediaConvert
   console:

4. Select an **Output group**.
5. Select an individual video output.
6. In the video output's **Encoding settings** section, expand
   **Per-frame metrics**.
7. Enable **Per-frame metrics**.
8. Under **Per-frame metrics**, select one or more metrics.
   To **enable Per-frame metrics** by using the API, SDK, or AWS Command Line Interface
   (AWS CLI), include the `perFrameMetrics` array in your output group settings or
   individual output settings.

The following is an excerpt of a job settings JSON that specifies per-frame metrics at the output group level:

```
...
  "outputGroups": [
    {
      "outputGroupSettings": {
        "type": "FILE_GROUP_SETTINGS",
        "fileGroupSettings": {
          "destination": "s3://amzn-s3-demo-bucket/output/"
        },
        "perFrameMetrics": [
          "PSNR",
          "SSIM",
          "MS_SSIM",
          "PSNR_HVS",
          "VMAF",
          "QVBR"
        ]
      }
    }
  ]
...
```

## Output files

When you generate per-frame metrics, MediaConvert writes CSV files to your Amazon S3 output
destination. Filenames use the following pattern:

```
[outputname]_[metric].csv
```

For example:

- `outputname_PSNR.csv`
- `outputname_SSIM.csv`
- `outputname_VMAF.csv`

Each CSV file contains frame-by-frame metrics with the following columns:

1. Frame number
2. Metric value

The files also include summary statistics at the end, showing the average, minimum, and
maximum values across all frames. Import the data into spreadsheet applications or data
analysis tools for further processing and visualization.

The following is an example PSNR per-frame metric:

```
Display_ID,Value
0,100.00
1,55.36
2,54.88
3,55.05
4,53.39
5,54.10
6,54.21
7,54.18
8,54.37
9,54.25
...
3591,40.71
3592,40.71
3593,40.58
3594,40.64
3595,40.53
3596,40.75
3597,40.64
3598,40.68
3599,40.65
3600,40.73
Average: 43.15
Min: 34.19
Max: 100.00
```
