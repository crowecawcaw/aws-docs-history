

# CLI examples by use case

This page collects end-to-end `aws textract` recipes for common Amazon Textract Insights workflows. Each recipe creates (or reuses) a configuration, starts a job, and shows what you poll for. All examples use account `111122223333`, AWS Region `us-east-1`, input bucket `amzn-s3-demo-bucket`, and output bucket `amzn-s3-demo-destination-bucket`. Replace ARNs with your own.

For the start-and-poll loop used after every start command, see [Running and monitoring Document Insights jobs](insights-running-monitoring.md).

## Extraction only
<a name="insights-cli-extraction-only"></a>

Extract text, layout, and reading order with no blueprint. With this configuration, you get bounding boxes, several granularities, and LLM-ready output formats.

```
aws textract create-project \
  --region us-east-1 \
  --project-name "extraction-project" \
  --extraction-configuration '{
    "BoundingBox": { "State": "ENABLED" },
    "Granularity": { "Types": ["DOCUMENT", "PAGE", "ELEMENT", "LINE", "WORD"] },
    "OutputFormat": {
      "AdditionalFileFormat": { "State": "ENABLED" },
      "TextFormat": { "Types": ["PLAIN_TEXT", "MARKDOWN", "HTML", "CSV"] }
    }
  }'
```

Start a job against the returned project ARN:

```
aws textract start-document-insights \
  --region us-east-1 \
  --input-configuration  S3Uri=s3://amzn-s3-demo-bucket/documents/invoice.pdf \
  --output-configuration S3Uri=s3://amzn-s3-demo-destination-bucket/results \
  --project-arn "arn:aws:textract:us-east-1:111122223333:project/abcd1234efgh"
```

## Custom extraction with a single blueprint
<a name="insights-cli-custom-single-blueprint"></a>

For a known document type, attach one blueprint and keep extraction minimal.

```
aws textract create-project \
  --region us-east-1 \
  --project-name "w2-custom-project" \
  --custom-configuration '{"Blueprints": [{"BlueprintArn": "arn:aws:textract:us-east-1:aws:blueprint/public-w2-form"}]}' \
  --extraction-configuration '{"BoundingBox": {"State": "DISABLED"}, "Granularity": {"Types": ["PAGE"]}, "OutputFormat": {"TextFormat": {"Types": ["MARKDOWN"]}, "AdditionalFileFormat": {"State": "DISABLED"}}}'
```

```
aws textract start-document-insights \
  --region us-east-1 \
  --input-configuration  S3Uri=s3://amzn-s3-demo-bucket/documents/w2.pdf \
  --output-configuration S3Uri=s3://amzn-s3-demo-destination-bucket/results \
  --project-arn "arn:aws:textract:us-east-1:111122223333:project/abcd1234efgh"
```

The job writes custom extraction results to `.../0/custom/0/result.json`. For more information about custom extraction results, see [Custom extraction result.json field reference](insights-custom-extraction.md#insights-custom-extraction-result).

## Packet split and classify
<a name="insights-cli-packet-split-classify"></a>

For a scanned packet holding several document types, enable splitting and attach multiple blueprints so the service classifies each split document and applies the matching one. Add an optional fallback blueprint for documents that match none of the candidates.

```
aws textract create-project \
  --region us-east-1 \
  --project-name "packet-split-classify-project" \
  --splitter-configuration '{"State": "ENABLED"}' \
  --custom-configuration '{
    "Blueprints": [
      {"BlueprintArn": "arn:aws:textract:us-east-1:aws:blueprint/public-invoice"},
      {"BlueprintArn": "arn:aws:textract:us-east-1:aws:blueprint/public-bank-statement"}
    ],
    "FallbackBlueprints": [
      {"BlueprintArn": "<YOUR_GENERIC_BLUEPRINT_ARN>"}
    ]
  }' \
  --extraction-configuration '{"BoundingBox": {"State": "DISABLED"}, "Granularity": {"Types": ["PAGE"]}, "OutputFormat": {"TextFormat": {"Types": ["MARKDOWN"]}, "AdditionalFileFormat": {"State": "DISABLED"}}}'
```

```
aws textract start-document-insights \
  --region us-east-1 \
  --input-configuration  S3Uri=s3://amzn-s3-demo-bucket/documents/invoice-bank-statement-packet.pdf \
  --output-configuration S3Uri=s3://amzn-s3-demo-destination-bucket/results \
  --project-arn "arn:aws:textract:us-east-1:111122223333:project/abcd1234efgh"
```

Each split document gets its own `extraction/<n>` and `custom/<n>` output. For more information about splitting and output locations, see [Splitting multi-document files](insights-splitting.md) and [Output location and file structure](insights-output-location.md).

## PII redaction
<a name="insights-cli-pii-redaction"></a>

Detect and mask sensitive data across extraction and custom extraction results. This example masks SSN, name, and address, using the entity type as the mask label.

```
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

```
aws textract start-document-insights \
  --region us-east-1 \
  --input-configuration  S3Uri=s3://amzn-s3-demo-bucket/documents/application.pdf \
  --output-configuration S3Uri=s3://amzn-s3-demo-destination-bucket/results \
  --project-arn "arn:aws:textract:us-east-1:111122223333:project/abcd1234efgh"
```

Send `redacted/result.json` downstream and restrict access to the unredacted `result.json`. For more information about detecting and redacting PII, see [Detecting and redacting sensitive data](insights-detecting-redacting.md).

## Inline blueprints (no project)
<a name="insights-cli-inline-blueprints"></a>

To run a one-off custom extraction without creating a project, pass `--blueprints` instead of `--project-arn`. This returns only custom extraction results. It performs no extraction, so there is no `extraction/` folder.

```
aws textract start-document-insights \
  --region us-east-1 \
  --input-configuration  S3Uri=s3://amzn-s3-demo-bucket/documents/w2.pdf \
  --output-configuration S3Uri=s3://amzn-s3-demo-destination-bucket/results \
  --blueprints '[{"BlueprintArn":"arn:aws:textract:us-east-1:aws:blueprint/public-w2-form"}]'
```

The output has only `.../0/custom/0/result.json` and `job_metadata.json`. For more information about output locations, see [Output location and file structure](insights-output-location.md).

## Customer managed KMS key
<a name="insights-cli-kms-key"></a>

Encrypt output with your own KMS key by adding `--encryption-configuration`. This can be set on the project and on the job; the example sets it on the job.

```
aws textract start-document-insights \
  --region us-east-1 \
  --input-configuration  S3Uri=s3://amzn-s3-demo-bucket/documents/invoice.pdf \
  --output-configuration S3Uri=s3://amzn-s3-demo-destination-bucket/results \
  --project-arn "arn:aws:textract:us-east-1:111122223333:project/abcd1234efgh" \
  --encryption-configuration '{"KmsKeyId":"arn:aws:kms:us-east-1:111122223333:key/abcd1234-..."}'
```

The calling role needs `kms:DescribeKey`, `kms:GenerateDataKey`, and `kms:Decrypt` on the key, and the key policy must allow them. For more information about data protection, see [Data protection and encryption](insights-data-protection.md).