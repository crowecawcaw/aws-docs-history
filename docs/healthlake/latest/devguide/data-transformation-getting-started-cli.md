# Getting started with the SDK and AWS CLI

## Install and configure

For installation and configuration instructions, see [Install
the AWS CLI](getting-started-setting-up.md#setting-up-install-cli "getting-started-setting-up.md#setting-up-install-cli").

## Step 1: Create a transformation profile

### Start from AWS Starter Profile (CCDA only)

```
aws healthlake create-data-transformation-profile \
  --region us-west-2 \
  --source-format CCDA \
  --profile-name "My CCDA Profile" \
  --source '{"StarterProfile": {"StarterProfileName": "ccda-starter-kit-v1"}}'
```

### Start from sample data (CSV only)

Create profile:

```
aws healthlake create-data-transformation-profile \
  --region us-west-2 \
  --source-format CSV \
  --profile-name "Patient CSV Mapping" \
  --source '{"SampleData": {"S3Uri": "s3://my-bucket/samples/patient-data.csv"}}'
```

Run the AI agent to create initial YAML mapping.

Initiate a new conversation with the agent to get a new conversation ID. Call the API again, this time passing the ConversationId from the previous response and your actual request. For a CSV profile, this is where the agent analyzes the sample files you provided at creation and generates the YAML mapping:

```
aws healthlake update-profile-with-agent \
  --region us-west-2 \
  --profile-id "a1b2c3d4e5f6a7b8c9d0e1f2a3b4c5d6" \
  --source-format CSV \
  --conversation-id "00154593-c867-4e4c-b870-25fb5237e54f" \
  --input-message '{"Body": "Generate a profile to convert my CSVs into FHIR.", "Type": "normal"}'
```

Continue the conversation with the same ConversationId to refine the mapping across multiple turns (for example, "Map the RACE\_CD column to a FHIR extension"). If the agent asks you to confirm a change, respond with "Type": "confirmation\_response".

### Start from local Mapping

```
aws healthlake create-data-transformation-profile \
  --region us-west-2 \
  --source-format CCDA \
  --profile-name "CI/CD Profile" \
  --source '{"ProfileMapping": {"ProfileMapping": {"Resources/Patient.vm": "#set($patient = $input)..."}}}'
```

### Clone from existing Profile

```
aws healthlake create-data-transformation-profile \
  --region us-east-1 \
  --source-format CCDA \
  --profile-name test-profile-clone \
  --source '{"ExistingVersionedProfileId": {"ProfileId": "e41af4b891d6f9211b42b90435cf0cea", "Version": 0}}'
```

Response:

```
{
    "ProfileId": "a1b2c3d4e5f6a7b8c9d0e1f2a3b4c5d6",
    "Version": 0,
    "SourceFormat": "CCDA",
    "TargetFormat": "FHIR_R4",
    "ProfileName": "My CCDA Profile",
    "LastUpdatedAt": "2026-07-01T12:00:00Z"
}
```

The profile is created in draft state (version 0).

## Step 2: Customize Profile with the AI agent (optional)

Initiate a new conversation with the agent to get a new conversation ID. Call the API again, this time passing the ConversationId

```
aws healthlake update-profile-with-agent \
  --region us-west-2 \
  --profile-id "a1b2c3d4e5f6a7b8c9d0e1f2a3b4c5d6" \
  --source-format CCDA \
  --conversation-id "conv-a1b2c3d4-e5f6-7890" \
  --input-message '{"Body": "Add a mapping for Medication resources", "Type": "normal"}'
```

Response:

```
{
    "chatOutput": {
        "body": "I can help you add a Medication resource mapping. Which CCDA section should I map from?",
        "type": "options",
        "optionsList": ["Medications Section", "Discharge Medications", "Immunizations"]
    },
    "conversationId": "conv-a1b2c3d4-e5f6-7890"
}
```

Continue the conversation with the returned conversationId:

```
aws healthlake update-profile-with-agent \
  --region us-west-2 \
  --profile-id "a1b2c3d4e5f6a7b8c9d0e1f2a3b4c5d6" \
  --source-format CCDA \
  --input-message '{"body": "Medications Section", "type": "confirmation_response"}' \
  --conversation-id "conv-a1b2c3d4-e5f6-7890"
```

## Step 3: Test with sync conversion (optional)

The sync conversion endpoint is REST-only. Test a profile against a sample document before publishing:

```
curl -X POST "https://datatransformation.healthlake.us-west-2.amazonaws.com/transform-data" \
  --aws-sigv4 "aws:amz:us-west-2:healthlake" \
  --user "${AWS_ACCESS_KEY_ID}:${AWS_SECRET_ACCESS_KEY}" \
  -H "x-amz-security-token: ${AWS_SESSION_TOKEN}" \
  -H "Content-Type: application/json" \
  -d '{
    "ProfileId": "a1b2c3d4e5f6a7b8c9d0e1f2a3b4c5d6",
    "InputData": {"CcdaInput": "<?xml version=\"1.0\"?><ClinicalDocument>...</ClinicalDocument>"},
    "DriftDetectionEnabled": true
  }'
```

Response:

```
{
    "TransformedData": "{\"resourceType\":\"Bundle\",\"type\":\"collection\",\"entry\":[...]}",
    "DriftReport": "{\"coverageRate\":0.95,\"unmappedElements\":[...]}"
}
```

- TransformedData: the converted FHIR resources as a JSON-encoded FHIR Bundle string.
- DriftReport: present only when DriftDetectionEnabled is true. A JSON-encoded drift report showing coverage rate and unmapped source elements.

###### Note

ProvenanceEnabled defaults to true. Provenance resources are generated unless you explicitly set "ProvenanceEnabled": false in the request.

## Step 4: Publish the profile

```
aws healthlake publish-data-transformation-profile \
  --region us-west-2 \
  --profile-id "a1b2c3d4e5f6a7b8c9d0e1f2a3b4c5d6" \
  --source-format CCDA \
  --change-description "Initial release - Patient, Observation, Medication mappings"
```

Publishing creates an immutable version (v1). Your draft remains editable, and bulk jobs use the latest published version automatically.

## Step 5: Convert data to FHIR

Data Transformation Agent offers 3 ways of converting your source data to FHIR R4.

### 1. Sync conversion

```
curl -X POST "https://datatransformation.healthlake.us-west-2.amazonaws.com/transform-data" \
  --aws-sigv4 "aws:amz:us-west-2:healthlake" \
  --user "${AWS_ACCESS_KEY_ID}:${AWS_SECRET_ACCESS_KEY}" \
  -H "x-amz-security-token: ${AWS_SESSION_TOKEN}" \
  -H "Content-Type: application/json" \
  -d '{
    "ProfileId": "a1b2c3d4e5f6a7b8c9d0e1f2a3b4c5d6",
    "InputData": {"CcdaInput": "<?xml version=\"1.0\"?><ClinicalDocument>...</ClinicalDocument>"},
    "DriftDetectionEnabled": true
  }'
```

### 2. Run a bulk transformation job to Amazon S3

```
aws healthlake start-data-transformation-job \
  --region us-west-2 \
  --profile-id "a1b2c3d4e5f6a7b8c9d0e1f2a3b4c5d6" \
  --input-data-config '{"S3Uri": "s3://my-source-bucket/ccda-files/", "SourceFormat": "CCDA"}' \
  --output-data-config '{"S3Configuration": {"S3Uri": "s3://my-output-bucket/fhir-output/", "KmsKeyId": "arn:aws:kms:us-west-2:123456789012:key/abcd1234"}}' \
  --data-access-role-arn "arn:aws:iam::123456789012:role/DTA-DataAccessRole" \
  --client-token "unique-token-$(date +%s)" \
  --job-name "cardiology-batch-july" \
  --drift-detection-enabled
```

Monitor the job:

```
# Check status
aws healthlake describe-data-transformation-job \
  --region us-west-2 \
  --job-id "a1b2c3d4e5f6a7b8c9d0e1f2a3b4c5d6"

# List recent completed jobs
aws healthlake list-data-transformation-jobs \
  --region us-west-2 \
  --job-status COMPLETED \
  --submitted-after "2026-07-01T00:00:00Z"
```

### 3. Run a bulk transformation job and ingest into a HealthLake datastore

To convert source files and load the resulting FHIR resources directly into a HealthLake datastore in a single step, use the existing StartFHIRImportJob API with the transformation profile fields:

```
aws healthlake start-fhir-import-job \
  --region us-west-2 \
  --datastore-id "your-datastore-id" \
  --input-data-config '{"S3Uri": "s3://my-source-bucket/ccda-files/"}' \
  --job-output-data-config '{"S3Configuration": {"S3Uri": "s3://my-output-bucket/import-output/", "KmsKeyId": "arn:aws:kms:us-west-2:123456789012:key/abcd1234"}}' \
  --data-access-role-arn "arn:aws:iam::123456789012:role/DTA-DataAccessRole" \
  --profile-id "a1b2c3d4e5f6a7b8c9d0e1f2a3b4c5d6" \
  --input-format "CCDA" \
  --drift-detection-enabled \
  --job-name "cardiology-import-july" \
  --client-token "import-$(date +%s)"
```

This starts a two-phase job: first the service converts your source files using the published profile, then it ingests the resulting FHIR resources into the datastore. The data is immediately queryable through the FHIR REST API once ingestion completes.

Monitor the job:

```
aws healthlake describe-fhir-import-job \
  --region us-west-2 \
  --datastore-id "your-datastore-id" \
  --job-id "returned-job-id"
```

###### Note

The datastore must be in ACTIVE state. Provenance is enabled by default. The data access role needs the same Amazon S3 and AWS KMS permissions as standalone jobs.
