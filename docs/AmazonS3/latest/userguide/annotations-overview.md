

# Annotating your objects
<a name="annotations-overview"></a>

Use annotations to attach named data payloads to your Amazon S3 objects. Each annotation is a custom metadata payload between 1 byte and 1 MiB in size that you can create, retrieve, list, and delete without modifying the object itself.

You can associate up to 1,000 annotations with an object version. Each annotation has a unique name and can store structured data such as AI-generated labels, document context, processing results, or compliance records.

Common use cases include storing machine learning inference results, AI-generated embeddings, content moderation labels, document classification output, data lineage and audit trails, compliance labels such as PII flags or retention policies, medical imaging metadata, digital asset rights information, and ETL pipeline status alongside the source object.

You manage annotations using dedicated API operations, so you don't need to re-upload the object to add or update metadata.

You can enable an annotation table as part of your S3 Metadata configuration to query annotation data at scale using Athena and other analytics services. S3 Metadata stores annotation data in fully managed Apache Iceberg tables that Amazon S3 automatically keeps up to date. For more information, see [Discovering your data with S3 Metadata tables](metadata-tables-overview.md).

Annotations are available in all commercial AWS Regions and China Regions (Beijing and Ningxia). Annotations are not available in the Middle East (UAE) and Middle East (Bahrain) Regions. S3 Metadata annotation tables are available in all Regions where S3 Metadata is available.

## When to use annotations vs. object tags
<a name="annotations-vs-tags"></a>

Use the following comparison to determine whether annotations or object tags are the best fit for your use case.


| Characteristic | Object tags | Annotations | 
| --- | --- | --- | 
| Maximum per object | 10 per object version | 1,000 per object version | 
| Maximum size | 128 chars (key) \+ 256 chars (value) | 512 bytes (name) \+ 1 MiB (payload) | 
| Data format | Key-value string pairs | Any UTF-8 text (JSON, XML, YAML, etc.) | 
| Mutability | Yes (PutObjectTagging) | Yes (PutObjectAnnotation) | 
| Set during upload | Yes (PutObject, POST) | No (PutObjectAnnotation only, after upload) | 

Choose annotations when you need to store structured data (such as JSON or XML), payloads larger than 256 characters, or more than 10 metadata entries per object. Choose object tags when you need IAM policy integration, Amazon S3 Lifecycle rule filtering, or cost allocation reporting.

## API operations for annotations
<a name="annotations-api-operations"></a>

Amazon S3 supports the following API operations for working with annotations:
+ **PutObjectAnnotation** – Creates or overwrites an annotation on an object. You specify the annotation name and payload in the request.
+ **GetObjectAnnotation** – Returns the payload of a specific annotation by name.
+ **ListObjectAnnotations** – Returns the list of annotations on an object. The response includes each annotation's name, size, ETag, and last modified date.
+ **DeleteObjectAnnotation** – Removes a specific annotation by name.

Amazon S3 also supports annotations in the following API operations:
+ **CopyObject** – Copies annotations from the source object by default. You can specify the `x-amz-annotation-directive` header to control whether annotations are copied (`COPY`) or excluded (`EXCLUDE`).
+ **UpdateBucketMetadataAnnotationTableConfiguration** – Enables or disables the annotation table in your S3 Metadata configuration.
+ **CreateBucketMetadataConfiguration** – Accepts a new `AnnotationTableConfiguration` parameter to enable annotation tables when you create an S3 Metadata configuration.
+ **GetBucketMetadataConfiguration** – Returns `AnnotationTableConfigurationResult` in the response, which indicates the current status of the annotation table.

## Annotation limits
<a name="annotations-limits"></a>

Each object version supports up to 1,000 annotations. Annotations that are associated with an object version must have unique annotation names. The following limits apply:
+ An annotation name can be up to 512 bytes in length (UTF-8), subject to the naming rules below.
+ An annotation payload must be between 1 byte and 1 MiB in size.
+ The total annotation storage per object can be up to 1 GiB (1,000 annotations at 1 MiB each).
+ Supported checksum algorithms: CRC32, CRC32C, CRC64NVME, SHA1, SHA256, SHA512, XXHASH64, XXHASH3, XXHASH128.

## Annotation naming rules
<a name="annotations-naming-rules"></a>

Annotation names must meet the following requirements:
+ Must be between 1 and 512 bytes in length.
+ Can contain only the following characters: letters (any language), digits (0-9), underscore (`_`), period (`.`), and hyphen (`-`).
+ Cannot start with `aws` or `s3` (case-insensitive). For example, `aws`, `AWS`, `s3`, and `S3` are all reserved prefixes.
+ Must not be empty or consist only of whitespace.

## Encryption
<a name="annotations-encryption"></a>

Annotations are automatically encrypted at rest using the same encryption configuration as the parent object. The encryption type is inherited from the parent object, not the bucket default.
+ **SSE-S3** – If the parent object uses server-side encryption with Amazon S3 managed keys (SSE-S3), annotations are encrypted with SSE-S3. If the parent object has no server-side encryption configured, annotations are encrypted with SSE-S3 by default.
+ **SSE-KMS** – If the parent object uses server-side encryption with AWS KMS keys (SSE-KMS), annotations are encrypted with the same KMS key. This applies to both customer managed keys and AWS managed keys. S3 Bucket Keys are supported.
+ **DSSE-KMS** – If the parent object uses dual-layer server-side encryption with AWS KMS keys (DSSE-KMS), annotations are encrypted with DSSE-KMS using the same key.
+ **SSE-C** – Server-side encryption with customer-provided keys (SSE-C) is not supported for annotations. If you attempt to add an annotation to an object encrypted with SSE-C, Amazon S3 returns an error.

