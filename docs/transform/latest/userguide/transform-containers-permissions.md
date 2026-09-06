

# Containerization permissions
<a name="transform-containers-permissions"></a>

During the containerization workflow, AWS Transform deploys an IAM role to your AWS account that uses to build container images and deploy infrastructure. You are asked to review and approve the creation of this role before the workflow continues.

The role is named `AWSTransformCodeBuildExecutionRole` and is deployed through an AWS CloudFormation stack. It includes the following managed policies.

## Base policy
<a name="transform-containers-permissions-base"></a>

Provides core permissions for the containerization workflow:
+ Amazon S3 — Read and write objects in `aws-transform-*` buckets
+ Amazon ECR — Authenticate, pull images (tagged with `Project: atx-migration`), and push images to repositories tagged with `CreatedBy: AWSTransform`
+ AWS CodeArtifact — Read from repositories tagged with `Project: atx-migration`, list repositories, obtain authorization tokens, and read repository endpoints. These permissions support both public dependency resolution and private dependency sources configured during the workflow
+ Amazon CloudWatch Logs — Create log groups and streams, and write log events for and Amazon ECS log groups
+ AWS KMS — Describe and decrypt keys (scoped to Amazon S3 via-service condition)
+ Amazon EC2 — Create and manage network interfaces for VPC-enabled projects
+ AWS CodeConnections — Use connections to access source code repositories through the configured CodeConnections ARN

## Networking policy
<a name="transform-containers-permissions-networking"></a>

Manages networking resources for deployed applications:
+ Elastic Load Balancing — Create, describe, and manage load balancers, target groups, listeners, and rules (tagged with `CreatedBy: AWSTransform`)
+ Route 53 — Create and manage hosted zones and DNS records
+ AWS Cloud Map — Create and manage namespaces and services for service discovery (tagged with `CreatedBy: AWSTransform`)

## Storage policy
<a name="transform-containers-permissions-storage"></a>

Manages storage resources for deployed applications:
+ Amazon S3 — Create and manage buckets, including encryption, versioning, lifecycle, and access policies
+ Amazon EFS — Create and manage file systems, mount targets, and access points (tagged with `CreatedBy: AWSTransform`)
+ Amazon EBS — Create and manage volumes and snapshots (tagged with `CreatedBy: AWSTransform`)

## AWS KMS policy
<a name="transform-containers-permissions-kms"></a>

Manages encryption key operations:
+ Describe keys, list aliases, and read key policies
+ Encrypt, decrypt, and generate data keys (scoped to Amazon CloudWatch Logs, Amazon EFS, Amazon EC2, and Amazon S3 via-service conditions)

## Amazon ECS policy
<a name="transform-containers-permissions-ecs"></a>

Manages Amazon Elastic Container Service resources for container deployments:
+ Create and manage clusters, services, and task definitions (tagged with `CreatedBy: AWSTransform`)
+ Register and deregister task definitions, run tasks
+ Pass IAM roles to Amazon ECS tasks and services
+ Read IAM role information and ACM certificates
+ Describe Amazon EC2 VPCs, subnets, security groups, and network interfaces

## Amazon EKS policy
<a name="transform-containers-permissions-eks"></a>

Manages Amazon Elastic Kubernetes Service resources for Kubernetes deployments:
+ Access the Kubernetes API, describe clusters, and list add-ons
+ Pass IAM roles to Amazon EKS

**Note**  
All permissions are scoped to your AWS account and AWS Region. Resources created by AWS Transform are tagged with `CreatedBy: AWSTransform`, and write operations are restricted to resources with this tag where applicable.