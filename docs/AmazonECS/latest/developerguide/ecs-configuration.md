# Architect your solution for Amazon ECS

You must architect your applications so that they can run on
_containers_. A container is a standardized unit of software
development that holds everything that your software application requires to run. This
includes relevant code, runtime, system tools, and system libraries. Containers are created
from a read-only template that's called an _image_. A container image, is
a static artifact containing your application and its dependencies. Images are typically
built from a Dockerfile. A Dockerfile is a plaintext file that contains the instructions for
building a container. After they're built, these images are stored in a
_registry_ such as Amazon ECR where they can be downloaded from.

After you create and store your image, you create an Amazon ECS task definition. A
_task definition_ is a blueprint for your application. It is a text
file in JSON format that describes the parameters and one or more containers that form your
application. For example, you can use it to specify the image and parameters for the
operating system, which containers to use, which ports to open for your application, and
what data volumes to use with the containers in the task. The specific parameters available
for your task definition depend on the needs of your specific application.

After you define your task definition, you deploy it as either a service or a task on your
cluster. A _cluster_ is a logical grouping of tasks or services that runs
on the capacity infrastructure that is registered to a cluster.

A _task_ is the instantiation of a task definition within a cluster.
You can run a standalone task, or you can run a task as part of a service. You can use an
Amazon ECS _service_ to run and maintain your desired number of
tasks simultaneously in an Amazon ECS cluster. How it works is that, if any of your tasks fail or
stop for any reason, the Amazon ECS service scheduler launches another instance based on your
task definition. It does this to replace it and thereby maintain your desired number of
tasks in the service.

The _container agent_ runs on each container instance within an Amazon ECS
cluster. The agent sends information about the current running tasks and resource
utilization of your containers to Amazon ECS. It starts and stops tasks whenever it receives a
request from Amazon ECS.

After you deploy the task or service, you can use any of the following tools to monitor
your deployment and application:

- CloudWatch
- Runtime Monitoring

## Capacity

The capacity is the infrastructure where your containers run. Amazon ECS offers three infrastructure types for your clusters:

- Amazon ECS Managed Instances - AWS fully manages the underlying Amazon EC2 instances
  running in your account, including provisioning, patching, and scaling. This
  option provides the optimal balance of performance, cost-effectiveness, and
  operational simplicity.
- Serverless (Fargate) - Pay only for the resources your tasks use without managing any infrastructure. Ideal for variable workloads and getting started quickly.
- Amazon EC2 instances - You manage the underlying Amazon EC2 instances directly, including instance selection, configuration, and maintenance.

Use Amazon ECS Managed Instances when:

- You want the simplicity of Fargate with more control over the underlying infrastructure.
- You need predictable performance and cost optimization.
- You want AWS to handle infrastructure management while maintaining flexibility.

Use Fargate when:

- You want to focus on your application without managing infrastructure.
- You have variable or unpredictable workloads.
- You're getting started with containers and want the simplest deployment option.

Use Amazon EC2 instances when:

- You need specialized hardware requirements (GPU acceleration, high-performance computing).
- You require capacity reservations or specific instance types.
- You need privileged capabilities or custom AMIs.

You specify the infrastructure when you create a cluster. You also specify the
infrastructure type when you register a task definition. The task definition refers to
the infrastructure as the "launch type". You can also use capacity providers.

## Service endpoints

The service endpoint is the URL of the entry point for Amazon ECS that you use to connect
to the service programmatically using either Internet Protocol version 4 (IPv4) or
Internet Protocol version 6 (IPv6). By default, requests that you make to connect to
Amazon ECS programmatically use service endpoints that support only IPv4 requests. To connect
programmatically with Amazon ECS using either IPv4 or IPv6 requests, you can use a dual-stack
endpoint. For information about using a dual-stack endpoint, see [Using Amazon ECS dual-stack endpoints](dual-stack-endpoint.md "dual-stack-endpoint.md").

## Networking

AWS resources are created in subnets. When you use EC2 instances, Amazon ECS launches the
instances in the subnet that you specify when you create a cluster. Your tasks run in
the instance subnet. For Fargate or on-premises virtual machines, you specify the
subnet when you run a task or create a service.

Depending on your application, the subnet can be a private or public subnet and the
subnet can be in any of the following AWS resources:

- Availability Zones
- Local Zones
- Wavelength Zones
- AWS Regions
- AWS Outposts

For more information, see [Amazon ECS applications in shared subnets, Local Zones, and Wavelength Zones](cluster-regions-zones.md "cluster-regions-zones.md") or [Amazon Elastic Container Service on AWS Outposts](using-outposts.md "using-outposts.md").

You can have your application connect to the internet by using one of the following
methods:

- A public subnet with an internet gateway

Use public subnets when you have public applications that require large
amounts of bandwidth or minimal latency. Applicable scenarios include video
streaming and gaming services.

- A private subnet with a NAT gateway

Use private subnets when you want to protect your containers from direct
external access. Applicable scenarios include payment processing systems or
containers storing user data and passwords.

- AWS PrivateLink

Use AWS PrivateLink to have private connectivity between VPCs, AWS services,
and your on-premises networks without exposing your traffic to the public
internet.

## Feature access

You can use your Amazon ECS account settings to access the following features:

- Container Insights

CloudWatch Container Insights collects, aggregates, and summarizes metrics and logs
from your containerized applications and microservices. The metrics include
utilization for resources such as CPU, memory, disk, and network.

- `awsvpc` trunking

For certain EC2 instances types, you can have additional network interfaces
(ENIs) available on newly launched container instances.

- Tagging authorization

Users must have permissions for actions that create a resource, such as
`ecsCreateCluster`. If tags are specified in the
resource-creating action, AWS performs additional authorization on the
`ecs:TagResource` action to verify if users or roles have
permissions to create tags.

- Fargate FIPS-140 compliance

Fargate supports the Federal Information Processing Standard (FIPS-140) which
specifies the security requirements for cryptographic modules that protect
sensitive information. It is the current United States and Canadian government
standard, and is applicable to systems that are required to be compliant with
Federal Information Security Management Act (FISMA) or Federal Risk and
Authorization Management Program (FedRAMP).

- Fargate task retirement time changes

You can configure the wait period before Fargate tasks are retired for
patching.

- Dual stack VPC

Allow tasks to communicate over IPv4, IPv6, or both.

- Amazon Resource Name (ARN) format

Certain features, such as tagging authorization, require a new Amazon Resource Name (ARN)
format.

For more information, see [Access Amazon ECS features with account settings](ecs-account-settings.md "ecs-account-settings.md").

## IAM roles

An IAM role is an IAM identity that you can create in your account that has
specific permissions. In Amazon ECS, you can create roles to grant permissions to Amazon ECS
resource such as containers or services.

Some Amazon ECS features require roles. For more information, see [IAM roles for Amazon ECS](ecs-iam-role-overview.md "ecs-iam-role-overview.md").

## Logging

Logging and monitoring are important aspects of maintaining the reliability,
availability, and performance of Amazon ECS workloads. The following options are
available:

- Amazon CloudWatch logs - route logs to
  Amazon CloudWatch
- FireLens for Amazon ECS - route logs to an AWS service or
  AWS Partner Network destination for log storage and analysis. The AWS Partner Network is a global
  community of partners that leverages programs, expertise, and resources to
  build, market, and sell customer offerings.

## Container image best practices

The following are key principles for Amazon ECS container images:

- Include all dependencies in the image
- Run one process per container
- Handle `SIGTERM` for graceful shutdowns
- Write logs to `stdout` and `stderr`
- Use unique tags, avoid `latest` in production
