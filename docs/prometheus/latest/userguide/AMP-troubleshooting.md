# Troubleshoot Amazon Managed Service for Prometheus errors

Use the following sections to help troubleshoot issues with Amazon Managed Service for Prometheus.

###### Topics

- [429 or limit exceeded errors](#AMP-troubleshoot-429 "#AMP-troubleshoot-429")
- [I see duplicate samples](#AMP-troubleshoot-duplicate "#AMP-troubleshoot-duplicate")
- [I see errors about sample timestamps](#AMP-troubleshoot-duplicate-ordering "#AMP-troubleshoot-duplicate-ordering")
- [I see an error message related to a limit](#AMP-troubleshoot-limiterror "#AMP-troubleshoot-limiterror")
- [Your local Prometheus server output exceeds the limit.](#AMP-understand-output "#AMP-understand-output")
- [Some of my data isn't appearing](#AMP-troubleshoot-discarded-data "#AMP-troubleshoot-discarded-data")
- [HTTP 422 error: query timeout](#AMP-troubleshoot-http-422 "#AMP-troubleshoot-http-422")

## 429 or limit exceeded errors

If you see a 429 error similar to the following example, your requests have exceeded
Amazon Managed Service for Prometheus ingestion quotas.

```
ts=2020-10-29T15:34:41.845Z caller=dedupe.go:112 component=remote level=error remote_name=e13b0c
url=http://iamproxy-external.prometheus.uswest2-prod.eks:9090/workspaces/`workspace_id`/api/v1/remote_write
msg="non-recoverable error" count=500 err="server returned HTTP status 429
Too Many Requests: ingestion rate limit (6666.666666666667) exceeded while adding 499 samples and 0 metadata
```

If you see a 429 error similar to the following example, your requests have exceeded
the Amazon Managed Service for Prometheus quota for the number of active metrics in a workspace.

```
ts=2020-11-05T12:40:33.375Z caller=dedupe.go:112 component=remote level=error remote_name=aps
url=http://iamproxy-external.prometheus.uswest2-prod.eks:9090/workspaces/`workspace_id`/api/v1/remote_write
msg="non-recoverable error" count=500 err="server returned HTTP status 429 Too Many Requests: user=`accountid`_`workspace_id`:
per-user series limit (local limit: 0 global limit: 3000000 actual local limit: 500000) exceeded
```

If you see a 429 error similar to the following example, your requests have exceeded
the Amazon Managed Service for Prometheus quota for the rate (transactions per second) that you can send data to
your workspace using the `RemoteWrite` Prometheus compatible API.

```
ts=2024-03-26T16:50:21.780708811Z caller=dedupe.go:112 component=remote level=error remote_name=ab123c
url=https://aps-workspaces.us-east-1.amazonaws.com/workspaces/`workspace_id`/api/v1/remote_write
msg="non-recoverable error" count=1000 exemplarCount=0 err="server returned HTTP status 429 Too Many Requests: {\"message\":\"Rate exceeded\"}"
```

If you see a 400 error similar to the following example, your requests have exceeded
Amazon Managed Service for Prometheus quota for active time series. For details about how active time series quotas
are handled, see [Active series default quotas](AMP_quotas.md#AMP-dynamic-series "AMP_quotas.md#AMP-dynamic-series").

```
ts=2024-03-26T16:50:21.780708811Z caller=push.go:53 level=warn
url=https://aps-workspaces.us-east-1.amazonaws.com/workspaces/`workspace_id`/api/v1/remote_write
msg="non-recoverable error" count=500 exemplarCount=0
err="server returned HTTP status 400 Bad Request: maxFailure (quorum) on a given error family, rpc error: code = Code(400)
desc = addr=10.1.41.23:9095 state=ACTIVE zone=us-east-1a, rpc error: code = Code(400)
desc = user=`accountid`_`workspace_id`: per-user series limit of 10000000 exceeded,
Capacity from 2,000,000 to 10,000,000 is automatically adjusted based on the last 30 min of usage.
If throttled above 10,000,000 or in case of incoming surges, please contact administrator to raise it.
(local limit: 0 global limit: 10000000 actual local limit: 92879)"
```

For more information about Amazon Managed Service for Prometheus service quotas and about how to request
increases, see [Amazon Managed Service for Prometheus service quotas](AMP_quotas.md "AMP_quotas.md")

## I see duplicate samples

If you are using a high-availability Prometheus group, you need to use external labels
on your Prometheus instances to set up deduplication. For more information, see [Deduplicating high availability metrics sent to Amazon Managed Service for Prometheus](AMP-ingest-dedupe.md "AMP-ingest-dedupe.md").

Other issues around duplicated data are discussed in the next section.

## I see errors about sample timestamps

Amazon Managed Service for Prometheus ingests data in order, and expects each sample to have a timestamp later
than the previous sample.

If your data does not arrive in order, you can see errors about `out-of-order
 samples`, `duplicate sample for timestamp`, or `samples with 
 different value but same timestamp`. These issues are typically caused by
incorrect setup of the client that is sending data to Amazon Managed Service for Prometheus. If you are using a
Prometheus client running in agent mode, check the configuration for rules with
duplicate series name, or duplicated targets. If your metrics provide the timestamp
directly, check that they are not out of order.

You can configure an out-of-order time window for your workspace to accept
out-of-order samples. For more information, see [Configure your workspace](AMP-workspace-configuration.md "AMP-workspace-configuration.md").

For more details about how this works, or ways to check your setup, see the blog post [Understanding Duplicate Samples and Out-of-order Timestamp Errors in Prometheus](https://promlabs.com/blog/2022/12/15/understanding-duplicate-samples-and-out-of-order-timestamp-errors-in-prometheus/ "https://promlabs.com/blog/2022/12/15/understanding-duplicate-samples-and-out-of-order-timestamp-errors-in-prometheus/")
from _Prom Labs_.

## I see an error message related to a limit

###### Note

Amazon Managed Service for Prometheus provides [CloudWatch usage metrics](AMP-CW-usage-metrics.md "AMP-CW-usage-metrics.md") to monitor Prometheus resource usage. Using the CloudWatch
usage metrics alarm feature, you can monitor Prometheus resources and usage to
prevent limit errors.

If you see one of the following error messages, you can request an increase in one of
the Amazon Managed Service for Prometheus quotas to solve the issue. For more information, see [Amazon Managed Service for Prometheus service quotas](AMP_quotas.md "AMP_quotas.md").

- **`per-user series limit of `<value>` exceeded, please contact
 administrator to raise it`**
- **`per-metric series limit of `<value>` exceeded, please contact
 administrator to raise it`**
- **`ingestion rate limit (...) exceeded`**
- **`series has too many labels (...) series: '%s'`**
- **`the query time range exceeds the limit (query length: xxx, limit:
 yyy)`**
- **`the query hit the max number of chunks limit while fetching chunks
 from ingesters`**
- **`Limit exceeded. Maximum workspaces per account.`**

## Your local Prometheus server output exceeds the limit.

Amazon Managed Service for Prometheus has service quotas for the amount of data that a workspace can receive from
Prometheus servers. To find the amount of data that your Prometheus server is sending to
Amazon Managed Service for Prometheus, you can run the following queries on your Prometheus server. If you find that
your Prometheus output is exceeding a Amazon Managed Service for Prometheus limit, you can request an increase of
the corresponding service quota. For more information, see [Amazon Managed Service for Prometheus service quotas](AMP_quotas.md "AMP_quotas.md").

Queries against your local self-run Prometheus server to find the output limits.| Type of data | Query to use |
| --- | --- |
| Current active series | `prometheus_tsdb_head_series` |
| Current ingestion rate | `rate(prometheus_tsdb_head_samples_appended_total[5m])` |
| Most-to-least list of active series per metric name | `sort_desc(count by(__name__) ({__name__!=""}))` |
| Number of labels per metric series | `group by(mylabelname) ({__name__!=""})` |

## Some of my data isn't appearing

Data that is sent to Amazon Managed Service for Prometheus can be discarded for various reasons. The following
table shows reasons that data might be discarded rather than being ingested.

You can track the amount and reasons that data is discarded using Amazon CloudWatch. For more
information, see [Use CloudWatch metrics to monitor Amazon Managed Service for Prometheus resources](AMP-CW-usage-metrics.md "AMP-CW-usage-metrics.md").

| Reason                                           | Meaning                                                                                                                                                                                                         |
| ------------------------------------------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| greater\_than\_max\_sample\_age                  | Discarding log lines which are older than the current time                                                                                                                                                      |
| new-value-for-timestamp                          | Duplicate samples are sent with the same timestamp as the previous sample<br>but with different values.                                                                                                         |
| per\_metric\_series\_limit                       | User has hit the active series per metric limit                                                                                                                                                                 |
| per\_user\_series\_limit                         | User has hit the total number of active series limit                                                                                                                                                            |
| rate\_limited                                    | Ingestion rate limited                                                                                                                                                                                          |
| sample-out-of-order                              | Samples are sent out of order and cannot be processed. This reason is only emitted when the out-of-order time window is set to 0.                                                                               |
| sample-too-old                                   | Sample is older than the configured out-of-order time window and cannot be processed.                                                                                                                           |
| out-of-order-rate-limit                          | Out-of-order ingestion rate limit was reached and the sample cannot be processed. For more information, see [Amazon Managed Service for Prometheus service quotas](AMP_quotas.md "AMP_quotas.md").              |
| label\_value\_too\_long                          | Label value is longer than allowed character limit                                                                                                                                                              |
| max\_label\_names\_per\_series                   | User has hit the label names per metric                                                                                                                                                                         |
| missing\_metric\_name                            | Metric name is not provided                                                                                                                                                                                     |
| metric\_name\_invalid                            | Invalid metric name provided                                                                                                                                                                                    |
| label\_invalid                                   | Invalid label provided                                                                                                                                                                                          |
| duplicate\_label\_names                          | Duplicate label names provided                                                                                                                                                                                  |
| native\_histogram\_sample\_size\_bytes\_exceeded | Native histogram sample exceeds the maximum allowed sample size.<br>Reduce the number of buckets or spans in the histogram on the client<br>side.                                                               |
| native\_histogram\_invalid\_schema               | Native histogram has an invalid schema value. Valid schemas range<br>from -4 to 8. Check your Prometheus client configuration for the<br>`NativeHistogramBucketFactor` setting.                                 |
| native\_histogram\_invalid                       | Native histogram fails validation (for example, negative bucket<br>counts, mismatched bucket counts, or malformed bucket spans). This<br>typically indicates a bug in the instrumentation library.              |
| native\_histogram\_buckets\_exceeded             | Native histogram exceeds the maximum bucket count limit and<br>resolution cannot be automatically reduced. Reduce the number of<br>buckets on the client side using<br>`NativeHistogramMaxBucketNumber`.        |
| native\_histogram\_rate\_limited                 | Native histogram sample was rejected because the native histogram<br>ingestion rate limit was reached. Reduce the number of native<br>histogram series or the scrape frequency, or request a limit<br>increase. |
| per\_user\_native\_histogram\_series\_limit      | User has hit the native histogram active series limit per<br>workspace. Reduce the number of native histogram series or request a<br>limit increase.                                                            |

## HTTP 422 error: query timeout

If your query runs for more than 1 minute, Amazon Managed Service for Prometheus returns an HTTP 422 status code.
The following example shows this error:

```
{"status":"error","errorType":"execution","error":"query timed out - consider simplifying your query"}
```

To reduce evaluation time, use one or more of the following approaches:

- Specify a shorter time window to evaluate fewer samples.
- Add label matchers to reduce the number of series that your query
  evaluates.
- Use [recording rules](AMP-ruler-rulesfile.md "AMP-ruler-rulesfile.md") to precompute
  expensive aggregations that you query frequently.
- Avoid regex matchers on high-cardinality labels (labels with many unique
  values).

For more information, see [Query your Prometheus metrics](AMP-query.md "AMP-query.md").
