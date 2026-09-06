

# CreateDatasetExportJob for Scenario Discovery
<a name="sd-export-job"></a>

## Prerequisites
<a name="sd-export-job-prereqs"></a>

### Destination S3 bucket with service access
<a name="sd-export-job-bucket-policy"></a>

Before you can export data, you must attach a bucket policy to your destination S3 bucket that allows the AWS IoT SiteWise service to write objects. Apply the following policy to your bucket (replace `{yourbucketname}` with your actual bucket name):

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "AllowServiceToWriteObjects",
            "Effect": "Allow",
            "Principal": {
                "Service": "iotsitewise.amazonaws.com"
            },
            "Action": "s3:*",
            "Resource": "arn:aws:s3:::{yourbucketname}/*"
        }
    ]
}
```

**Note**  
For production environments, consider narrowing the Action to only the S3 operations the service requires (for example, `s3:PutObject`, `s3:GetBucketLocation`) rather than using `s3:*`.

### The caller's IAM permissions
<a name="sd-export-job-caller-permissions"></a>

Your calling identity must have permission to invoke and describe the export job API. At minimum:

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "InvokeDatasetExportJob",
            "Effect": "Allow",
            "Action": [
                "iotsitewise:CreateDatasetExportJob",
                "iotsitewise:DescribeDatasetExportJob"
            ],
            "Resource": "*"
        }
    ]
}
```

## Request shape
<a name="sd-export-job-request-shape"></a>

### Endpoint
<a name="sd-export-job-endpoint"></a>

```
POST /workspaces/{workspaceName}/dataset-export-jobs HTTP/1.1
```

### URI parameters
<a name="sd-export-job-uri-params"></a>


| Parameter | Type | Constraints | Required | 
| --- | --- | --- | --- | 
| workspaceName | string | 1–64 chars, pattern: ^[a-zA-Z0-9\_-]\+$ | Yes | 

### Request body
<a name="sd-export-job-request-body"></a>


| Parameter | Type | Constraints | Required | Notes | 
| --- | --- | --- | --- | --- | 
| destinationS3Uri | string | Pattern: s3://[a-z0-9][a-z0-9.-]{1,61}[a-z0-9]/.\+ | Yes | Full S3 URI where exported data is written | 
| input | ProcessingInput (union) | Exactly one member specified | Yes | Input source for processing — specify exactly one option | 
| errorReportLocation | Object | Must contain s3Uri (string, S3 URI) | Yes | Amazon S3 URI where error reports are written | 
| clientToken | string | 36–64 chars, no whitespace | No | Idempotency token. Resubmitting the same request with the same token returns the original job without creating a duplicate. | 
| processingInput.trimSettings | Object | — | No | Configuration for trimming exported data segments. Controls start and end boundaries of exported content. | 
| processingInput.formatSettings | Object | — | No | Configuration for the output format of exported data. Specifies file format preferences and encoding options. | 

### Response
<a name="sd-export-job-response"></a>

```
{
    "jobId": "string",
    "workspaceName": "string"
}
```

HTTP status on success: 200 OK.


| Field | Type | Constraints | 
| --- | --- | --- | 
| jobId | string | Fixed length of 36 chars, pattern: [0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12} | 
| workspaceName | string | 1–64 chars, pattern: ^[a-zA-Z0-9\_-]\+$ | 

## Example request payload
<a name="sd-export-job-example"></a>

Save this as `export-job-request.json`:

```
{
    "destinationS3Uri": "s3://your-export-bucket/scenario-discovery/exports/car_120/2026-07-14/",
    "input": {
        "datasetId": "your-dataset-id"
    },
    "errorReportLocation": {
        "s3Uri": "s3://my-bucket/export-errors/"
    }
}
```

## AWS CLI
<a name="sd-export-job-cli"></a>

Command (using an input file):

```
aws iotsitewise create-dataset-export-job \
    --region us-east-1 \
    --workspace-name scenario_discovery_car120 \
    --cli-input-json file://export-job-request.json
```

Equivalent inline form:

```
aws iotsitewise create-dataset-export-job \
    --region us-east-1 \
    --workspace-name scenario_discovery_car120 \
    --destination-s3-uri "s3://your-export-bucket/scenario-discovery/exports/car_120/2026-07-14/" \
    --input '{"datasetId":"your-dataset-id"}' \
    --error-report-location '{"s3Uri":"s3://my-bucket/export-errors/"}'
```

CLI-only flags:
+ `--region <name>` (or `AWS_REGION` env var) — required
+ `--profile <name>` — selects a named profile from `~/.aws/config`
+ `--cli-input-json file://...` — read the request body from a JSON file
+ `--generate-cli-skeleton` — print a blank request template

