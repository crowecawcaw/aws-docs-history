

# Monitoring HealthLake events using Amazon EventBridge
<a name="monitoring-eventbridge"></a>

Amazon EventBridge is a serverless service that uses events to connect application components together, making it easier for you to build scalable event-driven applications. The basis of EventBridge is to create [rules](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-rules.html) that route [events](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-events.html) to [targets](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-targets.html). AWS HealthLake provides durable delivery of state changes to EventBridge. For more information, see [What is Amazon EventBridge?](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-what-is.html) in the *Amazon EventBridge User Guide*.

**Note**  
To learn how to send HealthLake events to Amazon EventBridge, see [ Amazon EventBridge integration for AWS HealthLake](https://aws.amazon.com/blogs/industries/amazon-eventbridge-integration-for-aws-healthlake) in the *AWS for Industries* blog. 

**Topics**
+ [HealthLake events sent to EventBridge](#event-notifications-listing)
+ [HealthLake event structure](#event-notifications-structure)

## HealthLake events sent to EventBridge
<a name="event-notifications-listing"></a>

The following table lists all HealthLake events sent to EventBridge for processing.

<a name="event-notifications-table"></a>
<table>
<thead>
  <tr><th>HealthLake event type</th><th>State</th></tr>
</thead>
<tbody>
  <tr><td colspan="2"> <b>Data store events</b> </td></tr>
  <tr><td>     Data Store Creating</td><td><code>CREATING</code></td></tr>
  <tr><td>     Data Store Active</td><td><code>ACTIVE</code></td></tr>
  <tr><td>     Data Store Deleting</td><td><code>DELETING</code></td></tr>
  <tr><td>     Data Store Deleted</td><td><code>DELETED</code></td></tr>
  <tr><td>     Data Store Creation Failed</td><td><code>CREATE_FAILED</code></td></tr>
  <tr><td colspan="2">For more information, see <a href="https://docs.aws.amazon.com/healthlake/latest/APIReference/API_DatastoreProperties.html#HealthLake-Type-DatastoreProperties-DatastoreStatus">https://docs.aws.amazon.com/healthlake/latest/APIReference/API_DatastoreProperties.html#HealthLake-Type-DatastoreProperties-DatastoreStatus</a> in the <i>AWS HealthLake API Reference.</i></td></tr>
  <tr><td colspan="2"> <b>Import job events</b> </td></tr>
  <tr><td>     Import Job Submitted</td><td><code>SUBMITTED</code></td></tr>
  <tr><td>     Import Job In Progress</td><td><code>IN_PROGRESS</code></td></tr>
  <tr><td>     Import Job Completed With Errors</td><td><code>COMPLETED_WITH_ERRORS</code></td></tr>
  <tr><td>     Import Job Completed</td><td><code>COMPLETED</code></td></tr>
  <tr><td>     Import Job Failed</td><td><code>FAILED</code></td></tr>
  <tr><td colspan="2">For more information, see <a href="https://docs.aws.amazon.com/healthlake/latest/APIReference/API_ImportJobProperties.html#HealthLake-Type-ImportJobProperties-JobStatus">https://docs.aws.amazon.com/healthlake/latest/APIReference/API_ImportJobProperties.html#HealthLake-Type-ImportJobProperties-JobStatus</a> in the <i>AWS HealthLake API Reference.</i></td></tr>
  <tr><td colspan="2"> <b>Export job events</b> </td></tr>
  <tr><td>     Export Job Submitted</td><td><code>SUBMITTED</code></td></tr>
  <tr><td>     Export Job In Progress</td><td><code>IN_PROGRESS</code></td></tr>
  <tr><td>     Export Job Completed With Errors</td><td><code>COMPLETED_WITH_ERRORS</code></td></tr>
  <tr><td>     Export Job Completed</td><td><code>COMPLETED</code></td></tr>
  <tr><td>     Export Job Failed</td><td><code>FAILED</code></td></tr>
  <tr><td colspan="2">For more information, see <a href="https://docs.aws.amazon.com/healthlake/latest/APIReference/API_ExportJobProperties.html#HealthLake-Type-ExportJobProperties-JobStatus">https://docs.aws.amazon.com/healthlake/latest/APIReference/API_ExportJobProperties.html#HealthLake-Type-ExportJobProperties-JobStatus</a> in the <i>AWS HealthLake API Reference.</i></td></tr>
</tbody>
</table>


## HealthLake event structure
<a name="event-notifications-structure"></a>

HealthLake events are objects with JSON structure that also contain metadata details. You can use the metadata as input to either recreate an event or learn more information. All associated metadata fields are listed in a table under the code examples in the following menus. For more information, see [AWS service event metadata](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-events-structure.html) in the *Amazon EventBridge User Guide*.

**Note**  
To learn how to send HealthLake events to Amazon EventBridge, see [ Amazon EventBridge integration for AWS HealthLake](https://aws.amazon.com/blogs/industries/amazon-eventbridge-integration-for-aws-healthlake) in the *AWS for Industries* blog. 

### Data store events
<a name="event-notifications-data-store"></a>

------
#### [ Data Store Creating ]

**State - `CREATING`**

```
{
    "version": "0",
    "id": "514ad836-bb8a-4523-a10b-fa2756c3bdb0",
    "detail-type": "Data Store Creating",
    "source": "aws.healthlake",
    "account": "123456789012",
    "time": "2023-12-08T08:58:12Z",
    "region": "us-east-1",
    "resources":
    [
        "arn:aws:healthlake:us-east-1:123456789012:datastore/fhir/eeb8005725ae22b35b4edbdc68cf2dfd"
    ],
    "detail":
    {
        "datastoreId": "eeb8005725ae22b35b4edbdc68cf2dfd",
        "datastoreName": "your-data-store-name",
        "datastoreTypeVersion": "R4",
        "datastoreEndpoint": "https://healthlake.us-east-1.amazonaws.com/datastore/eeb8005725ae22b35b4edbdc68cf2dfd/r4/"
    }
}
```

------
#### [ Data Store Active ]

**State - `ACTIVE`**

```
{
    "version": "0",
    "id": "d57105bc-0d2d-4009-b34d-453e2567c599",
    "detail-type": "Data Store Active",
    "source": "aws.healthlake",
    "account": "123456789012",
    "time": "2023-12-08T09:16:51Z",
    "region": "us-east-1",
    "resources":
    [
        "arn:aws:healthlake:us-east-1:123456789012:datastore/fhir/eeb8005725ae22b35b4edbdc68cf2dfd"
    ],
    "detail":
    {
        "datastoreId": "eeb8005725ae22b35b4edbdc68cf2dfd",
        "datastoreName": "your-data-store-name",
        "datastoreTypeVersion": "R4",
        "datastoreEndpoint": "https://healthlake.us-east-1.amazonaws.com/datastore/eeb8005725ae22b35b4edbdc68cf2dfd/r4/"
    }
}
```

------
#### [ Data Store Deleting ]

**State - `DELETING`**

```
{
    "version": "0",
    "id": "d135ee1f-e14a-4730-8766-7b98f822c94a",
    "detail-type": "Data Store Deleting",
    "source": "aws.healthlake",
    "account": "123456789012",
    "time": "2023-12-08T12:44:47Z",
    "region": "us-east-1",
    "resources":
    [
        "arn:aws:healthlake:us-east-1:123456789012:datastore/fhir/eeb8005725ae22b35b4edbdc68cf2dfd"
    ],
    "detail":
    {
        "datastoreId": "eeb8005725ae22b35b4edbdc68cf2dfd",
        "datastoreName": "your-data-store-name",
        "datastoreTypeVersion": "R4",
        "datastoreEndpoint": "https://healthlake.us-east-1.amazonaws.com/datastore/eeb8005725ae22b35b4edbdc68cf2dfd/r4/"
    }
}
```

------
#### [ Data Store Deleted ]

**State - `DELETED`**

```
{
    "version": "0",
    "id": "6d880b86-e115-4947-81a9-494db704571a",
    "detail-type": "Data Store Deleted",
    "source": "aws.healthlake",
    "account": "123456789012",
    "time": "2023-05-12T12:58:03Z",
    "region": "us-east-1",
    "resources":
    [
        "arn:aws:healthlake:us-east-1:123456789012:datastore/fhir/eeb8005725ae22b35b4edbdc68cf2dfd"
    ],
    "detail":
    {
        "datastoreId": "eeb8005725ae22b35b4edbdc68cf2dfd",
        "datastoreName": "your-data-store-name",
        "datastoreTypeVersion": "R4",
        "datastoreEndpoint": "https://healthlake.us-east-1.amazonaws.com/datastore/eeb8005725ae22b35b4edbdc68cf2dfd/r4/"
    }
}
```

------


**Data store events - metadata descriptions**  

| Name | Type | Description | 
| --- | --- | --- | 
| version | string | The EventBridge event schema version. | 
| id | string | The Version 4 UUID generated for every event. | 
| detail-type | string | The type of event that is being sent. | 
| source | string | Identifies the service that generated the event. | 
| account | string | The 12-digit AWS account ID of the data store owner. | 
| time | string | The time the event occurred. | 
| region | string | Identifies the AWS Region of the data store. | 
| resources | array (string) | A JSON array that contains the ARN of the data store. | 
| detail | object | A JSON object that contains information about the event. | 
| detail.datastoreId | string | The data store ID associated with the status change event. | 
| detail.datastoreName | string | The data store name. | 
| detail.datastoreTypeVersion | string | The data store FHIR version. | 
| detail.datastoreEndpoint | string | The data store endpoint. | 

### Import job events
<a name="event-notifications-import-jobs"></a>

------
#### [ Import Job Submitted ]

**State - `SUBMITTED`**

```
{
    "version": "0",
    "id": "25e606f7-800c-da41-45df-0e68587250c9",
    "detail-type": "Import Job Submitted",
    "source": "aws.healthlake",
    "account": "123456789012",
    "time": "2023-12-08T01:50:51Z",
    "region": "us-east-1",
    "resources":
    [
        "arn:aws:healthlake:us-east-1:123456789012:datastore/fhir/eeb8005725ae22b35b4edbdc68cf2dfd"
    ],
    "detail":
    {
        "jobId": "08c60716d6321710893ff88410e902c2",
        "submitTime": "2023-12-08T01:50:50.986Z",
        "datastoreId": "eeb8005725ae22b35b4edbdc68cf2dfd",
        "inputDataConfig":
        {
            "s3Uri": "s3://{{amzn-s3-demo-source-bucket}}/input/"
        }
    }
}
```

------
#### [ Import Job In Progress ]

**State - `IN_PROGRESS`**

```
{
    "version": "0",
    "id": "cc886b49-2737-19c4-7c4e-84ac9429ab73",
    "detail-type": "Import Job In Progress",
    "source": "aws.healthlake",
    "account": "123456789012",
    "time": "2023-12-08T01:51:23Z",
    "region": "us-east-1",
    "resources":
    [
        "arn:aws:healthlake:us-east-1:123456789012:datastore/fhir/eeb8005725ae22b35b4edbdc68cf2dfd"
    ],
    "detail":
    {
        "jobId": "08c60716d6321710893ff88410e902c2",
        "submitTime": "2023-12-08T01:50:50.986Z",
        "datastoreId": "eeb8005725ae22b35b4edbdc68cf2dfd",
        "inputDataConfig":
        {
            "s3Uri": "s3://{{amzn-s3-demo-source-bucket}}/input/"
        }
    }
}
```

------
#### [ Import Job Completed ]

**State - `COMPLETED`**

```
{
    "version": "0",
    "id": "36c865ef-da41-76ef-c882-3ba8dad8656b",
    "detail-type": "Import Job Completed",
    "source": "aws.healthlake",
    "account": "123456789012",
    "time": "2023-12-08T02:14:42Z",
    "region": "us-east-1",
    "resources":
    [
        "arn:aws:healthlake:us-east-1:123456789012:datastore/fhir/eeb8005725ae22b35b4edbdc68cf2dfd"
    ],
    "detail":
    {
        "jobId": "08c60716d6321710893ff88410e902c2",
        "submitTime": "2023-12-08T01:50:50.986Z",
        "datastoreId": "eeb8005725ae22b35b4edbdc68cf2dfd",
        "inputDataConfig":
        {
            "s3Uri": "s3://{{amzn-s3-demo-source-bucket}}/input/"
        }
    }
}
```

------
#### [ Import Job Completed With Errors ]

**State - `COMPLETED_WITH_ERRORS`**

```
{
    "version": "0",
    "id": "b61387d7-bffe-4f01-8291-65dc4be52cc1",
    "detail-type": "Import Job Completed With Errors",
    "source": "aws.healthlake",
    "account": "123456789012",
    "time": "2023-12-08T02:14:42Z",
    "region": "us-east-1",
    "resources":
    [
        "arn:aws:healthlake:us-east-1:123456789012:datastore/fhir/eeb8005725ae22b35b4edbdc68cf2dfd"
    ],
    "detail":
    {
        "jobId": "08c60716d6321710893ff88410e902c2",
        "submitTime": "2023-12-08T01:50:50.986Z",
        "datastoreId": "eeb8005725ae22b35b4edbdc68cf2dfd",
        "inputDataConfig":
        {
            "s3Uri": "s3://{{amzn-s3-demo-source-bucket}}/input/"
        }
    }
}
```

------
#### [ Import Job Failed ]

**State - `FAILED`**

```
{
    "version": "0",
    "id": "c4d65575-d1a7-4040-9c6c-c225bf6723c5",
    "detail-type": "Import Job Failed",
    "source": "aws.healthlake",
    "account": "123456789012",
    "time": "2023-12-08T02:14:42Z",
    "region": "us-east-1",
    "resources":
    [
        "arn:aws:healthlake:us-east-1:123456789012:datastore/fhir/eeb8005725ae22b35b4edbdc68cf2dfd"
    ],
    "detail":
    {
        "jobId": "08c60716d6321710893ff88410e902c2",
        "submitTime": "2023-12-08T01:50:50.986Z",
        "datastoreId": "eeb8005725ae22b35b4edbdc68cf2dfd",
        "inputDataConfig":
        {
            "s3Uri": "s3://{{amzn-s3-demo-source-bucket}}/input/"
        }
    }
}
```

------


**Import job events - metadata descriptions**  

| Name | Type | Description | 
| --- | --- | --- | 
| version | string | The EventBridge event schema version. | 
| id | string | The Version 4 UUID generated for every event. | 
| detail-type | string | The type of event that is being sent. | 
| source | string | Identifies the service that generated the event. | 
| account | string | The 12-digit AWS account ID of the data store owner. | 
| time | string | The time the event occurred. | 
| region | string | Identifies the AWS Region of the data store. | 
| resources | array (string) | A JSON array that contains the ARN of the data store. | 
| detail | object | A JSON object that contains information about the event. | 
| detail.jobId | string | The import job ID associated with the status change event. | 
| detail.submitTime | string | The time the import job was submitted. | 
| detail.datastoreId | string | The data store that generated the status change event. | 
| detail.inputDataConfig | string | The input prefix path for the Amazon S3 bucket that contains the FHIR files to be imported. | 

### Export job events
<a name="event-notifications-export-jobs"></a>

------
#### [ Export Job Submitted ]

**State - `SUBMITTED`**

```
{
    "version": "0",
    "id": "f8af7d04-2221-4f02-a01a-6fc3ae403bab",
    "detail-type": "Export Job Submitted",
    "source": "aws.healthlake",
    "account": "123456789012",
    "time": "2023-12-08T01:50:51Z",
    "region": "us-east-1",
    "resources":
    [
        "arn:aws:healthlake:us-east-1:123456789012:datastore/fhir/eeb8005725ae22b35b4edbdc68cf2dfd"
    ],
    "detail":
    {
        "jobId": "45e899e545bf774710388260fc60b143",
        "submitTime": "2023-12-08T01:50:50.986Z",
        "datastoreId": "eeb8005725ae22b35b4edbdc68cf2dfd",
        "outputDataConfig":
        {
            "s3Uri": "s3://{{amzn-s3-demo-source-bucket}}/output/"
        }
    }
}
```

------
#### [ Export Job In Progress ]

**State - `IN_PROGRESS`**

```
{
    "version": "0",
    "id": "7bb7e39c-707d-4a83-8532-cee015299100",
    "detail-type": "Export Job In Progress",
    "source": "aws.healthlake",
    "account": "123456789012",
    "time": "2023-12-08T01:51:23Z",
    "region": "us-east-1",
    "resources":
    [
        "arn:aws:healthlake:us-east-1:123456789012:datastore/fhir/eeb8005725ae22b35b4edbdc68cf2dfd"
    ],
    "detail":
    {
        "jobId": "45e899e545bf774710388260fc60b143",
        "submitTime": "2023-12-08T01:50:50.986Z",
        "datastoreId": "eeb8005725ae22b35b4edbdc68cf2dfd",
        "outputDataConfig":
        {
            "s3Uri": "s3://{{amzn-s3-demo-source-bucket}}/output/"
        }
    }
}
```

------
#### [ Export Job Completed ]

**State - `COMPLETED`**

```
{
    "version": "0",
    "id": "d7629aa7-e63a-4b84-858c-96a62b57ebc8",
    "detail-type": "Export Job Completed",
    "source": "aws.healthlake",
    "account": "123456789012",
    "time": "2023-12-08T02:14:42Z",
    "region": "us-east-1",
    "resources":
    [
        "arn:aws:healthlake:us-east-1:123456789012:datastore/fhir/eeb8005725ae22b35b4edbdc68cf2dfd"
    ],
    "detail":
    {
        "jobId": "45e899e545bf774710388260fc60b143",
        "submitTime": "2023-12-08T01:50:50.986Z",
        "datastoreId": "eeb8005725ae22b35b4edbdc68cf2dfd",
        "outputDataConfig":
        {
            "s3Uri": "s3://{{amzn-s3-demo-source-bucket}}/output/"
        }
    }
}
```

------
#### [ Export Job Completed With Errors ]

**State - `COMPLETED_WITH_ERRORS`**

```
{
    "version": "0",
    "id": "5fa50bc5-50e3-4bc4-b66a-1b1d2f7b07a7",
    "detail-type": "Export Job Completed With Errors",
    "source": "aws.healthlake",
    "account": "123456789012",
    "time": "2023-12-08T02:14:42Z",
    "region": "us-east-1",
    "resources":
    [
        "arn:aws:healthlake:us-east-1:123456789012:datastore/fhir/eeb8005725ae22b35b4edbdc68cf2dfd"
    ],
    "detail":
    {
        "jobId": "45e899e545bf774710388260fc60b143",
        "submitTime": "2023-12-08T01:50:50.986Z",
        "datastoreId": "eeb8005725ae22b35b4edbdc68cf2dfd",
        "outputDataConfig":
        {
            "s3Uri": "s3://{{amzn-s3-demo-source-bucket}}/output/"
        }
    }
}
```

------
#### [ Export Job Failed ]

**State - `FAILED`**

```
{
    "version": "0",
    "id": "49fce45e-7e02-4846-8582-e7f19ca039cb",
    "detail-type": "Export Job Failed",
    "source": "aws.healthlake",
    "account": "123456789012",
    "time": "2023-12-08T02:14:42Z",
    "region": "us-east-1",
    "resources":
    [
        "arn:aws:healthlake:us-east-1:123456789012:datastore/fhir/eeb8005725ae22b35b4edbdc68cf2dfd"
    ],
    "detail":
    {
        "jobId": "45e899e545bf774710388260fc60b143",
        "submitTime": "2023-12-08T01:50:50.986Z",
        "datastoreId": "eeb8005725ae22b35b4edbdc68cf2dfd",
        "outputDataConfig":
        {
            "s3Uri": "s3://{{amzn-s3-demo-source-bucket}}/output/"
        }
    }
}
```

------


**Export job events - metadata descriptions**  

| Name | Type | Description | 
| --- | --- | --- | 
| version | string | The EventBridge event schema version. | 
| id | string | The Version 4 UUID generated for every event. | 
| detail-type | string | The type of event that is being sent. | 
| source | string | Identifies the service that generated the event. | 
| account | string | The 12-digit AWS account ID of the data store owner. | 
| time | string | The time the event occurred. | 
| region | string | Identifies the AWS Region of the data store. | 
| resources | array (string) | A JSON array that contains the ARN of the data store. | 
| detail | object | A JSON object that contains information about the event. | 
| detail.jobId | string | The export job ID associated with the status change event. | 
| detail.submitTime | string | The time the export job was submitted. | 
| detail.datastoreId | string | The data store that generated the status change event. | 
| detail.outputDataConfig | string | The output prefix path for the Amazon S3 bucket that contains the FHIR files to be exported. | 