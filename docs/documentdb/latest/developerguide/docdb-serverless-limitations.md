# Requirements and limitations for DocumentDB serverless

## Feature requirements

### Region availability

The Amazon DocumentDB serverless instance type is available in the following regions:

The following AWS CLI command can be used to verify the exact DocumentDB serverless instance options offered in a particular region:

```
aws docdb describe-orderable-db-instance-options \
        --region `my_region` \
        --db-instance-class db.serverless \
        --engine docdb
```

### Engine version availability

DocumentDB serverless is supported by Amazon DocumentDB 5.0.0 engine version.

###### Note

DocumentDB serverless is supported only on newer patch versions of 5.0.0.
Please ensure that your cluster is updated to a recent engine patch version.
For more information on maintaining Amazon DocumentDB clusters, see [Maintaining Amazon DocumentDB](db-instance-maintain.md "db-instance-maintain.md")

### Cluster configuration

Before adding any Amazon DocumentDB serverless instances to an Amazon DocumentDB cluster, the cluster must also have the `ServerlessV2ScalingConfiguration` parameter set.
This defines the capacity range of DocumentDB serverless instances in the cluster.
For more information on scaling configuration, see [Amazon DocumentDB serverless scaling configuration](docdb-serverless-scaling-config.md "docdb-serverless-scaling-config.md").

### Minimum scaling capacity range settings for certain Amazon DocumentDB features

Some Amazon DocumentDB features work with DocumentDB serverless, but might cause issues if your capacity range is lower than needed for the memory requirements for those features with your specific workload.
In that case, your database might not perform as well as usual, or might encounter out-of-memory errors.

The following features require configuration of a higher `MinCapacity` and/or `MaxCapacity` value for best operation:

- Performance Insights
- Serverless instance creation on a cluster with a large data volume

This includes serverless instance creation as part of a cluster restore.

For recommendations about setting the appropriate capacity range (if you are using this feature), see [Choosing the scaling capacity range for a DocumentDB serverless cluster](docdb-serverless-scaling-config.md#docdb-serverless-scaling-capacity-choosing "docdb-serverless-scaling-config.md#docdb-serverless-scaling-capacity-choosing").
For troubleshooting information if your database encounters out-of-memory errors due to a misconfigured capacity range, see [Avoiding out-of-memory errors](docdb-serverless-scaling-config.md#docdb-serverless-scaling-mem-errors "docdb-serverless-scaling-config.md#docdb-serverless-scaling-mem-errors").

## Feature limitations

The following features from Amazon DocumentDB provisioned instances are not available for DocumentDB serverless instances:

- Global clusters
