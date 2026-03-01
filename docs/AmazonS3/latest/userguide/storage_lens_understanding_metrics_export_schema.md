# Understanding the Amazon S3 Storage Lens export schemas

S3 Storage Lens export schemas vary depending on your export destination. Choose the appropriate
schema based on whether you're exporting to S3 general purpose buckets or S3 tables.

###### Topics

- [Export schema for S3 general purpose buckets](#storage_lens_general_purpose_bucket_schema "#storage_lens_general_purpose_bucket_schema")
- [Export schemas for S3 tables](#storage_lens_s3_tables_schema "#storage_lens_s3_tables_schema")

## Export schema for S3 general purpose buckets

The following table contains the schema of your S3 Storage Lens metrics export when exporting
to S3 general purpose buckets.

| Attribute name     | Data type | Column name          | Description                                                                        |
| ------------------ | --------- | -------------------- | ---------------------------------------------------------------------------------- |
| `VersionNumber`    | String    | `version_number`     | The version of the S3 Storage Lens metrics being used.                             |
| `ConfigurationId`  | String    | `configuration_id`   | The `configuration_id` of your S3 Storage Lens configuration.                      |
| `ReportDate`       | String    | `report_date`        | The date that the metrics were tracked.                                            |
| `AwsAccountNumber` | String    | `aws_account_number` | Your AWS account number.                                                           |
| `AwsRegion`        | String    | `aws_region`         | The AWS Region for which the metrics are being tracked.                            |
| `StorageClass`     | String    | `storage_class`      | The storage class of the bucket in question.                                       |
| `RecordType`       | ENUM      | `record_type`        | The type of artifact that is being reported (`ACCOUNT`,<br>`BUCKET`, or `PREFIX`). |
| `RecordValue`      | String    | `record_value`       | The value of the `RecordType` artifact. NoteThe `record_value` is URL-encoded.     |
| `BucketName`       | String    | `bucket_name`        | The name of the bucket that is being reported.                                     |
| `MetricName`       | String    | `metric_name`        | The name of the metric that is being reported.                                     |
| `MetricValue`      | Long      | `metric_value`       | The value of the metric that is being reported.                                    |

### Example of an S3 Storage Lens metrics export

The following is an example of an S3 Storage Lens metrics export based on this schema.

###### Note

You can identify metrics for Storage Lens groups by looking for the
`STORAGE_LENS_GROUP_BUCKET` or `STORAGE_LENS_GROUP_ACCOUNT`
values in the `record_type` column. The `record_value` column will
display the Amazon Resource Name (ARN) for the Storage Lens group, for example,
`arn:aws:s3:us-east-1:123456789012:storage-lens-group/slg-1`.

![An example S3 Storage Lens metrics export file.](images/sample_storage_lens_export.png)

The following is an example of an S3 Storage Lens metrics export with Storage Lens groups
data.

![An example S3 Storage Lens metrics export file with Storage Lens groups data.](images/StorageLensGroups_metricsexport.png)

## Export schemas for S3 tables

When exporting S3 Storage Lens metrics to S3 tables, the data is organized into three separate
table schemas: storage metrics, bucket property metrics, and activity metrics.

###### Topics

- [Storage metrics table schema](#storage_lens_s3_tables_storage_metrics "#storage_lens_s3_tables_storage_metrics")
- [Bucket property metrics table schema](#storage_lens_s3_tables_bucket_property_metrics "#storage_lens_s3_tables_bucket_property_metrics")
- [Activity metrics table schema](#storage_lens_s3_tables_activity_metrics "#storage_lens_s3_tables_activity_metrics")

### Storage metrics table schema

| Name                                             | Type          | Description                                                                                                                                                                          |
| ------------------------------------------------ | ------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `version_number`                                 | string        | Version identifier of the schema of the table                                                                                                                                        |
| `configuration_id`                               | string        | S3 Storage Lens configuration name                                                                                                                                                   |
| `report_time`                                    | timestamptz   | Date the S3 Storage Lens report refers to                                                                                                                                            |
| `aws_account_id`                                 | string        | Account id the entry refers to                                                                                                                                                       |
| `aws_region`                                     | string        | Region                                                                                                                                                                               |
| `storage_class`                                  | string        | Storage Class                                                                                                                                                                        |
| `record_type`                                    | string        | Type of record, `related` to what is the level of aggregation of<br>data. Values: `ACCOUNT`, `BUCKET`, `PREFIX`,<br>`LENS GROUP`.                                                    |
| `record_value`                                   | string        | Disambiguator for record types that have more than one record under them. It<br>is used to reference the prefix                                                                      |
| `bucket_name`                                    | string        | Bucket name                                                                                                                                                                          |
| `object_count`                                   | long          | Number of objects stored for the current referenced item                                                                                                                             |
| `storage_bytes`                                  | DECIMAL(38,0) | Number of bytes stored for the current referenced item                                                                                                                               |
| `bucket_key_sse_kms_object_count`                | long          | Number of objects encrypted with a customer managed key stored for the current<br>referenced item                                                                                    |
| `bucket_key_sse_kms_storage_bytes`               | DECIMAL(38,0) | Number of bytes encrypted with a customer managed key stored for the current<br>referenced item                                                                                      |
| `current_version_object_count`                   | long          | Number of current version objects stored for the current referenced<br>item                                                                                                          |
| `current_version_storage_bytes`                  | DECIMAL(38,0) | Number of current version bytes stored for the current referenced<br>item                                                                                                            |
| `delete_marker_object_count`                     | long          | Number of delete marker objects stored for the current referenced<br>item                                                                                                            |
| `delete_marker_storage_bytes`                    | DECIMAL(38,0) | Number of delete marker bytes stored for the current referenced item                                                                                                                 |
| `encrypted_object_count`                         | long          | Number of encrypted objects stored for the current referenced item                                                                                                                   |
| `encrypted_storage_bytes`                        | DECIMAL(38,0) | Number of encrypted bytes stored for the current referenced item                                                                                                                     |
| `incomplete_mpu_object_older_than_7_days_count`  | long          | Number of incomplete multipart upload objects older than 7 days stored for<br>the current referenced item                                                                            |
| `incomplete_mpu_storage_older_than_7_days_bytes` | DECIMAL(38,0) | Number of incomplete multipart upload bytes stored older than 7 days for the<br>current referenced item                                                                              |
| `incomplete_mpu_object_count`                    | long          | Number of incomplete multipart upload objects stored for the current<br>referenced item                                                                                              |
| `incomplete_mpu_storage_bytes`                   | DECIMAL(38,0) | Number of incomplete multipart upload bytes stored for the current referenced<br>item                                                                                                |
| `non_current_version_object_count`               | long          | Number of non-current version objects stored for the current referenced<br>item                                                                                                      |
| `non_current_version_storage_bytes`              | DECIMAL(38,0) | Number of non-current version bytes stored for the current referenced<br>item                                                                                                        |
| `object_lock_enabled_object_count`               | long          | Number of objects stored for for objects with lock enabled in the current<br>referenced item                                                                                         |
| `object_lock_enabled_storage_bytes`              | DECIMAL(38,0) | Number of bytes stored for objects with lock enabled in the current<br>referenced item                                                                                               |
| `replicated_object_count`                        | long          | Number of objects replicated for the current referenced item                                                                                                                         |
| `replicated_storage_bytes`                       | DECIMAL(38,0) | Number of bytes replicated for the current referenced item                                                                                                                           |
| `replicated_object_source_count`                 | long          | Number of objects replicated as source stored for the current referenced<br>item                                                                                                     |
| `replicated_storage_source_bytes`                | DECIMAL(38,0) | Number of bytes replicated as source for the current referenced item                                                                                                                 |
| `sse_kms_object_count`                           | long          | Number of objects encrypted with SSE key stored for the current referenced<br>item                                                                                                   |
| `sse_kms_storage_bytes`                          | DECIMAL(38,0) | Number of bytes encrypted with SSE key stored for the current referenced<br>item                                                                                                     |
| `object_0kb_count`                               | long          | Number of objects with sizes equal to 0KB, including current version,<br>noncurrent versions, incomplete multipart uploads, and delete markers                                       |
| `object_0kb_to_128kb_count`                      | long          | Number of objects with sizes greater than 0KB and less than equal to 128KB,<br>including current version, noncurrent versions, incomplete multipart uploads, and<br>delete markers   |
| `object_128kb_to_256kb_count`                    | long          | Number of objects with sizes greater than 128KB and less than equal to 256KB,<br>including current version, noncurrent versions, incomplete multipart uploads, and<br>delete markers |
| `object_256kb_to_512kb_count`                    | long          | Number of objects with sizes greater than 256KB and less than equal to 512KB,<br>including current version, noncurrent versions, incomplete multipart uploads, and<br>delete markers |
| `object_512kb_to_1mb_count`                      | long          | Number of objects with sizes greater than 512KB and less than equal to 1MB,<br>including current version, noncurrent versions, incomplete multipart uploads, and<br>delete markers   |
| `object_1mb_to_2mb_count`                        | long          | Number of objects with sizes greater than 1MB and less than equal to 2MB,<br>including current version, noncurrent versions, incomplete multipart uploads, and<br>delete markers     |
| `object_2mb_to_4mb_count`                        | long          | Number of objects with sizes greater than 2MB and less than equal to 4MB,<br>including current version, noncurrent versions, incomplete multipart uploads, and<br>delete markers     |
| `object_4mb_to_8mb_count`                        | long          | Number of objects with sizes greater than 4MB and less than equal to 8MB,<br>including current version, noncurrent versions, incomplete multipart uploads, and<br>delete markers     |
| `object_8mb_to_16mb_count`                       | long          | Number of objects with sizes greater than 8MB and less than equal to 16MB,<br>including current version, noncurrent versions, incomplete multipart uploads, and<br>delete markers    |
| `object_16mb_to_32mb_count`                      | long          | Number of objects with sizes greater than 16MB and less than equal to 32MB,<br>including current version, noncurrent versions, incomplete multipart uploads, and<br>delete markers   |
| `object_32mb_to_64mb_count`                      | long          | Number of objects with sizes greater than 32MB and less than equal to 64MB,<br>including current version, noncurrent versions, incomplete multipart uploads, and<br>delete markers   |
| `object_64mb_to_128mb_count`                     | long          | Number of objects with sizes greater than 64MB and less than equal to 128MB,<br>including current version, noncurrent versions, incomplete multipart uploads, and<br>delete markers  |
| `object_128mb_to_256mb_count`                    | long          | Number of objects sizes greater than 128MB and less than equal to 256MB,<br>including current version, noncurrent versions, incomplete multipart uploads, and<br>delete markers      |
| `object_256mb_to_512mb_count`                    | long          | Number of objects sizes greater than 256MB and less than equal to 512MB,<br>including current version, noncurrent versions, incomplete multipart uploads, and<br>delete markers      |
| `object_512mb_to_1gb_count`                      | long          | Number of objects sizes greater than 512MB and less than equal to 1GB,<br>including current version, noncurrent versions, incomplete multipart uploads, and<br>delete markers        |
| `object_1gb_to_2gb_count`                        | long          | Number of objects sizes greater than 1GB and less than equal to 2GB,<br>including current version, noncurrent versions, incomplete multipart uploads, and<br>delete markers          |
| `object_2gb_to_4gb_count`                        | long          | Number of objects sizes greater than 2GB and less than equal to 4GB,<br>including current version, noncurrent versions, incomplete multipart uploads, and<br>delete markers          |
| `object_larger_than_4gb_count`                   | long          | Number of objects sizes greater than 4GB, including current version,<br>noncurrent versions, incomplete multipart uploads, and delete markers                                        |

### Bucket property metrics table schema

| Name                                                     | Type        | Description                                                                                                                  |
| -------------------------------------------------------- | ----------- | ---------------------------------------------------------------------------------------------------------------------------- |
| `version_number`                                         | string      | Version identifier of the schema of the table                                                                                |
| `configuration_id`                                       | string      | S3 Storage Lens configuration name                                                                                           |
| `report_time`                                            | timestamptz | Date the S3 Storage Lens report refers to                                                                                    |
| `aws_account_id`                                         | string      | Account id the entry refers to                                                                                               |
| `record_type`                                            | string      | Type of record, related to what is the level of aggregation of data. Values:<br>`ACCOUNT`, `BUCKET`, `PREFIX`, `LENS GROUP`. |
| `record_value`                                           | string      | Disambiguator for record types that have more than one record under them. It<br>is used to reference the prefix.             |
| `aws_region`                                             | string      | Region                                                                                                                       |
| `storage_class`                                          | string      | Storage Class                                                                                                                |
| `bucket_name`                                            | string      | Bucket name                                                                                                                  |
| `versioning_enabled_bucket_count`                        | long        | Number of buckets with versioning enabled for the current referenced<br>item                                                 |
| `mfa_delete_enabled_bucket_count`                        | long        | Number of buckets with MFA delete enabled for the current referenced<br>item                                                 |
| `sse_kms_enabled_bucket_count`                           | long        | Number of buckets with KMS enabled for the current referenced item                                                           |
| `object_ownership_bucket_owner_enforced_bucket_count`    | long        | Number of buckets with Object Ownership bucket owner enforced for the current<br>referenced item                             |
| `object_ownership_bucket_owner_preferred_bucket_count`   | long        | Number of buckets with Object Ownership bucket owner preferred for the<br>current referenced item                            |
| `object_ownership_object_writer_bucket_count`            | long        | Number of buckets with Object Ownership object writer for the current<br>referenced item                                     |
| `transfer_acceleration_enabled_bucket_count`             | long        | Number of buckets with transfer acceleration enabled for the current<br>referenced item                                      |
| `event_notification_enabled_bucket_count`                | long        | Number of buckets with event notification enabled for the current referenced<br>item                                         |
| `transition_lifecycle_rule_count`                        | long        | Number of transition lifecycle rules for the current referenced item                                                         |
| `expiration_lifecycle_rule_count`                        | long        | Number of expiration lifecycle rules for the current referenced item                                                         |
| `non_current_version_transition_lifecycle_rule_count`    | long        | Number of noncurrent version transition lifecycle rules for the current<br>referenced item                                   |
| `non_current_version_expiration_lifecycle_rule_count`    | long        | Number of noncurrent version expiration lifecycle rules for the current<br>referenced item                                   |
| `abort_incomplete_multipart_upload_lifecycle_rule_count` | long        | Number of abort incomplete multipart upload lifecycle rules for the current<br>referenced item                               |
| `expired_object_delete_marker_lifecycle_rule_count`      | long        | Number of expire object delete marker lifecycle rules for the current<br>referenced item                                     |
| `same_region_replication_rule_count`                     | long        | Number of Same-Region Replication rule count for the current referenced<br>item                                              |
| `cross_region_replication_rule_count`                    | long        | Number of Cross-Region Replication rule count for the current referenced<br>item                                             |
| `same_account_replication_rule_count`                    | long        | Number of Same-account replication rule count for the current referenced<br>item                                             |
| `cross_account_replication_rule_count`                   | long        | Number of Cross-account replication rule count for the current referenced<br>item                                            |
| `invalid_destination_replication_rule_count`             | long        | Number of buckets with Invalid destination replication for the current<br>referenced item                                    |

### Activity metrics table schema

| Name                                                 | Type         | Description                                                                                                                                                     |
| ---------------------------------------------------- | ------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `version_number`                                     | string       | Version identifier of the schema of the table                                                                                                                   |
| `configuration_id`                                   | string       | S3 Storage Lens configuration name                                                                                                                              |
| `report_time`                                        | timestamptz  | Date the S3 Storage Lens report refers to                                                                                                                       |
| `aws_account_id`                                     | string       | Account id the entry refers to                                                                                                                                  |
| `aws_region`                                         | string       | Region                                                                                                                                                          |
| `storage_class`                                      | string       | Storage Class                                                                                                                                                   |
| `record_type`                                        | string       | Type of record, related to what is the level of aggregation of data. Values:<br>`ACCOUNT`, `BUCKET`, `PREFIX`.                                                  |
| `record_value`                                       | string       | Disambiguator for record types that have more than one record under them. It<br>is used to reference the prefix                                                 |
| `bucket_name`                                        | string       | Bucket name                                                                                                                                                     |
| `all_request_count`                                  | long         | Number of \_all\_ requests for the current referenced item                                                                                                      |
| `all_sse_kms_encrypted_request_count`                | long         | Number of KMS encrypted requests for the current referenced item                                                                                                |
| `all_unsupported_sig_request_count`                  | long         | Number of unsupported sig requests for the current referenced item                                                                                              |
| `all_unsupported_tls_request_count`                  | long         | Number of unsupported TLS requests for the current referenced item                                                                                              |
| `bad_request_error_400_count`                        | long         | Number of 400 bad request errors for the current referenced item                                                                                                |
| `delete_request_count`                               | long         | Number of delete requests for the current referenced item                                                                                                       |
| `downloaded_bytes`                                   | decimal(0,0) | Number of downloaded bytes for the current referenced item                                                                                                      |
| `error_4xx_count`                                    | long         | Number of 4xx errors for the current referenced item                                                                                                            |
| `error_5xx_count`                                    | long         | Number of 5xx errors for the current referenced item                                                                                                            |
| `forbidden_error_403_count`                          | long         | Number of 403 forbidden errors for the current referenced item                                                                                                  |
| `get_request_count`                                  | long         | Number of get requests for the current referenced item                                                                                                          |
| `head_request_count`                                 | long         | Number of head requests for the current referenced item                                                                                                         |
| `internal_server_error_500_count`                    | long         | Number of 500 internal server errors for the current referenced item                                                                                            |
| `list_request_count`                                 | long         | Number of list requests for the current referenced item                                                                                                         |
| `not_found_error_404_count`                          | long         | Number of 404 not found errors for the current referenced item                                                                                                  |
| `ok_status_200_count`                                | long         | Number of 200 OK requests for the current referenced item                                                                                                       |
| `partial_content_status_206_count`                   | long         | Number of 206 partial content requests for the current referenced<br>item                                                                                       |
| `post_request_count`                                 | long         | Number of post requests for the current referenced item                                                                                                         |
| `put_request_count`                                  | long         | Number of put requests for the current referenced item                                                                                                          |
| `select_request_count`                               | long         | Number of select requests for the current referenced item                                                                                                       |
| `select_returned_bytes`                              | decimal(0,0) | Number of bytes returned by select requests for the current referenced<br>item                                                                                  |
| `select_scanned_bytes`                               | decimal(0,0) | Number of bytes scanned by select requests for the current referenced<br>item                                                                                   |
| `service_unavailable_error_503_count`                | long         | Number of 503 service unavailable errors for the current referenced<br>item                                                                                     |
| `uploaded_bytes`                                     | decimal(0,0) | Number of uploaded bytes for the current referenced item                                                                                                        |
| `average_first_byte_latency`                         | long         | Average per-request time between when an S3 bucket receives a complete<br>request and when it starts returning the response, measured over the past 24<br>hours |
| `average_total_request_latency`                      | long         | Average elapsed per-request time between the first byte received and the last<br>byte sent to an S3 bucket, measured over the past 24 hours                     |
| `read_0kb_request_count`                             | long         | Number of GetObject requests with data sizes of 0KB, including both range-based<br>requests and whole object requests                                           |
| `read_0kb_to_128kb_request_count`                    | long         | Number of GetObject requests with data sizes greater than 0KB and up to 128KB,<br>including both range-based requests and whole object requests                 |
| `read_128kb_to_256kb_request_count`                  | long         | Number of GetObject requests with data sizes greater than 128KB and up to<br>256KB, including both range-based requests and whole object requests               |
| `read_256kb_to_512kb_request_count`                  | long         | Number of GetObject requests with data sizes greater than 256KB and up to<br>512KB, including both range-based requests and whole object requests               |
| `read_512kb_to_1mb_request_count`                    | long         | Number of GetObject requests with data sizes greater than 512KB and up to 1MB,<br>including both range-based requests and whole object requests                 |
| `read_1mb_to_2mb_request_count`                      | long         | Number of GetObject requests with data sizes greater than 1MB and up to 2MB,<br>including both range-based requests and whole object requests                   |
| `read_2mb_to_4mb_request_count`                      | long         | Number of GetObject requests with data sizes greater than 2MB and up to 4MB,<br>including both range-based requests and whole object requests                   |
| `read_4mb_to_8mb_request_count`                      | long         | Number of GetObject requests with data sizes greater than 4MB and up to 8MB,<br>including both range-based requests and whole object requests                   |
| `read_8mb_to_16mb_request_count`                     | long         | Number of GetObject requests with data sizes greater than 8MB and up to 16MB,<br>including both range-based requests and whole object requests                  |
| `read_16mb_to_32mb_request_count`                    | long         | Number of GetObject requests with data sizes greater than 16MB and up to 32MB,<br>including both range-based requests and whole object requests                 |
| `read_32mb_to_64mb_request_count`                    | long         | Number of GetObject requests with data sizes greater than 32MB and up to 64MB,<br>including both range-based requests and whole object requests                 |
| `read_64mb_to_128mb_request_count`                   | long         | Number of GetObject requests with data sizes greater than 64MB and up to<br>128MB, including both range-based requests and whole object requests                |
| `read_128mb_to_256mb_request_count`                  | long         | Number of GetObject requests with data sizes greater than 128MB and up to<br>256MB, including both range-based requests and whole object requests               |
| `read_256mb_to_512mb_request_count`                  | long         | Number of GetObject requests with data sizes greater than 256MB and up to<br>512MB, including both range-based requests and whole object requests               |
| `read_512mb_to_1gb_request_count`                    | long         | Number of GetObject requests with data sizes greater than 512MB and up to 1GB,<br>including both range-based requests and whole object requests                 |
| `read_1gb_to_2gb_request_count`                      | long         | Number of GetObject requests with data sizes greater than 1GB and up to 2GB,<br>including both range-based requests and whole object requests                   |
| `read_2gb_to_4gb_request_count`                      | long         | Number of GetObject requests with data sizes greater than 2GB and up to 4GB,<br>including both range-based requests and whole object requests                   |
| `read_larger_than_4gb_request_count`                 | long         | Number of GetObject requests with data sizes greater than 4GB, including both<br>range-based requests and whole object requests                                 |
| `write_0kb_request_count`                            | long         | Number of PutObject, UploadPart, and CreateMultipartUpload requests with data<br>sizes of 0KB                                                                   |
| `write_0kb_to_128kb_request_count`                   | long         | Number of PutObject, UploadPart, and CreateMultipartUpload requests with data<br>sizes greater than 0KB and up to 128KB                                         |
| `write_128kb_to_256kb_request_count`                 | long         | Number of PutObject, UploadPart, and CreateMultipartUpload requests with data<br>sizes greater than 128KB and up to 256KB                                       |
| `write_256kb_to_512kb_request_count`                 | long         | Number of PutObject, UploadPart, and CreateMultipartUpload requests with data<br>sizes greater than 256KB and up to 512KB                                       |
| `write_512kb_to_1mb_request_count`                   | long         | Number of PutObject, UploadPart, and CreateMultipartUpload requests with data<br>sizes greater than 512KB and up to 1MB                                         |
| `write_1mb_to_2mb_request_count`                     | long         | Number of PutObject, UploadPart, and CreateMultipartUpload requests with data<br>sizes greater than 1MB and up to 2MB                                           |
| `write_2mb_to_4mb_request_count`                     | long         | Number of PutObject, UploadPart, and CreateMultipartUpload requests with data<br>sizes greater than 2MB and up to 4MB                                           |
| `write_4mb_to_8mb_request_count`                     | long         | Number of PutObject, UploadPart, and CreateMultipartUpload requests with data<br>sizes greater than 4MB and up to 8MB                                           |
| `write_8mb_to_16mb_request_count`                    | long         | Number of PutObject, UploadPart, and CreateMultipartUpload requests with data<br>sizes greater than 8MB and up to 16MB                                          |
| `write_16mb_to_32mb_request_count`                   | long         | Number of PutObject, UploadPart, and CreateMultipartUpload requests with data<br>sizes greater than 16MB and up to 32MB                                         |
| `write_32mb_to_64mb_request_count`                   | long         | Number of PutObject, UploadPart, and CreateMultipartUpload requests with data<br>sizes greater than 32MB and up to 64MB                                         |
| `write_64mb_to_128mb_request_count`                  | long         | Number of PutObject, UploadPart, and CreateMultipartUpload requests with data<br>sizes greater than 64MB and up to 128MB                                        |
| `write_128mb_to_256mb_request_count`                 | long         | Number of PutObject, UploadPart, and CreateMultipartUpload requests with data<br>sizes greater than 128MB and up to 256MB                                       |
| `write_256mb_to_512mb_request_count`                 | long         | Number of PutObject, UploadPart, and CreateMultipartUpload requests with data<br>sizes greater than 256MB and up to 512MB                                       |
| `write_512mb_to_1gb_request_count`                   | long         | Number of PutObject, UploadPart, and CreateMultipartUpload requests with data<br>sizes greater than 512MB and up to 1GB                                         |
| `write_1gb_to_2gb_request_count`                     | long         | Number of PutObject, UploadPart, and CreateMultipartUpload requests with data<br>sizes greater than 1GB and up to 2GB                                           |
| `write_2gb_to_4gb_request_count`                     | long         | Number of PutObject, UploadPart, and CreateMultipartUpload requests with data<br>sizes greater than 2GB and up to 4GB                                           |
| `write_larger_than_4gb_request_count`                | long         | Number of PutObject, UploadPart, and CreateMultipartUpload requests with data<br>sizes greater than 4GB                                                         |
| `concurrent_put_503_error_count`                     | long         | Number of 503 errors that are generated due to concurrent writes to the same<br>object                                                                          |
| `cross_region_request_count`                         | long         | Number of requests that originate from a client in different Region than<br>bucket's home Region                                                                |
| `cross_region_transferred_bytes`                     | decimal(0,0) | Number of bytes that are transferred from calls in different Region than<br>bucket's home Region                                                                |
| `cross_region_without_replication_request_count`     | long         | Number of requests that originate from a client in different Region than<br>bucket's home Region, excluding cross-region replication requests                   |
| `cross_region_without_replication_transferred_bytes` | decimal(0,0) | Number of bytes that are transferred from calls in different Region than<br>bucket's home Region, excluding cross-region replication bytes                      |
| `inregion_request_count`                             | long         | Number of requests that originate from a client in same Region as bucket's<br>home Region                                                                       |
| `inregion_transferred_bytes`                         | decimal(0,0) | Number of bytes that are transferred from calls from same Region as bucket's<br>home Region                                                                     |
| `unique_objects_accessed_daily_count`                | long         | Number of objects that were accessed at least once in last 24 hrs                                                                                               |
