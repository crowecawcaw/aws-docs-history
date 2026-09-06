

# Neptune Loader Cancel Job
<a name="load-api-reference-cancel"></a>

Cancels a load job.

To cancel a job, you must send an HTTP `DELETE` request to the `https://{{your-neptune-endpoint}}:{{port}}/loader` endpoint. The `loadId` can be appended to the `/loader` URL path, or included as a variable in the URL.

## Cancel Job request syntax
<a name="load-api-reference-cancel-syntax"></a>

```
DELETE https://{{your-neptune-endpoint}}:{{port}}/loader?loadId={{loadId}}
```

```
DELETE https://{{your-neptune-endpoint}}:{{port}}/loader/{{loadId}}
```

## Cancel Job Request Parameters
<a name="load-api-reference-cancel-parameters"></a>

**loadId**  
The ID of the load job.

## Cancel Job Response Syntax
<a name="load-api-reference-cancel-parameters-response"></a>

```
no response body
```

**200 OK**  
Successfully deleted load job returns a `200` code.

## Cancel Job Errors
<a name="load-api-reference-cancel-parameters-errors"></a>

When an error occurs, a JSON object is returned in the `BODY` of the response. The `message` object contains a description of the error.

**Error Categories**
+ **`Error 400`**   –   An invalid `loadId` returns an HTTP `400` bad request error. The message describes the error.
+ **`Error 500`**   –   A valid request that cannot be processed returns an HTTP `500` internal server error. The message describes the error.

## Cancel Job Error Messages
<a name="load-api-reference-cancel-parameters-errors-messages"></a>

The following are possible error messages from the cancel API with a description of the error.
+ `The load with id = {{load_id}} does not exist or not active` (HTTP 404)   –   The load was not found. Check the value of `id` parameter.
+ `Load cancellation is not permitted on a read replica instance.` (HTTP 405)   –   Loading is a write operation. Retry load on the read/write cluster endpoint. 

## Cancel Job Examples
<a name="load-api-reference-cancel-examples"></a>

**Example Request**  
The following is a request sent via HTTP `DELETE` using the `curl` command.  

```
aws neptunedata cancel-loader-job \
  --endpoint-url https://{{your-neptune-endpoint}}:{{port}} \
  --load-id {{0a237328-afd5-4574-a0bc-c29ce5f54802}}
```
For more information, see [cancel-loader-job](https://docs.aws.amazon.com/cli/latest/reference/neptunedata/cancel-loader-job.html) in the AWS CLI Command Reference.

```
import boto3
from botocore.config import Config

client = boto3.client(
    'neptunedata',
    endpoint_url='https://{{your-neptune-endpoint}}:{{port}}',
    config=Config(read_timeout=None, retries={'total_max_attempts': 1})
)

response = client.cancel_loader_job(
    loadId='{{0a237328-afd5-4574-a0bc-c29ce5f54802}}'
)

print(response)
```

```
awscurl 'https://{{your-neptune-endpoint}}:{{port}}/loader/{{0a237328-afd5-4574-a0bc-c29ce5f54802}}' \
  --region {{us-east-1}} \
  --service neptune-db \
  -X DELETE
```
This example assumes that your AWS credentials are configured in your environment. Replace {{us-east-1}} with the Region of your Neptune cluster.

```
curl -X DELETE 'https://{{your-neptune-endpoint}}:{{port}}/loader/{{0a237328-afd5-4574-a0bc-c29ce5f54802}}'
```