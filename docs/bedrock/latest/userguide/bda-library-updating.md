

# Updating Library Metadata
<a name="bda-library-updating"></a>

Use the [UpdateDataAutomationLibrary](bedrock/latest/APIReference/API_data-automation_UpdateDataAutomationLibrary.html) API to update the library metadata

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