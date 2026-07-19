# Understand the cost model for service-managed fleets

AWS Deadline Cloud service-managed fleets (SMFs) with job attachments have a fundamentally different
cost structure than traditional on-premises render farms or customer-managed fleets that use
network file systems. Understanding this difference helps you plan budgets, optimize
spending, and take advantage of elastic scaling without unexpected costs.

## Traditional render farm costs

On a traditional render farm, costs come from two main areas:

- **File storage** – A high-performance
  network file system (NFS or SAN) is required to serve assets to every worker
  simultaneously. The cost of this storage scales with the throughput it must
  support, which indirectly limits how many workers the farm can scale to.
- **Compute** – Workers (render nodes) are
  provisioned and maintained regardless of how much work is in the queue. Idle
  workers still incur hardware, power, and cooling costs.
- **Farm management** – A traditional farm
  also requires infrastructure and staff time for the render farm scheduler, its
  job database, software configuration, monitoring and reporting, and ongoing
  maintenance and upgrades.

Because the file system must be provisioned to handle peak throughput, scaling the
farm up and down is expensive and slow. Adding more workers requires additional file
system capacity, and that capacity cannot be released when workers are idle.

## How service-managed fleet costs differ

With service-managed fleets, costs are structured differently:

Compute (worker time)

You pay for EC2 instances only while they are processing jobs. There is no
cost to provision or decommission workers. When the fleet scales to zero
workers, your compute cost drops to zero. For more information about
pricing, see [AWS Deadline Cloud
pricing](https://aws.amazon.com/deadline-cloud/pricing/ "https://aws.amazon.com/deadline-cloud/pricing/").

Storage (Amazon EBS)

Each worker uses a local Amazon Elastic Block Store (Amazon EBS) volume. Deadline Cloud charges for
Amazon EBS storage only while the worker instance exists. The storage cost is
included in the Deadline Cloud service-managed fleet pricing.

Farm management

The scheduler, job database, fleet scaling, monitoring, and maintenance
are part of the Deadline Cloud service. There is no separate infrastructure to run or
maintain for farm management.

File transfer (job attachments)

Job attachments use Amazon Simple Storage Service (Amazon S3) to transfer files between your
workstation and workers. There is no charge for throughput or bytes
transferred between Amazon S3 and workers. The cost is based primarily on the
amount of data stored in Amazon S3. Amazon S3 API request fees apply for file uploads
and downloads but are typically not a significant cost driver. For more
information about Amazon Simple Storage Service pricing, see [Amazon Simple Storage Service pricing](https://aws.amazon.com/s3/pricing/ "https://aws.amazon.com/s3/pricing/").

###### Note

There is no high-performance file system to provision or maintain. Job
attachments throughput is virtually unlimited, scales automatically with the number
of workers, and requires no capacity planning.

## Why auto scaling is cost efficient with service-managed fleets

Because there is no fixed storage infrastructure to provision, SMFs can scale up and
down freely without incurring additional overhead. This changes how you think about fleet
sizing:

- **Scale up aggressively** – When a large job
  arrives, the fleet can grow to hundreds of workers. Each additional worker
  accesses job attachments in Amazon S3 without placing additional load on a shared file
  system.
- **Scale down to zero** – When work
  completes, the fleet can shrink to zero workers with no ongoing compute or
  storage cost (only Amazon S3 storage for cached assets).
- **Burst for deadlines** – Temporarily
  spinning up a large fleet to meet a deadline adds compute cost proportional to
  the duration, with no penalty for the scale.

For information about configuring auto scaling, see [Auto scaling configuration](auto-scaling-configuration.md "auto-scaling-configuration.md").

## Cost components at a glance

The following table summarizes where costs come from when using SMFs with job
attachments.

| Cost component                       | What drives the cost                                                      | How to optimize                                                                 |
| ------------------------------------ | ------------------------------------------------------------------------- | ------------------------------------------------------------------------------- |
| Amazon EC2 compute                   | Worker running time × instance size                                       | Use Spot Instances, right-size instance types, reduce task<br>duration          |
| Amazon EBS storage                   | Volume size × worker running time, plus IOPS/throughput<br>above baseline | Use the default volume size unless workloads need more local<br>space           |
| Amazon S3 storage (job attachments)  | Total bytes stored in the job attachments bucket                          | Apply an Amazon S3 Lifecycle policy to delete old assets<br>automatically       |
| Amazon S3 requests (job attachments) | Number of PUT and GET requests during upload and download                 | Typically not a significant cost driver; no action<br>needed for most workloads |
| Usage-based licensing (optional)     | License type × instance size × job duration                               | Use only for jobs that require the licensed software                            |
| Amazon CloudWatch Logs (optional)    | Volume of worker and task logs collected                                  | Reduce log verbosity, set retention policies                                    |

## Example: Comparing service-managed fleet costs to a traditional farm

Consider a project that renders 1,000 frames with an average render time of 20
minutes per frame, using workers with at least 16 vCPUs. The total input asset size is
50 GB.

Traditional farm approach

You maintain a network file system provisioned for the throughput required
by your peak worker count. The file system costs the same whether the farm
is idle or running at full capacity. Adding workers beyond the file system's
throughput limit requires an expensive upgrade.

SMF with job attachments approach

Workers scale up to process all frames and then scale down to zero. Each
worker downloads only the assets it needs from Amazon S3. Your costs are:

- **Compute**: ~333 worker-hours
  (1,000 frames × 20 minutes) at the applicable
  instance rate.
- **Amazon S3 storage**: 50 GB of assets
  stored at standard Amazon S3 rates (a few dollars per month).
- **Amazon S3 requests**: A small number of
  GET requests as workers download assets (fractions of a cent per
  1,000 requests).

When the job finishes, costs return to the Amazon S3 storage charge only.
There is no ongoing file system cost.

For additional pricing examples, see AWS Deadline Cloud pricing.

## Tips for managing service-managed fleet costs

- **Use Spot Instances** – Spot Instances
  provide significant savings over On-Demand pricing. Because render tasks are
  typically short and can be retried, Spot interruptions have minimal impact.
- **Set fleet maximum size** – Limit the
  maximum number of workers in your fleet to control the peak compute cost per job.
  For more information, see [Auto scaling configuration](auto-scaling-configuration.md "auto-scaling-configuration.md").
- **Use budgets** – Create an Deadline Cloud budget to
  set spending limits and receive notifications. For more information, see [Control costs with a budget](using-budget-manager.md "using-budget-manager.md").
- **Manage job attachment storage** – Apply an
  Amazon S3 Lifecycle configuration to automatically delete old job attachment files.
  Because job attachments uses content-addressable storage, unchanged files are not
  re-uploaded, which keeps storage costs low for iterative workflows.
- **Right-size your instances** – Choose the
  smallest instance type that meets your workload's CPU and memory requirements.
  Larger instances cost more per hour but may complete tasks faster, so compare
  total cost (rate × duration) across instance sizes.
- **Consider Wait and Save** – For
  non-urgent workloads, Wait and Save offers lower compute prices in exchange for
  flexible job start times.

## Related resources

- [AWS Deadline Cloud
  pricing](https://aws.amazon.com/deadline-cloud/pricing/ "https://aws.amazon.com/deadline-cloud/pricing/")
- [Cost management](cost-management.md "cost-management.md")
- [Control costs with a budget](using-budget-manager.md "using-budget-manager.md")
- [Amazon Simple Storage Service
  pricing](https://aws.amazon.com/s3/pricing/ "https://aws.amazon.com/s3/pricing/")
