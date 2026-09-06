

# Using Amazon EventBridge with HealthImaging
<a name="event-notifications"></a>

Amazon EventBridge is a serverless service that uses events to connect application components together, making it easier for you to build scalable event-driven applications. The basis of EventBridge is to create [rules](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-rules.html) that route [events](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-events.html) to [targets](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-targets.html). AWS HealthImaging provides durable delivery of state changes to EventBridge. For more information, see [What is Amazon EventBridge?](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-what-is.html) in the *Amazon EventBridge User Guide*.

**Topics**
+ [HealthImaging events sent to EventBridge](#event-notifications-listing)
+ [HealthImaging event structure and examples](#event-notifications-structure-examples)

## HealthImaging events sent to EventBridge
<a name="event-notifications-listing"></a>

The following table lists all HealthImaging events sent to EventBridge for processing.

<a name="event-notifications-table"></a>
<table>
<thead>
  <tr><th>HealthImaging event type</th><th>State</th></tr>
</thead>
<tbody>
  <tr><td colspan="2"> <b>Data store events</b> </td></tr>
  <tr><td>     Data Store Creating</td><td><code>CREATING</code></td></tr>
  <tr><td>     Data Store Creation Failed</td><td><code>CREATE_FAILED</code></td></tr>
  <tr><td>     Data Store Created</td><td><code>ACTIVE</code></td></tr>
  <tr><td>     Data Store Deleting</td><td><code>DELETING</code></td></tr>
  <tr><td>     Data Store Deleted</td><td><code>DELETED</code></td></tr>
  <tr><td colspan="2">     For more information, see <a href="https://docs.aws.amazon.com/healthimaging/latest/APIReference/API_DatastoreProperties.html#healthimaging-Type-DatastoreProperties-datastoreStatus">datastoreStatus</a> in the <i>AWS HealthImaging API Reference.</i></td></tr>
  <tr><td colspan="2"> <b>Import job events</b> </td></tr>
  <tr><td>     Import Job Submitted</td><td><code>SUBMITTED</code></td></tr>
  <tr><td>     Import Job In Progress</td><td><code>IN_PROGRESS</code></td></tr>
  <tr><td>     Import Job Completed</td><td><code>COMPLETED</code></td></tr>
  <tr><td>     Import Job Failed</td><td><code>FAILED</code></td></tr>
  <tr><td colspan="2">     For more information, see <a href="https://docs.aws.amazon.com/healthimaging/latest/APIReference/API_DICOMImportJobProperties.html#healthimaging-Type-DICOMImportJobProperties-jobStatus">jobStatus</a> in the <i>AWS HealthImaging API Reference.</i></td></tr>
  <tr><td colspan="2"> <b>Image set events</b> </td></tr>
  <tr><td>     Image Set Created</td><td><code>CREATED</code></td></tr>
  <tr><td>     Image Set Copying</td><td><code>COPYING</code></td></tr>
  <tr><td>     Image Set Copying With Read Only Access</td><td><code>COPYING_WITH_READ_ONLY_ACCESS</code></td></tr>
  <tr><td>     Image Set Copied</td><td><code>COPIED</code></td></tr>
  <tr><td>     Image Set Copy Failed</td><td><code>COPY_FAILED</code></td></tr>
  <tr><td>     Image Set Updating</td><td><code>UPDATING</code></td></tr>
  <tr><td>     Image Set Updated</td><td><code>UPDATED</code></td></tr>
  <tr><td>     Image Set Update Failed</td><td><code>UPDATE_FAILED</code></td></tr>
  <tr><td>     Image Set Deleting</td><td><code>DELETING</code></td></tr>
  <tr><td>     Image Set Deleted</td><td><code>DELETED</code></td></tr>
  <tr><td colspan="2">     For more information, see <a href="https://docs.aws.amazon.com/healthimaging/latest/APIReference/API_ImageSetProperties.html#healthimaging-Type-ImageSetProperties-ImageSetWorkflowStatus">ImageSetWorkflowStatus</a> in the <i>AWS HealthImaging API Reference.</i></td></tr>
</tbody>
</table>


## HealthImaging event structure and examples
<a name="event-notifications-structure-examples"></a>

HealthImaging events are objects with JSON structure that also contain metadata details. You can use the metadata as input to either recreate an event or learn more information. All associated metadata fields are listed in a table under the code examples in the following menus. For more information, see [Event structure reference](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-events-structure.html) in the *Amazon EventBridge User Guide*.

**Note**  
The `source` attribute for HealthImaging event structures is `aws.medical-imaging`.

### Data store events
<a name="event-notifications-data-store"></a>

------
#### [ Data Store Creating ]

**State - `CREATING`**

```
{
    "version": "0",
    "id": "7cf0fb1c-8720-4d48-baa3-6eb97b35a10e",
    "detail-type": "Data Store Creating",
    "source": "aws.medical-imaging",
    "account": "111122223333",
    "time": "2024-03-14T00:01:00Z",
    "region": "us-west-2",
    "resources": ["arn:aws:medical-imaging:us-west-2:111122223333:datastore/bbc4f3cccbae4095a34170fddc19b13d"],
    "detail": {
        "imagingVersion": "1.0",
        "datastoreId" : "bbc4f3cccbae4095a34170fddc19b13d",
        "datastoreName": "test",
        "datastoreStatus": "CREATING"     
    }
}
```

------
#### [ Data Store Creation Failed ]

**State - `CREATE_FAILED`**

```
{
    "version": "0",
    "id": "7cf0fb1c-8720-4d48-baa3-6eb97b35a10e",
    "detail-type": "Data Store Creation Failed",
    "source": "aws.medical-imaging",
    "account": "111122223333",
    "time": "2024-03-14T00:01:00Z",
    "region": "us-west-2",
    "resources": ["arn:aws:medical-imaging:us-west-2:111122223333:datastore/bbc4f3cccbae4095a34170fddc19b13d"],
    "detail": {
        "imagingVersion": "1.0",
        "datastoreId" : "bbc4f3cccbae4095a34170fddc19b13d",
        "datastoreName": "test",
        "datastoreStatus": "CREATE_FAILED"      
    }
}
```

------
#### [ Data Store Created ]

**State - `ACTIVE`**

```
{
    "version": "0",
    "id": "7cf0fb1c-8720-4d48-baa3-6eb97b35a10e",
    "detail-type": "Data Store Created",
    "source": "aws.medical-imaging",
    "account": "111122223333",
    "time": "2024-03-14T00:01:00Z",
    "region": "us-west-2",
    "resources": ["arn:aws:medical-imaging:us-west-2:111122223333:datastore/bbc4f3cccbae4095a34170fddc19b13d"],
    "detail": {
        "imagingVersion": "1.0",
        "datastoreId" : "bbc4f3cccbae4095a34170fddc19b13d",
        "datastoreName": "test",
        "datastoreStatus": "ACTIVE"     
    }
}
```

------
#### [ Data Store Deleting ]

**State - `DELETING`**

```
{
    "version": "0",
    "id": "7cf0fb1c-8720-4d48-baa3-6eb97b35a10e",
    "detail-type": "Data Store Deleting",
    "source": "aws.medical-imaging",
    "account": "111122223333",
    "time": "2024-03-14T00:01:00Z",
    "region": "us-west-2",
    "resources": ["arn:aws:medical-imaging:us-west-2:111122223333:datastore/bbc4f3cccbae4095a34170fddc19b13d"],
    "detail": {
        "imagingVersion": "1.0",
        "datastoreId" : "bbc4f3cccbae4095a34170fddc19b13d",
        "datastoreName": "test",
        "datastoreStatus": "DELETING"       
    }
}
```

------
#### [ Data Store Deleted ]

**State - `DELETED`**

```
{
    "version": "0",
    "id": "7cf0fb1c-8720-4d48-baa3-6eb97b35a10e",
    "detail-type": "Data Store Deleted",
    "source": "aws.medical-imaging",
    "account": "111122223333",
    "time": "2024-03-14T00:01:00Z",
    "region": "us-west-2",
    "resources": ["arn:aws:medical-imaging:us-west-2:111122223333:datastore/bbc4f3cccbae4095a34170fddc19b13d"],
    "detail": {
        "imagingVersion": "1.0",
        "datastoreId" : "bbc4f3cccbae4095a34170fddc19b13d",
        "datastoreName": "test",
        "datastoreStatus": "DELETED"  
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
| detail.imagingVersion | string | The version ID that tracks changes to HealthImaging's event detail schema. | 
| detail.datastoreId | string | The data store ID associated with the status change event. | 
| detail.datastoreName | string | The data store name. | 
| detail.datastoreStatus | string | The current data store status. | 

### Import job events
<a name="event-notifications-import-jobs"></a>

------
#### [ Import Job Submitted ]

**State - `SUBMITTED`**

```
{
    "version": "0",
    "id": "7cf0fb1c-8720-4d48-baa3-6eb97b35a10e",
    "detail-type": "Import Job Submitted",
    "source": "aws.medical-imaging",
    "account": "111122223333",
    "time": "2024-03-14T00:01:00Z",
    "region": "us-west-2",
    "resources": ["arn:aws:medical-imaging:us-west-2:111122223333:datastore/bbc4f3cccbae4095a34170fddc19b13d"],
    "detail": {
        "imagingVersion": "1.0",
        "datastoreId" : "bbc4f3cccbae4095a34170fddc19b13d",
        "jobId": "a6a1d220f152e7aab6d8925d995d8b76",
        "jobName": "test_only_1",
        "jobStatus": "SUBMITTED",
        "inputS3Uri": "s3://healthimaging-test-bucket/input/",
        "outputS3Uri": "s3://healthimaging-test-bucket/output/"
    }
}
```

------
#### [ Import Job In Progress ]

**State - `IN_PROGRESS`**

```
{
    "version": "0",
    "id": "7cf0fb1c-8720-4d48-baa3-6eb97b35a10e",
    "detail-type": "Import Job In Progress",
    "source": "aws.medical-imaging",
    "account": "111122223333",
    "time": "2024-03-14T00:01:00Z",
    "region": "us-west-2",
    "resources": ["arn:aws:medical-imaging:us-west-2:111122223333:datastore/bbc4f3cccbae4095a34170fddc19b13d"],
    "detail": {
        "imagingVersion": "1.0",
        "datastoreId" : "bbc4f3cccbae4095a34170fddc19b13d",
        "jobId": "a6a1d220f152e7aab6d8925d995d8b76",
        "jobName": "test_only_1",
        "jobStatus": "IN_PROGRESS",
        "inputS3Uri": "s3://healthimaging-test-bucket/input/",
        "outputS3Uri": "s3://healthimaging-test-bucket/output/"
    }
}
```

------
#### [ Import Job Completed ]

**State - `COMPLETED`**

```
{
    "version": "0",
    "id": "7cf0fb1c-8720-4d48-baa3-6eb97b35a10e",
    "detail-type": "Import Job Completed",
    "source": "aws.medical-imaging",
    "account": "111122223333",
    "time": "2024-03-14T00:01:00Z",
    "region": "us-west-2",
    "resources": ["arn:aws:medical-imaging:us-west-2:111122223333:datastore/bbc4f3cccbae4095a34170fddc19b13d"],
    "detail": {
        "imagingVersion": "1.0",
        "datastoreId" : "bbc4f3cccbae4095a34170fddc19b13d",
        "jobId": "a6a1d220f152e7aab6d8925d995d8b76",
        "jobName": "test_only_1",
        "jobStatus": "COMPLETED",
        "inputS3Uri": "s3://healthimaging-test-bucket/input/",
        "outputS3Uri": "s3://healthimaging-test-bucket/output/"
    }
}
```

------
#### [ Import Job Failed ]

**State - `FAILED`**

```
{
    "version": "0",
    "id": "7cf0fb1c-8720-4d48-baa3-6eb97b35a10e",
    "detail-type": "Import Job Failed",
    "source": "aws.medical-imaging",
    "account": "111122223333",
    "time": "2024-03-14T00:01:00Z",
    "region": "us-west-2",
    "resources": ["arn:aws:medical-imaging:us-west-2:111122223333:datastore/bbc4f3cccbae4095a34170fddc19b13d"],
    "detail": {
        "imagingVersion": "1.0",
        "datastoreId" : "bbc4f3cccbae4095a34170fddc19b13d",
        "jobId": "a6a1d220f152e7aab6d8925d995d8b76",
        "jobName": "test_only_1",
        "jobStatus": "FAILED",
        "inputS3Uri": "s3://healthimaging-test-bucket/input/",
        "outputS3Uri": "s3://healthimaging-test-bucket/output/"
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
| detail.imagingVersion | string | The version ID that tracks changes to HealthImaging's event detail schema. | 
| detail.datastoreId | string | The data store that generated the status change event. | 
| detail.jobId | string | The import job ID associated with the status change event. | 
| detail.jobName | string | The import job name. | 
| detail.jobStatus | string | The current job status. | 
| detail.inputS3Uri | string | The input prefix path for the S3 bucket that contains the DICOM files to be imported. | 
| detail.outputS3Uri | string | The output prefix of the S3 bucket where the results of the DICOM import job will be uploaded. | 

### Image set events
<a name="event-notifications-image-sets"></a>

------
#### [ Image Set Created ]

**State - `CREATED`**

```
{
   "version": "0",
   "id": "7cf0fb1c-8720-4d48-baa3-6eb97b35a10e",
   "detail-type": "Image Set Created",
   "source": "aws.medical-imaging",
   "account": "111122223333",
   "time": "2024-03-14T00:01:00Z",
   "region": "us-west-2",
   "resources": ["arn:aws:medical-imaging:us-west-2:846006145877:datastore/bbc4f3cccbae4095a34170fddc19b13d/imageset/207284eef860ac01c4b2a8de27a6fc11"],
   "detail": {
      "imagingVersion": "1.0",
      "isPrimary": true,
      "imageSetVersion": "1",
      "datastoreId": "bbc4f3cccbae4095a34170fddc19b13d",
      "imagesetId": "5b3a711878c34d40e888253319388649",
      "imageSetState": "ACTIVE",
      "imageSetWorkflowStatus": "CREATED"
   }
}
```

------
#### [ Image Set Copying ]

**State - `COPYING`**

```
{
   "version": "0",
   "id": "7cf0fb1c-8720-4d48-baa3-6eb97b35a10e",
   "detail-type": "Image Set Copying",
   "source": "aws.medical-imaging",
   "account": "111122223333",
   "time": "2024-03-14T00:01:00Z",
   "region": "us-west-2",
   "resources": ["arn:aws:medical-imaging:us-west-2:846006145877:datastore/bbc4f3cccbae4095a34170fddc19b13d/imageset/207284eef860ac01c4b2a8de27a6fc11"],
   "detail": {
      "imagingVersion": "1.0",
      "isPrimary": true,
      "imageSetVersion": "1",
      "datastoreId": "bbc4f3cccbae4095a34170fddc19b13d",
      "imagesetId": "5b3a711878c34d40e888253319388649",
      "imageSetState": "LOCKED",
      "imageSetWorkflowStatus": "COPYING",
      "sourceImageSetArn": "arn:aws:medical-imaging:us-west-2:147997158357:datastore/c381ee9b9ef34902a45b476dd7be068b/imageset/0309de3674fd551fa7ddd2880b21f990"
   }
}
```

------
#### [ Image Set Copying With Read Only Access ]

**State - `COPYING_WITH_READ_ONLY_ACCESS`**

```
{
   "version": "0",
   "id": "7cf0fb1c-8720-4d48-baa3-6eb97b35a10e",
   "detail-type": "Image Set Copying With Read Only Access",
   "source": "aws.medical-imaging",
   "account": "111122223333",
   "time": "2024-03-14T00:01:00Z",
   "region": "us-west-2",
   "resources": ["arn:aws:medical-imaging:us-west-2:846006145877:datastore/bbc4f3cccbae4095a34170fddc19b13d/imageset/207284eef860ac01c4b2a8de27a6fc11"],
   "detail": {
      "imagingVersion": "1.0",
      "isPrimary": true,
      "imageSetVersion": "1",
      "datastoreId": "bbc4f3cccbae4095a34170fddc19b13d",
      "imagesetId": "5b3a711878c34d40e888253319388649",
      "imageSetState": "LOCKED",
      "imageSetWorkflowStatus": "COPYING_WITH_READ_ONLY_ACCESS"
   }
}
```

------
#### [ Image Set Copied ]

**State - `COPIED`**

```
{
   "version": "0",
   "id": "7cf0fb1c-8720-4d48-baa3-6eb97b35a10e",
   "detail-type": "Image Set Copied",
   "source": "aws.medical-imaging",
   "account": "111122223333",
   "time": "2024-03-14T00:01:00Z",
   "region": "us-west-2",
   "resources": ["arn:aws:medical-imaging:us-west-2:846006145877:datastore/bbc4f3cccbae4095a34170fddc19b13d/imageset/207284eef860ac01c4b2a8de27a6fc11"],
   "detail": {
      "imagingVersion": "1.0",
      "isPrimary": true,
      "imageSetVersion": "1",
      "datastoreId": "bbc4f3cccbae4095a34170fddc19b13d",
      "imagesetId": "5b3a711878c34d40e888253319388649",
      "imageSetState": "ACTIVE",
      "imageSetWorkflowStatus": "COPIED"
   }
}
```

------
#### [ Image Set Copy Failed ]

**State - `COPY_FAILED`**

```
{
   "version": "0",
   "id": "7cf0fb1c-8720-4d48-baa3-6eb97b35a10e",
   "detail-type": "Image Set Copy Failed",
   "source": "aws.medical-imaging",
   "account": "111122223333",
   "time": "2024-03-14T00:01:00Z",
   "region": "us-west-2",
   "resources": ["arn:aws:medical-imaging:us-west-2:846006145877:datastore/bbc4f3cccbae4095a34170fddc19b13d/imageset/207284eef860ac01c4b2a8de27a6fc11"],
   "detail": {
      "imagingVersion": "1.0",
      "isPrimary": true,
      "imageSetVersion": "1",
      "datastoreId": "bbc4f3cccbae4095a34170fddc19b13d",
      "imagesetId": "5b3a711878c34d40e888253319388649",
      "imageSetState": "ACTIVE",
      "imageSetWorkflowStatus": "COPY_FAILED"
   }
}
```

------
#### [ Image Set Updating ]

**State - `UPDATING`**

```
{
   "version": "0",
   "id": "7cf0fb1c-8720-4d48-baa3-6eb97b35a10e",
   "detail-type": "Image Set Updating",
   "source": "aws.medical-imaging",
   "account": "111122223333",
   "time": "2024-03-14T00:01:00Z",
   "region": "us-west-2",
   "resources": ["arn:aws:medical-imaging:us-west-2:846006145877:datastore/bbc4f3cccbae4095a34170fddc19b13d/imageset/207284eef860ac01c4b2a8de27a6fc11"],
   "detail": {
      "imagingVersion": "1.0",
      "isPrimary": true,
      "imageSetVersion": "1",
      "datastoreId": "bbc4f3cccbae4095a34170fddc19b13d",
      "imagesetId": "5b3a711878c34d40e888253319388649",
      "imageSetState": "LOCKED",
      "imageSetWorkflowStatus": "UPDATING"
   }
}
```

------
#### [ Image Set Updated ]

**State - `UPDATED`**

```
{
   "version": "0",
   "id": "7cf0fb1c-8720-4d48-baa3-6eb97b35a10e",
   "detail-type": "Image Set Updated",
   "source": "aws.medical-imaging",
   "account": "111122223333",
   "time": "2024-03-14T00:01:00Z",
   "region": "us-west-2",
   "resources": ["arn:aws:medical-imaging:us-west-2:846006145877:datastore/bbc4f3cccbae4095a34170fddc19b13d/imageset/207284eef860ac01c4b2a8de27a6fc11"],
   "detail": {
      "imagingVersion": "1.0",
      "isPrimary": true,
      "imageSetVersion": "1",
      "datastoreId": "bbc4f3cccbae4095a34170fddc19b13d",
      "imagesetId": "5b3a711878c34d40e888253319388649",
      "imageSetState": "ACTIVE",
      "imageSetWorkflowStatus": "UPDATED"
   }
}
```

------
#### [ Image Set Update Failed ]

**State - `UPDATE_FAILED`**

```
{
   "version": "0",
   "id": "7cf0fb1c-8720-4d48-baa3-6eb97b35a10e",
   "detail-type": "Image Set Update Failed",
   "source": "aws.medical-imaging",
   "account": "111122223333",
   "time": "2024-03-14T00:01:00Z",
   "region": "us-west-2",
   "resources": ["arn:aws:medical-imaging:us-west-2:846006145877:datastore/bbc4f3cccbae4095a34170fddc19b13d/imageset/207284eef860ac01c4b2a8de27a6fc11"],
   "detail": {
      "imagingVersion": "1.0",
      "isPrimary": true,
      "imageSetVersion": "1",
      "datastoreId": "bbc4f3cccbae4095a34170fddc19b13d",
      "imagesetId": "5b3a711878c34d40e888253319388649",
      "imageSetState": "ACTIVE",
      "imageSetWorkflowStatus": "UPDATE_FAILED"
   }
}
```

------
#### [ Image Set Deleting ]

**State - `DELETING`**

```
{
   "version": "0",
   "id": "7cf0fb1c-8720-4d48-baa3-6eb97b35a10e",
   "detail-type": "Image Set Deleting",
   "source": "aws.medical-imaging",
   "account": "111122223333",
   "time": "2024-03-14T00:01:00Z",
   "region": "us-west-2",
   "resources": ["arn:aws:medical-imaging:us-west-2:846006145877:datastore/bbc4f3cccbae4095a34170fddc19b13d/imageset/207284eef860ac01c4b2a8de27a6fc11"],
   "detail": {
      "imagingVersion": "1.0",
      "isPrimary": true,
      "imageSetVersion": "1",
      "datastoreId": "bbc4f3cccbae4095a34170fddc19b13d",
      "imagesetId": "5b3a711878c34d40e888253319388649",
      "imageSetState": "LOCKED",
      "imageSetWorkflowStatus": "DELETING"
   }
}
```

------
#### [ Image Set Deleted ]

**State - `DELETED`**

```
{
   "version": "0",
   "id": "7cf0fb1c-8720-4d48-baa3-6eb97b35a10e",
   "detail-type": "Image Set Deleted",
   "source": "aws.medical-imaging",
   "account": "111122223333",
   "time": "2024-03-14T00:01:00Z",
   "region": "us-west-2",
   "resources": ["arn:aws:medical-imaging:us-west-2:846006145877:datastore/bbc4f3cccbae4095a34170fddc19b13d/imageset/207284eef860ac01c4b2a8de27a6fc11"],
   "detail": {
      "imagingVersion": "1.0",
      "isPrimary": true,
      "imageSetVersion": "1",
      "datastoreId": "bbc4f3cccbae4095a34170fddc19b13d",
      "imagesetId": "5b3a711878c34d40e888253319388649",
      "imageSetState": "DELETED",
      "imageSetWorkflowStatus": "DELETED"
   }
}
```

------


**Image set events - metadata descriptions**  

| Name | Type | Description | 
| --- | --- | --- | 
| version | string | The EventBridge event schema version. | 
| id | string | The Version 4 UUID generated for every event. | 
| detail-type | string | The type of event that is being sent. | 
| source | string | Identifies the service that generated the event. | 
| account | string | The 12-digit AWS account ID of the data store owner. | 
| time | string | The time the event occurred. | 
| region | string | Identifies the AWS Region of the data store. | 
| resources | array (string) | A JSON array that contains the ARN of the image set. | 
| detail | object | A JSON object that contains information about the event. | 
| detail.imagingVersion | string | The version ID that tracks changes to HealthImaging's event detail schema. | 
| detail.isPrimary | boolean | Indicates whether the imported data was successfully organized into the managed hierarchy or if there are metadata conflicts that need to be resolved. | 
| detail.imageSetVersion | string | The image set version will be incremented when an instance is imported more than once. The latest version will overwrite any older version stored within a primary image set. | 
| detail.datastoreId | string | The data store ID that generated the status change event. | 
| detail.imagesetId | string | The image set ID associated with the status change event. | 
| detail.imageSetState | string | The current image set state. | 
| detail.imageSetWorkflowStatus | string | The current image set workflow status. | 