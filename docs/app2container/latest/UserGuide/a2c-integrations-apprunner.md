AWS .NET Modernization Tools Porting Assistant (PA) for .NET, AWS App2Container (A2C), AWS Toolkit for .NET Refactoring (TR), and AWS Microservice Extractor (ME) for .NET is no longer open to new customers. If you would like to use the service, sign up prior to November 7, 2025. Alternatively use [AWS Transform](https://aws.amazon.com/transform/ "https://aws.amazon.com/transform/"), which is an agentic AI service developed to accelerate enterprise modernization of .NET.

# Deploy application containers to AWS App Runner with AWS App2Container

AWS App Runner is an AWS service that provides a way for existing container images or
source code to run directly as web services in AWS. App Runner uses Fargate as its
underlying environment, but has its own management layer on top. With App Runner, you can
access your application through an assigned web service URL, via HTTP requests.

Considerations for deploying to App Runner using App2Container:

- App Runner is not available in all Regions. To see the Regions and service
  endpoints for App Runner, refer to [App Runner Service
  endpoints](../../../general/latest/gr/apprunner.md#apprunner_region "../../../general/latest/gr/apprunner.md#apprunner_region") in the _AWS General Reference_.
- Resources that are created by App Runner reside in the multi-tenant App Runner
  service account. With other container management services, you might access
  resources such as an Amazon EC2 instance that your container runs on, or an Amazon EBS
  volume attached to your container instance, using the standard access methods
  for those resources directly. With App Runner you access resources that
  App Runner creates for your application through the App Runner service, using the
  App Runner console, API, SDKs, or by using **apprunner**
  commands in the AWS CLI.
- App Runner supports continuous integration and deployment from the Amazon ECR repository that App2Container
  creates on your behalf. When continuous deployment is configured, an update to the
  container image in the Amazon ECR repository automatically initiates an update in
  App Runner.

You can turn this on or off in the `deployment.json` file.
For more information, see [Configure deployment](config-deployment.md "config-deployment.md").

- App Runner integrates with Amazon CloudWatch and AWS CloudTrail to provide logging and
  monitoring support for your application. App Runner creates the following log
  groups for each App Runner service:

      + An application group, which contains `stdout` from your containers.
      + A service group, which contains high-level logs from App Runner to notify you about
       service-related events, such as new deployments or health check
       failures.

  These logs can also be viewed from the App Runner console, or by using
  the App Runner API, SDKs, or by using **apprunner** commands
  in the AWS CLI.

- App Runner enforces limits for the application containers that it hosts, such as the number of
  concurrent requests, the size of the application, and the amount of memory it can
  use. To learn more about Service Quotas for App Runner, see [App Runner Service
  quotas](../../../general/latest/gr/apprunner.md#limits_apprunner "../../../general/latest/gr/apprunner.md#limits_apprunner") in the _AWS General Reference_.
- Application state is not guaranteed to be maintained between requests.
  For more information about using App Runner to host your application container, see
  [What is AWS App Runner](../../../apprunner/latest/dg/what-is-apprunner.md "../../../apprunner/latest/dg/what-is-apprunner.md") in the
  _AWS App Runner Developer Guide_.

## Prerequisites

To configure an App Runner integration for your application container with App2Container, your application
must meet the following criteria:

- Your application runs on Linux. [*Windows applications are not currently supported.*]
- Your application meets all of the requirements that are listed in the
  [Supported applications](supported-applications.md "supported-applications.md") section for Linux.
- Your application container size is less than 3 GB.
- Your application must not be dependent on background processing. App Runner heavily
  throttles container CPU when requests are not actively being processed.

## App Runner integration for App2Container workflow

Setting up application containers for hosting in App Runner integrates smoothly with the App2Container
workflow. Initial steps for App2Container are the same for all applications:

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
      for hosting in App Runner (see [Prerequisites](#integrations-apprunner-prereq "#integrations-apprunner-prereq")).
    - Each container management service has its own section in the
      `deployment.json` file, and each section has a
      flag to indicate which container management service is the destination for
      your application container. Only one section can have its flag set to
      **true** – all others must be
      set to **false**.

    Amazon ECS is configured as the destination by default, but if your application is suitable
    for App Runner, you can set the `createAppRunnerArtifacts` flag in
    the `appRunnerParameters` section to **true**, and the `createEcsArtifacts` flag in
    the `ecsParameters` section to **false**.
    For more information about configuring the `deployment.json`
    file, see [Configure deployment](config-deployment.md "config-deployment.md").

5.  The deployment step generates a CloudFormation template and `pipeline.json`
    file that are targeted for the App Runner container management service, based on the
    settings in the `deployment.json` file, where the
    `createAppRunnerArtifacts` flag is set to **true**.
    - When you run the **generate app-deployment** command, App2Container
      validates the properties in the `deployment.json` file,
      and pushes the container image to Amazon ECR. This is the standard workflow.
    - The command generates a CloudFormation template for App Runner deployment that
      contains the IAM role that App Runner uses to pull your application
      container images from Amazon ECR, and the App Runner service definition.
    - The command generates the `pipeline.json` file to
      support creating a pipeline to deploy updates to your application
      container in Amazon ECR.
    - If you use the `--deploy` option for the **generate
      app-deployment** command, App2Container deploys the CloudFormation stack that creates
      the App Runner service for the containerized application, using the configuration
      values in the CloudFormation template that it generates. To customize the configuration,
      run the command without the `--deploy` option, and then manually
      deploy using the AWS CLI when you are ready.

6.  The pipeline step generates a CloudFormation template for the pipeline that is targeted
    for the App Runner container management service, based on the settings in the
    `pipeline.json` file.
    - When you run the **generate pipeline** command, App2Container
      validates the properties in the `pipeline.json`
      file, and verifies that initial deployment to App Runner has been completed,
      and that your application is active.
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

    ###### Note

    If you have automatic deployments configured for App Runner, an update to your
    application container image in Amazon ECR automatically kicks off an update for your
    application in App Runner.

    To configure automatic deployments, use the following settings in the
    `deployment.json` file:

        + Set `autoDeploymentsEnabled` to
         **true** to automatically deploy
         updates to App Runner when you deploy updates to Amazon ECR. *This
         is the default setting.*
        + Set `autoDeploymentsEnabled` to
         **false** if you want to update App Runner
         manually, using the App Runner service console, API, SDKs, or AWS CLI.
