

AWS .NET Modernization Tools Porting Assistant (PA) for .NET, AWS App2Container (A2C), AWS Toolkit for .NET Refactoring (TR), and AWS Microservice Extractor (ME) for .NET is no longer open to new customers. If you would like to use the service, sign up prior to November 7, 2025. Alternatively use [AWS Transform](https://aws.amazon.com/transform/), which is an agentic AI service developed to accelerate enterprise modernization of .NET.

# Product and service integrations for AWS App2Container
<a name="a2c-integrations"></a>

AWS App2Container integrates with an array of AWS services, and partner products and services. After you've deployed your application containers to run on Amazon ECS, Amazon EKS, or App Runner, you can use App2Containerto choose from several different continuous integration and delivery (CI/CD) platforms to keep your images up to date. Use the information in the following sections to help you configure App2Container to integrate with the products and services that you use.

**Topics**
+ [Automatic storage and registration using Amazon Elastic Container Registry](#integrations-ecr)
+ [Deploy to Amazon ECS](a2c-integrations-ecs.md)
+ [Deploy to Amazon EKS](a2c-integrations-eks.md)
+ [Deploy to App Runner](a2c-integrations-apprunner.md)
+ [Set up CodePipeline pipelines](a2c-integration_codepipeline.md)
+ [Set up Jenkins pipelines](a2c-integrations-jenkins.md)
+ [Set up Azure DevOps pipelines](a2c-integrations-azure-devops.md)
+ [Route logs using FireLens](a2c-integrations-firelens.md)

## Automatic storage and registration using Amazon Elastic Container Registry
<a name="integrations-ecr"></a>

App2Container uses the Amazon Elastic Container Registry (Amazon ECR) service to register and store container images for all of the environments it supports for application container deployment. When you run the **app2container generate app-deployment** command, App2Container creates an ECR repository and registers your application container image. The ECR repository name is the application ID that App2Container creates when you run the **app2container inventory** command on your application server or worker machine.

Amazon ECR includes the following features, which are not enabled by default when App2Container creates your repository and registers your container image.
+ Lifecycle policies that help you manage the lifecycle of your images, and clean up unused images. For more information, see [Lifecycle policies](https://docs.aws.amazon.com/AmazonECR/latest/userguide/LifecyclePolicies.html) in the *Amazon Elastic Container Registry User Guide*.
+ Image scanning that helps to identify software vulnerabilities in your container images. You can configure `scan on push` validation for your images. You can also run a manual scan on any of your images that are stored in Amazon ECR. For more information, see [Image scanning](https://docs.aws.amazon.com/AmazonECR/latest/userguide/image-scanning.html) in the *Amazon Elastic Container Registry User Guide*.
+ Cross-Region and cross-account replication to help you distribute your container image to destination accounts and Regions. For more information about replication settings for your registry, see [Private image replication](https://docs.aws.amazon.com/AmazonECR/latest/userguide/replication.html) in the *Amazon Elastic Container Registry User Guide*. 

To view your ECR repository, and change settings using the AWS Management Console, follow these steps:

1. Open the Amazon ECR console at [https://console.aws.amazon.com/ecr/](https://console.aws.amazon.com/ecr/).

   Verify that the console is showing the Region where you want to view and change settings for your repository. The current Region is displayed in the upper right corner of the console.

1. Select the option next to the **Repository name**, where the name matches your App2Container application ID.
**Tip**  
You can use any part of the application ID in the search bar to filter your results.

1. Choose **Edit** to view and change the settings for your repository.

1. Choose **Save** to save settings that you have changed, or **Cancel** to exit without saving.

To learn more about Amazon ECR, see [What is Amazon Elastic Container Registry?](https://docs.aws.amazon.com/AmazonECR/latest/userguide/what-is-ecr.html) in the *Amazon Elastic Container Registry User Guide*.