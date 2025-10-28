# Understanding archive retrieval options

The following are the available retrieval options when restoring an archived object in
Amazon S3:

- **Expedited** – Quickly access your data
  that is stored in the S3 Glacier Flexible Retrieval storage class or
  S3 Intelligent-Tiering Archive Access tier. You can use this option when occasional urgent
  requests for a subset of archives are required. For all but the largest archived
  objects (250 MB+), data that is accessed by using expedited retrievals is
  typically made available within 1–5 minutes.

###### Note

Expedited retrievals are a premium feature and are charged at the
Expedited request and retrieval rate.

For information about Amazon S3 pricing, see [Amazon S3 Pricing](https://aws.amazon.com/s3/pricing/ "https://aws.amazon.com/s3/pricing/").

Provisioned capacity helps ensure that retrieval capacity for expedited
retrievals from S3 Glacier Flexible Retrieval is available when you need it. For
more information, see [Provisioned capacity](#restoring-objects-expedited-capacity "#restoring-objects-expedited-capacity").

- **Standard** – Access any of your archived
  objects within several hours. Standard is the default option for retrieval
  requests that do not specify the retrieval option. Standard retrievals typically
  finish within 3–5 hours for objects stored in the S3 Glacier Flexible Retrieval
  storage class or S3 Intelligent-Tiering Archive Access tier. These retrievals typically finish
  within 12 hours for objects stored in the S3 Glacier Deep Archive
  storage class or S3 Intelligent-Tiering Deep Archive Access tier. Standard retrievals are free for
  objects that are stored in S3 Intelligent-Tiering.

###### Note

    + For objects stored in the S3 Glacier Flexible Retrieval storage class or the
     S3 Intelligent-Tiering Archive Access tier, Standard retrievals initiated by using the
     S3 Batch Operations restore operation typically start within minutes and finish
     within 3-5 hours.
    + For objects in the S3 Glacier Deep Archive storage class or the
     S3 Intelligent-Tiering Deep Archive Access tier, Standard retrievals initiated by using the
     Batch Operations restore operation typically start within 9 hours and finish
     within 12 hours.

- **Bulk** – Access your data by using the
  lowest-cost retrieval option in S3 Glacier storage classes. With Bulk retrievals, you can retrieve
  large amounts, even petabytes, of data inexpensively.

For objects that are stored in the S3 Glacier Flexible Retrieval storage class or
the S3 Intelligent-Tiering Archive Access tier, Bulk retrievals typically finish within 5–12
hours. For objects stored in the S3 Glacier Deep Archive storage class
or the S3 Intelligent-Tiering Deep Archive Access tier, these retrievals typically finish within 48
hours.

Bulk retrievals are free for objects that are stored in the
S3 Glacier Flexible Retrieval or S3 Intelligent-Tiering storage classes.
The following table summarizes the archive retrieval options. For information about
pricing, see [Amazon S3 pricing](https://aws.amazon.com/s3/pricing/ "https://aws.amazon.com/s3/pricing/").

| Storage class or tier                                                  | Expedited     | Standard (with Batch Operations) | Standard (without Batch Operations) | Bulk            |
| ---------------------------------------------------------------------- | ------------- | -------------------------------- | ----------------------------------- | --------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| S3 Glacier Flexible Retrieval or S3 Intelligent-Tiering Archive Access | 1–5 minutes   | Minutes–5 hours                  | 3–5 hours                           | 5–12 hours      |
| S3 Glacier Deep Archive or S3 Intelligent-Tiering Deep Archive Access  | Not available | 9-12 hours                       | Within 12 hours                     | Within 48 hours | To make an `Expedited`, `Standard`, or `Bulk` retrieval, set the `Tier` request element in the [RestoreObject](../API/RESTObjectPOSTrestore.md "../API/RESTObjectPOSTrestore.md") REST API operation request to the option that you want, or the equivalent in the AWS Command Line Interface (AWS CLI) or AWS SDKs. If you purchased provisioned capacity, all Expedited retrievals are automatically served through your provisioned capacity. ## Provisioned capacity Provisioned capacity helps ensure that your retrieval capacity for Expedited retrievals from S3 Glacier Flexible Retrieval is available when you need it. Each unit of capacity provides that at least three Expedited retrievals can be performed every 5 minutes, and it provides up to 150 megabytes per second (MBps) of retrieval throughput. If your workload requires highly reliable and predictable access to a subset of your data in minutes, consider purchasing provisioned retrieval capacity. Without provisioned capacity, Expedited retrievals might not be accepted during periods of high demand. If you require access to Expedited retrievals under all circumstances, we recommend that you purchase provisioned retrieval capacity. Provisioned capacity units are allocated to an AWS account. Thus, the requester of the Expedited data retrieval should purchase the provisioned capacity unit, not the bucket owner. You can purchase provisioned capacity by using the Amazon S3 console, the Amazon Glacier console, the [Purchase Provisioned Capacity](../../../amazonglacier/latest/dev/api-PurchaseProvisionedCapacity.md "../../../amazonglacier/latest/dev/api-PurchaseProvisionedCapacity.md") REST API operation, the AWS SDKs, or the AWS CLI. For provisioned capacity pricing information, see [Amazon S3 pricing](https://aws.amazon.com/s3/pricing/ "https://aws.amazon.com/s3/pricing/"). ## S3 Glacier restore initiation request rates When you initiate restore requests for objects that are stored in the S3 Glacier Flexible Retrieval or S3 Glacier Deep Archive storage class, a retrieval-requests quota is applied for your AWS account. S3 Glacier supports restore requests at a rate of 1,000 transactions per second. If this rate is exceeded otherwise valid requests are throttled or rejected and Amazon S3 returns a `ThrottlingException` error. Optionally, you can also use S3 Batch Operations to retrieve a large number of objects stored in S3 Glacier Flexible Retrieval or S3 Glacier Deep Archive with a single request. For more information, see [Performing object operations in bulk with Batch Operations](batch-ops.md "batch-ops.md"). |
