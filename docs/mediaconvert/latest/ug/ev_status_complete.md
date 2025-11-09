# Events with COMPLETE status

MediaConvert sends the event for `COMPLETE` when all outputs are
written to Amazon S3 without errors. It contains both warnings and output information for
the completed job. For more information about output file names and paths, see [Output file names and
paths](output-file-names-and-paths.md "output-file-names-and-paths.md").

The following JSON is an example event containing the `COMPLETE` status
for a job.

```
{
    "version": "0",
    "id": "1234abcd-12ab-34cd-56ef-1234567890ab",
    "detail-type": "MediaConvert Job State Change",
    "source": "aws.mediaconvert",
    "account": "111122223333",
    "time": "2022-12-19T19:07:12Z",
    "region": "us-west-2",
    "resources": [
        "arn:aws:mediaconvert:us-west-2::jobs/1671476818694-phptj0"
    ],
    "detail": {
        "timestamp": 1671476832124,
        "accountId": "111122223333",
        "queue": "arn:aws:mediaconvert:us-west-2:111122223333:queues/Default",
        "jobId": "1671476818694-phptj0",
        "status": "COMPLETE",
        "userMetadata": {},
        "warnings": [
            {
                "code": 000000,
                "count": 1
            }
        ],
        "outputGroupDetails": [
            {
                "outputDetails": [
                    {
                        "outputFilePaths": [
                            "s3://amzn-s3-demo-bucket/file/file.mp4"
                        ],
                        "durationInMs": 30041,
                        "videoDetails": {
                            "widthInPx": 1920,
                            "heightInPx": 1080,
                            "qvbrAvgQuality": 7.38,
                            "qvbrMinQuality": 7,
                            "qvbrMaxQuality": 8,
                            "qvbrMinQualityLocation": 2168,
                            "qvbrMaxQualityLocation": 25025
                        }
                    }
                ],
                "type": "FILE_GROUP"
            }
        ],
        "paddingInserted": 0,
        "blackVideoDetected": 10,
        "blackSegments": [
            {
                "start": 0,
                "end": 10
            }
        ]
    }
}
```

`COMPLETE` events contain additional information about your job and
outputs. The following table lists and describes the different properties available
in job event message details.

| COMPLETE event message details           | Property                    | Data type                                                                                                                                                                                                                                                                                                                                                                                 | Details |
| ---------------------------------------- | --------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------- |
| `paddingInserted`                        | integer                     | The total duration of blank frames MediaConvert inserted<br>across all outputs in your job, in milliseconds.<br>Video padding inserts blank frames to help keep audio and<br>video durations aligned. Large `paddingInserted`<br>values show that more blank frames were inserted. These values<br>also show to what extend your input audio tracks start late, or<br>end early, or both. |
| `qvbrAvgQuality`                         | float                       | The average video quality of your Quality-Defined Variable<br>Bitrate (QVBR) output.<br>Included for QVBR outputs only.                                                                                                                                                                                                                                                                   |
| `qvbrMinQuality`                         | float                       | The minimum video quality detected in your QVBR output.<br>Included for QVBR outputs only.                                                                                                                                                                                                                                                                                                |
| `qvbrMaxQuality`                         | float                       | The maximum video quality detected in your QVBR output.<br>Included for QVBR outputs only.                                                                                                                                                                                                                                                                                                |
| `qvbrMinQualityLocation`                 | integer                     | The location in your output where `qvbrMinQuality`<br>was detected, in milliseconds.<br>You can use `qvbrMinQualityLocation` while<br>reviewing your output video quality and bandwidth usage.<br>Included for QVBR outputs only.                                                                                                                                                         |
| `qvbrMaxQualityLocation`                 | integer                     | The location in your output where `qvbrMaxQuality`<br>was detected, in milliseconds.<br>You can use `qvbrMaxQualityLocation` while<br>reviewing your output video quality and bandwidth usage.<br>Included for QVBR outputs only.                                                                                                                                                         |
| `warnings`<br>code<br>count              | array<br>integer<br>integer | Any warning codes seen in the job and the number of times they<br>occurred.<br>For more information, see [Warning codes](warning_codes.md "warning_codes.md").                                                                                                                                                                                                                            |
| `blackVideoDetected`                     | integer                     | The total duration of black video frames in your outputs that<br>are also present in your inputs, in milliseconds.<br>`blackVideoDetected` does not include any black<br>frames inserted by MediaConvert.                                                                                                                                                                                 |
| `blackVideoSegments`<br>`start`<br>`end` | array<br>integer<br>integer | The location or locations in your output where black video<br>frames were detected.<br>Each segment of black video in your output is shown with its<br>own start and end.<br>`blackVideoSegments` does not include any black<br>frames inserted by MediaConvert.                                                                                                                          |
| `averageBitrate`                         | integer                     | The average bitrate of your video output, calculated by<br>dividing the duration by the total bits.                                                                                                                                                                                                                                                                                       |

You can use the following sample JSON to create an EventBridge event pattern for jobs
with a status of `COMPLETE`.

```
{
  "source": ["aws.mediaconvert"],
  "detail-type": ["MediaConvert Job State Change"],
  "detail": {
    "status": ["COMPLETE"]
  }
}
```
