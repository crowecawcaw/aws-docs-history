AWS .NET Modernization Tools Porting Assistant (PA) for .NET, AWS App2Container (A2C), AWS Toolkit for .NET Refactoring (TR), and AWS Microservice Extractor (ME) for .NET will no longer be open to new customers starting on November 7, 2025. If you would like to use the service, sign up prior to November 7, 2025. Alternatively use [AWS Transform](https://aws.amazon.com/transform/ "https://aws.amazon.com/transform/"), which is an agentic AI service developed to accelerate enterprise modernization of .NET.

# Manually deploy as independent

service

To deploy parts of your application as smaller services, we recommend that you set
up the following environment:

- Docker version 17.05 installed locally with administrator access
- An AWS profile with an attached policy that grants permissions to write
  to Amazon Elastic Container Registry and Amazon S3
- Windows Server 2019 or later
- A minimum of 50 GB of free disk space
  To deploy the extracted service as an independent service, perform the following
  high-level steps:

1. Refactor the source code, if necessary, to ensure that the extracted
   service builds successfully.
2. Navigate to the output location of the extracted service.
3. From the Dockerfile, manually create a Docker container image.
4. Push the Docker container image to Amazon Elastic Container Registry (Amazon ECR).
5. Use AWS CloudFormation to deploy the container image hosted in Amazon ECR to Amazon Elastic Container Service
   (ECS). For more information, see [Using Amazon ECR with Amazon ECS](../../../AmazonECS/latest/developerguide/ecr-repositories.md "../../../AmazonECS/latest/developerguide/ecr-repositories.md") and [Creating Amazon ECS resources with AWS CloudFormation](../../../AmazonECS/latest/developerguide/creating-resources-with-cloudformation.md "../../../AmazonECS/latest/developerguide/creating-resources-with-cloudformation.md").
