# Programmatic access to extracted information

Extracted information can be accessed programmatically through the following
channels:

- **Amazon S3** – Contact analysis output files
  (after-call work and post-contact processing)
- **API** – Real-time contact analysis
  segments (after-call work only)
- **Amazon Kinesis** – Real-time event
  delivery (after-call work only)

## Extracted information in Amazon S3

Extracted information is included in the contact analysis output written to Amazon S3. This
includes information extracted during after-call work and during post-contact
processing.

The following is an example of the extracted information structure in the JSON
output:

```
{
  "ExtractedInformation": {
    "Extractions": [
      {
        "Name": "Flight number",
        "DisplayLabel": "Flight #",
        "Value": "XX123",
        "PointsOfInterest": [
          {
            "BeginOffsetMillis": 15230,
            "EndOffsetMillis": 18450
          }
        ]
      },
      {
        "Name": "Next steps promised",
        "Value": "Refund to be processed within 7 days",
        "PointsOfInterest": [
          {
            "BeginOffsetMillis": 19010,
            "EndOffsetMillis": 22690
          }
        ]
      }
    ]
  }
}
```

Each extraction includes:

- **Name** — The extraction definition
  name.
- **DisplayLabel** — The display label, if
  configured.
- **Value** — The extracted information from
  the contact.
- **PointsOfInterest** — The timestamp offsets
  in the recording where the information was mentioned (voice contacts
  only).

## Extracted information through API

You can retrieve extracted information generated during after-call work
programmatically using the following APIs:

- **[ListRealtimeContactAnalysisSegments](../APIReference/API_connect-contact-lens_ListRealtimeContactAnalysisSegments.md "../APIReference/API_connect-contact-lens_ListRealtimeContactAnalysisSegments.md")** — Returns
  extracted information segments for **voice**
  contacts during after-contact work.
- **[ListRealtimeContactAnalysisSegmentsV2](../APIReference/API_ListRealtimeContactAnalysisSegmentsV2.md "../APIReference/API_ListRealtimeContactAnalysisSegmentsV2.md")** — Returns
  extracted information segments for **chat**
  contacts during after-contact work.

## Extracted information through Amazon Kinesis

If your Connect Customer instance is configured to send conversational analytics to
Amazon Kinesis Data Streams, extracted information events generated during
after-call work are delivered to your Kinesis stream as they are produced.

For more information, refer to [Use streaming for
contact analysis](contact-analysis-segment-streams.md "contact-analysis-segment-streams.md").
