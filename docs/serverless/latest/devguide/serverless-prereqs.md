

# Understanding prerequisites for serverless development
<a name="serverless-prereqs"></a>

Before you begin to develop a serverless application, there are some key concepts you need to understand. Review the serverless learning path in the following diagram.

Topics are shown in orange boxes. Large topics may be broken down into several sub-topics in blue. Icons represent related services or tools. Essential topics are noted with a green check box. Important, but not essential, items are noted with a red mark. When a high level orange topic is marked as essential, that means all of the sub-topics are essential too.

**Topics**
+ [Amazon Web Services account](#prereq_aws-account)
+ [Programming languages](#prereq_programming-language)
+ [Development environment](#prereq_development-environment)
+ [AWS cloud infrastructure](#prereq_aws-infrastructure)
+ [Security model](#prereq_security-model)

 ![Learning path for serverless prerequisites](http://docs.aws.amazon.com/serverless/latest/devguide/images/path-serverless-prereq.png) 

## Amazon Web Services account
<a name="prereq_aws-account"></a>

Before getting started, you must have or create an Amazon Web Services (AWS) account.

If you are creating a new account, you will create a root account using an email address. The **root** account has *unrestricted* *access*, similar to root accounts for an operating system. As a best practice, you should create an administrative user too.

**Granting administrative access to a user**  
As you might guess, granting administrative access to a user is still rather far reaching. An account with administrative level privileges will make getting started easier. For systems in production, follow the principle of least-privilege — granting only the minimum access necessary to accomplish tasks.
+ For a step-by-step guide to account types and login management, see [Signing in to the AWS Management Console](https://docs.aws.amazon.com/signin/latest/userguide/console-sign-in-tutorials.html).
+ AWS Identity and Access Management (IAM) is the service to manage entities and resources authorized to use services and service resources.

### Sign up for an AWS account
<a name="sign-up-for-aws"></a>

To get started with AWS, you need an AWS account. For information about creating an AWS account, see [Getting started with an AWS account](https://docs.aws.amazon.com/accounts/latest/reference/getting-started.html) in the *AWS Account Management Reference Guide*.

## Programming languages
<a name="prereq_programming-language"></a>

We assume that you have some experience with coding and deploying programs using one of the supported languages. This guide will *not* teach you how to program, but it will at times provide code samples.

Writing functions in an interpreted language like Python or JavaScript might be more straight-forward in some scenarios because your code can be added directly through the AWS Management Console web interface.

You can use one of the listed languages, or create your own Lambda runtime container.
+ Python, JavaScript/TypeScript — Commonly used interpreted languages
+ Java, C\#, Go — Compiled languages
+ Ruby, PowerShell — Less frequently used options

## Development environment
<a name="prereq_development-environment"></a>

For serverless development, you will likely want to set up and use a familiar editor or IDE, such as Visual Studio Code or PyCharm. Alternatively, you may prefer AWS Cloud9, a browser-based IDE and terminal "in the cloud" with direct access to your AWS account.

You should definitely install the AWS CLI for command line control and automation of services. For example, you can list your Amazon S3 buckets, update Lambda functions, or send test events to invoke service resources. Many tutorials will show how to complete tasks with the AWS CLI.

Another useful, but optional, tool is the AWS Serverless Application Model CLI, aka the "SAM CLI". AWS SAM templates define infrastructure services and code. You can use AWS SAM CLI to build and deploy from these templates to the cloud. AWS SAM CLI also provides features to test and debug locally and deploy changes to infrastructure and code.

**Tip**  
There are other tools that our customers use, such as the [AWS Cloud Development Kit (AWS CDK)](https://aws.amazon.com/cdk/) for programmatic creation of infrastructure and code, or several 3rd party IaC options.

You will find that some services provide emulators that can run on your local laptop. These tools can be useful for local development, but they are also limited in terms of service and API coverage. Serverless services are better suited to their native cloud environment.

Related resources:
+ [Install AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html) - to control and manage your AWS services from the command line
+ [Install AWS SAM CLI](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-sam-cli-install.html) - to create, deploy, test, and update your serverless code and resources from the command line
+ Note: These tools are provided by AWS Cloud9, but you should update to the latest available versions.

## AWS cloud infrastructure
<a name="prereq_aws-infrastructure"></a>

AWS provides services across the globe. You only need to understand how regions, availability zones, and data centers are related so that you can select a region. You will see the region code in URLs and Amazon Resource Names (ARNs), unique identifiers for AWS resources.

### Regions
<a name="prereq_aws-regions"></a>

Every solution you build that runs in the AWS cloud will be deployed to at least one region.
+ **Region** – a physical location around the world where we cluster data centers
+ **Availability Zone** or "AZ" - one or more discrete data centers with redundant power, networking, and connectivity *within* a Region
+ **Data center** – a physical location that contains servers, data storage drives, and network equipment

![Diagram showing US map with three regions (GovCloud, Oregon, N. California) and availability zones inside the us-west-1 region (aka N. California).](http://docs.aws.amazon.com/serverless/latest/devguide/images/regions-availability-zones.png)

Amazon has many regions all across the globe. Inside each region, there are one or more Availability Zones located tens of miles apart. The distance is near enough for low latency — the gap between requesting and receiving a response, and far enough to reduce the chance that multiple zones are affected if a disaster happens.

Each region is identified by a code, such as "us-west-1", "us-east-1" or "eu-west-2". Within each region, the multiple isolated locations known as *Availability Zones* or AZs are identified with the region code followed by a letter identifier. For example, `us-east-1a`. AWS handles deploying to multiple availability zones within a region for resilience.

### Amazon Resource Name (ARN)
<a name="prereq_aws-arn"></a>

Services are identified with regional endpoints. The general syntax of a regional endpoint is as follows:

```
protocol://<service-code>.<region-code>.amazonaws.com
```

For example, `https://dynamodb.us-west-1.amazonaws.com` is the endpoint for the Amazon DynamoDB service in the US West (N. California) Region.

The region code is also used to identify AWS resources with [Amazon Resource Names](https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html), also called "ARNs". Because AWS is deployed all over the world, ARNs function like an addressing system to precisely locate which specific part of AWS we are referring to. ARNs have a hierarchical structure:

```
arn:partition:service:region:account-id:resource-id
arn:partition:service:region:account-id:resource-type/resource-id
arn:partition:service:region:account-id:resource-type:resource-id
```
+ arn: literally, the string "arn"
+ `partition` is one of the three partitions: AWS Regions, AWS China Regions, or AWS GovCloud (US) Regions
+ `service` is the specific service such as Amazon EC2 or DynamoDB
+ `region` is the AWS region like `us-east-1` (North Virginia)
+ `account-id` is the AWS account ID
+ `resource-id` is the unique resource ID. Other forms for resource IDs like `resource-type/resource-id`, are used by services like IAM where IAM users have `resource-type` of `user` and `resource-id` a username like `MyUsername,`

Try to identify the service, region, and resource for the following example ARNs:

```
arn:aws::dynamodb:us-west-2:123456789012:table/myDynamoDBTable
arn:aws::lambda:us-east-2:123456789012:function:{{my-function:1}}
```

If you are interested in learning more, check out a [map of Regions and Availability Zones](https://aws.amazon.com/about-aws/global-infrastructure/regions_az/), a view of our [data centers](https://aws.amazon.com/compliance/data-center/data-centers/), and the complete list of [regional service endpoints](https://docs.aws.amazon.com/general/latest/gr/rande.html#ddb_region).

## Security model
<a name="prereq_security-model"></a>

Security is a top priority for AWS. Before you start building serverless solutions, you need to know how security factors into AWS solutions.

Amazon Web Services has a *shared responsibility model:*

 ![Block diagram showing elements of the shared security model. Details in the Cloud Security link.](http://docs.aws.amazon.com/serverless/latest/devguide/images/shared-responsibility-model.jpg) 

A shared security model means that Amazon manages certain aspects of security, and you are responsible for others.
+ AWS is responsible for the security *of* the cloud. This includes such thing as the physical security of the data centers.
+ You are responsible for the security *in* the cloud. For example, you are responsible for your data, and for granting functions only the access the need to complete their work.

For developers getting started with serverless and experts alike, the responsibility of securing the resources and functions will take effort to understand and implement.

We'll explain more along the way, but you should at least know that AWS commitment to security is not taken lightly. AWS services have carefully established security mechanisms for you to create secure solutions from the start. However, you have the responsibility to learn how and properly implement these mechanisms in your solutions.

For more details, see the [Shared Responsibility Model](https://aws.amazon.com/compliance/shared-responsibility-model/), [AWS Cloud Security](https://aws.amazon.com/security/), and [Security Documentation Index](https://docs.aws.amazon.com/security/?icmpid=docs_homepage_addtlrcs) with links to security documents for every service.