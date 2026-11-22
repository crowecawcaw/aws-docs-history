

# Detecting and redacting sensitive data

Amazon Textract Insights can detect personally identifiable information (PII) in your output and, optionally, redact it so downstream consumers never see raw sensitive values. You configure this on a project with `SensitiveDataConfiguration`, or you can leave it off entirely. If you configure `SensitiveDataConfiguration`, it applies to extraction output, summarization, figure captions, and custom output.

## Enabling sensitive data detection
<a name="insights-enabling-sensitive-data-detection"></a>

Add `--sensitive-data-configuration` to `create-project` (or `update-project`). The block has three parts. `DetectionMode` is required.


**SensitiveDataConfiguration fields**  

| **Field** | **Values** | **Purpose** | 
| --- | --- | --- | 
| `DetectionMode` | `DETECTION`, `DETECTION_AND_REDACTION`, `DISABLED` | Flag PII only, flag and mask it, or turn detection off. | 
| `PiiEntitiesConfiguration.PiiEntityTypes` | `ALL`, or a list of specific types | Which entity types to act on. | 
| `PiiEntitiesConfiguration.RedactionMaskMode` | `PII`, `ENTITY_TYPE` | How masked values appear when redaction is enabled. | 

```bash
aws textract create-project \
  --region us-east-1 \
  --project-name "pii-redaction-project" \
  --sensitive-data-configuration '{
    "DetectionMode": "DETECTION_AND_REDACTION",
    "PiiEntitiesConfiguration": {
      "PiiEntityTypes": ["US_SOCIAL_SECURITY_NUMBER", "NAME", "ADDRESS"],
      "RedactionMaskMode": "ENTITY_TYPE"
    }
  }' \
  --custom-configuration '{"Blueprints": [{"BlueprintArn": "arn:aws:textract:us-east-1:aws:blueprint/public-w2-form"}]}' \
  --extraction-configuration '{"BoundingBox": {"State": "DISABLED"}, "Granularity": {"Types": ["PAGE"]}, "OutputFormat": {"TextFormat": {"Types": ["MARKDOWN"]}, "AdditionalFileFormat": {"State": "DISABLED"}}}'
```

`DISABLED` turns sensitive data detection off. Send it in the full `SensitiveDataConfiguration` on `update-project`. Any `PiiEntitiesConfiguration` stored on the project is discarded.

## Detection modes
<a name="insights-detection-modes"></a>

**`DETECTION`** adds a `sensitive_data_detection` block to the extraction `result.json`. For `CUSTOM`, the custom extraction `result.json` gets a `blueprint_sensitive_data_detection` block instead, which mirrors the `inference_result` structure field by field. The detected spans are reported, but the text is not changed and the raw values remain in the output.

**`DETECTION_AND_REDACTION`** does everything `DETECTION` does and also writes redacted copies of the JSON results, with every detected span replaced by a mask token:
+ `extraction/<n>/redacted/result.json` for `EXTRACTION`. Its path is `redacted_extraction_path` in `job_metadata.json`.
+ `custom/<n>/redacted/result.json` for `CUSTOM`. Its path is `redacted_custom_path` in `job_metadata.json`.

**Only these two JSON files are redacted.** The additional output files (`result.md`, `result.html`, `result.txt`), table CSVs, and page images (`rectified_image_<page>.jpg`) are written from the unredacted content and contain raw values.

## Mask modes
<a name="insights-mask-modes"></a>

`RedactionMaskMode` controls how masked spans read in `redacted/result.json`:
+ **`ENTITY_TYPE`** replaces the value with its type label, such as [NAME], [ADDRESS], [EMAIL], [PHONE], or [URL]. This preserves what kind of value was removed, which is useful when the shape of the document still matters downstream.
+ **`PII`** replaces the value with a single generic marker regardless of type.

## Output structure
<a name="insights-output-structure"></a>

With detection enabled, the extraction `result.json` gains a top-level `sensitive_data_detection` object. It mirrors the output structure: a `pages[]` array keyed by text format, and (when present) an `elements[]` array. Each detected span is one entry:

