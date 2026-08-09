# Creating Library

Use the [CreateDataAutomationLibrary](bedrock/latest/APIReference/API_data-automation_CreateDataAutomationLibrary.md "bedrock/latest/APIReference/API_data-automation_CreateDataAutomationLibrary.md") API to create a new library container.

## AWS CLI Example:

**Request**

```
aws bedrock-data-automation create-data-automation-library \
    --library-name "healthcare-vocabulary" \
    --library-description "Medical terminology for transcription accuracy" \
    --region us-east-1
```

**Response**

```
{
  "libraryArn": "arn:aws:bedrock:us-east-1:123456789012:data-automation-library/healthcare-vocabulary",
  "status": "ACTIVE"
}
```

## AWS Console Example:

1. Navigate to "Manage libraries" page in BDA Console
2. Choose "Create library"

![Create library dialog with fields for library name, description, KMS key , and tags.](images/bda/library-create-console.png)

## Important Notes

1. Library creation is synchronous and returns immediately
2. Library names must be unique within your account and region
3. The library is empty until you run an entity ingestion job
4. Libraries can be associated with multiple projects
