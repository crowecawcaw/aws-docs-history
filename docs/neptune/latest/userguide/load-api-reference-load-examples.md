

# Neptune Loader Examples

 This example demonstrates how to use the Neptune loader to load data into a Neptune graph database using the Gremlin CSV format. The request is sent as an HTTP POST request to the Neptune loader endpoint, and the request body contains the necessary parameters to specify the data source, format, IAM role, and other configuration options. The response includes the load ID, which can be used to track the progress of the data loading process. 

 You must provide the `source`, `format`, `iamRoleArn`, and `region` fields. All other request fields are optional. For a full description of each field, see [Neptune Loader Request Parameters](load-api-reference-load.md#load-api-reference-load-parameters). 

**Example Request**  
The following is a request sent via HTTP POST using the `curl` command. It loads a file in the Neptune CSV format. For more information, see [Gremlin load data format](bulk-load-tutorial-format-gremlin.md).  

```
aws neptunedata start-loader-job \
  --endpoint-url https://{{your-neptune-endpoint}}:{{port}} \
  --source "s3://{{bucket-name}}/{{object-key-name}}" \
  --format "csv" \
  --iam-role-arn "{{ARN for the IAM role you are using}}" \
  --s3-bucket-region "{{region}}" \
  --no-fail-on-error \
  --parallelism "MEDIUM" \
  --no-update-single-cardinality-properties \
  --no-queue-request
```
For more information, see [start-loader-job](https://docs.aws.amazon.com/cli/latest/reference/neptunedata/start-loader-job.html) in the AWS CLI Command Reference.

```python
import boto3
from botocore.config import Config

client = boto3.client(
    'neptunedata',
    endpoint_url='https://{{your-neptune-endpoint}}:{{port}}',
    config=Config(read_timeout=None, retries={'total_max_attempts': 1})
)

response = client.start_loader_job(
    source='s3://{{bucket-name}}/{{object-key-name}}',
    format='csv',
    iamRoleArn='{{ARN for the IAM role you are using}}',
    s3BucketRegion='{{region}}',
    failOnError=False,
    parallelism='MEDIUM',
    updateSingleCardinalityProperties=False,
    queueRequest=False
)

print(response)
```

```
awscurl https://{{your-neptune-endpoint}}:{{port}}/loader \
  --region {{us-east-1}} \
  --service neptune-db \
  -X POST \
  -H 'Content-Type: application/json' \
  -d '{
        "source" : "s3://{{bucket-name}}/{{object-key-name}}",
        "format" : "csv",
        "iamRoleArn" : "{{ARN for the IAM role you are using}}",
        "region" : "{{region}}",
        "failOnError" : "FALSE",
        "parallelism" : "MEDIUM",
        "updateSingleCardinalityProperties" : "FALSE",
        "queueRequest" : "FALSE"
      }'
```
To connect to a cluster that has IAM authentication enabled, each request must be signed. See [Connecting from the command line](iam-auth-connect-command-line.md).

```
curl -X POST https://{{your-neptune-endpoint}}:{{port}}/loader \
  -H 'Content-Type: application/json' \
  -d '{
        "source" : "s3://{{bucket-name}}/{{object-key-name}}",
        "format" : "csv",
        "iamRoleArn" : "{{ARN for the IAM role you are using}}",
        "region" : "{{region}}",
        "failOnError" : "FALSE",
        "parallelism" : "MEDIUM",
        "updateSingleCardinalityProperties" : "FALSE",
        "queueRequest" : "FALSE"
      }'
```
To connect to a cluster that has IAM authentication enabled, each request must be signed. See [Connecting from the command line](iam-auth-connect-command-line.md).

**Example Response**  

```
{
    "status" : "200 OK",
    "payload" : {
        "loadId" : "{{ef478d76-d9da-4d94-8ff1-08d9d4863aa5}}"
    }
}
```