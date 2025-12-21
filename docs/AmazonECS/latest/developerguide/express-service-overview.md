# Amazon ECS Express Mode

An Amazon ECS Express Mode service reduces the complexity of deploying containerized applications by providing sensible defaults and automating
the configuration of supporting AWS services. Instead of managing configuration parameters across multiple services, an Express Mode service
requires only three things to get started:

- A container image
- A task execution role
- An infrastructure role
  Amazon ECS Express Mode orchestrates and configures all necessary infrastructure: a Fargate-based ECS service with a unique accessible URL,
  load balancer with SSL/TLS, auto scaling policies, monitoring, and networking components.

Use Amazon ECS Express Mode services in the following scenarios:

- Web applications and APIs - Stateless containerized applications that serve HTTP
  requests
- Rapid prototyping - Quickly deploy and test applications without infrastructure
  setup overhead
- Developer productivity - Enable application teams to deploy independently without
  deep AWS knowledge
- Platform team efficiency - Reduce maintenance overhead by providing self-service
  deployment capabilities
  Amazon ECS Express Mode services support either public or private HTTPS applications and automatically
  scale based on utilization or traffic.

## Benefits of Amazon ECS Express Mode services

Amazon ECS Express Mode services provide several key advantages for deploying and managing containerized applications on AWS.

- Simplified deployment - Deploy containerized applications with production-ready defaults across multiple AWS services.
- No compromise on capabilities - All underlying AWS resources remain accessible for direct management when you need fine-grained control or advanced features.
- Cost optimization - Shares Application Load Balancers across multiple Express Mode services using the same networking configuration to reduce costs.
- Transparent infrastructure - All resources are created in your AWS account with full visibility and accessibility through the AWS console and APIs.

## Pricing

There is no additional charge for using an Amazon ECS Express Mode service. You pay only for the underlying AWS resources that are created to run your application, including:

- Fargate compute resources
- Application Load Balancer
- CloudWatch logs and metrics
- Data transfer charges

## Availability

Amazon ECS Express Mode is available in all AWS Regions where Amazon ECS and Fargate are
supported. You can create and manage Express Mode services using any of the
following:

- The Amazon ECS console
- AWS AWS CLI
- AWS SDKs
- CloudFormation
- Terraform
- AWS Labs MCP Server for Amazon ECS
