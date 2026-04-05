# Updating Library Metadata

Use the [UpdateDataAutomationLibrary](../APIReference/API_data-automation_UpdateDataAutomationLibrary.md "../APIReference/API_data-automation_UpdateDataAutomationLibrary.md") api to update library metadata

```
aws bedrock-data-automation update-data-automation-library \
    --library-arn "arn:aws:bedrock:us-east-1:123456789012:data-automation-library/healthcare-vocabulary" \
    --library-description "Updated: Medical terminology for healthcare transcription"
```

**Response:**

```
{
  "libraryArn": "arn:aws:bedrock:us-east-1:123456789012:data-automation-library/healthcare-vocabulary",
  "status": "ACTIVE"
}
```
