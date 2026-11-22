

# Tutorial: Process your first document

This tutorial walks through a complete Amazon Textract Insights job: you create a project with extraction and a public W-2 blueprint, upload a document, start a job, poll for completion, and read both the extraction and custom extraction results from Amazon S3. It uses the AWS CLI, the example account 111122223333, AWS Region us-east-1, and the buckets amzn-s3-demo-bucket (input) and amzn-s3-demo-destination-bucket (output).

Before you begin, complete [Prerequisites and setup](insights-prerequisites.md).

## Step 1: Create a project
<a name="insights-tutorial-create-project"></a>

Create a project that enables extraction (required) and attaches the public W-2 blueprint for custom extraction. The `--extraction-configuration` block is required and must set `BoundingBox`, a non-empty `Granularity.Types`, and `OutputFormat`.

```
aws textract create-project \
  --region us-east-1 \
  --project-name "my-first-project" \
  --custom-configuration '{"Blueprints": [{"BlueprintArn": "arn:aws:textract:us-east-1:aws:blueprint/public-w2-form"}]}' \
  --extraction-configuration '{"BoundingBox": {"State": "ENABLED"}, "Granularity": {"Types": ["PAGE", "ELEMENT"]}, "OutputFormat": {"TextFormat": {"Types": ["MARKDOWN"]}, "AdditionalFileFormat": {"State": "DISABLED"}}}'
```

`CreateProject` is synchronous. It returns the project ARN and a status:

```json
{
  "ProjectArn": "arn:aws:textract:us-east-1:111122223333:project/abcdef123456",
  "Status": "COMPLETED"
}
```

## Step 2: Upload a document
<a name="insights-tutorial-upload-document"></a>

Upload the document you want to process to your input bucket:

```
aws s3 cp w2.pdf s3://amzn-s3-demo-bucket/w2.pdf --region us-east-1
```

## Step 3: Start the job
<a name="insights-tutorial-start-job"></a>

Start the analysis, pointing at the input document, the output prefix, and the project ARN from Step 1. The output S3 URI is a prefix; Amazon Textract Insights writes all result files beneath it.

```
aws textract start-document-insights \
  --region us-east-1 \
  --input-configuration '{"S3Uri": "s3://amzn-s3-demo-bucket/w2.pdf"}' \
  --output-configuration '{"S3Uri": "s3://amzn-s3-demo-destination-bucket/output"}' \
  --project-arn "arn:aws:textract:us-east-1:111122223333:project/abcdef123456"
```

The call returns a job ARN:

```json
{
  "JobArn": "arn:aws:textract:us-east-1:111122223333:job/abcdef123456"
}
```

## Step 4: Poll for completion
<a name="insights-tutorial-poll-completion"></a>

The job runs asynchronously. Poll its status with `GetDocumentInsights` using the job ARN:

```
aws textract get-document-insights \
  --region us-east-1 \
  --job-arn "arn:aws:textract:us-east-1:111122223333:job/abcdef123456"
```

The status is one of `IN_PROGRESS`, `SUCCEEDED`, or `FAILED`. When the status is `SUCCEEDED`, the response includes the output location, and you can read the results from Amazon S3. If the status is `FAILED`, the response includes `ErrorType` and `ErrorMessage`.

## Step 5: Read the job metadata
<a name="insights-tutorial-read-metadata"></a>

On success, Amazon Textract Insights writes a `job_metadata.json` file at `s3://<bucket>/<prefix>/<job-id>/job_metadata.json`. It lists the output paths for each document the job produced. Download it:

```
aws s3 cp s3://amzn-s3-demo-destination-bucket/output/<job-id>/job_metadata.json . --region us-east-1
```

The file points at the extraction and custom extraction result for each document:

```json
{
  "job_id": "abcdef123456",
  "output_metadata": [
    {
      "asset_id": 0,
      "segment_metadata": [
        {
          "extraction_path": "s3://amzn-s3-demo-destination-bucket/output/abcdef123456/0/extraction/0/result.json",
          "custom_path": "s3://amzn-s3-demo-destination-bucket/output/abcdef123456/0/custom/0/result.json",
          "custom_status": "MATCH"
        }
      ]
    }
  ]
}
```

For the full output layout, see [Output location and file structure](insights-output-location.md).

## Step 6: Read the extraction result
<a name="insights-tutorial-read-extraction"></a>

Download the extraction result named by `extraction_path`:

```
aws s3 cp s3://amzn-s3-demo-destination-bucket/output/abcdef123456/0/extraction/0/result.json . --region us-east-1
```

The extraction result contains document metadata, text representations, statistics, and the sections you enabled through granularity. For a detailed field reference, see [Extraction results](insights-extraction-results.md).

## Step 7: Read the custom extraction result
<a name="insights-tutorial-read-custom"></a>

Download the custom (blueprint) result named by `custom_path`:

```
aws s3 cp s3://amzn-s3-demo-destination-bucket/output/abcdef123456/0/custom/0/result.json . --region us-east-1
```

The custom extraction result reports which blueprint matched, the extracted field values in `inference_result`, and per-field confidence in `explainability_info`. The following output is trimmed and uses placeholder values:

```json
{
  "matched_blueprint": {
    "arn": "arn:aws:textract:us-east-1:aws:blueprint/public-w2-form",
    "name": "W2-Form",
    "confidence": 1
  },
  "document_class": { "type": "W2" },
  "inference_result": {
    "employee_general_info": {
      "first_name": "Jane",
      "employee_last_name": "Doe",
      "ssn": "123-45-6789",
      "employee_address": "123 Any Street, Anytown, WA 98101",
      "employee_zip_code": 98101
    },
    "employer_info": {
      "employer_name": "Example Corp",
      "ein": "12-3456789",
      "employer_address": "123 Any Street, Anytown, WA 98101",
      "employer_zip_code": 98101
    },
    "federal_wage_info": {
      "wages_tips_other_compensation": 68450,
      "social_security_wages": 68450,
      "medicare_wages_tips": 68450
    },
    "federal_tax_info": {
      "federal_income_tax": 9835,
      "social_security_tax": 4243.9,
      "medicare_tax": 992.53
    }
  },
  "explainability_info": [
    {
      "employee_general_info": {
        "first_name": {
          "success": true,
          "confidence": 0.9090,
          "geometry": [
            {
              "boundingBox": { "top": 0.2454, "left": 0.0656, "width": 0.0322, "height": 0.0083 },
              "vertices": [
                { "x": 0.0656, "y": 0.2454 }, { "x": 0.0979, "y": 0.2454 },
                { "x": 0.0979, "y": 0.2537 }, { "x": 0.0656, "y": 0.2537 }
              ],
              "token_scores": [1, 1],
              "page": 1,
              "word_references": [{ "word_index": 64, "page_index": 0 }]
            }
          ],
          "type": "string",
          "value": "Jane"
        }
      },
      "federal_wage_info": {
        "wages_tips_other_compensation": {
          "success": true,
          "confidence": 0.9235,
          "geometry": ["..."],
          "type": "number",
          "value": 68450
        }
      }
    }
  ]
}
```

A per-field confidence score appears in the `explainability_info` block that mirrors `inference_result`. Fields that are not found return an empty string. Use the confidence scores to decide which fields you can auto-accept and which you route to human review. For the full structure, see [Custom extraction with blueprints](insights-custom-extraction.md).

## Next steps
<a name="insights-tutorial-next-steps"></a>
+ Learn the job model and project configuration in [How Amazon Textract Insights works](insights-how-it-works.md) and [Working with projects](insights-working-with-projects.md).
+ Explore the extraction results in detail in [Extraction results](insights-extraction-results.md).