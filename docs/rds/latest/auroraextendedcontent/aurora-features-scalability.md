

# Scalability
<a name="aurora-features-scalability"></a>

**Topics**
+ [Serverless](#aurora-features-serverless)
+ [Automated horizontal scaling](#aurora-features-horizontal-scaling)
+ [Push-button compute scaling](#aurora-features-compute-scaling)
+ [Storage auto scaling](#aurora-features-storage-scaling)
+ [Low-latency read replicas](#aurora-features-read-replicas)
+ [Custom database endpoints](#aurora-features-custom-endpoints)

## Serverless
<a name="aurora-features-serverless"></a>

[Aurora serverless](https://aws.amazon.com/rds/aurora/serverless/) is an on-demand, auto-scaling configuration that automatically starts up, shuts down, and vertically scales capacity up or down based on your application's needs, so you never have to manage database capacity manually. You specify a capacity range in Aurora Capacity Units (ACUs), and Aurora scales within that range. When your database is idle, Aurora will automatically scale down to zero, so you only pay when your database is in use. It's especially well-suited for agentic AI applications, which typically have bursts of activity, long idle windows, and unpredictable patterns. You can also use Aurora serverless alongside with provisioned instances in your existing or new database clusters for a mixed-configuration approach.

## Automated horizontal scaling
<a name="aurora-features-horizontal-scaling"></a>

[Aurora PostgreSQL Limitless Database](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/limitless.html) horizontally scales beyond the write throughput and storage limits of the largest single instance while maintaining transactional consistency. Your database automatically scales based on the workload, and you only pay for what you use. In only a few steps in the [RDS Management Console](https://console.aws.amazon.com/rds/home) or [AWS CLI](https://aws.amazon.com/cli/), you can create a new Limitless Database cluster. Additional information is available in [Aurora PostgreSQL Limitless Database requirements and considerations](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/limitless-reqs-limits.html) documentation.

## Push-button compute scaling
<a name="aurora-features-compute-scaling"></a>

Aurora lets you scale provisioned instances using the RDS APIs or the [RDS Management Console](https://console.aws.amazon.com/console/home), and compute scaling operations typically complete in a few minutes.

## Storage auto scaling
<a name="aurora-features-storage-scaling"></a>

Aurora automatically scales I/O to match the needs of your most demanding applications and increases the size of your database volume as your storage needs grow. Your database volume expands in increments of 10 GB up to a maximum of 256 TiB so you never need to provision excess storage in advance. When using Aurora I/O-Optimized configuration, you can save up to 40% when I/O spend exceeds 25% of your Aurora database spend. Additional information is available in [Aurora storage and reliability](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/Aurora.Overview.StorageReliability.html) documentation.

## Low-latency read replicas
<a name="aurora-features-read-replicas"></a>

You can create up to 15 [read replicas](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/Aurora.Replication.html) to increase read throughput without impacting performance on the primary instance. Aurora read replicas share the same underlying storage as the primary instance, lowering costs and avoiding the need to perform writes at the replica nodes. This frees up more processing power to serve read requests and reduces the replica lag time—often down to single-digit milliseconds.

Aurora provides a reader endpoint for automatic connection routing and load balancing across read replicas and supports [auto scaling](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/Aurora.Integrating.AutoScaling.html) to add and remove replicas based on your performance metrics settings. The application can connect without having to keep track of replicas as they are added and removed. Aurora also supports cross-Region read replicas, which provide fast local reads to your users, and each Region can have an additional 15 Aurora read replicas to further scale local reads.

## Custom database endpoints
<a name="aurora-features-custom-endpoints"></a>

Custom endpoints allow you to distribute and load balance workloads across different sets of database instances. For example, you can provision a set of Aurora read replicas to use an instance type with higher memory capacity in order to run an analytics workload while keeping other instances isolated for transactional traffic.