```json
{
  "sensitive_data_detection": {
    "pages": [
      {
        "representation": {
          "markdown": [
            {
              "index": 76,
              "sensitive_data_type": "ADDRESS",
              "entity_type": "ADDRESS",
              "content": "123 Any Street, Anytown, WA 98101",
              "start_character_offset": 64,
              "end_character_offset": 80,
              "source_entity_id": "a457df98-e5b4-405c-8443-d37396c082f6"
            }
            // ...(more spans)
          ]
        }
      }
    ]
  }
}
```

Each span reports:


**Fields in a detected span**  

| **Field** | **Meaning** | 
| --- | --- | 
| `index` | Ordinal of this span within the output. | 
| `sensitive_data_type` | The detected category. | 
| `entity_type` | The entity type assigned to the span. | 
| `content` | The matched text. In the **unredacted** `result.json` this is the raw value; in `redacted/result.json` it is the mask token. | 
| `start_character_offset` / `end_character_offset` | Character range of the span within the referenced text representation. | 
| `source_entity_id` | The page or element the span was found in. | 

When redaction is enabled, `redacted/result.json` holds the masked text in each representation (for example [ADDRESS], [NAME], [URL]) and its own `sensitive_data_detection` block whose offsets index into the **redacted** text and whose content is the mask token:

```json
{
  "pages": [
    {
      "representation": {
        "text": "...[ADDRESS]...[NAME]...[URL]...",
        "markdown": "...# Office of Administration [ADDRESS] [ [URL] ]([URL])...",
        "html": "...<h1>... [ADDRESS] <a href=\"[URL]\"> [URL] </a></h1>..."
      }
    }
  ],
  "sensitive_data_detection": {
    "pages": [
      {
        "representation": {
          "text": [
            {
              "index": 0,
              "sensitive_data_type": "ADDRESS",
              "entity_type": "ADDRESS",
              "content": "[ADDRESS]",
              "start_character_offset": 15,
              "end_character_offset": 24,
              "source_entity_id": "a457df98-e5b4-405c-8443-d37396c082f6"
            }
            // ...(more spans)
          ]
        }
      }
    ]
  }
}
```

For where these files sit in the job output, see [Output location and file structure](insights-output-location.md).

## Protecting the raw output
<a name="insights-protecting-raw-output"></a>

**The original `result.json` always contains the raw, unredacted values**, even when redaction is enabled. Redaction produces an additional file; it does not remove sensitive data from the extraction results. To keep raw PII out of downstream systems:
+ Send only the redacted JSON files (`extraction/<n>/redacted/result.json` and `custom/<n>/redacted/result.json`) to downstream consumers, dashboards, or storage. Do not send the `.md`, `.html`, `.txt`, CSV, or page-image outputs of a job that processes sensitive documents, because they are not redacted.
+ Restrict access to the unredacted `result.json` (and to the input document) with Amazon S3 bucket policies and IAM. Grant read access only to the roles that genuinely need the raw values.
+ Consider a customer managed AWS KMS key on the output location. See [Data protection and encryption](insights-data-protection.md).

## Choosing entity types and validating results
<a name="insights-choosing-entity-types"></a>

Tune detection to your documents rather than enabling everything blindly:
+ **Choose `PiiEntityTypes` deliberately.** `ALL` acts on every supported type and can over-mask: form boilerplate and field labels that resemble names or addresses might be redacted along with the real values. Narrowing the list to the types you actually need to remove reduces false positives.
+ **Expect some misses.** Unlabeled numbers and values that lack surrounding context can be missed by detection. Do not treat redaction as a guarantee that a document is free of sensitive data.
+ **Validate on representative documents.** Before relying on redaction in a workflow, run it against a representative sample of your real documents. Inspect both `result.json` and `redacted/result.json`, and confirm the entity types you chose catch what you need without masking content you want to keep.

For the entity types you can request, see [Supported sensitive data entity types](insights-supported-entities.md).