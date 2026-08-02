# CreateBulkImportJob for Scenario Discovery

## Prerequisites

### Source and error-report S3 buckets

You need an S3 location holding the data files to ingest, and an S3 URI
where per-file error reports are written. The source and error-report locations can share
a bucket.

### The IAM role that AWS IoT SiteWise assumes (jobRoleArn)

Pass this role to AWS IoT SiteWise through the `jobRoleArn` parameter. AWS IoT SiteWise assumes
it to read your source objects and write error reports.

Trust policy — allow `iotsitewise.amazonaws.com` to assume the role:

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Principal": { "Service": "iotsitewise.amazonaws.com" },
            "Action": "sts:AssumeRole"
        }
    ]
}
```

Permission policy — grant AWS IoT SiteWise S3 access:

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": [
                "s3:GetObject",
                "s3:ListBucket",
                "s3:PutObject",
                "s3:GetBucketLocation"
            ],
            "Resource": [
                "arn:aws:s3:::your-bucket-name",
                "arn:aws:s3:::your-bucket-name/*"
            ]
        }
    ]
}
```

### The caller's IAM role and permissions

Your calling identity (user, role, or task role) needs permission to invoke the API
and pass the role from the preceding section to AWS IoT SiteWise.

Minimal caller permission policy:

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "InvokeBulkImport",
            "Effect": "Allow",
            "Action": [
                "iotsitewise:CreateBulkImportJob",
                "iotsitewise:DescribeBulkImportJob",
                "iotsitewise:ListBulkImportJobs"
            ],
            "Resource": "*"
        },
        {
            "Sid": "PassRoleToSiteWise",
            "Effect": "Allow",
            "Action": "iam:PassRole",
            "Resource": "arn:aws:iam::123456789012:role/UATSiteWiseBulkImportRole",
            "Condition": {
                "StringEquals": {
                    "iam:PassedToService": "iotsitewise.amazonaws.com"
                }
            }
        },
        {
            "Sid": "StageSourceObjectsInS3",
            "Effect": "Allow",
            "Action": [
                "s3:GetObject",
                "s3:ListBucket",
                "s3:PutObject",
                "s3:AbortMultipartUpload"
            ],
            "Resource": [
                "arn:aws:s3:::your-bucket-name",
                "arn:aws:s3:::your-bucket-name/*"
            ]
        }
    ]
}
```

The `PassRoleToSiteWise` statement makes it safe for you to hand
`jobRoleArn` to AWS IoT SiteWise. Without `iam:PassRole` (and the
`iam:PassedToService` condition), `CreateBulkImportJob` fails with
an authorization error.

If your caller is an application role, pair the policy with this trust policy so an
EC2, ECS, or Lambda workload can assume it:

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Principal": {
                "Service": [
                    "ec2.amazonaws.com",
                    "ecs-tasks.amazonaws.com",
                    "lambda.amazonaws.com"
                ]
            },
            "Action": "sts:AssumeRole"
        }
    ]
}
```

Trim the Service list to only the workload type that actually runs your code.

## Aliases

Aliases identify the physical or logical source of data. Using them consistently
enables Scenario Discovery to correlate video, telemetry, and annotations from the same
event.

### MP4 video

Alias identifies the vehicle and camera: `/car_120/front_left_camera/`

Set through the `File.alias` request field.

### Parquet telemetry

Aliases are per-row, not per-file. Your Parquet file must contain these columns:

| Column         | Notes                                                                           |
| -------------- | ------------------------------------------------------------------------------- |
| `timestamp_ns` | Nanoseconds since Unix epoch                                                    |
| `alias`        | Property alias for this telemetry point (for example,<br>`/car_120/speed/kph/`) |
| `value`        | Scalar value, encoded as string                                                 |
| `data_type`    | One of: BOOLEAN, INTEGER, DOUBLE, TIMESTAMP, STRING                             |

Do not set `File.alias` for Parquet telemetry imports.

### Annotation (OpenLABEL subset)

Alias identifies the vehicle: `/car_120/annotations/`

Set through the `File.alias` request field.

## Request shape

### Required top-level parameters (Scenario Discovery)

