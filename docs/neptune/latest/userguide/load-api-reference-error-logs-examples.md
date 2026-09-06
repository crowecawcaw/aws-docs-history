

# Neptune Loader Get-Status `errorLogs` examples
<a name="load-api-reference-error-logs-examples"></a>

 The following examples showcase the detailed status response from the Neptune loader when errors have occurred during the data loading process. The examples illustrate the structure of the response, including information about failed feeds, overall status, and detailed error logs. 

## Example detailed status response when errors occurred
<a name="load-api-reference-status-examples-details-request-errors"></a>

This a request sent via HTTP `GET` using `curl`:

------
#### [ AWS CLI ]

```
aws neptunedata get-loader-job-status \
  --endpoint-url https://{{your-neptune-endpoint}}:{{port}} \
  --load-id {{0a237328-afd5-4574-a0bc-c29ce5f54802}} \
  --details \
  --errors \
  --errors-per-page 3 \
  --page 1
```

For more information, see [get-loader-job-status](https://docs.aws.amazon.com/cli/latest/reference/neptunedata/get-loader-job-status.html) in the AWS CLI Command Reference.

------
#### [ SDK ]

```
import boto3
from botocore.config import Config

client = boto3.client(
    'neptunedata',
    endpoint_url='https://{{your-neptune-endpoint}}:{{port}}',
    config=Config(read_timeout=None, retries={'total_max_attempts': 1})
)

response = client.get_loader_job_status(
    loadId='{{0a237328-afd5-4574-a0bc-c29ce5f54802}}',
    details=True,
    errors=True,
    errorsPerPage=3,
    page=1
)

print(response)
```

------
#### [ awscurl ]

```
awscurl 'https://{{your-neptune-endpoint}}:{{port}}/loader/{{0a237328-afd5-4574-a0bc-c29ce5f54802}}?details=true&errors=true&page=1&errorsPerPage=3' \
  --region {{us-east-1}} \
  --service neptune-db
```

**Note**  
This example assumes that your AWS credentials are configured in your environment. Replace {{us-east-1}} with the Region of your Neptune cluster.

------
#### [ curl ]

```
curl -X GET 'https://{{your-neptune-endpoint}}:{{port}}/loader/{{0a237328-afd5-4574-a0bc-c29ce5f54802}}?details=true&errors=true&page=1&errorsPerPage=3'
```

------

**Example of a detailed response when errors have occurred**  
This is an example of the response that you might get from the query above, with an `errorLogs` object listing the load errors encountered:  

```
{
    "status" : "200 OK",
    "payload" : {
        "failedFeeds" : [
            {
                "datatypeMismatchErrors" : 0,
                "fullUri" : "s3://{{bucket}}/{{key}}",
                "insertErrors" : 0,
                "parsingErrors" : 5,
                "retryNumber" : 0,
                "runNumber" : 1,
                "status" : "LOAD_FAILED",
                "totalDuplicates" : 0,
                "totalRecords" : 5,
                "totalTimeSpent" : 3.0
            }
        ],
        "feedCount" : [
            {
                "LOAD_FAILED" : 1
            }
        ],
        "overallStatus" : {
            "datatypeMismatchErrors" : 0,
            "fullUri" : "s3://{{bucket}}/{{key}}",
            "insertErrors" : 0,
            "parsingErrors" : 5,
            "retryNumber" : 0,
            "runNumber" : 1,
            "status" : "LOAD_FAILED",
            "totalDuplicates" : 0,
            "totalRecords" : 5,
            "totalTimeSpent" : 3.0
        },
        "errors" : {
            "endIndex" : 3,
            "errorLogs" : [
                {
                    "errorCode" : "PARSING_ERROR",
                    "errorMessage" : "Expected '<', found: |",
                    "fileName" : "s3://{{bucket}}/{{key}}",
                    "recordNum" : 1
                },
                {
                    "errorCode" : "PARSING_ERROR",
                    "errorMessage" : "Expected '<', found: |",
                    "fileName" : "s3://{{bucket}}/{{key}}",
                    "recordNum" : 2
                },
                {
                    "errorCode" : "PARSING_ERROR",
                    "errorMessage" : "Expected '<', found: |",
                    "fileName" : "s3://{{bucket}}/{{key}}",
                    "recordNum" : 3
                }
            ],
            "loadId" : "{{0a237328-afd5-4574-a0bc-c29ce5f5480}}2",
            "startIndex" : 1
        }
    }
}
```

## Example of a `Data prefetch task interrupted` error
<a name="load-api-reference-status-examples-task-interrupted"></a>

Occasionally when you get a `LOAD_FAILED` status and then request more detailed information, the error returned may be a `PARSING_ERROR` with a `Data prefetch task interrupted` message, like this:

```
"errorLogs" : [
    {
        "errorCode" : "PARSING_ERROR",
        "errorMessage" : "Data prefetch task interrupted: Data prefetch task for 11467 failed",
        "fileName" : "s3://amzn-s3-demo-bucket/{{some-source-file}}",
        "recordNum" : 0
    }
]
```

This error occurs when there was a temporary interruption in the data load process that was typically not caused by your request or your data. It can usually be resolved simply by running the bulk upload request again. If you are using default settings, namely `"mode":"AUTO"`, and `"failOnError":"TRUE"`, the loader skips the files that it already successfully loaded and resumes loading files it had not yet loaded when the interruption occurred.