# Deleting Vocabulary List

Use the [InvokeDataAutomationLibraryIngestionJob](bedrock/latest/APIReference/API_data-automation_InvokeDataAutomationLibraryIngestionJob.md "bedrock/latest/APIReference/API_data-automation_InvokeDataAutomationLibraryIngestionJob.md") with "DELETE" operation type to remove specific entities from your library.

## AWS CLI Example:

### Option 1: Using S3 Manifest file

#### Step 1: Create a JSONL manifest file

Create a simple s3 manifest file with a list of entityIds.

Example: `cv-delete-manifest.json`

```
{"entityIds": ["medical-en", "medical-es"]}
```

#### Step 2: Upload the manifest to S3

```
aws s3 cp vocabulary-manifest.json s3://my-bucket/manifests/
```

#### Step 3: Start the ingestion job

Use the [InvokeDataAutomationLibraryIngestionJob](bedrock/latest/APIReference/API_data-automation_InvokeDataAutomationLibraryIngestionJob.md "bedrock/latest/APIReference/API_data-automation_InvokeDataAutomationLibraryIngestionJob.md") to start a vocabulary ingestion job with an operation type DELETE

**Request**

```
aws bedrock-data-automation invoke-data-automation-library-ingestion-job \
    --library-arn "arn:aws:bedrock:us-east-1:123456789012:data-automation-library/healthcare-vocabulary" \
    --entity-type "VOCABULARY" \
    --operation-type "DELETE" \
    --input-configuration '{"s3Object":{"s3Uri":"s3://my-bucket/manifests/cv-delete-manifest.json"}}' \
    --output-configuration '{"s3Uri":"s3://my-bucket/outputs/"}'
```

**Response:**

```
{
  "jobArn": "arn:aws:bedrock:us-east-1:123456789012:data-automation-library-ingestion-job/job-12345"
}
```

### Option 2: Using inline payload

**Request**

```
aws bedrock-data-automation invoke-data-automation-library-ingestion-job \
    --library-arn "arn:aws:bedrock:us-east-1:123456789012:data-automation-library/healthcare-vocabulary" \
    --entity-type "VOCABULARY" \
    --operation-type "DELETE" \
    --input-configuration '{"inlinePayload":{"deleteEntitiesInfo":{"entityIds": ["medical-en"]}}}' \
    --output-configuration '{"s3Uri": "s3://my-bucket/outputs/"}'
```

## AWS Console Example:

1. Navigate to the "Library details" page for your library
2. Choose the desired entity from the "Custom vocabulary lists"
3. Choose "Delete custom vocabulary list"
