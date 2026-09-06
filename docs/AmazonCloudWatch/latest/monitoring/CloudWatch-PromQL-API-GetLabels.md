

# GetLabels
<a name="CloudWatch-PromQL-API-GetLabels"></a>

The `GetLabels` operation returns label names that are present in the metric store, or returns the values for a specific label name.

Valid HTTP verbs  
`GET`, `POST` for `/api/v1/labels`.  
`GET` for `/api/v1/label/{{label_name}}/values`.

Valid URIs  
`/api/v1/labels` — returns the list of label names.  
`/api/v1/label/{{label_name}}/values` — returns the list of values for the specified label.

The full request URL combines the CloudWatch monitoring host for the AWS Region with the operation path, for example `https://monitoring.{{AWS Region}}.amazonaws.com/api/v1/labels`. For information about endpoints, signing, and required IAM permissions, see [PromQL querying](CloudWatch-PromQL-Querying.md).

## URL query parameters
<a name="CloudWatch-PromQL-API-GetLabels-Parameters"></a>

The following parameters are passed in the URL query string for `GET` requests, or as form-encoded body fields for `POST` requests.


| Parameter | Applies to | Description | 
| --- | --- | --- | 
| `match[]` | Both | Optional. A series selector that restricts which series are considered when computing the result. Selectors support exact match (`=`), not equal (`!=`), regex match (`=~`), and negative regex match (`!~`). Specify `match[]` one or more times to combine selectors. For more information about selector syntax, see [PromQL querying](CloudWatch-PromQL-Querying.md). | 
| `start` | Both | Optional. Start of the time range to consider, as an RFC 3339 timestamp or a Unix timestamp. | 
| `end` | Both | Optional. End of the time range to consider, as an RFC 3339 timestamp or a Unix timestamp. | 
| `limit` | Both | Optional. Maximum number of unique labels to return, from `1` to `10000`. If you do not specify `limit`, CloudWatch returns up to the maximum (10,000). See [Result limit](#CloudWatch-PromQL-API-GetLabels-Limits). | 

## Required IAM permissions
<a name="CloudWatch-PromQL-API-GetLabels-IAM"></a>

To call `GetLabels` on either path, the calling identity must have the following IAM action:
+ `cloudwatch:ListMetrics`

For the complete IAM action mapping for all PromQL operations, see [IAM permissions for PromQL](CloudWatch-PromQL.md#CloudWatch-PromQL-IAM).

## Result limit
<a name="CloudWatch-PromQL-API-GetLabels-Limits"></a>

A single `/api/v1/labels` or `/api/v1/label/{{label_name}}/values` response can return up to **10,000 labels**. To request fewer results, pass the `limit` parameter with a value from `1` to `10000`. If you do not specify `limit`, CloudWatch returns up to the maximum.

When the matching labels exceed the cap, the response is truncated and a message is included in the standard Prometheus `warnings` field. The HTTP status code remains `200`.

For the full list of PromQL limits, including TPS, concurrency, and 24-hour scan windows, see [PromQL limits and restrictions](CloudWatch-PromQL.md#CloudWatch-PromQL-Limits).

## Sample requests
<a name="CloudWatch-PromQL-API-GetLabels-Sample"></a>

List all label names with a `POST` request and an empty body:

```
POST /api/v1/labels HTTP/1.1
Host: monitoring.us-east-1.amazonaws.com
Content-Type: application/x-www-form-urlencoded
Content-Length: 0
Authorization: AUTHPARAMS
X-Amz-Date: 20260605T193725Z
User-Agent: awscurl/0.36
```

The same call with `awscurl`:

```
awscurl --service monitoring --region us-east-1 \
    -X POST 'https://monitoring.us-east-1.amazonaws.com/api/v1/labels' \
    -H 'Content-Type: application/x-www-form-urlencoded'
```

List label names matching a selector. The selector and time range are passed as form-encoded fields in the request body:

```
awscurl --service monitoring --region us-east-1 \
    -X POST 'https://monitoring.us-east-1.amazonaws.com/api/v1/labels' \
    -H 'Content-Type: application/x-www-form-urlencoded' \
    -d 'match[]={"http.server.active_requests","@aws.region"=~"us-.*"}&start=1780662000&end=1780665600'
```

List the values for the `@resource.service.name` label. The label name is part of the URL path and is percent-encoded (`@` → `%40`). This path supports only `GET`:

```
GET /api/v1/label/%40resource.service.name/values HTTP/1.1
Host: monitoring.us-east-1.amazonaws.com
Authorization: AUTHPARAMS
X-Amz-Date: 20260605T193725Z
User-Agent: awscurl/0.36
```

The same call with `awscurl`:

```
awscurl --service monitoring --region us-east-1 \
    'https://monitoring.us-east-1.amazonaws.com/api/v1/label/@resource.service.name/values'
```

## Sample responses
<a name="CloudWatch-PromQL-API-GetLabels-Response"></a>

A successful response uses the standard Prometheus JSON envelope. The `data` field is an array of strings.

Response for `/api/v1/labels`:

```
HTTP/1.1 200 OK
Content-Type: application/json

{
    "status": "success",
    "data": [
        "__name__",
        "@aws.account",
        "@aws.region",
        "@resource.service.name",
        "@resource.cloud.region",
        "InstanceId"
    ]
}
```

Response for `/api/v1/label/{{label_name}}/values`:

```
HTTP/1.1 200 OK
Content-Type: application/json

{
    "status": "success",
    "data": [
        "myservice",
        "checkout-api",
        "billing-worker"
    ]
}
```