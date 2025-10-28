# GetMetricMetadata

The `GetMetricMetadata` operation retrieves metadata about metrics that are
currently being scraped from targets. It does not provide any target information.

The data section of the query result consists of an object where each key is a metric
name and each value is a list of unique metadata objects, as exposed for that metric
name across all targets.

Valid HTTP verbs:

`GET`

Valid URIs:

`/workspaces/`workspaceId`/api/v1/metadata`

URL query parameters:

`limit=<number>` The maximum number of metrics to
return.

`metric=<string>` A metric name to filter metadata for.
If you keep this empty, all metric metadata is retrieved.

**Sample request**

```
GET /workspaces/ws-b226cc2a-a446-46a9-933a-ac50479a5568/api/v1/metadata HTTP/1.1
Content-Length: 0,
Authorization: AUTHPARAMS
X-Amz-Date: 20201201T193725Z
User-Agent: Grafana/8.1.0
```

**Sample response**

```
HTTP/1.1 200 OK
x-amzn-RequestId: 12345678-abcd-4442-b8c5-262b45e9b535
Connection: keep-alive
Date: Tue, 01 Dec 2020 19:37:25 GMT
Content-Type: application/json
Server: amazon
Transfer-Encoding: chunked

{
    "status": "success",
    "data": {
        "aggregator_openapi_v2_regeneration_count": [
            {
                "type": "counter",
                "help": "[ALPHA] Counter of OpenAPI v2 spec regeneration count broken down by causing APIService name and reason.",
                "unit": ""
            }
        ],
        ...
    }
}
```
