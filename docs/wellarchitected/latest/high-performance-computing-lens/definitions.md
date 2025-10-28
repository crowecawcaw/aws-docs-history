# Definitions

The AWS Well-Architected Framework is based on six pillars:
operational excellence, security, reliability, performance
efficiency, cost optimization, and sustainability. When architecting
solutions, you make tradeoffs between pillars based upon your
business context. These business decisions can drive your
engineering priorities. You might reduce cost at the expense of
reliability in development environments, or for mission-critical
solutions, you might improve reliability with increased costs.
Security and operational excellence are generally not traded off
against other pillars.

- **HPC workloads**: HPC users
  commonly speak of jobs. AWS refers to these as workloads.
- **Loosely coupled**: Loosely
  coupled workloads typically see a large number of small jobs
  working independently of one another. This is sometimes referred
  to as high-throughput computing (HTC).
- **Tightly coupled**: Tightly coupled workloads, such as [Computational Fluid Dynamics on AWS](../../../whitepapers/latest/computational-fluid-dynamics-on-aws/computational-fluid-dynamics-on-aws.md "../../../whitepapers/latest/computational-fluid-dynamics-on-aws/computational-fluid-dynamics-on-aws.md") and weather forecasting, have multi-threaded
  or multi-core processes working together. For additional information on these use cases, see
  the [Tightly Coupled Scenarios](tightly-coupled-scenarios.md "tightly-coupled-scenarios.md").
- **Workload scheduling:** Job
  scheduling is a means of queuing multiple jobs up to be
  processed (either sequentially or concurrently depending on
  compute resources available). Several industry-standard HPC job
  schedulers are available with AWS services, such as Slurm with
  AWS ParallelCluster, as well as AWS Partner Independent Software
  Vendors (ISVs) offerings. Job scheduling can also be defined
  using serverless algorithm design.
- **Compute vCPUs:** HPC users may
  refer to a server as a node while AWS refers to a virtual server
  as an Amazon EC2 instance. AWS names and sizes instances based
  on the available resources allocated to the instances, such as
  the number of vCPUs. Depending on the instance type, a vCPU
  could be a thread through simultaneous multithreading (SMT) or a
  physical CPU core. For instance specifics, see
  [Amazon EC2 instance type specifications](../../../ec2/latest/instancetypes/ec2-instance-type-specifications.md "../../../ec2/latest/instancetypes/ec2-instance-type-specifications.md").
- **Cluster placement group:** A
  cluster placement group is a logical grouping of your compute
  instances within a single Availability Zone (AZ) within the same
  high-bisection bandwidth segment of the network. Cluster
  placement groups provide low latency and high bandwidth between
  your compute instances.
- **Elastic Fabric Adapter:**
  Tightly coupled workloads on AWS often benefit from the use of
  the Elastic Fabric Adapter (EFA) and cluster placement groups.
  EFA is a networking technology that provides lower and more
  consistent latency and higher throughput than the TCP transport
  traditionally used in cloud-based HPC systems. EFA is described
  in more detail in the Networking section.
- **Amazon Machine Image (AMI):** An [Amazon Machine Images in Amazon EC2](../../../AWSEC2/latest/UserGuide/AMIs.md "../../../AWSEC2/latest/UserGuide/AMIs.md") is an image
  that contains the software for an EC2 instance to launch. These are images supported and
  maintained by AWS, as well as Marketplace offerings and the ability for users to create
  their own.
- **Blue/green instances:** A blue/green deployment is a
  strategy whereby two separate, but identical, deployments are created. The blue environment
  runs the current application version while the green environment runs the new application
  version.
- **CI/CD:** Continuous
  Integration and Continuous Development. CI is a set of SW coding
  practices that drive development teams to frequently implement
  small code changes and check them in to a version control
  repository. It establishes an automated way to build, package,
  and test their applications. This encourages developers to
  commit code changes more frequently, leading to better
  collaboration and code quality. CD automates application
  delivery to production, development, and testing environments
  and is an automated way to push code changes to these
  environments.
- **Computational Fluid Dynamics
  (CFD):** This is a form of Computational Aided
  Engineering (CAE) to simulate fluid flows around or within
  objects. It uses a Finite Volume approach to solve numerical
  equations across domains split into many smaller cells in an
  iterative approach. A commonly used example is aerodynamics of
  cars.
- **Data retention requirement:**
  Data management – where and how much data is retained – is a
  significant consideration for HPC environments. User and
  regulatory requirements for data retention should be considered,
  with different strategies possible.
- **EasyBuild:** Third party
  package management software that provides a software build and
  install framework to manage (chiefly scientific) software on
  High Performance Computing (HPC) systems efficiently.
- **Fail fast:** This is a
  philosophy for frequent, incremental, development and testing to
  determine whether a development path is the best one.
- **Finite Element Analysis (FEA):**
  A form of Computational Aided
  Engineering (CAE) that simulates structural analysis. This is
  used for many engineered products such as crash simulation in
  cars or building reaction to earthquakes. This simulation type
  is heavily used in Mechanical Engineering.