| Parameter             | Type      | Notes                                                                         |
| --------------------- | --------- | ----------------------------------------------------------------------------- |
| `jobName`             | string    | 1–256 chars, unique per account/region                                        |
| `jobRoleArn`          | string    | IAM role ARN from the prerequisites section                                   |
| `files`               | list      | List of File objects (at least one)                                           |
| `errorReportLocation` | structure | Object containing `s3Uri` (string, S3 URI where error reports are<br>written) |
| `datasetId`           | string    | ID of the Scenario Discovery dataset                                          |
| `workspaceName`       | string    | Name of the Scenario Discovery workspace (1–64 chars,<br>`^[a-zA-Z0-9_-]+$`)  |

### Optional top-level parameters

| Parameter                | Type    | Notes                                                                  |
| ------------------------ | ------- | ---------------------------------------------------------------------- |
| `adaptiveIngestion`      | boolean | Must always be `false` for Scenario Discovery                          |
| `deleteFilesAfterImport` | boolean | If `true`, source S3 objects are deleted after successful<br>ingestion |

### File object

| Field       | Required                  | Notes                                                                                                        |
| ----------- | ------------------------- | ------------------------------------------------------------------------------------------------------------ |
| `bucket`    | yes                       | Source S3 bucket name (3–63 chars)                                                                           |
| `key`       | yes                       | Object key                                                                                                   |
| `versionId` | no                        | Specific S3 object version                                                                                   |
| `alias`     | required (MP4/annotation) | File-level property alias (max 2048 chars)                                                                   |
| `startTime` | required for MP4          | Anchors the file's data to wall-clock time. Uses nanos format:<br>`{"timeInSeconds": N, "offsetInNanos": N}` |

### JobConfiguration.fileFormat

Exactly one of `mp4`, `parquet`, or
`annotation`:

```
{ "fileFormat": { "mp4": {} } }
{ "fileFormat": { "parquet": {} } }
{ "fileFormat": { "annotation": {} } }
```

For mixed jobs that import multiple file types in a single request, each file object
can specify its own `fileFormat` field. When a file-level
`fileFormat` is present, it overrides the job-level
`jobConfiguration.fileFormat` for that file. This enables you to import MP4
video, Parquet telemetry, and annotation files in a single bulk import job.

### Response

```
{
    "jobId": "string",
    "jobName": "string",
    "jobStatus": "PENDING | RUNNING | COMPLETED | FAILED | COMPLETED_WITH_FAILURES"
}
```

HTTP status on success: 202 Accepted.

## Example request payloads

### MP4 video

```
{
    "jobName": "car120-front-left-camera-2026-07-14",
    "jobRoleArn": "arn:aws:iam::123456789012:role/UATSiteWiseBulkImportRole",
    "files": [
        {
            "bucket": "your-bucket-name",
            "key": "video/car_120/2026-07-14/front_left_cam_0001.mp4",
            "alias": "/car_120/front_left_camera/",
            "startTime": {"timeInSeconds": 1720958400, "offsetInNanos": 0}
        }
    ],
    "errorReportLocation": {
        "s3Uri": "s3://your-bucket-name/bulk-import-errors/car_120/2026-07-14/"
    },
    "jobConfiguration": {
        "fileFormat": { "mp4": {} }
    },
    "datasetId": "your-dataset-id",
    "workspaceName": "scenario_discovery_car120",
    "adaptiveIngestion": false,
    "deleteFilesAfterImport": false
}
```

### Parquet telemetry

```
{
    "jobName": "car120-telemetry-2026-07-14",
    "jobRoleArn": "arn:aws:iam::123456789012:role/UATSiteWiseBulkImportRole",
    "files": [
        {
            "bucket": "your-bucket-name",
            "key": "telemetry/car_120/2026-07-14/part-0000.parquet"
        },
        {
            "bucket": "your-bucket-name",
            "key": "telemetry/car_120/2026-07-14/part-0001.parquet"
        }
    ],
    "errorReportLocation": {
        "s3Uri": "s3://your-bucket-name/bulk-import-errors/car_120/2026-07-14/"
    },
    "jobConfiguration": {
        "fileFormat": { "parquet": {} }
    },
    "datasetId": "your-dataset-id",
    "workspaceName": "scenario_discovery_car120",
    "adaptiveIngestion": false,
    "deleteFilesAfterImport": false
}
```

