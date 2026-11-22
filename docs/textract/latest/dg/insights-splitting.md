

# Splitting multi-document files

A single input file often contains several logical documents — for example a packet that holds a bank statement followed by an invoice. When you enable splitting, Amazon Textract Insights detects these boundaries, processes each sub-document on its own, and matches each one to a blueprint independently.

## When splitting applies
<a name="insights-splitting-when"></a>

Splitting is controlled by the project's `SplitterConfiguration`, which has a single `State` field (`ENABLED` or `DISABLED`). Two conditions must hold for it to take effect:
+ The project (or job) must provide blueprints. Splitting takes effect only when blueprints are present.
+ Splitting applies to custom extraction. Each detected sub-document is matched to a blueprint and gets its own custom extraction results.

If you enable splitting on a project that has no blueprints, there is nothing for the splitter to act on.

## Enable splitting on a project
<a name="insights-splitting-enable"></a>

Set `SplitterConfiguration.State` to `ENABLED` in the project configuration, alongside the blueprints you want to match against.

```
aws textract create-project \
  --project-name "packet-processing" \
  --extraction-configuration '{
    "BoundingBox": { "State": "ENABLED" },
    "Granularity": { "Types": ["DOCUMENT", "ELEMENT"] },
    "OutputFormat": {"TextFormat": {"Types": ["MARKDOWN"]}, "AdditionalFileFormat": {"State": "DISABLED"}}
  }' \
  --splitter-configuration '{"State": "ENABLED"}' \
  --custom-configuration '{
    "Blueprints": [
      { "BlueprintArn": "arn:aws:textract:us-east-1:aws:blueprint/public-invoice" },
      { "BlueprintArn": "arn:aws:textract:us-east-1:aws:blueprint/public-bank-statement" }
    ]
  }' \
  --region us-east-1
```

See [Working with projects](insights-working-with-projects.md) for the full set of configuration blocks.

## How a packet is split
<a name="insights-splitting-how"></a>

The following example uses a four-page file that contains a bank statement followed by a three-page invoice, processed with the public invoice and bank-statement blueprints and splitting enabled. Amazon Textract Insights produced two sub-documents:


**Sub-documents produced from a four-page packet**  

| **Sub-document** | **Pages** | **Matched blueprint** | 
| --- | --- | --- | 
| `0` | `[0]` | `Bank-Statement` | 
| `1` | `[1, 2, 3]` | `Invoice` | 

Each sub-document is numbered by `<n>` and gets its own extraction results under `extraction/<n>/` and its own custom extraction results under `custom/<n>/`.

## Reading the job metadata
<a name="insights-splitting-metadata"></a>

On a successful job, `job_metadata.json` lists the output for each sub-document. The following is the metadata for the split packet described earlier, with the bucket name replaced by a placeholder.

```json
{
  "job_id": "0df791a4-ef8e-4c8e-a99f-6d0022bd30d1",
  "job_status": "PROCESSED",
  "output_metadata": [
    {
      "asset_id": 0,
      "segment_metadata": [
        {
          "extraction_path": "s3://amzn-s3-demo-destination-bucket/output/<job-id>/0/extraction/0/result.json",
          "custom_path": "s3://amzn-s3-demo-destination-bucket/output/<job-id>/0/custom/0/result.json",
          "custom_status": "MATCH"
        },
        {
          "extraction_path": "s3://amzn-s3-demo-destination-bucket/output/<job-id>/0/extraction/1/result.json",
          "custom_path": "s3://amzn-s3-demo-destination-bucket/output/<job-id>/0/custom/1/result.json",
          "custom_status": "MATCH"
        }
      ]
    }
  ]
}
```

`output_metadata[].segment_metadata[]` has one entry per sub-document. Each entry points to that sub-document's extraction results (`extraction_path`) and custom extraction results (`custom_path`), and reports `custom_status` (`MATCH` when a blueprint matched). The leading `0` in each path is the `asset_id` of the input file.

The `job_status` field in `job_metadata.json` reads `PROCESSED` and is not the authoritative job state. Rely on the `Status` returned by `GetDocumentInsights` (`IN_PROGRESS`, `SUCCEEDED`, or `FAILED`), not on this field.

## Which pages belong to each sub-document
<a name="insights-splitting-pages"></a>

Each sub-document's custom `result.json` records the input pages it covers in `split_document.page_indices`. For the preceding invoice sub-document:

```json
{
  "matched_blueprint": {
    "arn": "arn:aws:textract:us-east-1:aws:blueprint/public-invoice",
    "name": "Invoice",
    "confidence": 1
  },
  "document_class": { "type": "Invoice" },
  "split_document": { "page_indices": [1, 2, 3] }
}
```

Page indices are zero-based and refer to pages of the original input file. For how a sub-document is matched to a blueprint and what happens when none matches, see [Blueprint matching and fallback blueprints](insights-blueprint-matching.md). For the full output layout on disk, see [Output location and file structure](insights-output-location.md).