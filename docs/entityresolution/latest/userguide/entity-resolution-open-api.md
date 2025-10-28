# Using the AWS Entity Resolution OpenAPI specification

The OpenAPI specification defines all the protocols associated with AWS Entity Resolution. This
specification is necessary to implement the integration.

The OpenAPI definition contains the following API operations:

- `POST AssignIdentities`
- `POST CreateJob`
- `GET GetJob`
- `POST StartJob`
- `POST MapIdentities`
- `GET Schema`
  To request the OpenAPI specification, contact the AWS Entity Resolution Business Development team at
  `<aws-entity-resolution-bd@amazon.com>`.

The OpenAPI specification support two types of integrations for both encoding and
transcoding consumer identifiers batch processing and synchronous processing. After you have
obtained the OpenAPI specification, implement the type of processing integration for your use
case.

###### Topics

- [Batch processing integration](#batch-processing-integration "#batch-processing-integration")
- [Synchronous processing
  integration](#entity-resolution-synchronous-processing "#entity-resolution-synchronous-processing")

## Batch processing integration

The batch processing integration follows an asynchronous design pattern. After a
workflow is initiated on AWS Data Exchange, it submits a job via a provider integration endpoint and
then the workflow waits on this job completion by periodically polling for job status. This
solution is more desirable for job runs that may take longer and have a lower provider
throughput. The provider will intake the dataset location as an Amazon S3 link, which they can
process on their end and write the results to a predetermined output S3 location.

The batch processing integration is enabled using three the API definitions. AWS Entity Resolution will
call the provider endpoint which is available through AWS Data Exchange in the following order:

1. `POST CreateJob`: This API operation submits the job information to the
   provider to process. These informations are about the type of job; Encoding or
   Transcoding, S3 locations, Schema provided by customer, and any additional job
   properties required.

This API returns a `JobId`, and the Status for the Job will be one of the
following: `PENDING`, `READY`, `IN_PROGRESS`,
`COMPLETE`, or `FAILED`.

**Sample request for encoding**

```
POST /jobs
{
  "actionType": "ID_ASSIGNMENT",
  "s3SourceLocation": "string",
  "s3TargetLocation": "string",
  "jobProperties": {
    "assignmentJobProperties": {
      "fieldMappings": [
        {
          "name": "string",
          "type": "NAME"
        }
      ]
    }
  },
  "customerSpecifiedJobProperties": {
    "property1": "string",
    "property2": "string"
  },
  "outputSourceConfiguration": {
    "KMSArn": "string"
  }
}
```

**Sample response**

```
{
  "jobId": "string",
  "status": "PENDING"
}
```

2. `POST StartJob`: This API lets the provider know to start the job based
   on the `JobId` provided. This allows the provider to perform any validations
   needed from `CreateJob` until `StartJob`.

This API returns a `JobId`, the `Status` for the Job, the
`statusMessage`, and `statusCode`.

**Sample request for encoding**

```
POST/jobs/{jobId}
{
  "customerSpecifiedJobProperties": {
    "property1": "string",
    "property2": "string"
  }
}
```

**Sample response**

```
{
  "jobId": "string",
  "status": "PENDING",
  "statusMessage": "string",
  "statusCode": 200
}
```

3. `GET GetJob`: This API informs AWS Entity Resolution if the job has been completed or any
   other status.

This API returns a `JobId`, the `Status` for the Job, the
`statusMessage`, and `statusCode`.

**Sample request for encoding**

```
GET /jobs/{jobId}
```

**Sample response**

```
{
  "jobId": "string",
  "status": "PENDING",
  "statusMessage": "string",
  "statusCode": 200
}
```

The full definition of these APIs are provided in the AWS Entity Resolution OpenAPI specification.

## Synchronous processing

integration

The synchronous processing solution is more desirable for the providers that have a near
real-time response time with real-time response time with higher throughput and higher TPS.
This AWS Entity Resolution workflow partitions the dataset and makes multiple API requests in parallel. The
AWS Entity Resolution workflow then handles writing the results to desired output location.

This process is enabled using one of the API definitions. AWS Entity Resolution calls the provider
endpoint which is available through AWS Data Exchange:

`POST AssignIdentities`: This API sends data to the provider using a
`source_id` identifier and `recordFields` associated with that
record.

This API returns the `assignedRecords`.

**Sample request for encoding**

```
POST /assignment
{
  "sourceRecords": [
    {
      "sourceId": "string",
      "recordFields": [
        {
          "name": "string",
          "type": "NAME",
          "value": "string"
        }
      ]
    }
  ]
}
```

**Sample response**

```
{
  "assignedRecords": [
    {
      "sourceRecord": {
        "sourceId": "string",
        "recordFields": [
          {
            "name": "string",
            "type": "NAME",
            "value": "string"
          }
        ]
      },
      "identity": any
    }
  ]
}
```

The full definition of these APIs are provided in the AWS Entity Resolution OpenAPI specification.

Depending on which approach the provider chooses, AWS Entity Resolution will create a configuration for
that the provider that will be used to initiate the encoding or transcoding. In addition,
these configurations are available to the customers using the APIs provided by AWS Entity Resolution.

This configuration is accessible using an Amazon Resource Name (ARN), which is derived
from where the provider service offering on AWS Data Exchange is hosted, and the type of the provider
service. AWS Entity Resolution refers to this ARN as the `providerServiceARN`.
