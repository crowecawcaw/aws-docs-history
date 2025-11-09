# Get statistics about your query usage for each query

Query [pricing](https://aws.amazon.com/prometheus/pricing/ "https://aws.amazon.com/prometheus/pricing/") is based
on the total number of query samples processed in a month from executed queries. You can
get statistics about each query that you make to keep track of your samples processed.
The query response for a `query` or a `queryRange` API can include
the statistics data about query samples processed by including the query parameter
`stats=all` in the request. A `samples` object is created in
the `stats` object and the `stats` data is returned in the
response.

The `samples` object consists of the following attributes:

| Attribute                      | Description                                                                                                                                                                            |
| ------------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `totalQueryableSamples`        | Total number of query samples processed. This is the information to<br>be used for billing.                                                                                            |
| `totalQueryableSamplesPerStep` | The number of query samples processed per each step. This is<br>structured as an array of arrays with the timestamp in epoch and the<br>number of samples loaded on the specific step. |

Sample requests and responses that include the `stats` information in the
response are as follows:

Example for `query`:

**GET**

```
`endpoint`/api/v1/query?query=up&time=1652382537&stats=all
```

**Response**

```
{
    "status": "success",
    "data": {
        "resultType": "vector",
        "result": [
            {
                "metric": {
                    "__name__": "up",
                    "instance": "localhost:9090",
                    "job": "prometheus"
                },
                "value": [
                    1652382537,
                    "1"
                ]
            }
        ],
        "stats": {
            "timings": {
                "evalTotalTime": 0.00453349,
                "resultSortTime": 0,
                "queryPreparationTime": 0.000019363,
                "innerEvalTime": 0.004508405,
                "execQueueTime": 0.000008786,
                "execTotalTime": 0.004554219
            },
            "samples": {
                "totalQueryableSamples": 1,
                "totalQueryableSamplesPerStep": [
                    [
                        1652382537,
                        1
                    ]
                ]
            }
        }
    }
}
```

Example for `queryRange`:

**GET**

```
`endpoint`/api/v1/query_range?query=sum+%28rate+%28go_gc_duration_seconds_count%5B1m%5D%29%29&start=1652382537&end=1652384705&step=1000&stats=all
```

**Response**

```
{
    "status": "success",
    "data": {
        "resultType": "matrix",
        "result": [
            {
                "metric": {},
                "values": [
                    [
                        1652383000,
                        "0"
                    ],
                    [
                        1652384000,
                        "0"
                    ]
                ]
            }
        ],
        "stats": {
            "samples": {
                "totalQueryableSamples": 8,
                "totalQueryableSamplesPerStep": [
                    [
                        1652382000,
                        0
                    ],
                    [
                        1652383000,
                        4
                    ],
                    [
                        1652384000,
                        4
                    ]
                ]
            }
        }
    }
}
```
