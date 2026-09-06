

# CreateEnrichmentJob for Scenario Discovery
<a name="sd-enrichment"></a>

## Prerequisites
<a name="sd-enrichment-prereqs"></a>

### A Scenario Discovery workspace and dataset containing video data
<a name="sd-enrichment-workspace-dataset"></a>

`CreateEnrichmentJob` operates on an existing workspace \+ dataset. Before you can call it:
+ The workspace must exist and be in ACTIVE state (not being deleted).
+ The dataset must exist inside that workspace and must contain the MP4 video time-series data to be analyzed. Use `CreateBulkImportJob` to ingest video data into a dataset if you haven't already.
+ If two requests share the same job type, workspace, property, and dataset but specify different time ranges, the system accepts both requests.

Your calling identity needs permission to invoke the enrichment-job APIs, read the target workspace/dataset/time-series resources, and (when the workspace uses a customer managed KMS key) decrypt with that key.

Minimal caller permission policy:

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "InvokeEnrichmentJob",
            "Effect": "Allow",
            "Action": [
                "iotsitewise:CreateEnrichmentJob",
                "iotsitewise:DescribeEnrichmentJob",
                "iotsitewise:CancelEnrichmentJob",
                "iotsitewise:ListEnrichmentJobs"
            ],
            "Resource": "*"
        },
        {
            "Sid": "ReadWorkspaceAndDataset",
            "Effect": "Allow",
            "Action": [
                "iotsitewise:DescribeWorkspace",
                "iotsitewise:DescribeDataset",
                "iotsitewise:ListDatasetDataSegments",
                "iotsitewise:ListTimeSeries",
                "iotsitewise:DescribeTimeSeries"
            ],
            "Resource": "*"
        },
        {
            "Sid": "DecryptWorkspaceCMK",
            "Effect": "Allow",
            "Action": [
                "kms:Decrypt",
                "kms:DescribeKey"
            ],
            "Resource": "arn:aws:kms:us-east-1:123456789012:key/00000000-0000-0000-0000-000000000000",
            "Condition": {
                "StringEquals": {
                    "kms:ViaService": "iotsitewise.us-east-1.amazonaws.com"
                }
            }
        }
    ]
}
```

Notes:
+ Omit or narrow `DecryptWorkspaceCMK` when the workspace uses the default AWS managed key. Include it (with the correct key ARN) when the workspace was created with a customer managed KMS key.
+ The service itself performs the video processing — you do not pass a service role (there is no `jobRoleArn`-style parameter). You only grant the caller enough permission to submit and track the job.
+ `AccessDeniedException` from the API almost always indicates missing AWS IoT SiteWise or KMS permissions on the caller identity.

If your caller is an application role, pair the policy with a trust policy for the workload type that runs the code:

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
<a name="sd-enrichment-aliases"></a>

Enrichment is scoped to a single video time series within the dataset. You identify that time series either by its system-assigned `timeSeriesId` or by its `propertyAlias`. Aliases are strongly preferred because they're readable, stable, and consistent with the alias conventions used during bulk import.

For a vehicle-mounted camera, the alias follows the same structure used for MP4 imports:

```
/car_120/front_left_camera/
```

Specify exactly one of `propertyAlias` or `timeSeriesId` in the request — never both. The API returns `ValidationException` if both are supplied.

## Request shape
<a name="sd-enrichment-request-shape"></a>

### Required top-level parameters
<a name="sd-enrichment-required-params"></a>


| Parameter | Type | Notes | 
| --- | --- | --- | 
| workspaceName | string | Name of the Scenario Discovery workspace (1–64 chars, ^[a-zA-Z0-9\_-]\+$). Sent as a URI path parameter, not in the JSON body. | 
| jobConfiguration | structure | Configuration union. Currently must contain exactly one member: eventDetection. | 

### Optional top-level parameters
<a name="sd-enrichment-optional-params"></a>


| Parameter | Type | Notes | 
| --- | --- | --- | 
| clientToken | string | 36–64 chars, no whitespace. Idempotency token — resubmitting the same request with the same token returns the original job without creating a duplicate. Use a UUID. | 

### EnrichmentJobConfiguration (union — exactly one member)
<a name="sd-enrichment-event-detection"></a>

Currently the only supported member is `eventDetection`.

EventDetection fields:


| Field | Required | Notes | 
| --- | --- | --- | 
| datasetId | yes | ID of the Scenario Discovery dataset containing the video time series | 
| timeSeriesId | one of timeSeriesId/alias | System-generated identifier for the video time series. 36–73 chars. | 
| propertyAlias | one of timeSeriesId/alias | Human-readable alias for the video time series (max 2048 chars). Preferred. | 
| trimSettings | yes | { startTime, endTime } — bounds the time window to process. Both bounds must lie within the dataset's actual time bounds. | 

### EnrichmentTrimSettings
<a name="sd-enrichment-trim-settings"></a>

Both `startTime` and `endTime` are TimeInNanos structures:

```
{
    "timeInSeconds": <Unix epoch seconds>,
    "offsetInNanos": <optional 0..999999999>
}
```

`endTime` must be strictly greater than `startTime`, and both must fall within the dataset's data range.

**Note**  
Only data segments FULLY encapsulated within this time range are enriched. Partial enrichment of data segments is not supported.

Python helper to compute the seconds/nanos split:

```
import datetime

