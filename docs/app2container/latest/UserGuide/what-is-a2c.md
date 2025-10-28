AWS .NET Modernization Tools Porting Assistant (PA) for .NET, AWS App2Container (A2C), AWS Toolkit for .NET Refactoring (TR), and AWS Microservice Extractor (ME) for .NET will no longer be open to new customers starting on November 7, 2025. If you would like to use the service, sign up prior to November 7, 2025. Alternatively use [AWS Transform](https://aws.amazon.com/transform/ "https://aws.amazon.com/transform/"), which is an agentic AI service developed to accelerate enterprise modernization of .NET.

# What is AWS App2Container?

AWS App2Container (A2C) is a command line tool to help you lift and shift applications that
run in your on-premises data centers or on virtual machines, so that they run in containers
that are managed by Amazon ECS, Amazon EKS, or AWS App Runner. For a console-based experience, you can use
the _Replatform applications to Amazon ECS_ template in the
[AWS Migration Hub Orchestrator console](https://console.aws.amazon.com/migrationhub/orchestrator?region=us-east-1#/templates "https://console.aws.amazon.com/migrationhub/orchestrator?region=us-east-1#/templates"). For more information, see [Replatform applications](../../../migrationhub-orchestrator/latest/userguide/replatform-to-ecs.md "../../../migrationhub-orchestrator/latest/userguide/replatform-to-ecs.md") to Amazon ECS in the _AWS Migration Hub Orchestrator User Guide_.

Moving legacy applications to containers is often the starting point toward application
modernization. There are many benefits to containerization:

- Reduces operational overhead and infrastructure costs
- Increases development and deployment agility
- Standardizes build and deployment processes across an organization

###### Contents

- [How App2Container works](#a2c-how-it-works "#a2c-how-it-works")
- [Accessing AWS through App2Container](#accessing-services "#accessing-services")
- [Pricing](#a2c-pricing "#a2c-pricing")

## How App2Container works

You can use App2Container to generate container images for one or more applications running on
Windows or Linux servers that are compatible with the Open Containers Initiative (OCI).
This includes commercial off-the-shelf applications (COTs). App2Container does not need source
code for the application to containerize it.

You can use App2Container directly on the application servers that are running your
applications, or perform the containerization and deployment steps on a worker
machine.

App2Container performs the following tasks:

- Creates an inventory list for the application server that identifies all
  running ASP.NET (Windows) and Java applications (Linux) that are candidates to
  containerize.
- Analyzes the runtime dependencies of supported applications that are running,
  including cooperating processes and network port dependencies.
- Extracts application artifacts for containerization and generates a
  Dockerfile.
- Initiates builds for the application container.
- Generates AWS artifacts and optionally deploys the containers on Amazon ECS,
  Amazon EKS, or AWS App Runner. For example:
  - a CloudFormation template to configure required compute, network, and
    security infrastructure to deploy containers using Amazon ECS, Amazon EKS, or
    AWS App Runner.
  - An Amazon ECR container image, Amazon ECS task definitions, or AWS CloudFormation templates
    for Amazon EKS or AWS App Runner that incorporate best practices for security and
    scalability of the application by integrating with various AWS
    services.
  - When deploying directly, App2Container can upload AWS CloudFormation resources to an
    Amazon S3 bucket, and create a CloudFormation stack.

- Optionally creates a CI/CD pipeline with AWS CodePipeline and associated services, to
  automate building and deploying your application containers.

## Accessing AWS through App2Container

When you initialize App2Container, you provide it with your AWS credentials. This allows
App2Container to do the following:

- Store artifacts in Amazon S3, if you configured it to do so.
- Create and deploy application containers using AWS services such as Amazon ECS,
  Amazon EKS, and AWS App Runner.
- Create CI/CD pipelines using AWS CodePipeline.

## Pricing

App2Container is offered at no additional charge. You are charged only when you use other
AWS services to run your containerized application, such as Amazon ECR, Amazon ECS, Amazon EKS, and
AWS App Runner. For more information, see [AWS
Pricing](https://aws.amazon.com/pricing/ "https://aws.amazon.com/pricing/").
