

# Output location and file structure

When a job reaches `SUCCEEDED`, Amazon Textract Insights has written all of its output beneath the S3 prefix you supplied in `OutputConfiguration.S3Uri`. The entry point is a single `job_metadata.json` file that points to every result the job produced. This page describes the layout and how to locate results.

## Finding the output
<a name="insights-output-location-finding"></a>

The `OutputConfiguration.S3Uri` you pass to `StartDocumentInsights` is a prefix. The job writes its output under a job-ID subpath, and `GetDocumentInsights` returns the path to the job's metadata file on success:

```
s3://<bucket>/<prefix>/<job-id>/job_metadata.json
```

For example, with output prefix `s3://amzn-s3-demo-destination-bucket/results`, a successful response reports:

```
s3://amzn-s3-demo-destination-bucket/results/abcd1234efgh/job_metadata.json
```

Always start from `job_metadata.json`. It lists the exact S3 path of every `result.json` the job produced, so you do not have to guess paths.

## S3 layout
<a name="insights-output-location-layout"></a>

A job writes the following structure beneath `<prefix>/<job-id>/`:

```
<prefix>/<job-id>/job_metadata.json
<prefix>/<job-id>/0/extraction/<n>/result.json                 # extraction results, one per (split) document n
<prefix>/<job-id>/0/extraction/<n>/result.md|.html|.txt        # when OutputFormat.AdditionalFileFormat is ENABLED
<prefix>/<job-id>/0/extraction/<n>/assets/<uuid>.csv           # one CSV per table, when CSV text format is requested
<prefix>/<job-id>/0/extraction/<n>/assets/rectified_image_<page>.jpg
<prefix>/<job-id>/0/extraction/<n>/redacted/result.json        # when DetectionMode is DETECTION_AND_REDACTION
<prefix>/<job-id>/0/custom/<n>/result.json                     # custom (blueprint) output, one per document n
<prefix>/<job-id>/0/custom/<n>/redacted/result.json            # when DetectionMode is DETECTION_AND_REDACTION
```

Notes on the path components:
+ **`0`** is the `asset_id` — the input file. (A single `StartDocumentInsights` call processes one input document.)
+ **`<n>`** is the (split) document index. Without splitting there is a single document `0`. With splitting enabled, each logical document in the packet gets its own `extraction/<n>` and `custom/<n>` subpath. See [Splitting multi-document files](insights-splitting.md).
+ **`extraction/`** holds extraction results; **`custom/`** holds custom extraction results. An extraction-only job has no `custom/` folder, and an inline-blueprint job has only `custom/` (no `extraction/`).
+ **`redacted/result.json`** appears only when redaction is enabled on the project: under `extraction/<n>/` for `EXTRACTION`, and under `custom/<n>/` for `CUSTOM`. No other output file has a redacted copy.

## job\_metadata.json
<a name="insights-output-location-metadata"></a>

`job_metadata.json` is the index into the job's output. It records the input and, for each document segment, the S3 paths of the extraction and custom extraction results:

```json
{
  "job_id": "abcd1234efgh",
  "job_status": "PROCESSED",
  "output_metadata": [
    {
      "asset_id": 0,
      "asset_input_path": {
        "s3_bucket": "amzn-s3-demo-bucket",
        "s3_key": "documents/invoice-bank-statement-packet.pdf"
      },
      "segment_metadata": [
        {
          "extraction_path": "s3://amzn-s3-demo-destination-bucket/results/abcd1234efgh/0/extraction/0/result.json",
          "custom_path": "s3://amzn-s3-demo-destination-bucket/results/abcd1234efgh/0/custom/0/result.json",
          "custom_status": "MATCH"
        },
        {
          "extraction_path": "s3://amzn-s3-demo-destination-bucket/results/abcd1234efgh/0/extraction/1/result.json",
          "custom_path": "s3://amzn-s3-demo-destination-bucket/results/abcd1234efgh/0/custom/1/result.json",
          "custom_status": "MATCH"
        }
      ]
    }
  ]
}
```

### Fields
<a name="insights-output-location-fields"></a>

The `job_metadata.json` file contains the following fields:


| **Field** | **Meaning** | 
| --- | --- | 
| **`job_id`** | The job identifier. | 
| **`job_status`** | An internal processing marker. Rely on the API `Status` from `GetDocumentInsights` to decide whether a job succeeded, not this field. | 
| **`output_metadata[]`** | One entry per input asset. | 
| **`output_metadata[].asset_id`** | The input file index (`0`). | 
| **`output_metadata[].asset_input_path`** | The input document's `s3_bucket` and `s3_key`. | 
| **`segment_metadata[]`** | One entry per (split) document segment. | 
| **`segment_metadata[].extraction_path`** | S3 path of the extraction `result.json` for this segment. Present when extraction ran for this segment. | 
| **`segment_metadata[].custom_path`** | S3 path of the custom (blueprint) `result.json` for this segment. | 
| **`segment_metadata[].custom_status`** | The classification outcome for this segment: `MATCH` when a primary blueprint was applied, `FALLBACK` when no primary blueprint matched and the fallback blueprint was applied, or `NO_MATCH` when no blueprint was applied. A `NO_MATCH` segment has no `custom_path`. See [Blueprint matching and fallback blueprints](insights-blueprint-matching.md). | 
| **`segment_metadata[].redacted_extraction_path`** | S3 path of the redacted extraction results, present when redaction is enabled for `EXTRACTION`. | 
| **`segment_metadata[].redacted_custom_path`** | S3 path of the redacted custom extraction results, present when redaction is enabled for `CUSTOM`. | 

**Rely on the API status, not `job_status`.** The `job_status` field inside `job_metadata.json` is an internal marker. Use the `Status` returned by `GetDocumentInsights` (`IN_PROGRESS`, `SUCCEEDED`, `FAILED`) as the source of truth for job completion.

## Locating a specific result
<a name="insights-output-location-locating"></a>

To read results after a successful job:

1. Read `OutputConfiguration.S3Uri` from `GetDocumentInsights` to get the `job_metadata.json` path.

1. Download `job_metadata.json`.

1. For each entry in `output_metadata[].segment_metadata[]`, read `extraction_path` for the extraction results and `custom_path` for the custom extraction results. If redaction is enabled, read `redacted_extraction_path` instead of `extraction_path`, and `redacted_custom_path` instead of `custom_path`, for downstream use.

For the contents of the extraction result, see [Extraction results](insights-extraction-results.md); for custom extraction results, see [Custom extraction result.json field reference](insights-custom-extraction.md#insights-custom-extraction-result); for the redacted file, see [Detecting and redacting sensitive data](insights-detecting-redacting.md).