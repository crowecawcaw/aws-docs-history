

# Step 6: Generate Infrastructure as Code
<a name="transform-containers-step-iac"></a>

In this step, AWS Transform generates AWS infrastructure templates for deploying your containerized application. You choose between Amazon Elastic Kubernetes Service and Amazon Elastic Container Service as your target platform.

## Amazon Elastic Kubernetes Service (Kubernetes)
<a name="transform-containers-iac-eks"></a>

If you choose Amazon EKS, AWS Transform generates Helm charts with Kubernetes manifests for your application. The generated templates include:
+ Deployments and services
+ Ingress rules
+ ConfigMaps and SecretProviderClass resources
+ Service accounts
+ Persistent volume claims (EBS and EFS)
+ Route 53 DNS records
+ Health check configurations

### Optional: CloudWatch logging
<a name="transform-containers-iac-eks-logging"></a>

AWS Transform asks if you want to include CloudWatch logging for your Amazon EKS deployment. If you opt in, AWS Transform generates a Fluent Bit DaemonSet configuration that collects pod logs and ships them to CloudWatch Logs.

If you choose CloudWatch logging, your cluster administrator must complete the following prerequisites before deployment:

1. Create the `amazon-cloudwatch` namespace in the cluster.

1. Create an IAM role for the Fluent Bit service account with CloudWatch Logs write permissions. You are prompted for the role ARN during deployment.

## Amazon Elastic Container Service (Terraform)
<a name="transform-containers-iac-ecs"></a>

If you choose Amazon ECS, AWS Transform generates Terraform modules for deploying your application. The generated templates include:
+ ECS cluster
+ ECS service with task definitions
+ Application Load Balancer with access logging
+ Amazon EFS for persistent storage
+ Private hosted zones for service discovery
+ Health check configurations

## Automated validation and security scanning
<a name="transform-containers-iac-validation"></a>

AWS Transform automatically validates the generated infrastructure templates before presenting them to you. The validation includes:
+ For Terraform: `terraform fmt` and `terraform validate` to check syntax and configuration correctness.
+ For Helm: Chart validation to verify that the generated manifests are well-formed.
+ Security scanning using Checkov to identify potential security misconfigurations in the generated infrastructure code.

AWS Transform reports any validation issues and resolves them before proceeding.

## Generating IaC without published images
<a name="transform-containers-iac-decoupled"></a>

You can generate infrastructure templates even if you did not publish container images in the previous step. The generated templates use placeholder image URIs that you can update later with your actual image locations.

## What you need to do
<a name="transform-containers-iac-user-actions"></a>

**To generate infrastructure templates**

1. When prompted, choose your target platform: **Amazon EKS** or **Amazon ECS**.

1. If you chose Amazon EKS, AWS Transform asks whether to include CloudWatch logging. Respond yes or no.

1. If prompted, provide health check endpoint details for your application (such as a `/health` path).

1. AWS Transform generates and validates the infrastructure templates. This step runs automatically and AWS Transform displays progress updates, including any validation or security scan results.

1. Review the generated templates when AWS Transform presents them.