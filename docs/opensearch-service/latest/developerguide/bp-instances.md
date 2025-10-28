# Choosing instance types and testing

After you calculate your storage requirements and choose the number of shards that
you need, you can start to make hardware decisions. Hardware requirements vary
dramatically by workload, but we can still offer some basic recommendations.

In general, [the storage limits](limits.md "limits.md") for each instance
type map to the amount of CPU and memory that you might need for light workloads.
For example, an `m6g.large.search` instance has a maximum EBS volume size
of 512 GiB, 2 vCPU cores, and 8 GiB of memory. If your cluster has many shards,
performs taxing aggregations, updates documents frequently, or processes a large
number of queries, those resources might be insufficient for your needs. If your
cluster falls into one of these categories, try starting with a configuration closer
to 2 vCPU cores and 8 GiB of memory for every 100 GiB of your storage
requirement.

###### Tip

For a summary of the hardware resources that are allocated to each instance
type, see [Amazon OpenSearch Service
pricing](https://aws.amazon.com/opensearch-service/pricing/ "https://aws.amazon.com/opensearch-service/pricing/").

Still, even those resources might be insufficient. Some OpenSearch users report
that they need many times those resources to fulfill their requirements. To find the
right hardware for your workload, you have to make an educated initial estimate,
test with representative workloads, adjust, and test again.

## Step 1: Make an initial estimate

To start, we recommend a minimum of three nodes to avoid potential OpenSearch
issues, such as a _split brain_ state (when a
lapse in communication leads to a cluster having two master nodes). If you have
three [dedicated master
nodes](managedomains-dedicatedmasternodes.md "managedomains-dedicatedmasternodes.md"), we still recommend a minimum of two data nodes for
replication.

## Step 2: Calculate storage requirements per

node

If you have a 184-GiB storage requirement and the recommended minimum number
of three nodes, use the equation 184 / 3 = 61 GiB to find the amount of storage
that each node needs. In this example, you might select three
`m6g.large.search` instances, where each uses a 90-GiB EBS
storage volume, so that you have a safety net and some room for growth over
time. This configuration provides 6 vCPU cores and 24 GiB of memory, so it's
suited to lighter workloads.

For a more substantial example, consider a 14 TiB (14,336 GiB) storage
requirement and a heavy workload. In this case, you might choose to begin
testing with 2 \* 144 = 288 vCPU cores and 8 \* 144 = 1152 GiB of memory. These
numbers work out to approximately 18 `i3.4xlarge.search` instances.
If you don't need the fast, local storage, you could also test 18
`r6g.4xlarge.search` instances, each using a 1-TiB EBS storage
volume.

If your cluster includes hundreds of terabytes of data, see [Petabyte scale in Amazon OpenSearch Service](petabyte-scale.md "petabyte-scale.md").

## Step 3: Perform representative testing

After configuring the cluster, you can [add your
indexes](indexing.md "indexing.md") using the number of shards you calculated earlier, perform
some representative client testing using a realistic dataset, and [monitor CloudWatch metrics](managedomains-cloudwatchmetrics.md "managedomains-cloudwatchmetrics.md") to see
how the cluster handles the workload.

## Step 4: Succeed or iterate

If performance satisfies your needs, tests succeed, and CloudWatch metrics are
normal, the cluster is ready to use. Remember to [set CloudWatch alarms](cloudwatch-alarms.md "cloudwatch-alarms.md") to detect unhealthy
resource usage.

If performance isn't acceptable, tests fail, or `CPUUtilization` or
`JVMMemoryPressure` are high, you might need to choose a
different instance type (or add instances) and continue testing. As you add
instances, OpenSearch automatically rebalances the distribution of shards
throughout the cluster.

Because it's easier to measure the excess capacity in an overpowered cluster
than the deficit in an underpowered one, we recommend starting with a larger
cluster than you think you need. Next, test and scale down to an efficient
cluster that has the extra resources to ensure stable operations during periods
of increased activity.

Production clusters or clusters with complex states benefit from [dedicated master nodes](managedomains-dedicatedmasternodes.md "managedomains-dedicatedmasternodes.md"),
which improve performance and cluster reliability.
