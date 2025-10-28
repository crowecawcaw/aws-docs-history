# FSIPERF02: How do you select your compute architecture?

## FSIPERF02-BP01 Select your compute architecture based on workload

requirements

The optimal compute solution for a particular architecture depends on the workload
deployment method, degree of automation, usage patterns, and configuration. Third-party
solutions can bring their own requirements for infrastructure, which must also be
considered. Different compute solutions may be chosen for each step of a process.
Selecting the wrong compute solutions for an architecture can lead to lower performance
efficiency.

Some financial services computing workloads, like risk modeling, are typically
loosely coupled and can benefit from event-driven architectures leveraging the scaling
capacity of AWS serverless compute options like AWS Lambda and AWS Fargate, combined
with messaging services including Amazon SQS and Amazon EventBridge to decouple components. These
serverless solutions minimize the overhead of capacity management, automatically
scaling in or out to meet demands.

Containerized infrastructure can enable financial services institutions to achieve
their goals for speed and scalability by providing a standardized environment to leverage
across multiple solutions, and supporting the development of microservice-based
architectures. Where scale is the primary factor, AWS serverless container compute
engine, AWS Fargate, can be used with both Amazon Elastic Container Service (Amazon ECS) and Amazon Elastic Kubernetes Service (Amazon EKS),
removing the overhead of managing and provisioning compute resources.

For solutions with more specific performance requirements, or needing to run on
virtual machines as their compute solution, AWS offers a wide range of Amazon Elastic Compute Cloud
(Amazon EC2) instance types, which you can use to select the configuration that is best suited
to your needs at any given time. This allows you to both take advantage of the latest
CPU technologies as they are released without consideration for prior investment,
and choose instance types with features that best suit your workload's requirements, for
example instance variants optimized for network, storage, or compute performance.

The [Financial Services Grid Computing on AWS](../../../whitepapers/latest/financial-services-grid-computing/grid-computing-on-aws.md "../../../whitepapers/latest/financial-services-grid-computing/grid-computing-on-aws.md") whitepaper explores this topic in
more detail for specific workloads.