Sample output:

```
{
    "jobId": "a1b2c3d4-5678-90ab-cdef-1234567890ab",
    "workspaceName": "scenario_discovery_car120"
}
```

## boto3 (Python)
<a name="sd-export-job-boto3"></a>

```
import boto3

client = boto3.client("iotsitewise", region_name="us-east-1")

response = client.create_dataset_export_job(
    workspaceName="scenario_discovery_car120",
    destinationS3Uri="s3://your-export-bucket/scenario-discovery/exports/car_120/2026-07-14/",
    input={
        "datasetId": "your-dataset-id"
    },
    errorReportLocation={
        "s3Uri": "s3://my-bucket/export-errors/"
    },
)

print(response["jobId"], response["workspaceName"])
```

boto3-specific notes:
+ `region_name` — required, passed to `boto3.client()` or set through `AWS_REGION` / `AWS_DEFAULT_REGION`
+ Credentials resolve through the standard boto3 chain (env vars, `~/.aws/credentials`, instance/task role, SSO)
+ All request parameters use camelCase names matching the API model. `workspaceName` is passed as a kwarg; boto3 places it on the URL path for you.
+ Wrap calls in `try / except botocore.exceptions.ClientError` to handle potential errors.

## curl (raw HTTPS)
<a name="sd-export-job-curl"></a>

`CreateDatasetExportJob` is `POST /workspaces/{workspaceName}/dataset-export-jobs` on the AWS IoT SiteWise data plane endpoint. Every request must be signed with AWS Signature Version 4 (SigV4).

### Endpoint
<a name="sd-export-job-curl-endpoint"></a>

```
https://data.iotsitewise.<region>.amazonaws.com/workspaces/<workspaceName>/dataset-export-jobs
```

### HTTP required elements
<a name="sd-export-job-curl-http"></a>


| Element | Value | 
| --- | --- | 
| Method | POST | 
| Path | /workspaces/<workspaceName>/dataset-export-jobs | 
| Host header | data.iotsitewise.<region>.amazonaws.com | 
| Content-Type header | application/json | 
| X-Amz-Date header | ISO 8601 basic format (for example, 20260714T170000Z) | 
| X-Amz-Security-Token | Required only with temporary credentials (STS) | 
| Authorization header | SigV4 signature (service = iotsitewise) | 
| Body | The JSON request payload | 

### Recommended: awscurl
<a name="sd-export-job-curl-awscurl"></a>

```
awscurl \
    --service iotsitewise \
    --region us-east-1 \
    -X POST \
    -H "Content-Type: application/json" \
    -d @export-job-request.json \
    https://data.iotsitewise.us-east-1.amazonaws.com/workspaces/scenario_discovery_car120/dataset-export-jobs
```

### Plain curl — pre-signed request skeleton
<a name="sd-export-job-curl-plain"></a>

```
curl -v -X POST \
    "https://data.iotsitewise.us-east-1.amazonaws.com/workspaces/scenario_discovery_car120/dataset-export-jobs" \
    -H "Host: data.iotsitewise.us-east-1.amazonaws.com" \
    -H "Content-Type: application/json" \
    -H "X-Amz-Date: 20260714T170000Z" \
    -H "X-Amz-Security-Token: <SESSION_TOKEN_IF_TEMP_CREDS>" \
    -H "Authorization: AWS4-HMAC-SHA256 \
Credential=<ACCESS_KEY_ID>/20260714/us-east-1/iotsitewise/aws4_request, \
SignedHeaders=content-type;host;x-amz-date;x-amz-security-token, \
Signature=<COMPUTED_HEX_SIGNATURE>" \
    --data-binary @export-job-request.json
```

See the AWS documentation on Signing AWS API requests for the full SigV4 derivation.

Sample HTTP response:

```
HTTP/1.1 200 OK
Content-Type: application/json

{
    "jobId": "a1b2c3d4-5678-90ab-cdef-1234567890ab",
    "workspaceName": "scenario_discovery_car120"
}
```

## S3 bucket policy reference
<a name="sd-export-job-bucket-policy-ref"></a>

You must apply this bucket policy to your destination bucket before calling `CreateDatasetExportJob`. Without it, the service cannot write exported data to your bucket.

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "AllowServiceToWriteObjects",
            "Effect": "Allow",
            "Principal": {
                "Service": "iotsitewise.amazonaws.com"
            },
            "Action": "s3:*",
            "Resource": "arn:aws:s3:::{yourbucketname}/*"
        }
    ]
}
```

Replace `{yourbucketname}` with your actual S3 bucket name.