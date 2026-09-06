

# Throughput and data freshness
<a name="msk-data-delivery-s3-bp-throughput"></a>
+ Set a Amazon CloudWatch alarm on `DataFreshness` to detect when freshness degrades beyond your configured interval.
+ You can configure multiple Channels to read from the same topic without consuming broker throughput.