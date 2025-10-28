# Design principles

The following are sustainability design principles to frame your
AWS workload:

- **Maximize utilization and reduce the
  downstream impact of your workloads:** HPC computing
  nodes are ephemeral in the cloud, you do not need to keep your
  computing nodes always up and running. Start the computing
  nodes only when you need to run a job and terminate the
  instances as soon as the job is completed to minimize the
  carbon emissions. Do not duplicate your data by copying the
  results back to your on-premises data center, unless there is
  a business need to store a local copy. Intermediate data
  should be removed when no longer needed

- **Anticipate and adopt new and more
  efficient hardware and software and use managed
  services:** HPC workloads aggregate computing power
  and storage to allow for fast processing and calculation to
  solve scientific, mathematical, and engineering challenges.
  Due to its scale, HPC is more energy-intensive than general
  purpose computing. Therefore, better use of resources, both
  hardware and software, coupled with shorter runtimes, means
  improving utilization and environmental sustainability.
  Since the impact of HPC is so relevant to help you achieve your sustainability goals, it
  is important to promote a culture of constant monitoring and improvement for this workload.
  HPC clusters on-premises usually have a life cycle that can spans years during which they are
  rarely updated. When running HPC in the cloud, leaders need to promote a culture of continuous
  innovation. This will help to improve performance, reduce cost and improve sustainability. To
  continually improve and streamline your HPC workloads, you can automate your cluster
  deployment using CI/CD pipelines to easily test and deploy potential performance improvements
  and limit errors caused by manual processes. Prefer AWS Managed Services such as AWS ParallelCluster or
  AWS Batch to automate the provisioning and de-provisioning of the computing nodes. Continually
  monitor the release of new instance types and take advantage of energy efficiency
  improvements, including those instance types designed to support specific workloads such as
  machine learning training and inference.
