# Elemental Inference performance metrics

## GetMetadata request count

The number of GetMetadata API requests made to retrieve metadata.

**Details**

- Name: GetMetadataRequestCount
- Supported dimension sets:
  - Feed
  - Feed, StatusCode: to monitor API requests that result in a specific category
    HTTP response codes.

- Recommended statistic: Sum
- Units: Count
- Meaning of zero: This metric will never emit zero.
- Meaning of no datapoints: There were no GetMetadata API calls on the specified
  feed.

## Processing fault count

The total number of processing failures.

**Details**

- Name: ProcessingFaultCount
- Supported dimension sets: Feed
- Recommended statistic: Sum
- Units: Count
- Meaning of zero: All video segments submitted to the feed were processed
  successfully without any failures.
- Meaning of no datapoints: No video segments were submitted. (PutMedia hasn’t been
  called.)

## Processing latency

The end-to-end time from when a video segment is submitted using PutMedia until the
metadata is available to be retrieved using GetMetadata.

**Details**

Name: ProcessingLatency

Supported dimension sets:

- Feed
- Feed, Feature

Recommended statistics: p50, p95, p99, Average

Units: Milliseconds

Meaning of zero: There is probably an issue with the source media. For example, if the
timestamp is wrong, it’s possible that the latency will seem to be 0.

Meaning of no datapoints: No video segments were submitted (PutMedia hasn’t been
called.)

## PutMedia request count

The number of PutMedia API requests made to submit video segments for processing.

**Details**

- Name: PutMediaRequestCount
- Supported dimension sets:

      + Feed,
      + Feed, StatusCode: to monitor API requests that result in a specific category
       HTTP response codes.

  Recommended statistic: Sum

- Units: Count
- Meaning of zero: This metric will never emit zero.
- Meaning of no datapoints: There were no PutMedia API calls on the specified
  feed.
