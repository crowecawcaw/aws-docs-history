AWS .NET Modernization Tools Porting Assistant (PA) for .NET, AWS App2Container (A2C), AWS Toolkit for .NET Refactoring (TR), and AWS Microservice Extractor (ME) for .NET is no longer open to new customers. If you would like to use the service, sign up prior to November 7, 2025. Alternatively use [AWS Transform](https://aws.amazon.com/transform/ "https://aws.amazon.com/transform/"), which is an agentic AI service developed to accelerate enterprise modernization of .NET.

# Deploy application containers to Amazon EKS with

AWS App2Container

Amazon Elastic Kubernetes Service (Amazon EKS) is a managed service that you can use to run Kubernetes on AWS. Amazon EKS
streamlines the provisioning of highly available and secure clusters, and automates key
maintenance tasks such as patching, node provisioning, and updates. Kubernetes is an
open-source system for automating the deployment, scaling, and management of containerized
applications. For more information about Amazon EKS, see [What is Amazon EKS?](../../../eks/latest/userguide/what-is-eks.md "../../../eks/latest/userguide/what-is-eks.md") in the
*[*Amazon EKS User Guide*](../../../eks/latest/userguide.md "../../../eks/latest/userguide.md")*.

## Prerequisites

To configure an Amazon EKS integration for your application container with App2Container,
your application must meet the following criteria.

- Java applications running on Linux must satisfy Java application framework
  requirements, and run on a supported Linux distribution. For details, see
  [Supported applications](supported-applications.md "supported-applications.md"),
  and expand the **Supported applications for Linux** section.
- .NET applications running on Windows must satisfy application framework and system
  requirements, and meet the criteria for supported applications. For details, see
  [Supported applications](supported-applications.md "supported-applications.md"),
  and expand the **Supported applications for Windows** section.
- Application containers that run in Amazon EKS must launch EC2 instances. App2Container does
  not currently support Fargate as a container launch type for Amazon EKS.

## Amazon EKS integration for App2Container workflow

The process for setting up application containers for hosting in Amazon EKS is integrated
smoothly with the App2Container workflow. Initial steps for App2Container are the same for all applications.

1. Install and set up the App2Container environment, as described in the
   [Prerequisites: Set up your servers](start-intro.md#start-containerize-prereq "start-intro.md#start-containerize-prereq") section.
2. Complete the initialization phase for your App2Container environment with the
   **init** command, and the **remote configure** command, if
   applicable. To learn more about what is included in all of the App2Container
   containerization phases, see the [Command reference](a2c-commands.md "a2c-commands.md").
3. Complete the analyze phase for each application that you want to containerize.
   - If you are running commands directly on application servers, use
     the **inventory** and **analyze** commands.
   - If you are running a remote workflow on a worker machine, use the
     **remote inventory** and **remote analyze**
     commands.

4. Integration begins with the containerization step.
   - When you run the **containerize** command, App2Container
     generates the `deployment.json` file, which provides
     configurable parameters for all supported container management service
     options that could apply to your application container.
   - Parameters for Amazon ECS and Amazon EKS are always included. Parameters for App Runner
     are also included if your application container meets the App2Container criteria
     for hosting in App Runner
   - Each container management service has its own section in the
     `deployment.json` file, and each section has a
     flag to indicate which container management service is the destination for
     your application container. Only one section can have its flag set to
     **true** – all others must be
     set to **false**.

   Amazon ECS is configured as the destination by default. To deploy your
   application containers to Amazon EKS, you can set the `createEksArtifacts`
   in the `eksParameters` section to **true**,
   and the `createEcsArtifacts` flag in the `ecsParameters`
   section to **false**. For more information about configuring the `deployment.json`
   file, see [Configure deployment](config-deployment.md "config-deployment.md").
   - App2Container configures HTTP-based deployments by default. To use HTTPS for your deployment,
     specify the Amazon Resource Name (ARN) of an AWS Certificate Manager (ACM)
     certificate in the `deployment.json` file. For more
     information, see [Configure deployment](config-deployment.md "config-deployment.md").

5. The deployment step creates artifacts that are targeted for the Amazon EKS container
   hosting service, based on the settings in the `deployment.json`
   file, where the `createEksArtifacts` flag is set to
   **true**.
   - When you run the **generate app-deployment** command, App2Container
     validates the properties in the `deployment.json` file,
     and pushes the container image to Amazon ECR. This is the standard workflow.
   - The command generates a CloudFormation template (`eks-master.yml`)
     that creates an EKS cluster, pulls your application container images from Amazon ECR, and
     deploys your application to the cluster.

   It also generates Kubernetes manifests
   (`eks_deployment.yaml`, `eks_service.yaml`, and
   `eks_ingress.yaml`), for post-deployment customizations using a tool
   such as `kubectl`.
   - The command generates the `pipeline.json` file to
     support creating a pipeline to deploy updates to your application
     container in Amazon ECR.
   - If you use the `--deploy` option for the **generate app-deployment**
     command, App2Container deploys the AWS CloudFormation stack that creates the Amazon EKS service for the containerized
     application, using the configuration values in the AWS CloudFormation template that it generates. To
     customize the configuration, run the command without the `--deploy` option, and
     then manually deploy using the AWS CLI when you are ready.

6. The pipeline step generates a CloudFormation template for the pipeline that is targeted for
   the Amazon EKS container management service, based on the settings in the
   `pipeline.json` file.
   - When you run the **generate pipeline** command, App2Container validates the
     properties in the `pipeline.json` file, and verifies that initial
     deployment to Amazon EKS has been completed, and that your application is active.
   - The command generates a CloudFormation template to create a two-step
     pipeline:
     1. Code commit – Creates or updates an AWS CodeCommit
        repository that contains the Dockerfile and application
        artifacts that are required to create your application container
        image.
     2. Code build – Builds the Docker image for your
        application container, and pushes the updated image to the Amazon ECR
        repository that you configured for your application.
     3. If you use the `--deploy` option for the **generate
        pipeline** command, App2Container deploys the pipeline with
        the configuration values in the CloudFormation template it generates. To
        customize the configuration, run the command without the `--deploy`
        option, and then manually deploy using the AWS CLI when you are ready.
