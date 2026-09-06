

# Neptune Loader Get-Status Examples
<a name="load-api-reference-status-examples"></a>

 The following examples showcase the usage of the Neptune loader's GET-Status API, which allows you to retrieve information about the status of your data loads into the Amazon Neptune graph database. These examples cover three main scenarios: retrieving the status of a specific load, listing the available load IDs, and requesting detailed status information for a specific load. 

## Example request for load status
<a name="load-api-reference-status-examples-status-request"></a>

The following is a request sent via HTTP `GET` using the `curl` command.

------
#### [ AWS CLI ]

```
aws neptunedata get-loader-job-status \
  --endpoint-url https://{{your-neptune-endpoint}}:{{port}} \
  --load-id {{loadId (a UUID)}}
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
    loadId='{{loadId (a UUID)}}'
)

print(response)
```

------
#### [ awscurl ]

```
awscurl 'https://{{your-neptune-endpoint}}:{{port}}/loader/{{loadId (a UUID)}}' \
  --region {{us-east-1}} \
  --service neptune-db
```

**Note**  
This example assumes that your AWS credentials are configured in your environment. Replace {{us-east-1}} with the Region of your Neptune cluster.

------
#### [ curl ]

```
curl -X GET 'https://{{your-neptune-endpoint}}:{{port}}/loader/{{loadId (a UUID)}}'
```

------

**Example Response**  

```
{
    "status" : "200 OK",
    "payload" : {
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
        }
    }
}
```

## Example request for loadIds
<a name="load-api-reference-status-examples-loadId-request"></a>

The following is a request sent via HTTP `GET` using the `curl` command.

------
#### [ AWS CLI ]

```
aws neptunedata list-loader-jobs \
  --endpoint-url https://{{your-neptune-endpoint}}:{{port}} \
  --limit 3
```

For more information, see [list-loader-jobs](https://docs.aws.amazon.com/cli/latest/reference/neptunedata/list-loader-jobs.html) in the AWS CLI Command Reference.

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

response = client.list_loader_jobs(
    limit=3
)

print(response)
```

------
#### [ awscurl ]

```
awscurl 'https://{{your-neptune-endpoint}}:{{port}}/loader?limit=3' \
  --region {{us-east-1}} \
  --service neptune-db
```

**Note**  
This example assumes that your AWS credentials are configured in your environment. Replace {{us-east-1}} with the Region of your Neptune cluster.

------
#### [ curl ]

```
curl -X GET 'https://{{your-neptune-endpoint}}:{{port}}/loader?limit=3'
```

------

**Example Response**  

```
{
    "status" : "200 OK",
    "payload" : {
         "loadIds" : [
            "a2c0ce44-a44b-4517-8cd4-1dc144a8e5b5",
            "09683a01-6f37-4774-bb1b-5620d87f1931",
            "58085eb8-ceb4-4029-a3dc-3840969826b9"
        ]
    }
}
```

## Example request for detailed status
<a name="load-api-reference-status-examples-details-request"></a>

The following is a request sent via HTTP `GET` using the `curl` command.

------
#### [ AWS CLI ]

```
aws neptunedata get-loader-job-status \
  --endpoint-url https://{{your-neptune-endpoint}}:{{port}} \
  --load-id {{loadId (a UUID)}} \
  --details
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
    loadId='{{loadId (a UUID)}}',
    details=True
)

print(response)
```

------
#### [ awscurl ]

```
awscurl 'https://{{your-neptune-endpoint}}:{{port}}/loader/{{loadId (a UUID)}}?details=true' \
  --region {{us-east-1}} \
  --service neptune-db
```

**Note**  
This example assumes that your AWS credentials are configured in your environment. Replace {{us-east-1}} with the Region of your Neptune cluster.

------
#### [ curl ]

```
curl -X GET 'https://{{your-neptune-endpoint}}:{{port}}/loader/{{loadId (a UUID)}}?details=true'
```

------

**Example Response**  

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
        }
    }
}
```