

# Creating an Amazon ECS Express Mode service
<a name="express-service-create-full"></a>

An Amazon ECS Express Mode service reduces the complexity of deploying containerized applications by providing sensible defaults and automating the configuration of supporting AWS services. Instead of managing configuration parameters across multiple services, an Express Mode service requires only a container image, task execution role and infrastructure role to get started.

After your deployment completes you will be returned a unique URL for your application. You can find the service you just deployed in *Clusters*, and if you did not specify a cluster it will be in the `Default` cluster.

## Prerequisites
<a name="express-service-create-full-prerequisites"></a>

Before creating an Express Mode service, ensure you have one of the following:
+ A container image stored in Amazon ECR.
+ Or a container image stored in a private registry. To use a private registry, configure a Secrets Manager secret. For more information, see [Create an AWS Secrets Manager secret](https://docs.aws.amazon.com/secretsmanager/latest/userguide/create_secret.html) in the *AWS Secrets Manager User Guide*.

**Note**  
IAM Roles are also required, but is covered in the [Console](express-service-first-run.html) and [CLI](express-service-getting-started.html) guides separately. The Amazon ECS Console has automated flows for role creation.

## Walkthroughs
<a name="express-service-create-options"></a>
+ For a simplified first-run experience using the console, see [Create your first Amazon ECS Express Mode service in the console](express-service-first-run.md).
+ To create an Express Mode service using the AWS CLI, see [Create your first Express Mode service using the AWS CLI](express-service-getting-started.md).
+ To learn more about what Express Mode creates and how it works, see [Resources created by Amazon ECS Express Mode services](express-service-work.md).

## Customizing
<a name="express-service-create-custom"></a>

 When creating an Express Mode service, Amazon ECS selects defaults for your Amazon ECS and other AWS resources. Customize the application when needed by using the optional parameters. Take advantage of an Express Mode service and customize the following:
+ Service name
+ Amazon ECS Cluster
+ Container settings - port and health check path
+ Environment variables and secrets
+ Custom commands
+ Task role - This role allows your application code (on the container) to use other AWS services.

  You need this role when your application accesses other AWS services, such as Amazon S3.
+ Compute resources - CPU and memory allocation
+ Network configuration - subnets and service security group
+ Application Auto Scaling policies - metrics, target values, and task limits
+ CloudWatch Logs configuration
+ Resource tags
+ Task definition – use your own custom task definition