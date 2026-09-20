

# How CloudWatch stores histogram metrics
<a name="metrics-otel-histograms"></a>

Histogram metrics describe the distribution of many measurements, such as request latency or payload size, instead of a single value. OpenTelemetry defines two histogram types, and Amazon CloudWatch (CloudWatch) stores both as exponential histograms:
+ **Explicit-bucket histograms** – also called fixed-boundary histograms. You choose the bucket boundaries in advance, and every measurement is counted into the bucket that contains it. This is the default aggregation for the `Histogram` instrument in most OpenTelemetry SDKs, and it is the format that Prometheus classic histograms use.
+ **Exponential histograms** – the bucket boundaries follow an exponential scale rather than a fixed list, so bucket width grows with the magnitude of the value. This gives consistent relative resolution across a wide range of values without you having to choose boundaries.

CloudWatch stores exponential histograms directly. It might reduce the scale of a histogram, which merges adjacent buckets and lowers resolution while preserving the total count and sum. The OpenTelemetry specification allows this, and any consumer of exponential histograms can do it. For more information, see [ExponentialHistogram](https://opentelemetry.io/docs/specs/otel/metrics/data-model/#exponentialhistogram) in the OpenTelemetry metrics data model.

When you send an explicit-bucket histogram, CloudWatch converts it to an exponential histogram at ingestion. This is a different operation from a scale reduction: the two formats describe the same distribution with different buckets, so the conversion has to place the counts from each source bucket into the exponential buckets that cover the same range of values.

## What the conversion preserves
<a name="metrics-otel-histograms-conversion"></a>

The following values are carried through the conversion exactly, and queries against them return the same result they would for the source histogram:
+ **Count** – the total number of recorded measurements.
+ **Sum** – the sum of the recorded values. Because count and sum are both exact, the average is also exact.
+ **Minimum and maximum** – when the source histogram carries them. Both fields are optional in OpenTelemetry, and not every SDK and exporter records them, so they aren't always available. When they are missing, CloudWatch doesn't estimate them.

Percentiles are the exception. A percentile read from a histogram of any kind is an estimate, because the histogram records how many measurements fell in each bucket but not the individual values. That is true of the source explicit-bucket histogram before any conversion takes place.

## How counts are redistributed
<a name="metrics-otel-histograms-redistribution"></a>

To place a source bucket's count into exponential buckets, CloudWatch subdivides the range that the source bucket covers. It then distributes the count across those subdivisions, weighting them by how the density of measurements compares with neighboring buckets instead of spreading them evenly.

**Note**  
Estimating a percentile directly from an explicit-bucket histogram – for example, with `histogram_quantile()` in Prometheus – interpolates linearly within the bucket that contains the percentile. This approach assumes that measurements are spread evenly across that bucket. Long-tailed distributions such as latency usually violate that assumption, so this is a known source of error in percentile estimates from explicit-bucket histograms. For more information, see [`histogram_quantile()`](https://prometheus.io/docs/prometheus/latest/querying/functions/#histogram_quantile) in the Prometheus documentation.

## What limits percentile accuracy
<a name="metrics-otel-histograms-accuracy"></a>

How closely an estimated percentile matches the true value depends mostly on the source histogram, not on the conversion. Once measurements are counted into a bucket, their individual values are gone, and no conversion can recover them. Accuracy is therefore best when your bucket boundaries are narrow across the range where your measurements actually fall.

Estimates are least accurate in these cases:
+ **Wide buckets** – a percentile that falls inside a wide bucket can only be located somewhere within that bucket's range.
+ **The unbounded top bucket** – the last bucket of an explicit-bucket histogram has no upper boundary. High percentiles that fall into this bucket are therefore the least constrained. This matters most for tail latency, where the values you care about are the ones above your highest boundary. If your SDK can record a minimum and maximum, enable it: the bucket counts alone don't capture the true extremes, and CloudWatch preserves those two values when they're present.
+ **Boundaries that don't match your data** – if most measurements land in one or two buckets, the histogram carries little information about the distribution regardless of how many buckets you defined.

If you rely on percentiles, configure your OpenTelemetry SDK to use exponential bucket aggregation for your `Histogram` instruments instead of the default explicit buckets. This avoids the redistribution described earlier, and you don't have to predict the range of your measurements in advance. For more information, see [Base2 Exponential Bucket Histogram Aggregation](https://opentelemetry.io/docs/specs/otel/metrics/sdk/#base2-exponential-bucket-histogram-aggregation) in the OpenTelemetry documentation.

## Querying histogram metrics
<a name="metrics-otel-histograms-querying"></a>

You query histograms in CloudWatch with the same [PromQL](CloudWatch-PromQL-Querying.md) histogram functions regardless of which format you sent. To estimate a percentile, use `histogram_quantile()`; to get the exact average, use `histogram_avg()`. For example, the following query returns the estimated 95th percentile of request duration:

```
histogram_quantile(0.95, http_request_duration_seconds)
```

For more information about querying metrics with PromQL, see [PromQL querying](CloudWatch-PromQL-Querying.md).