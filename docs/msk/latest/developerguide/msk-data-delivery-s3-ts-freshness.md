

# Data freshness higher than configured
<a name="msk-data-delivery-s3-ts-freshness"></a>
+ **Symptom:** `DataFreshness` is significantly higher than the configured interval.
+ **Causes:** A high number of source partitions; (less commonly) transient service issues or low source throughput.
+ **Resolution:** Verify your partitioning is appropriate for the data and avoid excessive partition cardinality. For low-throughput topics, increasing the configured data freshness gives the Channel more time to accumulate data for efficient delivery.