def as_time_in_nanos(dt: datetime.datetime) -> dict:
    ts_ns = int(dt.timestamp() * 1_000_000_000)
    return {
        "timeInSeconds": ts_ns // 1_000_000_000,
        "offsetInNanos": ts_ns % 1_000_000_000
    }
```

### Response
<a name="sd-enrichment-response"></a>

```
{
    "jobId": "string",
    "status": "PENDING | RUNNING | COMPLETED | FAILED | TIMED_OUT | CANCELLED",
    "createdAt": "2026-07-14T17:00:00Z"
}
```

HTTP status on success: 200 OK. (Unlike `CreateBulkImportJob` which returns 202, `CreateEnrichmentJob` returns 200.)

### Errors
<a name="sd-enrichment-errors"></a>


| Error | Meaning | 
| --- | --- | 
| ValidationException | Invalid parameters (for example, both timeSeriesId and propertyAlias specified, endTime <= startTime) | 
| AccessDeniedException | Missing AWS IoT SiteWise or KMS permissions on the caller | 
| ConflictException | A duplicate job (same workspace/dataset/property/type) is already running | 
| ResourceNotFoundException | Workspace, dataset, or time series does not exist | 
| ThrottlingException | Request rate exceeded | 
| LimitExceededException | Too many concurrent jobs | 
| InternalServerException | Service-side failure | 

## Example request payload
<a name="sd-enrichment-example-payload"></a>

Save this as `enrichment-job-request.json`. The `workspaceName` is passed on the URL path (or through a CLI flag), not in the JSON body.

```
{
    "jobConfiguration": {
        "eventDetection": {
            "datasetId": "9005f70f-ebb6-4380-b0f8-6ed83ddbea6a",
            "propertyAlias": "/camera/front",
            "trimSettings": {
                "startTime": {
                    "timeInSeconds": 1778275007,
                    "offsetInNanos": 0
                },
                "endTime": {
                    "timeInSeconds": 1778275307,
                    "offsetInNanos": 0
                }
            }
        }
    },
    "clientToken": "c9c1d2b8-2f4b-4d6a-9b83-8b8a9b9d9a0a"
}
```

Notes:
+ 1778275007 and 1778275307 represent a 5-minute analysis window.
+ `clientToken` is optional but recommended. If your caller retries, use the same token to avoid creating a duplicate job.
+ Only data segments fully contained within the `trimSettings` time range are enriched. Segments overlapping the start or end boundary but not fully within it are ignored.

## AWS CLI
<a name="sd-enrichment-cli"></a>

Command (using an input file):

```
aws iotsitewise create-enrichment-job \
    --region us-east-1 \
    --workspace-name scenario_discovery_car120 \
    --cli-input-json file://enrichment-job-request.json
```

Equivalent inline form:

```
aws iotsitewise create-enrichment-job \
    --region us-east-1 \
    --workspace-name ws-1778278606 \
    --job-configuration '{
      "eventDetection": {
        "datasetId": "9005f70f-ebb6-4380-b0f8-6ed83ddbea6a",
        "propertyAlias": "/camera/front",
        "trimSettings": {
          "startTime": {
            "timeInSeconds": 1778275007
          },
          "endTime": {
            "timeInSeconds": 1778275307
          }
        }
      }
    }'
```

CLI-only flags:
+ `--region <name>` (or `AWS_REGION` env var) — required
+ `--profile <name>` — selects a named profile from `~/.aws/config`
+ `--cli-input-json file://...` — read the request body from a JSON file
+ `--generate-cli-skeleton` — print a blank request template

Sample output:

```
{
    "jobId": "9a8b7c6d-5e4f-3a2b-1c0d-e1f2a3b4c5d6",
    "status": "PENDING",
    "createdAt": "2026-07-14T17:00:00Z"
}
```

## boto3 (Python)
<a name="sd-enrichment-boto3"></a>

```
import uuid
import boto3

client = boto3.client("iotsitewise", region_name="us-east-1")

response = client.create_enrichment_job(
    workspaceName="ws-1778278606",
    jobConfiguration={
        "eventDetection": {
            "datasetId": "9005f70f-ebb6-4380-b0f8-6ed83ddbea6a",
            "propertyAlias": "/camera/front",
            "trimSettings": {
                "startTime": {"timeInSeconds": 1778275007, "offsetInNanos": 0},
                "endTime":   {"timeInSeconds": 1778275307, "offsetInNanos": 0},
            },
        },
    },
    clientToken=str(uuid.uuid4()),
)

print(response["jobId"], response["status"], response["createdAt"])
```