- **Genomics:** A branch of study
  that refers to mapping the genetic code of living tissues to
  identify the genetic material and the result of interactions of
  genes with each other and their environment.
- **Hypervisor:** Software
  that allows for the running of multiple virtual machines on a
  single physical machine. AWS use the
  [AWS Nitro
  System](https://aws.amazon.com/ec2/nitro/ "https://aws.amazon.com/ec2/nitro/").
- **IOPS:** Input/output operations per second. This is a
  measure of data throughput on a bus, in a CPU or GPU, or when using a storage device.
- **Job scheduling software:**
  This is software that knows what resources are available and
  allows users to submit work to run on the compute machines. If
  all resources are busy, jobs are queued up until the required
  resources are available.
- **Lazy load:** When data in an S3 bucket linked to a Data
  Repository Association (for FSx for Lustre) is accessed, Amazon
  File Cache automatically loads the metadata and file contents if
  they are not already present in the cache.
  [Lazy
  load](../../../fsx/latest/FileCacheGuide/mdll-lazy-load.md "../../../fsx/latest/FileCacheGuide/mdll-lazy-load.md") allows reading or writing data or metadata to files
  in a DRA directory.
- **Luigi:** A lightweight,
  open-sourced, Python-based workflow scheduler that is typically
  used for orchestrating data assets in the Hadoop ecosystem.
- **Memory to Core Ratio:** A
  compute machine has a physical amount of Random Access Memory
  (RAM) available as well as number of cores. By dividing RAM by
  core count it is possible to determine the amount of RAM per
  core available. If the machine has a job running on it that
  divides the compute resources equally, the workload that is
  going to run will be limited on a per-core basis by the amount
  of memory available for that core. This can place an upper limit
  on workload sizes on a particular machine configuration.
- **Monte Carlo simulations:** The
  Monte Carlo simulation method is a means of modelling
  approximate solutions using repeated random sampling.
- **Message Passing Interface (MPI):**Message Passing
  Interface is a standard that defines communication between
  machines that are working on workloads together, allowing those
  workloads to scale out to more than one instance while solving
  the same problem.
- **Network access control lists (NACLs):** A
  [Control
  subnet traffic with network access control lists](../../../vpc/latest/userguide/vpc-network-acls.md "../../../vpc/latest/userguide/vpc-network-acls.md") allows
  administrators to control who has access into a network. This
  controls traffic at the subnet level rather than at an instance.
- **Parallel file system:** This
  is a file system that allows multiple machines to access the
  same file system. It is also possible for multiple reads/writes
  to be made synchronously by a single instance to speed up file
  input/output.
- **Personally identifiable information
  (PII):** Information that identifies one or more
  details about a person including, but not limited to, name,
  address, gender, birth-date, SSN, and Government identifier and
  has strict compliance restrictions on organizations that use it.
- **Placement group:** In a
  physical, on-premises, High Performance Compute (HPC) cluster,
  machines would generally be physically in very close proximity
  to each other. This reduces network latency as the transmission
  distance between machines is low while also needing few numbers
  of 'hops' across different hardware (e.g. network switches). The
  equivalent on AWS is requesting instances in a Placement Group
  whereby requested instances will be allocated as close to each
  other as possible.
- **Recovery Point Objective (RPO):** According to the US National Institute of Standards and
  Technology,
  [Recovery
  Point Objective](https://csrc.nist.gov/glossary/term/recovery_point_objective "https://csrc.nist.gov/glossary/term/recovery_point_objective") is defined as The point in time to which
  data must be recovered after an outage.
- **Recovery Time Objective (RTO):** According to the US National Institute of Standards and
  Technology,
  [Recovery
  Time Objective](https://csrc.nist.gov/glossary/term/recovery_time_objective "https://csrc.nist.gov/glossary/term/recovery_time_objective") is defined as The overall length of time
  an information system's components can be in the recovery phase
  before negatively impacting the organization's mission or
  mission/business processes.
- **REST-based communication:**
  REST is defined by the US NIST as a software architectural style
  that defines a common method for defining APIs for Web services.
- **Role-based access control (RBAC):** the US NIST provides a
  definition as 'Access control based on user roles (that is a collection of access
  authorizations that a user receives based on an explicit or implicit assumption of a given
  role). Role permissions may be inherited through a role hierarchy and typically reflect the
  permissions needed to perform defined functions within an organization. A given role may
  apply to a single individual or to several individuals.'
- **SBGrid:** Third party package
  management software that provides a software build and install
  framework to manage software on High Performance Computing (HPC)
  systems efficiently.
- **Slurm:** This is an
  open-source workload manager (queuer) to schedule jobs for Linux
  or Unix based systems. Now also known as the Slurm Workload
  Manager, previously Simple Linux Utility for Resource Management
  (Slurm). This is the default choice for scheduler for AWS ParallelCluster.
- **Slurm partition:**
  Computational resources on a cluster with a queue hosted by a
  Slurm system can be split across different partitions, allowing
  users to choose what hardware configuration to queue their jobs
  on to.
- **Spack:** Third party package
  management software that provides a software build and install
  framework to manage (chiefly scientific) software on High
  Performance Computing (HPC) systems efficiently.
