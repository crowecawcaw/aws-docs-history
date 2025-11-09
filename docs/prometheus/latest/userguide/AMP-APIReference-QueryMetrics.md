# QueryMetrics

The `QueryMetrics` operation evaluates an instant query at a single point
in time or over a range of time.

Valid HTTP verbs:

`GET`, `POST`

Valid URIs:

`/workspaces/`workspaceId`/api/v1/query`
This URI evaluates an instant query at a single point in time.

`/workspaces/`workspaceId`/api/v1/query_range`
This URI evaluates an instant query over a range of time.

URL query parameters:

`query=<string>` A Prometheus expression query string.
Used in both `query` and `query_range`.

`time=<rfc3339 | unix_timestamp>` (Optional) Evaluation
timestamp if you are using the `query` for an instant query at a
single point in time.

`timeout=<duration>` (Optional) Evaluation timeout.
Defaults to and is capped by the value of the `-query.timeout`
flag. Used in both `query` and `query_range`.

`start=<rfc3339 | unix_timestamp>` Start timestamp if you
are using `query_range` to query for a range of time.

`end=<rfc3339 | unix_timestamp>` End timestamp if you are
using `query_range` to query for a range of time.

`step=<duration | float>` Query resolution step width in
`duration` format or as a `float` number of
seconds. Use only if you are using `query_range` to query for a
range of time, and required for such queries.

`max_samples_processed_warning_threshold=<integer>`
(Optional) Sets the warning threshold for Query Samples Processed (QSP).
When queries hit this threshold, a warning message will be returned in the
API response.

`max_samples_processed_error_threshold=<integer>>`
(Optional) Sets the error threshold for Query Samples Processed (QSP).
Queries that exceed this threshold will be rejected with an error and will
not be charged. Used to prevent excessive query costs.

**Duration**

A `duration` in a Prometheus-compatible API is a number, followed
immediately by one of the following units:

- `ms` milliseconds
- `s` seconds
- `m` minutes
- `h` hours
- `d` days, assuming a day always has 24h
- `w` weeks, assuming a week always has 7d
- `y` years, assuming a year always has 365d
  **Sample request**

```
POST /workspaces/ws-b226cc2a-a446-46a9-933a-ac50479a5568/api/v1/query?query=sum(node_cpu_seconds_total) HTTP/1.1
Content-Length: 0,
Authorization: AUTHPARAMS
X-Amz-Date: 20201201T193725Z
User-Agent: Grafana/8.1.0
```

**Sample response**

```
HTTP/1.1 200 OK
x-amzn-RequestId: 12345678-abcd-4442-b8c5-262b45e9b535
Content-Length: 132
Connection: keep-alive
Date: Tue, 01 Dec 2020 19:37:25 GMT
Content-Type: application/json
Server: amazon
content-encoding: gzip

{
    "status": "success",
    "data": {
        "resultType": "vector",
        "result": [
            {
                "metric": {},
                "value": [
                    1634937046.322,
                    "252590622.81000024"
                ]
            }
        ]
    }
}
```
