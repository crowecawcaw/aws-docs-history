# Amazon ECS clusters

An Amazon ECS cluster is a logical grouping of tasks or services that provides the infrastructure capacity for your containerized applications. When creating a cluster, you choose from the three primary infrastructure types, each optimized for different use cases and operational requirements.

## Choosing the right cluster type

Amazon ECS offers three infrastructure types for your clusters. Choose the type that best matches your workload requirements, operational preferences, and cost optimization goals:

Amazon ECS Managed Instances (Recommended)

**Best for most workloads** - AWS fully manages the underlying Amazon EC2 instances, including provisioning, patching, and scaling. This option provides the optimal balance of performance, cost-effectiveness, and operational simplicity.

**Use when:**

- You want AWS to handle infrastructure management
- You need cost-effective compute with automatic optimization
- You want to focus on your applications rather than infrastructure
- You need predictable performance with flexible scaling

Fargate

**Serverless compute** - Pay only for the resources your tasks use without managing any infrastructure. Ideal for variable workloads and getting started quickly.

**Use when:**

- You want completely serverless operations
- You have unpredictable or variable workloads
- You want to minimize operational overhead
- You need rapid deployment and scaling

Amazon EC2 instances

**Full control** - You manage the underlying Amazon EC2 instances directly, including instance selection, configuration, and maintenance.

**Use when:**

- You need specific instance types or configurations
- You have existing Amazon EC2 infrastructure to leverage
- You require custom AMIs or specialized software
- You need maximum control over the underlying infrastructure

###### Note

Amazon ECS Managed Instances is the recommended choice for most new workloads as it provides the best combination of performance, cost optimization, and operational simplicity while allowing AWS to handle infrastructure management tasks.

## Cluster components

In addition to the infrastructure capacity, a cluster consists of the following resources:

- The network (VPC and subnet) where your tasks and services run

When you use Amazon ECS Managed Instances or Amazon EC2 instances for the capacity, the subnet can be in Availability Zones, Local
Zones, Wavelength Zones, or AWS Outposts.

- An optional namespace

A namespace is used for service-to-service communication with Service Connect.

- A monitoring option

CloudWatch Container Insights comes at an additional cost and is a fully managed service. It automatically
collects, aggregates, and summarizes Amazon ECS metrics and logs.

## Cluster concepts

The following are general concepts about Amazon ECS clusters.

- You create clusters to separate your resources.
- Clusters are AWS Region specific.
- Clusters can be in any of the following states.

ACTIVE

The cluster is ready to accept tasks and, if applicable, you can
register container instances with the cluster.

PROVISIONING

The cluster has capacity providers associated with it and the
resources needed for the capacity provider are being created.

DEPROVISIONING

The cluster has capacity providers associated with it and the
resources needed for the capacity provider are being deleted.

FAILED

The cluster has capacity providers associated with it and the
resources needed for the capacity provider have failed to create.

INACTIVE

The cluster has been deleted. Clusters with an `INACTIVE`
status may remain discoverable in your account for a period of time.
This behavior is subject to change in the future, so make sure you do
not rely on `INACTIVE` clusters persisting.

- A cluster can contain a mix of tasks that are hosted on Amazon ECS Managed Instances,
  AWS Fargate, Amazon EC2 instances, or external instances. Tasks can run on
  Amazon ECS Managed Instances, Fargate or EC2 infrastructure as
  a launch type or a capacity provider strategy. If you use EC2 capacity providers, Amazon ECS doesn't track and scale the capacity of Amazon EC2 Auto Scaling
  groups.
- A cluster can contain a mix of Amazon ECS Managed Instances capacity providers, Amazon EC2 Auto Scaling group capacity providers, and Fargate
  capacity providers. A capacity provider strategy can only contain Amazon ECS Managed Instances capacity providers, Amazon EC2 Auto Scaling group
  capacity providers, or Fargate capacity providers.
- You can use different instance types for the Amazon ECS Managed Instances and EC2, or Amazon EC2 Auto Scaling
  group capacity providers. An instance can only be registered to one cluster at a
  time.
- You can restrict access to clusters by creating custom IAM policies. For
  information, see [Amazon ECS cluster examples](security_iam_id-based-policy-examples.md#IAM_cluster_policies "security_iam_id-based-policy-examples.md#IAM_cluster_policies") section in [Identity-based policy examples for
  Amazon Elastic Container Service](security_iam_id-based-policy-examples.md "security_iam_id-based-policy-examples.md").
- You can use Service Auto Scaling to scale Fargate tasks. For more information, see [Automatically scale your Amazon ECS service](service-auto-scaling.md "service-auto-scaling.md").
- You can configure a default Service Connect namespace for a cluster. After you
  set a default Service Connect namespace, any new services created in the cluster
  can be added as client services in the namespace by turning on Service Connect. No
  additional configuration is required. For more information, see [Use Service Connect to connect Amazon ECS services with short
  names](service-connect.md "service-connect.md").

## Capacity providers

Amazon ECS capacity providers manage the scaling of infrastructure for tasks in your
clusters. Each cluster can have one or more capacity providers and an optional capacity
provider strategy. You can assign a default capacity provider strategy to the cluster.
The capacity provider strategy determines how the tasks are spread across the cluster's
capacity providers. When you run a standalone task or create a service, you either use
the cluster's default capacity provider strategy or a capacity provider strategy that
overrides the default one. The cluster's default capacity provider strategy only applies
when you don't specify a launch type, or capacity provider strategy for your task or
service. If you provide either of these parameters, the default strategy isn't used.

Amazon ECS offers three types of capacity providers for your clusters:

Amazon ECS Managed Instances capacity providers

AWS fully manages the underlying Amazon EC2 instances, including provisioning, patching, scaling, and lifecycle management. This provides the optimal balance of performance, cost-effectiveness, and operational simplicity. Amazon ECS Managed Instances capacity providers automatically optimize instance selection and scaling based on your workload requirements.

With Amazon ECS Managed Instances, you benefit from:

- Automatic instance provisioning and scaling
- Managed patching and security updates
- Cost optimization through intelligent instance selection
- Reduced operational overhead

Fargate capacity providers

Serverless compute where you pay only for the resources your tasks use without managing any infrastructure. You just need to associate the pre-defined capacity providers (Fargate and Fargate Spot) with the cluster.

Amazon EC2 Auto Scaling group capacity providers

When you use Amazon EC2 instances for your capacity, you use Amazon EC2 Auto Scaling group to manage the Amazon EC2 instances. Amazon EC2 Auto Scaling helps ensure that you have the correct number of Amazon EC2 instances available to handle the application load. You have full control over the underlying infrastructure.

A cluster can contain a mix of tasks that are hosted on Amazon ECS Managed Instances,
AWS Fargate, Amazon EC2 instances, or external instances. Tasks can run on
Amazon ECS Managed Instances, Fargate or EC2 infrastructure as a
launch type or a capacity provider strategy. If you use EC2 as a launch
type, Amazon ECS doesn't track and scale the capacity of Amazon EC2 Auto Scaling groups.

A cluster can contain a mix of Amazon ECS Managed Instances capacity providers, Amazon EC2 Auto Scaling group capacity providers, and Fargate
capacity providers. A capacity provider strategy can only contain Amazon ECS Managed Instances capacity providers, Amazon EC2 Auto Scaling group capacity
providers, or Fargate capacity providers.
