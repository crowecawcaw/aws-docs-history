# Design principles

Consider the following design principles when building an HPC
workload in the cloud:

- **Use dynamic architectures**:
  Avoid defaulting to static architectures and cost estimates that
  use a steady-state model. Your architecture can be dynamic,
  growing and shrinking to match your HPC demands over time. Match
  your architecture design and cost management explicitly to the
  natural cycles of HPC activity.
- **Align the procurement model to the
  workload**: AWS makes a range of compute procurement
  models, such as on-demand and savings plans, available for
  different HPC demand patterns. By selecting the correct model,
  you only pay for what you need. You can potentially combine
  models for a committed rate while having burst capacity with
  on-demand compute.
- **Consider your data**:
  Understand your data before you begin designing your
  architecture. Consider your data's location, size, update, and
  regulatory requirements. A holistic optimization of performance
  and cost focuses on compute and includes data considerations.
  Your data requirements may shape optimal performance based on
  available resources in your selected Regions.
- **Automate with infrastructure as
  code:** Consider products, such as AWS ParallelCluster
  and AWS Research and Engineering Studio, to ease your effort in
  automating your infrastructure. Alternatively, you can customize
  your infrastructure with services, such as AWS CloudFormation,
  if needed but plan for a higher development effort.
- **Collaborate securely**: HPC
  work often occurs in a collaborative context and is usually part
  of a larger workflow. Take full advantage of the security and
  collaboration features that make AWS an excellent environment
  for you and your collaborators to solve your HPC problems. For
  example, you can grant cross-account access to share a full or
  partial data set with Amazon S3 to another AWS account. This
  helps your computing solutions and datasets achieve a greater
  impact by securely sharing within a selective group or publicly
  sharing with the broader community. When collaborating, consider
  data locality and workflow architecture. For example, use remote
  visualization with Amazon DCV rather than transferring data to
  users.
- **Use designs built for the
  cloud**: Directly replicating your on-premises
  architecture is usually unnecessary and suboptimal when
  migrating workloads to AWS. Consider the breadth and depth of
  AWS services to create new design patterns with solutions that
  are built for cloud architectures*.* For
  example, in the cloud, each user or group can use a separate
  cluster, which can independently scale depending on the load.
- **Test real-world workloads**:
  You only pay for what you actually use with AWS, which makes it
  possible to create a realistic proof-of-concept with your own
  representative models. Most HPC applications are complex, and
  their memory, CPU, and network patterns often can't be reduced
  to simplified microbenchmarks or theoretical performance
  benchmarks. With AWS, you can quickly get started, iterate, and
  optimize your design with only paying for consumed resources as
  you finalize your architecture.
- **Balance your desired price and time-to-results**: Use time
  and cost to analyze performance. Sometimes you can prioritize reducing cost when you do not
  immediately require results. For time-critical workloads, consider trading cost optimization
  for faster time-to-results. Determine your desired price-for-performance approach based on
  your results timeline and available budget.
