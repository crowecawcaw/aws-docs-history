# PreviewAnomalyDetector API

Use the `PreviewAnomalyDetector` operation to create an endpoint that
demonstrates how your metric data will be analyzed by the anomaly detection algorithm
during your specified time period. This endpoint helps you evaluate and validate the
detector's performance before implementation.

Valid HTTP verbs

`GET`, `POST`

Supported payload types

URL-encoded parameters

`application/x-www-form-urlencoded` for
`POST`

Supported parameters

`query=<string>` A Prometheus expression query
string.

`start=<rfc3339 | unix_timestamp>` Start timestamp if you
are using `query_range` to query for a range of time.

`end=<rfc3339 | unix_timestamp>` End timestamp if you are
using `query_range` to query for a range of time.

`step=<duration | float>` Query resolution step width in
`duration` format or as a `float` number of
seconds. Use only if you are using `query_range` to query for a
range of time, and required for such queries.

## Query parameter

formatting

Wrap your original PromQL expression with the RandomCutForest (RCF) pseudo
function in the query parameter. For more information, see [RandomCutForestConfiguration](../APIReference/API_RandomCutForestConfiguration.md "../APIReference/API_RandomCutForestConfiguration.md") in the _Amazon Managed Service for Prometheus API
Reference_.

The RCF function uses this format:

```
RCF(<query>
[,shingle size
[,sample size
[,ignore near expected from above
[,ignore near expected from below
[,ignore near expected from above ratio
[,ignore near expected from below ratio]]]]])
```

All parameters except the query are optional and use default values when omitted.
The minimal syntax is:

```

RCF(<query>)

```

You must wrap your query with an aggregation function. To use specific optional
parameters while omitting others, leave empty positions in the function:

```

RCF(<query>,,,,,1.0,1.0)

```

This example sets only the ratio parameters that ignore anomaly detection spikes
and drops based on the ratio between expected and observed values.

## API request and

response

Successful calls return the same format as the [QueryMetrics API](AMP-APIReference-QueryMetrics.md "AMP-APIReference-QueryMetrics.md"). In addition to
the original time series, the API returns these new time series when sufficient
samples are available:

- `anomaly_detector_preview:lower_band` – Lower band for
  the expected value of the PromQL expression result
- `anomaly_detector_preview:score` – Anomaly score between
  0 and 1, where 1 indicates high confidence of an anomaly at that data
  point
- `anomaly_detector_preview:upper_band` – Upper band for
  the expected value of the PromQL expression result

**Sample request**

```
POST /workspaces/`workspace-id`/anomalydetectors/preview
Content-Type: application/x-www-form-urlencoded

query=RCF%28avg%28vector%28time%28%29%29%29%2C%208%2C%20256%29&start=1735689600&end=1735695000&step=1m
```

**Sample response**

```
200 OK
...

{
  "status": "success",
  "data": {
    "result": [
      {
        "metric": {},
        "values": [
          [
            1735689600,
            "1735689600"
          ],
          [
            1735689660,
            "1735689660"
          ],
          .........
        ]
      },
      {
        "metric": {
          "anomaly_detector_preview": "upper_band"
        },
        "values": [
          [
            1735693500,
            "1.7356943E9"
          ],
          [
            1735693560,
            "1.7356945E9"
          ]
          ],
          .........
        ]
      },
      {
        "metric": {
          "anomaly_detector_preview": "lower_band"
        },
        "values": [
          [
            1735693500,
            "1.7356928E9"
          ],
          [
            1735693560,
            "1.7356929E9"
          ],
          .........
        ]
      },
      {
        "metric": {
          "anomaly_detector_preview": "score"
        },
        "values": [
          [
            1735693500,
            "0.0"
          ],
          [
            1735695000,
            "0.0"
          ],
          .........
        ]
      }
    ],
    "resultType": "matrix"
  }
}
```
