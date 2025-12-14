# GAMESUS02-BP02 Right-size your compute and deploy GPU

performance only where needed

Architect your game servers and backend to efficiently utilize
compute resources. Over-provisioning compute can lead to unnecessary
costs and minimizes the amount of idle or under-utilized resources.
GPU instances should be used to support specific development efforts
like HLOD rebuilds in Unreal, or if you game servers require them by
design. This greatly reduces the environmental impact and costs of
your workloads.

**Level of risk exposed if this best practice
is not established:** High

## Implementation guidance

You should optimize your game servers and backend services to use
multiple EC2 instances types and the least number of instances
needed. This increases the number of instances available to meet
your needs during development or for your games launch. You should
also match the instance type to the specific workload you're
deploying. Compute Optimized instances support a wide range of
use-cases including game servers and backend services like
matchmaking. Memory Optimized instances are designed to deliver
fast performance for workloads that process large data sets in
memory. Use GPU instances as required for high performance
requirements, but not for general computing tasks. If able,
architect your services or game servers to run on ARM with
[AWS Graviton instances](https://aws.amazon.com/ec2/graviton/ "https://aws.amazon.com/ec2/graviton/"). Graviton is the most performant to
energy efficient instance type available on AWS. They also offer
improved performance and costs when compared to x86 instance
types.

Use the
[AWS Compute Optimizer](https://aws.amazon.com/compute-optimizer/ "https://aws.amazon.com/compute-optimizer/") to identify the optimal AWS resource
configurations, such as Amazon Elastic Compute Cloud (EC2)
instance types, Amazon Elastic Block Store (EBS) volume
configurations, task sizes of Amazon Elastic Container Service
(ECS) services on AWS Fargate, commercial software licenses, AWS Lambda function memory sizes, and Amazon Relational Database Service (RDS) DB instance classes, using machine learning to
analyze historical utilization metrics. Compute Optimizer provides
a set of APIs and a console experience to reduce costs and
increase workload performance by recommending the optimal AWS
resources for your AWS workloads.

### Implementation steps

- Match compute resources to specific workloads by using
  Compute Optimized instances for game servers, Memory
  Optimized instances for large data sets, and GPU instances
  only for tasks like HLOD rebuilds or GPU-dependent game
  servers.
- Optimize compute utilization by deploying AWS Graviton
  instances where possible for energy efficiency, better
  performance, and cost savings compared to x86 instances.
- Use AWS Compute Optimizer to analyze historical utilization
  and recommend the most efficient configurations for EC2, AWS
  ECS, AWS Lambda, and Amazon RDS workloads to reduce costs
  and improve performance.
