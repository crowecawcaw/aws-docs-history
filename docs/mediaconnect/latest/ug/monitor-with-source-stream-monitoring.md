# Monitoring using source metadata

MediaConnect source metadata monitoring displays information about the transport stream and
its program media. You can view status messages about the flow's source as well as
details about the program's video, audio, and other data. Source metadata monitoring can
be used with the MediaConnect console, API, AWS CLI, or SDK. For more information about the API,
see: [`DescribeFlowSourceMetadata`](../api/v1-flows-flowarn-source-metadata.md "../api/v1-flows-flowarn-source-metadata.md") in the _MediaConnect API
Reference._

###### Note

If you are using more than one source for your flow, source metadata is only
displayed for the source currently used by the flow.

## Source metadata

details

The following sections provide details about the type of information displayed by
source metadata monitoring.

### Alerts

and messages

The **active alerts** section of the **Source
metadata** console tab and the **messages**
section of the `DescribeFlowSourceMetadata` API/CLI response can
contain status messages with more information about the transport stream. If
MediaConnect detects an issue or cannot retrieve the source stream metadata, an
associated status message will be displayed.

### Programs

The **programs** section contains information about the
individual programs contained in the transport stream. This section contains the
following fields:

| Field          | Details                                                                                                                     |
| -------------- | --------------------------------------------------------------------------------------------------------------------------- |
| Program number | The program number of the program.                                                                                          |
| Program PID    | The program Packet Identifier (PID).                                                                                        |
| PCR PID        | The Program Clock Reference (PCR) PID of the program.                                                                       |
| Program name   | The name of the program. The program name is sourced from the<br>service name value in the Service Description Table (SDT). |
| Streams        | The nested sections contain info about the video, audio, and<br>data stream types.                                          |

### Streams

The **streams** section is nested within each individual
transport stream program. This section contains the following fields:

| Field            | Details                                                                                                                                                                                                                                                                                                                                     |
| ---------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Stream type      | The type of content that the stream contains. This value can<br>be video, audio, data, or unknown.                                                                                                                                                                                                                                          |
| Codec            | The codec of the stream. This value will vary depending on<br>the type of stream. Example: a video stream type might display a<br>value of `H264` while an audio stream type displays<br>`AAC`.                                                                                                                                             |
| PID              | The Packet Identifier (PID) of the stream.                                                                                                                                                                                                                                                                                                  |
| Frame rate       | The frame rate of the video stream, displayed in<br>frames-per-second (fps).                                                                                                                                                                                                                                                                |
| Frame resolution | The resolution of the video stream. In the console, this<br>field will display the frame width followed by the frame height.<br>Example: A frame width of 1920 and a frame height of<br>1080 is displayed in the console as `1920 x<br>1080`.In the API/CLI response, the frame<br>height and frame width are displayed as separate values. |
| Channels         | The number of channels in the audio stream.                                                                                                                                                                                                                                                                                                 |
| Sample rate      | The sample rate of the audio stream. In the API/CLI response,<br>the sample rate is displayed in hertz (Hz). In the console, the<br>sample rate is displayed in Hz, unless it exceeds 1000 Hz, then<br>it is displayed in kilohertz (kHz).                                                                                                  |
| Sample size      | The sample size of the audio stream. The sample size is<br>displayed in bits.                                                                                                                                                                                                                                                               |

## Using source

metadata monitoring (console)

You can retrieve the latest source metadata from MediaConnect by using the
console.

1. Open the MediaConnect console at [https://console.aws.amazon.com/mediaconnect/](https://console.aws.amazon.com/mediaconnect/ "https://console.aws.amazon.com/mediaconnect/").
2. From the **Flows** screen, select the flow you want to
   inspect.
3. Select the **Source metadata** tab.
4. The **source metadata** tab contains an expandable list
   of every active alert, program, and stream for the selected flow's
   source.

## Using source metadata

monitoring (AWS CLI)

You can retrieve the latest source metadata from MediaConnect by using the AWS CLI. The
following example shows the AWS CLI command and return value for a typical
scenario.

1. In the AWS CLI, use the `describe-flow-source-metadata` command
   with the `--flow-arn` option of the flow you want to inspect.

```
aws mediaconnect describe-flow-source-metadata --flow-arn `arn:aws:mediaconnect:us-east-1:111122223333:flow:1-23aBC45dEF67hiJ8-12AbC34DE5fG:AwardsShow`
```

2. The return value will contain the media information for the selected
   flow's source. The following is a generic example of the format of the
   return value. In this example, there are no messages to display.

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

### Example

source metadata API/CLI response

The following is another example of the response from the
`DescribeFlowSourceMetadata` API/CLI. In this example, there are
two programs. Each program has one video stream and two audio streams. The first
program has a SCTE-35 data stream. The second program has an invalid stream type
on PID 139. The invalid stream type is indicated by the status code in the
messages section and the `Unknown` stream type in the program
section.

```
{
    "FlowArn": "arn:aws:mediaconnect:us-east-1:111122223333:flow:1-23aBC45dEF67hiJ8-12AbC34DE5fG:BasketballGame",
    "TransportMediaInfo": {
        "Messages": [
            {
                "StatusCode": "InvalidType",
                "Message": "We could not determine the type of pid 139 on program 2"
            }
        ],
        "Programs": [
          {
                "ProgramNumber": 1,
                "ProgramPid": 16,
                "PcrPid": 56,
                "ProgramName": "Basketball HD",
                "Streams": [
                    {
                        "Codec": "H264",
                        "FrameRate": "59.94",
                        "FrameResolution": {
                            "FrameHeight": 1080,
                            "FrameWidth": 1920
                        },
                        "Pid": 126,
                        "StreamType": "Video"
                    },
                    {
                        "Channels": 1,
                        "Codec": "AAC",
                        "Pid": 127,
                        "SampleRate": 50,
                        "SampleSize": 16,
                        "StreamType": "Audio"
                    },
                    {
                        "Channels": 1,
                        "Codec": "AAC",
                        "Pid": 128,
                        "SampleRate": 50,
                        "SampleSize": 16,
                        "StreamType": "Audio"
                    },
                    {
                        "StreamType": "Data",
                        "Codec": "SCTE35",
                        "Pid": 129
                    }
                ]
          },
          {
                "ProgramNumber": 2,
                "ProgramPid": 26,
                "PcrPid": 66,
                "ProgramName": "Basketball SD",
                "Streams": [
                    {
                        "Codec": "H264",
                        "FrameRate": "29.97",
                        "FrameResolution": {
                            "FrameHeight": 480,
                            "FrameWidth": 640
                        },
                        "Pid": 136,
                        "StreamType": "Video"
                    },
                    {
                        "Channels": 1,
                        "Codec": "AAC",
                        "Pid": 137,
                        "SampleRate": 50,
                        "SampleSize": 16,
                        "StreamType": "Audio"
                    },
                    {
                        "Channels": 1,
                        "Codec": "AAC",
                        "Pid": 138,
                        "SampleRate": 50,
                        "SampleSize": 16,
                        "StreamType": "Audio"
                    },
                    {
                        "StreamType": "Unknown",
                        "Codec": "Unknown",
                        "Pid": 139
                    }
                ]
          }
       ]
    },
}
```
