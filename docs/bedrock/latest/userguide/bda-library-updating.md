

# Updating Library Metadata

Use the [UpdateDataAutomationLibrary](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_data-automation_UpdateDataAutomationLibrary.html) API to update the library metadata

```bash
aws bedrock-data-automation update-data-automation-library \
    --library-arn "arn:aws:bedrock:us-east-1:123456789012:data-automation-library/healthcare-vocabulary" \
    --library-description "Updated: Medical terminology for healthcare transcription"
```

**Response:**

```json
{
  "libraryArn": "arn:aws:bedrock:us-east-1:123456789012:data-automation-library/healthcare-vocabulary",
  "status": "ACTIVE"
}
```