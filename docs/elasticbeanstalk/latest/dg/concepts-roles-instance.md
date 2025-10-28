# Elastic Beanstalk instance profile

An instance profile is an IAM role that's applied to Amazon EC2 instances that are launched
in your Elastic Beanstalk environment. When creating an Elastic Beanstalk environment, you specify the instance
profile that's used when your EC2 instances take the following actions:

- Retrieve [application versions](concepts.md#concepts-version "concepts.md#concepts-version") from Amazon Simple Storage Service
  (Amazon S3)
- Write logs to Amazon S3
- In [AWS X-Ray integrated
  environments](environment-configuration-debugging.md "environment-configuration-debugging.md"), upload debugging data to X-Ray
- In Amazon ECS managed Docker environments, coordinate container deployments with
  Amazon Elastic Container Service (Amazon ECS)
- In worker environments, read from an Amazon Simple Queue Service (Amazon SQS) queue
- In worker environments, perform leader election with Amazon DynamoDB
- In worker environments, publish instance health metrics to Amazon CloudWatch

## Managed policies

Elastic Beanstalk provides a set of managed policies that allow the EC2 instances in your environment
to perform required operations. The managed policies required for basic use cases are the
following.

- `AWSElasticBeanstalkWebTier`
- `AWSElasticBeanstalkWorkerTier`
- `AWSElasticBeanstalkMulticontainerDocker`

If your web application requires access to other additional AWS services, add statements
or managed policies to the instance profile that allow access to those services. For more
information, see [Adding permissions to the default instance profile](iam-instanceprofile.md#iam-instanceprofile-addperms "iam-instanceprofile.md#iam-instanceprofile-addperms").

## Creating an EC2 instance profile

If your AWS account doesn’t have an EC2 instance profile, you must create one using the IAM service. You can then assign the EC2 instance
profile to new environments that you create.
The **Create environment** steps in the Elastic Beanstalk console provides you access to the IAM console,
so that you can create an EC2 instance profile with the required permissions.

You can also create an EC2 instance profile by directly accessing the IAM console,
without going through the Elastic Beanstalk console. For detailed steps to create an Elastic Beanstalk EC2 instance
profile in the IAM console, see [Creating an instance profile](iam-instanceprofile.md#iam-instanceprofile-create "iam-instanceprofile.md#iam-instanceprofile-create").
