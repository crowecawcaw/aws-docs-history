

# Source code containerization
<a name="transform-containers"></a>

AWS Transform supports replatforming applications to containers during migration to AWS. This chapter describes AWS Transform's agentic AI capabilities to automate the containerization of your source code. You can migrate and modernize in parallel, reducing the time and complexity of moving from on-premises to cloud-native architectures. You can containerize source code from GitHub, Bitbucket, GitLab, or .zip files, generate Docker images, publish to Amazon Elastic Container Registry (Amazon ECR), and deploy to Amazon Elastic Container Service (Amazon ECS) or Amazon Elastic Kubernetes Service (Amazon EKS). This brings containerization into the same workflow you use to plan and execute rehost migrations.

## Capabilities and key features
<a name="transform-containers-capabilities"></a>

AWS Transform offers the following capabilities for containerizing your applications.
+ **AI-driven source code analysis**. Analyzes your application source code and automatically generates Docker artifacts, including Dockerfiles and related configuration files. No Docker expertise required.
+ **Container image building and publishing**. Builds and tests container images automatically, and publishes them to Amazon Elastic Container Registry with automated vulnerability scanning.
+ **Infrastructure as Code generation**. Generates production-ready deployment infrastructure for either Amazon Elastic Kubernetes Service (Helm charts) or Amazon Elastic Container Service (Terraform modules), with automated validation and security scanning. No need to write IaC from scratch.
+ **Private dependency support**. You can optionally configure AWS CodeArtifact repositories (Maven, PyPI, npm) and private Amazon ECR base images as dependency sources for your builds.
+ **Iterative test and cutover deployment**. Deploys test infrastructure for validation, then deploys finalized infrastructure for production cutover.

**Note**  
Source code containerization is designed for applications that are not yet containerized. It requires access to your application source code and does not support migrating existing containerized workloads. To migrate existing containers to AWS, use standard deployment methods for Amazon Elastic Container Service or Amazon Elastic Kubernetes Service.

## How containerization works
<a name="transform-containers-how-it-works"></a>

AWS Transform uses an AI-powered agent to guide you through the containerization process in a chat-based workflow. The agent handles the entire process from code analysis to deployed container, reducing days of manual Dockerfile authoring and infrastructure setup to hours. AWS Transform coordinates specialized tasks such as source code analysis, Docker image generation, and infrastructure creation. At key points in the workflow, you review and approve the output before proceeding.

You access source code containerization by creating a migration job. Within the job, you can run containerization as a standalone workflow, or as part of an end-to-end migration when a wave's migration strategy is set to *containerize*. For more information, see [Migrations (including VMware)](transform-app-vmware.md).

## Prerequisites
<a name="transform-containers-prerequisites"></a>

Before you begin, ensure that you have the following:
+ An AWS Transform workspace. For information about getting a workspace, see [Getting started](https://docs.aws.amazon.com/transform/latest/userguide/getting-started.html).
+ Your application source code in a Git repository accessible through AWS CodeConnections, or packaged as zip files for upload. Individual files must not exceed 1 GB, and the total size of all source code must not exceed 8 GB.
+ (Optional) An Amazon ECR repository for publishing container images. You can configure Amazon ECR access later in the workflow when you are ready to publish.
+ For Amazon EKS deployments: An existing Amazon EKS cluster, or permissions to create the required infrastructure.
+ For Amazon ECS deployments: Permissions to create Amazon ECS clusters, services, and related resources using Terraform, AWS CloudFormation, or AWS Cloud Development Kit (AWS CDK).

## Containerization workflow
<a name="transform-containers-workflow-overview"></a>

The containerization workflow consists of the following steps. The AWS Transform agent guides you through each step in the chat interface.

1. [Step 1: Review security disclaimer](transform-containers-step-disclaimer.md). Review and accept the security disclaimer.

1. [Step 2: Clone source code](transform-containers-step-clone.md). Provide your application source code.

1. [Step 3: Containerize](transform-containers-step-containerize.md). AI agent analyzes your code and generates Docker artifacts.

1. [Step 4: Review Docker artifacts and code changes](transform-containers-step-review.md). Review generated artifacts and approve code changes.

1. [Step 5: Publish images](transform-containers-step-publish.md). Publish container images to Amazon ECR.

1. [Step 6: Generate Infrastructure as Code](transform-containers-step-iac.md). Generate Amazon EKS or Amazon ECS deployment templates.

1. [Step 7: Deploy test infrastructure](transform-containers-step-test-deploy.md). Deploy and validate test infrastructure.

1. [Step 8: Clean up test infrastructure](transform-containers-step-cleanup.md). Tear down test resources.

1. [Step 9: Deploy cutover infrastructure](transform-containers-step-cutover.md). Deploy production infrastructure.

## Starting a containerization job
<a name="transform-containers-starting"></a>

To containerize your applications, you first create a VMware migration job in your AWS Transform workspace. From within the job, you can choose to run a standalone containerization workflow or an end-to-end migration flow that includes containerization.
+ **Standalone containerization** — Containerize your source code without performing a full VMware migration. Choose this option when you want to containerize applications independently of any infrastructure migration.
+ **End-to-end migration with containerization** — Run the full VMware migration workflow with a *containerize* migration strategy assigned to one or more waves. The containerization workflow runs as part of the migration for those waves. For more information about VMware migration, see [Migrations (including VMware)](transform-app-vmware.md).

**To start a containerization job**

1. On your workspace landing page, choose **Create a job**.

1. Choose **VMware migration**.

1. Choose whether to run a standalone containerization workflow or an end-to-end migration flow that includes containerization.

1. AWS Transform guides you through the workflow steps, starting with [Step 1: Review security disclaimer](transform-containers-step-disclaimer.md).