

# Running jobs with inline blueprints

Instead of creating a project, you can pass blueprints directly on a job with the `Blueprints` parameter of `StartDocumentInsights`. This is useful for one-off jobs or quick tests, where defining a reusable project is unnecessary. A job provides exactly one of `ProjectArn` or `Blueprints` — not both.

## Inline jobs return custom extraction results only
<a name="insights-inline-blueprints-custom-only"></a>

A job started with inline blueprints returns **custom extraction results only**. It does not produce extraction results: there is no `extraction/` folder, only the `custom/` folder and `job_metadata.json`. If you need extraction as well, use a project with an `ExtractionConfiguration`; see [Working with projects](insights-working-with-projects.md).

## Start a job with inline blueprints
<a name="insights-inline-blueprints-start"></a>

Pass the blueprints as a JSON array to `--blueprints`. Each entry carries a `BlueprintArn` and an optional `BlueprintVersion`. The call returns a `JobArn`.

```
aws textract start-document-insights \
  --input-configuration '{ "S3Uri": "s3://amzn-s3-demo-bucket/w2.pdf" }' \
  --output-configuration '{ "S3Uri": "s3://amzn-s3-demo-destination-bucket/output/" }' \
  --blueprints '[{"BlueprintArn":"arn:aws:textract:us-east-1:aws:blueprint/public-w2-form"}]' \
  --region us-east-1
```

Then poll `GetDocumentInsights` with the returned job identifier until `Status` is `SUCCEEDED` or `FAILED`. See [Running and monitoring Document Insights jobs](insights-running-monitoring.md).

## Output layout for an inline job
<a name="insights-inline-blueprints-output"></a>

On success, the output location holds only the custom extraction result and the job metadata — no `extraction/` folder:

```
<prefix>/<job-id>/job_metadata.json
<prefix>/<job-id>/0/custom/0/result.json
```

The `job_metadata.json` for an inline job lists only `custom_path` entries in `segment_metadata` (there is no `extraction_path`), with the bucket name shown here as a placeholder:

```json
{
  "job_id": "b949fd79-3eee-4167-87bb-e35bac1d2d46",
  "job_status": "PROCESSED",
  "output_metadata": [
    {
      "asset_id": 0,
      "segment_metadata": [
        {
          "custom_path": "s3://amzn-s3-demo-destination-bucket/output/<job-id>/0/custom/0/result.json",
          "custom_status": "MATCH"
        }
      ]
    }
  ]
}
```

The custom `result.json` has the same shape as the project-based custom extraction results, including `matched_blueprint`, `document_class`, `split_document`, `inference_result`, and `explainability_info`. See [Custom extraction with blueprints](insights-custom-extraction.md) for the full field reference.

## When to use a project instead
<a name="insights-inline-blueprints-when-project"></a>

Use inline blueprints for one-off or exploratory jobs. Use a project when you want to:
+ produce extraction results alongside custom extraction results,
+ reuse the same configuration across many jobs,
+ enable splitting, generative output, sensitive-data handling, or a fallback blueprint.

See [Working with projects](insights-working-with-projects.md) for the configuration blocks a project supports. For request parameters and errors, see the Amazon Textract Insights API Reference. 