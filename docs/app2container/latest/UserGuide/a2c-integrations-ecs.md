AWS .NET Modernization Tools Porting Assistant (PA) for .NET, AWS App2Container (A2C), AWS Toolkit for .NET Refactoring (TR), and AWS Microservice Extractor (ME) for .NET will no longer be open to new customers starting on November 7, 2025. If you would like to use the service, sign up prior to November 7, 2025. Alternatively use [AWS Transform](https://aws.amazon.com/transform/ "https://aws.amazon.com/transform/"), which is an agentic AI service developed to accelerate enterprise modernization of .NET.

# Deploy application containers to Amazon Elastic Container Service with AWS App2Container

Amazon Elastic Container Service (Amazon ECS) is a fully managed container orchestration service that helps
you to deploy, manage, and scale containerized applications. It provides
a secure solution for running container workloads with high availability across
multiple Availability Zones within a Region. Amazon ECS offers a variety of hosting
options for your container environment. For more information about Amazon ECS, see
[What is Amazon Elastic Container Service?](../../../AmazonECS/latest/developerguide/Welcome.md "../../../AmazonECS/latest/developerguide/Welcome.md") in the
_Amazon Elastic Container Service Developer Guide_.

AWS App2Container integrates with Amazon ECS, to deploy your application containers to the
following Amazon ECS environments:

- **Amazon ECS** – In the default environment,
  your containers run on EC2 instances. App2Container supports Windows .NET application
  containers for this environment. Linux is not currently supported for this environment.
- **AWS Fargate** –
  Fargate is a serverless architecture. App2Container supports both Linux and
  Windows application containers for this environment. To learn more about
  Fargate, see [Amazon ECS on
  AWS Fargate](../../../AmazonECS/latest/developerguide/AWS_Fargate.md "../../../AmazonECS/latest/developerguide/AWS_Fargate.md") in the _Amazon Elastic Container Service Developer Guide_.

###### Tip

To containerize your applications with a console-based experience and deploy them on
Amazon ECS on AWS Fargate, you can use the _Replatform applications to
Amazon ECS_ template on the [AWS Migration Hub Orchestrator
console](https://console.aws.amazon.com/migrationhub/orchestrator?region=us-east-1#/templates "https://console.aws.amazon.com/migrationhub/orchestrator?region=us-east-1#/templates"). For more information, see [Replatform
applications to Amazon ECS](../../../migrationhub-orchestrator/latest/userguide/replatform-to-ecs.md "../../../migrationhub-orchestrator/latest/userguide/replatform-to-ecs.md") in the _AWS Migration Hub Orchestrator User
Guide_.

## Prerequisites

To configure an Amazon ECS integration for your application container with App2Container,
your application must meet the following criteria.

###### Amazon ECS

- For deployment to the Amazon ECS default environment, App2Container supports
  .NET applications running on Windows. [*Linux applications
  are not currently supported.*]
- .NET applications running on Windows must satisfy application framework and system
  requirements, and meet the criteria for supported applications. For details, see
  [Supported applications](supported-applications.md "supported-applications.md"),
  and expand the **Supported applications for Windows** section.

###### Fargate

- For deployment to Fargate, App2Container supports the following types of
  applications:
  - Java applications running on Linux.
  - .NET applications running on Windows Server 2019.

- Java applications running on Linux must satisfy Java application framework
  requirements, and run on a supported Linux distribution. For details, see
  [Supported applications](supported-applications.md "supported-applications.md"),
  and expand the **Supported applications for Linux** section.
- For .NET application containers, the container operating system must be
  Windows Server 2019. Prior versions are not supported for deployment to Fargate.
  The container operating system is derived from the application server or worker
  machine where containerization runs, so the applicable server operating system
  must also be Windows Server 2019.

Additionally, .NET applications running on Windows must satisfy application framework
requirements, and meet the criteria for supported applications. For details, see
[Supported applications](supported-applications.md "supported-applications.md"),
and expand the **Supported applications for Windows** section.

- gMSA is not supported.

## Amazon ECS integration for App2Container workflow

To set up application containers for hosting in Amazon ECS within the App2Container workflow,
follow these steps:

Initial steps for App2Container are the same for all applications deploying to Amazon ECS:

1.  Install and set up the App2Container environment, as described in the
    [Prerequisites: Set up your servers](start-intro.md#start-containerize-prereq "start-intro.md#start-containerize-prereq") section.
2.  Complete the initialization phase for your App2Container environment with the
    **init** command, and the **remote configure** command, if
    applicable. To learn more about what is included in all of the App2Container
    containerization phases, see the [Command reference](a2c-commands.md "a2c-commands.md").
3.  Complete the analyze phase for each application that you want to containerize.
    - If you are running commands directly on application servers, use
      the **inventory** and **analyze** commands.
    - If you are running a remote workflow on a worker machine, use the
      **remote inventory** and **remote analyze**
      commands.

4.  Integration begins with the containerization step.
    - When you run the **containerize** command, App2Container
      generates the `deployment.json` file, which provides
      configurable parameters for all supported container management service
      options that could apply to your application container.
    - Parameters for Amazon ECS and Amazon EKS are always included. Parameters for App Runner
      are also included if your application container meets the App2Container criteria
      for hosting in App Runner.
    - Each container management service has its own section in the
      `deployment.json` file, and each section has a
      flag to indicate which container management service is the destination for
      your application container. Only one section can have its flag set to
      **true** – all others must be
      set to **false**.

    Amazon ECS is configured by default as the container management service
    for your application. However, the destination settings differ, depending
    on system requirements and the type of application you have.

    In the `deployment.json` file, App2Container initially sets the
    `deployTarget` parameter as follows:

        + `ec2` – App2Container targets the Amazon ECS default environment,
         which runs containers on EC2 instances, for .NET applications that do not
         meet the criteria specified in the **Fargate**
         section under [Prerequisites](#integrations-ecs-prereq "#integrations-ecs-prereq"). Java applications
         are not currently supported for this deployment target.
        + `fargate` – App2Container targets the Fargate environment
         by default for Java applications, and for .NET applications that meet the
         criteria specified in the **Fargate** section
         under [Prerequisites](#integrations-ecs-prereq "#integrations-ecs-prereq").


        If you want your container to run on EC2 instances instead of running
         in Fargate, you can change the `deployTarget` parameter to
         `ec2`. However, this is currently only true for .NET applications.
         If you change the value for a Java application, the **generate
         app-deployment** command throws an error when you run it.

    For more information about configuring the `deployment.json`
    file, see [Configure deployment](config-deployment.md "config-deployment.md").

    ###### Note

    The gMSAParameters are not valid for deployments to
    Fargate, and will generate an error when the **generate app-deployment**
    command runs.

5.  The deployment step generates an ECS task definition and `pipeline.json`
    file that are targeted for the Amazon ECS container management service, based on the settings in
    the `deployment.json` file, where the `createEcsArtifacts`
    flag is set to **true**.
    - When you run the **generate app-deployment** command, App2Container
      validates the properties in the `deployment.json` file,
      and pushes the container image to Amazon ECR. This is the standard workflow.
    - The command generates a CloudFormation template for Amazon ECS deployment
      (`ecs-master.yml`) that contains the IAM role that
      Amazon ECS uses to pull your application container images from Amazon ECR, and
      the Amazon ECS service definition.
    - The command generates the `pipeline.json` file to
      support creating a pipeline to deploy updates to your application
      container in Amazon ECR.
    - If you use the `--deploy` option for the **generate
      app-deployment** command, App2Container deploys the CloudFormation stack that creates
      the Amazon ECS service for the containerized application, using the configuration
      values in the CloudFormation template that it generates. To customize the configuration,
      run the command without the `--deploy` option, and then manually
      deploy using the AWS CLI when you are ready.

6.  The pipeline step generates a CloudFormation template for the
    pipeline that is targeted for the Amazon ECS container management service,
    based on the settings in the `pipeline.json` file.
    - When you run the **generate pipeline** command,
      App2Container validates the properties in the `pipeline.json`
      file, verifies that initial deployment to Amazon ECS has been completed,
      and verifies that your application is active.
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
