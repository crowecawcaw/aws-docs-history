

# Blueprint matching and fallback blueprints

When a project or job provides more than one blueprint, Amazon Textract Insights matches each document (or each sub-document, when splitting is enabled) to the blueprint that best fits it, and extracts fields using that blueprint. A fallback blueprint lets you handle documents that do not match any of your primary blueprints.

## How matching works
<a name="insights-blueprint-matching-how"></a>

For each document, Amazon Textract Insights selects the matching blueprint and records it in the custom `result.json`:

```json
{
  "matched_blueprint": {
    "arn": "arn:aws:textract:us-east-1:aws:blueprint/public-bank-statement",
    "name": "Bank-Statement",
    "confidence": 1
  },
  "document_class": { "type": "Bank-Statement" }
}
```
+ `matched_blueprint.arn` and `matched_blueprint.name` identify the blueprint that was used.
+ `matched_blueprint.confidence` is the match confidence, from 0 to 1.
+ `document_class.type` is the matched blueprint's class.

When splitting is enabled, matching runs per sub-document, so one input file can produce several documents each matched to a different blueprint. In the observed bank-statement-plus-invoice packet, sub-document 0 matched `Bank-Statement` and sub-document 1 matched `Invoice`, each with a match confidence of 1. See [Splitting multi-document files](insights-splitting.md).

Matching considers each blueprint's name, description, and fields, so blueprints with specific, descriptive names and descriptions match more reliably.

## When no blueprint matches
<a name="insights-blueprint-matching-no-match"></a>

`job_metadata.json` reports the outcome for each document in `custom_status`:


**custom\_status values**  

| **custom\_status** | **Meaning** | 
| --- | --- | 
| `MATCH` | A blueprint matched. The document has a `custom_path` pointing to its custom extraction `result.json`. | 
| `NO_MATCH` | No blueprint matched. The document has extraction results (`extraction_path`) but no custom extraction results, and there is no `custom/<n>/` folder for it. | 
| `FALLBACK` | No primary blueprint matched, and the project's fallback blueprint was used. The document has a `custom_path` pointing to its custom extraction `result.json`. See [How fallback results are reported](#insights-blueprint-matching-reported). | 

A `NO_MATCH` document does not fail the job: the job still reaches `SUCCEEDED`. Check `custom_status` for every entry in `segment_metadata` rather than assuming each document has a `custom_path`.

```json
{
  "segment_metadata": [
    {
      "extraction_path": "s3://amzn-s3-demo-destination-bucket/results/<job-id>/0/extraction/0/result.json",
      "custom_status": "NO_MATCH"
    }
  ]
}
```

## Fallback blueprints
<a name="insights-blueprint-matching-fallback"></a>

A fallback blueprint is used when a document does not match any of the project's primary blueprints. Configure it in `CustomConfiguration.FallbackBlueprints`. You can specify at most one fallback blueprint per project. See [Limits and quotas](insights-quotas.md). On `UpdateProject`, a `CustomConfiguration` that omits `FallbackBlueprints` clears the stored fallback blueprint.

```
aws textract create-project \
  --project-name "mixed-documents" \
  --extraction-configuration '{
    "BoundingBox": { "State": "ENABLED" },
    "Granularity": { "Types": ["DOCUMENT", "ELEMENT"] },
    "OutputFormat": {"TextFormat": {"Types": ["MARKDOWN"]}, "AdditionalFileFormat": {"State": "DISABLED"}}
  }' \
  --custom-configuration '{
    "Blueprints": [
      { "BlueprintArn": "arn:aws:textract:us-east-1:aws:blueprint/public-invoice" },
      { "BlueprintArn": "arn:aws:textract:us-east-1:aws:blueprint/public-bank-statement" }
    ],
    "FallbackBlueprints": [
      { "BlueprintArn": "arn:aws:textract:us-east-1:111122223333:blueprint/catch-all-blueprint" }
    ]
  }' \
  --region us-east-1
```

Like primary blueprints, a fallback blueprint entry carries a `BlueprintArn` and an optional `BlueprintVersion`. Use a fallback blueprint when your input mix might include documents outside your known types and you still want a consistent set of fields extracted from them.

### Matching behavior by configuration
<a name="insights-blueprint-matching-behavior"></a>

Whether matching runs, and what match confidence you get, depends on how many primary blueprints the project has and whether it has a fallback blueprint:


**Matching behavior by configuration**  

| **Configuration** | **Matching behavior** | **Match confidence** | 
| --- | --- | --- | 
| One blueprint, no fallback | Matching is skipped. Every document is extracted with the single blueprint. | Always 1 | 
| One blueprint, with fallback | Matching runs against the single blueprint. A document that doesn't match is extracted with the fallback blueprint. | The match score, or 0 when the fallback is used | 
| Multiple blueprints, no fallback | Matching runs against all blueprints and picks the best match. A document that matches none gets `NO_MATCH`. | The match score, or no custom results for `NO_MATCH` | 
| Multiple blueprints, with fallback | Matching runs against all blueprints and picks the best match. A document that matches none is extracted with the fallback blueprint. | The match score, or 0 when the fallback is used | 

With a single blueprint, adding a fallback blueprint turns matching on, so `matched_blueprint.confidence` reflects how well each document actually fits the blueprint instead of always being 1.

### How fallback results are reported
<a name="insights-blueprint-matching-reported"></a>

A document that matches none of the primary blueprints is processed with the fallback blueprint. Its results differ from a matched document in two ways:
+ In `job_metadata.json`, the segment's `custom_status` is `FALLBACK`, not `MATCH`, and `custom_path` points at the custom extraction results as usual.
+ In the custom extraction `result.json`, `matched_blueprint` names the fallback blueprint and its confidence is 0.

```json
"segment_metadata": [
  {
    "extraction_path": "s3://amzn-s3-demo-destination-bucket/results/abcd1234efgh/0/extraction/0/result.json",
    "custom_path": "s3://amzn-s3-demo-destination-bucket/results/abcd1234efgh/0/custom/0/result.json",
    "custom_status": "FALLBACK"
  }
]
```

If your code checks `custom_status` for `MATCH` before reading `custom_path`, also accept `FALLBACK`, or the fallback results are skipped.

## Best practices for blueprint matching
<a name="insights-blueprint-matching-best-practices"></a>

To improve matching accuracy, follow these best practices:
+ Give each blueprint an explicit, descriptive name and description. Matching uses them.
+ Create separate blueprints for document formats that differ significantly.
+ Don't attach two blueprints for the same document type (for example, two W-2 blueprints) to one project. Overlapping blueprints compete during matching and reduce accuracy.

## Choosing primary blueprints
<a name="insights-blueprint-matching-choosing"></a>

Give the project the blueprints for the document types you expect. Public blueprints cover many common types (see [Custom extraction with blueprints](insights-custom-extraction.md) for the full list), and custom blueprints cover the rest (see [Creating blueprints](insights-creating-blueprints.md)). Reserve the single fallback slot for documents that fall outside those types.

For the complete `result.json` field reference, including `explainability_info` and per-field confidence, see [Custom extraction with blueprints](insights-custom-extraction.md). For request parameters and errors, see the Amazon Textract Insights API Reference. 