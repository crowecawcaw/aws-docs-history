AWS Mainframe Modernization Service (Managed Runtime Environment experience) will no longer be open to new customers starting on November 7, 2025. If you would like to use the service, please sign up prior to November 7, 2025. For capabilities similar to AWS Mainframe Modernization Service (Managed Runtime Environment experience) explore AWS Mainframe Modernization Service (Self-Managed Experience). Existing customers can continue to use the service as normal. For more information, see
[AWS Mainframe Modernization availability change](mainframe-modernization-availability-change.md "mainframe-modernization-availability-change.md").

# AWS Blu Age Runtime options

AWS Blu Age offers three types of Runtime options to cater to different stages of your
modernization journey and operational needs. This page describes each option, its
characteristics, use cases, and how to access them.

## Non-managed Runtime

With AWS Blu Age Runtime (non-managed), you can deploy your modernized application in your own AWS account
, allowing you to manage your own infrastructure. This option provides both
release and pre-release versions, giving you the flexibility to operate all the
technical components required to run your modernized application the way you want. You
can choose between stable releases for production environments or pre-release versions
for testing and development purposes.

The non-managed runtime is deployed and managed by the customer, offering more control
over the runtime environment. It provides automated refactoring capabilities and is
suitable for customized deployment scenarios.

### When to use

The non-managed runtime is suitable for testing and production environments, and
is particularly useful when specific customization of the runtime environment is
required.

### How to access

To request access to the Non-managed Runtime artifacts, see
[Onboarding AWS Blu Age Runtime](ba-runtime-setup-onboard.md "ba-runtime-setup-onboard.md").

### Deployment

AWS Blu Age Runtime (non-managed) is available for deployment on:

- Amazon EC2
- Amazon ECS on Amazon EC2
- Amazon EKS on Amazon EC2
- Amazon ECS managed by AWS Fargate

Deploying on Amazon EC2 can be done directly in the instance or through a Docker
containerized application, which is the preferred way when using Amazon ECS or
Amazon EKS.

For detailed deployment instructions, see [Set
up AWS Blu Age Runtime (non-managed)](ba-runtime-setup.md "ba-runtime-setup.md") documentation.

## Managed Runtime

With AWS Blu Age Runtime managed, you can deploy your modernized application to an AWS-managed
environment that simplifies your experience, so you don't need to manage the underlying
infrastructure that runs your modernized application.

The managed runtime features infrastructure managed by AWS, with automatic updates and
patches. It offers simplified operations and maintenance. Only release versions are
available in the managed runtime, ensuring stability and reliability for your production
environments.

### When to use

The managed runtime is ideal for production environments and is best suited for
situations where you prefer a hands-off approach to runtime management.

### How to access

To access the AWS Blu Age Runtime Managed version, you simply need access to the
following AWS services:

- Amazon S3
- AWS Mainframe Modernization

With the appropriate account permissions, you can seamlessly interact with the
managed runtime environment. This streamlined access ensures that you can leverage
the full capabilities of Blu Age Runtime while benefiting from AWS's managed
services.

### Deployment

To learn how to set up and use the Managed Runtime, see [Set up managed runtime for AWS Blu Age](tutorial-runtime-ba.md "tutorial-runtime-ba.md")
documentation.

## Developer Runtime (BluInsights toolbox)

The Developer Runtime is accessible from BluInsights Toolbox, and is designed for
development and testing phases and is frequently updated with the latest features. This
runtime includes both Release versions and Alpha pre-release versions, providing
developers with access to stable builds as well as cutting-edge features. Its primary
purpose is to support specific test or development activities in a local development
environment, typically from an IDE. Importantly, this runtime is limited to 2 hours of
use, making it suitable for focused development sessions rather than long-term or
production deployments.

### When to use

The Developer Runtime is ideal during initial development and modernization
projects, as well as for quick iterations and testing of modernized
applications.

### How to access

Access to the BluInsights Toolbox is provided as part of your AWS Blu Age project
engagement. The Developer Runtime is available through AWS Blu Age toolbox requests. Once
approved, you'll have access to specific S3 buckets:
`s3://toolbox-dev-runtime-<region>`

These buckets are available in the us-east-1 and us-east-2 regions. To use the
available bucket, append the region to the bucket name (e.g.,
`s3://toolbox-dev-runtime-us-east-1`).

For detailed instructions on how to request access and set up the necessary
permissions, see [Dev and Special
AWS Blu Age Runtimes](https://bluinsights.aws/docs/dev-special-bluage-runtime "https://bluinsights.aws/docs/dev-special-bluage-runtime") documentation.

### Deployment

To deploy the Developer Runtime:

1. List available versions using AWS CLI:

```
aws s3 ls s3://toolbox-dev-runtime
```

2. Choose a specific version and list its contents:

```
aws s3 ls s3://toolbox-dev-runtime/[version]/
```

3. Download the runtime artifact:

```
aws s3 cp s3://toolbox-dev-runtime/[version]/gapwalk-[version]-dev.tar.gz
```

4. Extract and set up the runtime according to your project
   requirements.

For more detailed deployment instructions and usage guidelines, see [Dev and Special
AWS Blu Age Runtimes](https://bluinsights.aws/docs/dev-special-bluage-runtime "https://bluinsights.aws/docs/dev-special-bluage-runtime") documentation.

###### Note

Ensure you have the necessary S3 read permissions on your AWS account to
access these buckets. An example IAM policy can be found in the [Dev and
Special AWS Blu Age Runtimes](https://bluinsights.aws/docs/dev-special-bluage-runtime "https://bluinsights.aws/docs/dev-special-bluage-runtime") documentation.
