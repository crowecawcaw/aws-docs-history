# AOSPERF06-BP01 Identify index refresh controls for optimal

ingestion performance

Improve indexing throughput and speed by adjusting the
refresh_interval value to more than 30 seconds.

**Level of risk exposed if this best practice
is not established:** Medium

**Desired outcome**: The
refresh_interval value is set to more than 30 seconds, which could
potentially lead to increased indexing throughput and faster
indexing speeds.

**Benefits of establishing this best
practice:** By adjusting the `refresh_interval`, you can
optimize index write performance, as less frequent refreshes allow
for more efficient ongoing writes which usually results as faster
indexing speeds.

## Implementation guidance

A refresh operation makes all updates to an index accessible for
search. The default refresh interval is one second, indicating
that OpenSearch Service performs a refresh every second during ongoing
index writes.

### Implementation steps

- Check the current `refresh_interval` value for your index.

```
GET /<index-name>/_settings/index.refresh_interval
```

- Change the `refresh_interval` value to 30s or more

```
PUT /sample_data/_settings
        {
        "index" : {
        "refresh_interval" : "30s"
        }
        }
```

- It is also possible to disable the automatic refreshes by setting
  `refresh_interval": "-1"`
- If the `refresh_interval` is disabled, you can manually
  refresh an index running `POST <index-name>/_refresh`.
- If you're loading new data into your domain through a batch
  process, it might be beneficial to disable the automatic
  refresh just before the batch process begins, and re-enable
  it after the process concludes.

## Resources

- [Optimize
  OpenSearch Refresh Interval](https://opensearch.org/blog/optimize-refresh-interval/ "https://opensearch.org/blog/optimize-refresh-interval/")
