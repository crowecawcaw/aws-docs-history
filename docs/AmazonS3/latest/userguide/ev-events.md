

# EventBridge event message structure
<a name="ev-events"></a>

The notification message that Amazon S3 sends to publish an event is in the JSON format. When Amazon S3 sends an event to Amazon EventBridge, the following fields are present.
+ `version` – Currently 0 (zero) for all events. This is an Amazon EventBridge envelope field and is not used for schema versioning. For event schema versioning, see the *event-version* field in the *detail* field.
+ `id` – A UUID generated for every event.
+ `detail-type` – The type of event that's being sent. See [Using EventBridge](EventBridge.md) for a list of event types.
+ `source` – Identifies the service that generated the event.
+ `account` – The 12-digit AWS account ID of the bucket owner.
+ `time` – The time the event occurred.
+ `region` – Identifies the AWS Region of the bucket.
+ `resources` – A JSON array that contains the Amazon Resource Name (ARN) of the bucket.
+ `detail` – A JSON object that contains information about the event. For more information about what can be included in this field, see [Event message detail field](#ev-events-detail).

## Event message structure examples
<a name="ev-events-list"></a>

The following are examples of some of the Amazon S3 event notification messages that can be sent to Amazon EventBridge.

### Object created
<a name="ev-events-object-created"></a>

```
{
  "version": "0",
  "id": "17793124-05d4-b198-2fde-7ededc63b103",
  "detail-type": "Object Created",
  "source": "aws.s3",
  "account": "111122223333",
  "time": "2021-11-12T00:00:00Z",
  "region": "ca-central-1",
  "resources": [
    "arn:aws:s3:::amzn-s3-demo-bucket1"
  ],
  "detail": {
    "version": "0",
    "event-version": "1.1",
    "bucket": {
      "name": "amzn-s3-demo-bucket1",
      "aws-generated-tags": {
        "aws:cloudformation:stack-id": "arn:aws:cloudformation:us-east-1:111122223333:stack/amzn-s3-demo-stack/51af3dc0-da77-11e4-872e-1234567db123",
        "aws:cloudformation:logical-id": "S3DemoBucket",
        "aws:cloudformation:stack-name": "amzn-s3-demo-stack"
      }
    },
    "object": {
      "key": "example-key",
      "size": 5,
      "etag": "b1946ac92492d2347c6235b4d2611184",
      "version-id": "IYV3p45BT0ac8hjHg1houSdS1a.Mro8e",
      "sequencer": "617f08299329d189"
    },
    "request-id": "N4N7GDK58NMKJ12R",
    "requester": "123456789012",
    "source-ip-address": "1.2.3.4",
    "reason": "PutObject"
  }
}
```

### Object deleted (using DeleteObject)
<a name="ev-events-object-deleted"></a>

```
{
  "version": "0",
  "id": "2ee9cc15-d022-99ea-1fb8-1b1bac4850f9",
  "detail-type": "Object Deleted",
  "source": "aws.s3",
  "account": "111122223333",
  "time": "2021-11-12T00:00:00Z",
  "region": "ca-central-1",
  "resources": [
    "arn:aws:s3:::amzn-s3-demo-bucket1"
  ],
  "detail": {
    "version": "0",
    "event-version": "1.1",
    "bucket": {
      "name": "amzn-s3-demo-bucket1"
    },
    "object": {
      "key": "example-key",
      "etag": "d41d8cd98f00b204e9800998ecf8427e",
      "version-id": "1QW9g1Z99LUNbvaaYVpW9xDlOLU.qxgF",
      "sequencer": "617f0837b476e463"
    },
    "request-id": "0BH729840619AG5K",
    "requester": "123456789012",
    "source-ip-address": "1.2.3.4",
    "reason": "DeleteObject",
    "deletion-type": "Delete Marker Created"
  }
}
```

### Object deleted (using lifecycle expiration)
<a name="ev-events-object-deleted-lifecycle"></a>

```
{
  "version": "0",
  "id": "ad1de317-e409-eba2-9552-30113f8d88e3",
  "detail-type": "Object Deleted",
  "source": "aws.s3",
  "account": "111122223333",
  "time": "2021-11-12T00:00:00Z",
  "region": "ca-central-1",
  "resources": [
    "arn:aws:s3:::amzn-s3-demo-bucket1"
  ],
  "detail": {
    "version": "0",
    "event-version": "1.1",
    "bucket": {
      "name": "amzn-s3-demo-bucket1"
    },
    "object": {
      "key": "example-key",
      "etag": "d41d8cd98f00b204e9800998ecf8427e",
      "version-id": "mtB0cV.jejK63XkRNceanNMC.qXPWLeK",
      "sequencer": "617b398000000000"
    },
    "request-id": "20EB74C14654DC47",
    "requester": "s3.amazonaws.com",
    "reason": "Lifecycle Expiration",
    "deletion-type": "Delete Marker Created"
  }
}
```

### Object restore completed
<a name="ev-events-object-restore-complete"></a>

```
{
  "version": "0",
  "id": "6924de0d-13e2-6bbf-c0c1-b903b753565e",
  "detail-type": "Object Restore Completed",
  "source": "aws.s3",
  "account": "111122223333",
  "time": "2021-11-12T00:00:00Z",
  "region": "ca-central-1",
  "resources": [
    "arn:aws:s3:::amzn-s3-demo-bucket1"
  ],
  "detail": {
    "version": "0",
    "event-version": "1.1",
    "bucket": {
      "name": "amzn-s3-demo-bucket1"
    },
    "object": {
      "key": "example-key",
      "size": 5,
      "etag": "b1946ac92492d2347c6235b4d2611184",
      "version-id": "KKsjUC1.6gIjqtvhfg5AdMI0eCePIiT3"
    },
    "request-id": "189F19CB7FB1B6A4",
    "requester": "s3.amazonaws.com",
    "restore-expiry-time": "2021-11-13T00:00:00Z",
    "source-storage-class": "GLACIER"
  }
}
```

### Object annotation created
<a name="ev-events-object-annotation-created"></a>

```
{
  "version": "0",
  "id": "8c2bfa57-4a67-b2ea-c4e0-6d420ea3b3a6",
  "detail-type": "Object Annotation Created",
  "source": "aws.s3",
  "account": "111122223333",
  "time": "2025-03-15T00:00:00Z",
  "region": "us-east-1",
  "resources": [
    "arn:aws:s3:::amzn-s3-demo-bucket1"
  ],
  "detail": {
    "version": "0",
    "event-version": "1.1",
    "bucket": {
      "name": "amzn-s3-demo-bucket1"
    },
    "object": {
      "key": "example-key",
      "etag": "b1946ac92492d2347c6235b4d2611184",
      "version-id": "IYV3p45BT0ac8hjHg1houSdS1a.Mro8e",
      "sequencer": "617f08299329d189"
    },
    "request-id": "4B4NGD358NMKJ12R",
    "requester": "123456789012",
    "source-ip-address": "1.2.3.4",
    "reason": "PutObjectAnnotation",
    "object-annotation": {
      "name": "my-annotation",
      "size": 24,
      "etag": "05df351ea190dffc26f55c74425b9d7a"
    }
  }
}
```

### Object annotation removed
<a name="ev-events-object-annotation-removed"></a>

```
{
  "version": "0",
  "id": "a3d1bc94-5f82-c7e1-d290-7e531fb4c5b8",
  "detail-type": "Object Annotation Removed",
  "source": "aws.s3",
  "account": "111122223333",
  "time": "2025-03-15T00:00:00Z",
  "region": "us-east-1",
  "resources": [
    "arn:aws:s3:::amzn-s3-demo-bucket1"
  ],
  "detail": {
    "version": "0",
    "event-version": "1.1",
    "bucket": {
      "name": "amzn-s3-demo-bucket1"
    },
    "object": {
      "key": "example-key",
      "etag": "b1946ac92492d2347c6235b4d2611184",
      "version-id": "IYV3p45BT0ac8hjHg1houSdS1a.Mro8e",
      "sequencer": "617f08299329d190"
    },
    "request-id": "7C5NGD358NMKJ34S",
    "requester": "123456789012",
    "source-ip-address": "1.2.3.4",
    "reason": "DeleteObjectAnnotation",
    "object-annotation": {
      "name": "my-annotation"
    }
  }
}
```

## Event message detail field
<a name="ev-events-detail"></a>

The detail field contains a JSON object with information about the event. The following fields may be present in the detail field.
+ `version` – Currently 0 (zero) for all events.
+ `event-version` – The event schema version in the form `{{major}}.{{minor}}` (for example, `1.1`).

  The major version is incremented if Amazon S3 makes a change to the event structure that's not backward compatible. This includes removing a JSON field that's already present or changing how the contents of a field are represented (for example, a date format).

  The minor version is incremented if Amazon S3 makes a backward-compatible change to the event structure. This includes adding new fields to the event structure or introducing new event types. To stay compatible with new minor versions of the event structure, we recommend that your applications ignore new fields.

  To ensure that your applications can parse the event structure correctly, we recommend that you do an equal-to comparison on the major version number. To ensure that the fields that are expected by your application are present, we also recommend doing a greater-than-or-equal-to comparison on the minor version.
+ `bucket` – Information about the Amazon S3 bucket involved in the event.
+ `aws-generated-tags` – Tags attached to the bucket by AWS services. Only present when AWS generated tags exist on the bucket. This field is not present for cross-Region replication events.
+ `object` – Information about the Amazon S3 object involved in the event.
+ `request-id` – Request ID in S3 response.
+ `requester` – AWS account ID or AWS service principal of requester.
+ `source-ip-address` – Source IP address of S3 request. Only present for events triggered by an S3 request.
+ `reason` – For **Object Created** events, the S3 API used to create the object: [PutObject](https://docs.aws.amazon.com/AmazonS3/latest/API/API_PutObject.html), [POST Object](https://docs.aws.amazon.com/AmazonS3/latest/API/RESTObjectPOST.html), [CopyObject](https://docs.aws.amazon.com/AmazonS3/latest/API/API_CopyObject.html), or [CompleteMultipartUpload](https://docs.aws.amazon.com/AmazonS3/latest/API/API_CompleteMultipartUpload.html). For **Object Deleted** events, this is set to **DeleteObject** when an object is deleted by an S3 API call, or **Lifecycle Expiration** when an object is deleted by an S3 Lifecycle expiration rule. For more information, see [Expiring objects](lifecycle-expire-general-considerations.md).
+ `deletion-type` – For **Object Deleted** events, when an unversioned object is deleted, or a versioned object is permanently deleted, this is set to **Permanently Deleted**. When a delete marker is created for a versioned object, this is set to **Delete Marker Created**. For more information, see [Deleting object versions from a versioning-enabled bucket](DeletingObjectVersions.md).
**Note**  
Some object attributes (such as `etag` and `size`) are present only when a delete marker is created.
+ `restore-expiry-time` – For **Object Restore Completed** events, the time when the temporary copy of the object will be deleted from S3. For more information, see [Working with archived objects](archived-objects.md).
+ `source-storage-class` – For **Object Restore Initiated** and **Object Restore Completed** events, the storage class of the object being restored. For more information, see [Working with archived objects](archived-objects.md).
+ `destination-storage-class` – For **Object Storage Class Changed** events, the new storage class of the object. For more information, see [Transitioning objects using Amazon S3 Lifecycle](lifecycle-transition-general-considerations.md).
+ `destination-access-tier` – For **Object Access Tier Changed** events, the new access tier of the object. For more information, see [Managing storage costs with Amazon S3 Intelligent-Tiering](intelligent-tiering.md).
+ `object-annotation` – For **Object Annotation Created** and **Object Annotation Removed** events, the `detail` field includes an `object-annotation` field containing information about the annotation.
+ `has-object-annotation` – For **Object Created** events with reason `CopyObject`, the `object` block includes a `has-object-annotation` boolean field that indicates whether the copied object has annotations.