## Checksums
<a name="annotations-checksums"></a>

When you upload an annotation using `PutObjectAnnotation`, you can provide a checksum to verify data integrity. The checksum algorithm for an annotation is independent from the parent object's checksum algorithm.

When you copy an object using `CopyObject`, Amazon S3 preserves the annotation checksum values from the source. If you specify a different checksum algorithm in the copy request, the new algorithm applies to both the object and its annotations.

Supported algorithms: CRC32, CRC32C, CRC64NVME, SHA1, SHA256, SHA512, XXHASH64, XXHASH3, XXHASH128.

If the annotation doesn't have a specified checksum algorithm or checksum value, Amazon S3 uses the CRC-64/NVME algorithm to calculate the checksum value for the annotation.

## Versioning behavior
<a name="annotations-versioning"></a>

Annotations are attached to a specific object version.

Annotations of one object version are independent of annotations on other versions of the same object. Creating a new version does not copy annotations from the previous version. Deleting or adding an annotation on one version does not affect annotations on other versions. Overwriting an object replaces its annotations with whatever annotations the new version has (if none, effectively deletes them).

Adding, updating, or removing an annotation does not modify the parent object's ETag.

In a non-versioned bucket, if you delete or overwrite the object, the annotations are deleted with it.

In a versioned bucket, the following behavior applies:
+ A simple DELETE request (without specifying a version ID) creates a delete marker but preserves annotations on the underlying version.
+ Deleting a specific version ID deletes that version and all associated annotations.
+ Annotations are not independently versioned. When you overwrite an annotation with the same name, Amazon S3 replaces the previous value without creating a new object version.

**Important**  
Annotation deletion is permanent and irreversible, even in a versioned bucket. Unlike objects in versioned buckets, annotations do not have delete markers or version history. Once you delete an annotation, it cannot be recovered.

## Copy behavior and consistency
<a name="annotations-copy-behavior"></a>

When you copy an object using the `CopyObject` API (for objects smaller than 5 GiB), Amazon S3 copies annotations along with the object in a single operation.

When you copy objects using multipart upload (for example, when the AWS CLI or AWS SDKs use Transfer Manager for objects larger than approximately 8 MB), annotations are not copied by default. To include annotations, specify `--copy-props all` in the AWS CLI or the equivalent SDK configuration. With this opt-in, the SDK reads source annotations, completes the multipart upload, and then writes each annotation to the destination. Between the upload completion and the last annotation write, the destination object exists without all its annotations.

## Considerations
<a name="annotations-considerations"></a>
+ You cannot add annotations as part of a `PutObject` or multipart upload request. To add annotations to an object, call `PutObjectAnnotation` after the object is uploaded. To copy an existing object with its annotations to a new location, use `CopyObject` with the default annotation directive.
+ To add or update annotations across many objects in bulk, use Batch Operations to invoke an Lambda function that calls `PutObjectAnnotation` on each object. For more information, see [Invoke AWS Lambda function](batch-ops-invoke-lambda.md).
+ Annotations are not supported by the following features: S3 Inventory Reports, API Gateway, S3 Storage Lens, Amazon S3 File Gateway, Amazon FSx, S3 on Outposts, S3 Express One Zone (directory buckets), and Amazon S3 Files.
+ To ensure you are writing annotations to the current version of an object and not one that has been overwritten, use the `x-amz-object-if-match` conditional header with `PutObjectAnnotation` or `DeleteObjectAnnotation`. This header validates the parent object's ETag to confirm the object has not been overwritten since the caller last read it. Adding tags or annotations does not change the ETag.
+ You cannot add an annotation conditionally on the presence or absence of another annotation. The `x-amz-object-if-match` header validates the parent object's ETag only, not annotation state.
+ Annotation payloads must be valid UTF-8 encoded text. To store binary data, encode the data with Base64 before writing the annotation.
+ You can call annotation API operations (`PutObjectAnnotation`, `GetObjectAnnotation`, `ListObjectAnnotations`, `DeleteObjectAnnotation`) on objects in any storage class, including S3 Glacier and S3 Glacier Deep Archive, without restoring the object first.

## Additional configurations
<a name="annotations-additional-configurations"></a>

This section explains how annotations relate to other configurations.

### Replication
<a name="annotations-replication"></a>

If you have S3 Replication configured on your bucket, Amazon S3 replicates annotations automatically. Each annotation replicates independently. For more information, see [What does Amazon S3 replicate?](replication-what-is-isnot-replicated.md).

To replicate annotations, add `s3:GetObjectVersionAnnotationForReplication` to the source bucket permissions in your replication IAM role. For more information, see [Setting up permissions for live replication](setting-repl-config-perm-overview.md).

To prevent annotation replication while allowing object replication, add a deny statement for `s3:ReplicateObjectAnnotation` in the replication role policy. Object replication continues to succeed; only annotation replication is blocked.

### Event notifications
<a name="annotations-event-notifications"></a>

Amazon S3 can send event notifications when annotations are created, updated, or deleted. You can configure the following event types:
+ `s3:ObjectAnnotation:Put` – Sent when an annotation is created or updated.
+ `s3:ObjectAnnotation:Delete` – Sent when an annotation is deleted.

For more information, see [Event notification types and destinations](notification-how-to-event-types-and-destinations.md).