Each row in the Parquet file contains: timestamp\_ns (nanoseconds), alias, value, and
data\_type.

### Annotation (OpenLABEL subset)

```
{
    "jobName": "car120-annotations-2026-07-14",
    "jobRoleArn": "arn:aws:iam::123456789012:role/UATSiteWiseBulkImportRole",
    "files": [
        {
            "bucket": "your-bucket-name",
            "key": "annotations/car_120/2026-07-14/labels.json",
            "alias": "/car_120/annotations/"
        }
    ],
    "errorReportLocation": {
        "s3Uri": "s3://your-bucket-name/bulk-import-errors/car_120/2026-07-14/"
    },
    "jobConfiguration": {
        "fileFormat": { "annotation": {} }
    },
    "datasetId": "your-dataset-id",
    "workspaceName": "scenario_discovery_car120",
    "adaptiveIngestion": false,
    "deleteFilesAfterImport": false
}
```

## AWS CLI — CreateBulkImportJob

Command (using an input file):

```
aws iotsitewise create-bulk-import-job \
    --region us-east-1 \
    --cli-input-json file://bulk-import-request.json
```

Equivalent inline form (MP4 example):

```
aws iotsitewise create-bulk-import-job \
    --region us-east-1 \
    --job-name car120-front-left-camera-2026-07-14 \
    --job-role-arn arn:aws:iam::123456789012:role/UATSiteWiseBulkImportRole \
    --files '[{"bucket":"your-bucket-name","key":"video/car_120/2026-07-14/front_left_cam_0001.mp4","alias":"/car_120/front_left_camera/","startTime":{"timeInSeconds":1720958400,"offsetInNanos":0}}]' \
    --error-report-location '{"s3Uri":"s3://your-bucket-name/bulk-import-errors/car_120/2026-07-14/"}' \
    --job-configuration '{"fileFormat":{"mp4":{}}}' \
    --dataset-id your-dataset-id \
    --workspace-name scenario_discovery_car120 \
    --no-adaptive-ingestion \
    --no-delete-files-after-import
```

CLI-only flags:

- `--region <name>` (or `AWS_REGION` env var) —
  required
- `--profile <name>` — selects a named profile from
  `~/.aws/config`
- `--cli-input-json file://...` — read the entire request body from a JSON
  file
- `--generate-cli-skeleton` — print a blank request template

## boto3 (Python) — CreateBulkImportJob

### Code — MP4

```
import boto3

client = boto3.client("iotsitewise", region_name="us-east-1")

response = client.create_bulk_import_job(
    jobName="car120-front-left-camera-2026-07-14",
    jobRoleArn="arn:aws:iam::123456789012:role/UATSiteWiseBulkImportRole",
    files=[
        {
            "bucket": "your-bucket-name",
            "key": "video/car_120/2026-07-14/front_left_cam_0001.mp4",
            "alias": "/car_120/front_left_camera/",
            "startTime": {"timeInSeconds": 1720958400, "offsetInNanos": 0},
        },
    ],
    errorReportLocation={
        "s3Uri": "s3://your-bucket-name/bulk-import-errors/car_120/2026-07-14/",
    },
    jobConfiguration={
        "fileFormat": {"mp4": {}},
    },
    datasetId="your-dataset-id",
    workspaceName="scenario_discovery_car120",
    adaptiveIngestion=False,
    deleteFilesAfterImport=False,
)

print(response["jobId"], response["jobStatus"])
```

### Code — Parquet telemetry

```
response = client.create_bulk_import_job(
    jobName="car120-telemetry-2026-07-14",
    jobRoleArn="arn:aws:iam::123456789012:role/UATSiteWiseBulkImportRole",
    files=[
        {"bucket": "your-bucket-name", "key": "telemetry/car_120/2026-07-14/part-0000.parquet"},
        {"bucket": "your-bucket-name", "key": "telemetry/car_120/2026-07-14/part-0001.parquet"},
    ],
    errorReportLocation={
        "s3Uri": "s3://your-bucket-name/bulk-import-errors/car_120/2026-07-14/",
    },
    jobConfiguration={"fileFormat": {"parquet": {}}},
    datasetId="your-dataset-id",
    workspaceName="scenario_discovery_car120",
    adaptiveIngestion=False,
)
```

