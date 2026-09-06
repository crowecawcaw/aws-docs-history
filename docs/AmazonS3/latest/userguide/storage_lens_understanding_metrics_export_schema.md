

# Understanding the Amazon S3 Storage Lens export schemas
<a name="storage_lens_understanding_metrics_export_schema"></a>

S3 Storage Lens export schemas vary depending on your export destination. Choose the appropriate schema based on whether you're exporting to S3 general purpose buckets or S3 tables.

**Topics**
+ [Export schema for S3 general purpose buckets](#storage_lens_general_purpose_bucket_schema)
+ [Export schemas for S3 tables](#storage_lens_s3_tables_schema)

## Export schema for S3 general purpose buckets
<a name="storage_lens_general_purpose_bucket_schema"></a>

The following table contains the schema of your S3 Storage Lens metrics export when exporting to S3 general purpose buckets.


| Attribute name  | Data type | Column name | Description | 
| --- | --- | --- | --- | 
|  VersionNumber  | String |  version\_number  | The version of the S3 Storage Lens metrics being used. | 
|  ConfigurationId  | String |  configuration\_id  | The  configuration\_id of your S3 Storage Lens configuration. | 
|  ReportDate  | String  |  report\_date  | The date that the metrics were tracked. | 
|  AwsAccountNumber  |  String  |  aws\_account\_number  | Your AWS account number. | 
|  AwsRegion  |  String  |  aws\_region  | The AWS Region for which the metrics are being tracked. | 
|  StorageClass  |  String  |  storage\_class  | The storage class of the bucket in question. | 
|  RecordType  |  ENUM  |  record\_type  |  The type of artifact that is being reported (ACCOUNT, BUCKET, or PREFIX).  | 
|  RecordValue  |  String  |  record\_value  | The value of the RecordType artifact.  The `record_value` is URL-encoded.   | 
|  BucketName  |  String  |  bucket\_name  | The name of the bucket that is being reported. | 
|  MetricName  |  String  |  metric\_name  | The name of the metric that is being reported. | 
|  MetricValue  |  Long  |  metric\_value  | The value of the metric that is being reported. | 

### Example of an S3 Storage Lens metrics export
<a name="storage_lens_sample_metrics_export"></a>

The following is an example of an S3 Storage Lens metrics export based on this schema. 

**Note**  
You can identify metrics for Storage Lens groups by looking for the `STORAGE_LENS_GROUP_BUCKET` or `STORAGE_LENS_GROUP_ACCOUNT` values in the `record_type` column. The `record_value` column will display the Amazon Resource Name (ARN) for the Storage Lens group, for example, `arn:aws:s3:us-east-1:123456789012:storage-lens-group/slg-1`. 

![An example S3 Storage Lens metrics export file.](http://docs.aws.amazon.com/AmazonS3/latest/userguide/images/sample_storage_lens_export.png)


The following is an example of an S3 Storage Lens metrics export with Storage Lens groups data.

![An example S3 Storage Lens metrics export file with Storage Lens groups data.](http://docs.aws.amazon.com/AmazonS3/latest/userguide/images/StorageLensGroups_metricsexport.png)


## Export schemas for S3 tables
<a name="storage_lens_s3_tables_schema"></a>

When exporting S3 Storage Lens metrics to S3 tables, the data is organized into three separate table schemas: storage metrics, bucket property metrics, and activity metrics.

**Topics**
+ [Storage metrics table schema](#storage_lens_s3_tables_storage_metrics)
+ [Bucket property metrics table schema](#storage_lens_s3_tables_bucket_property_metrics)
+ [Activity metrics table schema](#storage_lens_s3_tables_activity_metrics)

### Storage metrics table schema
<a name="storage_lens_s3_tables_storage_metrics"></a>


| Name | Type | Description | 
| --- | --- | --- | 
|  version\_number  | string | Version identifier of the schema of the table | 
|  configuration\_id  | string | S3 Storage Lens configuration name | 
|  report\_time  | timestamptz | Date the S3 Storage Lens report refers to | 
|  aws\_account\_id  | string | Account id the entry refers to | 
|  aws\_region  | string | Region | 
|  storage\_class  | string | Storage Class | 
|  record\_type  | string | Type of record, related to what is the level of aggregation of data. Values: ACCOUNT, BUCKET, PREFIX, LENS GROUP.  | 
|  record\_value  | string | Disambiguator for record types that have more than one record under them. It is used to reference the prefix | 
|  bucket\_name  | string | Bucket name | 
|  object\_count  | long | Number of objects stored for the current referenced item | 
|  storage\_bytes  | DECIMAL(38,0) | Number of bytes stored for the current referenced item | 
|  bucket\_key\_sse\_kms\_object\_count  | long | Number of objects encrypted with a customer managed key stored for the current referenced item | 
|  bucket\_key\_sse\_kms\_storage\_bytes  | DECIMAL(38,0) | Number of bytes encrypted with a customer managed key stored for the current referenced item | 
|  current\_version\_object\_count  | long | Number of current version objects stored for the current referenced item | 
|  current\_version\_storage\_bytes  | DECIMAL(38,0) | Number of current version bytes stored for the current referenced item | 
|  delete\_marker\_object\_count  | long | Number of delete marker objects stored for the current referenced item | 
|  delete\_marker\_storage\_bytes  | DECIMAL(38,0) | Number of delete marker bytes stored for the current referenced item | 
|  encrypted\_object\_count  | long | Number of encrypted objects stored for the current referenced item | 
|  encrypted\_storage\_bytes  | DECIMAL(38,0) | Number of encrypted bytes stored for the current referenced item | 
|  incomplete\_mpu\_object\_older\_than\_7\_days\_count  | long | Number of incomplete multipart upload objects older than 7 days stored for the current referenced item | 
|  incomplete\_mpu\_storage\_older\_than\_7\_days\_bytes  | DECIMAL(38,0) | Number of incomplete multipart upload bytes stored older than 7 days for the current referenced item | 
|  incomplete\_mpu\_object\_count  | long | Number of incomplete multipart upload objects stored for the current referenced item | 
|  incomplete\_mpu\_storage\_bytes  | DECIMAL(38,0) | Number of incomplete multipart upload bytes stored for the current referenced item | 
|  non\_current\_version\_object\_count  | long | Number of non-current version objects stored for the current referenced item | 
|  non\_current\_version\_storage\_bytes  | DECIMAL(38,0) | Number of non-current version bytes stored for the current referenced item | 
|  object\_lock\_enabled\_object\_count  | long | Number of objects stored for for objects with lock enabled in the current referenced item | 
|  object\_lock\_enabled\_storage\_bytes  | DECIMAL(38,0) | Number of bytes stored for objects with lock enabled in the current referenced item | 
|  replicated\_object\_count  | long | Number of objects replicated for the current referenced item | 
|  replicated\_storage\_bytes  | DECIMAL(38,0) | Number of bytes replicated for the current referenced item | 
|  replicated\_object\_source\_count  | long | Number of objects replicated as source stored for the current referenced item | 
|  replicated\_storage\_source\_bytes  | DECIMAL(38,0) | Number of bytes replicated as source for the current referenced item | 
|  sse\_kms\_object\_count  | long | Number of objects encrypted with SSE key stored for the current referenced item | 
|  sse\_kms\_storage\_bytes  | DECIMAL(38,0) | Number of bytes encrypted with SSE key stored for the current referenced item | 
|  object\_0kb\_count  | long | Number of objects with size equal to 0KB, including current version, noncurrent versions, incomplete multipart uploads, and delete markers | 
|  object\_0kb\_to\_128kb\_count  | long | Number of objects with size greater than 0KB and less than or equal to 128KB, including current version, noncurrent versions, incomplete multipart uploads, and delete markers | 
|  object\_128kb\_to\_256kb\_count  | long | Number of objects with size greater than 128KB and less than or equal to 256KB, including current version, noncurrent versions, incomplete multipart uploads, and delete markers | 
|  object\_256kb\_to\_512kb\_count  | long | Number of objects with size greater than 256KB and less than or equal to 512KB, including current version, noncurrent versions, incomplete multipart uploads, and delete markers | 
|  object\_512kb\_to\_1mb\_count  | long | Number of objects with size greater than 512KB and less than or equal to 1MB, including current version, noncurrent versions, incomplete multipart uploads, and delete markers | 
|  object\_1mb\_to\_2mb\_count  | long | Number of objects with size greater than 1MB and less than or equal to 2MB, including current version, noncurrent versions, incomplete multipart uploads, and delete markers | 
|  object\_2mb\_to\_4mb\_count  | long | Number of objects with size greater than 2MB and less than or equal to 4MB, including current version, noncurrent versions, incomplete multipart uploads, and delete markers | 
|  object\_4mb\_to\_8mb\_count  | long | Number of objects with size greater than 4MB and less than or equal to 8MB, including current version, noncurrent versions, incomplete multipart uploads, and delete markers | 
|  object\_8mb\_to\_16mb\_count  | long | Number of objects with size greater than 8MB and less than or equal to 16MB, including current version, noncurrent versions, incomplete multipart uploads, and delete markers | 
|  object\_16mb\_to\_32mb\_count  | long | Number of objects with size greater than 16MB and less than or equal to 32MB, including current version, noncurrent versions, incomplete multipart uploads, and delete markers | 
|  object\_32mb\_to\_64mb\_count  | long | Number of objects with size greater than 32MB and less than or equal to 64MB, including current version, noncurrent versions, incomplete multipart uploads, and delete markers | 
|  object\_64mb\_to\_128mb\_count  | long | Number of objects with size greater than 64MB and less than or equal to 128MB, including current version, noncurrent versions, incomplete multipart uploads, and delete markers | 
|  object\_128mb\_to\_256mb\_count  | long | Number of objects with size greater than 128MB and less than or equal to 256MB, including current version, noncurrent versions, incomplete multipart uploads, and delete markers | 
|  object\_256mb\_to\_512mb\_count  | long | Number of objects with size greater than 256MB and less than or equal to 512MB, including current version, noncurrent versions, incomplete multipart uploads, and delete markers | 
|  object\_512mb\_to\_1gb\_count  | long | Number of objects with size greater than 512MB and less than or equal to 1GB, including current version, noncurrent versions, incomplete multipart uploads, and delete markers | 
|  object\_1gb\_to\_2gb\_count  | long | Number of objects with size greater than 1GB and less than or equal to 2GB, including current version, noncurrent versions, incomplete multipart uploads, and delete markers | 
|  object\_2gb\_to\_4gb\_count  | long | Number of objects with size greater than 2GB and less than or equal to 4GB, including current version, noncurrent versions, incomplete multipart uploads, and delete markers | 
|  object\_larger\_than\_4gb\_count  | long | Number of objects with size greater than 4GB, including current version, noncurrent versions, incomplete multipart uploads, and delete markers | 

### Bucket property metrics table schema
<a name="storage_lens_s3_tables_bucket_property_metrics"></a>


| Name | Type | Description | 
| --- | --- | --- | 
|  version\_number  | string | Version identifier of the schema of the table | 
|  configuration\_id  | string | S3 Storage Lens configuration name | 
|  report\_time  | timestamptz | Date the S3 Storage Lens report refers to | 
|  aws\_account\_id  | string | Account id the entry refers to | 
|  record\_type  | string | Type of record, related to what is the level of aggregation of data. Values: ACCOUNT, BUCKET, PREFIX, LENS GROUP.  | 
|  record\_value  | string | Disambiguator for record types that have more than one record under them. It is used to reference the prefix. | 
|  aws\_region  | string | Region | 
|  storage\_class  | string | Storage Class | 
|  bucket\_name  | string | Bucket name | 
|  versioning\_enabled\_bucket\_count  | long | Number of buckets with versioning enabled for the current referenced item | 
|  mfa\_delete\_enabled\_bucket\_count  | long | Number of buckets with MFA delete enabled for the current referenced item | 
|  sse\_kms\_enabled\_bucket\_count  | long | Number of buckets with KMS enabled for the current referenced item | 
|  object\_ownership\_bucket\_owner\_enforced\_bucket\_count  | long | Number of buckets with Object Ownership bucket owner enforced for the current referenced item | 
|  object\_ownership\_bucket\_owner\_preferred\_bucket\_count  | long | Number of buckets with Object Ownership bucket owner preferred for the current referenced item | 
|  object\_ownership\_object\_writer\_bucket\_count  | long | Number of buckets with Object Ownership object writer for the current referenced item | 
|  transfer\_acceleration\_enabled\_bucket\_count  | long | Number of buckets with transfer acceleration enabled for the current referenced item | 
|  event\_notification\_enabled\_bucket\_count  | long | Number of buckets with event notification enabled for the current referenced item | 
|  transition\_lifecycle\_rule\_count  | long | Number of transition lifecycle rules for the current referenced item | 
|  expiration\_lifecycle\_rule\_count  | long | Number of expiration lifecycle rules for the current referenced item | 
|  non\_current\_version\_transition\_lifecycle\_rule\_count  | long | Number of noncurrent version transition lifecycle rules for the current referenced item | 
|  non\_current\_version\_expiration\_lifecycle\_rule\_count  | long | Number of noncurrent version expiration lifecycle rules for the current referenced item | 
|  abort\_incomplete\_multipart\_upload\_lifecycle\_rule\_count  | long | Number of abort incomplete multipart upload lifecycle rules for the current referenced item | 
|  expired\_object\_delete\_marker\_lifecycle\_rule\_count  | long | Number of expire object delete marker lifecycle rules for the current referenced item | 
|  same\_region\_replication\_rule\_count  | long | Number of Same-Region Replication rule count for the current referenced item | 
|  cross\_region\_replication\_rule\_count  | long | Number of Cross-Region Replication rule count for the current referenced item | 
|  same\_account\_replication\_rule\_count  | long | Number of Same-account replication rule count for the current referenced item | 
|  cross\_account\_replication\_rule\_count  | long | Number of Cross-account replication rule count for the current referenced item | 
|  invalid\_destination\_replication\_rule\_count  | long | Number of buckets with Invalid destination replication for the current referenced item | 

### Activity metrics table schema
<a name="storage_lens_s3_tables_activity_metrics"></a>


| Name | Type | Description | 
| --- | --- | --- | 
|  version\_number  | string | Version identifier of the schema of the table | 
|  configuration\_id  | string | S3 Storage Lens configuration name | 
|  report\_time  | timestamptz | Date the S3 Storage Lens report refers to | 
|  aws\_account\_id  | string | Account id the entry refers to | 
|  aws\_region  | string | Region | 
|  storage\_class  | string | Storage Class | 
|  record\_type  | string | Type of record, related to what is the level of aggregation of data. Values: ACCOUNT, BUCKET, PREFIX.  | 
|  record\_value  | string | Disambiguator for record types that have more than one record under them. It is used to reference the prefix | 
|  bucket\_name  | string | Bucket name | 
|  all\_request\_count  | long | Number of \_all\_ requests for the current referenced item | 
|  all\_sse\_kms\_encrypted\_request\_count  | long | Number of KMS encrypted requests for the current referenced item | 
|  all\_unsupported\_sig\_request\_count  | long | Number of unsupported sig requests for the current referenced item | 
|  all\_unsupported\_tls\_request\_count  | long | Number of unsupported TLS requests for the current referenced item | 
|  bad\_request\_error\_400\_count  | long | Number of 400 bad request errors for the current referenced item | 
|  delete\_request\_count  | long | Number of delete requests for the current referenced item | 
|  downloaded\_bytes  | decimal(0,0) | Number of downloaded bytes for the current referenced item | 
|  error\_4xx\_count  | long | Number of 4xx errors for the current referenced item | 
|  error\_5xx\_count  | long | Number of 5xx errors for the current referenced item | 
|  forbidden\_error\_403\_count  | long | Number of 403 forbidden errors for the current referenced item | 
|  get\_request\_count  | long | Number of get requests for the current referenced item | 
|  head\_request\_count  | long | Number of head requests for the current referenced item | 
|  internal\_server\_error\_500\_count  | long | Number of 500 internal server errors for the current referenced item | 
|  list\_request\_count  | long | Number of list requests for the current referenced item | 
|  not\_found\_error\_404\_count  | long | Number of 404 not found errors for the current referenced item | 
|  ok\_status\_200\_count  | long | Number of 200 OK requests for the current referenced item | 
|  partial\_content\_status\_206\_count  | long | Number of 206 partial content requests for the current referenced item | 
|  post\_request\_count  | long | Number of post requests for the current referenced item | 
|  put\_request\_count  | long | Number of put requests for the current referenced item | 
|  select\_request\_count  | long | Number of select requests for the current referenced item | 
|  select\_returned\_bytes  | decimal(0,0) | Number of bytes returned by select requests for the current referenced item | 
|  select\_scanned\_bytes  | decimal(0,0) | Number of bytes scanned by select requests for the current referenced item | 
|  service\_unavailable\_error\_503\_count  | long | Number of 503 service unavailable errors for the current referenced item | 
|  uploaded\_bytes  | decimal(0,0) | Number of uploaded bytes for the current referenced item | 
|  average\_first\_byte\_latency  | long | Average per-request time between when an S3 bucket receives a complete request and when it starts returning the response, measured over the past 24 hours | 
|  average\_total\_request\_latency  | long | Average elapsed per-request time between the first byte received and the last byte sent to an S3 bucket, measured over the past 24 hours | 
|  read\_0kb\_request\_count  | long | Number of GetObject requests with data sizes of 0KB, including both range-based requests and whole object requests | 
|  read\_0kb\_to\_128kb\_request\_count  | long | Number of GetObject requests with data sizes greater than 0KB and up to 128KB, including both range-based requests and whole object requests | 
|  read\_128kb\_to\_256kb\_request\_count  | long | Number of GetObject requests with data sizes greater than 128KB and up to 256KB, including both range-based requests and whole object requests | 
|  read\_256kb\_to\_512kb\_request\_count  | long | Number of GetObject requests with data sizes greater than 256KB and up to 512KB, including both range-based requests and whole object requests | 
|  read\_512kb\_to\_1mb\_request\_count  | long | Number of GetObject requests with data sizes greater than 512KB and up to 1MB, including both range-based requests and whole object requests | 
|  read\_1mb\_to\_2mb\_request\_count  | long | Number of GetObject requests with data sizes greater than 1MB and up to 2MB, including both range-based requests and whole object requests | 
|  read\_2mb\_to\_4mb\_request\_count  | long | Number of GetObject requests with data sizes greater than 2MB and up to 4MB, including both range-based requests and whole object requests | 
|  read\_4mb\_to\_8mb\_request\_count  | long | Number of GetObject requests with data sizes greater than 4MB and up to 8MB, including both range-based requests and whole object requests | 
|  read\_8mb\_to\_16mb\_request\_count  | long | Number of GetObject requests with data sizes greater than 8MB and up to 16MB, including both range-based requests and whole object requests | 
|  read\_16mb\_to\_32mb\_request\_count  | long | Number of GetObject requests with data sizes greater than 16MB and up to 32MB, including both range-based requests and whole object requests | 
|  read\_32mb\_to\_64mb\_request\_count  | long | Number of GetObject requests with data sizes greater than 32MB and up to 64MB, including both range-based requests and whole object requests | 
|  read\_64mb\_to\_128mb\_request\_count  | long | Number of GetObject requests with data sizes greater than 64MB and up to 128MB, including both range-based requests and whole object requests | 
|  read\_128mb\_to\_256mb\_request\_count  | long | Number of GetObject requests with data sizes greater than 128MB and up to 256MB, including both range-based requests and whole object requests | 
|  read\_256mb\_to\_512mb\_request\_count  | long | Number of GetObject requests with data sizes greater than 256MB and up to 512MB, including both range-based requests and whole object requests | 
|  read\_512mb\_to\_1gb\_request\_count  | long | Number of GetObject requests with data sizes greater than 512MB and up to 1GB, including both range-based requests and whole object requests | 
|  read\_1gb\_to\_2gb\_request\_count  | long | Number of GetObject requests with data sizes greater than 1GB and up to 2GB, including both range-based requests and whole object requests | 
|  read\_2gb\_to\_4gb\_request\_count  | long | Number of GetObject requests with data sizes greater than 2GB and up to 4GB, including both range-based requests and whole object requests | 
|  read\_larger\_than\_4gb\_request\_count  | long | Number of GetObject requests with data sizes greater than 4GB, including both range-based requests and whole object requests | 
|  write\_0kb\_request\_count  | long | Number of PutObject, UploadPart, and CreateMultipartUpload requests with data sizes of 0KB | 
|  write\_0kb\_to\_128kb\_request\_count  | long | Number of PutObject, UploadPart, and CreateMultipartUpload requests with data sizes greater than 0KB and up to 128KB | 
|  write\_128kb\_to\_256kb\_request\_count  | long | Number of PutObject, UploadPart, and CreateMultipartUpload requests with data sizes greater than 128KB and up to 256KB | 
|  write\_256kb\_to\_512kb\_request\_count  | long | Number of PutObject, UploadPart, and CreateMultipartUpload requests with data sizes greater than 256KB and up to 512KB | 
|  write\_512kb\_to\_1mb\_request\_count  | long | Number of PutObject, UploadPart, and CreateMultipartUpload requests with data sizes greater than 512KB and up to 1MB | 
|  write\_1mb\_to\_2mb\_request\_count  | long | Number of PutObject, UploadPart, and CreateMultipartUpload requests with data sizes greater than 1MB and up to 2MB | 
|  write\_2mb\_to\_4mb\_request\_count  | long | Number of PutObject, UploadPart, and CreateMultipartUpload requests with data sizes greater than 2MB and up to 4MB | 
|  write\_4mb\_to\_8mb\_request\_count  | long | Number of PutObject, UploadPart, and CreateMultipartUpload requests with data sizes greater than 4MB and up to 8MB | 
|  write\_8mb\_to\_16mb\_request\_count  | long | Number of PutObject, UploadPart, and CreateMultipartUpload requests with data sizes greater than 8MB and up to 16MB | 
|  write\_16mb\_to\_32mb\_request\_count  | long | Number of PutObject, UploadPart, and CreateMultipartUpload requests with data sizes greater than 16MB and up to 32MB | 
|  write\_32mb\_to\_64mb\_request\_count  | long | Number of PutObject, UploadPart, and CreateMultipartUpload requests with data sizes greater than 32MB and up to 64MB | 
|  write\_64mb\_to\_128mb\_request\_count  | long | Number of PutObject, UploadPart, and CreateMultipartUpload requests with data sizes greater than 64MB and up to 128MB | 
|  write\_128mb\_to\_256mb\_request\_count  | long | Number of PutObject, UploadPart, and CreateMultipartUpload requests with data sizes greater than 128MB and up to 256MB | 
|  write\_256mb\_to\_512mb\_request\_count  | long | Number of PutObject, UploadPart, and CreateMultipartUpload requests with data sizes greater than 256MB and up to 512MB | 
|  write\_512mb\_to\_1gb\_request\_count  | long | Number of PutObject, UploadPart, and CreateMultipartUpload requests with data sizes greater than 512MB and up to 1GB | 
|  write\_1gb\_to\_2gb\_request\_count  | long | Number of PutObject, UploadPart, and CreateMultipartUpload requests with data sizes greater than 1GB and up to 2GB | 
|  write\_2gb\_to\_4gb\_request\_count  | long | Number of PutObject, UploadPart, and CreateMultipartUpload requests with data sizes greater than 2GB and up to 4GB | 
|  write\_larger\_than\_4gb\_request\_count  | long | Number of PutObject, UploadPart, and CreateMultipartUpload requests with data sizes greater than 4GB | 
|  concurrent\_put\_503\_error\_count  | long | Number of 503 errors that are generated due to concurrent writes to the same object | 
|  cross\_region\_request\_count  | long | Number of requests that originate from a client in different Region than bucket's home Region | 
|  cross\_region\_transferred\_bytes  | decimal(0,0) | Number of bytes that are transferred from calls in different Region than bucket's home Region | 
|  cross\_region\_without\_replication\_request\_count  | long | Number of requests that originate from a client in different Region than bucket's home Region, excluding cross-region replication requests | 
|  cross\_region\_without\_replication\_transferred\_bytes  | decimal(0,0) | Number of bytes that are transferred from calls in different Region than bucket's home Region, excluding cross-region replication bytes | 
|  inregion\_request\_count  | long | Number of requests that originate from a client in same Region as bucket's home Region | 
|  inregion\_transferred\_bytes  | decimal(0,0) | Number of bytes that are transferred from calls from same Region as bucket's home Region | 
|  unique\_objects\_accessed\_daily\_count  | long | Number of objects that were accessed at least once in last 24 hrs | 