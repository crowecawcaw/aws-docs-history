# Scenarios

HPC cases are typically complex computational problems that require
parallel-processing techniques. To support the calculations, a
well-architected HPC infrastructure is capable of sustained
performance for the duration of the calculations. HPC workloads span
traditional applications, like computational chemistry, financial
risk modeling, computer aided engineering, weather prediction, and
seismic imaging, as well as emerging applications, like artificial
intelligence, autonomous driving, and bioinformatics.

The traditional grids or HPC clusters that support these
calculations are similar in architecture with particular cluster
attributes optimized for the specific workload. In a traditional
on-premises HPC cluster, every workload has to be optimized for the
given infrastructure. In AWS, the network, storage type, compute
(instance) type, and deployment method can be chosen to optimize
performance, cost, robustness and usability for a particular
workload.

In this section we will introduce the following scenarios commonly
seen with HPC workloads:

- Loosely coupled cases
- Tightly coupled cases
- Hybrid HPC cases

We also provide a reference architecture for each workload type.
Architecture may differ based on a workload's data access pattern,
so for each of the scenarios, there are considerations for
data-light and data-intensive workloads. The reference architectures
provided here are representative examples and do not exclude the
possible selection of other AWS services or third-party solutions.

Loosely coupled cases are those where the multiple or parallel
processes do not strongly interact with each other in the course of
the entire simulation (often it is based on data parallelism). With
loosely coupled workloads, the completion of an entire calculation
or simulation often requires hundreds to millions of parallel
processes. These processes occur in any order and at any speed
through the course of the simulation. This offers flexibility on the
computing infrastructure required for loosely coupled simulations.

Tightly coupled cases are those where the parallel processes are
simultaneously running and regularly exchanging information between
each other at each iteration or step of the simulation. Typically,
these tightly coupled simulations run on a homogenous cluster using
MPI. The total core or processor count can range from tens to
thousands and occasionally to hundreds of thousands if the
infrastructure allows. The interactions of the processes during the
simulation place extra demands on the infrastructure, such as the
compute nodes and network infrastructure.

In a hybrid HPC case, an on-premises HPC infrastructure interacts
with HPC resources on AWS to extend on-premises resources and
functionalities. Hybrid scenarios vary from minimal coordination,
like compute separation, to tightly integrated approaches, like
scheduler driven job placement. On-premises infrastructure is
normally connected with AWS through a secure VPN tunnel or a
dedicated network. Typically, some or all of the data is synced in
between the on-premises environment and AWS through this network.

The infrastructure used to run the huge variety of loosely coupled
and tightly coupled workloads is differentiated by its ability for
process interactions across nodes and storage infrastructure. There
are fundamental aspects that apply to loosely and tightly coupled
scenarios, as well as specific design considerations. There are
additional aspects for hybrid scenarios to be considered. Consider
the following fundamentals for all scenarios when selecting an HPC
infrastructure on AWS:

- **Network:** Network requirements
  can range from cases with low demands, such as loosely coupled
  applications with minimal communication traffic, to tightly
  coupled and massively parallel applications that require a
  performant network with high bandwidth and low latency. For
  hybrid scenarios, a secure link between the on-premises data
  center and AWS may be required, such as
  [AWS Direct Connect](https://aws.amazon.com/directconnect/ "https://aws.amazon.com/directconnect/") or
  [Site-to-Site VPN](../../../vpn/latest/s2svpn/VPC_VPN.md "../../../vpn/latest/s2svpn/VPC_VPN.md").
- **Storage:** HPC calculations
  use, create, and move data in unique ways. Storage
  infrastructure must support these requirements during each step
  of the calculation. Factors to be considered include data size,
  media type, transfer speeds, shared access, and storage
  properties (for example, durability and availability). AWS
  offers a wide range of storage options to meet the performance
  requirements of both data-light and data-intensive workloads.
- **Compute:** The
  [Amazon EC2 instance type](https://aws.amazon.com/ec2/instance-types/ "https://aws.amazon.com/ec2/instance-types/") defines the hardware capabilities
  available for your HPC workload. Hardware capabilities include
  the processor type, core frequency, processor features (for
  example, vector extensions), memory-to-core ratio, and network
  performance. In the cloud, you can also use HPC resources
  interactively through AWS-managed tools such as
  [Amazon
  DCV](https://aws.amazon.com/hpc/dcv/ "https://aws.amazon.com/hpc/dcv/") desktops, open source tools such as
  [Jupyter](https://jupyter.org/ "https://jupyter.org/"), or other
  third-party options for domain specific applications.
- **Deployment:** AWS provides many
  options for deploying HPC workloads. For an automated
  deployment, a variety of software development kits (SDKs) are
  available for coding end-to-end solutions in different
  programming languages. A popular HPC deployment option combines
  bash shell scripting with the
  [AWS Command Line Interface (AWS CLI)](https://aws.amazon.com/cli/ "https://aws.amazon.com/cli/"). There are also
  [Infrastructure
  as code (IaC)](../../../whitepapers/latest/introduction-devops-aws/infrastructure-as-code.md "../../../whitepapers/latest/introduction-devops-aws/infrastructure-as-code.md") options such as
  [AWS CloudFormation](https://aws.amazon.com/cloudformation/ "https://aws.amazon.com/cloudformation/") and
  [AWS ParallelCluster](https://aws.amazon.com/hpc/parallelcluster/ "https://aws.amazon.com/hpc/parallelcluster/"), as well as managed deployment services
  for container-based workloads such as
  [Amazon Elastic Container Service (Amazon ECS)](https://aws.amazon.com/ecs/ "https://aws.amazon.com/ecs/"),
  [Amazon Elastic Kubernetes Service (Amazon EKS)](https://aws.amazon.com/eks/ "https://aws.amazon.com/eks/"),
  [AWS Fargate](https://aws.amazon.com/fargate/ "https://aws.amazon.com/fargate/"), and
  [AWS Batch](https://aws.amazon.com/batch/ "https://aws.amazon.com/batch/").

In the following sections, we review a few example scenarios and
architectures to demonstrate how AWS can address requirements for
the wide range of HPC use cases.

###### Scenarios

- [Loosely coupled scenarios](loosely-coupled-scenarios.md "loosely-coupled-scenarios.md")
- [Tightly coupled scenarios](tightly-coupled-scenarios.md "tightly-coupled-scenarios.md")
- [Hybrid scenarios](hybrid-scenarios.md "hybrid-scenarios.md")