### Code — Annotation

```
response = client.create_bulk_import_job(
    jobName="car120-annotations-2026-07-14",
    jobRoleArn="arn:aws:iam::123456789012:role/UATSiteWiseBulkImportRole",
    files=[
        {
            "bucket": "your-bucket-name",
            "key": "annotations/car_120/2026-07-14/labels.json",
            "alias": "/car_120/annotations/",
        },
    ],
    errorReportLocation={
        "s3Uri": "s3://your-bucket-name/bulk-import-errors/car_120/2026-07-14/",
    },
    jobConfiguration={"fileFormat": {"annotation": {}}},
    datasetId="your-dataset-id",
    workspaceName="scenario_discovery_car120",
    adaptiveIngestion=False,
)
```

### boto3-specific notes

- `region_name` — required, passed to `boto3.client()` or set
  through `AWS_REGION` / `AWS_DEFAULT_REGION`
- Credentials resolve through the standard boto3 chain (env vars,
  `~/.aws/credentials`, instance/task role, SSO)
- All request parameters use camelCase names matching the API model
- Wrap calls in `try / except botocore.exceptions.ClientError` to handle:
  `InvalidRequestException`, `ResourceAlreadyExistsException`,
  `ResourceNotFoundException`, `InternalFailureException`,
  `ThrottlingException`, `LimitExceededException`,
  `ConflictingOperationException`

## curl (raw HTTPS) — CreateBulkImportJob

`CreateBulkImportJob` is `POST /jobs` on the AWS IoT SiteWise data plane
endpoint. Every request must be signed with AWS Signature Version 4 (SigV4).

### Endpoint

```
https://data.iotsitewise.<region>.amazonaws.com/jobs
```

### HTTP required elements

| Element              | Value                                                   |
| -------------------- | ------------------------------------------------------- |
| Method               | POST                                                    |
| Path                 | `/jobs`                                                 |
| Host header          | `data.iotsitewise.<region>.amazonaws.com`               |
| Content-Type header  | `application/json`                                      |
| X-Amz-Date header    | ISO 8601 basic format (for example, `20260714T170000Z`) |
| X-Amz-Security-Token | Required only with temporary credentials (STS)          |
| Authorization header | SigV4 signature (service = iotsitewise)                 |
| Body                 | The JSON request payload                                |

### Recommended: awscurl

```
awscurl \
    --service iotsitewise \
    --region us-east-1 \
    -X POST \
    -H "Content-Type: application/json" \
    -d @bulk-import-request.json \
    https://data.iotsitewise.us-east-1.amazonaws.com/jobs
```

### Plain curl — pre-signed request skeleton

```
curl -v -X POST \
    "https://data.iotsitewise.us-east-1.amazonaws.com/jobs" \
    -H "Host: data.iotsitewise.us-east-1.amazonaws.com" \
    -H "Content-Type: application/json" \
    -H "X-Amz-Date: 20260714T170000Z" \
    -H "X-Amz-Security-Token: <SESSION_TOKEN_IF_TEMP_CREDS>" \
    -H "Authorization: AWS4-HMAC-SHA256 \
Credential=<ACCESS_KEY_ID>/20260714/us-east-1/iotsitewise/aws4_request, \
SignedHeaders=content-type;host;x-amz-date;x-amz-security-token, \
Signature=<COMPUTED_HEX_SIGNATURE>" \
    --data-binary @bulk-import-request.json
```

See the AWS documentation on Signing AWS API requests for the full SigV4
derivation.

## Verifying the job

```
aws iotsitewise describe-bulk-import-job \
    --region us-east-1 \
    --job-id d1e2f3a4-5678-90ab-cdef-1234567890ab
```

The `jobStatus` progresses: `PENDING` → `RUNNING` →
one of `COMPLETED`, `COMPLETED_WITH_FAILURES`, or
`FAILED`. When the terminal state is `COMPLETED_WITH_FAILURES` or
`FAILED`, inspect the error report objects at the S3 URI specified in
`errorReportLocation.s3Uri`.
