

# Viewing source metadata for a flow
<a name="view-source-metadata-flow"></a>

View source metadata for a flow in the MediaConnect console, or by calling [DescribeFlowSourceMetadata](https://docs.aws.amazon.com/mediaconnect/latest/api/API_DescribeFlowSourceMetadata.html). For the fields returned for each source protocol, see [Source metadata field reference](source-metadata-field-reference.md).

**To view source metadata for a flow (console)**

1. Open the MediaConnect console at [https://console.aws.amazon.com/mediaconnect/](https://console.aws.amazon.com/mediaconnect/).

1. From the **Flows** screen, select the flow you want to inspect.

1. Select the **Source metadata** tab.

You can also retrieve source metadata for a flow by using the AWS CLI. The following example shows the AWS CLI command and return value for a typical scenario.

**To view source metadata for a flow (AWS CLI)**

1. In the AWS CLI, use the `describe-flow-source-metadata` command with the `--flow-arn` option of the flow you want to inspect. 

   ```
   aws mediaconnect describe-flow-source-metadata --flow-arn arn:aws:mediaconnect:us-east-1:111122223333:flow:1-23aBC45dEF67hiJ8-12AbC34DE5fG:AwardsShow
   ```

1.  The return value will contain the media information for the selected flow's source. The following is a generic example of the format of the return value. In this example, there are no messages to display.

   ```
   {
       "FlowArn": "arn:aws:mediaconnect:us-east-1:111122223333:flow:1-23aBC45dEF67hiJ8-12AbC34DE5fG:AwardsShow",
       "Messages": [],
       "Timestamp": "2023-12-06T19:57:54Z",
       "TransportMediaInfo": {
           "Programs": [
               {
                   "PcrPid": 1000,
                   "ProgramNumber": 1,
                   "ProgramPid": 2000,
                   "ProgramName": "AwardsShow HD",
                   "Streams": [
                       {
                           "Codec": "H264",
                           "FrameRate": "59.94",
                           "FrameResolution": {
                               "FrameHeight": 1080,
                               "FrameWidth": 1920
                           },
                           "Pid": 256,
                           "StreamType": "Video"
                       },
                       {
                           "Channels": 1,
                           "Codec": "AAC",
                           "Pid": 257,
                           "SampleRate": 50,
                           "SampleSize": 16,
                           "StreamType": "Audio"
                       },
                       {
                           "StreamType": "Data",
                           "Codec": "SCTE35",
                           "Pid": 258
                       }
                   ]
               }
           ]
       }
   }
   ```

## Active alerts
<a name="monitor-with-source-stream-monitoring-status-messages"></a>

The **Active alerts** section of the flow's **Source metadata** tab displays status messages about the flow's source. These messages correspond to the `Messages` field of the `DescribeFlowSourceMetadata` API/CLI response. If MediaConnect detects an issue or cannot retrieve the source stream metadata, an associated status message is displayed.

## Example: source metadata alerts
<a name="monitor-with-source-stream-monitoring-status-example"></a>

When MediaConnect detects an issue while retrieving source metadata, it returns a status code and message in the `Messages` field of the response. For example, if a transport stream contains more programs than source metadata monitoring can display, the response includes an alert and returns only the first 50 programs. The following example shows the `Messages` field for this scenario.

```
{
    "FlowArn": "arn:aws:mediaconnect:us-east-1:111122223333:flow:1-23aBC45dEF67hiJ8-12AbC34DE5fG:AwardsShow",
    "Messages": [
        {
            "Code": "MediaInfoMonitoringTruncated",
            "Message": "Program limit (50) exceeded. Monitoring only the first 50 programs of 60 in the transport stream."
        }
    ],
    "Timestamp": "2023-12-06T19:57:54Z",
    "TransportMediaInfo": {
        "Programs": [
            {
                "PcrPid": 1000,
                "ProgramNumber": 1,
                "ProgramPid": 2000,
                "ProgramName": "AwardsShow HD",
                "Streams": [
                    {
                        "Codec": "H264",
                        "FrameRate": "59.94",
                        "FrameResolution": {
                            "FrameHeight": 1080,
                            "FrameWidth": 1920
                        },
                        "Pid": 256,
                        "StreamType": "Video"
                    }
                ]
            }
            ...
        ]
    }
}
```