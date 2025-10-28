# Configuring a job with TAMS inputs

To process content from a TAMS server, you configure your job input settings with the TAMS server URL and specify the content you want to process.

To configure a TAMS input by using the MediaConvert console:

1. In the **Inputs** section, choose **Add**.
2. For **Input file URL**, enter the base URL of your TAMS server API endpoint using HTTPS protocol. For example, `https://tams-server.example.com/api`. Do not include source IDs, flow IDs, or query parameters in this URL.
3. Expand **TAMS settings**.
4. For **Source ID**, enter the UUID of the TAMS source you want to process.
5. For **Time range**, enter the time range in the format `[start:nanoseconds_end:nanoseconds]`. For example, `[15:0_35:0]` processes content from 15 seconds to 35 seconds.
6. For **Gap handling**, choose how to handle missing segments:
   - **Skip gaps** – Skip missing segments and create discontinuity markers in the output.
   - **Fill with black** – Fill missing segments with black frames to maintain consistent duration.
   - **Hold last frame** – Repeat the last frame before each gap while maintaining audio silence.

7. For **Authentication connection ARN**, enter the ARN of the EventBridge connection that contains your TAMS server authentication credentials.
8. Within **Video selector**, expand **Video
   correction** set **Timecode source** to **Start at
   0**.
   To configure a TAMS input by using the API, SDK, or AWS Command Line Interface (AWS CLI), include the
   following in your job input settings. The FileInput should contain only the base TAMS server URL using HTTPS protocol. MediaConvert automatically appends the necessary API paths. Replace the example values with your TAMS server URL, source ID, and EventBridge connection ARN:

```
...
    "Inputs": [{
        "FileInput": "https://tams-server.example.com/api",
        "TamsSettings": {
            "SourceId": "be1d6b1c-1e90-4107-a269-336446adeb1c",
            "Timerange": "[15:0_35:0)",
            "GapHandling": "SKIP_GAPS",
            "AuthConnectionArn": "arn:aws:events:us-west-2:111122223333:connection/tams-auth/a85c6758-9e36-46b6-9d34-6005f212609a"
        },
        "TimecodeSource": "ZEROBASED"
    }]
...
```
