# Design principles

Several strategies help reduce costs when running high performance
computing (HPC) workloads in the cloud such as:

- **Find your desired
  price-for-performance configuration:** Many HPC
  workloads are part of a data processing pipeline that includes
  multiple steps. These will vary depending on the workload and
  often include; data transfer in, pre-processing, computational
  calculations, post-processing and data transfer out. In the
  cloud, rather than on a large and expensive server, the
  computing platform can be optimized at each step. For example,
  if a single step in an HPC workflow pipeline requires a large
  amount of memory such as mesh or grid generation, you only
  need to pay for a more expensive large-memory server for the
  memory-intensive application. Other parts of the workflow
  should be similarly deployed on EC2 or storage configurations
  best suited for that job. When comparing different
  configurations, think about the cost as well as the
  performance.
- **Burst workloads in the most efficient
  way:** Savings are obtained for HPC workloads through
  horizontal scaling in the cloud. When scaling horizontally,
  many jobs or iterations of an entire workload are run
  simultaneously for less total elapsed wall time. Depending on
  the application, horizontal scaling can be cost neutral while
  offering indirect cost savings by delivering results in a
  fraction of the time.
- **Evaluate spot pricing:**
  Amazon EC2 Spot Instances offer spare compute capacity in AWS
  at steep discounts compared to On-Demand instances. However,
  Spot Instances can be interrupted when EC2 needs to reclaim
  the capacity. Spot Instances are frequently the most
  cost-effective resource for flexible or fault-tolerant
  workloads. The intermittent nature of HPC workloads makes them
  well suited to Spot Instances. The risk of Spot Instance
  interruption can be minimized by working with the Spot
  Advisor, and the interruption impact can be mitigated by
  changing the default interruption behavior and using Spot
  Fleet to manage your Spot Instances. The need to occasionally
  restart a workload is easily offset by the cost savings of
  Spot Instances. Some HPC workloads can be checkpointed and
  resumed, this can make spot a very good fit.
- **Assess the trade-off of cost versus
  time**: Tightly coupled, massively parallel workloads
  are able to run on a wide range of core counts. For these
  workloads, the scaling or parallel efficiency of a case falls
  off at higher core counts. Curves are specific to the workload
  (model size, application, solver algorithm, IO, user defined
  functions) as scaling depends significantly on the ratio of
  computational load to non-parallelizable components of the
  solve time (network latency, serial operations, and other
  blocking functions). Larger models are generally capable of
  scaling further than smaller models. Running on less cores is
  generally more cost efficient than running on more cores, at
  the cost of increasing turnaround-time. With an understanding
  of the cost versus turnaround-time tradeoff, the most
  appropriate scaling can be used.

For example, if a job is being submitted over the weekend and
the results needed on Monday, there is no value in running on
more cores with a lower parallel efficiency and incurring extra
costs to get the results ready by Saturday morning.
Alternatively, if the results of a calculation are in the
critical path of releasing a new product, reducing the
time-to-solution to allow for more design iteration or result
analysis may be very worthwhile. In addition, consider software
licenses when thinking about overall cost. Some licenses can be
expensive, and it may be overall more cost effective to run your
workload less efficiently to reduce turnaround time and
licensing cost.

- **Choose Region based on workloads
  requirements and cost goals:** AWS has many regions
  around the world. Capabilities vary between different regions.
  For example, some instance types may not be available in all
  regions, moving your calculations to a different region might
  allow the use of a more efficient instance type or storage
  configuration. Costs can also vary between different regions.
  In some cases, you may have regulatory or legal requirements
  that restrict choice of the regions you can use. In other
  cases, you may be free to use resources anywhere in the world.
  Balance the complexity of running in multiple regions with
  cost savings.
