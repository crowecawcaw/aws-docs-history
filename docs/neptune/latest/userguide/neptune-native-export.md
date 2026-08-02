# Native export for RDF data

The Neptune export API enables you to export data from your Neptune database to Amazon S3. You can export RDF data in N-Triples or N-Quads format.

## How native export works

Native export runs on the writer instance of your Neptune cluster and
writes exported data to Amazon S3 using multipart uploads. Because export uses
the writer instance's compute resources, we strongly recommend running
exports against a cloned cluster to avoid impacting production workloads.
See [Recommendations](#neptune-native-export-recommendations "#neptune-native-export-recommendations")
for more information.

### Export throughput

Export throughput scales approximately linearly with instance size up to
`r7i.16xlarge`. As a conservative planning estimate, expect
approximately **50,000 statements per second per
vCPU**.

Use this formula to estimate export duration:

```
export_seconds = total_statements / (vCPUs × 50,000)
```

Actual throughput depends on dataset characteristics including
predicate cardinality, statement complexity, and cluster size.

## Prerequisites

Before using the export API, you must:

- Have a Neptune database cluster running version 1.4.6.0 or later (version 1.4.8.0 or later for `exportFilter` support)
- [Create an IAM role with permissions to access your S3 bucket](#neptune-native-export-iam-s3 "#neptune-native-export-iam-s3")
- [Associate the IAM role with your Neptune cluster](bulk-load-tutorial-IAM-add-role-cluster.md "bulk-load-tutorial-IAM-add-role-cluster.md")
- [Configure an S3 VPC endpoint in your Neptune cluster's VPC](bulk-load-tutorial-vpc.md "bulk-load-tutorial-vpc.md")

## Recommendations

[We strongly recommend running export operation on a cloned cluster without any read/write workloads to avoid impact on production performance.](manage-console-cloning.md "manage-console-cloning.md")

For optimal price-to-performance ratio, we recommend using **16xlarge** instances for export operations. This instance type provides:

- Sufficient memory to handle large datasets without performance degradation
- Optimal CPU resources for concurrent export processing
- Best cost efficiency for export workloads

## IAM permissions

The export feature involves two separate IAM roles:

- **Caller's IAM role** – The IAM
  principal (user or role) that sends requests to the export API endpoint. This role
  needs Neptune data-access permissions.
- **S3 access IAM role** – The role
  that Neptune assumes to write exported data to Amazon S3. You pass this role's ARN
  in the `iamRoleArn` parameter of the export request, and it must be
  associated with your Neptune cluster.

### Caller permissions (Neptune data-access actions)

The IAM principal calling the export API must have the following Neptune
data-access actions in its IAM policy:

```
`{
 "Version": "2012-10-17",
 "Statement": [
 {
 "Sid": "AllowNeptuneExportActions",
 "Effect": "Allow",
 "Action": [
 "neptune-db:StartExportJob",
 "neptune-db:GetExportJobStatus",
 "neptune-db:ListExportJobs",
 "neptune-db:CancelExportJob"
 ],
 "Resource": "arn:aws:neptune-db:us-east-1:123456789012:`cluster-resource-id`/*"
 }
 ]
}`
```

For more information, see [Using IAM data-access policy statements](iam-dp-actions.md "iam-dp-actions.md").

### S3 access role permissions

The IAM role passed in the `iamRoleArn` request parameter must be
associated with your Neptune cluster and must grant Neptune permission to write
to the target S3 bucket. For steps on creating an IAM role and associating it with
your cluster, see
[Create
an IAM role to allow Neptune to access Amazon S3](bulk-load-tutorial-IAM-CreateRole.md "bulk-load-tutorial-IAM-CreateRole.md").

###### Note

The export API requires _write_ permissions to S3,
unlike the bulk loader which only requires read access. Use the following permissions policy
instead of the `AmazonS3ReadOnlyAccess` managed policy described on that page.

Attach the following permissions policy to the S3 access role:

```
`{
 "Version": "2012-10-17",
 "Statement": [
 {
 "Sid": "AllowS3WriteForNeptuneExport",
 "Effect": "Allow",
 "Action": [
 "s3:ListBucket",
 "s3:GetObject",
 "s3:PutObject",
 "s3:AbortMultipartUpload",
 "s3:GetBucketPublicAccessBlock"
 ],
 "Resource": [
 "arn:aws:s3:::amzn-s3-demo-bucket",
 "arn:aws:s3:::amzn-s3-demo-bucket/*"
 ]
 }
 ]
}`
```

### Optional KMS permissions

If you specify a `kmsKeyIdentifier` in the export request, add the
following permissions to the S3 access role:

```
`{
 "Version": "2012-10-17",
 "Statement": [
 {
 "Sid": "AllowKMSForNeptuneExport",
 "Effect": "Allow",
 "Action": [
 "kms:Decrypt",
 "kms:Encrypt",
 "kms:GenerateDataKey"
 ],
 "Resource": "arn:aws:kms:us-east-1:123456789012:key/`key-id`"
 }
 ]
}`
```

## Export endpoint

To export data, you send HTTP requests to the `https://your-neptune-endpoint:port/export` endpoint.

## Export request syntax

```
POST https://your-neptune-endpoint:port/export
```

### Request headers

- `Content-Type: application/json`

### Request body

```
{
  "destination": "string",
  "format": "string",
  "iamRoleArn": "string",
  "region": "string",
  "compression": "string",
  "kmsKeyIdentifier": "string",
  "exportFilter": {
    "namedGraphUris": ["string"]
  }
}
```

### Request parameters

**destination** (string)
Required. The S3 URI where the exported data will be stored. Must be in the format `s3://bucket-name/optional-prefix/`.

**format** (string)

Required. The format for the exported data. Valid values:

- `ntriples` – Export data in N-Triples format
- `nquads` – Export data in N-Quads format

**iamRoleArn** (string)
Required. The Amazon Resource Name (ARN) of the IAM role that Neptune assumes to access the S3 bucket.

**region** (string)
Required. The AWS Region of the S3 bucket. Must be the same region as your Neptune cluster.

**compression** (string)

Optional. Format of compression for exported files. Valid values:

- `gz` - Compress files in .gz format

**kmsKeyIdentifier** (string)
Optional. The ARN of the AWS KMS key to use for encrypting the exported data.

**exportFilter** (object)
Optional. Filters to selectively export a subset of RDF data.
Available in engine version 1.4.8.0 and later.

**namedGraphUris** (array of strings)
Named graph URIs to export (maximum 100). Only data in the specified graphs is exported. If a specified graph is empty, the export succeeds with an empty result. Invalid URIs fail with `InvalidParameterException`.

### Response syntax

```
{
  "status": "string",
  "payload": {
    "exportId": "string"
  }
}
```

**status** (string)
The HTTP status of the request.

**exportId** (string)
A unique identifier for the export task.

## Export status endpoint

To check the status of an export task, you send an HTTP GET request to the export endpoint with the export ID.

```
GET https://your-neptune-endpoint:port/export?exportId=export-id
```

### Request parameters

**exportId** (string)
Required. The unique identifier of the export task.

### Response syntax

```
{
  "status": "string",
  "payload": {
    "exportId": "string",
    "destination": "string",
    "status": "string",
    "statusReason": "string",
    "format": "string",
    "iamRoleArn": "string",
    "kmsKeyIdentifier": "string",
    "exportFilter": {
      "namedGraphUris": ["string"]
    },
    "exportTaskDetails": {
      "timeElapsedSeconds": number,
      "startTime": number,
      "numRecordsWritten": number,
      "progressPercentage": number
    }
  }
}
```

**exportId** (string)
The unique identifier of the export task.

**destination** (string)
The S3 URI where the data is being exported.

**status** (string)

The current status of the export task. Valid values:

- `EXPORT_NOT_STARTED` – Export has been queued but not started
- `EXPORT_IN_PROGRESS` – Export is currently running
- `EXPORT_COMPLETED` – Export completed successfully
- `EXPORT_CANCELLING` – Export is being cancelled
- `EXPORT_CANCELLED_BY_USER` – Export was cancelled by user
- `EXPORT_S3_ERROR` – Export failed due to S3 access error
- `EXPORT_FAILED` – Export failed due to other error

**statusReason** (string)
Additional information about the export status.

**format** (string)
The format of the exported data.

**iamRoleArn** (string)
The ARN of the IAM role used for S3 access.

**kmsKeyIdentifier** (string)
The ARN of the KMS key used for encryption, if specified.

**exportFilter** (object)
The export filter that was applied, if one was specified in the request.

- **namedGraphUris** (array of strings) – The named graph URIs used to filter the export.

**exportTaskDetails** (object)

Details about the export task progress:

- **timeElapsedSeconds** (number) – Time elapsed since export started
- **startTime** (number) – Epoch time when export started
- **numRecordsWritten** (number) – Number of records written to S3
- **progressPercentage** (number) – Percentage of export completed

## List exports endpoint

To list all export tasks, you send an HTTP GET request to the export endpoint.

```
GET https://your-neptune-endpoint:port/export
```

### Response syntax

```
{
  "status": "string",
  "payload": [
    "string"
  ]
}
```

**payload** (array)
An array of export IDs for all export tasks.

## Cancel export endpoint

To cancel an export task, you send an HTTP DELETE request to the export endpoint with the export ID.

```
DELETE https://your-neptune-endpoint:port/export?exportId=export-id
```

### Request parameters

**exportId** (string)
Required. The unique identifier of the export task to cancel.

### Response syntax

```
{
  "status": "string",
  "payload": {
    "message": "string"
  }
}
```

## Export output format

### S3 directory structure

Exported data is organized in your S3 bucket as follows:

```
s3://your-bucket/export-id/
├── data/
│   ├── part-00000.nt
│   ├── part-00001.nt
│   └── ...
└── export_status.json
```

**data/** directory
Contains the exported graph data files in the specified format.

**export\_status.json** file
Contains metadata about the export operation.

## Error responses

### Common error codes

**BadRequestException**
The request contains invalid parameters or an export is already in progress.

**AccessDeniedException**
The IAM role lacks required permissions for S3 or KMS access.

### Example error response

```
{
  "code": "BadRequestException",
  "requestId": "request-id",
  "message": "Export already in progress with ID 'existing-id'. Please wait or cancel it first.",
  "detailedMessage": "Detailed error description"
}
```

## Examples

### Start an export

```
curl -X POST https://your-cluster-endpoint:8182/export \
  -H "Content-Type: application/json" \
  -d '{
    "destination": "s3://my-bucket/exports/",
    "format": "ntriples",
    "iamRoleArn": "arn:aws:iam::123456789012:role/neptune-export-role",
    "region": "us-west-2"
  }'
```

### Start a filtered export (named graphs)

```
curl -X POST https://your-cluster-endpoint:8182/export \
  -H "Content-Type: application/json" \
  -d '{
    "destination": "s3://my-bucket/exports/",
    "format": "nquads",
    "iamRoleArn": "arn:aws:iam::123456789012:role/neptune-export-role",
    "region": "us-west-2",
    "exportFilter": {
      "namedGraphUris": [
        "http://example.com/graph1",
        "http://example.com/graph2"
      ]
    }
  }'
```

### Check export status

```
curl -X GET "https://your-cluster-endpoint:8182/export?exportId=<id>"
```

### Cancel an export

```
curl -X DELETE "https://your-cluster-endpoint:8182/export?exportId=<id>"
```

## Limitations

Native export has the following limitations:

- **Instance support** –
  Native export is not supported on Neptune Serverless instances or on
  read replicas. Export always runs on the writer instance of a
  provisioned cluster.
- **One export per cluster**
  – Only one export can be active on a cluster at a time. If you
  submit a new export request while another export is in progress, the
  request fails.
- **No auto-resume** –
  If the engine restarts during an export, the export fails and must be
  restarted from the beginning. Export progress is not preserved across
  engine restarts.
- **Status availability after engine
  events** – If the engine crashes, you can't retrieve
  the export status through the status API.
- **Consistency during writes**
  – If your cluster is servicing write traffic during an export,
  the exported data may reflect a partial or inconsistent view of the
  graph. To guarantee a consistent export, run the export against a
  cloned cluster.
