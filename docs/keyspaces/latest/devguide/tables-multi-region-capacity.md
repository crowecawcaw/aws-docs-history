# Estimate and provision capacity for a multi-Region table in Amazon Keyspaces

You can configure the throughput capacity of a multi-Region table in one of two ways:

- On-demand capacity mode, measured in write request units (WRUs)
- Provisioned capacity mode with auto scaling, measured in write capacity units
  (WCUs)
  You can use provisioned capacity mode with auto scaling or on-demand capacity mode to
  help ensure that a multi-Region table has sufficient capacity to perform replicated
  writes to all AWS Regions.

###### Note

Changing the capacity mode of the table in one of the Regions changes the capacity
mode for all replicas.

By default, Amazon Keyspaces uses on-demand mode for multi-Region tables. With on-demand mode,
you don't need to specify how much read and write throughput that you expect your
application to perform. Amazon Keyspaces instantly accommodates your workloads as they ramp up or
down to any previously reached traffic level. If a workload’s traffic level hits a new
peak, Amazon Keyspaces adapts rapidly to accommodate the workload.

If you choose provisioned capacity mode for a table, you have to configure the number
of read capacity units (RCUs) and write capacity units (WCUs) per second that your
application requires.

To plan a multi-Region table's throughput capacity needs, you should first estimate
the number of WCUs per second needed for each Region. Then you add the writes from all
Regions that your table is replicated in, and use the sum to provision capacity for each
Region. This is required because every write that is performed in one Region must also
be repeated in each replica Region.

If the table doesn't have enough capacity to handle the writes from all Regions,
capacity exceptions will occur. In addition, inter-Regional replication wait times will
rise.

For example, if you have a multi-Region table where you expect 5 writes per second in
US East (N. Virginia), 10 writes per second in US East (Ohio), and 5 writes per second
in Europe (Ireland), you should expect the table to consume 20 WCUs in each Region:
US East (N. Virginia), US East (Ohio), and Europe (Ireland). That means that in this
example, you need to provision 20 WCUs for each of the table's replicas. You can monitor
your table's capacity consumption using Amazon CloudWatch. For more information, see [Monitoring Amazon Keyspaces with Amazon CloudWatch](monitoring-cloudwatch.md "monitoring-cloudwatch.md").

Each write is billed as 1 WCU, so you would see a total of
60 WCUs billed in this example. For more information about pricing, see [Amazon Keyspaces (for Apache Cassandra) pricing](https://aws.amazon.com/keyspaces/pricing "https://aws.amazon.com/keyspaces/pricing").

For more information about provisioned capacity with Amazon Keyspaces auto scaling, see [Manage throughput capacity automatically with Amazon Keyspaces auto scaling](autoscaling.md "autoscaling.md").

###### Note

If a table is running in provisioned capacity mode with auto scaling, the
provisioned write capacity is allowed to float within those auto scaling settings
for each Region.
