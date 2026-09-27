

# Viewing source metadata for a router input
<a name="view-source-metadata-router-input"></a>

View source metadata for a router input in the MediaConnect console, or by calling [GetRouterInputSourceMetadata](https://docs.aws.amazon.com/mediaconnect/latest/api/API_GetRouterInputSourceMetadata.html). For the fields returned, see [Source metadata field reference](source-metadata-field-reference.md).

**To view source metadata for a router input (console)**

1. Open the MediaConnect console at [https://console.aws.amazon.com/mediaconnect/](https://console.aws.amazon.com/mediaconnect/).

1. From the **Router inputs** screen, select the router input you want to inspect.

1. Select the **Monitoring** tab.

1. Expand the **Source metadata** section.

You can also retrieve source metadata for a router input by using the AWS CLI. The following example shows the AWS CLI command and return value for a typical scenario.

**To view source metadata for a router input (AWS CLI)**

1. In the AWS CLI, use the `get-router-input-source-metadata` command with the `--arn` option of the router input you want to inspect.

   ```
   aws mediaconnect get-router-input-source-metadata --arn arn:aws:mediaconnect:us-east-1:111122223333:routerInput:a1b2c3d4e5f6
   ```

1. The return value contains the media information for the router input's source. The following is a generic example of the format of the return value. In this example, there are no messages to display.

   ```
   {
       "Arn": "arn:aws:mediaconnect:us-east-1:111122223333:routerInput:a1b2c3d4e5f6",
       "Name": "StadiumFeed",
       "SourceMetadataDetails": {
           "SourceMetadataMessages": [],
           "Timestamp": "2023-12-06T19:57:54Z",
           "RouterInputMetadata": {
               "TransportStreamMediaInfo": {
                   "Programs": [
                       {
                           "PcrPid": 1000,
                           "ProgramNumber": 1,
                           "ProgramPid": 2000,
                           "ProgramName": "StadiumFeed HD",
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
       }
   }
   ```

## Example: source metadata alerts
<a name="view-source-metadata-router-input-example"></a>

When MediaConnect detects an issue while retrieving source metadata, it returns a status code and message in the `SourceMetadataMessages` field of the response. For example, if a transport stream contains more programs than source metadata monitoring can display, the response includes an alert and returns only the first 50 programs. The following example shows the `SourceMetadataMessages` field for this scenario.

```
{
    "Arn": "arn:aws:mediaconnect:us-east-1:111122223333:routerInput:a1b2c3d4e5f6",
    "Name": "StadiumFeed",
    "SourceMetadataDetails": {
        "SourceMetadataMessages": [
            {
                "Code": "MediaInfoMonitoringTruncated",
                "Message": "Program limit (50) exceeded. Monitoring only the first 50 programs of 60 in the transport stream."
            }
        ],
        "Timestamp": "2023-12-06T19:57:54Z",
        "RouterInputMetadata": {
            "TransportStreamMediaInfo": {
                "Programs": [
                    {
                        "PcrPid": 1000,
                        "ProgramNumber": 1,
                        "ProgramPid": 2000,
                        "ProgramName": "StadiumFeed HD",
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
    }
}
```