boto3-specific notes:
+ `region_name` — required, passed to `boto3.client()` or set through `AWS_REGION` / `AWS_DEFAULT_REGION`
+ Credentials resolve through the standard boto3 chain (env vars, `~/.aws/credentials`, instance/task role, SSO)
+ All request parameters use camelCase names matching the API model. `workspaceName` is passed as a kwarg; boto3 places it on the URL path for you.
+ Wrap calls in `try / except botocore.exceptions.ClientError` to handle: `ValidationException`, `AccessDeniedException`, `ConflictException`, `ResourceNotFoundException`, `ThrottlingException`, `LimitExceededException`, `InternalServerException`

## curl (raw HTTPS)
<a name="sd-enrichment-curl"></a>

`CreateEnrichmentJob` is `POST /workspaces/{workspaceName}/enrichment-jobs` on the AWS IoT SiteWise data plane endpoint. Every request must be signed with AWS Signature Version 4 (SigV4).

### Endpoint
<a name="sd-enrichment-curl-endpoint"></a>

```
https://data.iotsitewise.<region>.amazonaws.com/workspaces/<workspaceName>/enrichment-jobs
```

### HTTP required elements
<a name="sd-enrichment-curl-http"></a>


| Element | Value | 
| --- | --- | 
| Method | POST | 
| Path | /workspaces/<workspaceName>/enrichment-jobs | 
| Host header | data.iotsitewise.<region>.amazonaws.com | 
| Content-Type header | application/json | 
| X-Amz-Date header | ISO 8601 basic format (for example, 20260714T170000Z) | 
| X-Amz-Security-Token | Required only with temporary credentials (STS) | 
| Authorization header | SigV4 signature (service = iotsitewise) | 
| Body | The JSON request payload | 

### Recommended: awscurl
<a name="sd-enrichment-curl-awscurl"></a>

```
awscurl \
    --service iotsitewise \
    --region us-east-1 \
    -X POST \
    -H "Content-Type: application/json" \
    -d @enrichment-job-request.json \
    https://data.iotsitewise.us-east-1.amazonaws.com/workspaces/scenario_discovery_car120/enrichment-jobs
```

### Plain curl — pre-signed request skeleton
<a name="sd-enrichment-curl-plain"></a>

```
curl -v -X POST \
    "https://data.iotsitewise.us-east-1.amazonaws.com/workspaces/scenario_discovery_car120/enrichment-jobs" \
    -H "Host: data.iotsitewise.us-east-1.amazonaws.com" \
    -H "Content-Type: application/json" \
    -H "X-Amz-Date: 20260714T170000Z" \
    -H "X-Amz-Security-Token: <SESSION_TOKEN_IF_TEMP_CREDS>" \
    -H "Authorization: AWS4-HMAC-SHA256 \
Credential=<ACCESS_KEY_ID>/20260714/us-east-1/iotsitewise/aws4_request, \
SignedHeaders=content-type;host;x-amz-date;x-amz-security-token, \
Signature=<COMPUTED_HEX_SIGNATURE>" \
    --data-binary @enrichment-job-request.json
```

See the AWS documentation on Signing AWS API requests for the full SigV4 derivation.

Sample HTTP response:

```
HTTP/1.1 200 OK
Content-Type: application/json

{
    "jobId": "9a8b7c6d-5e4f-3a2b-1c0d-e1f2a3b4c5d6",
    "status": "PENDING",
    "createdAt": "2026-07-14T17:00:00Z"
}
```

## Verifying the job
<a name="sd-enrichment-verify"></a>

```
aws iotsitewise describe-enrichment-job \
    --region us-east-1 \
    --workspace-name scenario_discovery_car120 \
    --job-id 9a8b7c6d-5e4f-3a2b-1c0d-e1f2a3b4c5d6
```

The status progresses: `PENDING` → `RUNNING` → one of `COMPLETED`, `FAILED`, `TIMED_OUT`, or `CANCELLED`.
+ `COMPLETED` — embeddings are available and the video can be searched through Scenario Discovery's semantic search.
+ `FAILED` — inspect the `failureMessage` field in the `DescribeEnrichmentJob` response for details.

### Cancelling a running job
<a name="sd-enrichment-cancel"></a>

```
aws iotsitewise cancel-enrichment-job \
    --region us-east-1 \
    --workspace-name scenario_discovery_car120 \
    --job-id 9a8b7c6d-5e4f-3a2b-1c0d-e1f2a3b4c5d6
```

`CancelEnrichmentJob` is idempotent — calling it more than once for the same `jobId` returns the current status without error, as long as the job is not already in a non-CANCELLED terminal state (`COMPLETED`, `FAILED`, `TIMED_OUT`), in which case it returns `ConflictException`. Cancelling a RUNNING enrichment job might fail with an exception if data ingestion into the storage service has already begun.