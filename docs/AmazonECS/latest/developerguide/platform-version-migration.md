# Migrating to Linux platform version 1.4.0

on Amazon ECS

Consider the following when migrating your Amazon ECS on Fargate tasks from platform
version `1.0.0`, `1.1.0`, `1.2.0`, or
`1.3.0` to platform version `1.4.0`. It is best practice to
confirm your task works properly on platform version `1.4.0` before you
migrate the tasks.

- The network traffic behavior to and from tasks has been updated. Starting with
  platform version 1.4.0, all Amazon ECS on Fargate tasks receive a single elastic
  network interface (referred to as the task ENI) and all network traffic flows
  through that ENI within your VPC. The traffic is visible to you through your VPC
  flow logs. For more information see [Amazon ECS task networking options for Fargate](fargate-task-networking.md "fargate-task-networking.md").
- If you use interface VPC endpoints, consider the following.
  - For container images hosted with Amazon ECR, you need the following
    endpoints. For more information, see [Amazon ECR interface
    VPC endpoints (AWS PrivateLink)](../../../AmazonECR/latest/userguide/vpc-endpoints.md "../../../AmazonECR/latest/userguide/vpc-endpoints.md") in the
    _Amazon Elastic Container Registry User Guide_.
    - **com.amazonaws.`region`.ecr.dkr**
      Amazon ECR VPC endpoint
    - **com.amazonaws.`region`.ecr.api**
      Amazon ECR VPC endpoint
    - Amazon S3 gateway endpoint

  - When your task definition references Secrets Manager secrets to retrieve
    sensitive data for your containers, you must create the interface VPC
    endpoints for Secrets Manager. For more information, see [Using Secrets Manager with VPC Endpoints](../../../secretsmanager/latest/userguide/vpc-endpoint-overview.md "../../../secretsmanager/latest/userguide/vpc-endpoint-overview.md") in the
    _AWS Secrets Manager User Guide_.
  - When your task definition references Systems Manager Parameter Store parameters
    to retrieve sensitive data for your containers, you must create the
    interface VPC endpoints for Systems Manager. For more information, see [Improve
    the security of EC2 instances by using VPC endpoints for
    Systems Manager](../../../systems-manager/latest/userguide/setup-create-vpc.md "../../../systems-manager/latest/userguide/setup-create-vpc.md") in the _AWS Systems Manager User Guide_.
  - The security group for the Elastic Network Interface (ENI) associated
    with your task needs the security group rules to allow traffic between
    the task and the VPC endpoints.
