

# GetSeries
<a name="CloudWatch-PromQL-API-GetSeries"></a>

The `GetSeries` operation returns the list of time series whose labels match one or more selectors.

Valid HTTP verbs  
`GET`, `POST`

Valid URI  
`/api/v1/series`

The full request URL combines the CloudWatch monitoring host for the AWS Region with the operation path, for example `https://monitoring.{{AWS Region}}.amazonaws.com/api/v1/series`. For information about endpoints, signing, and required IAM permissions, see [PromQL querying](CloudWatch-PromQL-Querying.md).

## URL query parameters
<a name="CloudWatch-PromQL-API-GetSeries-Parameters"></a>

The following parameters are passed in the URL query string for `GET` requests, or as form-encoded body fields for `POST` requests.


| Parameter | Description | 
| --- | --- | 
| `match[]` | Required. A series selector that filters the time series to return. Each selector must include an exact match (`=`) on the metric name — for example, `{"http.server.active_requests"}` or `{__name__="http.server.active_requests"}`. Selectors without a metric-name equal matcher are not supported. In addition to exact match, label matchers also support not equal (`!=`), regex match (`=~`), and negative regex match (`!~`). Specify `match[]` one or more times to combine selectors. For more information about selector syntax, see [PromQL querying](CloudWatch-PromQL-Querying.md). | 
| `start` | Required. Start of the time range to consider, as an RFC 3339 timestamp or a Unix timestamp. | 
| `end` | Required. End of the time range to consider, as an RFC 3339 timestamp or a Unix timestamp. | 
| `limit` | Optional. Maximum number of unique time series to return, from `1` to `10000`. If you do not specify `limit`, CloudWatch returns up to the maximum (10,000). See [Result limit](#CloudWatch-PromQL-API-GetSeries-Limits). | 

## Required IAM permissions
<a name="CloudWatch-PromQL-API-GetSeries-IAM"></a>

To call `GetSeries`, the calling identity must have the following IAM action:
+ `cloudwatch:ListMetrics`

For the complete IAM action mapping for all PromQL operations, see [IAM permissions for PromQL](CloudWatch-PromQL.md#CloudWatch-PromQL-IAM).

## Result limit
<a name="CloudWatch-PromQL-API-GetSeries-Limits"></a>

A single `/api/v1/series` response can return up to **10,000 unique time series**. To request fewer results, pass the `limit` parameter with a value from `1` to `10000`. If you do not specify `limit`, CloudWatch returns up to the maximum.

When the matching series exceed the cap, the response is truncated and a message is included in the standard Prometheus `warnings` field. The HTTP status code remains `200`.

For the full list of PromQL limits, including TPS, concurrency, and 24-hour scan windows, see [PromQL limits and restrictions](CloudWatch-PromQL.md#CloudWatch-PromQL-Limits).

## Sample requests
<a name="CloudWatch-PromQL-API-GetSeries-Sample"></a>

The following `POST` request uses an exact match selector. The selector, `start`, and `end` are passed as form-encoded fields in the request body. Special characters such as `{`, `}`, `"`, and `,` are percent-encoded. The decoded `match[]` value is `{"http.server.active_requests","@resource.service.name"="myservice"}`.

```
POST /api/v1/series HTTP/1.1
Host: monitoring.us-east-1.amazonaws.com
Content-Type: application/x-www-form-urlencoded
Authorization: AUTHPARAMS
X-Amz-Date: 20260605T193725Z
User-Agent: awscurl/0.36

match%5B%5D=%7B%22http.server.active_requests%22%2C%22%40resource.service.name%22%3D%22myservice%22%7D&start=1780662000&end=1780665600
```

The following `POST` request uses a regex match selector. The decoded `match[]` value is `{"http.server.active_requests","@aws.region"=~"us-.*"}`.

```
POST /api/v1/series HTTP/1.1
Host: monitoring.us-east-1.amazonaws.com
Content-Type: application/x-www-form-urlencoded
Authorization: AUTHPARAMS
X-Amz-Date: 20260605T193725Z
User-Agent: awscurl/0.36

match%5B%5D=%7B%22http.server.active_requests%22%2C%22%40aws.region%22%3D~%22us-.*%22%7D&start=1780662000&end=1780665600
```

The same call with `awscurl`:

```
awscurl --service monitoring --region us-east-1 \
    -X POST 'https://monitoring.us-east-1.amazonaws.com/api/v1/series' \
    -H 'Content-Type: application/x-www-form-urlencoded' \
    -d 'match[]={"http.server.active_requests","@aws.region"=~"us-.*"}&start=1780662000&end=1780665600'
```

## Sample response
<a name="CloudWatch-PromQL-API-GetSeries-Response"></a>

A successful response uses the standard Prometheus JSON envelope. The `data` field is an array of label maps, one per matched series.

```
HTTP/1.1 200 OK
x-amzn-RequestId: 12345678-abcd-4442-b8c5-262b45e9b535
Content-Type: application/json

{
    "status": "success",
    "data": [
        {
            "__name__": "http.server.active_requests",
            "@resource.service.name": "myservice",
            "@aws.region": "us-east-1"
        },
        {
            "__name__": "http.server.active_requests",
            "@resource.service.name": "myservice",
            "@aws.region": "us-west-2"
        }
    ]
}
```