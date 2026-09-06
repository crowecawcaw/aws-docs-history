

# Exporting HealthLake data with FHIR `$export`
<a name="reference-fhir-operations-export"></a>

You can export data in bulk from your HealthLake data store using the FHIR $export operation. HealthLake supports FHIR `$export` using `POST` and `GET` requests. To make an export request with `POST`, you must have a IAM user, group, or role with the required permissions, specify `$export` as part of the request, and include desired parameters in the request body.

**Note**  
All HealthLake export requests made using FHIR `$export` are returned in `ndjson` format and exported to an Amazon S3 bucket, where each Amazon S3 object contains only a single FHIR resource type.  
You can queue export requests per the AWS account service quotas. For more information, see [Service quotas](reference-healthlake-endpoints-quotas.md#reference-healthlake-quotas).

HealthLake supports the following three types of bulk export endpoint requests.


**HealthLake bulk `$export` types**  

| Export type | Description | Syntax | 
| --- | --- | --- | 
| System | Export all data from the HealthLake FHIR server. | `POST https://healthlake.{{region}}.amazonaws.com/datastore/{{datastoreId}}/r4/$export` | 
| All patients | Export all data relating to all patients including resource types associated with the Patient resource type. | `POST https://healthlake.{{region}}.amazonaws.com/datastore/{{datastoreId}}/r4/Patient/$export`<br />`GET https://healthlake.{{region}}.amazonaws.com/datastore/{{datastoreId}}/r4/Patient/$export` | 
| Group of patients | Export all data relating to a group of patients specified with a Group ID. | `POST https://healthlake.{{region}}.amazonaws.com/datastore/{{datastoreId}}/r4/Group/{{id}}/$export`<br />`GET https://healthlake.{{region}}.amazonaws.com/datastore/{{datastoreId}}/r4/Group/{{id}}/$export` | 

## Before you begin
<a name="export-rest-before-you-begin"></a>

Meet the following requirements to make an export request using the FHIR REST API for HealthLake.
+ You must have set up a user, group, or role that has the necessary permissions to make the export request. To learn more, see [Authorizing an `$export` request](#export-rest-auth).
+ You must have created a service role that grants HealthLake access to the Amazon S3 bucket to which you want your data to be exported. The service role must also specify HealthLake as the service principal. For more information about setting up permissions, see [Setting up permissions for export jobs](getting-started-setting-up.md#setting-up-export-permissions).

## Authorizing an `$export` request
<a name="export-rest-auth"></a>

To make a successful export request using the FHIR REST API, authorize your user, group, or role using either IAM or OAuth2.0. You must also have a service role.

**Authorizing a request using IAM**  
When you make an `$export` request, the user, group, or role must have IAM actions included in the policy. For more information, see [Setting up permissions for export jobs](getting-started-setting-up.md#setting-up-export-permissions).

**Authorizing a request using SMART on FHIR (OAuth 2.0)**  
When you make an `$export` request on a SMART on FHIR-enabled HealthLake data store, you must have the appropriate scopes assigned. For more information, see [SMART on FHIR resource scopes for HealthLake](reference-smart-on-fhir-oauth-scopes.md#smart-on-fhir-scopes-rest).

**Note**  
FHIR `$export` with `GET` requests require the same authentication method or bearer token (in the case of SMART on FHIR) to request the export and retrieve files. Files exported using FHIR `$export` with `GET` are available for download for 48 hours.

## Making an `$export` request
<a name="export-rest-request"></a>

This section describes the required steps you must take when making an export request using the FHIR REST API.

To avoid accidental charges on your AWS account, we recommend testing your requests by making a `POST` request without supplying the `$export` syntax.

To make the request, you must do the following:

1. Specify `$export` in the `POST` request URL for a supported endpoint.

1. Specify the required header parameters.

1. Specify a request body that defines the required parameters.

### Step 1: Specify `$export` in the `POST` request URL for a supported [endpoint](reference-healthlake-endpoints-quotas.md#reference-healthlake-endpoints).
<a name="export-rest-request-step-1"></a>

HealthLake supports three types of bulk export endpoint requests. To make a bulk export request, you must make a `POST`-based request on one of the three supported endpoints. The following examples demonstrate where to specify `$export` in the request URL.
+ `POST https://healthlake.{{region}}.amazonaws.com/datastore/{{datastoreId}}/r4/$export`
+ `POST https://healthlake.{{region}}.amazonaws.com/datastore/{{datastoreId}}/r4/Patient/$export`
+ `POST https://healthlake.{{region}}.amazonaws.com/datastore/{{datastoreId}}/r4/Group/{{id}}/$export`

You can use the following supported search parameters in the `POST` request string.

#### Supported search parameters
<a name="export-rest-query-parameters"></a>

HealthLake supports the following search modifiers in bulk export requests.

The following examples include special characters which must be encoded prior to submitting your request.


| Name | Required? | Description | Example | 
| --- | --- | --- | --- | 
| \_outputFormat | No | The format for the requested Bulk Data files to be generated. Accepted values are application/fhir\+ndjson, application/ndjson, ndjson. |  | 
| \_type | No | A string of comma delimited FHIR resource types that you want included in your export job. We recommend including \_type because this can have a cost implication when all resources are exported. | &\_type=MedicationStatement, Observation | 
| \_since | No | Resource types modified on or after the date time stamp. If a resource type does not have a last updated time they will be included in your response. | &\_since=2024-05-09T00%3A00%3A00Z | 
| \_until | No | Resources types modified on or before the date time stamp. Used in combination with \_since to define a specific time range for export. If a resource type does not have a last updated time they will be excluded from your response. | &\_until=2024-12-31T23%3A59%3A59Z | 
| \_security | No | Filter exported resources by meta.security Coding values. Use the system\|code format. When multiple values are provided, resources must match all of them (AND semantics). Use system\| (trailing pipe, no code) to match any code from a given system. | &\_security=https://myorg.com/tenant%7Cclinic-A | 
| \_tag | No | Filter exported resources by meta.tag Coding values. Uses the same system\|code format and AND semantics as \_security. When both \_security and \_tag are specified, resources must match both filters. | &\_tag=https://myorg.com/dept%7Ccardiology | 

### Step 2: Specify the required header parameters
<a name="export-rest-request-step-2"></a>

To make an export request using the FHIR REST API, you must specify the following header parameters.
+ Content-Type: `application/fhir+json`
+ Prefer: `respond-async`

Next, you must specify the required elements in the request body.

### Step 3: Specify a request body the defines the required parameters.
<a name="export-rest-request-step-3"></a>

The export request also requires a body in `JSON` format. The body can include the following parameters.


| Key | Required? | Description | Value | 
| --- | --- | --- | --- | 
| DataAccessRoleArn | Yes | An ARN of a HealthLake service role. The service role used must specify HealthLake as the service principal. | arn:aws:iam::444455556666:role/your-healthlake-service-role | 
| JobName | No | The name of the export request. | your-export-job-name | 
| S3Uri | Yes | Part of an OutputDataConfig key. The S3 URI of the destination bucket where your exported data will be downloaded. | s3://amzn-s3-demo-bucket/EXPORT-JOB/ | 
| KmsKeyId | Yes | Part of an OutputDataConfig key. The ARN of the AWS KMS key used to secure the Amazon S3 bucket. | arn:aws:kms:region-of-bucket:123456789012:key/1234abcd-12ab-34cd-56ef-1234567890ab | 

**Example Body of an export request made using the FHIR REST API**  
To make an export request by using the FHIR REST API, you must specify a body, as shown in the following.  

```
{
  "DataAccessRoleArn": "arn:aws:iam::444455556666:role/your-healthlake-service-role",
  "JobName": "your-export-job",
  "OutputDataConfig": {
    "S3Configuration": {
      "S3Uri": "s3://amzn-s3-demo-bucket/EXPORT-JOB",
      "KmsKeyId": "arn:aws:kms:region-of-bucket:444455556666:key/1234abcd-12ab-34cd-56ef-1234567890ab"
    }
  }
}
```

When your request is successful, you will receive the following response.

*Response Header*

```
content-location: https://healthlake.{{region}}.amazonaws.com/datastore/{{datastoreId}}/r4/export/your-export-request-job-id
```

*Response Body*

```
{
  "datastoreId": "your-data-store-id",
  "jobStatus": "SUBMITTED",
  "jobId": "your-export-request-job-id"
}
```

## Managing your export request
<a name="export-rest-management"></a>

After making a successful export request, you can manage the request using `$export` to describe the status of a current export request, and `$export` to cancel a current export request.

When you cancel an export request using the REST API, you are only billed for the portion of the data that was exported up to the time you submitted the cancel request.

The following topics describe how you can get the status on or cancel a current export request.

### Canceling an export request
<a name="export-rest-management-describe"></a>

To cancel an export request, make a `DELETE` request and supply the job ID in the request URL.

```
DELETE https://healthlake.{{region}}.amazonaws.com/datastore/{{datastoreId}}/r4/export/your-export-request-job-id
```

When your request is successful, you receive the following.

```
{
  "exportJobProperties": {
    "jobId": "your-original-export-request-job-id",
    "jobStatus": "CANCEL_SUBMITTED",
    "datastoreId": "your-data-store-id"
  }
}
```

When your request is not successful, you receive the following.

```
{
  "resourceType": "OperationOutcome",
  "issue": [
    {
      "severity": "error",
      "code": "not-supported",
      "diagnostics": "Interaction not supported."
    }
  ]
}
```

### Describing an export request
<a name="export-rest-management-describe"></a>

To get the status of an export request, make a `GET` request by using `export` and your `export-request-job-id`.

```
GET https://healthlake.{{region}}.amazonaws.com/datastore/{{datastoreId}}/r4/export/your-export-request-id
```

The JSON response will contain an `ExportJobProperties` object. It may contain the following key:value pairs.


| Name | Required? | Description | Value | 
| --- | --- | --- | --- | 
| DataAccessRoleArn | No | An ARN of a HealthLake service role. The service role used must specify HealthLake as the service principal. | arn:aws:iam::444455556666:role/your-healthlake-service-role | 
| SubmitTime | No | The date time an export job was submitted. | Apr 21, 2023 5:58:02 | 
| EndTime | No | The time an export job was completed. | Apr 21, 2023 6:00:08 PM | 
| JobName | No | The name of the export request. | your-export-job-name | 
| JobStatus | No |  | Valid values are:<pre>SUBMITTED | IN_PROGRESS | COMPLETED_WITH_ERRORS | COMPLETED |<br />      FAILED</pre> | 
| S3Uri | Yes | Part of an [OutputDataConfig](https://docs.aws.amazon.com/healthlake/latest/APIReference/API_OutputDataConfig.html) object. The Amazon S3 URI of the destination bucket where your exported data will be downloaded. | s3://amzn-s3-demo-bucket/EXPORT-JOB/ | 
| KmsKeyId | Yes | Part of an [OutputDataConfig](https://docs.aws.amazon.com/healthlake/latest/APIReference/API_OutputDataConfig.html) object. The ARN of the AWS KMS key used to secure the Amazon S3 bucket. | arn:aws:kms:region-of-bucket:123456789012:key/1234abcd-12ab-34cd-56ef-1234567890ab | 

**Example : Body of a describe export request made using the FHIR REST API**  
When successful, you will get the following JSON response.  

```
{
  "exportJobProperties": {
    "jobId": "your-export-request-id",
    "JobName": "your-export-job",
    "jobStatus": "SUBMITTED",
    "submitTime": "Apr 21, 2023 5:58:02 PM",
    "endTime": "Apr 21, 2023 6:00:08 PM",
    "datastoreId": "your-data-store-id",
    "outputDataConfig": {
      "s3Configuration": {
        "S3Uri": "s3://amzn-s3-demo-bucket/EXPORT-JOB",
        "KmsKeyId": "arn:aws:kms:region-of-bucket:444455556666:key/1234abcd-12ab-34cd-56ef-1234567890ab""
      }
    },
    "DataAccessRoleArn": "arn:aws:iam::444455556666:role/your-healthlake-service-role",
  }
}
```