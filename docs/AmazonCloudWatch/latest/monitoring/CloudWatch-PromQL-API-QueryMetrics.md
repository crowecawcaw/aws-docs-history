

# QueryMetrics
<a name="CloudWatch-PromQL-API-QueryMetrics"></a>

The `QueryMetrics` operation evaluates a PromQL instant query at a single point in time, or evaluates a query over a range of time.

Valid HTTP verbs  
`GET`, `POST`

Valid URIs  
`/api/v1/query` — evaluates an instant query at a single point in time.  
`/api/v1/query_range` — evaluates a query over a range of time.

The full request URL combines the CloudWatch monitoring host for the AWS Region with the operation path, for example `https://monitoring.{{AWS Region}}.amazonaws.com/api/v1/query`. For information about endpoints, signing, and required IAM permissions, see [PromQL querying](CloudWatch-PromQL-Querying.md).

## URL query parameters
<a name="CloudWatch-PromQL-API-QueryMetrics-Parameters"></a>

The following parameters are passed in the URL query string for `GET` requests, or as form-encoded body fields for `POST` requests.


| Parameter | Applies to | Description | 
| --- | --- | --- | 
| `query` | Both | Required. The PromQL expression string to evaluate. The expression must select a metric by name — for example, `{"http.server.active_requests"}` or `{__name__="http.server.active_requests"}`. Selecting series only by labels, without a metric name, is not supported. | 
| `time` | `/api/v1/query` | Optional. Evaluation timestamp as an RFC 3339 timestamp or a Unix timestamp. Defaults to the current server time. | 
| `start` | `/api/v1/query_range` | Required. Start of the time range, as an RFC 3339 timestamp or a Unix timestamp. | 
| `end` | `/api/v1/query_range` | Required. End of the time range, as an RFC 3339 timestamp or a Unix timestamp. | 
| `step` | `/api/v1/query_range` | Required. Query resolution step width, in `duration` format or as a floating-point number of seconds. | 
| `limit` | Both | Optional. Maximum number of unique time series to return, from `1` to `500`. If you do not specify `limit`, CloudWatch returns up to the maximum (500). See [Result limit](#CloudWatch-PromQL-API-QueryMetrics-Limits). | 

**Duration**

A `duration` in a Prometheus-compatible API is a number, followed immediately by one of the following units:
+ `ms` milliseconds
+ `s` seconds
+ `m` minutes
+ `h` hours
+ `d` days, assuming a day always has 24h
+ `w` weeks, assuming a week always has 7d
+ `y` years, assuming a year always has 365d

## Required IAM permissions
<a name="CloudWatch-PromQL-API-QueryMetrics-IAM"></a>

To call `QueryMetrics`, the calling identity must have both of the following IAM actions:
+ `cloudwatch:GetMetricData`
+ `cloudwatch:ListMetrics`

For the complete IAM action mapping for all PromQL operations, see [IAM permissions for PromQL](CloudWatch-PromQL.md#CloudWatch-PromQL-IAM).

## Result limit
<a name="CloudWatch-PromQL-API-QueryMetrics-Limits"></a>

A single `/api/v1/query` or `/api/v1/query_range` response can return up to **500 unique time series**. To request fewer results, pass the `limit` parameter with a value from `1` to `500`. If you do not specify `limit`, CloudWatch returns up to the maximum.

When the matching series exceed the cap, the response is truncated and a message is included in the standard Prometheus `warnings` field. The HTTP status code remains `200`.

For the full list of PromQL limits, including TPS, concurrency, and 24-hour scan windows, see [PromQL limits and restrictions](CloudWatch-PromQL.md#CloudWatch-PromQL-Limits).

## Sample request
<a name="CloudWatch-PromQL-API-QueryMetrics-Sample"></a>

The following `POST` request passes the PromQL expression in a form-encoded body. Special characters such as `{`, `}`, and `"` are percent-encoded.

```
POST /api/v1/query HTTP/1.1
Host: monitoring.us-east-1.amazonaws.com
Content-Type: application/x-www-form-urlencoded
Authorization: AUTHPARAMS
X-Amz-Date: 20260605T193725Z
User-Agent: awscurl/0.36

query=sum(%7B%22http.server.active_requests%22%7D)
```

The same call with `awscurl`:

```
awscurl --service monitoring --region us-east-1 \
    -X POST 'https://monitoring.us-east-1.amazonaws.com/api/v1/query' \
    -H 'Content-Type: application/x-www-form-urlencoded' \
    -d 'query=sum({"http.server.active_requests"})'
```

## Sample response
<a name="CloudWatch-PromQL-API-QueryMetrics-Response"></a>

A successful response uses the standard Prometheus JSON envelope:

```
HTTP/1.1 200 OK
x-amzn-RequestId: 12345678-abcd-4442-b8c5-262b45e9b535
Content-Type: application/json

{
    "status": "success",
    "data": {
        "resultType": "vector",
        "result": [
            {
                "metric": {},
                "value": [
                    1780000000.000,
                    "42"
                ]
            }
        ]
    }
}
```

When the result set exceeds the per-call cap, CloudWatch returns a truncated `result` array and includes a message in the `warnings` field:

```
HTTP/1.1 200 OK
Content-Type: application/json

{
    "status": "success",
    "data": {
        "resultType": "vector",
        "result": [ ... up to 500 series ... ]
    },
    "warnings": [
        "result truncated to the maximum of 500 series; refine the query or use the limit parameter"
    ]
}
```