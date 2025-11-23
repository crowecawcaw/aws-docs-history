# FHIR R4 `$davinci-data-export` operation for HealthLake

The `$davinci-data-export` operation is an asynchronous FHIR operation that enables the export of Member Attribution List data from AWS HealthLake. This operation is a specialized version of the standard FHIR `$export` operation, designed specifically to meet the requirements of the DaVinci Member Attribution (ATR) List Implementation Guide.

## Key Features

- _Asynchronous Processing_: Follows the standard FHIR asynchronous request pattern
- _Group-Level Export_: Exports data for members within a specific attribution list (Group)
- _Specialized Resource Handling_: Focuses on attribution-related resources
- _Flexible Filtering_: Supports filtering by patients, resource types, and time ranges
- _NDJSON Output_: Provides data in newline-delimited JSON format

## Operation Endpoint

```
GET  [base]/Group/[id]/$davinci-data-export
POST [base]/Group/[id]/$davinci-data-export
```

## Request Parameters

| Parameter  | Cardinality | Description                                                                                         |
| ---------- | ----------- | --------------------------------------------------------------------------------------------------- |
| patient    | 0..\*       | Specific members whose data should be exported. When omitted, all members in the Group are exported |
| \_type     | 0..1        | Comma-delimited list of FHIR resource types to export                                               |
| \_since    | 0..1        | Only include resources updated after this date/time                                                 |
| exportType | 0..1        | Type of export to perform (default: hl7.fhir.us.davinci-atr)                                        |

### Supported Resource Types

When using the `_type` parameter, only the following resource types are supported:

- Group
- Patient
- Coverage
- RelatedPerson
- Practitioner
- PractitionerRole
- Organization
- Location

## Sample Request

### Starting an Export Job

```
GET https://healthlake.region.amazonaws.com/datastore/datastoreId/r4/Group/example-group/$davinci-data-export?_type=Group,Patient,Coverage&exportType=hl7.fhir.us.davinci-atr

or

POST https://healthlake.region.amazonaws.com/datastore/datastoreId/r4/Group/example-group/$davinci-data-export?_type=Group,Patient,Coverage&exportType=hl7.fhir.us.davinci-atr
Content-Type: application/json

{
  "DataAccessRoleArn": "arn:aws:iam::444455556666:role/your-healthlake-service-role",
  "JobName": "attribution-export-job",
  "OutputDataConfig": {
    "S3Configuration": {
      "S3Uri": "s3://your-export-bucket/EXPORT-JOB",
      "KmsKeyId": "arn:aws:kms:region:444455556666:key/1234abcd-12ab-34cd-56ef-1234567890ab"
    }
  }
}
```

### Sample Response

```
{
  "datastoreId": "eaee622d8406b41eb86c0f4741201ff9",
  "jobStatus": "SUBMITTED",
  "jobId": "48d7b91dae4a64d00d54b70862f33f61"
}
```

## Resource Relationships

The operation exports resources based on their relationships within the Member Attribution List:

```
Group (Attribution List)
├── Patient (Members)
├── Coverage → RelatedPerson (Subscribers)
├── Practitioner (Attributed Providers)
├── PractitionerRole → Location
└── Organization (Attributed Providers)
```

### Resource Sources

| Resource         | Source Location                           | Description                                          |
| ---------------- | ----------------------------------------- | ---------------------------------------------------- |
| Patient          | Group.member.entity                       | The patients who are members of the attribution list |
| Coverage         | Group.member.extension:coverageReference  | Coverage that resulted in patient membership         |
| Organization     | Group.member.extension:attributedProvider | Organizations patients are attributed to             |
| Practitioner     | Group.member.extension:attributedProvider | Individual practitioners patients are attributed to  |
| PractitionerRole | Group.member.extension:attributedProvider | Practitioner roles patients are attributed to        |
| RelatedPerson    | Coverage.subscriber                       | Subscribers of the coverage                          |
| Location         | PractitionerRole.location                 | Locations associated with practitioner roles         |
| Group            | Input endpoint                            | The attribution list itself                          |

## Job Management

Check Job Status
`GET [base]/export/[job-id]`

Cancel Job
`DELETE [base]/export/[job-id]`

### Job Lifecycle

- `SUBMITTED` - Job has been received and queued
- `IN_PROGRESS` - Job is actively processing
- `COMPLETED` - Job finished successfully, files available for download
- `FAILED` - Job encountered an error

## Output Format

- _File Format_: NDJSON (Newline Delimited JSON)
- _File Organization_: Separate files for each resource type
- _File Extension_: .ndjson
- _Location_: Specified S3 bucket and path

## Error Handling

The operation returns HTTP 400 Bad Request with an OperationOutcome for the following conditions:

Authorization Errors

- Invalid or insufficient permissions for data access
- S3 bucket access issues
- KMS key access problems

Parameter Validation Errors

- `patient` parameter not formatted as "Patient/id,Patient/id,..."
- Invalid patient references or patients not part of the Group
- `exportType` value other than hl7.fhir.us.davinci-atr
- `_type` parameter containing unsupported resource types
- `_type` parameter missing required minimum types (Group, Patient, Coverage) for the exportType of hl7.fhir.us.davinci-atr

Resource Validation Errors

- Requested Group resource does not exist
- Group has empty member list
- Group members don't reference valid Patient resources

## Security and Authorization

- Standard FHIR authorization mechanisms apply
- Clients must have appropriate read permissions for the Group and related resources
- S3 bucket write permissions required for output location
- KMS key permissions required if encryption is specified

## Best Practices

- _Resource Type Selection_: Only request the resource types you need to minimize export size and processing time
- _Time-based Filtering_: Use `_since` parameter for incremental exports
- _Patient Filtering_: Use `patient` parameter when you only need data for specific members
- _Job Monitoring_: Regularly check job status for large exports
- _Error Handling_: Implement proper retry logic for failed jobs

## Limitations

- Maximum of 512 patients can be specified in the `patient` parameter
- Export is limited to Group-level operations only
- Only supports the predefined set of attribution-related resource types
- Output is always in NDJSON format
