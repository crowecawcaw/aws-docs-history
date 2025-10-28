# Limitations

The following are limitations for the Pipedrive connector:

- Pipedrive supports field based partitioning for only one entity (Activities).
- Pipedrive supports record based partitioning for Activities, Deals, Notes, Persons, Organizations and Products entities.
- In Deals entity, status field as filter will returned all record if invalid value filter value is used.
- In Deals entity, ordering with multiple fields is not supported.
- To obtain performance data, we utilize a local AWS account. However, due to the limitation of refreshing the access token
  locally, the AWS Glue job for processing 1 GB of data is failing. Consequently, we have optimized the performance test with 179 MB of data, and
  the above results are based on this optimization. Nevertheless, we have observed that with an increasing number of partitions, the SaaS endpoint
  is taking more time compared to a single partition. We have consulted with the Pipedrive support team regarding this behavior, and they
  informed us that Pipedrive is silently throttling requests and delaying the response. Therefore, when running the AWS Glue job with large datasets
  or calling the same API endpoint multiple times, it may result in a timeout issue due to Pipedrive API's implementation. However, the connector
  and shim response times are decreasing as expected with an increase in the number of partitions.
